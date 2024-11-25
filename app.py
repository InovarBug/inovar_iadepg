from flask import Flask, request, render_template_string, jsonify
from code_generation_model import CodeGenerationModel
import os

app = Flask(__name__)
model = CodeGenerationModel()

@app.route('/', methods=['GET'])
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Inovar IADEPG - Gerador de Código</title>
            <style>
                body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; }
                h1 { color: #333; }
                form { background: #f4f4f4; padding: 20px; border-radius: 5px; }
                label { display: block; margin-bottom: 5px; }
                select, textarea { width: 100%; padding: 8px; margin-bottom: 10px; }
                input[type="submit"] { background: #333; color: #fff; padding: 10px 15px; border: none; cursor: pointer; }
                input[type="submit"]:hover { background: #555; }
                #result { margin-top: 20px; background: #e9e9e9; padding: 20px; border-radius: 5px; white-space: pre-wrap; }
            </style>
        </head>
        <body>
            <h1>Bem-vindo ao Inovar IADEPG - Gerador de Código</h1>
            <form id="codeForm">
                <label for="language">Linguagem:</label>
                <select name="language" id="language">
                    <option value="python">Python</option>
                    <option value="java">Java</option>
                    <option value="javascript">JavaScript</option>
                    <option value="kotlin">Kotlin</option>
                    <option value="xml">XML</option>
                </select>
                <label for="prompt">Prompt:</label>
                <textarea name="prompt" id="prompt" rows="4" required></textarea>
                <input type="submit" value="Gerar Código">
            </form>
            <div id="result"></div>
            <script>
                document.getElementById('codeForm').addEventListener('submit', function(e) {
                    e.preventDefault();
                    var formData = new FormData(this);
                    fetch('/generate', {
                        method: 'POST',
                        body: formData
                    })
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('result').textContent = data.generated_code;
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        document.getElementById('result').textContent = 'Erro ao gerar código. Por favor, tente novamente.';
                    });
                });
            </script>
        </body>
        </html>
    ''')

@app.route('/generate', methods=['POST'])
def generate_code():
    language = request.form.get('language', 'python')
    prompt = request.form.get('prompt', '')
    
    generated_code = model.generate_code(language, prompt)
    
    return jsonify({'generated_code': generated_code})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

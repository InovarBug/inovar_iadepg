
from flask import Flask, request, jsonify, render_template_string
from code_generation_model import CodeGenerationModel

app = Flask(__name__)
model = CodeGenerationModel()

@app.route('/', methods=['GET'])
def home():
    return render_template_string('''
        <h1>Bem-vindo ao Inovar IADEPG API</h1>
        <p>Use o endpoint /generate para gerar código.</p>
        <form action="/generate" method="post">
            <label for="language">Linguagem:</label>
            <select name="language" id="language">
                <option value="python">Python</option>
                <option value="java">Java</option>
                <option value="javascript">JavaScript</option>
                <option value="kotlin">Kotlin</option>
                <option value="xml">XML</option>
            </select><br><br>
            <label for="prompt">Prompt:</label><br>
            <textarea name="prompt" id="prompt" rows="4" cols="50"></textarea><br><br>
            <input type="submit" value="Gerar Código">
        </form>
    ''')

@app.route('/generate', methods=['POST'])
def generate_code():
    language = request.form.get('language', 'python')
    prompt = request.form.get('prompt', '')
    
    generated_code = model.generate_code(language, prompt)
    
    return render_template_string('''
        <h2>Código Gerado:</h2>
        <pre>{{ code }}</pre>
        <a href="/">Voltar</a>
    ''', code=generated_code)

if __name__ == '__main__':
    app.run(debug=True)

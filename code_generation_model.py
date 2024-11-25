from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class CodeGenerationModel:
    def __init__(self):
        self.models = {
            'python': ('huggingface/CodeBERTa-small-v1', AutoModelForCausalLM),
            'java': ('microsoft/codebert-base', AutoModelForCausalLM),
            'javascript': ('microsoft/codebert-base-mlm', AutoModelForCausalLM),
            'kotlin': ('microsoft/codebert-base', AutoModelForCausalLM),  # Using CodeBERT for Kotlin as well
        }
        self.tokenizers = {}
        self.loaded_models = {}

    def load_model(self, language):
        if language not in self.models:
            raise ValueError(f"Unsupported language: {language}")
        
        if language not in self.loaded_models:
            model_name, model_class = self.models[language]
            self.tokenizers[language] = AutoTokenizer.from_pretrained(model_name)
            self.loaded_models[language] = model_class.from_pretrained(model_name)

    def generate_code(self, prompt, language, max_length=100):
        self.load_model(language)
        
        input_ids = self.tokenizers[language].encode(prompt, return_tensors="pt")
        output = self.loaded_models[language].generate(input_ids, max_length=max_length, num_return_sequences=1)
        generated_code = self.tokenizers[language].decode(output[0], skip_special_tokens=True)
        return generated_code

    def generate_android_component(self, component_type):
        if component_type not in ['activity', 'fragment', 'service', 'broadcast_receiver']:
            raise ValueError(f"Unsupported Android component type: {component_type}")

        prompts = {
            'activity': "class MainActivity : AppCompatActivity() {",
            'fragment': "class MainFragment : Fragment() {",
            'service': "class MyService : Service() {",
            'broadcast_receiver': "class MyReceiver : BroadcastReceiver() {"
        }

        return self.generate_code(prompts[component_type], 'kotlin')

if __name__ == "__main__":
    model = CodeGenerationModel()
    
    # Test Python
    python_prompt = "def fibonacci(n):"
    python_code = model.generate_code(python_prompt, 'python')
    print(f"Generated Python code:\n{python_code}\n")
    
    # Test Java
    java_prompt = "public static int fibonacci(int n) {"
    java_code = model.generate_code(java_prompt, 'java')
    print(f"Generated Java code:\n{java_code}\n")
    
    # Test JavaScript
    js_prompt = "function fibonacci(n) {"
    js_code = model.generate_code(js_prompt, 'javascript')
    print(f"Generated JavaScript code:\n{js_code}\n")

    # Test Kotlin and Android components
    kotlin_prompt = "fun fibonacci(n: Int): Int {"
    kotlin_code = model.generate_code(kotlin_prompt, 'kotlin')
    print(f"Generated Kotlin code:\n{kotlin_code}\n")

    # Generate Android Activity
    android_activity = model.generate_android_component('activity')
    print(f"Generated Android Activity:\n{android_activity}\n")


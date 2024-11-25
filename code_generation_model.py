from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class CodeGenerationModel:
    def __init__(self):
        self.models = {
            'python': ('huggingface/CodeBERTa-small-v1', AutoModelForCausalLM),
            'java': ('microsoft/codebert-base', AutoModelForCausalLM),
            'javascript': ('microsoft/codebert-base-mlm', AutoModelForCausalLM),
            'kotlin': ('microsoft/codebert-base', AutoModelForCausalLM),
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

    def generate_code(self, prompt, language, max_length=200):
        self.load_model(language)
        
        input_ids = self.tokenizers[language].encode(prompt, return_tensors="pt")
        output = self.loaded_models[language].generate(input_ids, max_length=max_length, num_return_sequences=1, temperature=0.7)
        generated_code = self.tokenizers[language].decode(output[0], skip_special_tokens=True)
        return generated_code

    def generate_android_component(self, component_type):
        if component_type not in ['activity', 'fragment', 'service', 'broadcast_receiver']:
            raise ValueError(f"Unsupported Android component type: {component_type}")

        prompts = {
            'activity': """
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        // TODO: Initialize UI components and set up event listeners
    }
    
    // TODO: Implement other lifecycle methods as needed
}
""",
            'fragment': """
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment

class MainFragment : Fragment() {
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View? {
        return inflater.inflate(R.layout.fragment_main, container, false)
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        
        // TODO: Initialize UI components and set up event listeners
    }
    
    // TODO: Implement other lifecycle methods as needed
}
""",
            'service': """
import android.app.Service
import android.content.Intent
import android.os.IBinder

class MyService : Service() {
    override fun onBind(intent: Intent): IBinder? {
        return null
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        // TODO: Implement service logic
        return START_STICKY
    }
    
    // TODO: Implement other lifecycle methods as needed
}
""",
            'broadcast_receiver': """
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent

class MyReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        // TODO: Handle the received broadcast
    }
}
"""
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


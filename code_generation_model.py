from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class CodeGenerationModel:
    def __init__(self):
        self.models = {
            'python': ('huggingface/CodeBERTa-small-v1', AutoModelForCausalLM),
            'java': ('microsoft/codebert-base', AutoModelForCausalLM),
            'javascript': ('microsoft/codebert-base-mlm', AutoModelForCausalLM),
            'kotlin': ('microsoft/codebert-base', AutoModelForCausalLM),
            'xml': ('microsoft/codebert-base', AutoModelForCausalLM),  # Using CodeBERT for XML as well
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

    def generate_code(self, language, prompt, max_length=200):
        try:
            self.load_model(language)
            
            input_ids = self.tokenizers[language].encode(prompt, return_tensors="pt")
            output = self.loaded_models[language].generate(input_ids, max_length=max_length, num_return_sequences=1, temperature=0.7)
            generated_code = self.tokenizers[language].decode(output[0], skip_special_tokens=True)
            return generated_code
        except Exception as e:
            return f"Error generating code: {str(e)}"

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

    def generate_android_layout(self, layout_type):
        if layout_type not in ['activity', 'fragment', 'list_item']:
            raise ValueError(f"Unsupported Android layout type: {layout_type}")

        prompts = {
            'activity': """
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout 
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <!-- TODO: Add your UI components here -->

</androidx.constraintlayout.widget.ConstraintLayout>
""",
            'fragment': """
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout 
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainFragment">

    <!-- TODO: Add your UI components here -->

</androidx.constraintlayout.widget.ConstraintLayout>
""",
            'list_item': """
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout 
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:padding="16dp">

    <!-- TODO: Add your list item components here -->

</androidx.constraintlayout.widget.ConstraintLayout>
"""
        }

        return self.generate_code(prompts[layout_type], 'xml')

if __name__ == "__main__":
    model = CodeGenerationModel()
    
    # Test Android layout generation
    activity_layout = model.generate_android_layout('activity')
    print(f"Generated Android Activity Layout:\n{activity_layout}\n")

    fragment_layout = model.generate_android_layout('fragment')
    print(f"Generated Android Fragment Layout:\n{fragment_layout}\n")

    list_item_layout = model.generate_android_layout('list_item')
    print(f"Generated Android List Item Layout:\n{list_item_layout}\n")


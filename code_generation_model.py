
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class CodeGenerationModel:
    def __init__(self, model_name="microsoft/codebert-base"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_code(self, prompt, max_length=100):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(input_ids, max_length=max_length, num_return_sequences=1)
        generated_code = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_code

if __name__ == "__main__":
    model = CodeGenerationModel()
    prompt = "def fibonacci(n):"
    generated_code = model.generate_code(prompt)
    print(f"Generated code:\n{generated_code}")

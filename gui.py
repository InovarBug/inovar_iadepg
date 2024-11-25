import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
from code_generation_model import CodeGenerationModel
import xml.etree.ElementTree as ET
import threading
import time

class CodeGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Inovar IADEPG - Code Generator")
        self.model = CodeGenerationModel()
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        # ... (previous widget creation code remains the same)

        # Progress bar
        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.grid(row=8, column=0, columnspan=2, pady=10, padx=5, sticky="we")

        # Status label
        self.status_label = ttk.Label(self.master, text="Ready")
        self.status_label.grid(row=9, column=0, columnspan=2, pady=5)

    def generate_code(self):
        language = self.language_var.get()
        component = self.component_var.get()
        prompt = self.prompt_entry.get()
        temperature = self.temperature_var.get()
        max_length = self.max_length_var.get()

        self.generate_button["state"] = "disabled"
        self.progress_bar["value"] = 0
        self.status_label["text"] = "Generating code..."

        def generate():
            try:
                if language in ["kotlin", "xml"] and component:
                    if language == "kotlin":
                        generated_code = self.model.generate_android_component(component, temperature=temperature, max_length=max_length)
                    else:  # XML
                        generated_code = self.model.generate_android_layout(component, temperature=temperature, max_length=max_length)
                    self.preview_button["state"] = "normal"  # Enable preview button for XML
                else:
                    generated_code = self.model.generate_code(prompt, language, temperature=temperature, max_length=max_length)
                    self.preview_button["state"] = "disabled"  # Disable preview button for non-XML

                self.output_area.delete(1.0, tk.END)
                self.output_area.insert(tk.END, generated_code)
                
                # Add to history
                self.history.append({
                    'language': language,
                    'component': component,
                    'prompt': prompt,
                    'code': generated_code,
                    'temperature': temperature,
                    'max_length': max_length
                })

                self.status_label["text"] = "Code generation complete"
            except Exception as e:
                self.output_area.delete(1.0, tk.END)
                self.output_area.insert(tk.END, f"Error: {str(e)}")
                self.status_label["text"] = "Error in code generation"
            finally:
                self.generate_button["state"] = "normal"

        def update_progress():
            for i in range(100):
                time.sleep(0.05)  # Simulate work being done
                self.progress_bar["value"] = i + 1
                self.master.update_idletasks()

        threading.Thread(target=generate).start()
        threading.Thread(target=update_progress).start()

    # ... (other methods remain the same)

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeGeneratorGUI(root)
    root.mainloop()

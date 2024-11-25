import tkinter as tk
from tkinter import ttk, scrolledtext
from code_generation_model import CodeGenerationModel

class CodeGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Inovar IADEPG - Code Generator")
        self.model = CodeGenerationModel()

        self.create_widgets()

    def create_widgets(self):
        # Language selection
        ttk.Label(self.master, text="Select Language:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.language_var = tk.StringVar()
        self.language_combo = ttk.Combobox(self.master, textvariable=self.language_var, 
                                           values=["python", "java", "javascript", "kotlin", "xml"])
        self.language_combo.grid(row=0, column=1, sticky="we", padx=5, pady=5)
        self.language_combo.set("python")

        # Android component selection (for Kotlin and XML)
        ttk.Label(self.master, text="Android Component:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.component_var = tk.StringVar()
        self.component_combo = ttk.Combobox(self.master, textvariable=self.component_var, 
                                            values=["activity", "fragment", "service", "broadcast_receiver", "layout"])
        self.component_combo.grid(row=1, column=1, sticky="we", padx=5, pady=5)

        # Prompt input
        ttk.Label(self.master, text="Enter Prompt:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.prompt_entry = ttk.Entry(self.master, width=50)
        self.prompt_entry.grid(row=2, column=1, sticky="we", padx=5, pady=5)

        # Generate button
        self.generate_button = ttk.Button(self.master, text="Generate Code", command=self.generate_code)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Output area
        self.output_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=60, height=20)
        self.output_area.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def generate_code(self):
        language = self.language_var.get()
        component = self.component_var.get()
        prompt = self.prompt_entry.get()

        try:
            if language in ["kotlin", "xml"] and component:
                if language == "kotlin":
                    generated_code = self.model.generate_android_component(component)
                else:  # XML
                    generated_code = self.model.generate_android_layout(component)
            else:
                generated_code = self.model.generate_code(prompt, language)

            self.output_area.delete(1.0, tk.END)
            self.output_area.insert(tk.END, generated_code)
        except Exception as e:
            self.output_area.delete(1.0, tk.END)
            self.output_area.insert(tk.END, f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeGeneratorGUI(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
from code_generation_model import CodeGenerationModel

class CodeGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Inovar IADEPG - Code Generator")
        self.model = CodeGenerationModel()
        self.history = []

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

        # Generation parameters
        ttk.Label(self.master, text="Temperature:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.temperature_var = tk.DoubleVar(value=0.7)
        self.temperature_entry = ttk.Entry(self.master, textvariable=self.temperature_var, width=10)
        self.temperature_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(self.master, text="Max Length:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.max_length_var = tk.IntVar(value=200)
        self.max_length_entry = ttk.Entry(self.master, textvariable=self.max_length_var, width=10)
        self.max_length_entry.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        # Generate button
        self.generate_button = ttk.Button(self.master, text="Generate Code", command=self.generate_code)
        self.generate_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Output area
        self.output_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=60, height=20)
        self.output_area.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        # Save button
        self.save_button = ttk.Button(self.master, text="Save Code", command=self.save_code)
        self.save_button.grid(row=7, column=0, pady=10)

        # History button
        self.history_button = ttk.Button(self.master, text="Show History", command=self.show_history)
        self.history_button.grid(row=7, column=1, pady=10)

    def generate_code(self):
        language = self.language_var.get()
        component = self.component_var.get()
        prompt = self.prompt_entry.get()
        temperature = self.temperature_var.get()
        max_length = self.max_length_var.get()

        try:
            if language in ["kotlin", "xml"] and component:
                if language == "kotlin":
                    generated_code = self.model.generate_android_component(component, temperature=temperature, max_length=max_length)
                else:  # XML
                    generated_code = self.model.generate_android_layout(component, temperature=temperature, max_length=max_length)
            else:
                generated_code = self.model.generate_code(prompt, language, temperature=temperature, max_length=max_length)

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
        except Exception as e:
            self.output_area.delete(1.0, tk.END)
            self.output_area.insert(tk.END, f"Error: {str(e)}")

    def save_code(self):
        generated_code = self.output_area.get(1.0, tk.END).strip()
        if not generated_code:
            messagebox.showwarning("Empty Code", "No code to save. Please generate code first.")
            return

        file_types = [('Python Files', '*.py'), ('Java Files', '*.java'), ('JavaScript Files', '*.js'),
                      ('Kotlin Files', '*.kt'), ('XML Files', '*.xml'), ('All Files', '*.*')]
        file_path = filedialog.asksaveasfilename(filetypes=file_types, defaultextension=".txt")
        
        if file_path:
            with open(file_path, 'w') as file:
                file.write(generated_code)
            messagebox.showinfo("Save Successful", f"Code saved to {file_path}")

    def show_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("Code Generation History")

        for i, item in enumerate(reversed(self.history)):
            frame = ttk.Frame(history_window, padding="10")
            frame.pack(fill=tk.X, expand=True)

            ttk.Label(frame, text=f"Language: {item['language']}").pack(anchor="w")
            if item['component']:
                ttk.Label(frame, text=f"Component: {item['component']}").pack(anchor="w")
            if item['prompt']:
                ttk.Label(frame, text=f"Prompt: {item['prompt']}").pack(anchor="w")
            ttk.Label(frame, text=f"Temperature: {item['temperature']}").pack(anchor="w")
            ttk.Label(frame, text=f"Max Length: {item['max_length']}").pack(anchor="w")
            
            code_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=10)
            code_area.pack(fill=tk.X, expand=True)
            code_area.insert(tk.END, item['code'])
            code_area.config(state=tk.DISABLED)

            ttk.Button(frame, text="Use This Code", command=lambda code=item['code']: self.use_history_code(code)).pack(pady=5)

            if i < len(self.history) - 1:
                ttk.Separator(history_window, orient='horizontal').pack(fill='x', padx=10, pady=10)

    def use_history_code(self, code):
        self.output_area.delete(1.0, tk.END)
        self.output_area.insert(tk.END, code)

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeGeneratorGUI(root)
    root.mainloop()

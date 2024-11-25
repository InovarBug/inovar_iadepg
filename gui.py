import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
from code_generation_model import CodeGenerationModel
import xml.etree.ElementTree as ET

class CodeGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Inovar IADEPG - Code Generator")
        self.model = CodeGenerationModel()
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        # ... (previous widget creation code remains the same)

        # Preview button (initially disabled)
        self.preview_button = ttk.Button(self.master, text="Preview XML", command=self.preview_xml, state="disabled")
        self.preview_button.grid(row=7, column=1, pady=10)

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
        except Exception as e:
            self.output_area.delete(1.0, tk.END)
            self.output_area.insert(tk.END, f"Error: {str(e)}")

    def preview_xml(self):
        xml_code = self.output_area.get(1.0, tk.END).strip()
        if not xml_code:
            messagebox.showwarning("Empty XML", "No XML to preview. Please generate XML first.")
            return

        preview_window = tk.Toplevel(self.master)
        preview_window.title("XML Preview")

        tree_view = ttk.Treeview(preview_window)
        tree_view.pack(fill=tk.BOTH, expand=True)

        try:
            root = ET.fromstring(xml_code)
            self.populate_tree(tree_view, "", root)
        except ET.ParseError:
            messagebox.showerror("XML Parse Error", "Unable to parse the XML. Please check if it's valid.")

    def populate_tree(self, tree, parent, element):
        tree_item = tree.insert(parent, 'end', text=element.tag, open=True)
        for attr, value in element.attrib.items():
            tree.insert(tree_item, 'end', text=f"{attr}: {value}")
        for child in element:
            self.populate_tree(tree, tree_item, child)

    # ... (other methods remain the same)

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeGeneratorGUI(root)
    root.mainloop()

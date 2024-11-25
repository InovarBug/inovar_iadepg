import argparse
from code_generation_model import CodeGenerationModel

def main():
    parser = argparse.ArgumentParser(description="Generate code using AI")
    parser.add_argument("--language", choices=["python", "java", "javascript", "kotlin"], required=True, help="Programming language")
    parser.add_argument("--prompt", required=True, help="Code prompt")
    parser.add_argument("--android", choices=["activity", "fragment", "service", "broadcast_receiver"], help="Generate Android component")

    args = parser.parse_args()

    model = CodeGenerationModel()

    if args.android:
        generated_code = model.generate_android_component(args.android)
        print(f"Generated Android {args.android.capitalize()}:\n{generated_code}")
    else:
        generated_code = model.generate_code(args.prompt, args.language)
        print(f"Generated {args.language.capitalize()} code:\n{generated_code}")

if __name__ == "__main__":
    main()

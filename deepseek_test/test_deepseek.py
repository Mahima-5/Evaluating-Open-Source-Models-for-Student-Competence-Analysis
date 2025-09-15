from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import re
import time
import student_code  


class PythonEducator:
    def __init__(self, model_path=r"C:\models\deepseek-coder-1.3b-base"):
        print("Loading tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        print("Loading model (this may take a while)...")
        start_time = time.time()

        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            trust_remote_code=True,
            dtype=torch.float32,  # Use dtype instead of torch_dtype
            low_cpu_mem_usage=True
        )

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {self.device}")
        self.model.to(self.device)
        self.model.eval()

        load_time = time.time() - start_time
        print(f"Model loaded in {load_time:.2f} seconds")

    def analyze_student_code(self, code_snippet, concept):
        prompt = f"""Analyze this Python code about {concept}:

{code_snippet}

Provide feedback in this exact format:

ERRORS:
- [list errors here, one per line starting with -]

QUESTIONS:
- [question 1]
- [question 2] 
- [question 3]

HINT:
[your hint here]

BEGIN RESPONSE:
ERRORS:
"""
        print("Generating analysis...")
        start_time = time.time()

        with torch.no_grad():
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=400,
                temperature=0.3,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id,
                repetition_penalty=1.1,
                num_return_sequences=1
            )
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        gen_time = time.time() - start_time
        print(f"Analysis generated in {gen_time:.2f} seconds")
        
        # Extract the response after the prompt
        response = response[len(prompt):].strip()
        print(f"Raw response:\n{response}\n")  # Show full response for debugging
        
        return self._parse_response(response)

    def _parse_response(self, response):
        result = {"errors": [], "questions": [], "hint": ""}
        
        # More flexible parsing that handles different formats
        lines = response.split('\n')
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            # Detect section headers
            if line.upper().startswith('ERRORS:'):
                current_section = 'errors'
                line = line[7:].strip()  # Remove "ERRORS:" prefix
            elif line.upper().startswith('QUESTIONS:'):
                current_section = 'questions'
                line = line[10:].strip()  # Remove "QUESTIONS:" prefix
            elif line.upper().startswith('HINT:'):
                current_section = 'hint'
                line = line[5:].strip()  # Remove "HINT:" prefix
                result['hint'] = line
                continue
            
            # Process content based on current section
            if current_section == 'errors' and line:
                if line.startswith('-'):
                    result['errors'].append(line[1:].strip())
                elif line:  # Handle lines without dashes
                    result['errors'].append(line)
            
            elif current_section == 'questions' and line:
                if line.startswith('-'):
                    result['questions'].append(line[1:].strip())
                elif line and not line.upper().startswith('HINT:'):  # Handle lines without dashes
                    # Remove numbering like "1.", "2." etc.
                    clean_line = re.sub(r'^\d+[\.\)]\s*', '', line)
                    result['questions'].append(clean_line)
            
            elif current_section == 'hint' and line and not line.upper().startswith(('ERRORS:', 'QUESTIONS:')):
                # Append to hint if we're in hint section and it's not a new section header
                if result['hint']:
                    result['hint'] += ' ' + line
                else:
                    result['hint'] = line
        
        return result


# ---------------- MAIN EXECUTION ----------------
if __name__ == "__main__":
    educator = PythonEducator()

    # Analyze just one example from student_code.py
    print("\n=== Analyzing student_code_1 ===")
    analysis = educator.analyze_student_code(student_code.student_code_1, "function definition and loops")
    print("\n=== ANALYSIS RESULTS ===")
    print("Errors:", analysis["errors"])
    print("Questions:", analysis["questions"])
    print("Hint:", analysis["hint"])
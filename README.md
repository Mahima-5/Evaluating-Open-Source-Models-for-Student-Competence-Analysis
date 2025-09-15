# Evaluating-Open-Source-Models-for-Student-Competence-Analysis

Research Plan
Approach to Model Identification and Evaluation
Our approach to identifying and evaluating relevant AI models for educational assessment begins with a comprehensive survey of open-source models specifically designed for code understanding and generation. We prioritize models that demonstrate strong performance on programming tasks while remaining computationally accessible for educational institutions. The evaluation criteria focus on several key dimensions: code comprehension accuracy (ability to correctly analyze Python syntax and semantics), pedagogical appropriateness (capacity to generate educationally useful feedback), misconception identification (skill at detecting common student errors), and resource requirements (computational cost and accessibility). We specifically examine the DeepSeek Coder 1.3B model as our primary candidate due to its balance between capability and practicality, testing it against a curated dataset of student code examples with varying complexity levels and common error patterns.

To validate model applicability, we implement a structured testing framework that assesses both quantitative metrics (response relevance, error detection rate) and qualitative factors (educational value of generated prompts, appropriateness of hints). This involves creating benchmark tasks where the model analyzes student code, generates assessment questions, and provides constructive feedback. Validation occurs through both automated evaluation (measuring response quality against predetermined rubrics) and human assessment (having experienced Python educators rate the model's outputs for pedagogical effectiveness). The reasoning behind this approach is that effective competence assessment requires not just technical accuracy but also educational sensitivity, which necessitates a hybrid evaluation methodology combining computational metrics with human judgment.

Testing Methodology and Decision Process
Our testing methodology employs a multi-layered approach to assess model performance. First, we create a diverse dataset of student Python code samples representing common learning stages and misconception patterns. We then develop specific prompt templates that guide the model to analyze code, identify potential misunderstandings, generate probing questions, and offer constructive hints. Each model response is evaluated against criteria including: conceptual relevance to the programming concept being assessed, ability to uncover reasoning processes rather than just syntax errors, appropriateness for the student's apparent skill level, and effectiveness at encouraging deeper thinking without providing direct solutions. We particularly focus on whether the model can distinguish between syntactic errors and conceptual misunderstandings, which is crucial for high-level competence analysis.

The decision to focus on DeepSeek Coder 1.3B stems from its optimal balance between several competing factors: it is large enough to understand code semantics but small enough to be deployable in resource-constrained educational environments; it specializes in code rather than general language, making it more suitable for programming education; and it provides open weights that allow for customization and experimentation. Our reasoning acknowledges that while larger models might offer marginally better performance, their computational requirements and closed nature make them less practical for widespread educational use. We consciously accept the trade-off of slightly reduced accuracy for substantially improved accessibility and customizability, which aligns better with real-world educational constraints.

Reasoning and Model Evaluation
What makes a model suitable for high-level competence analysis?
A model suitable for high-level competence analysis must possess several key characteristics: First, it needs deep understanding of the subject matter domain (Python programming concepts, in this case) rather than surface-level pattern recognition. Second, it must be able to reason about intent and conceptual understanding, not just identify syntax errors. Third, it should have pedagogical awareness—the ability to generate responses that guide learning without simply providing answers. Fourth, it needs to contextualize errors within a learning progression, recognizing which concepts are foundational and which are more advanced. Finally, it must balance specificity with generality, providing targeted feedback while recognizing multiple valid approaches to problems.

How would you test whether a model generates meaningful prompts?
We would test prompt meaningfulness through a multi-method approach: (1) Automated evaluation using metrics like relevance scoring (comparing generated prompts to concept maps of Python knowledge), (2) Expert review by Python educators rating prompts on criteria like conceptual focus, appropriateness for level, and ability to provoke deeper thinking, (3) Student testing where learners interact with the prompts and we measure resulting learning gains or conceptual clarification, and (4) Comparison against validated assessment items from educational resources to ensure alignment with established pedagogical practices. Meaningful prompts should target specific conceptual understandings, be open-ended enough to allow for multiple reasoning paths, and avoid leading students toward particular solutions.

What trade-offs might exist between accuracy, interpretability, and cost?
Significant trade-offs exist between these dimensions: Larger models generally offer higher accuracy but at substantially increased computational cost and decreased interpretability (black-box nature). Smaller models like DeepSeek Coder 1.3B are more computationally efficient and somewhat more interpretable but may sacrifice some accuracy on complex reasoning tasks. Cost considerations include not just computational resources but also implementation time, maintenance requirements, and customization effort. In educational contexts, we often prioritize interpretability and cost over maximal accuracy, since educators need to understand and trust the assessment process, and schools typically have limited computational resources.

Why did you choose the model you evaluated, and what are its strengths or limitations?
We selected DeepSeek Coder 1.3B for several reasons: It provides a practical balance between capability and accessibility, specializing in code understanding (unlike general-purpose LLMs), offering open weights for customization, and maintaining a manageable computational footprint. Its strengths include: Python-specific optimization, reasonable performance on code analysis tasks, relatively low resource requirements, and open accessibility for educational use. Limitations include: Occasional missing of subtle conceptual errors, limited context window for longer code samples, potential for generating incorrect or irrelevant responses, and the need for careful prompt engineering to maximize educational value. Despite these limitations, it represents a viable option for educational settings where larger models would be impractical.

Setup and Installation
bash
# Clone the repository
git clone https://github.com/your-username/python-competence-assessor.git
cd python-competence-assessor

# Install dependencies
pip install torch transformers

# Run the assessment tool
python educator.py
Usage Example
The repository includes sample student code in student_code.py that demonstrates common Python learning challenges. The main implementation in educator.py provides three key functions:

analyze_student_code() - analyzes code and provides educational feedback

generate_assessment_questions() - creates concept-specific questions

evaluate_code_completion() - tests ability to complete partial code

Example usage:

python
from educator import PythonEducator

educator = PythonEducator()
analysis = educator.analyze_student_code(student_code, "loops")
print("Educational assessment:", analysis)
Project Structure
text
python-competence-assessor/
├── test_deepseek.py              # Main implementation
├── student_code.py          # Sample student code examples
└── README.md               # This file

This project demonstrates how open-source AI models can be adapted for educational assessment while acknowledging both their potential and limitations in real-world learning contexts.

# Evaluating Open-Source Models for Student Competence Analysis

## Project Overview

This project explores the potential of **open-source AI models** to analyze Python code written by students and provide meaningful feedback that assesses their conceptual understanding. The goal is to determine whether these models can:

- Analyze student-written Python code for **logical and syntactic errors**.  
- Generate **prompts that encourage conceptual understanding**.  
- Identify **gaps in reasoning or misconceptions**.  
- Encourage **deeper learning** without simply providing the solution.  

For this project, **Python learning** is used as a test case. The system uses an open-source model, **[DeepSeek Coder 1.3B Base]([https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-base])**, to analyze small Python functions and provide feedback including:

- **Errors:** Points out potential issues or misconceptions in the student code.  
- **Questions:** Prompts conceptual understanding without giving away solutions.  
- **Hints:** Offers guidance to help students correct their code or understand concepts.  

This project demonstrates how AI models can be adapted for **educational assessment** while acknowledging both their potential and limitations in real-world learning contexts.

---

## Research Plan

### Approach and Evaluation

To evaluate AI models for assessing Python student code, I focused on freely available **open-source models** capable of understanding programming logic, particularly **DeepSeek Coder 1.3B Base**. The evaluation approach included multiple steps:

1. **Model Selection:** Identifying models that can analyze code, generate prompts, and be deployed locally to avoid API costs.  
2. **Prompt Design:** Creating structured prompts instructing the model to provide three sections: **errors**, **conceptual questions**, and **hints**, with explicit instructions to guide reasoning rather than provide full solutions.  
3. **Testing & Validation:** Feeding representative Python snippets, such as functions using loops, accumulators, and basic arithmetic, and analyzing both **raw model output** and **parsed structured output** to assess correctness, clarity, and educational relevance.  
4. **Iterative Refinement:** Adjusting prompt wording and parsing logic to handle inconsistent formatting, multi-line hints/questions, and cases where headers like `ERRORS:` might be missing.  

The evaluation criteria included the model’s ability to identify logical or syntactic errors, generate meaningful conceptual questions that promote reasoning, and provide hints that encourage problem-solving without giving away direct solutions.

---

### Reasoning, Suitability, and Observations

A model is considered suitable for **high-level competence analysis** if it can interpret Python code correctly, detect gaps in reasoning, and produce outputs that support conceptual learning. **DeepSeek Coder** was chosen because it demonstrates several key strengths:

- Understanding Python **loops, variables, and function logic**.  
- Generating **actionable conceptual questions**.  
- Providing **hints** that help students reason through problems.  

Observations from testing show that the model can:

- Identify missing logic, such as the omission of division for averages.  
- Pose meaningful questions about loops and accumulators.  
- Give practical guidance without revealing answers directly.  

**Trade-offs include:** occasional hallucinated errors (e.g., misidentifying correct variables), output inconsistencies requiring robust parsing, and slower CPU inference (~50–150 seconds per snippet).  

To validate applicability, outputs were **manually inspected** and structured using parsing code, ensuring **errors**, **questions**, and **hints** were captured reliably. Overall, the model demonstrates strong potential for **educational assessment**, balancing **code understanding**, **conceptual prompting**, and **guided learning**, while highlighting the importance of **prompt design, parsing robustness, and careful evaluation** to maximize accuracy and interpretability.

---

## Setup Instructions

1. **Clone the repository**

        git clone https://github.com/Mahima-5/Evaluating-Open-Source-Models-for-Student-Competence-Analysis.git
        cd deepseek_test

2. **Set up a virtual environment**

        python -m venv .venv
        .venv\Scripts\activate   # Windows
        ### OR
        source .venv/bin/activate  # Linux/Mac


3. **Install dependencies**

        pip install torch transformers


    - Download or specify the model path
    
    - Place DeepSeek Coder 1.3B Base in C:\models\ or any local path.
    
    - Download DeepSeek model from Hugging Face
    
    - Update model_path in test_deepseek.py if needed.

4. **Run analysis**

        python test_deepseek.py

## References

DeepSeek Coder 1.3B Base on Hugging Face[https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-base]

DeepSeek GitHub Repository[https://github.com/deepseek-ai/deepseek-coder]

## Conclusion

This project demonstrates that open-source LLMs like DeepSeek Coder can be adapted to assess Python code conceptually, providing meaningful feedback through errors, questions, and hints. While limitations exist—such as occasional hallucinated errors, inconsistent output formatting, and slower CPU inference—the model is promising for educational applications. With robust prompt design, parsing strategies, and careful evaluation, such AI models can support conceptual learning, identify reasoning gaps, and enhance student engagement in programming education.

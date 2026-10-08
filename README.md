# Prompt-Engineering

# PROMPTXPERT AI

## Transform Simple Ideas into Powerful AI Prompts

PromptXpert AI is a Prompt Engineering application that helps users experiment with different prompting techniques and generate AI-powered responses.

The application allows users to select a prompting technique, enter a question or task, adjust response creativity and response length, and generate an AI response.

## Features

- Simple and user-friendly interface
- Multiple Prompt Engineering techniques
- Zero-Shot Prompting
- One-Shot Prompting
- Few-Shot Prompting
- Chain of Thought
- Manual Chain of Thought
- Tree of Thoughts
- Multi-Step Chain of Thought (MCOT)
- Response creativity control
- Response length control
- AI-powered response generation
- Generated prompt preview
- Streamlit-based web interface

## Prompting Techniques

### Zero-Shot Prompting

Generates a response without providing examples to the AI model.

### One-Shot Prompting

Provides one example to guide the AI model before processing the user's question.

### Few-Shot Prompting

Provides multiple examples to help the AI understand the expected response pattern.

### Chain of Thought

Uses a structured problem-solving approach to produce a clear explanation and final answer.

### Manual CoT

Uses predefined reasoning steps to organize the problem-solving process.

### Tree of Thoughts

Considers multiple possible approaches and selects a suitable solution.

### MCOT

Uses a multi-step structure including problem understanding, strategy, solution, verification, and final answer.

## Technologies Used

- Python
- Streamlit
- Hugging Face
- Hugging Face Inference API
- python-dotenv

## Project Structure

```text
Prompt engineering/
│
├── app.py
├── llm.py
├── prompt_template.py
├── requirements.txt
├── .env
└── .gitignore



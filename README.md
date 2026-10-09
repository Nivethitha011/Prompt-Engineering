# PROMPTXPERT AI

A Streamlit-based Prompt Engineering application that demonstrates different prompting techniques using a Large Language Model (LLM).

The application allows users to enter a task or question, select a prompting technique, adjust response settings, generate the corresponding prompt, and receive an AI-generated response.

##Project Images
<img width="701" height="445" alt="image" src="https://github.com/user-attachments/assets/e9b4e2df-1979-48ca-af59-fdd97ad88bb1" />
<img width="758" height="441" alt="image" src="https://github.com/user-attachments/assets/14a7f17b-1235-4bdc-8118-b5c55d9cfa76" />
<img width="851" height="427" alt="image" src="https://github.com/user-attachments/assets/d033037b-4f1d-4143-9e7f-79b30d2a83af" />
<img width="862" height="445" alt="image" src="https://github.com/user-attachments/assets/1a39e41f-4b59-45ed-a919-b12c1d217b6a" />





## Project Overview

This project demonstrates how different Prompt Engineering techniques can influence the way an LLM understands instructions and generates responses.

The application supports:

- Zero-shot Prompting
- One-shot Prompting
- Few-shot Prompting
- Chain of Thought (CoT)
- Manual Chain of Thought
- Tree of Thoughts (ToT)
- Multi-Step Chain of Thought (MCOT)

The application uses Hugging Face for AI-powered response generation and Streamlit for the user interface.

## Features

### 1. Zero-shot Prompting

The model receives a task without any examples and generates a response directly.

### 2. One-shot Prompting

The model receives one example before processing the user's task.

### 3. Few-shot Prompting

The model receives multiple examples to understand the expected response style before answering the user's task.

### 4. Chain of Thought

The model is guided to solve a problem using a structured approach and provide a concise explanation without exposing private internal reasoning.

### 5. Manual Chain of Thought

The prompt provides a predefined structure for solving the problem, including:

1. Understand the problem
2. Identify the important information
3. Apply the appropriate method
4. Verify the result
5. Provide the final answer

### 6. Tree of Thoughts

The model is guided to consider multiple possible approaches, compare them, and select the most suitable approach.

### 7. Multi-Step Chain of Thought

The model follows a multi-step structure including problem understanding, important information, strategy, solution, verification, and final answer.

## Technologies Used

- Python
- Streamlit
- Hugging Face
- Hugging Face Inference API
- Python-dotenv
- Prompt Engineering
- Large Language Models (LLMs)

## Project Structure

```text
Prompt engineering/
│
├── app.py
├── llm.py
├── prompt_template.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

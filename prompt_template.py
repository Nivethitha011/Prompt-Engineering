def create_prompt(technique, user_input):

    if technique == "Zero-Shot":

        prompt = f"""
You are an expert AI assistant.

Answer the user's question directly without using
any examples.

User Question:
{user_input}

Give a clear, accurate and simple answer.
"""

    elif technique == "One-Shot":

        prompt = f"""
You are an expert AI assistant.

Use the following single example as a guide.

Example:

Question: What is Artificial Intelligence?

Answer: Artificial Intelligence is the ability of
machines to perform tasks that normally require
human intelligence.

Now answer this question in a similar style:

Question:
{user_input}

Give a clear and simple answer.
"""

    elif technique == "Few-Shot":

        prompt = f"""
You are an expert AI assistant.

Learn the answering pattern from these examples.

Example 1:

Question: What is CPU?

Answer: CPU is the main processing unit of a computer.


Example 2:

Question: What is RAM?

Answer: RAM is temporary memory used by a computer
to store data while programs are running.


Example 3:

Question: What is a database?

Answer: A database is an organized collection of
data that can be stored and retrieved efficiently.


Now answer:

Question:
{user_input}

Follow the same simple question-answer style.
"""

    elif technique == "Chain of Thought":

        prompt = f"""
You are an expert problem-solving assistant.

Analyze the problem carefully before giving the answer.

Question:
{user_input}

Break the problem into logical steps and then provide
the final answer.

Do not provide hidden or private chain-of-thought.
Give only a concise explanation of the important
steps and the final answer.
"""

    elif technique == "Manual CoT":

        prompt = f"""
You are solving a problem using manually specified
reasoning steps.

Follow this structure:

Step 1: Understand the problem.
Step 2: Identify the important information.
Step 3: Apply the appropriate concept or method.
Step 4: Verify the result.
Step 5: Give the final answer.

Problem:
{user_input}

Return a concise explanation of these steps
followed by the final answer.
"""

    elif technique == "Tree of Thoughts":

        prompt = f"""
You are an expert problem-solving assistant.

Use a Tree of Thoughts style approach.

Problem:
{user_input}

Consider multiple possible approaches to solve
the problem.

Approach 1:
Consider the first possible solution.

Approach 2:
Consider an alternative solution.

Approach 3:
Consider another possible solution.

Compare the approaches and select the most suitable one.

Then provide the final answer with a short explanation.

Do not reveal hidden or private chain-of-thought.
"""

    elif technique == "MCOT":

        prompt = f"""
You are an expert AI assistant.

Solve the following problem using a multi-step
reasoning process.

Problem:
{user_input}

Use this structure:

1. Problem understanding
2. Important information
3. Method or strategy
4. Solution
5. Verification
6. Final answer

Keep the explanation concise and clear.

Do not provide hidden or private chain-of-thought.
"""


    else:

        prompt = f"""
You are an expert AI assistant.

Answer the following question clearly and accurately.

Question:
{user_input}

Give a simple, useful and easy-to-understand answer.
"""


    return prompt.strip()

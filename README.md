Phase 1 Final Assessment: Local AI Support Assistant

Estimated time: 3–5 hours

Open-book practical assessment; documentation is allowed.



Required stack: Python, FastAPI, Pydantic, Ollama, pytest

Use your existing virtual environment and Git workflow.



1. Your mission
Build a Local AI Support Assistant that accepts a technical question, sends it to a local Ollama model, and returns a useful response through an HTTP API.

Example use case: a developer reports that an API returns an HTTP 500 error. Your application should accept the question and return troubleshooting suggestions.

You are not building RAG or an advanced AI agent yet. This assessment tests whether your Python and API foundations are ready for those topics.
2. Requirements
Assessment checklist
0/7



[ ] 1. Project setup — 10 points

Use a virtual environment, organize your files into modules, and document how to install and run the project. Keep secrets and local configuration out of Git.


[ ] 2. Python fundamentals — 15 points

Create reusable functions, use appropriate data structures, add type hints, and separate API, model-client, and configuration responsibilities.


[ ] 3. Request validation — 15 points

Create a POST /chat endpoint with Pydantic request and response models. Reject empty prompts and prompts exceeding 2,000 characters.


[ ] 4. Ollama integration — 20 points

Send the validated prompt to a local Ollama model and return the model's response. Do not hard-code the model name throughout the application.


[ ] 5. Error handling and logging — 15 points

Handle the model service being unavailable and model errors without crashing the application. Return appropriate HTTP errors and log useful diagnostic information without logging sensitive prompts unnecessarily.


[ ] 6. Automated testing — 15 points

Write pytest tests for valid requests, invalid prompts, and model-service failures. Mock the model call so tests can run without a running model.


[ ] 7. Documentation and Git — 10 points

Write a README with setup, configuration, run instructions, endpoint examples, and test commands. Commit your work to a dedicated Git branch.

Use this checklist to track completion, not to award yourself points automatically. I'll grade the actual implementation.

3. Suggested project structure
Create this inside your existing project or a separate assessment folder.
phase1-final-assessment/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── config.py
│   └── llm_client.py
├── tests/
│   ├── __init__.py
│   └── test_chat.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md


You may change this structure if you can explain why your design is better.
4. API contract
Your API must expose the following endpoint:

POST /chat

Request example:
{
  "prompt": "My API returns HTTP 500. How do I troubleshoot it?"
}


Expected response format:
{
  "response": "Check the application logs, reproduce the error, and inspect the server-side exception..."
}


The response content will vary depending on your local model. You are not graded on whether the model gives the exact example answer.

Your application should also handle these cases:
Scenario	Expected behavior
Valid prompt	Return HTTP 200 with a response
Empty prompt	Return HTTP 422
Prompt over 2,000 characters	Return HTTP 422
Ollama is unavailable	Return an appropriate 5xx response
Model returns an error	Return a controlled error response
Automated tests	Pass without requiring Ollama to be running

5. Rules for the assessment
To make this a useful assessment:
- You may use official documentation and search for syntax.
- You may use AI assistance to understand an error, but try to implement the solution yourself first.
- Do not copy an entire ready-made project.
- Do not begin Phase 2 topics such as RAG, vector databases, LangGraph, or agent frameworks.
- Your code must run locally, and you must be able to explain how it works.
One important distinction: Pydantic is required; Pydantic AI is not. You are testing the fundamentals before introducing another framework.
6. How I will grade you

80–100 points: Ready for Phase 2

Your fundamentals are strong enough to begin LLM application development and more advanced model integration.




60–79 points: Almost ready

We'll identify weak areas and complete targeted improvements before moving on.




Below 60 points: Strengthen Phase 1

We'll work through the specific skills that need improvement rather than repeating the entire phase.



Regardless of your score, you must have a working endpoint, valid request validation, and at least basic automated tests before I recommend proceeding.
7. Final submission
When you finish, send me:
1. Your project file structure.
2. The contents of main.py, schemas.py, config.py, and llm_client.py.
3. Your test file and the output of pytest.
4. A sample successful API response and one error response.
5. Your README.
You can paste the code here or upload the project as a ZIP file. Remove any real secrets before sharing it.

I'll review your submission like a technical mentor: score each category, identify bugs and design issues, explain what you did well, and give you a clear pass, conditional pass, or retry decision.

Your goal is not just to make it work. It's to understand why it works. Once you pass, we'll build on this foundation in Phase 2.
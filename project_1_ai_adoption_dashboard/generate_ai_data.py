import pandas as pd
import numpy as np

np.random.seed(47)

n = 5267

cities = ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast", "Newcastle", "Wollongong", "Cairns", "Townsville"]
industries = ["IT", "Finance", "Healthcare", "E-commerce", "EdTech", "Manufacturing"]
roles = ["Data Scientist", "ML Engineer", "AI Engineer", "Data Analyst", "AI Researcher"]
ai_tools = ["ChatGPT", "TensorFlow", "PyTorch", "Scikit-learn", "Azure AI", "AWS AI"]

data = []

for _ in range(n):
    experience = np.random.randint(0, 12)
    role = np.random.choice(roles)
    
    # Salary logic (realistic-ish)
    base_salary = 3.5 + experience * 2 + np.random.normal(0, 2)
    
    if role == "AI Researcher":
        base_salary += 5
    elif role == "ML Engineer":
        base_salary += 3

    salary = max(3, round(base_salary, 2))  # in LPA

    data.append([
        np.random.choice(cities),
        np.random.choice(industries),
        role,
        experience,
        salary,
        np.random.choice(ai_tools),
        np.random.choice([0, 1], p=[0.3, 0.7])  # AI adoption flag
    ])

df = pd.DataFrame(data, columns=[
    "city",
    "industry",
    "role",
    "experience_years",
    "salary_lpa",
    "primary_ai_tool",
    "ai_adopted"
])

df.to_csv("data/ai_australia_data.csv", index=False)

print("AI dataset generated successfully!")
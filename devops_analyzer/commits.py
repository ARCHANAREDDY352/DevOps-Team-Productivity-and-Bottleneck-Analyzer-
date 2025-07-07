import pandas as pd

# Sample commit data
data = {
    "author": ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob", "Charlie"],
    "date": [
        "2024-06-01T10:00:00Z",
        "2024-06-01T11:30:00Z",
        "2024-06-02T09:00:00Z",
        "2024-06-03T15:00:00Z",
        "2024-06-05T08:00:00Z",
        "2024-06-06T10:00:00Z",
        "2024-06-06T12:00:00Z"
    ],
    "message": [
        "Initial commit",
        "Add login feature",
        "Fix bug in authentication",
        "Improve UI",
        "Add README",
        "Refactor dashboard code",
        "Update dependencies"
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Export to commits.csv
df.to_csv("commits.csv", index=False)

print("✅ commits.csv file created successfully!")

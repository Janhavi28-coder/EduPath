import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Subjects
SUBJECTS = ["Math", "Science", "English", "Logical Thinking", "Computer Science", "Social Studies", "Arts"]

# Streams and weights (rule-based)
STREAM_WEIGHTS = {
    "STEM": {"Math": 0.25, "Science": 0.25, "Logical Thinking": 0.2, "Computer Science": 0.3},
    "Arts": {"Arts": 0.4, "English": 0.3, "Social Studies": 0.3},
    "Commerce": {"Math": 0.3, "English": 0.3, "Social Studies": 0.4},
    "Computer Science": {"Computer Science": 0.4, "Math": 0.3, "Logical Thinking": 0.3}
}

# Proficiency levels
def proficiency_level(score):
    if score >= 85:
        return "Advanced"
    elif score >= 70:
        return "Proficient"
    elif score >= 50:
        return "Developing"
    else:
        return "Needs Support"

# Read dataset
df = pd.read_excel("students.xlsx")

# Rule-based prediction
def rule_based_prediction(student):
    scores = {}
    for stream, weights in STREAM_WEIGHTS.items():
        total = sum(student[subj] * w for subj, w in weights.items())
        scores[stream] = total
    best_stream = max(scores, key=scores.get)
    return best_stream, scores[best_stream]

# Prepare ML dataset
X = df[SUBJECTS]
y = []
for _, row in df.iterrows():
    stream, _ = rule_based_prediction(row)
    y.append(stream)

# Train ML model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print("ML Model Accuracy:", accuracy_score(y_test, y_pred))

# Save model
joblib.dump(clf, "decision_tree.pkl")

# Predict for all students
predictions = []
for _, row in df.iterrows():
    rule_stream, conf = rule_based_prediction(row)
    ml_stream = clf.predict([row[SUBJECTS]])[0]
    predictions.append({
        "Roll No": row["Roll No"],
        "Name": row["Name"],
        **{subj: row[subj] for subj in SUBJECTS},
        "Rule_Based_Stream": rule_stream,
        "ML_Stream": ml_stream,
        "Confidence": round(conf/100, 2),
        **{f"{subj}_Proficiency": proficiency_level(row[subj]) for subj in SUBJECTS}
    })

result_df = pd.DataFrame(predictions)
result_df.to_csv("predictions.csv", index=False)
print("Predictions saved to predictions.csv")

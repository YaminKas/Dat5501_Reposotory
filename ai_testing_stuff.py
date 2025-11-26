import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


#LOAD DATA

df = pd.read_csv("car.csv", header=None)

df.columns = [
    "buying", "maint", "doors", "persons",
    "lug_boot", "safety", "class"
]

#Features + target
X = df.drop("class", axis=1)
y = df["class"]

#TRAIN/TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


#ENCODING + MODEL PIPELINE

categorical_features = X.columns.tolist()

preprocess = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

model = Pipeline(steps=[
    ("prep", preprocess),
    ("clf", RandomForestClassifier(n_estimators=200, random_state=42))
])

#TRAIN MODEL

model.fit(X_train, y_train)


#EVALUATE

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
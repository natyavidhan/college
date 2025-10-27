import pandas as pd
import numpy as np
from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split, cross_validate, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


iris = load_iris()
X1 = pd.DataFrame(iris.data, columns=iris.feature_names)
y1 = iris.target

wine = load_wine()
X2 = pd.DataFrame(wine.data, columns=wine.feature_names)
y2 = wine.target

scaler = StandardScaler()
X1_scaled = scaler.fit_transform(X1)
X2_scaled = scaler.fit_transform(X2)

models = {
    "Naive Bayes": GaussianNB(),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(random_state=42)
}

def evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    return {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, average='weighted'),
        "Recall": recall_score(y_test, y_pred, average='weighted'),
        "F1-score": f1_score(y_test, y_pred, average='weighted')
    }

# Holdout Validation

holdout_results = []

for dataset_name, (X, y) in {"Iris": (X1_scaled, y1), "Wine": (X2_scaled, y2)}.items():
    for split, test_size in {"80/20": 0.2, "66.6/33.3": 0.333}.items():
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)

        for model_name, model in models.items():
            scores = evaluate_model(model, X_train, X_test, y_train, y_test)
            holdout_results.append({
                "Dataset": dataset_name,
                "Split": split,
                "Model": model_name,
                **scores
            })

holdout_df = pd.DataFrame(holdout_results)
print("\n=== Holdout Method Results ===")
print(holdout_df)

# Cross-Validation

cv_results = []

for dataset_name, (X, y) in {"Iris": (X1_scaled, y1), "Wine": (X2_scaled, y2)}.items():
    for folds in [5, 10]:
        kf = KFold(n_splits=folds, shuffle=True, random_state=42)

        for model_name, model in models.items():
            scores = cross_validate(model, X, y, cv=kf,
                                    scoring=['accuracy', 'precision_weighted', 'recall_weighted', 'f1_weighted'])
            
            cv_results.append({
                "Dataset": dataset_name,
                "CV_Folds": folds,
                "Model": model_name,
                "Accuracy": np.mean(scores['test_accuracy']),
                "Precision": np.mean(scores['test_precision_weighted']),
                "Recall": np.mean(scores['test_recall_weighted']),
                "F1-score": np.mean(scores['test_f1_weighted'])
            })

cv_df = pd.DataFrame(cv_results)
print("\n=== Cross-Validation Results ===")
print(cv_df)


# Comparison of Holdout vs Cross-Validation
print("\n===== FINAL COMPARISON =====")
print(pd.concat([holdout_df, cv_df], ignore_index=True))

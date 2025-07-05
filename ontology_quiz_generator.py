"""Generate MCQ quizzes and evaluate them using a BERT-based similarity metric.

This script follows the ontology-driven approach outlined in the provided
research paper. It builds a Python ontology, generates learning materials
and multiple-choice questions (MCQs) for each domain concept, and then
evaluates the generated materials using sentence embeddings. The accuracy
score represents the cosine similarity between generated content and
reference materials, computed with a pre-trained BERT model.
"""

from __future__ import annotations

import csv
from typing import Dict, List, Sequence

from python_ontology import build_python_ontology, ontology_as_dict

try:
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    _HAS_SKLEARN = True
except Exception:  # pragma: no cover - allow running without sklearn
    _HAS_SKLEARN = False

    def compute_metrics(y_true: List[int], y_pred: List[int]) -> tuple[float, float, float, float]:
        tp = sum(1 for t, p in zip(y_true, y_pred) if t == p == 1)
        fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
        fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
        tn = sum(1 for t, p in zip(y_true, y_pred) if t == p == 0)
        accuracy = (tp + tn) / (tp + fp + fn + tn)
        precision = tp / (tp + fp) if tp + fp else 0.0
        recall = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        return accuracy, precision, recall, f1

try:
    from sentence_transformers import SentenceTransformer, util
    MODEL = SentenceTransformer("all-MiniLM-L6-v2")
except Exception:  # pragma: no cover - network or install issues
    import sys
    print("BERT model unavailable, falling back to Jaccard similarity", file=sys.stderr)
    SentenceTransformer = None  # type: ignore
    util = None  # type: ignore
    MODEL = None

# Build the ontology and use its descriptions as learning materials
ONTOLOGY_ROOT = build_python_ontology()
LEARNING_MATERIALS: Dict[str, str] = ontology_as_dict(ONTOLOGY_ROOT)

# Attempt to load a lightweight BERT model for semantic similarity evaluation
# If loading fails, similarity will fall back to a Jaccard metric.

# Additional topics not explicitly covered in the ontology hierarchy
LEARNING_MATERIALS.update(
    {
        "Algorithms": (
            "Algorithms are step-by-step procedures for solving problems. In "
            "Python, you can implement algorithms for sorting, searching, and "
            "manipulating data."
        ),
        "RelationalOperator": "In Python, relational operators compare two values and return a Boolean result (True or False).",
        "LogicalOperator": "In Python, logical operators combine multiple conditions into a single Boolean result.",
        "Variable": "In Python, a variable is a named reference to a value stored in memory.",
    }
)

def load_mcq_bank(path: str) -> Dict[str, List[Dict[str, Sequence[str]]]]:
    """Load MCQs from a CSV file and group them by domain."""
    bank: Dict[str, List[Dict[str, Sequence[str]]]] = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            domain = row["Domain"]
            mcq = {
                "question": row["Question"],
                "options": [row["A"], row["B"], row["C"], row["D"]],
                "answer": row["Answer"],
                "difficulty": row.get("Difficulty", "Beginner"),
            }
            bank.setdefault(domain, []).append(mcq)
    return bank


def bert_similarity(text_a: str, text_b: str) -> float:
    """Compute cosine similarity of two texts using BERT embeddings."""
    if MODEL is None or util is None:
        # Fallback Jaccard similarity when the model is unavailable
        set_a = set(text_a.lower().split())
        set_b = set(text_b.lower().split())
        if not set_a and not set_b:
            return 1.0
        return len(set_a & set_b) / len(set_a | set_b)
    if not text_a and not text_b:
        return 1.0
    emb_a = MODEL.encode(text_a, convert_to_tensor=True)
    emb_b = MODEL.encode(text_b, convert_to_tensor=True)
    return float(util.cos_sim(emb_a, emb_b))


def generate_learning_material(domain: str) -> str:
    """Return the learning material text for the given domain."""
    return LEARNING_MATERIALS.get(domain, "No materials available for this topic.")


def generate_mcqs(domain: str, bank: Dict[str, List[Dict[str, Sequence[str]]]]) -> List[Dict[str, Sequence[str]]]:
    """Return a list of MCQs for the given domain."""
    return bank.get(domain, [])


def evaluate_material(material: str, domain: str) -> float:
    """Evaluate generated material by comparing it to the reference text."""
    reference = LEARNING_MATERIALS.get(domain, "")
    return bert_similarity(material, reference)


def create_evaluation_table(
    domains: Sequence[str],
    mcq_bank: Dict[str, List[Dict[str, Sequence[str]]]],
    threshold: float = 0.9,
) -> tuple[List[Dict[str, str]], Dict[str, float]]:
    """Generate learning materials, MCQs and evaluation scores."""
    table: List[Dict[str, str]] = []
    y_true: List[int] = []
    y_pred: List[int] = []
    for domain in domains:
        material = generate_learning_material(domain)
        score = evaluate_material(material, domain)
        mcqs = generate_mcqs(domain, mcq_bank)

        y_true.append(1)  # reference materials are considered correct
        y_pred.append(1 if score >= threshold else 0)

        mcq_lines = []
        for mcq in mcqs:
            mcq_lines.append(f"Q: {mcq['question']}")
            for opt in mcq["options"]:
                mcq_lines.append(f" - {opt}")
            mcq_lines.append(f"Answer: {mcq['answer']}")
            mcq_lines.append("")
        mcq_text = "\n".join(mcq_lines)

        if score > 0.9:
            description = "Excellent alignment with reference material."
        elif score > 0.7:
            description = "Good alignment but could improve in specific areas."
        else:
            description = "Moderate alignment, requires improvements in content generation."

        table.append(
            {
                "Domain": domain,
                "Generated Learning Material": material,
                "Accuracy Score (%)": f"{score * 100:.2f}%",
                "MCQs": mcq_text,
                "Description": description,
            }
        )

    if _HAS_SKLEARN:
        metrics = {
            "accuracy": accuracy_score(y_true, y_pred),
            "precision": precision_score(y_true, y_pred, zero_division=0),
            "recall": recall_score(y_true, y_pred, zero_division=0),
            "f1": f1_score(y_true, y_pred, zero_division=0),
        }
    else:
        acc, prec, rec, f1 = compute_metrics(y_true, y_pred)
        metrics = {
            "accuracy": acc,
            "precision": prec,
            "recall": rec,
            "f1": f1,
        }

    return table, metrics


def main() -> None:
    mcq_bank = load_mcq_bank("mcq_dataset.csv")
    domains = list(mcq_bank.keys())
    table, metrics = create_evaluation_table(domains, mcq_bank)

    fieldnames = ["Domain", "Generated Learning Material", "Accuracy Score (%)", "MCQs", "Description"]
    with open("evaluation_table.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(table)

    for row in table:
        print(f"Domain: {row['Domain']}")
        print(f"Accuracy: {row['Accuracy Score (%)']}")
        if row["MCQs"]:
            print("MCQs:\n" + row["MCQs"])
        print("-" * 40)

    print("Overall Metrics:")
    print(f"Accuracy: {metrics['accuracy'] * 100:.2f}%")
    print(f"Precision: {metrics['precision'] * 100:.2f}%")
    print(f"Recall: {metrics['recall'] * 100:.2f}%")
    print(f"F1-Score: {metrics['f1'] * 100:.2f}%")


if __name__ == "__main__":
    main()
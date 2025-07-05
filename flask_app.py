from __future__ import annotations

import random
from flask import Flask, render_template, request

from python_ontology import (
    build_python_ontology,
    ontology_as_dict,
    iter_nodes,
)
from ontology_quiz_generator import load_mcq_bank, evaluate_material

app = Flask(__name__)

# Load ontology and MCQ bank once on startup
ONTOLOGY_ROOT = build_python_ontology()
LEARNING_MATERIALS = ontology_as_dict(ONTOLOGY_ROOT)
MCQ_BANK = load_mcq_bank("mcq_dataset.csv")
DOMAINS = sorted(MCQ_BANK.keys())
DIFFICULTY_MAP = {node.name: node.difficulty for node in iter_nodes(ONTOLOGY_ROOT)}
DIFFICULTIES = ["Any", "Beginner", "Intermediate", "Advanced"]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", domains=DOMAINS, difficulties=DIFFICULTIES)

@app.route("/quiz", methods=["POST"])
def quiz():
    domain = request.form.get("domain")
    difficulty = request.form.get("difficulty", "Any")
    try:
        num = int(request.form.get("num", 5))
    except ValueError:
        num = 5
    # Do not automatically change the user's selected domain. Instead, filter
    # the questions by difficulty if a specific level was requested.
    questions = MCQ_BANK.get(domain, [])
    if difficulty != "Any":
        questions = [q for q in questions if q.get("difficulty") == difficulty]
    sampled = random.sample(questions, min(num, len(questions)))
    
    # Only calculate similarity if there are questions available for the selected difficulty
    if len(questions) > 0:
        sim = evaluate_material(LEARNING_MATERIALS.get(domain, ""), domain) * 100
    else:
        sim = 0.0  # No similarity when no questions are available
    return render_template(
        "quiz.html",
        domain=domain,
        questions=sampled,
        difficulty=difficulty,
        similarity=f"{sim:.2f}",
    )

if __name__ == "__main__":
    app.run(debug=True)
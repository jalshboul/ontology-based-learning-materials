from __future__ import annotations

"""Comprehensive ontology for Python programming concepts."""

from dataclasses import dataclass, field
from typing import Dict, Iterable, List


@dataclass
class Relationship:
    """Represents a semantic relationship between ontology concepts."""

    type: str
    target: str


@dataclass
class OntologyNode:
    """A node in the Python programming ontology."""

    name: str
    description: str
    difficulty: str = "Beginner"
    examples: List[str] = field(default_factory=list)
    relationships: List[Relationship] = field(default_factory=list)
    children: List["OntologyNode"] = field(default_factory=list)

    def add_child(self, child: "OntologyNode") -> None:
        self.children.append(child)

    def add_relationship(self, relation: str, target: str) -> None:
        self.relationships.append(Relationship(relation, target))


def build_python_ontology() -> OntologyNode:
    """Return the root node of a comprehensive Python ontology."""

    root = OntologyNode(
        "PythonProgramming",
        "Comprehensive ontology covering Python concepts and their relationships.",
    )

    # ---------------------- Core Language Features ----------------------
    core = OntologyNode("CoreLanguage", "Fundamental Python syntax and features.")

    data_types = OntologyNode(
        "DataTypes",
        "Primitive and composite types available in Python.",
        difficulty="Beginner",
        examples=["x = 1", "name = 'Alice'"]
    )
    numbers = OntologyNode(
        "Numbers",
        "Integers, floats and numeric operations.",
        difficulty="Beginner",
        examples=["result = 2 + 3"]
    )
    strings = OntologyNode(
        "Strings",
        "Text sequences and related operations.",
        difficulty="Beginner",
        examples=["greeting = 'hello'.upper()"]
    )
    lists = OntologyNode(
        "Lists",
        "Mutable ordered collections.",
        difficulty="Beginner",
        examples=["items = [1, 2, 3]"]
    )
    tuples = OntologyNode(
        "Tuples",
        "Immutable ordered collections.",
        difficulty="Beginner",
        examples=["point = (1, 2)"]
    )
    dictionaries = OntologyNode(
        "Dictionaries",
        "Key-value mappings.",
        difficulty="Beginner",
        examples=["ages = {'Bob': 30}"]
    )
    sets = OntologyNode(
        "Sets",
        "Unordered collections of unique elements.",
        difficulty="Beginner",
        examples=["unique = set([1, 2, 2, 3])"]
    )
    booleans = OntologyNode(
        "Booleans",
        "True/False values used in logic.",
        difficulty="Beginner",
        examples=["flag = True"]
    )
    arithmetic = OntologyNode(
        "Arithmetic",
        "Basic mathematical operations such as addition and subtraction.",
        difficulty="Beginner",
        examples=["result = 2 + 2", "total = 5 - 3"],
    )
    keywords = OntologyNode(
        "Keywords",
        "Reserved words that have special meaning in Python syntax.",
        difficulty="Beginner",
        examples=["if", "for", "while"],
    )
    builtins_node = OntologyNode(
        "Builtins",
        "Common functions that are always available in Python.",
        difficulty="Beginner",
        examples=["len(obj)", "range(10)"],
    )
    modules = OntologyNode(
        "Modules",
        "Organizing and importing reusable pieces of code.",
        difficulty="Intermediate",
        examples=["import math"],
    )
    for node in [
        numbers,
        strings,
        lists,
        tuples,
        dictionaries,
        sets,
        booleans,
        arithmetic,
        keywords,
        builtins_node,
        modules,
    ]:
        data_types.add_child(node)

    control_structures = OntologyNode(
        "ControlStructures",
        "Flow control statements and loops.",
        difficulty="Beginner",
        examples=["if x > 0:", "for i in range(5):"]
    )
    conditions = OntologyNode(
        "Conditions",
        "if/elif/else statements.",
        difficulty="Beginner",
        examples=["if value == 1:"]
    )
    loops = OntologyNode(
        "Loops",
        "for and while loops.",
        difficulty="Beginner",
        examples=["while count < 10:"]
    )
    control_structures.children.extend([conditions, loops])

    functions = OntologyNode(
        "Functions",
        "Function definitions and calls.",
        difficulty="Intermediate",
        examples=["def add(a, b):", "return a + b"]
    )
    classes = OntologyNode(
        "Classes",
        "Object-oriented programming with classes.",
        difficulty="Intermediate",
        examples=["class Car:", "    pass"]
    )
    fileio = OntologyNode(
        "FileIO",
        "Reading from and writing to files on disk.",
        difficulty="Intermediate",
        examples=["open('data.txt', 'r')"],
    )
    exceptions = OntologyNode(
        "Exceptions",
        "Handling errors with try/except blocks.",
        difficulty="Intermediate",
        examples=["try:\n    pass\nexcept Exception:"],
    )
    concurrency = OntologyNode(
        "Concurrency",
        "Running multiple operations at the same time.",
        difficulty="Advanced",
        examples=["import threading"],
    )
    core.children.extend([
        data_types,
        control_structures,
        functions,
        classes,
        fileio,
        exceptions,
    ])

    # ---------------------- Standard Library ----------------------
    stdlib = OntologyNode(
        "StandardLibrary",
        "Commonly used modules that ship with Python.",
        difficulty="Intermediate",
        examples=["import os", "import sys"]
    )
    json_mod = OntologyNode(
        "json",
        "JSON encoding and decoding.",
        difficulty="Intermediate",
        examples=["import json", "json.loads('{\"key\": 1}')"]
    )
    csv_mod = OntologyNode(
        "csv",
        "CSV reading and writing.",
        difficulty="Intermediate",
        examples=["import csv", "csv.reader(...)"]
    )
    stdlib.children.extend([json_mod, csv_mod])

    # ---------------------- Functional Programming ----------------------
    functional = OntologyNode(
        "FunctionalProgramming",
        "Using functions as first-class objects and related paradigms.",
        difficulty="Intermediate",
        examples=["map(str, items)", "lambda x: x * 2"]
    )
    decorators = OntologyNode(
        "Decorators",
        "Functions that modify other functions or methods.",
        difficulty="Advanced",
        examples=["@cache", "def func(...): ..."]
    )
    functional.add_child(decorators)

    # ---------------------- Data Structures & Algorithms ----------------------
    ds_algo = OntologyNode(
        "DataStructuresAlgorithms",
        "Classic data structures and algorithms.",
        difficulty="Intermediate",
        examples=["stack.append(x)", "sorted(items)"]
    )
    searching = OntologyNode(
        "Searching",
        "Techniques such as binary search.",
        difficulty="Intermediate",
        examples=["bisect.bisect_left(...)"]
    )
    sorting = OntologyNode(
        "Sorting",
        "Algorithms that order data.",
        difficulty="Intermediate",
        examples=["sorted(list_of_values)"]
    )
    algorithms = OntologyNode(
        "Algorithms",
        "General techniques for solving computational problems.",
        difficulty="Intermediate",
        examples=["binary search", "merge sort"],
    )
    ds_algo.children.extend([searching, sorting, algorithms])

    # ---------------------- Web Development ----------------------
    web = OntologyNode(
        "WebFrameworks",
        "Popular Python web frameworks.",
        difficulty="Intermediate",
        examples=["from flask import Flask"]
    )
    flask = OntologyNode(
        "Flask",
        "Lightweight WSGI web application framework.",
        difficulty="Intermediate",
        examples=["app = Flask(__name__)"]
    )
    django = OntologyNode(
        "Django",
        "Full-featured web framework for large applications.",
        difficulty="Intermediate",
        examples=["django-admin startproject mysite"]
    )
    web.children.extend([flask, django])

    # ---------------------- Data Science Libraries ----------------------
    data_science = OntologyNode(
        "DataScienceLibraries",
        "Libraries used for data analysis and visualization.",
        difficulty="Intermediate",
        examples=["import numpy as np", "import pandas as pd"]
    )
    numpy_node = OntologyNode(
        "NumPy",
        "Numerical computing with arrays.",
        difficulty="Intermediate",
        examples=["np.array([1, 2, 3])"]
    )
    pandas_node = OntologyNode(
        "Pandas",
        "Data analysis and manipulation library.",
        difficulty="Intermediate",
        examples=["pd.DataFrame({'a': [1, 2]})"]
    )
    matplotlib_node = OntologyNode(
        "Matplotlib",
        "2D plotting library for creating visualizations.",
        difficulty="Intermediate",
        examples=["plt.plot(x, y)"]
    )
    data_science.children.extend([numpy_node, pandas_node, matplotlib_node])

    # ---------------------- Machine Learning Frameworks ----------------------
    ml = OntologyNode(
        "MachineLearning",
        "Frameworks for building machine learning models.",
        difficulty="Advanced",
        examples=["import tensorflow as tf"]
    )
    tensorflow_node = OntologyNode(
        "TensorFlow",
        "End-to-end platform for machine learning.",
        difficulty="Advanced",
        examples=["tf.constant([1, 2])"]
    )
    pytorch_node = OntologyNode(
        "PyTorch",
        "Deep learning framework emphasizing flexibility.",
        difficulty="Advanced",
        examples=["import torch"]
    )
    ml.children.extend([tensorflow_node, pytorch_node])

    # ---------------------- Testing & Debugging ----------------------
    testing = OntologyNode(
        "TestingDebugging",
        "Tools for testing and debugging Python code.",
        difficulty="Intermediate",
        examples=["import unittest"]
    )
    unittest_node = OntologyNode(
        "unittest",
        "Built-in unit testing framework.",
        difficulty="Intermediate",
        examples=["unittest.TestCase"]
    )
    pytest_node = OntologyNode(
        "pytest",
        "Popular third-party testing framework.",
        difficulty="Intermediate",
        examples=["pytest.raises(ValueError)"]
    )
    testing.children.extend([unittest_node, pytest_node])

    # ---------------------- DevOps & Deployment ----------------------
    devops = OntologyNode(
        "DevOps",
        "Practices for packaging and deploying Python applications.",
        difficulty="Advanced",
        examples=["docker build", "pip install"]
    )
    venv_node = OntologyNode(
        "VirtualEnvironments",
        "Isolated Python environments for dependency management.",
        difficulty="Intermediate",
        examples=["python -m venv env"]
    )
    packaging_node = OntologyNode(
        "Packaging",
        "Creating distributable Python packages.",
        difficulty="Advanced",
        examples=["python -m build"]
    )
    devops.children.extend([venv_node, packaging_node])

    # Assemble ontology tree
    root.children.extend(
        [
            core,
            stdlib,
            functional,
            ds_algo,
            web,
            data_science,
            ml,
            concurrency,
            testing,
            devops,
        ]
    )
    return root


def iter_nodes(root: OntologyNode) -> Iterable[OntologyNode]:
    """Yield all nodes in the ontology tree."""
    stack = [root]
    while stack:
        node = stack.pop()
        yield node
        stack.extend(node.children)


def ontology_as_dict(root: OntologyNode) -> Dict[str, str]:
    """Return a mapping of node names to descriptions."""
    return {node.name: node.description for node in iter_nodes(root)}
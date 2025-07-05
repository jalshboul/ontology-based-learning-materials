# Ontology-Based Automatic Generation of Learning Materials for Python Programming

This repository contains a Flask web application that demonstrates **ontology-based automatic generation of learning materials** for Python programming education. The system uses a structured ontology to generate quizzes with multiple-choice questions (MCQs) and evaluates the semantic similarity between learning materials and quiz content.

## 🚀 Features

- **Ontology-driven quiz generation**: Uses a comprehensive Python programming ontology
- **Adaptive difficulty levels**: Supports Beginner, Intermediate, and Advanced difficulty levels
- **Semantic similarity evaluation**: Calculates similarity between learning materials and quiz content
- **Domain-specific content**: Covers various Python programming domains (Variables, Functions, Data Structures, etc.)
- **Interactive web interface**: Clean and user-friendly Flask-based web application

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ontology-based-learning-materials.git
cd ontology-based-learning-materials
```

### 2. Create a Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

**Option A: Using requirements.txt (Recommended)**
```bash
pip install -r requirements.txt
```

**Option B: Manual installation**
```bash
pip install flask scikit-learn
```

### 4. Verify Required Files
Make sure the following files are present in the project directory:
- `flask_app.py` - Main Flask application
- `python_ontology.py` - Python programming ontology
- `ontology_quiz_generator.py` - Quiz generation and evaluation logic
- `mcq_dataset.csv` - Multiple-choice questions dataset
- `templates/` - HTML templates directory
  - `base.html`
  - `index.html` 
  - `quiz.html`

## 🏃‍♂️ Running the Application

### Option 1: Direct Python Execution
```bash
python flask_app.py
```

### Option 2: Using Flask Command (Alternative)
```bash
# Set Flask environment variables
set FLASK_APP=flask_app.py
set FLASK_ENV=development

# Run the application
flask run
```

The application will start on `http://127.0.0.1:5000` (or `http://localhost:5000`)

## 📖 Usage

1. **Access the Application**: Open your web browser and navigate to `http://localhost:5000`

2. **Select Parameters**:
   - Choose a **Domain** (e.g., Variables, Functions, Data Structures)
   - Select a **Difficulty Level** (Any, Beginner, Intermediate, Advanced)
   - Enter the **Number of Questions** you want to generate

3. **Generate Quiz**: Click the "Generate Quiz" button

4. **View Results**: The application will display:
   - Generated quiz questions with multiple-choice answers
   - Learning Material Similarity percentage
   - Domain and difficulty information

## 🏗️ Project Structure

```
ontology-flask-app-clean/
├── flask_app.py                 # Main Flask application
├── python_ontology.py           # Python programming ontology definition
├── ontology_quiz_generator.py   # Quiz generation and evaluation logic
├── mcq_dataset.csv             # Multiple-choice questions dataset
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── .gitignore                  # Git ignore rules
└── templates/                  # HTML templates
    ├── base.html              # Base template
    ├── index.html             # Home page
    └── quiz.html              # Quiz display page
```

## 🔧 Configuration

The application loads the ontology and MCQ dataset on startup. Key configuration happens in `flask_app.py`:

- **Ontology Loading**: `ONTOLOGY_ROOT = build_python_ontology()`
- **MCQ Dataset**: `MCQ_BANK = load_mcq_bank("mcq_dataset.csv")`
- **Debug Mode**: `app.run(debug=True)` for development

## 📊 How It Works

1. **Ontology Construction**: The system builds a comprehensive Python programming ontology with hierarchical relationships
2. **Content Generation**: Learning materials are generated based on ontological concepts
3. **Quiz Filtering**: Questions are filtered by domain and difficulty level
4. **Similarity Evaluation**: Semantic similarity is calculated between learning materials and quiz content
5. **Web Interface**: Results are presented through a clean Flask web interface

## 🐛 Troubleshooting

### Common Issues

**1. Import Errors**
```bash
ModuleNotFoundError: No module named 'flask'
```
**Solution**: Make sure you've activated your virtual environment and installed dependencies:
```bash
pip install flask scikit-learn
```

**2. Template Not Found**
```bash
jinja2.exceptions.TemplateNotFound: index.html
```
**Solution**: Ensure the `templates/` directory exists with all required HTML files.

**3. CSV File Not Found**
```bash
FileNotFoundError: [Errno 2] No such file or directory: 'mcq_dataset.csv'
```
**Solution**: Verify that `mcq_dataset.csv` is in the project root directory.

**4. Port Already in Use**
```bash
OSError: [Errno 48] Address already in use
```
**Solution**: Either stop the existing process or run on a different port:
```bash
python flask_app.py --port 5001
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Work

This project implements concepts from research in:
- Ontology-based learning systems
- Automatic educational content generation
- Semantic similarity evaluation in educational contexts
- Adaptive learning technologies

## 📧 Contact

For questions or support, please open an issue in the GitHub repository.

---

**Note**: This is a research prototype demonstrating ontology-based learning material generation. For production use, consider adding authentication, database integration, and enhanced security measures.  
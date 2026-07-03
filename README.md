# AI Toolkit CLI

An AI Toolkit CLI built with Python that uses tools, such as translate texts, analyse sentiment and summarise the texts.

---

## Repository Structure

```
AI-Toolkit-CLI/
├── main.py
├── README.md
├── requirements.txt
├── .env.example
├── .env
└── .gitignore
```

---

## Prerequisites

| Tool     | Version |
|----------|---------|
| Python   | ≥ 3.9   |
| pip      | Latest  |

---

## Quick Start

### 1. Clone the Repository

```bash
Git clone https://github.com/Renz-Victa/AI-Toolkit-CLI
cd AI-Toolkit-CLI
```

### 2. Install the Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create your .env file and API key

Copy the example in the .env.example and paste it in the .env file.

```bash
OPENAI_API_KEY=your_api_key
```

### 4. Run the CLI

Summarise the texts:

```bash
python main.py summarise --text "input your your summary here."
```

Translate text:

```bash
python main.py translate --language Spanish --text "input your text in any language here and it will translate in Spanish."
```

Sentiment Analysis:

```bash 
python main.py  sentiment -- text "I love this food, but the preparation is confusing at first."
```

Use a text file that you want to summarise:

```bash
python main.py summarise --file summarise.txt
```

---

### Configuration

Create a .env file in the project root, if the toolkit needs an API key

```
API_KEY=your_api_key_here
```

After that, load it in main.py file before you run the CLI.

---

## License

This project is licensed under the MIT License.
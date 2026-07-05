import argparse
import sys
from dataclasses import dataclass
from typing import List
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()
client = os.dotenv("OPENAI_API_KEY")

parser = argparse.ArgumentParser(description="prompt")
parser.add_argument("-v", "--verbose", action="store_true", help="Turn on verbose logging")
parser.add_argument("-o", "--output", type=str, default="research.txt", help="Output file path")
args = parser.parse_args()

if args.verbose:
  print(f"Verbose mode active. Saving results to: {args.output}")

flag_active = "--flag" in sys.argv or "-f" in sys.argv
print("Flag is on!" if flag_active else "Flag is off.")

def greet(name: Optional[str]) -> str: 
  if name is None:
    return "Hello, Guest"
  return f"Hello, {name}"

def train_model(data, model, *, epochs, learning_rate):
  print(f"Training {model} for {epochs} epochs with lr={learning_rate}")

train_model("dataset.csv", epochs=10, learning_rate=0.001)

def build_optimizer(model, *, lr=0.001, weight_decay=0.0, beta1=0.9):
  print("Optimizer configured")

class Dataset:
  def __init__(self, data):
    self.data = data  

  def predict(self, x):
    return self.data
  
model = Dataset(data=2)

result = model.predict(5)
print(result)

class BaseModel:
  def train(self):
    print("Training the Model...")
  
  def predict(self, x):
    print("Making a Prediction")

class NeuralNetwork(BaseModel):
  def __init__(self):
    print("Neural Network Initialised")

  def predict(self, x):
    print("Deep learning prediction")

model = NeuralNetwork()
model.train()
model.predict(10)

# ---------------------
# DataClass Syntax
# ---------------------

@dataclass
class TrainingConfig:
  learning_rate: float = 0.001
  batch_size: int = 32
  epochs: int = 10

config = TrainingConfig(
  learning_rate=0.001,
  batch_size=32,
  epochs=10
)

print(config.learning_rate)
print(config.batch_size)

@dataclass
class ModelConfig:
  model_name: str
  max_tokens: int
  temperature: float
  hidden_size: int = 768
  num_layers: int = 12
  dropout: float = 0.1
  vocab_size: int = 20000

config = ModelConfig(
  hidden_size=128,
  num_layers=12,
  dropout=0.1,
  vocab_size=50000,
  model_name="gpt-model",
  max_tokens=1000,
  temperature=0.5
)

@dataclass
class Message: 
  timestamp: str
  model: str = "gpt-3.5"
  input: str = ""

# ---------------------
# Dictionary, List, and String Syntax
# ---------------------

model = os.getenv["gpt-3.5":"OPENAI_API_KEY"]
tokens_used = os.dotenv("OPENAI_API_KEY")
status = f"{model} has used {tokens_used} tokens so far."

model_config = {
  "model": "gpt-3.5",
  "temperature": "0.",
  "max_tokens": 900
}

tools = [
  {"tool": "Translate Texts"},
  {"tool": "Analyse Sentiment"},
  {"tool": "Summarise the Texts"}
]

# ---------------------
# 2. Type Hints
# ---------------------

features: list[str, float]

# ---------------------
# 4. Input from user
# ---------------------

def user_prompt(client, model):
  user_prompt = input("Enter your question: ")
  response = f"AI Response to: {user_prompt}"
  print(response)

# ---------------------
# 5. Conditionals
# ---------------------

def spam():
  spam_probability = 0.70
  if spam_probability >= 0.70:
    print("This email is spam")
  else: 
    print("This email is not spam")

# ---------------------
# 6. Loops
# ---------------------

def loop():
  while True: 
    message = input("Do you want to exit? yes/no")

    if message.lower() == "yes":
      print("Goodbye!")
      break

  print("Received Successfully!")

# ---------------------
# 7. Set Comprehensions
# ---------------------

unique_tools = {t["tool"] for t in tools}

# ---------------------
# 9. *args and **kwargs
# ---------------------

class LLM_Model:
  def __init__(self, *layers, **config):
    self.layers = layers
    self.lr = config.get("lr", 0.001)
    self.activation = config.get("activation", "relu")

# ---------------------
# 11. Exception Handling
# ---------------------

def test_API(client):
  try:
    response = client.responses.create(
      model="gpt-3.5"
    )
  
  except Exception as e:
    print(f"LLM API failed: {e}")
  except ConnectionError:
    print("Failed to connect to the API.")

class RetrievalError(Exception):
  def retrieve_documents():
    try: 
      file = open("summarise.txt")
      data = file.retrieve_documents()
    except FileNotFoundError:
      print("File missing")
    except ValueError:
      print("Invalid data")
    except Exception as e:
      print(f"Unexpected error: {e}")
    except RetrievalError as e:
      print(str(e))
    except TimeoutError:
      print("Request time out. Please try again later.")
    finally:
      print("Finished!")
    return data

def read_file(client):
  try:
    file = open("summarise.txt")
    data = file.read()

  except FileNotFoundError:
    print("File not found")
    return data

# ---------------------
# 14. File Reading and Writing
# ---------------------

def summary():
  with open("summarise.txt", "r") as f:
    prompt = f.read()

  with open("summarise.txt", "w") as f:
    f.write()

  with open("sumarise.txt", "a") as f:
    f.write("Model run completed\n")
  return prompt
    

# ---------------------
# 15. Path Handling
# ---------------------

def path_handling():
  prompt_path = Path("prompts") / "summarise.txt"
  with prompt_path.open("r") as f:
    prompt = f.read()

  with prompt_path.open("w") as f:
    f.write("Generated summary from this model.")

def ask_openai(client, prompt, model=os.getenv("OPENAI_API_KEY")):
  response = client.responses.create(
    model="gpt-3.5",
    input=""
  )
  return response.output_text
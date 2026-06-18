import argparse
import sys
from dataclasses import dataclass
from typing import List
import json
from pathlib import Path
from typing import Optional

parser = argparse.ArgumentParser(description="A script with a optional flags")

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

def train_model(data, *, epochs, learning_rate):
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
  hidden_size: int = 768
  num_layers: int = 12
  dropout: float = 0.1
  vocab_size: int = 20000
  model_name: str
  max_tokens: int
  temperature: float

config = ModelConfig(
  hidden_size=128,
  num_layers=12,
  dropout=0.1,
  vocab_size=50000,
  model_name="gpt-model",
  max_tokens=1000,
  temperature=0.5
)

model = ModelConfig(config)

@dataclass
class Message: 
  role: str
  content: str = ""
  timestamp: str

message1 = Message(
  role="user", 
  content="What is this model?"
)

message2 = Message(
  role="assistant",
  content="This is an AI Toolkit CLI"
)

# ---------------------
# Dictionary, List, and String Syntax
# ---------------------

model_config = {
  "model": "gpt-3.5",
  "temperature": "0.5",
  "max_tokens": 900
}

tools = [
  "websearch",
  "calculator",
  "file-reader",
  "code_executor"
]

model = "gpt-3.5"
tokens_used = 100

status = f"model {model} has used {tokens_used} tokens so far"

# ---------------------
# 2. Type Hints
# ---------------------

features: list[str, float]

# ---------------------
# 4. Input from user
# ---------------------

user_prompt: str = input("Enter your question: ")
response = f"AI Response to: {user_prompt}"
print(response)

# ---------------------
# 5. Conditionals
# ---------------------

spam_probability = 0.70

if spam_probability >= 0.70:
  print("This email is spam")
else: 
  ("This email is not spam")

# ---------------------
# 6. Loops
# ---------------------

while True: 
  message = input("You need: ")

  if message.lower() == "exit":
    print("Bot: Goodbye!")
    break

  print("Bot: I received:", message)

# ---------------------
# 7. Set Comprehensions
# ---------------------

tools = [
  {"tool": "load prompts from files"},
  {"tool": "Run through an LLM Model"},
  {"tool": "Save responses automatically"},
  {"tool": "Keep History"}
]

unique_tools = {t["tool"] for t in tools}

# ---------------------
# 9. *args and **kwargs
# ---------------------

class LLM_Model:
  def __init__(self, *layers, **config):
    self.layers = layers
    self.lr = config.get("lr", 0.001)
    self.activation = config.get("activation", "relu")

model = LLM_Model(64, 128, 10, lr=0.001, activation="tanh")

# ---------------------
# 11. Exception Handling
# ---------------------

try:
  response = model_config.responses.create(
    model="gpt-3.5"
    )
  
except Exception as e:
  print(f"LLM API failed: {e}")

try: 
  data = json.loads(tools)
except json.JSONDecodeError:
  print("Invalid JSON from model")

try:
  file = open("research.txt")
  data = file.read()

except FileNotFoundError:
  print("File not found")

finally:
  print("Cleanup complete")

class RetrievalError(Exception):
  pass

def retrieve_documents():
  raise RetrievalError("Failed to retrieve documents")

try: 
  retrieve_documents()
except FileNotFoundError:
  print("File missing")
except ValueError:
  print("Invalid data")
except Exception as e:
  print(f"Unexpected error: {e}")
except RetrievalError as e:
  print(e)
finally:
  print("Finished!")

vector_db = []

try: 
  docs = vector_db.search(message1)

  response = model.generate(
    query=message1,
    context=docs
  )

except ConnectionError:
  response = "Knowledge base unavailable"

except TimeoutError:
  response = "Request timed out. Please try again."

# ---------------------
# 14. File Reading and Writing
# ---------------------

with open("research.txt", "r") as f:
  prompt = f.read()

response = "This is a generated answer."

with open("research.txt", "w") as f:
  f.write(response)

with open("sumarise.txt", "a") as f:
  f.write("Model run completed\n")

# ---------------------
# 15. Path Handling
# ---------------------

data_path = Path("data") / "train.csv"

prompt_path = Path("prompts") / "sumarise.txt"

with prompt_path.open("r") as f:
  prompt = f.read()

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

output_file = output_dir / "sumarise.txt"

with output_file.open("w") as f:
  f.write("Generated answer from this model.")

# ---------------------
# 16. JSON
# ---------------------

{
  "model": "gpt-3.5",
  "task": "Research Hubspot",
  "priority": "medium",
  "output_format": "summary"
}
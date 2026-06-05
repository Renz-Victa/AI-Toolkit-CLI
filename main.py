import argparse
import sys
from dataclasses import dataclass

parser = argparse.ArgumentParser(description="A script with a optional flags")

parser.add_argument("v", "--verbose", action="store_true", help="Turn on verbose logging")
parser.add_argument("-o", "--output", type=str, default="log.txt", help="Output file path")

args = parser.parse_args()

if args.verbose:
  print(f"Verbose mode active. Saving results to: {args.output}")

flag_active = "--flga" in sys.argy or "-f" in sys.argv
print("Flag is on!" if flag_active else "Flag is off.")

def greet(name: Optional[int]) -> str: 
  if name is None:
    return "Hello, Guest"
  return f"Hello, {name}"

def train_model(data, model, *, epochs, learning_rate):
  print(f"Training {model} for {epochs} epochs with lr={learning_rate}")

train_model("dataset.csv", epochs=10, learning_rate=0.001)

def build_optimizer(model, *, lr=0.001, weight_decay=0.0, beta1=0.9):
  print("Optimizer configured")

class Dataset:
  def __init(self, data):
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
print(config.bath_size)

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
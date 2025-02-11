from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset
import torch

# Step 1: Load the dataset
dataset = load_dataset("glue", "mrpc")

# Step 2: Load the tokenizer and encode the text data
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def tokenize_function(examples):
    return tokenizer(examples["sentence1"], examples["sentence2"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Step 3: Load the model
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# Step 4: Define training arguments
training_args = TrainingArguments(
    output_dir="./model",          # output directory
    evaluation_strategy="epoch",     # evaluation strategy to adopt during training
    learning_rate=2e-5,              # learning rate
    per_device_train_batch_size=16,  # batch size for training
    per_device_eval_batch_size=16,   # batch size for evaluation
    num_train_epochs=3,              # number of training epochs
    weight_decay=0.01,               # strength of weight decay
)

# Step 5: Define the Trainer
trainer = Trainer(
    model=model,                         # the model to be trained
    args=training_args,                  # training arguments
    train_dataset=tokenized_datasets["train"],  # training dataset
    eval_dataset=tokenized_datasets["validation"], # evaluation dataset
)

# Step 6: Train the model
trainer.train()

# Step 7: Evaluate the model
eval_results = trainer.evaluate()
print(eval_results)
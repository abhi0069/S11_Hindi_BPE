from hindi_bpe_implementation import HindiTokenizer

# Initialize tokenizer
tokenizer = HindiTokenizer()

# Example texts
texts = [
    "भारत एक महान देश है",
    "हिंदी भाषा बहुत सुंदर है",
    "नमस्ते दुनिया"
]

# Demonstrate tokenization
for text in texts:
    tokens = tokenizer.encode(text)
    decoded = tokenizer.decode(tokens)
    print(f"\nOriginal: {text}")
    print(f"Tokens: {tokens}")
    print(f"Decoded: {decoded}") 
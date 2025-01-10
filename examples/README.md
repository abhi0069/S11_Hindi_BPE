# Hindi BPE Tokenizer

A byte-pair encoding (BPE) tokenizer optimized for Hindi text, achieving >3.2x compression ratio with a vocabulary size under 5000 tokens.

## Overview
This project implements a byte-pair encoding tokenizer specifically designed for Hindi text. It uses regex-based preprocessing and byte-level BPE to achieve efficient tokenization of Devanagari script.

## Features
- Specialized for Hindi/Devanagari text
- Vocabulary size < 5000 tokens
- Compression ratio > 3.2x
- Unicode-aware tokenization
- Preserves Hindi character combinations

## Statistics
- Vocabulary Size/Token Count: 400
    - Base tokens: 256
    - Merged tokens: 144
- Compression Ratio: 4.05X

## Requirements
- Python 3.6+
- PyTorch
- regex

## License
MIT
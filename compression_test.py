def test_compression(tokenizer, test_text):
    # Original size in bytes
    original_size = len(test_text.encode('utf-8'))
    
    # Tokenized size (each token uses ~2 bytes)
    tokens = tokenizer.encode(test_text)
    tokenized_size = len(tokens) * 2
    
    compression_ratio = original_size / tokenized_size
    return compression_ratio 
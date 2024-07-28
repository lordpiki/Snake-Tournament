import tokenize

# Ignored tokens are new lines, comments, and other irrelevant tokens
ignored_tokens = [tokenize.NEWLINE, tokenize.NL, tokenize.COMMENT, tokenize.ENCODING, tokenize.ENDMARKER]

def count_tokens(file_path):
    with open(file_path, 'rb') as f:
        tokens = list(tokenize.tokenize(f.readline))
    
    # Filter out newlines and other irrelevant tokens
    filtered_tokens = [token for token in tokens if token.type not in ignored_tokens]
    
    token_count = len(filtered_tokens)
    return token_count

file_path = 'Bot.py'  # Replace with your file path
token_count = count_tokens(file_path)
print(f"Number of tokens: {token_count}")

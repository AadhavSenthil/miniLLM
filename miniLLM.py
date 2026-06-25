import sys
import os
import urllib.request
import re
import tiktoken

def tokenizer(file_path):

    with open(file_path, "r") as f:
        raw_text = f.read()

    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = [item.strip().replace(" ","_") for item in preprocessed if item.strip()]
    print(len(preprocessed))
    return preprocessed

def assign_token_id(tokenized_text):
    all_text = sorted(set(tokenized_text))
    print(len(all_text))
    vocab = {token:integer for integer,token in enumerate(all_text) }
    ids = {vocab[token] for token in all_text}
    print(ids)


def decoder(ids):
    token = "5"


def main():

    tokenized_text = tokenizer("the-verdict.txt")
    assign_token_id(tokenized_text)
    return 0



if __name__ == "__main__":
    sys.exit(main())
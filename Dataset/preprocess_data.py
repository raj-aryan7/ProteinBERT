from tape import TAPETokenizer

tokenizer = TAPETokenizer(vocab='iupac')

sequence = "MKVLYNLV"

tokens = tokenizer.encode(sequence)

print("Original sequence:", sequence)
print("Tokenized sequence:", tokens)

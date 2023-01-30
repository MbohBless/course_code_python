import re                                 # for performing regex expressions

tokens = []  
def fmtcharRecog(text):
        new_text = ""
        for i in range(len(text)):
            if re.match(r'\.|,|\'|\)|\}|\]|\:|\;|\=|\>|\+|\#', text[i]):
                new_text = new_text+" "+text[i]+" "
            elif re.match(r'\(|\{|\<|\[|\s', text[i]):
                new_text = new_text+" "+text[i]+" "
            else:
                new_text = new_text+text[i]
        return new_text
 # for string tokens
# turning source code into list of words
source_code = 'int main() { int sum = 0; for (int i = 0; i < 50; i+10) { sum = sum + i; } return sum; }'

data = fmtcharRecog(source_code).split()
# Loop through each source code wordj
for word in data:

    if word in ['str', 'int', 'bool', 'char', 'float', 'double', 'vector','long']:
        tokens.append(['DATATYPE', word])
    elif word in ["auto", "break", "case", "char", "const", "continue", "default", 
      "do", "else", "enum", "extern", "for", "goto", "if","include"
        "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]:
        tokens.append(['KEYWORD', word])

   # This will look for an identifier which would be just a word
    elif re.match("[a-z]", word) or re.match("[A-Z]", word):
        tokens.append(['IDENTIFIER', word])
    # This will look for an operator
    elif word in '*-/+%=':
        tokens.append(['OPERATOR', word])
    elif word in '(){}':
        tokens.append(['BRACKET', word])
    elif word in '#':
        tokens.append(['PREPROCESSOR', word])
    # This will look for integer items and cast them as a number
    elif re.match('\d+', word):
            tokens.append(["INTEGER", word])
    elif word in ';':
        tokens.append(['TERMINATOR', word])

print(data)
print(tokens) 

from pathlib import Path

from botok import WordTokenizer, Text, Config

###########################################
in_str = "ལེ གས། བཀྲ་ཤིས་མཐའི་ ༆ ཤི་བཀྲ་ཤིས་  tr བདེ་་ལེ གས། བཀྲ་ཤིས་བདེ་ལེགས་༡༢༣ཀཀ། མཐའི་རྒྱ་མཚོར་གནས་པའི་ཉས་ཆུ་འཐུང་།། །།མཁའ།"
WT = WordTokenizer()
tokens = WT.tokenize(in_str)

in_str = "ལ་པོ་ལ་པོ་ལ་པོ་"
t = Text(in_str, tok_params={"config": Config()})
tokens = t.tokenize_words_raw_text
tt = Text(
    in_str, tok_params={"config": Config.from_path("./tests/data/trie_dialect_pack")},
)
ttokens = tt.tokenize_words_raw_text
print(tokens)
print(ttokens)
###########################################

#
# ### Extract token-string / POS pairs ########
#
# tagged = ['"{}"/{}'.format(w.text, w.pos) for w in tokens]
# print(', '.join(tagged))
#
#
# ### Extract the cleaned version of the tokens
#
# cleaned = [w.text_cleaned for w in tokens if w.text_cleaned]
# print(' '.join(cleaned))

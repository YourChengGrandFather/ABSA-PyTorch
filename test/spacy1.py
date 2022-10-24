import spacy
import numpy as np
nlp = spacy.load("en_core_web_sm")

# Construction 1
# doc = nlp("Some text i an Beijing ren")
# for token in doc:
#     print(token,token.i)
#     for child in token.children:
#         print('child', child)
# # Construction 2
# from spacy.tokens import Doc

# words = ["hello", "world", "!"]
# spaces = [True, True, False]
# doc = Doc(nlp.vocab, words=words, spaces=spaces)
# print(doc)


# Construction 3
# doc = nlp("Give it back! He pleaded.")
# for token in doc:
#     print('token-->', token)
#     give_children = token.children
#     print('>>>',list(give_children) )
# # print([t.text for t in give_children] == ["it", "back", "!"])

# Construction 4

# def dependency_adj_matrix(text):
#     # https://spacy.io/docs/usage/processing-text
#     tokens = nlp(text)
#     words = text.split()
#     matrix = np.zeros((len(words), len(words))).astype('float32')
#     assert len(words) == len(list(tokens))

#     for token in tokens:
#         print(token.lemma_)
#         matrix[token.i][token.i] = 1
#         for child in token.children:
#             matrix[token.i][child.i] = 1
#             matrix[child.i][token.i] = 1

#     return matrix

# matrix = dependency_adj_matrix('Some text i an Beijing ren')
# print(matrix)

# Construction 5
# def pad_and_truncate(sequence, maxlen, dtype='int64', padding='pre', truncating='pre', value=0):
#     x = (np.ones(maxlen) * value).astype(dtype)
#     if truncating == 'pre':
#         trunc = sequence[-maxlen:]
#     else:
#         trunc = sequence[:maxlen]
#     trunc = np.asarray(trunc, dtype=dtype)
#     if padding == 'post':
#         x[:len(trunc)] = trunc
#     else:
#         x[-len(trunc):] = trunc
#     return x
# sequence = [1,2,3,4,5]
# x = pad_and_truncate(sequence,10)
# print(x)


text = "$T$ I used to have all the records  's broken & set memorized , but now there 's too many to remember . lady $T$ fuck you , you 're too awesome !"
text_left, _, text_right = [s.lower().strip() for s in text.partition("$T$")]

print(text_left)
print(text_right)

print('---------------')
print([s.lower().strip() for s in text.partition("$T$")])
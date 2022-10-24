# def _load_word_vec(path, word2idx=None, embed_dim=25):
#     fin = open(path, 'r', encoding='utf-8', newline='\n', errors='ignore')
#     word_vec = {}
#     for line in fin:
#         tokens = line.rstrip().split()
#         word, vec = ' '.join(tokens[:-embed_dim]), tokens[-embed_dim:]
#         print('word-->', word)
#         print('vec-->', vec )
#         break
#     #     if word in word2idx.keys():
#     #         word_vec[word] = np.asarray(vec, dtype='float32')
#     # return word_vec

# path = '../glove.twitter.27B/glove.twitter.27B.25d.txt'
# _load_word_vec(path)

print([0]*5)

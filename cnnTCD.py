import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
from keras.preprocessing.text import Tokenizer # convert a sentence to a list of strings
from keras.preprocessing.sequence import pad_sequences # all sequences must of same length
from keras.layers import Dense, Input, GlobalMaxPooling1D
from keras.layers import Conv1D, MaxPooling1D, Embedding
from keras.models import Model
from sklearn.metrics import roc_auc_score # area under curve metric (used under binary classification)

# configuration
max_seq_length = 100 #internet comments not more than 100 words/sentence
max_vocab_size = 20000 #if more than 20k words in dataset/ truncate down (native english speaker knows approc 20k word)
embedding_dim = 100 #size of each word vector as pre-trained word vectors come in specific sizes
validation_split = 0.2
batch_size = 128
epochs = 10

#load pre-trained word vectors
print('Loading word vectors..')
word2vec = {}
with open('glove.6B.100d.txt', encoding = 'utf-8') as f:
    for line in f:
        values = line.split()
        word = values[0]
        vec = np.asarray(values[1:], dtype = 'float32')
        word2vec[word] = vec
print('Found 100d word vectors.',  len(word2vec))

# load data (internet comments)
train = pd.read_csv('train.csv')
sentences = train["comment_text"].fillna("Dummy_val").values
possible_labels = ["toxic","severe_toxic","obscene","threat","insult","identity_hate"]
targets = train[possible_labels].values

# convert sentences into strings
tokenizer = Tokenizer(num_words=max_vocab_size)
tokenizer.fit_on_texts(sentences)
sequences = tokenizer.texts_to_sequences(sentences)

# word integer mapping
word2idx = tokenizer.word_index
print('%s unique tokens' % len(word2idx))

data = pad_sequences(sequences, maxlen = max_seq_length)
print('Shape of data tensor', data.shape )

# preparing embedding matrix
num_words = min(max_vocab_size, len(word2idx)+1)
embedding_matrix = np.zeros((num_words, embedding_dim))
for word, i in word2idx.items():
    if i < max_vocab_size:
        embedding_vector = word2vec.get(word)
        if embedding_vector is not None:
            embedding_matrix[i] = embedding_vector

# loading pre-trained word embeddings
embedding_layer = Embedding(num_words,
                            embedding_dim,
                            weights = [embedding_matrix],
                           input_length = max_seq_length,
                           trainable = False)

input_ = Input(shape = (max_seq_length,))
x = embedding_layer(input_)
x = Conv1D(128, 3, activation = 'relu')(x)
x = MaxPooling1D(3)(x)
x = Conv1D(128, 3, activation = 'relu')(x)
x = MaxPooling1D(3)(x)
x = Conv1D(128, 3, activation = 'relu')(x)
x = GlobalMaxPooling1D()(x)
x = Dense(128, activation = 'relu')(x)
output = Dense(len(possible_labels), activation = 'sigmoid')(x)

model = Model(input_, output)
model.compile(
    loss = 'binary_crossentropy',
    optimizer = 'rmsprop',
    metrics = ['accuracy'])
)

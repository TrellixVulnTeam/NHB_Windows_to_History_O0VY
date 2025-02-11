TARGET_SIZE = (299, 299, 3)
TOKENIZER_FILE = './nlp/tokenizer.json'
GLOVE_FILE = './nlp/glove.840B.300d.gensim'
ENCODER_FILE = './nlp/encoder.tf'
DECODER_FILE = './nlp/decoder.tf'
N_VOCABS = 20000
EMBEDDING_DIM = 300  # embedding_matrix.shape[1] # 300 for Glove
UNITS = 512  # GRU hidden vector
VOCAB_SIZE = N_VOCABS + 1  # +1 for <unk>
MAX_LEN = 47

import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

text = "Natural language processing (NLP) is a field of computer science and artificial intelligence concerned with the interactions between computers and human (natural) languages."

# Tokenization
tokens = nltk.word_tokenize(text)
print("===========================================================================================================================================================")
print("Tokenized text:", tokens)

# Stopword removal
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
filtered_text = [word for word in tokens if word.lower() not in stop_words]
print("===========================================================================================================================================================")
print("Filtered text:", filtered_text)

# Stemming
from nltk.stem import PorterStemmer
ps = PorterStemmer()
stemmed_words = [ps.stem(word) for word in filtered_text]
print("===========================================================================================================================================================")
print("Stemmed words:", stemmed_words)
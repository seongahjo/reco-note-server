import gensim
import smart_open
from gensim.models import doc2vec


def read_corpus(fname, tokens_only=False):
    with smart_open.smart_open(fname, encoding="UTF-8") as f:
        for i, line in enumerate(f):
            if tokens_only:
                yield gensim.utils.simple_preprocess(line)
            else:
                yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(line), [i])


def train():

    sentences = list(read_corpus("./file/test.txt"))
    # sentences = doc2vec.TaggedLineDocument("./test.txt")
    doc_vectorizer = doc2vec.Doc2Vec(alpha=0.025, min_alpha=0.025)
    doc_vectorizer.build_vocab(sentences)
    model_file = 'model.model'
    doc_vectorizer.train(sentences, epochs=10, total_examples=doc_vectorizer.corpus_count)
    doc_vectorizer.save(model_file)
    print(len(sentences))
    for doc_id in range(len(sentences)):
        inferred_vector = doc_vectorizer.infer_vector(sentences[doc_id].words)
        sims = doc_vectorizer.docvecs.most_similar([inferred_vector], topn=1)
        print(sims)
        # print(doc_vectorizer.wv.most_similar(u'멀티미디어',topn=5))

if __name__ == "__main__":
    train()

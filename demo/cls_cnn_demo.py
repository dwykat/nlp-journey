from smartnlp.classfication.dl.base_classifier import TextCnnClassifier

if __name__ == '__main__':
    base_classifier = TextCnnClassifier(model_path='./model/cnn/',
                                        config_path='./model/cnn/config.pkl',
                                        train=False,
                                        vector_path='../tutorials/03.poem_generation/data/GoogleNews-vectors-negative300.bin.gz')
    out = base_classifier.predict(
        ['this is very good movie , i want to watch it again!', 'this is very bad movie , i hate it!'])
    out2 = base_classifier.predict('this is very good movie , i want to watch it again!')
    print(out)
    print(out2)

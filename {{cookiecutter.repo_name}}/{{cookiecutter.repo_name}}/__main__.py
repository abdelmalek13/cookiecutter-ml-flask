import logging

import plac
from sklearn.externals import joblib

from {{cookiecutter.repo_name}}.data import read_train_data, read_test_data
from {{cookiecutter.repo_name}}.metrics import benchmark
from {{cookiecutter.repo_name}}.pipeline import preprocess_pipeline, prediction_pipeline

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


def train(training_data, model_path, test_data=None):
    X_train, y_train = read_train_data(training_data, freq_treshold=treshold)

    logging.info("Training on {} examples for {} labels".format(len(X_train), len(set(y_train))))
    logging.info("Starting the training")
    prediction_pipeline.fit(preprocess_pipeline.fit_transform(X_train, y_train), y_train)

    if test_data != None:
        X_test, y_test = read_test_data(test_data, y_train)
        logging.info("Evaluating the model")
        X_test = preprocess_pipeline.transform(X_test)
        benchmark(prediction_pipeline, X_train, y_train, X_test, y_test, verbose=2)

    logging.info("Storing the model")
    joblib.dump(prediction_pipeline, model_path)


if __name__ == "__main__":
    plac.call(train)

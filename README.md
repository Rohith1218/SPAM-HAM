# Spam-Ham Classifier using Support Vector Classifier (SVC)

This project implements a spam-ham classifier using the Support Vector Classifier (SVC) model. The goal is to classify text messages as either spam or ham (non-spam) based on their content. The project utilizes the Spam Ham dataset for training and evaluation.

## Dataset

The dataset used for this project is the Spam Ham dataset, which contains labeled text messages. The dataset can be accessed from the following URL: [Spam Ham Dataset](https://raw.githubusercontent.com/diazoniclabs/Machine-Learning-using-sklearn/master/Datasets/spam.tsv)

## Getting Started

To get started with the project, follow these steps:

1. Install the required dependencies: Python, pandas, scikit-learn (sklearn).

2. Clone the project repository: `git clone <repository_url>`

3. Navigate to the project directory: `cd spam-ham-classifier`

4. Create a virtual environment (optional): `python -m venv env` and activate it: `source env/bin/activate`

5. Install the project dependencies: `pip install -r requirements.txt`

6. Run the project: `python spam_ham_classifier.py`

## Usage

The `spam_ham_classifier.py` script performs the following steps:

1. Loads the Spam Ham dataset from the provided URL.

2. Divides the data into input (text messages) and output (spam/ham labels).

3. Splits the data into training and testing sets using the train_test_split function.

4. Applies TF-IDF vectorization to convert the text messages into numerical features.

5. Trains a Support Vector Classifier (SVC) model on the training data.

6. Predicts the labels for the test data.

7. Calculates and displays the accuracy of the model.

8. Provides the option to evaluate specific messages or custom texts.

## Additional Notes

- The project uses the TfidfVectorizer from scikit-learn to convert text messages into numerical features based on term frequency-inverse document frequency.

- The SVC model is employed for classification, and the accuracy score is used to evaluate its performance.

- The project utilizes a pipeline to combine the TfidfVectorizer and SVC into a single model for ease of use and deployment.

- The trained model can be saved using joblib and loaded for future use.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to explore and modify the code as needed. Contributions are always welcome!


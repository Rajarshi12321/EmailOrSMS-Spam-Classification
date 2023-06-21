# EmailOrSMS-Spam-Classification

Welcome to the EmailOrSMS-Spam-Classification repository! This project focuses on classifying emails and SMS messages as spam or non-spam using machine learning techniques. The goal is to develop a model that can accurately differentiate between spam and legitimate messages.

## Table of Contents

- [EmailOrSMS-Spam-Classification](#emailorsms-spam-classification)
  - [Table of Contents](#table-of-contents)
  - [Background](#background)
  - [Installation](#installation)
  - [Data](#data)
  - [Model](#model)
  - [Results](#results)
  - [Contributing](#contributing)
  - [License](#license)

## Background

Spam messages can be a nuisance and often pose security risks. This project aims to tackle the problem of spam detection by leveraging machine learning algorithms. By training a model on a dataset containing labeled examples of spam and non-spam messages, we can create a predictive model that can classify new, unseen messages.

## Installation

To run this project locally, please follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/Rajarshi12321/EmailOrSMS-Spam-Classification.git

2. Install the required dependencies. We recommend setting up a virtual environment first:
   ```shell
   cd EmailOrSMS-Spam-Classification
   python3 -m venv venv
   source venv/bin/activate

3. Once the dependencies are installed, you're ready to use the project.

## Data
The dataset used for this project is included in the repository. 

* The dataset is in CSV file named "spam.csv".
It contains two columns: "v1" and "v2".
* The v1 column indicates whether the message is spam or non-spam(ham) (0 for non-spam, 1 for spam)..
* The v2 column contains the text of each email or SMS message.

Make sure to checkout our dataset in the data/ directory once.

## Model
The spam classification model is built using a machine learning algorithm. The project provides a basic implementation using a Random Forest Classification (RFC) using CountVecterizer. However, feel free to experiment with different models or algorithms by modifying the code accordingly.

## Results
The results of the model can be evaluated using various performance metrics such as accuracy and precision. These metrics help assess the effectiveness of the spam classification model. RFC (Random Forest Classifier) has got perfect precision with highest accuracy(0.971) using CountVectorizer, so we are choosing to use Random Forest algorithm.

## Contributing
Contributions to this project are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request. Let's work together to enhance the spam classification model and make it more accurate.

## License
This project is licensed under the MIT License. Feel free to modify and distribute it as per the terms of the license.

We hope this README provides you with the necessary information to get started with the EmailOrSMS-Spam-Classification project. If you have any further questions or need assistance, please feel free to reach out to the project owner or contributors. Happy spam detection!
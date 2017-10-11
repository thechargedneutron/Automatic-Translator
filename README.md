# Handwritten-Language-Translator

## Introduction

A simple language translator which takes in strokes of letters and converts the word so formed into a desired language. The translator is based on a Neural Network model which handles the recognition part. Also, MyMemory API is used to recieve a translated version of the original word into the other language.

## Dependencies

* scikit-learn
* translate (MyMemory API)
* Python-Kivy

## Implementation

* Input :- A Python-Kivy GUI takes input and converts it into a numpy array by dividing the box into the number of columns and rows. This can be used to collect dataset as well.

* Training :- The training is done by collecting samples and then using a deep neural network learning from the dataset. The trained estimator is pickled so as to avoid training every single time.

* Prediction :- The prediction is easy once the data is trained. The predicted labels are then converted into appropriate letters, thus forming a word.

* Translation :- The word and the languages are passed as parameters to the API to get the translation in the desired language.

## Demo

<iframe width="420" height="315" src="https://www.youtube.com/embed/KbpMcCN0BSA" frameborder="0" allowfullscreen></iframe>

## Examples


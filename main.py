import textstat
import numpy as np


def read_file_to_string(filename):
  with open(filename, 'r') as file:
    data = file.read()
  return data


def count_outliers(arr):
  q1, q3 = np.percentile(arr, [25, 75])
  iqr = q3 - q1
  lower_bound = q1 - (1.5 * iqr)
  upper_bound = q3 + (1.5 * iqr)
  outliers = [x for x in arr if x < lower_bound or x > upper_bound]
  return len(outliers)


outlier = 50

text = read_file_to_string("Text.txt")
sentences = text.split(' ')

scores = []

for test_data in sentences:
  t = textstat.flesch_reading_ease(test_data)
  scores.append(t)

count = count_outliers(scores)
if count / len(sentences) < 0.1:
  print("probably AI\n")
  print(count / len(sentences))
else:
  print("Probably not AI\n")
  print(count / len(sentences))

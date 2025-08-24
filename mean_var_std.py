import numpy as np

def calculate(list):
 """
  Calculates the mean, variance, standard deviation, max, min, and sum of a 3x3 matrix.

  Args:
    list: A list containing 9 numbers.

  Returns:
    A dictionary containing the calculated statistical values.

  Raises:
    ValueError: If the input list does not contain exactly nine numbers.
  """
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")


  matrix = np.array(list).reshape(3, 3)

  calculations = {
      'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()],
      'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()],
      'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()],
      'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()],
      'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()],
      'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
  }

  return calculations
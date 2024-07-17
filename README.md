# DataAnalysis072024

Python examples for Data Analysis, now with a commit from Willem's laptop.

## Libraries

This section contains the most important libraries we'll cover in this training.

- [NumPy: Numerical Python](#numpy)
- [Pandas](#pandas)
- [Scikit-learn](#scikit-learn)
- [Matplotlib](#data-visualisation)

### NumPy

NumPy stands for **Num**erical **Py**thon. It is the base for libraries such as Pandas and SciPy and is 
most famous for its fast numerical computations using vectors and matrices.

- [Official docs](https://numpy.org/)
- [100 NumPy exercises](https://github.com/rougier/numpy-100)

### Pandas

Pandas is the standard for representing datasets in Python, working with two new datatypes: the Series and 
the DataFrame.

- [Official docs](https://pandas.pydata.org/)
- [Pandas Cookbook](https://github.com/jvns/pandas-cookbook)
- [Practice Pandas on Kaggle](https://www.kaggle.com/learn/pandas)
- [Comparison with SAS](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html)

### Data Visualisation

Data visualization is usually done with either matplotlib or Seaborn. Matplotlib is a library from MATlab, which 
Seaborn extends. Generally, Seaborn figures are more aesthetically appealing and more user-friendly to generate.

- [Matplotlib documentation](https://matplotlib.org/)
- [Seaborn documentation](https://seaborn.pydata.org/)

### Scikit-learn

Scikit-learn is a machine learning toolkit.

- [Official docs](https://scikit-learn.org/stable/index.html)

## Books

### Python Data Science Handbook

The book ["Python Data Science Handbook"](https://jakevdp.github.io/PythonDataScienceHandbook/) by Jake Vanderplas 
is one of the most popular sources for data analysis. It was published by O'Reilly and is freely available. 
There are also several [code examples](https://github.com/jakevdp/PythonDataScienceHandbook) on the corresponding 
GitHub page.

### Hands-on Machine Learning with scikit-learn, Tensorflow and Keras

The book ["Hands-on Machine Learning with scikit-learn, Tensorflow and Keras"](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)
(available for free through trial). This is a more advanced book we'll be covering in the Machine Learning training. There is also a 
GitHub repo with [code examples](https://github.com/ageron/handson-ml3?tab=readme-ov-file) for this book.

### Free Programming Books Repository

[Free Programming book repository on GitHub](https://github.com/EbookFoundation/free-programming-books/blob/main/books/free-programming-books-subjects.md)

## Datasets

### Practice Datasets

The easiest way is to use pre-existing datasets from major libraries such as scikit-learn, fairlearn or seaborn. We can 
directly import these in Python to learn from.

```python
# Convention to import seaborn. 
import seaborn as sns

sns.load_dataset('penguins')
```

- [Load dataset documentation](https://seaborn.pydata.org/generated/seaborn.load_dataset.html)
- [Available sets on GitHub](https://github.com/mwaskom/seaborn-data)

### Importing Datasets

[Kaggle.com](https://www.kaggle.com) offers a wide variety of datasets, also indicating a usability score per dataset. 
Another great source is [HuggingFace](https://huggingface.co/datasets). You can download any dataset and import it 
using a suitable I/O library.

## Contact

Any questions? You can e-mail me at selina.blijleven@code-cafe.nl.
# DataAnalysis072024

Python examples for Data Analysis

## Libraries

This section contains the most important libraries we'll cover in this training.

### Data Science

- [NumPy: Numerical Python]()
- [Pandas]()
- [Scikit-learn]()
- [Matplotlib & Seaborn]()

### Other important libraries

- [requests](https://libraries.io/pypi/requests): for HTTP requests to any webpage
- [csv](): for reading CSV files (we can also do this with Pandas)
- [json](): for working with json data
- [typing](https://pypi.org/project/typing/): for type hinting in Python (including things like Optional types)

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
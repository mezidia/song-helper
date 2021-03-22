#Custom transformer using spaCy
from sklearn.base import TransformerMixin


class Predictors(TransformerMixin):
    """[summary]

    Args:
        TransformerMixin ([type]): [description]
    """
    def transform(self, X, **transform_params):
        return [self.clean_text(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}

    # Basic function to clean the text
    def clean_text(self, text):
        return text.strip().lower()

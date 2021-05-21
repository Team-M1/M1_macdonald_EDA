import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class McDonald:
    def __init__(self):
        self.data = pd.read_csv("./menu.csv")
        
    def head(self) -> pd.DataFrame:
        self.data.head(5)
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class McDonald:
    def __init__(self):
        self.data = pd.read_csv("./menu.csv")
        
    def head(self) -> pd.DataFrame:
        self.data.head(5)

    @st.cache
    def CPF_and_calories_relationship_graph(self):
        fig, ax = plt.subplots(1, 3, sharey=True, figsize=(15, 5))
        x = ["Carbohydrates", "Protein", "Total Fat"]
        for i in range(3):
            sns.regplot(x=x[i], y="Calories", data=self.data, ax=ax[i])
        st.pyplot(fig)

    @st.cache
    def weight_and_calories_relationship_graph(self):
        size_calories_data = self.data[["Serving Size", "Calories", "Item"]]
        idx = (
            size_calories_data["Serving Size"].str.contains("cup").map(lambda x: not x)
        )
        size_calories_data = size_calories_data.loc[idx, :]
        size_calories_data["gram"] = (
            size_calories_data["Serving Size"].apply(lambda x: x.split("(")[-1][:3]).astype(float)
        )
        dfX = size_calories_data["gram"]
        dfy = size_calories_data["Calories"]

        fig, ax = plt.subplots()
        sns.regplot(x=dfX, y=dfy)
        st.pyplot(fig)
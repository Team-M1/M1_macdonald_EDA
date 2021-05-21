import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class McDonald:
    def __init__(self):
        self.data = pd.read_csv("./menu.csv")

    def head(self) -> pd.DataFrame:
        self.data.head(5)

    @st.cache
    def fig1(self, title=True):
        if title:
            st.title("탄수화물, 단백질, 지방과 칼로리의 관계")
        fig, ax = plt.subplots(1, 3, sharey=True, figsize=(15, 5))
        x = ["Carbohydrates", "Protein", "Total Fat"]
        for i in range(3):
            sns.regplot(x=x[i], y="Calories", data=self.data, ax=ax[i])
        st.pyplot(fig)

    @st.cache
    def fig2(self, title=True, contents=True):
        size_calories_data = self.data[["Serving Size", "Calories", "Item"]]
        idx = (
            size_calories_data["Serving Size"].str.contains("cup").map(lambda x: not x)
        )
        size_calories_data = size_calories_data.loc[idx, :]
        size_calories_data["gram"] = (
            size_calories_data["Serving Size"]
            .apply(lambda x: x.split("(")[-1][:3])
            .astype(float)
        )
        dfX = size_calories_data["gram"]
        dfy = size_calories_data["Calories"]

        if title:
            st.title("메뉴의 gram수와 칼로리와의 상관관계")

        fig, ax = plt.subplots()
        sns.regplot(x=dfX, y=dfy)
        st.pyplot(fig)

        if contents:
            st.write("음식의 gram수와 칼로리의 상관계수는 0.920")


if __name__ == "__main__":
    mcdonald = McDonald()
    mcdonald.fig1()
    mcdonald.fig2()

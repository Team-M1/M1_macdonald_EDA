import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(page_title='McDonald EDA', page_icon = "https://img.icons8.com/color/452/mcdonalds.png", layout = 'wide', initial_sidebar_state = 'expanded')


class McDonald:
    def __init__(self):
        self.data = pd.read_csv("./menu.csv")
        
    def head(self) -> pd.DataFrame:
        return self.data.head(5)

    def CPF_and_calories_relationship_graph(self):
        fig, ax = plt.subplots(1, 3, sharey=True, figsize=(15, 5))
        x = ["Carbohydrates", "Protein", "Total Fat"]
        for i in range(3):
            sns.regplot(x=x[i], y="Calories", data=self.data, ax=ax[i])
        st.pyplot(fig)

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
    
    def all_categories(self):
        new_data = self.data.groupby('Category').mean()
        new_data = new_data[['Calories', 'Carbohydrates', 'Protein', 'Total Fat', 'Cholesterol', 'Sodium', 'Sugars']]
        fig, ax = plt.subplots(len(new_data.columns),1, figsize=(16, 30))
        for i in range(len(ax)):
            sns.barplot(x=new_data.index, y=new_data.columns[i], data=new_data, ax=ax[i])
        st.pyplot(fig)


def sidebar():
    with st.sidebar:
        st.image(
            "https://img.icons8.com/color/452/mcdonalds.png",
            width=300,
        )
        st.markdown("# Mcdonald EDA")
        st.markdown("## 맥도날드 데이터셋을 사용한 EDA 프로젝트")
        st.markdown("[Github Repo](https://github.com/Team-M1/M1_macdonald_EDA)")


def main():
    mcdonald = McDonald()

    st.markdown("# Mcdonald EDA")

    st.dataframe(mcdonald.head())
    mcdonald.CPF_and_calories_relationship_graph()

if __name__ == "__main__":
    sidebar()
    main()
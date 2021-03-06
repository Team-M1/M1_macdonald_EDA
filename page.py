import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


st.set_page_config(page_title='McDonald EDA', page_icon = "https://img.icons8.com/color/452/mcdonalds.png", layout = 'wide', initial_sidebar_state = 'expanded')


class McDonald:
    def __init__(self):
        self.data = pd.read_csv("./menu.csv")
    
    @st.cache
    def head(self) -> pd.DataFrame:
        return self.data.head(5)

    @st.cache(hash_funcs={matplotlib.figure.Figure: hash}, suppress_st_warning=True)
    def CPF_and_calories_relationship(self):
        fig, ax = plt.subplots(1, 3, sharey=True, figsize=(15, 5))
        x = ["Carbohydrates", "Protein", "Total Fat"]
        for i in range(3):
            sns.regplot(x=x[i], y="Calories", data=self.data, ax=ax[i])
        
        return fig
        #plt.savefig('CPF_and_calories_relationship.png')
    
    @st.cache(hash_funcs={matplotlib.figure.Figure: hash}, suppress_st_warning=True)
    def all_categories(self):
        new_data = self.data.groupby('Category').mean()
        new_data = new_data[['Calories', 'Carbohydrates', 'Protein', 'Total Fat', 'Cholesterol', 'Sodium', 'Sugars']]
        fig, ax = plt.subplots(len(new_data.columns), 1, figsize=(16, 30))
        for i in range(len(ax)):
            sns.barplot(x=new_data.index, y=new_data.columns[i], data=new_data, ax=ax[i])
        
        return fig
        #plt.savefig('all_categories.png')
    
    @st.cache(hash_funcs={matplotlib.figure.Figure: hash}, suppress_st_warning=True)
    def fat_relationship_sum(self):
        fig, ax = plt.subplots(figsize=(8,8))
        sns.scatterplot(x='Saturated Fat', y='Total Fat', hue='Trans Fat', s=100, data=self.data)
        
        return fig
        #plt.savefig('fat_relationship_sum.png')
    
    @st.cache(hash_funcs={matplotlib.figure.Figure: hash}, suppress_st_warning=True)
    def fat_relationship_sep(self):
        fig = plt.figure(figsize=(16,8))
        ax1 = fig.add_subplot(1, 2, 1)
        ax2 = fig.add_subplot(1, 2, 2)
        x = self.data['Saturated Fat']
        x_p= self.data['Trans Fat']
        y = self.data['Total Fat']
        ax1.scatter(x, y)
        ax1.set_title('Total Fat and Saturated Fat Relationship')
        ax1.set_xlabel('Saturated Fat')
        ax1.set_ylabel('Total Fat')
        ax2.scatter(x_p, y)
        ax2.set_title('Total Fat and Trans Fat Relationship')
        ax2.set_xlabel('Trans Fat')
        ax2.set_ylabel('Total Fat')
        
        return fig
        #plt.savefig('fat_relationship_sep.png')
    
    @st.cache(hash_funcs={matplotlib.figure.Figure: hash}, suppress_st_warning=True)
    def heatmap(self):
        fig, ax = plt.subplots()
        sns.heatmap(self.data.corr())

        return fig
        #plt.savefig('heatmap.png')


mcdonald = McDonald()


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
    st.markdown("# Mcdonald EDA")
    st.markdown("맥도날드 데이터셋을 사용하여 분석한 EDA 프로젝트 코드입니다.")

    st.markdown("## head 로 빠르게 살펴보기")
    st.dataframe(mcdonald.head())

    st.markdown("## 히트맵")
    st.pyplot(mcdonald.heatmap())

    st.markdown("## 카테고리별 비교")
    st.pyplot(mcdonald.all_categories())
    st.markdown("`Smoothies & Shakes` 메뉴의 탄수화물, 당류가 높게 나타났다. (당류의 경우 압도적으로 높게 나타났다.)")
    st.markdown("`Breakfast` 메뉴의 콜레스테롤이 높게 나타났다.")
    st.markdown("`Beef & Pork`, `Breakfast`, `Chicken & Fish` 메뉴들은 대체로 영양성분이 비슷했다.")

    st.markdown("## 칼로리와 탄단지의 전반적인 상관관계")
    st.pyplot(mcdonald.CPF_and_calories_relationship())

    st.markdown("## Total Fat은 Saturated Fat 과 Trans Fat과 관련성이 있는가?\n- 가정 : Saturated Fat 과 Trans Fat 모두 지방이므로 전체 지방 미치는 영향이 비슷할 것이다.")
    st.pyplot(mcdonald.fat_relationship_sep())
    st.pyplot(mcdonald.fat_relationship_sum())
    st.markdown("Total Fat은 Saturated Fat과 관계도는 0.847 정도로 관계성이 높으나, Trans Fat 과의 관계성은 0.434 정도로 생각보다 낮은 경향을 보였다.")

if __name__ == "__main__":
    sidebar()
    main()
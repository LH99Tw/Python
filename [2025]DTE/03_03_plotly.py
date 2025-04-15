import plotly.express as px
df = px.data.iris()     # iris는 판다스 데이터프레임
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()

fig = px.parallel_coordinates(df, color="species_id", 
                labels={"species_id": "Species",
                "sepal_width": "Sepal Width",          "sepal_length": "Sepal Length",
                "petal_width": "Petal Width",             "petal_length": "Petal Length", },
                color_continuous_scale=px.colors.diverging.Tealrose,
                color_continuous_midpoint=2)
fig.show()

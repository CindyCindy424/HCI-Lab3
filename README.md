## Lab3 - Data Visualization

> 1850477 邓欣凌

### 0. Project Development 

#### 0.1 Development Environment

- Windows
- Python
- PyCharm

#### 0.2 How to run

Open file `dashboard.py` in the original submitted folder, run the script and open the local browser for http://127.0.0.1:8050/ and you will see the project as is shown in the following Figure.

```
Project Structure


```



![image-20210624175714585](C:\Users\Cindy Deng\AppData\Roaming\Typora\typora-user-images\image-20210624175714585.png)





### 1. Dataset Overview

I chose the second dataset provided in this assignment, which is about the apps in Google Play Store, to conduct my experiments for data visualization. 

The dataset is stored in a csv file named `googleplaystore.csv`. It contains detailed features for the apps in the google play store. Figure 2 shows the detailed structure of `googleplaystore.csv`.

The dataset contains information about the ratings, installs and the number of reviews and etc., which serves as a definitely great raw material for the data analysts to reveal shocking truth and drive the app-making businesses to success.

<img src="C:\Users\Cindy Deng\AppData\Roaming\Typora\typora-user-images\image-20210624154250807.png" alt="image-20210624154250807" style="zoom:50%;" />

*Figure 2. Structure visualization of the dataset*



### 2. Data Pre-processing

To better display the data processing and reveal more hidden information, I wrote a python script and did a data pre-processing before the following tasks.

The result is stored in the file `./dataset/googleplaystore-byrating.csv`.

<img src="C:\Users\Cindy Deng\AppData\Roaming\Typora\typora-user-images\image-20210624175037626.png" alt="image-20210624175037626" style="zoom: 50%;" />



### 3. Visualization Tasks

Based on a thorough estimation on the dataset, I decide to explore some specific relationship between some of the features provided in the dataset.

#### 3.1 Installation Numbers & Rating Results 

##### (1) Design Concepts

 This task is aimed to explore the relationship between `Review Numbers` and `Rating Results` affecting by the `Type` and ` Category`.

In this way, I design to take `Reviews` as the independent variable while taking `Rating` as the dependent variable of the axes. From the raw data shown above, we could tell that there are lots of possible features affecting the relationship between review numbers and rating results. Therefore, I need to design a interactive interface and show the possible relationship. 

##### (2) Implementation

![image-20210624161323880](C:\Users\Cindy Deng\AppData\Roaming\Typora\typora-user-images\image-20210624161323880.png)

Here I choose a scatter chart as the representation method. The users are allowed to choose a certain App category from the dropdown list and see the details about Reviews and Ratings. The color of the bubbles represents the difference of charges. The light purple bubble represents the Free of Charge Apps while the red one stands for the Paid ones.

1. Dropdown list 

   <img src="C:\Users\Cindy Deng\AppData\Roaming\Typora\typora-user-images\image-20210624161922842.png" alt="image-20210624161922842" style="zoom: 25%;" />

2. Type representation

   <img src="C:\Users\Cindy Deng\AppData\Roaming\Typora\typora-user-images\image-20210624161947743.png" alt="image-20210624161947743" style="zoom:25%;" />

##### (3) Key Functions

```python
@app.callback(
    Output('graph1', 'figure'),
    Input('category', 'value'))
def update_figure(selected_category):
    filtered_df = df[df['Category'] == selected_category]
    fig = px.scatter(filtered_df, x="Reviews", y="Rating",
                     size="Reviews", color="Type", hover_name="App",
                     size_max=100)
    fig.update_layout(transition_duration=500)
    return fig
```



#### 3.2 Category & Numbers of Apps

##### (1) Design Concepts

In this sub-task, I want to reveal the [quantity]() and [quality]() of different types of apps. In other words, I will research on the relationship between `Category`, `Numbers of Apps`  and `Rating Range`.

✨Attention：

To successfully and efficiently implement this idea, I pre-process the given dataset and generate a auxiliary table stored in `/dataset/googleplaystore-byrating.csv`, which has already been covered in the second part of my report.

##### (2) Implementations

![image-20210624162956462](C:\Users\Cindy Deng\AppData\Roaming\Typora\typora-user-images\image-20210624162956462.png)



For this task, I choose to implement [a bar chart with wide format data](). Wide-form data has one row per value of one of the first variable, and one column per value of the second variable. This is suitable for storing and displaying 2-dimensional data. In this case, the 2 variables are `Category` and `Rating Range` respectively.

##### (3) Key Functions

```python
@app.callback(
    Output('graph2', 'figure'),
    Input('category', 'value'))
def update_figure2(selected_category):
    fig = px.bar(df2, x='Category', y='Number of Apps', color='Rating Range', pattern_shape='Rating Range',
                 pattern_shape_sequence=[".", "x", "+"])
    return fig
```

 

#### 3.3 Content Rating & Reviews

##### (1) Design Concepts

Here I would like to examine the relationship between the sum of `Reviews `  and `Content Rating `for both Free of charge type or payment-needed type.

##### (2) Implementations

![image-20210624165104215](C:\Users\Cindy Deng\AppData\Roaming\Typora\typora-user-images\image-20210624165104215.png)

Here we choose a bar chart to represent the relationship. Due to the enormous data imbalance, the box plot on the top isn't showing the normal form.

##### (3) Key Functions

```python
@app.callback(
    Output("graph3", "figure"),
    [Input("dist-marginal", "value")])
def display_graph(marginal):
    fig = px.histogram(
        df, x="Content Rating", y="Reviews", color="Type",
        marginal=marginal,
        hover_data=df.columns)

    return fig
```

#### 3.4 Proportion of different app types

##### (1) Design Concepts

This task is design to show **market share** of different types of apps.

##### (2) Implementations

![image-20210624171744641](C:\Users\Cindy Deng\AppData\Roaming\Typora\typora-user-images\image-20210624171744641.png)

Here I choose to implement a [pie-chart]() to show the market share of each type of apps. The full list of App Category is shown on the right.

##### (3) Key Functions

```python
dcc.Graph(id="pie-chart",
              figure=px.pie(df2, values='Number of Apps', names='Category', title='Proportion of different app types'))
```





#### 3.5 Category & Number of Apps & Rating Range

##### (1) Design Concepts

This task is design to show the relationship between `Category`, `Numbers of Apps`  and `Rating Range`, which is of the same objective as task2. The difference is that here I try to deploy the result using another kind of graphical representation.

##### (2) Implementations

![image-20210624172009803](C:\Users\Cindy Deng\AppData\Roaming\Typora\typora-user-images\image-20210624172009803.png)

Here I use a [wind rose graphic](), a.k.a. [polar bar chart](), the feature representations are as follows:

- Radius: Number of Apps of certain Category
- Theta: different Category of Apps
- Color: Rating Range



##### (3) Key Functions

```python
dcc.Graph(id='graph5',
              figure=px.bar_polar(df2, r='Number of Apps', theta='Category', color='Rating Range', color_discrete_sequence=px.colors.sequential.Plasma_r))
```



### 4. Information revealed

| Visualization ID | Information revealed                                         |
| ---------------- | ------------------------------------------------------------ |
| 1                | ① Apps with low ratings usually don't have much reviews      |
|                  | ② Apps with the most reviews don't usually have the highest score yet a relatively high rating |
|                  | ③ There's no significant difference in the abstract results between different categories |
| 2                | ① For each category, medium rating(4.0~4.5) are always of the most proportion |
|                  | ② Family type of Apps are of the biggest number in the market, followed by the Game type |
| 3                | ① Apps available to everyone are of the most proportion in market |
|                  | ② Free Apps far outrange the Paid Apps                       |
| 4                | ① The detailed proportion of different type of Apps (already shown in the chart) |
| 5                | ① Family Type of Apps, Game Type and Tools Type are the largest number of Apps on the market. |
|                  | ② Apps with medium ratings(4.0~4.5) are most common and of the largest number. |






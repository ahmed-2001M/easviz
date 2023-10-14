import nbformat as nbf
import pandas as pd

def generate(notebook_path, dataset_path):
    # Create a new Jupyter Notebook
    nb = nbf.v4.new_notebook()
    df = pd.read_csv(dataset_path)

    # Markdown cell with a title
    title_cell = nbf.v4.new_markdown_cell("# Data Analysis Notebook")
    nb.cells.append(title_cell)

    nb.cells.append(nbf.v4.new_code_cell(
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
import os
warnings.filterwarnings('ignore')
%matplotlib inline
from IPython.display import Markdown
    """
    ))


    nb.cells.append(nbf.v4.new_code_cell(
"""

def theme1():
    plt.style.use('seaborn-v0_8-whitegrid')
    custom_params = {
        'figure.figsize': (15, 6),
        'font.size': 16,
        'font.weight': 'bold',
        'axes.titlesize': 20,
        'axes.labelsize': 18,
        'xtick.labelsize': 14,
        'ytick.labelsize': 14,
        'axes.spines.top': False,
        'axes.spines.right':False,

    }
    plt.rcParams.update(custom_params)
    sns.set_palette(["#c7522a","#fbf2c4","#008585", "#003f5c", "#58508d", "#ffa600" , "#660e60","#6c584c"])
    
    
def theme2():
    plt.style.use('seaborn-v0_8-dark-palette')
    custom_params = {
        'figure.figsize': (15, 6),
        'font.size': 16,
        'font.weight': 'bold',
        'axes.titlesize': 20,
        'axes.labelsize': 18,
        'xtick.labelsize': 14,
        'ytick.labelsize': 14,
        'axes.spines.top': False,
        'axes.spines.right':False,
    }
    plt.rcParams.update(custom_params)
    sns.set_palette(["#c7522a","#fbf2c4","#008585", "#003f5c", "#58508d", "#ffa600", "#660e60","#6c584c"])
theme1()



def doughnuts(data):
    # Create a pieplot
    plt.pie(x= data.values , labels=data.index , autopct='%.2f%%',shadow=True , startangle=90)
    plt.axis('equal')
    # plt.legend(loc='upper right')
    # add a circle at the center to transform it in a donut chart
    my_circle=plt.Circle( (0,0), 0.7, color='white')
    p=plt.gcf()
    p.gca().add_artist(my_circle)

    return p




    """
    ))

    nb.cells.append(nbf.v4.new_code_cell(f"""df = pd.read_csv(r'{dataset_path}')"""))
    nb.cells.append(nbf.v4.new_code_cell("""df.head()"""))
    nb.cells.append(nbf.v4.new_code_cell("""df.info()"""))
    nb.cells.append(nbf.v4.new_code_cell("""df.describe()"""))
    nb.cells.append(nbf.v4.new_code_cell("""
    
def null_percent(col):
    percentage = round(col.isnull().sum()/len(col)*100,2)
    if percentage > 0:
        print(f'{col.name}==>{percentage} |', end=' ')
print('+'*46)
df.apply(null_percent)
print()
print('+'*46)
fig, ax = plt.subplots(figsize=(15, 7))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False)


    """))

    

    # Markdown cell with an analysis section
    nb.cells.append(nbf.v4.new_markdown_cell("## Univariate Analysis"))



    numerical = []
    categorical = []
    numerical_with_errors = []

    for feature in df.columns:
        if (df[feature].dtype == 'O') & (df[feature].nunique() > 50):
            numerical_with_errors.append(feature)
        elif df[feature].dtype == 'O':
            categorical.append(feature)
        else:
            numerical.append(feature)
    

    nb.cells.append(nbf.v4.new_markdown_cell("## Numerical Features"))
    for feature in numerical:
        nb.cells.append(nbf.v4.new_markdown_cell(f"> {feature}"))
        nb.cells.append(nbf.v4.new_code_cell(f"""df['{feature}'].describe()"""))
        nb.cells.append(nbf.v4.new_code_cell(f"""
fig,ax = plt.subplot_mosaic([['hist','hist','box']])
sns.histplot(data=df, x='{feature}', bins=30, kde=True, ax=ax['hist'])
sns.boxplot(df['{feature}'],ax=ax['box'])
plt.title('{feature} Histogram')
plt.show()
        """))



    nb.cells.append(nbf.v4.new_markdown_cell("## Categorical Features"))
    for feature in categorical:
        nb.cells.append(nbf.v4.new_markdown_cell(f"> {feature}"))
        nb.cells.append(nbf.v4.new_code_cell(f"""df['{feature}'].describe()"""))
        nb.cells.append(nbf.v4.new_code_cell(f"""
fig,ax = plt.subplot_mosaic([['hist','hist','doughnut']])
g= df['{feature}'].value_counts()
sns.barplot(x=g.index , y=g.values, ax=ax['hist'])
ax['doughnut']=doughnuts(g)
plt.show()

        """))





    nb.cells.append(nbf.v4.new_markdown_cell("## Numerical Features With Errors"))
    for feature in numerical_with_errors:
        nb.cells.append(nbf.v4.new_markdown_cell(f"> {feature}"))
        nb.cells.append(nbf.v4.new_code_cell(f"""df['{feature}'].describe()"""))
        nb.cells.append(nbf.v4.new_code_cell(f"""df['{feature}'].unique()"""))










    # cells = []
    # for feature in df.columns:
    #     nb.cells.append(nbf.v4.new_markdown_cell(f"> {feature}"))
    #     nb.cells.append(nbf.v4.new_code_cell("""df.describe()"""))
        



    # # Example analysis code cell (you can add more)
    # code_cell_analysis = nbf.v4.new_code_cell(
    #     "# Add your data analysis code here"
    # )
    # nb.cells.append(code_cell_analysis)

    # Save the notebook to the specified path
    with open(notebook_path, 'w') as f:
        nbf.write(nb, f)














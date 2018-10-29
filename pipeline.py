import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def acquire():
    data = pd.read_csv('./data/vehicles.csv')
    return data

def wrangle(data, year):
    return data[data['Year']==year]

def analyze(filtered):
    grouped = filtered.groupby('Make').agg({'Combined MPG':'mean'}).reset_index()
    results = grouped.sort_values('Combined MPG', ascending=False).head(10)
    return results

## Data reporting
def save_visualize(pepe, title):
    fig, ax = plt.subplots(figsize=(15,8))
    barchart = sns.barplot(data=pepe, x='Make', y='Combined MPG')
    plt.title(title + "\n", fontsize=16)
    fig = barchart.get_figure()
    fig.savefig(title + '.png')


if __name__ == '__main__':
    year = int(input('Enter the year: '))
    title = 'Top 10 Manufacturers by Fuel Efficiency ' + str(year)
    data = acquire()
    filtered = wrangle(data, year)
    results = analyze(filtered)
    save_visualize(results, title)

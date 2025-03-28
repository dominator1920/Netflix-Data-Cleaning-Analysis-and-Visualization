# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


# %%
data = pd.read_csv(r"C:\Users\Kshit\Desktop\Data analysis\project data set\netflix1.csv")


# %%
print(data.head())

# %%
data.columns

# %%
print(data.isnull().sum())


# %%
data.drop_duplicates(inplace=True)


# %%
data.dropna(subset=['director','country'],inplace=True)

# %%
data['date_added'] = pd.to_datetime(data['date_added'])

# %%
print(data.dtypes)

# %%
# Count the number of Movies and TV Shows

# %%
type_counts = data['type'].value_counts()

# %%
plt.figure(figsize=(8, 6))
sns.barplot(x=type_counts.index, y=type_counts.values,
palette='Set2')
plt.title('Distribution of Content by Type')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# %%
data['genres'] = data['listed_in'].apply(lambda x: x.split(','))
all_genres = sum(data['genres'], [])
genre_counts = pd.Series(all_genres).value_counts().head(10)

# %%
# Plot the most common genres

# %%
plt.figure(figsize=(10, 6))
sns.barplot(x=genre_counts.values, y=genre_counts.index,palette='Set3')
plt.title('Most Common Genres on Netflix')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.show()


# %%
data['year_added'] = data['date_added'].dt.year
data['month_added'] = data['date_added'].dt.month

# %%
# Plot content added over the years

# %%
plt.figure(figsize=(12, 6))
sns.countplot(x='year_added', data=data, palette='coolwarm')
plt.title('Content Added Over Time')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()


# %%
# Count titles by director

# %%
top_directors = data['director'].value_counts().head(10)

# %%
top_directors

# %%
plt.figure(figsize=(10, 6))
sns.barplot(x=top_directors.values, y=top_directors.index,
palette='Blues_d')
plt.title('Top 10 Directors with the Most Titles')
plt.xlabel('Number of Titles')
plt.ylabel('Director')
plt.show()


# %%
# Generate word cloud


# %%
movie_titles = data[data['type'] == 'Movie']['title']
wordcloud = WordCloud(width=800, height=400,
background_color='black').generate(' '.join(movie_titles))

# %%
# Plot word cloud

# %%
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()



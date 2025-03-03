# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 15:49:25 2025

@author: vs981
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 14:29:11 2025

@author: vs981
"""

# -*- coding: utf-8 -*-
"""
Netflix Dataset Analysis Report
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:\\Users\\vs981\\Downloads\\netflix_titles.csv\\netflix_titles.csv")

# Data Cleaning
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['country'].fillna('Unknown', inplace=True)
df['rating'].fillna('Not Rated', inplace=True)
df['year_added'] = df['date_added'].dt.year

# Split cast members into separate rows
df_cast = df.dropna(subset=['cast']).copy()
df_cast['cast'] = df_cast['cast'].str.split(', ')
df_cast = df_cast.explode('cast')
df_cast['cast'] = df_cast['cast'].str.strip()

# Split 'listed_in' into genres
df['genre'] = df['listed_in'].str.split(', ')
df_genre = df.explode('genre')
df_genre['genre'] = df_genre['genre'].str.strip()
top_genres = df_genre['genre'].value_counts().head(6).index
df_genre = df_genre[df_genre['genre'].isin(top_genres)]
df_genre_year = df_genre.groupby(['release_year', 'genre']).size().reset_index(name='count')
df_genre_year = df_genre_year[df_genre_year['release_year'] >= 2010]
df_genre_pivot = df_genre_year.pivot(index='release_year', columns='genre', values='count').fillna(0)

# Summary Statistics
type_counts = df['type'].value_counts()
top_countries = df['country'].value_counts().head(10)
content_per_year = df['year_added'].value_counts().sort_index()
rating_counts = df['rating'].value_counts().head(10)

# Rating vs Release Year Preparation
df_clean = df.dropna(subset=['release_year'])
df_rating_year = df_clean.groupby(['release_year', 'rating']).size().reset_index(name='count')
df_rating_year = df_rating_year[df_rating_year['rating'].isin(df_rating_year['rating'].value_counts().head(6).index)]
df_rating_year = df_rating_year[df_rating_year['release_year'] >= 2010]
df_pivot = df_rating_year.pivot(index='release_year', columns='rating', values='count').fillna(0)

# Cast vs Release Year Preparation
df_cast_year = df_cast.groupby(['release_year', 'cast']).size().reset_index(name='count')
top_cast_names = df_cast['cast'].value_counts().head(6).index
df_cast_year = df_cast_year[df_cast_year['cast'].isin(top_cast_names)]
df_cast_year = df_cast_year[df_cast_year['release_year'] >= 2010]
df_cast_pivot = df_cast_year.pivot(index='release_year', columns='cast', values='count').fillna(0)

# Top Cast Members by Number of Movies
top_cast = df_cast['cast'].value_counts().head(10)

# Most Recent Year Genre Distribution
most_recent_year = df['year_added'].max()
df_recent_genre = df_genre[df_genre['year_added'] == most_recent_year]
recent_genre_counts = df_recent_genre['genre'].value_counts()

# Plotting All Visualizations in a Single Column Layout
fig, axes = plt.subplots(9, 1, figsize=(14, 54))
fig.suptitle("Netflix Dataset Analysis", fontsize=20)

# Plot 1: Movies vs TV Shows
sns.barplot(x=type_counts.index, y=type_counts.values, ax=axes[0], palette='viridis')
axes[0].set_title("Number of Movies vs TV Shows")
axes[0].set_ylabel("Count")

# Plot 2: Top 10 Countries with Most Content
sns.barplot(x=top_countries.values, y=top_countries.index, ax=axes[1], palette='coolwarm')
axes[1].set_title("Top 10 Countries with Most Content")

# Plot 3: Content Added Over the Years
content_per_year.plot(kind='line', ax=axes[2], color='purple', marker='o')
axes[2].set_title("Content Added Over the Years")
axes[2].set_ylabel("Count")

# Plot 4: Top 10 Ratings
sns.barplot(x=rating_counts.values, y=rating_counts.index, ax=axes[3], palette='magma')
axes[3].set_title("Top 10 Ratings")

# Plot 5: Rating vs Release Year (Top 6 Ratings)
df_pivot.plot(kind='line', ax=axes[4], linewidth=2, colormap='tab10')
axes[4].set_title("Rating vs Release Year (Top 6 Ratings)")
axes[4].set_xlabel("Release Year")
axes[4].set_ylabel("Count")
axes[4].legend(title='Rating', loc='upper left')

# Plot 6: Top Cast Members by Number of Movies
sns.barplot(x=top_cast.values, y=top_cast.index, ax=axes[5], palette='Blues_r')
axes[5].set_title("Top 10 Cast Members by Number of Movies")
axes[5].set_xlabel("Number of Movies")

# Plot 7: Release Year vs Top Cast Members (Top 6 Cast Members)
df_cast_pivot.plot(kind='line', ax=axes[6], linewidth=2, colormap='tab10')
axes[6].set_title("Release Year vs Top Cast Members (Top 6 Cast Members)")
axes[6].set_xlabel("Release Year")
axes[6].set_ylabel("Number of Movies")
axes[6].legend(title='Cast', loc='upper left')

# Plot 8: Release Year vs Genre (Top 6 Genres)
df_genre_pivot.plot(kind='line', ax=axes[7], linewidth=2, colormap='Set1')
axes[7].set_title("Release Year vs Genre (Top 6 Genres)")
axes[7].set_xlabel("Release Year")
axes[7].set_ylabel("Count")
axes[7].legend(title='Genre', loc='upper left')

# Plot 9: Most Recent Year Genre Distribution
sns.barplot(x=recent_genre_counts.values, y=recent_genre_counts.index, ax=axes[8], palette='Set2')
axes[8].set_title(f"Genre Distribution in {most_recent_year}")
axes[8].set_xlabel("Count")

# Adjust layout to avoid overlap
plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.show()

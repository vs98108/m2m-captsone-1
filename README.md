# m2m-captsone-1
Netflix Dataset Analysis Report

# Netflix Dataset Analysis Report

## Dataset Details
The dataset used for this project contains information about Netflix's movies and TV shows, including details like title, type, director, cast, country, release year, rating, genre, and date added. The data helps to explore the content distribution patterns, popular genres, and key contributors on the platform.

## Objective
The objective of this analysis is to provide a comprehensive overview of Netflix's content catalog, highlighting key trends in content type, genre distribution, country-wise contributions, top actors, and ratings over the years.

## Data Cleaning
- Missing values in the **country** column were replaced with **"Unknown"**.
- Missing ratings were filled with **"Not Rated"**.
- The **date_added** field was converted to datetime format, and a new column **year_added** was created.
- Cast members and genres were split into individual records to allow deeper analysis.

## Key Insights

### Number of Movies vs TV Shows
The dataset reveals that Netflix features more **Movies** than **TV Shows**, indicating a preference for cinematic content.
![image](https://github.com/user-attachments/assets/34aa5e68-f72f-440a-befe-0f08ac46745e)


### Top 10 Countries with Most Content
The United States contributes the highest volume of content, followed by India and the United Kingdom, highlighting Netflix's focus on key global markets.
![image](https://github.com/user-attachments/assets/9102ca13-c807-4ca1-a2c7-676c7706ecd2)


### Content Added Over the Years
Netflix experienced significant content growth from **2015 to 2020**, reflecting its rapid expansion. However, the number of additions shows a slight decline in recent years.
![image](https://github.com/user-attachments/assets/fb8f3aa2-ca1b-45ef-b313-1fc2a3a1d65e)


### Top 10 Ratings
The most common ratings include **TV-MA**, **TV-14**, and **TV-PG**, suggesting that Netflix caters to a diverse audience with content for different age groups.
![image](https://github.com/user-attachments/assets/9ff395b9-99c8-417f-83eb-559ce19de6f9)


### Top 10 Cast Members by Number of Movies
The most frequent actors on Netflix include several globally recognized names, reflecting Netflix's partnerships with popular artists.
![image](https://github.com/user-attachments/assets/514e1dff-7c45-4f41-8836-12b544c27ed0)


### Rating vs Release Year
Analysis of content ratings over time reveals that mature content (**TV-MA**) has increased significantly, indicating a shift toward adult-oriented programming.
![image](https://github.com/user-attachments/assets/06352e10-5c09-4b32-8b67-3473ccccf5b3)


### Release Year vs Genre
Genres like **Documentaries** and **Dramas** dominate Netflix's catalog, with a consistent rise in **Reality Shows** and **Stand-Up Comedy** in recent years.
![image](https://github.com/user-attachments/assets/2f343f94-082d-4fa5-bb3c-41431cecc623)


### Genre Distribution in 2021
In the most recent dataset year, **Documentaries** and **Dramas** were the most prevalent genres, aligning with Netflix's strategy to cater to both entertainment and educational content.
![image](https://github.com/user-attachments/assets/bb92785e-f1ee-43fb-9434-6bf31ca8cb28)


## Conclusion
This analysis highlights Netflix's evolving content strategy, with a clear focus on diverse genres, popular actors, and mature content. While the platform's growth peaked in the mid-2010s, recent trends suggest a more curated approach to content acquisition. Further analysis could explore viewership patterns and the impact of regional content on Netflix's global expansion.


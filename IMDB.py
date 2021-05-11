import pandas as pd 
from matplotlib import pyplot as plt 
import missingno as msno
import numpy as np
import seaborn as sns
df=pd.read_csv('imdb_top_1000.csv')

#understanding the data
print(df.head(5))
print(df.info())

### handling the missing values

msno.bar(df)
msno.matrix(df)
print(plt.show())
#The Missing values are in columns(Certificate ,Meta_score ,Gross)
#filling the missing data
df['Certificate'].fillna('missing',inplace=True)
df['Meta_score'].fillna(0,inplace=True)

df['Gross']=df['Gross'].str.replace(',','')
df['Gross'].fillna(0,inplace=True)
df['Gross']=pd.to_numeric(df['Gross'],errors='coerce')
print(df.info())

#Quick Analysis for the data
df1=df.describe(include='all')
#top 10 movies according to ratings
plt.style.use('seaborn')

plt.bar(df['Series_Title'][:10],df['IMDB_Rating'][:10],label='IMDB Ratings',color='#CFB53B')
plt.title('Top 10 Movies According To Ratings')
plt.ylabel('IMDB Ratings')
plt.xlabel('Movies Title')
plt.grid(True)
plt.legend()
plt.gcf().autofmt_xdate()
plt.show()

#Top 10 Movies according to Gross
Gross=df.sort_values('Gross',ascending=False)
plt.bar(Gross['Series_Title'][:10],Gross['Gross'][:10],color='black',label='Gross')
plt.title('Top 10 movies according to Gross')
plt.ylabel('Gross')
plt.xlabel('Movies Titles')
plt.gcf().autofmt_xdate()
plt.legend()
plt.grid(True)
plt.show()

#Top Genres
genre=df['Genre'].tolist()
Genre=[]

for i in range(len(genre)):
    x=genre[i].split(',')
    Genre.append(x)
GENRE=[]
for i in    range(len(Genre)):
    x=Genre[i]
    for g in range(len(x)):
                    GENRE.append(x[g])

df_genre=pd.DataFrame(GENRE)
df_genre=df_genre.value_counts()
df_genre_counts=pd.DataFrame(df_genre.value_counts())
df_genre_counts.drop('Drama',inplace=True)
df_genre_counts.iloc[0]=df_genre_counts.iloc[0]+289
df_genre_counts.plot(kind='bar',title='Top Genres',xlabel='Genre',ylabel='Counts',legend=False)

#Top 10 Actors acts on a movieas that have a high ratings
df_ratings=df[df['IMDB_Rating']>=8]
cast=df_ratings['Star1']+','+df_ratings['Star2']+','+df_ratings['Star3']+','+df_ratings['Star4']

Cast=cast.tolist()
Cast_modified=[]

for i in range(len(Cast)):
      x=Cast[i].split(',')
      Cast_modified.append(x)
Actor=[]
for i in    range(len(Cast_modified)):
    x=Cast_modified[i]
    for g in range(len(x)):
                    Actor.append(x[g])
df_Actors=pd.DataFrame(Actor)
df_Actors.value_counts()[:10].plot(kind='bar',title='Top Actors act on movies have a highest ratings',xlabel='Actors'
                                    ,ylabel='Numbers of movies',legend=False,color='black')
plt.gcf().autofmt_xdate()

# top 10 director directs movies have hieghest ratings
df_ratings['Director'].value_counts()[:10].plot(kind='bar',title='Top directors act on movies have a highest ratings',
                                            ylabel='Numbers of movies',xlabel='Director',color='black'   )
plt.gcf().autofmt_xdate()

# Top 10 Actors acts on a movieas that have a high Gross
cast_Gross=Gross['Star1']+','+Gross['Star2']+','+Gross['Star3']+','+Gross['Star4']
Cast_Gross=cast_Gross.tolist()
Cast_modified_Gross=[]

for i in range(len(Cast_Gross)):
      x=Cast_Gross[i].split(',')
      Cast_modified_Gross.append(x)
Actor_Gross=[]
for i in    range(len(Cast_modified_Gross)):
    x=Cast_modified_Gross[i]
    for g in range(len(x)):
                    Actor_Gross.append(x[g])
df_Actors_Gross=pd.DataFrame(Actor_Gross)
df_Actors_Gross.value_counts()[:10].plot(kind='bar',title='Top Actors act on movies have a highest ratings',xlabel='Actors'
                                    ,ylabel='Numbers of movies',legend=False,color='black')
plt.gcf().autofmt_xdate()

# top 10 director directs movies have hieghest Gross
Gross['Director'].value_counts()[:10].plot(kind='bar',title='Top directors act on movies have a highest ratings',
                                            ylabel='Numbers of movies',xlabel='Director',color='black'   )
plt.gcf().autofmt_xdate()

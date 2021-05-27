# Importing libraries
import pandas as pd
import numpy as np

def recommendation():
    
    # Read csv file into a pandas dataframe
    df = pd.read_csv("books.csv")
    df = df[df.language_code =='eng']
    df['Title'] = df['title'].str.split('(').str[0]

    search= input("enter to search ")
    if search=="random":
        df_new= df.sample(replace=True)[['Title', 'authors',"rating"]]
        print("Title: ", df_new[['Title']].to_string(index=False, header=False))
        print("Author: ", df_new[['authors']].to_string(index=False, header=False))
        print("Rating: ", df_new[['rating']].to_string(index=False, header=False))
        return "Enjoy!"
    elif "rating" in search:
            search=search.split()
            rate=float(search[1])
            df_rate = df[df['rating'].astype(float) >= rate]
            df_new= df_rate.sample(replace=True)[['Title', 'authors',"rating"]]
            print("Title: ", df_new[['Title']].to_string(index=False, header=False))
            print("Author: ", df_new[['authors']].to_string(index=False, header=False))
            print("Rating: ", df_new[['rating']].to_string(index=False, header=False))
            return "Enjoy!"
print(recommendation())
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "C:/Users/Emery/Downloads/Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products_May19.csv.zip",
    compression='zip'
)

print(df.head())
print(df.columns)

df.columns = df.columns.str.strip()
df = df.drop_duplicates()
df["dateAdded"] = pd.to_datetime(df["dateAdded"])
df["dateUpdated"] = pd.to_datetime(df["dateUpdated"])

#ajout dune nouvelle colonne

df["annee_ajout"] = df["dateAdded"].dt.year

#compte les ajouts par annees 

ajout_par_annee = df["annee_ajout"].value_counts().sort_index()
#visualisations les ajouts par annees
ajout_par_annee.plot(kind='bar', figsize=(8, 5), color='red')
plt.title("Nombre de produits ajoutés par année")
plt.xlabel("Années")
plt.ylabel("Nombre de produits")
plt.tight_layout()
plt.show()
# les 10 marques les plus presents 
marques = df["brand"].value_counts().head(10)
#visualisations de ses marques 
marques.plot(kind='bar', figsize=(8, 6), color='orange')
plt.title("Top 10 des marques les plus présentes")
plt.xlabel("marques")
plt.ylabel("nombres de produits")
plt.tight_layout()
plt.show()
#les 10 categories les plus presents
categories = df['categories'].value_counts().head(10)
categories.index = categories.index.str.strip().str.slice(0, 30)

# visulisations
categories.plot(kind='bar', color='green', figsize=(12, 6))
plt.title("Top 10 des catégories les plus présentes")
plt.xlabel("categores")
plt.ylabel("nombres de produits")
plt.tight_layout()
plt.xticks(rotation=45, ha='right')

plt.show()





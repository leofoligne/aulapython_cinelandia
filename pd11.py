import pandas as pd
df = pd.read_csv('ClassicDisco.csv')

#Filtrar musicas lançadas depoi de 1980
print(df[df['Year'] > 1980])
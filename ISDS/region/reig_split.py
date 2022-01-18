import pandas as pd

dir = "/home/mglee/VSCODE/git/ISDS/region/(안전영역)기초_농어촌_순위.xlsx"
df = pd.read_excel(dir)
As = []
Bs = []
print(df)
for row in df['기초_농어촌(군)']:
    a, b = row.split()
    As.append(a)
    Bs.append(b)

df['Unnamed: 0'] = As
df['기초_농어촌(군)'] = Bs
df.columns = ['광역','순위', '기초', '점수']
df_modi = df[['광역', '기초', '점수','순위']]
df_modi.to_excel("/home/mglee/VSCODE/git/ISDS/region/(수정)(안전영역)기초_농어촌_순위.xlsx")
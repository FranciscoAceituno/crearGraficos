from processFile import ProcessFile
import pandas as pd


def readFile():
    df = pd.read_csv('public_transportation_statistics_by_zip_code.csv')
    df.dropna()
    df = df[df['public_transportation_pct'] > 0]

    return df

df = readFile()
process = ProcessFile(df)
try:
    if __name__ == "__main__":
        
        process.menuPrincipal()
        
except KeyboardInterrupt:
    print("\n Hasta Luego.....")
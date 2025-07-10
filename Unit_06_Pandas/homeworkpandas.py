import pandas as pd

df = pd.read_csv("Unit_06_Pandas\pokedex.csv")

df.drop(columns=["Abil1", "Abil2"], inplace=True)

df["Type2"] = df.apply(
    lambda row: row["Type1"] if row["Type2"] == "..." else row["Type2"], axis=1
)
df.rename(
    columns={
        "PA": "ph_Atk",
        "PD": "ph_Def",
        "SA": "sp_Atk",
        "SD": "sp_Def",
        "SP": "speed",
        "BST": "total_Stats",
    },
    inplace=True,
)

stats = ["HP", "ph_Atk", "ph_Def", "sp_Atk", "sp_Def", "speed"]
top_pokemon = {"stat": [], "topPokemon": []}

for stat in stats:
    top_row = df.loc[df[stat].idxmax()]
    top_pokemon["stat"].append(stat)
    top_pokemon["topPokemon"].append(top_row["Name"])

top_df = pd.DataFrame(top_pokemon)
top_df

print(df)

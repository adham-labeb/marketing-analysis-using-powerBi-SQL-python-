import pandas as pd
import gender_guesser.detector as gender



df: pd.DataFrame = pd.read_csv('out/dim_customers.csv')


d: gender.Detector = gender.Detector()

def correct_gender(row: pd.Series) -> str:
    name = row['CustomerName'].split(' ')[0]
    current_gender = row['Gender']
    
    guessed_gender = d.get_gender(name)
    
    if guessed_gender in ['male', 'mostly_male']:
        guessed_gender = 'Male'
    elif guessed_gender in ['female', 'mostly_female']:
        guessed_gender = 'Female'
    else:
        guessed_gender = None

    if guessed_gender and guessed_gender != current_gender:
        return guessed_gender
    return current_gender

df['Gender'] = df.apply(correct_gender, axis=1)

df.to_csv('out/dim_customers_updated.csv', index=False)
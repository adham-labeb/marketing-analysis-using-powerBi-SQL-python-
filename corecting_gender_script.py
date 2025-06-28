#-- importing the pandas and gender_guesser libraries --
import pandas as pd
import gender_guesser.detector as gender


# Read the CSV file into a pandas DataFrame.
df = pd.read_csv(r'C:\Users\Home\Desktop\NTI-final-project\dim_customers.csv')

# Initialize the gender detector from the gender_guesser library.
d = gender.Detector()

# Define a function to correct gender based on a customer's name.
# This function will be applied row-wise to the DataFrame.
def correct_gender(row: pd.DataFrame):

# Extract the first word of the 'CustomerName' as the primary name for gender detection.

    name = row['CustomerName'].split(' ')[0]
    
# Get the current gender value from the DataFrame row

    current_gender = row['Gender']
    
# Use the gender detector to guess the gender based on the extracted name.

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

# Apply the 'correct_gender' function to each row of the DataFrame.

df['Gender'] = df.apply(correct_gender, axis=1)

# Save the modified DataFrame to a new CSV file.

df.to_csv('dim_customers_updated.csv', index=False)

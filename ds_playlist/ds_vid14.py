import pandas as pd
import matplotlib.pyplot as plt

data = {
    'SSN': [123,567,890,234],
    'Name': ["Anaa", 'Bob', 'John', 'Tyler'],
    'Age': [24,32,22,45],
    'Height': [165,173,180,170]
}

df = pd.DataFrame(data)
df.set_index("SSN", inplace=True)

print(df.Height.mean()) # all numpy stats functions (.std .mode etc)

print(df.Height.describe())
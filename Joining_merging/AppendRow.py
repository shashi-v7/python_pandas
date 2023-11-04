# Write a Pandas program to append rows to an existing DataFrame and display the combined data.

import pandas as pd

d1 = pd.DataFrame({
    'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
    'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
    'marks': [200, 210, 190, 222, 199]
})
new_rows = pd.DataFrame({
    'student_id': ['S6'],
    'name': ['Scarlette Fisher'],
    'marks': [205]
})

combined_data = pd.concat([d1, new_data], ignore_index=True)
print(combined_data)
students=[{'name': 'Aarav', 'number': 28}, {'name': 'Amit', 'number': 12}, {'name': 'Akash', 'number': 15}, {'name': 'Deepika', 'number': 34}, {'name': 'Isha', 'number': 33}, {'name': 'Jaya', 'number': 3}, {'name': 'Kiran', 'number': 19}, {'name': 'Maya', 'number': 49}, {'name': 'Neha', 'number': 6}, {'name': 'Rohan', 'number': 42}, {'name': 'Shreya', 'number': 28}, {'name': 'Tanvi', 'number': 45}, {'name': 'Vikram', 'number': 4}, {'name': 'Yash', 'number': 37}, {'name': 'Zara', 'number': 41}, {'name': 'Arjun', 'number': 18}, {'name': 'Devika', 'number': 18}, {'name': 'Gaurav', 'number': 32}, {'name': 'Kavya', 'number': 37}, {'name': 'Manisha', 'number': 22}, {'name': 'Nisha', 'number': 10}, {'name': 'Raj', 'number': 7}, {'name': 'Shivani', 'number': 10}, {'name': 'Tara', 'number': 5}, {'name': 'Varun', 'number': 50}, {'name': 'Vijay', 'number': 31}, {'name': 'Anaya', 'number': 20}, {'name': 'Ishita', 'number': 8}, {'name': 'Krishna', 'number': 29}, {'name': 'Pooja', 'number': 31}]

zeroToTen=[marks['name'] for marks in students if marks['number'] > 0 and marks['number'] < 11]
print("0-10", zeroToTen)

elevenToTwenty=[marks['name'] for marks in students if marks['number'] > 11 and marks['number'] < 20]
print("11-20", elevenToTwenty)

twentyOneToThirty=[marks['name'] for marks in students if marks['number'] > 21 and marks['number'] < 30]
print("21-30", twentyOneToThirty)

thirtyOneToForty=[marks['name'] for marks in students if marks['number'] > 31 and marks['number'] < 40]
print("31-40", thirtyOneToForty)

fortyOneToFifty=[marks['name'] for marks in students if marks['number'] > 41 and marks['number'] < 51]
print("41-50", fortyOneToFifty)

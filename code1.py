import csv
import os
province_count = 0
city_count = 0
for filename in os.listdir('.'):
    if filename.endswith('.csv'):
        province = os.path.splitext(filename)[0].replace('_', ' ')
        province_count +=1
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')  # use comma as delimiter
            next(reader)  # skip header row
            for row in reader:
                print(row)  # debug print
                if len(row) < 3:  # update the condition for the number of columns
                    print(f"Error: row has only {len(row)} columns")
                    continue
                province = province.replace(' ', '+')
                city = row[1].replace('_', ' ')  # update the column index
                city = city.replace(' ', '+')
                lat = row[2]
                lon = row[3]
                city_count +=1
                url = f"https://example.com/?province={province}&city={city}&lat={lat}&lon={lon}"
                print(url)
print(province_count)
print(city_count)
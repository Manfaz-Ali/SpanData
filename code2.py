import csv
import os
import json

urls = []  # create an empty list to store URLs
province_count = 0
city_count = 0

for filename in os.listdir('.'):
    if filename.endswith('.csv'):
        province = os.path.splitext(filename)[0].replace('_', ' ')
        province_count += 1
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)  # skip header row
            for row in reader:
                if len(row) < 4:
                    print(f"Error: row has only {len(row)} columns")
                    continue
                province = province.replace(' ', '+')
                city = row[1].replace('_', ' ')
                city = city.replace(' ', '+')
                lat = row[2]
                lon = row[3]
                city_count += 1
                url = f"https://example.com/?province={province}&city={city}&lat={lat}&lon={lon}"
                urls.append(url)  # add the URL to the list

# write the list to a JSON file
with open('urls.json', 'w') as f:
    json.dump(urls, f)

print(f"Processed {province_count} provinces and {city_count} cities.")

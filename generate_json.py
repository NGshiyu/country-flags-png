#!/usr/bin/env python3
import json
import os

# Read countries.json
with open('countries.json', 'r', encoding='utf-8') as f:
    countries = json.load(f)

# Get list of PNG files
png_files = []
for file in sorted(os.listdir('png')):
    if file.endswith('.png'):
        code = file.replace('.png', '')
        png_files.append(code)

# Generate icons list - both code and full name for each country
icons = []
for code in png_files:
    if code in countries:
        country_name = countries[code]
        url = f"https://raw.githubusercontent.com/NGshiyu/country-flags-png/main/png/{code}.png"
        # Add entry with full name
        icons.append({
            "name": country_name,
            "url": url
        })
        # Add entry with code
        icons.append({
            "name": code,
            "url": url
        })

# Generate complete JSON
result = {
    "name": "NGshiyu's Icon Package",
    "description": "Fork from hampusborgos/country-flags,reform by https://t.me/NG_shiyu. Acknowledgements to hampusborgos and ligeicon",
    "icons": icons
}

# Write to file with escaped slashes
json_str = json.dumps(result, ensure_ascii=False, indent=2)
# Manually escape forward slashes
json_str = json_str.replace('/', '\\/')
with open('NGshiyu_flag_icons.json', 'w', encoding='utf-8') as f:
    f.write(json_str)

print(f"Generated {len(icons)} icon entries")

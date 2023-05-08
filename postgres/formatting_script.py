import json
import re

with open('postgres/sample_data.json') as f:
    input_data = json.load(f)

def clean_data(input_data):
    output = []

    for item in input_data:
        # 1
        if item.get("remote_service") == "tak":
            item.update({"remote_service": True})
        else:
            item.update({"remote_service": False})

        # 2
        if item.get("elevator") == "tak":
            item.update({"elevator": True})
        else:
            item.update({"elevator": False})

        # 3
        try:
            item.update({"year_of_construction": int(item.get("year_of_construction"))})
        except Exception:
            item.update({"year_of_construction": None})

        # 4
        try:
            item.update({"number_of_rooms": int(item.get("number_of_rooms"))})
        except Exception:
            item.update({"number_of_rooms": None})

        # 5
        try:
            s = item.get("footer")
            numeric_val = re.findall(r'\d+\.?\d*', s)
            numeric_val = float(numeric_val[0].replace(',', '.'))
            item.update({"footer": numeric_val})
        except Exception:
            item.update({"footer": None})
        
        # 6
        try:
            s = item.get("price")
            ss = s.replace(" ", "")
            numeric_val = re.findall(r'\d+\.?\d*', ss)
            numeric_val = float(numeric_val[0].replace(',', '.'))
            item.update({"price": numeric_val})
        except Exception:
            item.update({"price": None})
        
        # 7
        try:
            s = item.get("price_per_meter")
            ss = s.replace(" ", "")
            numeric_val = re.findall(r'\d+\.?\d*', ss)
            numeric_val = float(numeric_val[0].replace(',', '.'))
            item.update({"price_per_meter": numeric_val})
        except Exception:
            item.update({"price_per_meter": None})

        #8
        try:
            s = item.get("rent")
            ss = s.replace(" ", "")
            numeric_val = re.findall(r'\d+\.?\d*', ss)
            numeric_val = float(numeric_val[0].replace(',', '.'))
            item.update({"rent": numeric_val})
        except Exception:
            item.update({"rent": None})

        output.append(item)

    return output


formatted_data = clean_data(input_data)

with open('postgres/formatted_sample_data.json', 'w') as f:
    json.dump(formatted_data, f)
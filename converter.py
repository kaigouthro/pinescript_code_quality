
#  pu the successful entrties here, and this will convver them to jsonl that can be used tto fine tune a model,..
# the point of this is if you can create synthetic data en masse, with tons of different instructions and completions that might exist...
# you caqn use this tool to repair any synthetic data to ensure it compiles, hen use 100% compiling coode o fine une, or create beer snthettic data.

data = [   ]

import json
def convert_to_jsonl(data):
    jsonl_data = ""

    for item in data:
        instruction = item["instruction"]
        completion = item["completion"]

        jsonl_data += json.dumps({"messages": [
            {"role": "system", "content": "You are a Pine Script coder."},
            {"role": "user", "content": instruction},
            {"role": "assistant", "content": completion}
        ]}) + "\n"

    return jsonl_data


with open("pine.jsonl", "w") as f:
    f.write(convert_to_jsonl(data))

print("Json file created!")

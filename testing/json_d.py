from pathlib import Path
import json


input = Path("sampleCN.txt")
output1 = Path("output_v1.json")
output2 = Path("output_v2.json")
output3 = Path("output_v3.json")

with input.open(mode="r", encoding="utf-8") as f:
    read_result = f.read()
    # print(type(read_result))
    # print(read_result)

data = {"data": read_result}

with output1.open(mode="w") as f:
    tmp = str(data)
    print(">>>", type(tmp))
    print(tmp)
    f.write(tmp)


with output2.open(mode="w") as f:
    tmp = json.dumps(data, indent=4, ensure_ascii=False)
    print(">>>", type(tmp))
    print(tmp)
    f.write(tmp)


with output3.open(mode="w") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file_name, delimiter=",", new_line="\n") -> list[dict]:
    with open(file_name) as f:
        count = 1
        rest_line = []
        final_list = []

        for line in f:
            if count == 1:
                line_1 = line.rstrip(new_line).split(delimiter)
                count += 1
                continue
            line_2 = line.rstrip(new_line).split(delimiter)
            dict_data = dict(zip(line_1, line_2))
            final_list.append(dict_data)

    return final_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))



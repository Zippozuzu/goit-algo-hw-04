import sys

def get_cats_info(path):
    dict_cats = []
    keys = ["id", "name", "age"]

    try:
        with open(path, 'r') as fh:
            content = fh.read()
            content = content.split("\n")               # from str to list, divided by "\n"

        for i in content:
            values = i.split(',')                       # list of separate values, divided by ","
            dictionary = dict(zip(keys, values))
            dict_cats.append(dictionary)

        return dict_cats
      
    except FileNotFoundError:
       print(f"There is no {path} file")
       sys.exit(1)
import json


def reader(FileName=None):
    if FileName is not None:
        with open(FileName, encoding='utf8') as jsonfile:
            reader = json.load(jsonfile)
            if isinstance(reader, dict):
                return reader
            else:
                data = ()
                for row in reader:
                    data = list(data)
                    data.append(row)
                    data = tuple(data)
                return data


def write(FileName=None, data=None):
    if FileName is None and data is not None:
        if isinstance(data, tuple) or isinstance(data, list):
            try:
                data = list(data)
            except:
                data = [data]
        with open(str(FileName), 'w', encoding='utf8') as f:
            json.dump(data, f, indent=4)
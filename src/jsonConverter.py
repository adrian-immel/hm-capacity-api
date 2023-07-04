import sys
import jsonpickle


def json_creator(data, filename: str):
    """
    creates a Json files out of given data and saves them
    is used to create the static json api

    :param data: used to create json of
    :param filename:  filename of the generated json file
    :return: None
    """

    filename = (sys.path[0] + r'/../capacity-api/' + filename + ".json")
    json_object = jsonpickle.encode(data, unpicklable=False, indent=4)
    with open(filename, 'w') as f:
        f.write(json_object)

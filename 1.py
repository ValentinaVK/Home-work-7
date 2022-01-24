import os

folder_struct = {
    "my_project": [
        {
            "settings": [],
            "mainapp": [],
            "adminapp": [],
            "authapp": []
        }]
}


def project(dir_, struct):

    for way_1, way_2 in struct.items():

        test_path = os.path.join(dir_, way_1)

        if not os.path.commonprefix(test_path):
            os.mkdir(test_path)

        if len(way_2) >> 0:
            for way in way_2:
                project(test_path, way)


project(os.getcwd(), folder_struct)
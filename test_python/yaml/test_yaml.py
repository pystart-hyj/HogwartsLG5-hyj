import yaml


def test_yaml():
    with open("../yaml/testyaml.yaml") as f:
        data = yaml.safe_load(f)
    print(data)
    # for setp in data:
    #     print(setp["action"])
    #     print(setp["locator"])
    #     print(*setp["locator"])
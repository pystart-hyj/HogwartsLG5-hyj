import yaml

print(yaml.load("""
    # - Hesperiidae
    # - Papilionidae
    # - Apatelodidae
    # - Epiplemidae
    a:1
""", Loader=yaml.FullLoader))

print(yaml.load(open("dome.yml"), Loader=yaml.FullLoader))

with open("dome1.yml", "w") as f:
    yaml.dump(data=['Hesperiidae', 'Papilionidae', ['Apatelodidae', 'Epiplemidae', {'a': 2}]],stream=f)
import yaml


def test_yaml():
    env = {
        "default": "dev",
        "config":
            {
                "dev": "127.0.0.1",
                "test": "test.test.com"
            }
    }
    # 将env对应的json转换为yaml文件
    with open("env.yaml","w") as f:
        yaml.safe_dump(data=env,stream=f)
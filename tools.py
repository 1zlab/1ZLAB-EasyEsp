def make_config(is_dev):
    with open('./esp_config.json','r') as f:
        config = f.read()
    if is_dev:
        pass

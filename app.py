import hcl2, json

def main():
    with open('terraform/variables.tf', 'r') as variables:
        variables_dict = hcl2.load(variables)
    print(json.dumps(variables_dict))
    config_files = ['regional-configs.json', 'app-configs.json']
    for config_file in config_files:
        with open('configs/' + config_file, 'r') as c:
            configs_dict = json.load(c)
            print("configs, " + config_file + ":")
            print(configs_dict)
            for prop in configs_dict:
                for idx,v in enumerate(variables_dict['variable']):
                    if v.get(prop):
                        variables_dict['variable'][idx][prop]['value'] = configs_dict[prop]
    print(json.dumps(variables_dict))

if __name__ == "__main__":
    main()

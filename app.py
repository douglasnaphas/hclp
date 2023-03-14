import hcl2, json

def main():
    with open('terraform/variables.tf', 'r') as variables:
        variables_dict = hcl2.load(variables)
    config_files = ['regional-configs.json', 'app-configs.json']
    for config_file in config_files:
        with open('configs/' + config_file, 'r') as c:
            configs_dict = json.load(c)
            for prop in configs_dict:
                for idx,v in enumerate(variables_dict['variable']):
                    if v.get(prop):
                        variables_dict['variable'][idx][prop]['value'] = configs_dict[prop]
    out_dict = dict()
    for var_idx, var_dict in enumerate(variables_dict['variable']):
        for var_name in var_dict: # only one property in this dict
            out_dict[var_name] = var_dict[var_name]['value']
    print("writing terraform.tfvars.json as:")
    print(json.dumps(out_dict))
    with open('terraform/terraform.tfvars.json', 'a') as tfvars_json_file:
        tfvars_json_file.write(json.dumps(out_dict))

if __name__ == "__main__":
    main()

import hcl2

def main():
    with open('outputs.tf', 'r') as outputs:
        outputs_dict = hcl2.load(outputs)
        print(outputs_dict)

if __name__ == "__main__":
    main()

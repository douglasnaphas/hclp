import hcl2

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

def test_using_hcl2():
    with open('outputs.tf', 'r') as outputs:
        outputs_dict = hcl2.load(outputs)
        

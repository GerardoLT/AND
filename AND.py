import random 
import itertools

def AND(self,num_vars):
    input_values = [[0, 1] for _ in range(num_vars)]
    input_combinations = list(itertools.product(*input_values))

    and_results = []
    for inputs in input_combinations:
        result = all(inputs)
        and_results.append(result)

    table = list(zip(input_combinations, and_results))
   
    for row in table:
        input_str = " ".join([str(input_val) for input_val in row[0]])
        result_str = str(row[1])
        print(f"{input_str} = {result_str}")


def TAND(self,num_trials, num_vars):
    for i in range(num_trials):
        inputs = [random.randint(0, 2) for _ in range(num_vars)]
        for row in table:
         nuevos_val = " ".join([str(self.input_val) for input_val in row[0]])
         
        output = all(inputs)
        if output:
            print(f"Inputs: {inputs}; Output: {output}")
        else:
            print(f"Inputs: {inputs}; Output: {output}")

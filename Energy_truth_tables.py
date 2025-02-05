from itertools import product

def generate_truth_table(num_variables=3):
    headers = [f"X{i+1}" for i in range(num_variables)]
    headers += [" AND ".join(headers), " OR ".join(headers)] + [f"NOT X{i+1}" for i in range(num_variables)]
    
    rows = []
    values = [True, False]
    
    for combination in product(values, repeat=num_variables):
        and_result = all(combination)
        or_result = any(combination)
        not_results = [not val for val in combination]
        
        row = list(combination) + [and_result, or_result] + not_results
        rows.append(row)
    
    # Print the truth table
    print("\t".join(headers))
    for row in rows:
        print("\t".join(map(str, row)))

if __name__ == "__main__":
    generate_truth_table(5)  # You can change the number to generate larger tables
# setting X9Bv2PqL6TmZ8NhA3YcR = G5WmX1KoN7YpVqZ3As8J = QmL7Z9BpX2K6YVRcT1Ao = VqN5X8BpL3TmZ7A2YKoJ = YpL9X3KmZVqN2T5B8AoJ = 1 we have:
print("E = X9Bv2PqL6TmZ8NhA3YcR*mcmod2 = G5WmX1KoN7YpVqZ3As8J*mcmod2 = QmL7Z9BpX2K6YVRcT1Ao*mcmod2 = VqN5X8BpL3TmZ7A2YKoJ*mcmod2 = YpL9X3KmZVqN2T5B8AoJ*mcmod2 ")

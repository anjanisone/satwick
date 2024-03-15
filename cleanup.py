from tqdm import tqdm
def process_file(file_path):
    with open(file_path, 'r+') as file:
        data = file.readlines()
        print("All LInes read complete")
        file.seek(0)
        for line in tqdm(data, total=len(data), desc="Processing Lines"):
            if '""Coeur d\'Alene, ID""' in line:
                line = line.replace('""Coeur d\'Alene, ID""','"Coeur d\'Alene, ID"')
            elif '"coeur d\'alene"' in line:
                line = line.replace("\'","'")
            file.write(line)
        file.truncate()

file_path = "HICustomerLifecycle_20240305"
process_file(file_path)

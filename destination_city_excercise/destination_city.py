paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

def end_destination(paths):
    start_cities = set()
    end_cities = set()

    for path in paths:
        start_cities.add(path[0])
        end_cities.add(path[1])
        

    for city in end_cities:
        if city not in start_cities:
            return city

    return None
print(end_destination(paths))  # Output: "Sao Paulo"
print(end_destination([["A","E"],["B","C"],["C","d"]]))
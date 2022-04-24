# TODO 1: Add two parameters (length_ft and width_ft)
def calc_square_meters_from_feet(width, height):    
    area = width * height
    # TODO 2: Modify the code below:
    metric_area = area * 0.3048
    # Leave the line below as it is
    return metric_area

print(calc_square_meters_from_feet(10, 10))
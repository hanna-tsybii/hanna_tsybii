def can_fit_through_door(h, w, a, b, c):
    # Check if any side of the box is larger than the corresponding dimension of the door
    if (a <= h and b <= w) or (a <= w and b <= h):
        return True
    elif (a <= h and c <= w) or (a <= w and c <= h):
        return True
    elif (b <= h and c <= w) or (b <= w and c <= h):
        return True
    else:
        return False

# Example usage
door_height = 80
door_width = 30
box_length = 60
box_width = 20
box_height = 40

if can_fit_through_door(door_height, door_width, box_length, box_width, box_height):
    print("The box can fit through the door.")
else:
    print("The box cannot fit through the door.")

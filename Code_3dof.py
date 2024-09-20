import math

# Constants for lengths of base and arms
len_base = 25
len_arm1 = 25
len_arm2 = 25

# Coordinates of the target point (x, y, z)
x = 25
y = 25
z = 25

RAD2DEG = 180 / math.pi

# Function to calculate the angles for inverse kinematics
def get_angle(x, y, z, base, arm1, arm2):
    # Distance from the origin to the point in the XY plane
    xy_distance = math.sqrt(x**2 + y**2)
    
    # Total distance from the base to the point in 3D space
    d = math.sqrt(xy_distance**2 + (z - base)**2)

    # Check if the point is reachable based on the arm lengths
    if d > (arm1 + arm2) or d < abs(arm1 - arm2):
        print("The point is out of reach for the given arm configuration.")
        return None

    # Calculate the base rotation angle in the XY plane (angle of base)
    if x != 0:
        angle_base = math.atan2(y, x)
    else:
        angle_base = math.pi / 2

    # Use law of cosines to calculate the angles for the two arms

    # Angle of the first arm (arm1)
    angle_arm1 = math.atan2(z - base, xy_distance) + \
        math.acos((arm1**2 + d**2 - arm2**2) / (2 * arm1 * d))

    # Angle of the second arm (arm2)
    angle_arm2 = math.acos((arm1**2 + arm2**2 - d**2) / (2 * arm1 * arm2))

    # Convert radians to degrees
    angle_base = angle_base * RAD2DEG
    angle_arm1 = angle_arm1 * RAD2DEG
    angle_arm2 = angle_arm2 * RAD2DEG

    # Return the calculated angles
    angles = [angle_base, angle_arm1, angle_arm2]

    print(f"Angle of Base = {angle_base:.2f} degrees")
    print(f"Angle of Arm1 = {angle_arm1:.2f} degrees")
    print(f"Angle of Arm2 (w.r.t. Arm1) = {angle_arm2:.2f} degrees")

    return angles

# Call the function to get the angles
angles = get_angle(x, y, z, len_base, len_arm1, len_arm2)

if angles:
    print(f"Calculated angles: {angles}")
else:
    print("Could not calculate angles as the point is unreachable.")

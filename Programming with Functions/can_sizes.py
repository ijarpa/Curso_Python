 #can sizes
import math

pi = math.pi

def compute_volume(radius, height):
    volume = pi * radius**2 * height
    return volume


def compute_surface_area(radius, height):
    surf_area = 2 * pi * radius * (radius + height)
    return surf_area

def compute_store_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surf_area = compute_surface_area(radius, height)    
    storage_efficiency = volume / surf_area
    return storage_efficiency

def main():
    name = "1 Picnic"
    radius = 6.83
    height = 10.16
    storage_efficiency = compute_store_efficiency(radius, height)
    print(f"{name} {storage_efficiency:.2f}")

    name = "1 Tall"
    radius = 7.78
    height = 11.91
    storage_efficiency = compute_store_efficiency(radius, height)
    print(f"{name} {storage_efficiency:.2f}")

    name = "2"
    radius = 8.73
    height = 11.59
    storage_efficiency = compute_store_efficiency(radius, height)
    print(f"{name} {storage_efficiency:.2f}")

    name = "2.5"
    radius = 10.32
    height = 11.91
    storage_efficiency = compute_store_efficiency(radius, height)
    print(f"{name} {storage_efficiency:.2f}")

    name = "3 Cylinder"
    radius = 10.79
    height = 17.78
    storage_efficiency = compute_store_efficiency(radius, height)
    print(f"{name} {storage_efficiency:.2f}")

    name = "5"
    radius = 13.02
    height = 14.29
    storage_efficiency = compute_store_efficiency(radius, height)
    print(f"{name} {storage_efficiency:.2f}")

    name = "6Z"
    radius = 5.4
    height = 8.89
    storage_efficiency = compute_store_efficiency(radius, height)
    print(f"{name} {storage_efficiency:.2f}")

    name = "8Z short"
    radius = 6.83
    height = 7.62
    storage_efficiency = compute_store_efficiency(radius, height)
    print(f"{name} {storage_efficiency:.2f}")

    name = "10"
    radius = 15.72
    height = 17.78
    storage_efficiency = compute_store_efficiency(radius, height)
    print(f"{name} {storage_efficiency:.2f}")

    name = "211"
    radius = 6.83
    height = 12.38
    storage_efficiency = compute_store_efficiency(radius, height)
    print(f"{name} {storage_efficiency:.2f}")

    name = "300"
    radius = 7.62
    height = 11.27
    storage_efficiency = compute_store_efficiency(radius, height)
    print(f"{name} {storage_efficiency:.2f}")

    name = "303"
    radius = 8.1
    height = 11.11
    storage_efficiency = compute_store_efficiency(radius, height)
    print(f"{name} {storage_efficiency:.2f}")

main()



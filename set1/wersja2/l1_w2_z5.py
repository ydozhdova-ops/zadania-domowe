from random import uniform

n = float(input("długość odcinka="))

points = []
points.append(uniform(0,n))
points.append(uniform(0,n))
points.sort()

print(f"Trzy losowe segmenty: (0,{points[0]:.4f}), ({points[0]:.4f},{points[1]:.4f}), ({points[1]:.4f},{n:.4f})")
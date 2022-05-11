def pretty_point(point: tuple[float, float]):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"Y={y}"
        case (x, 0):
            return f"X={x}"
        case (x, y):
            return f"X={x}, Y={y}"
        case _:
            raise ValueError("Not a point")

P = (0, 20)
print(pretty_point(P))

def sort(width, height, length, mass):
    # Calculate the total volume of the package
    volume = width * height * length

    # A package is bulky if:
    # 1) volume is >= 1,000,000 cm^3
    # 2) any single dimension is >= 150 cm
    bulky = (
        volume >= 1_000_000 or
        width >= 150 or
        height >= 150 or
        length >= 150
    )

    # Heavy if mass is 20kg or more
    heavy = mass >= 20

    # If it's both bulky and heavy, reject it
    if bulky and heavy:
        return "REJECTED"

    # If it's either bulky or heavy, send to special handling
    if bulky or heavy:
        return "SPECIAL"

    # Otherwise it’s a normal package
    return "STANDARD"


# quick tests to make sure logic works
def run_tests():
    assert sort(10, 10, 10, 1) == "STANDARD"        # small and light
    assert sort(150, 10, 10, 5) == "SPECIAL"        # bulky due to dimension
    assert sort(100, 100, 100, 5) == "SPECIAL"      # bulky due to volume
    assert sort(10, 10, 10, 20) == "SPECIAL"        # heavy only
    assert sort(150, 10, 10, 20) == "REJECTED"      # bulky + heavy

    print("All tests passed")


if __name__ == "__main__":
    run_tests()

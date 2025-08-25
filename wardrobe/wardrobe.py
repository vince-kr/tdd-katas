def compute_configurations(
        elements: set[int],
        wall_length: int) -> list[tuple[int, ...]]:
    solutions = set()
    stack = [([], wall_length)]

    while stack:
        current, remaining = stack.pop()
        if remaining == 0:
            solutions.add(tuple(sorted(current)))
            continue
        for element in elements:
            if element <= remaining:
                stack.append((current + [element], remaining - element))

    return sorted([tuple(config) for config in solutions])

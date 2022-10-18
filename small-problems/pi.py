# Calculating pi using Leibniz formula


def calculate_pi(n_terms: int) -> float:
    num = 4.0
    den = 1
    operation = 1
    pi = 0.0

    for _ in range(n_terms):
        pi += operation * (num/den)
        operation *= -1.0  # Sign changes every iteration
        den += 2

    return pi


if __name__ == "__main__":
    print(calculate_pi(100000))

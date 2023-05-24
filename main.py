"""Module with functions."""

def largest_sum(numbers: list[int]) -> tuple[int, int]:
    """Encontra e retorna os dois números que somados dão o maior valor."""
    if len(numbers) < 2:
        return None
    
    sorted_numbers = sorted(numbers, reverse=True)
    primeiro = sorted_numbers[0]
    segundo = sorted_numbers[1]
    
    return (min(primeiro, segundo), max(primeiro, segundo))

testes1 = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [10, -5, 20, 15, -30],
    [0, 0, 0, 0],
    [-10, -5, -2, -1],
    [5],
    []
]

for i, teste2 in enumerate(testes1):
    print(largest_sum(teste2))
    print()
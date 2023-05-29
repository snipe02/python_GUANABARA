import random
def generate_numbers():
    return random.sample(range(1, 26), 15)
def read_numbers():
    while True:
        try:
            numbers = list(map(int, input("Digite seus 15 números (separados por espaço): ").split()))
            if len(numbers) != 15:
                print("Você deve digitar exatamente 15 números.")
            elif any(num < 1 or num > 25 for num in numbers):
                print("Os números devem estar entre 1 e 25.")
            else:
                return numbers
        except ValueError:
            print("Você deve digitar apenas números inteiros.")
def compare_numbers(winning_numbers, user_numbers):
    num_hits = sum(num in winning_numbers for num in user_numbers)
    return num_hits
def play_game():
    print("Bem-vindo ao jogo da Lotofácil!")
    winning_numbers = generate_numbers()
    user_numbers = read_numbers()
    num_hits = compare_numbers(winning_numbers, user_numbers)
    print(f"Os números sorteados foram: {winning_numbers}")
    print(f"Você acertou {num_hits} números!")

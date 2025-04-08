import random
from colorama import init, Fore, Style
import time

init()

def print_colored(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

def play_game():
    print_colored("\n Игра - 'Угадай число'!", Fore.CYAN)
    print_colored("Попробуй угадать! число от 1 до 100!\n", Fore.YELLOW)
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 15
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"{Fore.GREEN}Введите число (попытка {attempts + 1}/{max_attempts}): {Style.RESET_ALL}"))
            attempts += 1
            
            if guess < secret_number:
                print_colored("Загаданное число больше! ⬆️", Fore.BLUE)
            elif guess > secret_number:
                print_colored("Загаданное число меньше! ⬇️", Fore.BLUE)
            else:
                print_colored(f"\n Поздравляем! Вы угадали число {secret_number} за {attempts} попыток!", Fore.MAGENTA)
                return True
                
            if attempts < max_attempts:
                remaining = max_attempts - attempts
                print_colored(f"Осталось попыток: {remaining}", Fore.YELLOW)
                
        except ValueError:
            print_colored("Пожалуйста, введите корректное число!", Fore.RED)
            attempts -= 1
            
    print_colored(f"\n Игра окончена! Загаданное число было: {secret_number}", Fore.RED)
    return False

def main():
    while True:
        play_game()
        while True:
            play_again = input(f"\n{Fore.CYAN}Хотите сыграть еще раз? (да/нет): {Style.RESET_ALL}").lower()
            if play_again in ['да', 'нет']:
                break
            print_colored("Пожалуйста, введите 'да' или 'нет'", Fore.RED)
            
        if play_again == 'нет':
            print_colored("\nСпасибо за игру!", Fore.CYAN)
            break

if __name__ == "__main__":
    main() 
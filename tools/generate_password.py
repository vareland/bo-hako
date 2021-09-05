import secrets
import string


def get_random_char() -> str:
    chars: str = ''
    chars += string.digits
    chars += string.ascii_letters
    # chars += string.punctuation
    return secrets.choice(chars)


def get_password(length: int) -> str:
    password: str = ''
    for i in range(length):
        password += get_random_char()
    return password


def main() -> None:
    while True:
        length: str = input('length: ')
        if not length.isdigit():
            print('quit')
            print('---')
            break
        password: str = get_password(int(length))
        print(password)
        print('---')
    print('---')


if __name__ == '__main__':
    main()

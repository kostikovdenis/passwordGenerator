import string
import secrets

length_password = 8             # Длина пароля
min_required_chars = 1          # Минимальное количество рекомендуемых символов
special_keys = '!@$%^&*()_-+'   # Можно заменить на string.punctuation, если нужны ВСЕ спецсимволы

chars = string.ascii_letters + string.digits + special_keys
while True:
    password = ''.join(secrets.choice(chars) for i in range(length_password))
    if (sum(c.islower() for c in password) >= min_required_chars
            and sum(c.isupper() for c in password) >= min_required_chars
            and sum(c.isdigit() for c in password) >= min_required_chars
            and sum(c in special_keys for c in password) >= min_required_chars):
        break

print(password)


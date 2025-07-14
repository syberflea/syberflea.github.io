from string import ascii_lowercase, ascii_uppercase
nickname = input()
len_name = len(nickname)
is_len_ok = len_name > 7
is_any_num = any(c.isdigit() for c in nickname)
is_any_upper = any(c for c in nickname if c in ascii_uppercase)
is_any_lower = any(c for c in nickname if c in ascii_lowercase)
print("YES") if is_any_upper and is_any_lower and is_any_num and is_len_ok else print("NO")
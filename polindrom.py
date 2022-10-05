text = input()
if not text:
    print('false')
    exit(0)
text = ''.join(text.strip().split())
print('true' if text == text[::-1] else 'false')

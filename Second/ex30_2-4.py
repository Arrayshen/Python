#检查用户名和pin码是否存在于数据库中
database = [
    ['tom','123'],
    ['jerry','456'],
    ['jones','789']
]

username = input("username:")
pin = input("pin:")

if [username, pin] in database:print('Access granted')
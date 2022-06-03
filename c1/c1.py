import string


def ex_gcd(a: int, b: int) -> (int, int, int):
    if a == 0:
        return b, 0, 1
    (r, r_x, r_y) = ex_gcd(b % a, a)
    # 回溯
    x = r_y - int(b / a) * r_x
    y = r_x
    return r, x, y


def inverse_element(a: int, b: int) -> (int, int):
    ab_gcd, x, y = ex_gcd(a, b)
    if ab_gcd != 1:
        raise ValueError("a, b 不互素，a 不存在逆元!")
    return x, y


def caesar_encrypt(p: str, offset: int = 3) -> str:
    """
    凯撒密码（移位变换密码）
    :param p: 明文输入，仅支持大写英文
    :param offset: 偏移量 0 - 26
    :return: 密文输出
    """
    e = ""
    for c in p:
        if c not in string.ascii_uppercase:
            raise ValueError('p must in %s' % string.ascii_uppercase)
        e += chr(((ord(c) - ord('A') + offset) % 26) + ord('A'))
    return e


def affine_encrypt(p: int, a: int, b: int) -> int:
    """
    仿射密码加密
    :param p: 明文
    :param a: 密钥，必须与26互素，且 0 <= a <= 25
    :param b: 密钥，0 <= b <= 25
    :return: 密文
    """
    return (a * p + b) % 26


def affine_decrypt(e: int, a: int, b: int) -> int:
    """
    仿射密码解密
    :param e: 密文
    :param a: 密钥，必须与26互素，且 0 <= a <= 25
    :param b: 密钥，0 <= b <= 25
    :return: 明文
    """
    x, y = inverse_element(a, 26)
    return x * (e - b) % 26

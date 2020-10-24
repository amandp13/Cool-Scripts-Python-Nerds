class Base62Converter():
    def __init__(self):
        self.__BASE62: tuple = tuple('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
        self.__BASE62INDEX: dict = dict()
        for i, char in enumerate(self.__BASE62):
            self.__BASE62INDEX[char] = i

    def __encodeToBase62(self, decimal: int):
        if decimal <= 0:
            return 0
        else:
            quotient, reminder = divmod(decimal, len(self.__BASE62))
            ans: str = self.__BASE62[reminder]

            while True:
                if quotient == 0:
                    break
                else:
                    quotient, reminder = divmod(quotient, len(self.__BASE62))
                    ans = self.__BASE62[reminder] + ans
            return ans

    def encode(self, string: str):
        if string:
            decimal: int = int.from_bytes(bytes(string, 'utf-8'), 'big')
            return self.__encodeToBase62(decimal)
        else:
            return 'Invalid String!'

    def decode(self, string: str):
        num: int = 0
        for idx, char in enumerate(string):
            power: int = (len(string) - (idx + 1))
            num += self.__BASE62.index(char) * (len(self.__BASE62)**power)

        return num.to_bytes((num.bit_length() + 7) // 8, 'big').decode('utf-8')


if __name__ == '__main__':
    string: str = 'Hello World!'
    EncodedText: str = Base62Converter().encode(string)
    DecodedText: str = Base62Converter().decode(EncodedText)
    print('Text: {0}\nEncoded: {1}\nDecoded: {2}'.format(string, EncodedText, DecodedText))
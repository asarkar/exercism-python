class PhoneNumber:
    def __init__(self, number: str) -> None:
        num = []
        for x in number:
            if x.isdigit():
                num.append(x)
            elif x.isspace():
                continue
            elif x.isalpha():
                raise ValueError('letters not permitted')
            elif x not in {'+', '(', ')', '.', '-'}:
                raise ValueError('punctuations not permitted')

        n = len(num)
        if (n == 11 and num[0] == '1') or (n == 10):
            xs = ''.join(num[-10:])
            self.area_code, self.exchange_code, self.line_number = PhoneNumber.parse(xs)
            self.number = xs
        elif n == 11 and num[0] != '1':
            raise ValueError('11 digits must start with 1')
        elif n > 11:
            raise ValueError('must not be greater than 11 digits')
        elif n < 10:
            raise ValueError('must not be fewer than 10 digits')

    def pretty(self) -> str:
        return '-'.join([f'({self.area_code})', self.exchange_code, self.line_number])

    @staticmethod
    def parse(num: str, name: str = None) -> str | tuple[str, str, str]:
        n = len(num)
        if n == 10:
            area_code = num[:3]
            exchange_code = num[3:6]
            return PhoneNumber.parse(area_code, 'area'), PhoneNumber.parse(exchange_code, 'exchange'), num[6:]
        if n == 3:
            if num[0] == '0':
                raise ValueError(f'{name} code cannot start with zero')
            if num[0] == '1':
                raise ValueError(f'{name} code cannot start with one')
            return num
        return None

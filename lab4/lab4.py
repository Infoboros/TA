G_NOT_TERMINALS = 'SZOPYWE'
G_TERMINALS = '{[a=<!+*]}(,)'

RULES = [('S', 'OZ'),
         ('Z', 'S'),
         ('Z', ''),
         ('O', '{P'),
         ('P', '[S]Y}'),
         ('P', 'Y[S]}'),
         ('O', 'a=E'),
         ('Y', 'aW'),
         ('W', '=a'),
         ('W', '<a'),
         ('Y', '!(Y)'),
         ('E', '+(E,E)'),
         ('E', '*(E,E)'),
         ('E', 'a')]


class MP:
    class ParseError(Exception):
        def __init__(self):
            super().__init__('Цепочка не пренадлежит языку')

    TABLE = {
        'S': {
            '{': RULES[0],
            'a': RULES[0]
        },

        'Z': {
            '{': RULES[1],
            'a': RULES[1],
            '$': RULES[2]
        },

        'O': {
            '{': RULES[3],
            'a': RULES[6]
        },

        'P': {
            '[': RULES[4],
            'a': RULES[5],
            '!': RULES[5]
        },

        'Y': {
            'a': RULES[7],
            '!': RULES[10]
        },

        'W': {
            '=': RULES[8],
            '<': RULES[9]
        },

        'E': {
            'a': RULES[13],
            '+': RULES[11],
            '*': RULES[12]
        }
    }

    def _print_rule(self, rule: (str, str)):
        rule_num = RULES.index(rule) + 1
        print(f'{" " if rule_num < 10 else ""}{rule_num}. {rule[0]} -> {rule[1] if rule[1] else "e"}')

    def check(self, chain: str):
        stack = ['$', 'S']
        chain += '$'
        indexInSym = 0
        run_flag = True
        print('Вывод')
        while run_flag:
            X = stack[-1]
            if (X in G_TERMINALS) or (X == '$'):
                if X == chain[indexInSym]:
                    stack.pop()
                    indexInSym += 1
                else:
                    raise MP.ParseError()
            else:
                try:
                    rule: (str, str) = MP.TABLE[X][chain[indexInSym]]  # тут вылетит ошибка если ячейка таблицы пуста
                    stack.pop()
                    stack += rule[1][::-1]
                    self._print_rule(rule)
                except:
                    raise MP.ParseError()

            run_flag = (X != '$')


class Recurse:

    def __init__(self, chain: str):
        self.chain = chain

    def S(self):
        FIRST = {
            '{': 'OZ',
            'a': 'OZ',
        }
        try:
            inSym = self.chain[0]
            print(f'S -> {FIRST[inSym]}')
            self.parse(FIRST[inSym])
        except:
            raise MP.ParseError()  # В данном случае из нетерминала не выводится пустая цепочка

    def Z(self):
        FIRST = {
            '{': 'S',
            'a': 'S'
        }
        try:
            inSym = self.chain[0]
            print(f'Z -> {FIRST[inSym]}')
            self.parse(FIRST[inSym])
        except:
            if not self.chain:
                print('Цепочка принадлежит языку')
            else:
                raise MP.ParseError()  # В данном случае из нетерминала не выводится пустая цепочка

    def O(self):
        FIRST = {
            '{': '{P',
            'a': 'a=E'
        }
        try:
            inSym = self.chain[0]
            print(f'O -> {FIRST[inSym]}')
            self.parse(FIRST[inSym])
        except:
            raise MP.ParseError()  # В данном случае из нетерминала не выводится пустая цепочка

    def P(self):
        FIRST = {
            '[': '[S]Y}',
            'a': 'Y[S]}',
            '!': 'Y[S]}'
        }
        try:
            inSym = self.chain[0]
            print(f'P -> {FIRST[inSym]}')
            self.parse(FIRST[inSym])
        except:
            raise MP.ParseError()  # В данном случае из нетерминала не выводится пустая цепочка

    def Y(self):
        FIRST = {
            'a': 'aW',
            '!': '!(Y)'
        }
        try:
            inSym = self.chain[0]
            print(f'Y -> {FIRST[inSym]}')
            self.parse(FIRST[inSym])
        except:
            raise MP.ParseError()  # В данном случае из нетерминала не выводится пустая цепочка

    def W(self):
        FIRST = {
            '=': '=a',
            '<': '<a'
        }
        try:
            inSym = self.chain[0]
            print(f'Y -> {FIRST[inSym]}')
            self.parse(FIRST[inSym])
        except:
            raise MP.ParseError()  # В данном случае из нетерминала не выводится пустая цепочка

    def E(self):
        FIRST = {
            'a': 'a',
            '+': '+(E,E)',
            '*': '*(E,E)'
        }
        try:
            inSym = self.chain[0]
            print(f'E -> {FIRST[inSym]}')
            self.parse(FIRST[inSym])
        except:
            raise MP.ParseError()  # В данном случае из нетерминала не выводится пустая цепочка

    def parse(self, u:str):
        v = u
        while v:
            X = v[0]
            z = v[1::]
            if X in G_TERMINALS:
                if X != self.chain[0]:
                    raise MP.ParseError()
                else:
                    self.chain = self.chain[1::]
            else:
                {
                    'S': self.S,
                    'Z': self.Z,
                    'O': self.O,
                    'P': self.P,
                    'Y': self.Y,
                    'W': self.W,
                    'E': self.E,
                }[X]()
            v = z


if __name__ == '__main__':
    print('Введите цепочку:', end=' ')
    # chain = input()
    chain = 'a=*(a,a)'
    print('Выберите реализацию:')
    print('1 - низходящий МП-распознаватель')
    print('2 - метод рекурсивного спуска')

    # flag = int(input())
    flag = 2
    if flag == 1:
        try:
            MP().check(chain)
            print('Цепочка принадлежит языку')
        except Exception as e:
            print(e)
    else:
        try:
            Recurse(chain).S()
        except Exception as e:
            print(e)
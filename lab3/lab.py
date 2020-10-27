class RecognizeException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)


class Recognizer:
    YES = 'допустить'
    NO = 'отвергнуть'

    TABLE = [[2, -2, 6, 6, 6, 6, 2],  # Апостроф
             [-1, -2, -3, -1, -1, -1, 0],  # Плюс
             [-1, -2, 1, 1, 1, 1, -1]].append(  # Диез
             [[-1, 3, -4, 4, 5, -1, -1]].append(  # Восьмиричные числа
             [[-1, -2, 2, 2, 2, 2, -1]]))  # Все остальные символы

    ERROR_DICT ={
        -1:'Строка начинается с апострофа',
        -2:'После Диез должна стоять хотя бы одна восьмиричная цифра',
        -3: '+ ставится только между частями строки',
        -4:
    }

APOSTROPH = "'"
PLUS = '+'
DIEZ = '#'
EIGTH_DIGIT = '01234567'


def _S0(self, chain: str):
    if not chain:
        return self.NO
    if chain[0] in self.APOSTROPH:
        return self._S2(chain[1:])
    else:
        raise RecognizeException('Строка начинается с апострофа')


def _S1(self, chain: str):
    if not chain:
        return self.NO
    ch = chain[0]
    if ch in self.EIGTH_DIGIT:
        return self._S3(chain[1:])
    else:
        raise RecognizeException('После Диез должна стоять хотя бы одна восьмиричная цифра')


def _S2(self, chain: str):
    if not chain:
        return self.NO
    ch = chain[0]
    if ch in self.APOSTROPH:
        return self._S6(chain[1:])
    elif ch in self.DIEZ:
        return self._S1(chain[1:])
    elif ch in self.PLUS:
        raise RecognizeException('+ ставится только между частями строки')
    elif ch in self.EIGTH_DIGIT:
        raise RecognizeException('Восьмиричные числа пишутся после диеза')
    else:
        return self._S2(chain[1:])


def _S3(self, chain: str):
    if not chain:
        return self.NO
    ch = chain[0]
    if ch in self.APOSTROPH:
        return self._S6(chain[1:])
    elif ch in self.DIEZ:
        return self._S1(chain[1:])
    elif ch in self.PLUS:
        raise RecognizeException('+ ставится только между частями строки')
    elif ch in self.EIGTH_DIGIT:
        raise self._S4(chain[1:])
    else:
        return self._S2(chain[1:])


def _S4(self, chain: str):
    if not chain:
        return self.NO
    ch = chain[0]
    if ch in self.APOSTROPH:
        return self._S6(chain[1:])
    elif ch in self.DIEZ:
        return self._S1(chain[1:])
    elif ch in self.PLUS:
        raise RecognizeException('+ ставится только между частями строки')
    elif ch in self.EIGTH_DIGIT:
        raise self._S5(chain[1:])
    else:
        return self._S2(chain[1:])


def _S5(self, chain: str):
    if not chain:
        return self.NO
    ch = chain[0]
    if ch in self.APOSTROPH:
        return self._S6(chain[1:])
    elif ch in self.DIEZ:
        return self._S1(chain[1:])
    elif ch in self.PLUS:
        raise RecognizeException('+ ставится только между частями строки')
    elif ch in self.EIGTH_DIGIT:
        raise RecognizeException('Слишком много восьмиричных чисел под ряд')
    else:
        return self._S2(chain[1:])


def _S6(self, chain: str):
    if not chain:
        return self.YES
    ch = chain[0]
    if ch in self.APOSTROPH:
        return self._S2(chain[1:])
    elif ch in self.DIEZ:
        raise RecognizeException('Диез ставится внутри части строки')
    elif ch in self.PLUS:
        return self._S0(chain[1:])
    elif ch in self.EIGTH_DIGIT:
        raise RecognizeException('Восьмиричные числа пишутся после диеза')
    else:
        raise RecognizeException('Буквы пишутся внутри апострофов')


def check_inter(self, chain: str):
    pass


def check_comp(self, chain: str):
    return self._S0(chain)


if __name__ == '__main__':
    recognizer = Recognizer()
    print('Вы хотите работать с консолью или файлом?')
    print('1 - консоль')
    print('2 - файл')

    flag = 1
    if flag == 1:
        print('Введите цепочку', end=' ')
        chain = input()

        print('Выберите тип реализации')
        print('1 - компиляционный')
        print('2 - интерпретационный')
        flag = 1
        if flag == 1:
            print(recognizer.check_comp(chain))
        elif flag == 2:
            pass

    elif flag == 2:
        pass

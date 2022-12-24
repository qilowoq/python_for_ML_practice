class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        self._bank = bank
        self._entry = entry
        self._targets = targets
        self._close = close
        
    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        return self._targets

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        return [round((i/self._entry - 1)*100, 3) for i in self._targets]

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        return [round(self._bank*i/self._entry, 3) for i in self._targets]

    def __str__(self):
        # текстовое представление сделки
        s1 = 'BANK: {}\nSTART_PRICE: {}\nSTOP_PRICE: {}\n'.format(self._bank, self._entry, self._close)
        l2 = []
        pers = self.get_target_percents()
        bnks = self.get_target_banks()
        for i, tar in enumerate(self._targets):
            l2.append('{} target: {}\nPercent: {}%\nBank: {} \n\n'.format(i+1, tar, pers[i], bnks[i]))
        return s1 + '\n' + ''.join(l2)


def read_data(name):
    with open(name, 'r') as f:
        return f.read()

def process(data):
    ans = []
    for item in data.split('-----'):
        dd = dict()
        for line in item.split('\n'):
            if line.startswith('BANK'):
                dd['bank'] = float(line.strip().split()[-1])
            elif line.startswith('Вход'):
                dd['entry'] = float(line.strip().split()[-1])
            elif line.startswith('Таргет'):
                dd['targets'] = list(map(float, line.strip().split(': ')[-1].split(', ')))
            elif line.startswith('Выход'):
                dd['close'] = float(line.strip().split()[-1])
        if dd != dict():
            ans.append(dd)
    return ans
            

def write_data(file_name, data, t='a'):
    with open(file_name, t) as f:
        f.write(data)
        f.write('-----\n')


def main():
    content = read_data('deals.txt')
    write_data('out.txt', '', t='w')
    for item in process(content):
        strdeal = StrategyDeal(**item)
        write_data('out.txt', str(strdeal))


if __name__ == '__main__':
    main()

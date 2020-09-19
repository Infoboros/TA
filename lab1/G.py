from random import choices

class G:
    def __init__(self, n=set(), a=set(), p=dict(), s='S'):
        self.N : set  = n
        self.A : set  = a
        self.P : dict = p
        self.S : str  = s

    def input_n(self):
        print("Введите конечное множество нетерминальных символов", end=": ")
        self.N.clear()
        for n in input().split():
            self.N.add(n)

    def input_a(self):
        print("Введите конечное множество терминальных символов", end=": ")
        self.A.clear()
        for a in input().split():
            self.A.add(a)

    def input_p(self):
        self.P.clear()
        print("Введите колличество правил", end=": ")
        count_p = int(input())
        print("Введите %d правил:" % count_p)
        for i in range(1, count_p+1):
            list_rule = input().split("->")
            key = list_rule[0]
            value = list_rule[1]
            if key in self.P.keys():
                self.P[key].append([value, i])
            else:
                self.P.update({key: [[value, i]]}.copy())

    def input_s(self):
        print("Введите начальный нетерминал", end=": ")
        self.S = input()

    def input_all(self):
        self.input_n()
        self.input_a()
        self.input_p()
        self.input_s()

    def _get_non_term_rules(self, non_term):
        rule_list = []
        rights = self.P[non_term]
        for r in rights:
            rule_list.append(str(r[1]) + ". " + non_term + "->" + r[0])
        rule_list.sort()
        return rule_list

    def __str__(self):
        print("КС-грамматика: ")
        rule_list = []
        for non_term in self.P.keys():
            rule_list += self._get_non_term_rules(non_term)
        rule_list.sort()
        return "\n".join(rule_list)

    def left_tree(self, chain, list_rule):
        offset = 0
        for rule in list_rule:
            newChain = chain[:offset]
            for ch_i in range(offset, len(chain)):
                newChain += chain[ch_i]
                if chain[ch_i] in self.N:
                    offset = len(newChain)
                    newChain += "(" + rule[0] + ")"
                    newChain += chain[ch_i+1:]
                    break

            chain = newChain
        return chain


    def left_vivod(self):
        print("Левый вывод\n")
        chain = self.S
        step = 1
        step_by_step = []

        while(True):
            chain.replace("e", "")
            flag = True
            newChain = ""
            for ch in chain:
                if (ch in self.N) and flag:
                    print("Шаг %d." % step)
                    step += 1

                    print("Промежуточная цепочка: %s" % chain)
                    flag = False
                    rules = self._get_non_term_rules(ch)
                    print("Можно применить правила:")
                    print("\n".join(rules))

                    rule = choices(self.P[ch])[0]
                    print("Применяем правило %d" % rule[1])
                    step_by_step.append(rule)
                    newChain += rule[0]
                else:
                    newChain += ch
            print()
            if (flag):
                break
            chain = newChain
        chain.replace("e", "")
        print("Шаг %d." % step)
        print("Терминальная цепочка: %s" % chain)
        print("Последовательность правил: %s" % ' '.join([str(step[1]) for step in step_by_step]))
        print("ЛСФ ДВ: " + self.left_tree(self.S, step_by_step).replace("e", ""))

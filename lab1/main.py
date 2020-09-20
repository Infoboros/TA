from G import G
if __name__ == "__main__":
    G = G()
    G.input_all()
    print("Левый вывод")

    print("Введите номера правил: ",end="")
    rule_list = map(int, input().split())
    if G.check_left_rules(rule_list):
        print("Да")
    else:
        print("Нет")
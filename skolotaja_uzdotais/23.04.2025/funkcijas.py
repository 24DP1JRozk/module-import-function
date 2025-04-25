def say_word(vards):
    """
    Izvada sveicienu ar personalizētu vārdu.

    Parametri:
    vards (str): Vārds, kuram tiks pievienots sveiciens.

    Atgriež:
    Nekas netiek atgriezts, rezultāts tiek izvadīts terminālī.
    """
    print("Hello,", vards)


def say_hello():
    """
    Izvada vienkāršu sveicienu "Hello".

    Šī funkcija neprasa nekādus ievades datus
    un izvada noklusēto sveicienu terminālī.
    """
    print("Hello")


def sum_2_nums(num_a: int, num_b: int):
    """
    Saskaita un izvada divu veselie skaitļu summu.

    Parametri:
    num_a (int): Pirmais skaitlis.
    num_b (int): Otrais skaitlis.

    Atgriež:
    Nekas netiek atgriezts, summa tiek izvadīta terminālī.
    """
    sum_nums = num_a + num_b
    print(sum_nums)

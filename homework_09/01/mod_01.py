# 9.1

"""
Обчислення площі круга
Обчислення довжини круга
"""


def circle_a(rad):
    # формула площі
    s_circle = 3.145926 * rad**2
    return s_circle


def circle_l(rad):
    # формула довжини 2*pi*r
    return 2 * 3.1415926 * rad


# ця функція спрацює лише при запуску з цього модуля, якщо з іншого не працює
def main():
    r = int(input("Який радіус кола?: >"))
    print("Площа круга = ", circle_a(r))
    print("Довжина круга = ", circle_l(r))


if __name__ == "__main__":
    main()

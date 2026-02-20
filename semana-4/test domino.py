import unittest

def contar_formas_dominos_3xn(n):
    """
    Calcula la cantidad de formas de cubrir un tablero 3xn con dominós 2x1.
    """

    if not isinstance(n, int) or n < 0:
        return 0

    if n % 2 == 1:
        return 0

    formas_completas = [0] * (n + 1)
    formas_con_hueco = [0] * (n + 1)

    formas_completas[0] = 1

    if n >= 2:
        formas_completas[2] = 3
        formas_con_hueco[2] = 1

    for i in range(4, n + 1, 2):
        formas_con_hueco[i] = formas_completas[i - 2] + formas_con_hueco[i - 2]
        formas_completas[i] = formas_completas[i - 2] + 2 * formas_con_hueco[i - 2]

    return formas_completas[n]


class PruebasDomino(unittest.TestCase):

    def prueba_n_0(self):
        self.assertEqual(contar_formas_dominos_3xn(0), 1)

    def prueba_n_2(self):
        self.assertEqual(contar_formas_dominos_3xn(2), 3)

    def prueba_n_4(self):
        self.assertEqual(contar_formas_dominos_3xn(4), 11)

    def prueba_n_8(self):
        self.assertEqual(contar_formas_dominos_3xn(8), 153)

    def prueba_n_impar(self):
        self.assertEqual(contar_formas_dominos_3xn(5), 0)

    def prueba_entrada_invalida(self):
        self.assertEqual(contar_formas_dominos_3xn(-3), 0)


if __name__ == "__main__":
    unittest.main()
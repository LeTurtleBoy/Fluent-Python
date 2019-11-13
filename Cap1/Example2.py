# -*- coding: latin-1 -*-
# Special Methods


class Polynomial:
    def __init__(self, coeff):
        err_message = "Arguments should be dict in the form {Exponent: Coefficient,...}"
        if type(coeff) is not dict:
            raise ValueError(err_message)
        coeff_ret = {}
        for key in sorted(coeff.keys())[::-1]:
            if coeff[key] != 0:
                coeff_ret[key] = coeff[key]
        self._coeff = coeff_ret

    def __repr__(self):
        rep = ' + '.join('{}*x^{}'.format(coe, exp)
                         if coe is not 1
                         else 'x^{}'.format(exp)
                         for (exp, coe) in self._coeff.items())
        rep = rep.replace(" x^0", " 1").replace("*x^0", "").replace("+ -", "- ")

        return rep

    def __abs__(self):
        for (exp, coeff) in self._coeff.items():
            self._coeff[exp] = abs(coeff)
        return self

    def __add__(self, other):
        result = {}
        other = other.get_dict()
        for key in self._coeff.keys():
            if key in other.keys():
                result[key] = self._coeff[key] + other[key]
            else:
                result[key] = self._coeff[key]
        for key in other.keys():
            if key in self._coeff.keys():
                pass
            else:
                result[key] = other[key]
        return Polynomial(result)

    def __sub__(self, other):
        result = {}
        other = other.get_dict()
        for key in self._coeff.keys():
            if key in other.keys():
                result[key] = self._coeff[key] - other[key]
            else:
                result[key] = self._coeff[key]
        for key in other.keys():
            if key in self._coeff.keys():
                pass
            else:
                result[key] = other[key]
        return Polynomial(result)

    def __mul__(self, other):
        if type(other) in [int, float]:
            for (key, value) in self._coeff.items():
                self._coeff[key] = other * value
            return self

        if type(other) is Polynomial:
            other = other.get_dict()
            results = []
            for (key, value) in other.items():
                temp = {}
                for (key_2, value_2) in self._coeff.items():
                    temp[key + key_2] = value * value_2
                results.append(Polynomial(temp))
            aux = results[0]
            for index in range(len(results)-1):
                aux = aux + results[index+1]
            return aux

    def __getitem__(self, x):
        sol = sum([c*x**e for (e, c) in self._coeff.items()])
        return sol

    def get_dict(self):
        return self._coeff

    def eval(self, x):
        sol = sum([c*x**e for (e, c) in self._coeff.items()])
        return sol


if __name__ == "__main__":
    try:
        base = [1, 2, 4, 5, 7]
        Pol_bad = Polynomial(base)
    except Exception as e:
        print("Error:", type(e), str(e))

    Pol1 = Polynomial({2: 1, 1: 2, 0: 1})
    Pol2 = Polynomial({2: 1, -1: -2, 0: 1})
    print("A = ", Pol1)
    print("B = ", Pol2)
    print("A + B = ", Pol1 + Pol2)
    print("A - B = ", Pol1 - Pol2)
    print("abs(B) = ", abs(Pol2))  # 2 * abs(Pol2)
    print("A * B = ", Pol1*Pol2)
    #print("2 * B = ", 2*Pol2)  # sobrecargar la suma para int
    print("B * 2 = ", Pol2*2)  # sobrecargar la mult para Poly
    print("A(10) = ", Pol1.eval(10))
    print(Pol1[10])

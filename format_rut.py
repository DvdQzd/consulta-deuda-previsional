class Rut:
    def formatter(rut):
        n = len(rut)
        if(n < 10):
            rut = "0" + rut
            n = 10

        part1 = rut[:n-8]
        part2 = rut[n-8:5]
        part3 = rut[n-5:]

        rut = part1 + "." + part2 + "." + part3
        return rut
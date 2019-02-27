def cost(x1, x2):
    #ini adalah fungsi matematika yang diberikan soal
    #nilai adalah sebagai cost
    #x1 --> solusi 1
    #x2 --> solusi 2

    nilai = (4 - 2.1 * x1 ** 2 + x1 ** 4. / 3) * x1 ** 2 + x1 * x2 + (-4 + 4 * x2 ** 2) * x2 ** 2
    return nilai

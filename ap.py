def acceptance_prob (old_cost, new_cost, temp):
    #ini untuk mencari nilai AP
    #digunakan saat nilai new_cost > nilai old_cost
    #dan sukses kalau AP > random()

    nilai = 2.71828 ** ((old_cost - new_cost)/temp)
    return nilai
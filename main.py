import random
import math_function
import ap

def simulated_annealing():
    sol1 = random.uniform(-10,10) #generate nilai dari -10 sampai 10
    sol2 = random.uniform(-10,10)
    old_cost = math_function.cost(sol1, sol2) #memasukkan fungsi yang telah ditentukan dosen
    t_mulai = 10000 #kenapa kalo dirubah jadi 1 sampai 0.00001 malah error
    t_stop  = 1
    alpha   = 0.93 #bebas ini mah
    while t_mulai > t_stop:
        count   = 1 #apa bedanya sama count yang ditaruh diluar loop
        while count < 100:
            sol1 = random.uniform(-10,10) #ini adalah neighbor dari tiap X nya
            sol2 = random.uniform(-10,10)
            new_cost = math_function.cost(sol1, sol2)
            a_p = ap.acceptance_prob(old_cost, new_cost, t_mulai) #ini keadaan kalau new_cost > old_cost
            if a_p > random.random():
                old_cost = new_cost
            count += 1
        t_mulai = t_mulai * alpha #ini untuk setiap kali loop yang luar
    print sol1, sol2, old_cost #bukan return, tapi print

simulated_annealing()
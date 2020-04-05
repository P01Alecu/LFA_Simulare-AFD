###########Simulare AFD
##in fisierul 'in.txt' se gasesc datele de intrare
##fisierul este de forma:
##stare_initiala Stari_finale
##cuvant cuvant cuvant......
##litera starea_din_care_pleaca starea_in_care_ajunge
##...
##litera starea_din_care_pleaca starea_in_care_ajunge


def parcurgere(start, sir):
    ok = True
    point = 0 #pointeaza litera pana la care s-a parcurs sirul
    f = open("out.txt", "a")
    f.write('Cuvantul: ' + str(sir) + '\n')

    while (start != '-1' and start != '-2' and point<len(sir)):
        f.write(str(start) + ' ' + str(sir[point:]) + "\n") #scrie in fisier
        print(str(start) + ' ' + str(sir[point:]))  #scrie in consola
        start = cautare(sir[point], start, m)
        if(start == -1 or start == -2):
            ok = False
            break
        point = point+1

    if(ok): #verifica daca starea in care s-a ajuns dupa parcurgerea cuvantului este finala
        f.write(str(start) + ' ' + "''\n") #scrie in fisier
        print(str(start) + ' ' + "''")  #scrie in consola
        ok = verificare(start, final)
    if(ok):
        f.write(str(start) + ' ' + "''\n")
        print(str(start) + ' ' + "''")
        f.write('Cuvantul este acceptat!\n')
        print('Cuvantul este acceptat!')
    else:
        if (start == '-2'):
            f.write('Automatul nu este afd!\n')
            print('Automatul nu este afd!')
        else:
            f.write('Nu se poate!\n')
            print('Nu se poate!')
    f.write('\n')
    f.close()

def cautare(litera, starea, text):  #cauta starea a carei tranzitie accepta o litera anume, si in caz ca sunt gasite mai multe (automatul nu este afd) returneaza -2, in caz ca nu s-a gasit returneaza -1
    start = '-1'
    for i in range(0, len(text.splitlines())):
        if(text.splitlines()[i][0] == litera and text.splitlines()[i][2] == starea):
            if (start != '-1'):
                start = '-2'
                return start
            else:
                start = text.splitlines()[i][4]
    return start


def verificare(vf, final):   #verifica daca starea in care s-a ajuns este stare finala
    ok = False
    for i in range(0, len(final)):
        if (final[i] == vf):
            ok = True
    return ok

f = open("in.txt", "r")
final = []
m = f.read()

start = str(m[0])    #starea initiala
final = m.splitlines()[0][2:].split()   #vector cu starile finale
f.close()
sir = m.splitlines()[1].split()


f = open("out.txt", "w")    #solutie simpla ptr a sterge un posibil vechi fisier "out.txt" si a creea unul nou in care se va face append
f.close()
for i in range(0, len(sir)):
    print()
    print(sir[i])
    parcurgere(start, sir[i])
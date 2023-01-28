from src.AstralObject import Polyanet

my_candidate_id = "2cec4c2a-c75f-4275-b16e-fd9a605aaeb4";

if __name__ == '__main__':
    for i in range(2, 9):
        p1 = Polyanet(i, i)
        p2 = Polyanet(i, 10-i)
        p1.delete()
        p2.delete()

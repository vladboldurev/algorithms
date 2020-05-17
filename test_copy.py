import copy

class CopyTest:

    def copy(self, a):
        print('copy')
        b = copy.copy(a)
        print(a)
        print(b)
        print(id(a))
        print(id(b))

    def deep_copy(self, a):
        print('deep_copy')
        b = copy.deepcopy(a)
        print(a)
        print(b)
        print(id(a))
        print(id(b))

class TestA:

    def __init__(self):
        self.a = [1, 2, 3]

    def __str__(self):
        result = ''
        for item in self.a:
            result += str(item)
        return "value: {}".format(result)

if __name__ == "__main__":
    # copy_test = CopyTest()
    # a = TestA()
    # copy_test.copy(a)
    # b = 10
    # copy_test.copy(b)
    # c = [95, 85, 82]
    # copy_test.copy(c)
    # a = TestA()
    # copy_test.deep_copy(a)
    # b = 112
    # copy_test.deep_copy(b)
    # c = [95, 85, 82]
    # copy_test.deep_copy(c)
    #
    # d = [95, 85, 82]
    # d1 = copy.copy(d)
    # d2 = copy.deepcopy(d)
    # d.append(100)
    # d[0] = 0
    # d1.append(200)
    # print('##########')
    # print(d)
    # print(d1)
    # print(d2)
    # print(id(d))
    # print(id(d1))
    # print(id(d2))

    result_A = TestA()
    result_B = result_A

    result_B.a = ['a', 'b', 'c']

    print("Original List: ")
    print(result_A)
    print(id(result_A))
    print("Shallow Copy:")
    print(result_B)
    print(id(result_B))
def remov_nb(n):
    # your code
    total = n * (n + 1) // 2
    result = []
    for a in range(1, n+1):
        b = (total - a) / (a + 1)
        if b.is_integer() and b <= n and b != a:
            result.append((a, int(b)))
    return result
  
  
  import codewars_test as test
        
@test.describe("Cheating Friend")
def tests():   
    def testing(n, exp):
        try:
            actual = removNb(n)
        except NameError:
            actual = remov_nb(n)
        test.assert_equals(actual, exp)
    @test.it("Fixed tests")
    def basics():
        testing(26, [(15, 21), (21, 15)])
        testing(100, [])
        testing(101, [(55, 91), (91, 55)])

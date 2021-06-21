n = gets.to_i
ans = (10**n - (9**n + 9**n - 8**n)) % (10**9 + 7)
puts ans

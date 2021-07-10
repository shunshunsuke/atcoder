n = gets.to_i
ans = ''
table = [*'a'..'z']
while n.positive?
  n -= 1
  ans += table[n % 26]
  n /= 26
end
puts ans.reverse

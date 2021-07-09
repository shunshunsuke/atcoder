N = gets.to_i
A = gets.split.map(&:to_i)
ans = 0
sum = 0
(1..N - 1).each do |i|
  sum += A[i - 1]
  ans += A[i] * sum
end
puts ans % (10**9 + 7)

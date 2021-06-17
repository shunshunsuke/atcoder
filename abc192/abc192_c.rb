N, K = gets.split.map(&:to_i)
cnt = 0
a = N
while cnt < K
  g2 = a.to_s.chars.sort.join
  g1 = g2.reverse
  a = g1.to_i - g2.to_i
  cnt += 1
end
puts a

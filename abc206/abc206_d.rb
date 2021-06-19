require 'set'
N = gets.to_i
A = gets.split.map(&:to_i)
count = {}
s = Set.new
(0..N / 2).each do |i|
  a, b = A[i], A[N - 1 - i]
  next if a == b
  a, b = b, a if a > b
  key = [a, b]
  count[key] = count[key].to_i + 1
  s.add(a)
  s.add(b)
end
if count.size.zero?
  puts 0
else
  ans = 1
  max = count.sort_by { |_, v| v }.reverse
  a, b = max[0][0][0], max[0][0][1]
  s.delete(a)
  s.delete(b)
  ans += s.size
  puts ans
end

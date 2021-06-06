N = gets.to_i
A = gets.split.map(&:to_i)
ans = 0
A.each do |a|
  x = a - 10
  ans += x if x > 0
end
puts ans

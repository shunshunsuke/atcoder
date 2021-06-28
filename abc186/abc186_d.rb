N = gets.to_i
A = gets.split.map(&:to_i).sort
ans = 0
A.each_with_index do |a, i|
  ans += i * a - (N - 1 - i) * a
end
puts ans

n = gets.chomp.split('').map(&:to_i)
if (n.sum % 3).zero?
  ans = 0
else
  a1 = 0
  a2 = 0
  n.each do |nn|
    a1 += 1 if nn % 3 == 1
    a2 += 1 if nn % 3 == 2
  end
  ans = [(a1 % 3 - a2 % 3).abs, (a1 - a2).abs].min
  ans = -1 if ans >= n.size
end
puts ans

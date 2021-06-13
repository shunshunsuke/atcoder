N = gets.chomp.to_s
if N.size < 4
  puts 0
  exit
end
ans = 0
3.step(N.size - 1, 3) do |dig|
  max = 10**(dig + 3) - 1
  max = N.to_i if N.to_i < max
  ans += (dig / 3) * ((max - 10**dig) + 1)
end
puts ans

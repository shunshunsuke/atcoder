a, b = gets.split.map(&:to_i)
ans = b - a
if ans < 0
  puts 0
else
  puts ans + 1
end

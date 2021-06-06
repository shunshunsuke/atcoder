a, b, c = gets.split.map(&:to_i)
if a == b
  puts c
elsif b == c
  puts a
elsif a == c
  puts b
else
  puts 0
end

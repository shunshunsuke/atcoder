N, X = gets.split.map(&:to_i)
a = gets.split.map(&:to_i)
b = []
a.each_with_index do |aa, i|
  if (i + 1) % 2 == 0
    b << aa - 1
  else
    b << aa
  end
end
if X >= b.sum
  puts 'Yes'
else
  puts 'No'
end

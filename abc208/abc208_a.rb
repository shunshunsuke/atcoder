a, b = gets.split.map(&:to_i)
if b <= a * 6 && b >= a
  puts 'Yes'
else
  puts 'No'
end

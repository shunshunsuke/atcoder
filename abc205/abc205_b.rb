N = gets.to_i
A = gets.split.map(&:to_i)
x = (1..N).to_a
if A.sort == x
  puts 'Yes'
else
  puts 'No'
end

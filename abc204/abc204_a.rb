x, y = gets.split.map(&:to_i)
if x == y
  puts x
else
  a = [0, 1, 2]
  a.delete(x)
  a.delete(y)
  puts a[0]
end

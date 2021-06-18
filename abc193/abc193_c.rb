require 'set'
N = gets.to_i
a = 2
s = Set.new
while a**2 <= N
  b = 2
  while a**b <= N
    s.add(a**b)
    b += 1
  end
  a += 1
end
puts N - s.size

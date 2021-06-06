N = gets.to_i
T = gets.split.map(&:to_i)
if N == 1
  puts T[0]
  exit
end
T.sort!
o1 = T.pop
o2 = T.pop
t1 = o1
t2 = o2
until T.empty?
  if o1 > o2
    o1 -= o2
    o2 = T.pop
    t2 += o2
  else
    o2 -= o1
    o1 = T.pop
    t1 += o1
  end
end
puts t1 > t2 ? t1 : t2

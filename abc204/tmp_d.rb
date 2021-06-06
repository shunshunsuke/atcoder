N = gets.to_i
T = gets.split.map(&:to_i)
ans = Float::INFINITY
(1..N / 2).each do |i|
  T.combination(i).to_a.each do |t|
    o1 = t.sum
    o2 = T.sum - o1
    x = [o1, o2].max
    ans = x if x < ans
  end
end
puts ans
tmp = []
(1..100).each do |i|
  tmp << i
end
puts tmp.join(' ')

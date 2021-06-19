require 'set'
N, M = gets.split.map(&:to_i)
AB = []
M.times do
  a, b = gets.split.map(&:to_i)
  AB << [a, b]
end
K = gets.to_i
CD = []
K.times do
  c, d = gets.split.map(&:to_i)
  CD << [c, d]
end

ans = 0
[0, 1].repeated_permutation(K).to_a.each do |ptn|
  tmp = 0
  s = Set.new
  CD.each_with_index do |cd, i|
    s.add(cd[ptn[i]])
  end
  AB.each do |ab|
    tmp += 1 if s.include?(ab[0]) && s.include?(ab[1])
  end
  ans = tmp if tmp > ans
end
puts ans

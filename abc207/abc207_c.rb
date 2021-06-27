N = gets.to_i
tlrs = [[]]
N.times do
  tlrs << gets.split.map(&:to_i)
end

ans = 0
(1..N).to_a.combination(2).to_a.each do |pair|
  tlr1 = tlrs[pair[0]]
  tlr2 = tlrs[pair[1]]
  t1 = tlr1[0]
  l1 = tlr1[1]
  r1 = tlr1[2]
  t2 = tlr2[0]
  l2 = tlr2[1]
  r2 = tlr2[2]
  if (l1 <= l2 && l2 < r1) || (l1 < r2 && r2 <= r1) || (l2 < l1 && r1 < r2)
    ans += 1
  elsif r1 == l2
    ans += 1 if [1, 3].include?(t1) && [1, 2].include?(t2)
  elsif l1 == r2
    ans += 1 if [1, 2].include?(t1) && [1, 3].include?(t2)
  end
end
puts ans

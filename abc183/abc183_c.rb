N, K = gets.split.map(&:to_i)
T = Array.new { [] }
N.times do
  T << gets.split.map(&:to_i)
end
ans = 0
(1..N - 1).to_a.permutation.to_a.each do |route|
  sum = T[0][route[0]] + T[route[-1]][0]
  (route.size - 1).times do |i|
    sum += T[route[i]][route[i + 1]]
  end
  ans += 1 if sum == K
end
puts ans

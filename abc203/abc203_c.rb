n, k = gets.split.map(&:to_i)
friends = {}
n.times do
  a, b = gets.split.map(&:to_i)
  friends[a] = friends[a].to_i + b
end
friends = friends.sort
ans = k
friends.each do |a, b|
  break if a > ans
  ans += b
end
puts ans

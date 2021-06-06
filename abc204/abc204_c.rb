N, M = gets.split.map(&:to_i)
G = Array.new(N) { [] }
M.times do
  a, b = gets.split.map(&:to_i)
  G[a - 1] << b - 1
end
ans = 0
N.times do |i|
  ans += 1
  seen = Array.new(N, false)
  seen[i] = true
  stack = []
  stack << i
  until stack.empty?
    G[stack.pop].each do |v|
      next if seen[v]
      seen[v] = true
      stack << v
      ans += 1
    end
  end
end
puts ans

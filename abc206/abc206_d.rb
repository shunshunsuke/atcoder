N = gets.to_i
A = gets.split.map(&:to_i)
G = Array.new(A.max + 1) { [] }
(0..N / 2).each do |i|
  a = A[i]
  b = A[N - 1 - i]
  next if a == b
  G[a] << b
  G[b] << a
end

ans = 0
seen = Array.new(A.max + 1, false)
(A.max + 1).times do |i|
  next if seen[i] || G[i].empty?
  size = 1
  seen[i] = true
  todo = [i]
  until todo.empty?
    v = todo.pop
    G[v].each do |nxt|
      next if seen[nxt]
      seen[nxt] = true
      todo.push(nxt)
      size += 1
    end
  end

  ans += size - 1
end
puts ans

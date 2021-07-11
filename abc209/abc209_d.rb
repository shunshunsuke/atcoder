N, Q = gets.split.map(&:to_i)
@G = Array.new(N + 1) { [] }
(N - 1).times do
  a, b = gets.split.map(&:to_i)
  @G[a] << b
  @G[b] << a
end

def dps
  seen = Array.new(N + 1, nil)
  seen[1] = 0
  queue = [1]
  while queue.size.positive?
    t = queue.pop
    routes = @G[t]
    routes.each do |r|
      unless seen[r]
        queue.push(r)
        seen[r] = seen[t] + 1
      end
    end
  end
  seen
end

seen = dps
Q.times do
  c, d = gets.split.map(&:to_i)
  if (seen[d] - seen[c]).even?
    puts 'Town'
  else
    puts 'Road'
  end
end

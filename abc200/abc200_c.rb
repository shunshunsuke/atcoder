N = gets.to_i
h = {}
A = gets.split.map do |a|
  a = a.to_i % 200
  h[a] = h[a].to_i + 1
  a
end
ans = 0
h.each do |key, val|
  ans += (val * (val - 1)) / 2
end
puts ans

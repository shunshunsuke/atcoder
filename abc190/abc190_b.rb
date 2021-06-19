N, S, D = gets.split.map(&:to_i)
ans = 'No'
N.times do
  x, y = gets.split.map(&:to_i)
  if x < S && y > D
    ans = 'Yes'
    break
  end
end
puts ans

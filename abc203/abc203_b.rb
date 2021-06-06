N, K = gets.split.map(&:to_i)
ans = 0
N.times do |i|
  K.times do |j|
    ans += (i + 1) * 100 + j + 1
  end
end
puts ans

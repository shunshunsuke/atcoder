N = gets.to_i
waru = 10**9 + 7
C = gets.split.map(&:to_i).sort
ans = 1
C.each_with_index do |c, i|
  ans = (ans * [0, c - i].max) % waru
end
puts ans

N = gets.to_i
A = gets.split.map(&:to_i)
A.sort!
ans = (N * (N - 1)) / 2
prev = 0
count = 0
A.each_with_index do |a, i|
  if a == prev
    count += 1
    ans -= (count * (count - 1)) / 2 if i == A.size - 1
  else
    if count > 1
      ans -= (count * (count - 1)) / 2
    end
    count = 1
    prev = a
  end
end
puts ans

N = gets.to_i
ans = N.to_s.size
a = 2
while a * a <= N
  if (N % a).zero?
    b = (N / a).to_s.size
    ans = b if b < ans
  end
  a += 1
end
puts ans

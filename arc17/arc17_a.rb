N = gets.to_i
i = 2
ans = 'YES'
while i * i <= N
  if (N % i).zero?
    ans = 'NO'
    break
  end
  i += 1
end
puts ans

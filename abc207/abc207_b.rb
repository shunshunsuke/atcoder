a, b, c, d = gets.split.map(&:to_i)
if c * d - b <= 0
  puts -1
else
  ans = 1
  loop do
    if (a + ans * b) <= (c * ans) * d
      puts ans
      exit
    end
    ans += 1
  end
end

N = gets.chomp
ans = 0
2.step(N.size, 2) do |n|
  (10**(n / 2 - 1)..10**(n / 2) - 1).each do |x|
    ans += 1 if (x.to_s * 2).to_i <= N.to_i
  end
end
puts ans

N = gets.to_i
(1..10**6).each do |i|
  if (i.to_s * 2).to_i > N
    puts i - 1
    exit
  end
end

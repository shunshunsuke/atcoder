N = gets.to_i
ans = N
(1..N).each do |n|
  if n.to_s.split('').include?('7')
    ans -= 1
  elsif n.to_s(8).include?('7')
    ans -= 1
  end
end
puts ans

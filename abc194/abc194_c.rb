N = gets.to_i
A = gets.split.map(&:to_i)
C = {}
A.each do |a|
  C[a] = C[a].to_i + 1
end

ans = 0
(-200..199).each do |i|
  (i + 1..200).each do |j|
    ans += C[i].to_i * C[j].to_i * (i - j)**2
  end
end
puts ans

N = gets.to_i
dots = []
N.times do
  x, y = gets.split.map(&:to_i)
  dots << [x, y]
end

dots.combination(3).to_a.each do |tgt|
  dot1 = tgt[0]
  dot2 = [tgt[1][0] - dot1[0], tgt[1][1] - dot1[1]]
  dot3 = [tgt[2][0] - dot1[0], tgt[2][1] - dot1[1]]
  if dot2[1] * dot3[0] == dot3[1] * dot2[0]
    puts 'Yes'
    exit
  end
end
puts 'No'

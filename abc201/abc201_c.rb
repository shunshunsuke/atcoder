S = gets.chomp
valid = []
unknown = []
invalid = []
S.size.times do |i|
  case S[i]
  when 'o'
    valid << i.to_s
  when '?'
    unknown << i.to_s
  else
    invalid << i.to_s
  end
end

ans = 0
10000.times do |i|
  target = i.to_s.rjust(4, '0').split('')
  next unless (valid - target).empty?
  ans += 1 if (invalid - target).size == invalid.size
end
puts ans

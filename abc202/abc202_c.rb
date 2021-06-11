N = gets.to_i
A = gets.split.map(&:to_i)
B = gets.split.map(&:to_i)
C = gets.split.map(&:to_i)
a = {}
b = {}
c = {}
A.each_with_index do |val, i|
  if a[val].nil?
    a[val] = [i]
  else
    a[val] << i
  end
end
B.each_with_index do |val, i|
  if b[val].nil?
    b[val] = [i]
  else
    b[val] << i
  end
end
C.each_with_index do |val, i|
  if c[val - 1].nil?
    c[val - 1] = [i]
  else
    c[val - 1] << i
  end
end

ans = 0
a.each do |key, val|
  b[key]&.each do |bi|
    ans += val.size * c[bi].size unless c[bi].nil?
  end
end
puts ans

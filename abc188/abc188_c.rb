N = gets.to_i
A = gets.split.map(&:to_i)
half = A.each_slice(2**N / 2).to_a
val = [half[0].max, half[1].max].min
puts A.index(val) + 1

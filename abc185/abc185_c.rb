L = gets.to_i
c = (L - 11..L - 1).inject { |res, i| res * i }
p = (1..11).inject { |res, i| res * i }
puts c / p

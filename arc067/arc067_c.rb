N = gets.to_i
if N == 1
  puts 1
  exit
end
total = (1..N).to_a.inject { |result, i| result * i }
res = []
i = 2
while i * i <= total
  if (total % i).zero?
    ex = 0
    while (total % i).zero?
      ex += 1
      total /= i
    end
    res << ex + 1
  end
  i += 1
end
res << 2 unless total == 1

puts res.inject { |result, i| result * i } % (10**9 + 7)

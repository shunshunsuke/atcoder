a, b, c = gets.split.map(&:to_i)
if a > b
  puts 'Takahashi'
elsif a < b
  puts 'Aoki'
else
  if c.zero?
    puts 'Aoki'
  else
    puts 'Takahashi'
  end
end

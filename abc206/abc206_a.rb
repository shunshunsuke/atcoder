N = gets.to_i
ans = (1.08 * N).floor
if ans < 206
  puts 'Yay!'
elsif ans > 206
  puts ':('
else
  puts 'so-so'
end

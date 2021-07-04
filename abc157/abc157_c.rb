N, M = gets.split.map(&:to_i)
ans = Array.new(N, 0)
ans[0] = 1
pair = {}
M.times do
  s, c = gets.split.map(&:to_i)
  if !pair[s].nil? && pair[s] != c
    puts -1
    exit
  end
  pair[s] = c
  ans[s - 1] = c
end
if N > 1 && ans[0].zero?
  puts -1
elsif N == 1 && M.zero?
  puts 0
else
  puts ans.join('')
end

N = gets.to_i
S = gets.chomp.split('')
Q = gets.to_i
query = []
Q.times do
  query << gets.split.map(&:to_i)
end
ans = S
reverse = false
query.each do |q|
  if q[0] == 2
    reverse = !reverse
  else
    if reverse
      q[1] = if q[1] <= N
               N + q[1]
             else
               q[1] - N
             end
      q[2] = if q[2] <= N
               N + q[2]
             else
               q[2] - N
             end
    end
    ans[q[1] - 1], ans[q[2] - 1] = ans[q[2] - 1], ans[q[1] - 1]
  end
end
ans = ans[N..2 * N - 1].concat(ans[0..N - 1]) if reverse
puts ans.join

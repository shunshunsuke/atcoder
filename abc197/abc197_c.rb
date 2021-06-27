N = gets.to_i
A = gets.split.map(&:to_i)
ans = Float::INFINITY
[0, 1].repeated_permutation(N - 1) do |bits|
  tot = 0
  cur = 0
  (N - 1).times do |i|
    cur |= A[i]
    if bits[i] == 1
      tot ^= cur
      cur = 0
    end
  end
  cur |= A[N - 1]
  tot ^= cur
  ans = tot if tot < ans
end
puts ans

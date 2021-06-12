A, B, K = gets.split.map(&:to_i)
@dp = Array.new(A + 1) { Array.new(B + 1, 0) }
@dp[0][0] = 1

def find_kth(a, b, k)
  return 'b' * b if a.zero?
  return 'a' * a if b.zero?
  return 'a' + find_kth(a - 1, b, k) if k <= @dp[a - 1][b]
  'b' + find_kth(a, b - 1, k - @dp[a - 1][b])
end

(A + 1).times do |i|
  (B + 1).times do |j|
    @dp[i][j] += @dp[i - 1][j] if i > 0
    @dp[i][j] += @dp[i][j - 1] if j > 0
  end
end
puts find_kth(A, B, K)

N = gets.to_i
T = gets.split.map(&:to_i)
W = T.sum / 2
dp = Array.new(N + 1) { Array.new(W + 1, false) }
dp[0][0] = true
N.times do |i|
  (W + 1).times do |w|
    next unless dp[i][w]
    # i番目の料理を選ぶ場合
    dp[i + 1][w + T[i]] = true if w + T[i] <= W
    # i番目の料理を選ばない場合
    dp[i + 1][w] = true
  end
end
dp[N].each_with_index.reverse_each do |flag, w|
  if flag
    puts T.sum - w
    break
  end
end

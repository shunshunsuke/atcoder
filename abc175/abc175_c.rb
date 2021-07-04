x, K, D = gets.split.map(&:to_i)
x = x.abs
if K * D <= x
  ans = x - K * D
else
  threshold = (x.to_f / D).ceil
  ans = if (K - threshold).even?
          x - threshold * D
        else
          x - threshold * D + D
        end
end
puts ans.abs

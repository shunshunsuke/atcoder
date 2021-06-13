R, X, Y = gets.split.map(&:to_i)
g = Math.sqrt(X**2 + Y**2)
ans = if g == R
        1
      elsif g <= 2 * R
        2
      else
        (g / R).ceil
      end
puts ans

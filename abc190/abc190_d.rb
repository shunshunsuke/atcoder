N = gets.to_i
t = 2 * N
x = 1
ans = 0
while x * x <= t
  if (t % x).zero?
    y = t / x
    ans += 1 if (x + y).odd?
  end
  x += 1
end
puts ans * 2

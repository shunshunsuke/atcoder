p = gets.to_i
ans = 0
1.upto(10) do |i|
  if p <= (1..i).inject(1,:*) || i == 10
    tgt = p
    i.downto(1) do |j|
      a, b = tgt.divmod((1..j).inject(1,:*))
      ans += a
      tgt = b
    end
    break
  end
end
puts ans

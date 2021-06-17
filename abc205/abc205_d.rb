N, Q = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)
C = Array.new(N, 0)
A.each_with_index do |a, i|
  C[i] = a - i - 1
end
Q.times do
  k = gets.to_i
  if k > C[N - 1]
    puts A[N - 1] + (k - C[N - 1])
  else
    r = C.bsearch_index { |x| x >= k }
    if r.zero?
      puts k
    else
      puts A[r - 1] + (k - C[r - 1])
    end
  end
end

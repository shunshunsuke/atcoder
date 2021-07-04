N, K = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)
A_sort = A.sort
A.each do |a|
  i = A_sort.bsearch_index { |x| x >= a }
  a, b = K.divmod(N)
  if i <= b - 1
    puts a + 1
  else
    puts a
  end
end

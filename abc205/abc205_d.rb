require 'set'

N, Q = gets.split.map(&:to_i)
A = gets.split.map(&:to_i)
search = Set.new(A)
qa = []
Q.times do
  qa << gets.to_i
end

lower_hash = {}
qa.each do |q|
  if q >= A[-1]
    i = nil
  elsif q < A[0]
    i = 0
  else
    i = A.bsearch_index { |x| x >= q }
  end
  if i.nil?
    i = A.size
  elsif A[i] == q
    i += 1
  end
  lower_hash[q] = i
  if i.zero?
    puts q
    next
  end

  pos = 1
  while i > 0
    if search.include?(q + pos)
      pos += 1
      next
    end
    i -= 1
    pos += 1 if i > 0
  end
  puts q + pos
end

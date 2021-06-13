a, b, c = gets.split.map(&:to_i)
if a == b
  puts '='
elsif a >= 0 && b >= 0
  if a < b
    puts '<'
  elsif a == b
    puts '='
  else
    puts '>'
  end
elsif a >= 0 && b < 0
  if c.even?
    if a.abs < b.abs
      puts '<'
    elsif a.abs == b.abs
      puts '='
    else
      puts '>'
    end
  else
    puts '>'
  end
elsif a < 0 && b >= 0
  if c.even?
    if a.abs == b.abs
      puts '='
    elsif a.abs < b.abs
      puts '<'
    else
      puts '>'
    end
  else
    puts '<'
  end
else
  if c.even?
    if a == b
      puts '='
    elsif a < b
      puts '>'
    else
      puts '<'
    end
  else
    if a == b
      puts '='
    elsif a < b
      puts '<'
    else
      puts '>'
    end
  end
end

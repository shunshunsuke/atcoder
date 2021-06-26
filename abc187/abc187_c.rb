require 'set'
N = gets.to_i
S = Set.new
N.times do
  word = gets.chomp
  if word[0] == '!'
    w = word.delete_prefix('!')
    if S.include?(w)
      puts w
      exit
    end
  elsif S.include?("!#{word}")
    puts word
    exit
  end
  S.add(word)
end
puts 'satisfiable'

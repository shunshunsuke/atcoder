S = gets.chomp.reverse!
puts S.gsub(/6|9/, '6' => '9', '9' => '6')

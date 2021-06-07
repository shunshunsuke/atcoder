# http://algorithms.blog55.fc2.com/blog-entry-132.html
N = gets.to_i
A = gets.split.map(&:to_i)
A.push(0)

class Rectangle < Struct.new(:height, :pos)
end
ans = 0
stack = []
(N + 1).times do |i|
  rect = Rectangle.new(A[i], i)
  if stack.empty?
    stack.push(rect)
  else
    if stack[-1].height < rect.height
      stack.push(rect)
    elsif stack[-1].height > rect.height
      target = i
      while !stack.empty? && stack[-1].height >= rect.height
        pre = stack.pop
        area = pre.height * (i - pre.pos)
        ans = [ans, area].max
        target = pre.pos
      end
      rect.pos = target
      stack.push(rect)
    end
  end
end
puts ans

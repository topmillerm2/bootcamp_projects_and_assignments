# my_array = [3,5,1,2,7,9,8,13,25,32]
# puts my_array.reduce(:+)
# my_array.reject { |elem| puts elem if elem >10}


names = ["John", "KB", "Oliver", "Cory", "Matthew", "Christopher"]
# puts names.shuffle
# names.select { |elem| puts elem if elem.length >5} 

y = []
("a".."z").each { |elem| y << elem }
puts y.shuffle!.last
x= y.first
y.each { |elem| puts "This is a vowel" if x == "a", "i", "o", "u", "e"}

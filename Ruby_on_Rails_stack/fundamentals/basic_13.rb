# #print 1-255

(1..255).each { |i| puts i}

# #odd 1-255

(1..255).each { |i| puts i if i.odd? }

# #print sum
sum = 0 
(0..255).each { |i| puts "New Number: #{i} Sum: #{sum +=i}"}

#iterate thru array

[1 ,3, 5, 7, 9, 13].each { |elem| puts elem}

#find max

puts [-3, -5, -7].max 

# #get average
sum =0
my_array = [2, 10, 3]
my_array.each { |i| sum += i}
puts sum/my_array.length


# y=[]
(1..255).each { |i| y << i  if i.odd?}
puts y

#greater than Y
 arr = [1, 3, 5, 7]
 y = 3
 puts arr.count { |elem| elem > y}

#square the values
 arr = [1, 5, 10, -2]
 puts arr.map! { |elem| elem * elem }

# eliminate negative numbers 
arr = [1, 5, 10, -2]
puts arr.each_index { |index| arr[index] = 0 if arr[index] < 0}

#max, min, avg
arr = [1, 5, 10, -2]
{ max: arr.max, min: arr.min, average: arr.reduce(:+) / arr.length.to_f }

#shift values
arr = [1, 5, 10, 7, -2]
arr.rotate!(1)[arr.length-1] = 0
puts arr

#number to string
arr = [-1, -3, 2]
puts arr.each_index { |index| arr[index] = "Dojo" if arr[index] < 0 }
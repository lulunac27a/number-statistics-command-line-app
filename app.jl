using Statistics#use statistics package for stats
numbers = Int[]#list of numbers
while true
    println("Enter a number: ")#enter number value to add to list
    input = readline()#read input
    try
        push!(numbers, parse(Int, input))#parse input as integer and add to list
    catch
        break#if input is not a number, break out of loop and print statistics
        println("Invalid input. It will now print the statistics.")
    end
end
sort!(numbers)#sort numbers
println("Minimum: ", minimum(numbers))#minimum value
println("First quartile: ", quantile(numbers, 0.25))#first quartile
println("Median: ", median(numbers))#median value
println("Third quartile: ", quantile(numbers, 0.75))#third quartile
println("Maximum: ", maximum(numbers))#maximum value
println("Mean: ", mean(numbers))#mean value
println("Standard deviation: ", std(numbers))#standard deviation
while true
    println("Enter quartile value: ")#enter custom quartile value
    input = readline()#read input
    try
        quartile = parse(Float64, input)#parse input as float
        if quartile >= 0 && quartile <= 1#if quartile is between 0 and 1
            println("Quartile: ", quantile(numbers, quartile))#print quartile value
        else
            break#end the program
            println("Invalid quartile input. The program will now end.")
        end
    catch
        break#end the program
        println("Invalid input. The program will now end.")
    end
end
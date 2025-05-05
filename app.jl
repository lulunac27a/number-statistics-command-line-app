using Statistics
numbers = Int[]
while true
    println("Enter a number: ")
    input = readline()
    try
        push!(numbers, parse(Int, input))
    catch
        break
        print("Invalid input. It will now print the statistics.")
    end
end
sort!(numbers)
println("Minimum: ", minimum(numbers))
println("First quartile: ", quantile(numbers, 0.25))
println("Median: ", median(numbers))
println("Third quartile: ", quantile(numbers, 0.75))
println("Maximum: ", maximum(numbers))
println("Mean: ", mean(numbers))
println("Standard deviation: ", std(numbers))
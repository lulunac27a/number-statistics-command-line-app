using Statistics
numbers = Int[]
while true
    println("Enter a number: ")
    input = readline()
    try
        push!(numbers, parse(Int, input))
    catch
        break
        println("Invalid input. It will now print the statistics.")
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
while true
    println("Enter quartile value: ")
    input = readline()
    try
        quartile = parse(Float64, input)
        if quartile >= 0 && quartile <= 1
            println("Quartile: ", quantile(numbers, quartile))
        else
            break
            println("Invalid input. The program will now end.")
        end
    catch
        break
        println("Invalid input. The program will now end.")
    end
end
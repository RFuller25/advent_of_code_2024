global counter = 0

for i in 1:1000
    input_line = readline()
    split_input = split(input_line)
    ints_from_input = Int64[]

    for i in split_input
        push!(ints_from_input, parse(Int, i))
    end
    flag = "N"
    last = -1
    bad = false
    rules_broken = 0
    for i in ints_from_input
        rules_broken = 0
        if last == -1
            last = i 
            continue
        end
        if last == i 
            bad = true
            rules_broken = rules_broken + 1
        end
        if last < i && flag == "D"
            bad = true
            last = i
            rules_broken = rules_broken + 1
        end
        if last < i 
            flag = "I"
        end
        if last > i && flag == "I"
            last = i
            bad = true
            rules_broken = rules_broken + 1
        end
        if last > i 
            flag = "D"
        end
        if abs(last - i) > 3
            last = i
            bad = true
            rules_broken = rules_broken + 1
        end
        last = i
    end
    if rules_broken > 1
        global counter = counter + 1
    end 

end

println(counter)


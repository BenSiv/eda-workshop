-- generate dataset for exploratory data analysis workshop

using("dates")

local function get_salary(min, max)
    local salary = math.random(min, max)
    return salary
end

local function get_salary_day()
    local day_in_month = math.random(1, 10)
    return day_in_month
end

local function get_expenses_range()
    local expenses_range = {
        min = math.random(0, 500),
        max = math.random(500, 3000)
    }
    return expenses_range
end

local function get_expense(expenses_range)
    local expense = math.random(expenses_range.min, expenses_range.max)
    return expense
end

local function get_major_expense(expenses_range, factor)
    local expense = get_expense(expenses_range)
    local major_expense = expense * factor
    return major_expense
end

-- the probability to make an expence each day
local function get_expense_probability()
    local expense_probability = math.random()
    return expense_probability
end

local function get_person(id)
    -- define a person
    local person = {
        id = id,
        salary = get_salary(8000, 20000),
        salary_day = get_salary_day(),
        expenses_range = get_expenses_range(),
        expense_probability = get_expense_probability(),
        major_expenses_factor = math.random(2, 10)
    }

    return person
end

local function does_expend(person)
    local random_value = math.random()
    local expend = false
    if random_value > person.expense_probability then
        expend = true
    else
        expend = false
    end
    return expend
end

function generate_month(person, initial_balance, year, month)
    local data = {
        Id = {},
        In = {},
        Out = {},
        Balance = {}
    }
    local balance = initial_balance
    local day = 1
    local current_date = os.date("%Y-%m-%d", os.time{year=year, month=month, day=day})
    while get_month(current_date) == month do
        local balance_in = 0
        local balance_out = 0
        table.insert(data.Id, person.id)
        if get_day(current_date) == person.salary_day then
            balance_in = person.salary
            table.insert(data.In, balance_in)
        end
        if does_expend() then
            balance_out = get_expense(person.expenses_range)
            table.insert(data.out, balance_out)
        end
        balance = balance - balance_out + balance_out
        table.insert(data.balance, balance)
        day = day + 1
        current_date = os.date("%Y-%m-%d", os.time{year=year, month=month, day=day})
    end

    return data
end

function main()
    local person = get_person()
    generate_month(person, 1000, 2024, 1)
end
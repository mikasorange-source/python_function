# 入力チェック系（validate群）
# 0以上か、数字か
def validate_amount(amount):
    try:
        num = int(amount)
    except:
        return False
    if num <= 0:
        return False
    return True

# 数字に変換できるか
def validate_int_str(amount):
    try:
        num = int(amount)
    except:
        return False
    return True

# 既存カテゴリか、追加か
def validate_category(category):
    if category == 0:
        return True
    return False

# 0~カテゴリー数の範囲か
def validate_category2(category, category_list):
    if 0 <= category <= len(category_list):
        return True
    return False

# 計算系（return中心）
# remains辞書を返す
def calc_remains(budgets, expenses):
    remains = {}
    for category in budgets:
        remain = budgets[category] - expenses[category]
        remains[category] = remain
    return remains

# 総支出
def calc_total_expense(expenses):
    total_expense = 0
    for category in expenses:
        total_expense += expenses[category]
    return total_expense

# 総予算
def calc_total_budget(budgets):
    total_budget = 0
    for category in budgets:
        total_budget += budgets[category]
    return total_budget

# 消費率（％）辞書
def calc_rate(budgets, expenses):
    rates = {}
    for category in budgets:
        if budgets[category] == 0:
            rate = 0
        else:
            rate = expenses[category] / budgets[category]
        rates[category] = int(rate * 100)
    return rates

# 一番支出の多いカテゴリと金額を返す
def get_max_category(expenses):
    max_expense = -1
    max_category = ''
    for category in expenses:
        if expenses[category] > max_expense:
            max_expense = expenses[category]
            max_category = category
    print('一番支出の多いカテゴリは' + max_category + 'です（' + str(max_expense) + '円）')

# 判定系（judge / evaluate）
# 各カテゴリの判定を返す
def judge_category_health(budgets, expenses, category):
    budget = budgets[category]
    expense = expenses[category]
    total_expense = calc_total_expense(expenses)
    if expense > budget:
        return '危険'
    if category == '交通費':
        if 80< expense / budget <= 100 or expense / total_expense >= 50:
            return '注意'
        else:
            return '健全'
    else:
        if 70< expense / budget <= 100 or expense / total_expense >= 50:
            return '注意'
        else:
            return '健全'

def judge_overall_health(budgets, expenses, total_budget, total_expense):
    total_expense = calc_total_expense(expenses)
    total_budget = calc_total_budget(budgets)
    if total_expense / total_budget <= 0.7:
        return '健全'
    elif 0.7 < total_expense / total_budget <= 1:
        return '注意'
    else:
        return '危険'

def print_category_report(category, expenses, budgets, remains, rates, status):
    remains = calc_remains(budgets, expenses)
    rates = calc_rate(budgets, expenses)
    status = judge_category_health(budgets, expenses, category)
    print(category + '：支出' + str(expenses[category]) + '円・予算' + str(budgets[category]) + '円・残金' + str(remains[category]) + '円・消費率' + str(rates[category]) + '％・判定' + status)

def print_overall_report(expenses, budgets, total_expense, total_budget, overall_status):
    total_expense = calc_total_expense(expenses)
    total_budget = calc_total_budget(budgets)
    overall_status = judge_overall_health(budgets, expenses, total_budget, total_expense)
    print('総支出' + str(total_expense) + '円・総予算' + str(total_budget) + '円・全体判定' + overall_status)

def print_action_tips(budgets, expenses, category):
    danger = []
    for category in budgets:
        status = judge_category_health(budgets, expenses, category)
        if status == '危険':
            danger.append(category)
        else:
            continue
    if danger == []:
        print('危険カテゴリなし')
    else:
        text = ''
        for i in range(len(danger)):
            text += danger[i]
            if i != len(danger) - 1:
                text += '、' 
        print('来月は' + text + 'カテゴリの支出を抑えましょう')
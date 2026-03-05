budgets = {'食費':30000, '日用品':10000, '娯楽':15000, '交通費':10000, 'その他':20000}
expenses = {'食費':0, '日用品':0, '娯楽':0, '交通費':0, 'その他':0}
import utils

input_continue = '0'
category_list = list(budgets.keys())
while input_continue == '0':
    input_category = -1
    while True:
        input_category_str = 'a'
        while utils.validate_int_str(input_category_str) == False:
            menu = '0:追加'
            i = 1
            for category in category_list:
                menu += '/' + str(i) + ':' + category
                i += 1
            input_category_str = input('記録したい支出のカテゴリはなんですか？' + menu + '：')
            if utils.validate_int_str(input_category_str):
                input_category = int(input_category_str)
                break
            else:
                print('半角数字で入力してください')
        if utils.validate_category2(input_category, category_list) == True:
            if utils.validate_category(input_category):
                input_newcategory = input('追加したいカテゴリの名前を入力してください：')
                input_budget_str = 'a'
                while utils.validate_amount(input_budget_str) == False:
                    input_budget_str = input('追加したいカテゴリの1ヶ月の予算を入力してください：')
                    if utils.validate_amount(input_budget_str):
                        break
                    else:
                        print('0より大きい半角数字で入力してください')
                budgets[input_newcategory] = int(input_budget_str)
                expenses[input_newcategory] = 0
                category_list = list(budgets.keys())
                continue
            break
        else:
            print('そのカテゴリーはありません')

    input_expense = 'a'
    while utils.validate_amount(input_expense) == False:
        input_expense = input('いくら使いましたか？')
        if utils.validate_amount(input_expense):
            break
        else:
            print('0より大きい半角数字で入力してください')
    category_list = list(budgets.keys())
    real_category = category_list[input_category-1]
    expenses[real_category] += int(input_expense)

    while True:
        input_continue = input('今月の入力を続けますか？0:yes/1:no')
        if input_continue == '0' or input_continue == '1':
            break
        else:
            print('正しく入力してください')

remains = utils.calc_remains(budgets, expenses)
rates = utils.calc_rate(budgets, expenses)
total_expense = utils.calc_total_expense(expenses)
status = ''
total_budget = 0
overall_status = ''
for category in budgets:
    utils.print_category_report(category, expenses, budgets, remains, rates, status)
utils.print_overall_report(expenses, budgets, total_expense, total_budget, overall_status)
utils.get_max_category(expenses)
utils.print_action_tips(budgets, expenses, category)

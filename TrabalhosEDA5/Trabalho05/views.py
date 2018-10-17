from django.shortcuts import render

# Coins list used in coin changing algorithm
coins_list = [1, 5, 10, 25, 50, 100]


def home(request):
    if request.method == 'POST' and request.FILES['myfile'] and request.POST['selectedOption']:
        myfile = request.FILES['myfile']
        byte_str = myfile.file.read()

        # Convert to a "unicode" object
        text_obj = byte_str.decode('UTF-8')

        # Choosing algorithm options
        if request.POST['selectedOption'] == "Greed - Coin Changing":
            change_list = read_csv_coin(text_obj.splitlines())
            print(change_list)
            change_list_results = calculate_all_changes(change_list)
            print(change_list_results)
        elif request.POST['selectedOption'] == "Greed - Interval Scheduling":
            pass
        else:
            # Nothing to do
            pass

        columns_descriptions, all_data = read_csv(text_obj.splitlines())

        return render(request, 'result.html', {'columns_descriptions': columns_descriptions})
    else:
        # Nothing to do
        pass

    return render(request, 'home.html')


def read_csv_coin(file):
    change_list = []

    for line in file:
        change_list.append(int(line))

    return change_list


def calculate_all_changes(change_list):
    change_list_results = []

    for change in change_list:
        change_list_results.append(coin_changing(change))

    return change_list_results


def coin_changing(change_value):

    current_position = len(coins_list) - 1
    coins_selected = []

    while change_value != 0:
        if coins_list[current_position] > change_value:
            current_position -= 1
        elif current_position < 0:
            coins_selected.append(-1)
            return coins_selected
        else:
            change_value -= coins_list[current_position]
            coins_selected.append(coins_list[current_position])

    return coins_selected


def read_csv(file):
    all_data = []
    columns_descriptions = []

    # Save all csv data in a list of lists, removing '\n' at the last line element.
    for line in file:
        if not columns_descriptions:
            columns_descriptions = line.split(",")
            columns_descriptions[-1] = columns_descriptions[-1].strip("\n")
        else:
            line_splitted = line.split(",")
            line_splitted[-1] = line_splitted[-1].strip("\n")
            all_data.append(line_splitted)

    return columns_descriptions, all_data

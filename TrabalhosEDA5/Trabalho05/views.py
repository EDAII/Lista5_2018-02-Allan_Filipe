from django.shortcuts import render
from datetime import datetime
import time

# Coins list used in coin changing greed algorithm
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

            change_list_results, change_list_times, time_final_total = calculate_all_changes(change_list)

            change_list_full = coin_changing_formating_result(change_list, change_list_results, change_list_times)

            return render(request, 'result.html', {'algorithm': request.POST['selectedOption'],
                                                   'change_list_full': change_list_full,
                                                   'change_list': change_list,
                                                   'change_list_results': change_list_results,
                                                   'time_final_total': time_final_total,
                                                   'change_list_times': change_list_times})

        elif request.POST['selectedOption'] == "Greed - Interval Scheduling":
            columns_descriptions, all_data = read_csv_jobs(text_obj.splitlines())

            jobs_list = sorted(all_data, key=getKey)

            jobs_list = convert_to_datetime(jobs_list)

            jobs_selected, execution_time = interval_scheduling_jobs(jobs_list)

            return render(request, 'result.html', {'algorithm': request.POST['selectedOption'],
                                                   'columns_descriptions': columns_descriptions,
                                                   'jobs_list': jobs_list,
                                                   'jobs_selected': jobs_selected,
                                                   'execution_time': execution_time})
        else:
            # Nothing to do
            pass
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
    change_list_times = []
    time_initial_total = time.time()

    for change in change_list:
        time_initial = time.time()

        change_list_results.append(coin_changing(change))

        time_final = time.time() - time_initial

        change_list_times.append(time_final)

    time_final_total = time.time() - time_initial_total
    return change_list_results, change_list_times, time_final_total


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


def coin_changing_formating_result(change_list, change_list_results, change_list_times):
    change_list_full = []

    for i in range(len(change_list)):
        current_vector = []
        current_vector.append("{0:.2f}".format(change_list[i] / 100.00))
        current_vector = add_coins_count(current_vector, change_list_results[i])
        current_vector.append(round(change_list_times[i], 15))
        change_list_full.append(current_vector)

    return change_list_full


def add_coins_count(current_vector, change_list_results):
    coin_1 = 0
    coin_5 = 0
    coin_10 = 0
    coin_25 = 0
    coin_50 = 0
    coin_100 = 0

    for coin in change_list_results:
        if coin == 1:
            coin_1 += 1
        elif coin == 5:
            coin_5 += 1
        elif coin == 10:
            coin_10 += 1
        elif coin == 25:
            coin_25 += 1
        elif coin == 50:
            coin_50 += 1
        elif coin == 100:
            coin_100 += 1
        else:
            # Nothing to do.
            pass

    current_vector.append(coin_1)
    current_vector.append(coin_5)
    current_vector.append(coin_10)
    current_vector.append(coin_25)
    current_vector.append(coin_50)
    current_vector.append(coin_100)

    return current_vector


def read_csv_jobs(file):
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


def convert_to_datetime(jobs_list):
    for job in jobs_list:
        job[1] = datetime.strptime(job[1], '%H:%M:%S').time()
        job[2] = datetime.strptime(job[2], '%H:%M:%S').time()

    return jobs_list


def interval_scheduling_jobs(jobs_list):
    time_initial = time.time()

    jobs_selected = [jobs_list[0], ]
    jobs_list[0].append(True)
    current_position = len(jobs_selected) - 1

    for i in range(1, len(jobs_list)):
        if jobs_selected[current_position][2] <= jobs_list[i][1]:
            jobs_selected.append(jobs_list[i])
            jobs_list[i].append(True)
            current_position += 1
        else:
            jobs_list[i].append(False)

    time_final = time.time() - time_initial

    return jobs_selected, time_final


def getKey(item):
    return item[2]

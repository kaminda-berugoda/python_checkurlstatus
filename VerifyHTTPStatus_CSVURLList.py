# This script can be used to verify a list of URL's HTTP Status
import csv
import time
import urllib.request, urllib.error

#csv file path and name
csv_file_name = "path to your list"

with open(csv_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader: #Iterate through the CSV file's url list
        if line_count == 0: #Ignoring the first line as it is the header row
            line_count += 1
        else:
            url = row[0]
            line_count += 1

            try:
                conn = urllib.request.urlopen(url)
            except urllib.error.HTTPError as e:
                # Return code error (e.g. 404, 501, ...)
                print(url + ' - HTTPError: {}'.format(e.code))
            except urllib.error.URLError as e:
                # Not an HTTP-specific error (e.g. connection refused)
                print(url + ' - URLError: {}'.format(e.reason))
            else:
                # 200
                print(url + ' - good')
        time.sleep(5) #Process sleeps for 5 seconds this is to avoid the program being blocked from the server
        print(f'Processed {line_count} lines.')


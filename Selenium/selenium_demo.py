import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.


def get_top_scorers_matrix():
    driver.get('http://www.espn.com/nba/history/leaders')

    final_matrix = []
    for row_index, row in enumerate(driver.find_elements_by_tag_name("tr")):
        final_matrix.append([])
        for cell_index, cell in enumerate(row.find_elements_by_tag_name("td")):
            final_matrix[row_index].append(cell.text)

    return final_matrix


top_scorers = get_top_scorers_matrix()

for row_index, scorer_row in enumerate(top_scorers):
    if row_index < 2:
        continue
    for data_index, data in enumerate(scorer_row):
        if data_index == 2:
            delimiter = "///"
        else:
            delimiter = "**"
        print "**{data}{delimiter}".format(data=data, delimiter=delimiter),
        if data_index == 2:
            print("")

# driver.quit()
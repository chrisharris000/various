import openpyxl

def retrieve_speeding_data(file_name):
    data_2014 = {}
    data_2015 = {}
    
    book = openpyxl.load_workbook(file_name)
    curr_sheet = book.get_sheet_by_name("Report ")

    for row in range(19,615):
        postcode = curr_sheet.cell(row = row, column = 2).value
        
        n_offences_speed_2014 = curr_sheet.cell(row = row, column = 3).value
        value_speed_2014 = curr_sheet.cell(row = row, column = 4).value
        n_offences_police_2014 = curr_sheet.cell(row = row, column = 7).value
        value_police_2014 = curr_sheet.cell(row = row, column = 8).value

        n_offences_speed_2015 = curr_sheet.cell(row = row, column = 5).value
        value_speed_2015 = curr_sheet.cell(row = row, column = 6).value
        n_offences_police_2015 = curr_sheet.cell(row = row, column = 9).value
        value_police_2015 = curr_sheet.cell(row = row, column = 10).value
        
        data_2014[postcode] = [[n_offences_speed_2014, value_speed_2014],[n_offences_police_2014, value_police_2014]]
        data_2015[postcode] = [[n_offences_speed_2015, value_speed_2015],[n_offences_police_2015, value_police_2015]]

    return curr_sheet, data_2014, data_2015

def retrieve_postocde_data(file_name):
    book = openpyxl.load_workbook(file_name)
    curr_sheet = book.get_sheet_by_name("Final Data")

    collated_data = {}
    metro_pcode = []
    
    
    for row in range(1,4768):
        postcode = curr_sheet.cell(row = row, column = 1).value
        suburb = curr_sheet.cell(row = row, column = 2).value
        lat = curr_sheet.cell(row = row, column = 4).value
        long = curr_sheet.cell(row = row, column = 5).value
        region = curr_sheet.cell(row = row, column = 6).value

        collated_data[suburb] = [postcode, lat, long, region]

        if region == "Metro" and postcode not in metro_pcode:
            metro_pcode.append(postcode)
        
    return collated_data,metro_pcode;
        

def retrieve_ranked_n(data,n,top = True):
    fine_rank = []
    pcode_map = {}
    top_n = []
    top_n_pcode = []
    bottom_n = []
    bottom_n_pcode = []
    
    for entry in data:
        fine_value = data[entry][0][1] + data[entry][1][1]
        fine_rank.append(fine_value)
        pcode_map[entry] = fine_value
        
    fine_rank = sorted(fine_rank)

    if top:
        for i in range(len(fine_rank)-1, len(fine_rank) - n - 1, -1):
            top_n.append(fine_rank[i])
            for entry in pcode_map:
                if pcode_map[entry] == fine_rank[i]:
                    top_n_pcode.append(entry)
        return top_n, top_n_pcode
    
    else:
        for i in range(n):
            bottom_n.append(fine_rank[i])
            for entry in pcode_map:
                if pcode_map[entry] == fine_rank[i]:
                    bottom_n_pcode.append(entry)
        return bottom_n, bottom_n_pcode
    

def text_results(data_2014, data_2015, n):
    h_fine, h_pcode = retrieve_ranked_n(data_2014,n, top = True)
    print("Top",n,"Postcodes for Speeding Fines 2014")
    for p in range(len(h_pcode)):
        if h_pcode[p] in metro_pcode:
            print(str(p + 1) + '.\t', h_pcode[p], "$" + str(h_fine[p]) + ' - Metro')
        else:
            print(str(p + 1) + '.\t', h_pcode[p], "$" + str(h_fine[p]) + ' - Regional')

    h_fine, h_pcode = retrieve_ranked_n(data_2015,n, top = True)
    print("\nTop",n,"Postcodes for Speeding Fines 2015")
    for p in range(len(h_pcode)):
        if h_pcode[p] in metro_pcode:
            print(str(p + 1) + '.\t', h_pcode[p], "$" + str(h_fine[p]) + ' - Metro')
        else:
            print(str(p + 1) + '.\t', h_pcode[p], "$" + str(h_fine[p]) + ' - Regional')

    h_fine, h_pcode = retrieve_ranked_n(data_2014,n, top = False)
    print("\nBottom",n,"Postcodes for Speeding Fines 2014")
    for p in range(len(h_pcode)):
        if h_pcode[p] in metro_pcode:
            print(str(p + 1) + '.\t', h_pcode[p], "$" + str(h_fine[p]) + ' - Metro')
        else:
            print(str(p + 1) + '.\t', h_pcode[p], "$" + str(h_fine[p]) + ' - Regional')   

    h_fine, h_pcode = retrieve_ranked_n(data_2015,n, top = False)
    print("\nBottom",n,"Postcodes for Speeding Fines 2015")
    for p in range(len(h_pcode)):
        if h_pcode[p] in metro_pcode:
            print(str(p + 1) + '.\t', h_pcode[p], "$" + str(h_fine[p]) + ' - Metro')
        else:
            print(str(p + 1) + '.\t', h_pcode[p], "$" + str(h_fine[p]) + ' - Regional')
    
curr_sheet, data_2014, data_2015 = retrieve_speeding_data("./speeding_stats.xlsx")
collated_data, metro_pcode = retrieve_postocde_data("./Australian_Post_Codes_Lat_Lon.xlsx")

from utils import download_stock_list


def main(params):

    # if not all ready download list of stocks from wiki page for SP500
    if params["download_stock_list"]: download_stock_list(params)


    #get and save data as selenium
    #create stock classes (maybe getting the data is a method in class)

    pass


if __name__ == '__main__':
    params = {"download_stock_list":False}
    main(params)
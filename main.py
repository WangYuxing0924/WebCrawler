from selenium import webdriver
import flightdb
from lxml import etree

def webcrawler(date, fromCity, toCity):
    driver = webdriver.Chrome(executable_path=r"/Users/xiefang/chromedriver")
    driver.get("https://flights.ctrip.com/actualtime/list?departCity="+fromCity+"&arriveCity="+toCity+"&departPort=&arrivePort=&date="+date)
    html_source = driver.page_source
    page = etree.HTML(driver.page_source)
    #print("============="+driver.page_source)
    #print("=========="+html_source)
    print("==============================================================================")
    list=page.xpath('//div[@class="list-item"]')
    print(len(list))
    #driver.quit()
    flight_list = []
    for info in list:
        flight_dict = {}
        print("===========\n")
        #flight_dict['flight_NO'] = info.text
        flightNoList=info.xpath('./div[@class="list-item-part left"]/div[@class="list-item-flight"]/div[@class="info"]/div[@class="flight"]')
        try:
            print("航班号：" +flightNoList[0].text)
            flight_dict['flight_no'] = flightNoList[0].text
        except:
            flight_dict['flight_no'] = ""
        flightTime = info.xpath('./div[@class="list-item-part left"]/div[@class="depart-info"]/div[@class="time"]')
        try:
            flight_dict['depart_time']=flightTime[0].text
            print("起飞时间：" + flightTime[0].text)
        except:
            flight_dict['depart_time'] = ""
        depart_airport=info.xpath('./div[@class="list-item-part left"]/div[@class="depart-info"]/div[@class="airport-info depart"]/div[@class="airport"]')
        try:
            flight_dict['depart_airport']=depart_airport[0].text
            print("起飞机场："+depart_airport[0].text)
        except:
            flight_dict['depart_airport']=""
        depart_terminal = info.xpath('./div[@class="list-item-part left"]/div[@class="depart-info"]/div[@class="airport-info depart"]/div[@class="terminal"]')
        try:
            flight_dict['depart_terminal'] = depart_terminal[0].text
            print("起飞航站楼：" + depart_terminal[0].text)
        except:
            flight_dict['depart_terminal'] = ""
        arriveTime = info.xpath(
            './div[@class="list-item-part right"]/div[@class="arrive-info"]/div[@class="time"]')
        try:
            print("到达时间：" + arriveTime[0].text)
            flight_dict['arrive_time'] = arriveTime[0].text
        except:
            flight_dict['arrive_time'] = ""

        arriveAirPort = info.xpath(
            './div[@class="list-item-part right"]/div[@class="arrive-info"]/div[@class="airport-info"]/div[@class="airport"]')
        try:
            print("到达机场：" + arriveAirPort[0].text)
            flight_dict['arrive_airPort'] = arriveAirPort[0].text
        except:
            flight_dict['arrive_airPort'] = ""
        terminal = info.xpath(
            './div[@class="list-item-part right"]/div[@class="arrive-info"]/div[@class="airport-info"]/div[@class="terminal"]')
        try:
            print("到达航站楼：" + terminal[0].text)
            flight_dict['arrive_terminal'] = terminal[0].text
        except:
            flight_dict['arrive_terminal'] = ""
        statusGreen = info.xpath(
            './div[@class="list-item-part right"]/div[@class="status green"]')
        try:
            print("状态：" + statusGreen[0].text)
            flight_dict['status_green'] = statusGreen[0].text
        except:
            flight_dict['status_green'] = ""
            if flight_dict['status_green']=="":
                print("=====2222=======状态空")
                statusRed = info.xpath(
                './div[@class="list-item-part right"]/div[@class="status red"]')
                try:
                    print("状态：" + statusRed[0].text)
                    flight_dict['status_green'] = statusRed[0].text
                except:
                    flight_dict['status_green'] = ""
                if flight_dict['status_green']=="":
                    statusOrange = info.xpath(
                        './div[@class="list-item-part right"]/div[@class="status orange"]')
                    try:
                        print("状态：" + statusOrange[0].text)
                        flight_dict['status_green'] = statusOrange[0].text
                    except:
                        flight_dict['status_green'] = ""
        flight_list.append(flight_dict)
    return flight_list

#mysqlquery()
#mysqldelete()
if __name__ == '__main__':
    date = '2021-07-22'
    fromCity = "SHA"
    toCity = "BJS"
    flight_list = webcrawler(date, fromCity, toCity)
    print("flight list len:"+str(len(flight_list)))
    tableDate = date.replace("-","")
    tableName="flight"+tableDate
    print("table name:"+tableName)
    flightdb.createTable(tableName)
    flightdb.mysqlInsert(tableName,flight_list)




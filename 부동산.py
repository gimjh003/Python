class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

apartment = House("강남", "아파트", "매매", "10억", "2010년")
officetel = House("마포", "오피스텔", "전세", "5억", "2007년")
villa = House("송파", "빌라", "월세", "500/50", "2000년")

House_list = []

House_list.append(apartment)
House_list.append(officetel)
House_list.append(villa)

print("총 {}대의 매물이 있습니다.".format(len(House_list)))
for zip in House_list:
    zip.show_detail()
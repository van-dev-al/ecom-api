import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from fake_useragent import UserAgent
import threading

ua = UserAgent()
headers = {
    "User-Agent": ua.random
}

@dataclass
class Part():
    '''
    Lớp đại diện cho một phần từ một trang web nhất định
    '''
    title: str
    current_price: str
    discount: str
    rate: str
    link: str
    img_link: str
    site: str

    def get_price(self):
        try:
            return float(''.join(self.current_price[1:].split(",")))
        except:
            return 0

    def __str__(self):
        return(f"Part name: {self.title}\nPrice: {self.price}\nDiscount: {self.discount}\nCurrent price: {self.current_price}\nWebsite: {self.link}\nImage Link: {self.img_link}")


def get_search_url(part_name, site, space_separator):
    search_url = site.replace(
        "item goes here", space_separator.join(part_name.split()))
    return search_url


def get_soup(url):
    response = requests.get(url, headers=headers)
    if(response.status_code == requests.codes.ok):
        soup = BeautifulSoup(response.text, "lxml")
        return soup
    else:
        return


def part_list_threading(site, part_name, space_separator, sites_part_list, file):
    search_url = get_search_url(part_name, site[1], space_separator)
    site_soup = get_soup(search_url)
    if(site_soup != None):
        temp_part_list = file.scrape_site(site[0], part_name, site_soup)
        part_list = []
        for part in temp_part_list:
            part_list.append(Part(part[0], part[1], part[2], part[3], part[4]))
    else:
        part_list = []
    sites_part_list.extend(part_list)
    return


def sort_according_to_price(part_list):
    '''
    Chức năng sắp xếp Danh sách linh kiện theo Giá
    Nó trả về một danh sách các Đối tượng Phần được sắp xếp tăng dần theo giá của chúng
    Phải mất một đối số của danh sách Đối tượng Phần chưa được sắp xếp
    '''
    price_sort = []
    for item in part_list:
        price_sort.append((item.get_price()))
    price_sort.sort()
    new_part_list = []
    for price in price_sort:
        for item in part_list:
            if(item.get_price() == price):
                new_part_list.append(part_list.pop(part_list.index(item)))
    return new_part_list


def get_part_list(part_name, part_cat):
    if(part_cat == "Laptops"):
        import categories.laptops
        file = categories.laptops
    elif(part_cat == "Mobiles"):
        import categories.mobiles
        file = categories.mobiles
    elif(part_cat == "Tablets"):
        import categories.tablets
        file = categories.tablets
    # Một danh sách để lưu trữ Tất cả danh sách các Đối tượng Phần
    sites_part_list = []
    # Tạo danh sách lưu trữ chủ đề cho mỗi trang
    threads = []
    for space_separator, url in file.parts_sites.items():
        for a_site in url:
            thread_obj = threading.Thread(target=part_list_threading, args=[
                                          a_site, part_name, space_separator, sites_part_list, file])
            threads.append(thread_obj)
            thread_obj.start()
    for thread in threads:
        #Đang chờ tất cả các chủ đề hoàn thành
        thread.join()
    sites_part_list = sort_according_to_price(sites_part_list)
    return sites_part_list

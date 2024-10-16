parts_sites = {
    "%20": [("www.shopee.vn", "https://shopee.vn/mall/search?keyword=item goes here"), ("www.cellphones.com.vn", "https://cellphones.com.vn/catalogsearch/result?q=item goes here"), ("www.tiki.vn", "https://tiki.vn/search?q=item goes here"), ("www.lazada.vn", "https://www.lazada.vn/tag/samsung-s23/?q=item goes here" ), ("www.didongviet.vn", "https://didongviet.vn/search?q=item goes here")],
    "+": [("www.thegioididong.com", "https://www.thegioididong.com/tim-kiem?key=item goes here")]
}


def scrape_site(site, part_name, soup):
    '''
    Chức năng gọi Parts Scraper cho Site tương ứng
    Nó trả về danh sách các đối tượng Phần tương ứng với tên bộ phận đã cho trong một trang tương ứng
    Nó lấy đối số tên trang web, tên bộ phận, đối tượng BeautifulSoup của trang web
    '''
    if(site == "www.shopee.vn"):
        site_function = shopee
    elif(site == "www.cellphones.com.vn"):
        site_function = cellphones
    elif(site == "www.tiki.vn"):
        site_function = tiki
    elif(site == "www.lazada.vn"):
        site_function = lazada
    elif(site == "www.didongviet.vn"):
        site_function = ddviet
    elif(site == "www.thegioididong.com"):
        site_function = tgdd
    part_list = site_function(soup, part_name, site)
    return part_list

def shopee(soup, part_name, site):
    '''
    Chức năng cạo Part từ shopee.vn
    Nó trả về một danh sách các bộ dữ liệu theo thứ tự tiêu đề, giá cả, liên kết, img_link, tên trang web
    Nó lấy đối tượng Arguments BeautifulSoup của shopee.vn tìm kiếm phần, tên phần
    '''
    items = soup.findAll("div", {"class": "h-full duration-100 ease-sharp-motion-curve hover:shadow-hover active:shadow-active hover:-translate-y-[1px] active:translate-y-0 relative hover:z-[1] box-content relative border border-solid border-shopee-black9"})
    part_list = []

    for i in items:
        try:
            link = i.a['href']
            img_link = i.find("div", {"class": "relative z-0 w-full pt-full"}).img["src"]
            title = i.find("div", {"class": "whitespace-normal line-clamp-2 break-words min-h-[2.5rem] text-sm"}).text.strip()
            current_price = i.find("div", {"class": "truncate flex items-baseline"}).find("span", {"class": "font-medium text-base/5 truncate"}).text
            discount = i.find("div", {"class": "text-shopee-primary font-medium bg-shopee-pink py-0.5 px-1 text-sp10/3 h-4 rounded-[2px] shrink-0 mr-1"}).find("span").text
            rate = i.find("div", {"class":"flex-none flex items-center space-x-0.5 h-sp14"}).find("div", {"class" : "text-shopee-black87 text-xs/sp14 flex-none"}).text.strip()

            current_price_numeric = float(current_price.replace('.', '').strip())
            discount_numeric = float(discount.replace('-', '').replace('%', '').strip())

            flag = 0
            for word in part_name.split(" "):
                if (word not in title.lower().split()):
                    flag = 1
                    break
            if (flag == 0):
                part_list.append((title, current_price_numeric, discount_numeric, rate, link, img_link, site))

        except:
            continue

    return part_list

def cellphones(soup, part_name, site):
    '''
    Function to scrape Part from mdcomputers.in
    It returns a list of tuples in the order of title, price, link, img_link, websitename
    It takes Arguments BeautifulSoup object of mdcomputers.in part search, part name
    '''
    items = soup.findAll("div", {"class": "product-info-container product-item"})
    part_list = []

    for i in items:
        try:
            link = i.find("div", {"class": "product-info"}).a["href"]
            img_link = i.find("div", {"class": "product__image"}).img["src"]
            title = i.find("div", {"class": "product__name"}).h3.text
            current_price = i.find("div", {"class": "box-info__box-price"}).find("p", {"class": "product__price--show"}).text
            discount = i.find("div", {"class": "product__price--percent"}).find("p", {"class": "product__price--percent-detail"})
            if discount:
                discount = discount.text.replace('Giảm&nsb;', '').replace('%', '').strip()
            else:
                discount = "0"

            current_price_numeric = current_price.replace('đ', '').replace('.', '').strip()
            discount_numeric = float(discount)

            rate = 0
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append((title, current_price_numeric, discount_numeric, rate, link, img_link, site))
        except:
            continue
    return part_list

def tiki(soup, part_name, site):
    '''
    Function to scrape Part from amazon.in
    It returns a list of Part objects satisfying the part name
    It takes Arguments BeautifulSoup object of amazon.in part search, part name
    '''
    results = soup.findAll("div", {"class": "a-section a-spacing-medium"})
    part_list = []
    for item in results:
        try:
            title = item.find(
                "span", {"class": "a-size-medium a-color-base a-text-normal"}).get_text().strip()
            price = item.find(
                "span", {"class": "a-offscreen"}).get_text().strip()
            link = "https://amazon.in" + \
                item.find(
                    "a", {"class": "a-link-normal a-text-normal"})['href'].strip()
            img_link = item.find(
                "div", {"class": "a-section aok-relative s-image-fixed-height"}).img["src"]
            flag = 0
            for word in part_name.split(" "):
                if(word not in title.lower().split()):
                    flag = 1
                    break
            if(flag == 0):
                part_list.append((title, price, link, img_link, site))
        except:
            continue
    return part_list



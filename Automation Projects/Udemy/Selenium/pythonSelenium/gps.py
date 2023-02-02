from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

class WebDriver:

	location_data = {}

	def __init__(self):
		self.PATH = "chromedriver.exe"
		self.options = Options()
		# self.options.binary_location = "
		self.options.add_argument("--headless")
		self.driver = webdriver.Chrome(self.PATH, options=self.options)

		self.location_data["rating"] = "NA"
		self.location_data["reviews_count"] = "NA"
		self.location_data["location"] = "NA"
		self.location_data["contact"] = "NA"
		self.location_data["website"] = "NA"
		self.location_data["Time"] = {"Monday":"NA", "Tuesday":"NA", "Wednesday":"NA", "Thursday":"NA", "Friday":"NA", "Saturday":"NA", "Sunday":"NA"}
		self.location_data["Reviews"] = []
		self.location_data["Popular Times"] = {"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[], "Saturday":[], "Sunday":[]}

	def click_open_close_time(self):

		if(len(list(self.driver.find_elements_by_class_name("cX2WmPgCkHi__section-info-hour-text")))!=0):
			element = self.driver.find_element_by_class_name("cX2WmPgCkHi__section-info-hour-text")
			self.driver.implicitly_wait(5)
			ActionChains(self.driver).move_to_element(element).click(element).perform()

	def click_all_reviews_button(self):

		try:
			WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "allxGeDnJMl__button")))

			element = self.driver.find_element_by_class_name("allxGeDnJMl__button")
			element.click()
		except:
			self.driver.quit()
			return False

		return True

	def get_location_data(self):

		try:
			avg_rating = self.driver.find_element_by_class_name("section-star-display")
			total_reviews = self.driver.find_element_by_class_name("section-rating-term")
			address = self.driver.find_element_by_css_selector("[data-item-id='address']")
			phone_number = self.driver.find_element_by_css_selector("[data-tooltip='Copy phone number']")
			website = self.driver.find_element_by_css_selector("[data-item-id='authority']")
		except:
			pass
		try:
			self.location_data["rating"] = avg_rating.text
			self.location_data["reviews_count"] = total_reviews.text[1:-1]
			self.location_data["location"] = address.text
			self.location_data["contact"] = phone_number.text
			self.location_data["website"] = website.text
		except:
			pass


	def get_location_open_close_time(self):

		try:
			days = self.driver.find_elements_by_class_name("lo7U087hsMA__row-header")
			times = self.driver.find_elements_by_class_name("lo7U087hsMA__row-interval")

			day = [a.text for a in days]
			open_close_time = [a.text for a in times]

			for i, j in zip(day, open_close_time):
				self.location_data["Time"][i] = j
		
		except:
			pass

	def get_popular_times(self):
		try:
			a = self.driver.find_elements_by_class_name("section-popular-times-graph")
			dic = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
			l = {"Sunday":[], "Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[], "Saturday":[]}
			count = 0

			for i in a:
				b = i.find_elements_by_class_name("section-popular-times-bar")
				for j in b:
					x = j.get_attribute("aria-label")
					l[dic[count]].append(x)
				count = count + 1

			for i, j in l.items():
				self.location_data["Popular Times"][i] = j
		except:
			pass

	def scroll_the_page(self):
		try:
			WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "section-layout-root")))

			pause_time = 2
			max_count = 5
			x = 0

			while(x<max_count):
				scrollable_div = self.driver.find_element_by_css_selector('div.section-layout.section-scrollbox.scrollable-y.scrollable-show')
				try:
					self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
				except:
					pass
				time.sleep(pause_time)
				x=x+1
		except:
			self.driver.quit()

	def expand_all_reviews(self):
		try:
			element = self.driver.find_elements_by_class_name("section-expand-review")
			for i in element:
				i.click()
		except:
			pass

	def get_reviews_data(self):
		try:
			review_names = self.driver.find_elements_by_class_name("section-review-title")
			review_text = self.driver.find_elements_by_class_name("section-review-review-content")
			review_dates = self.driver.find_elements_by_css_selector("[class='section-review-publish-date']")
			review_stars = self.driver.find_elements_by_css_selector("[class='section-review-stars']")

			review_stars_final = []

			for i in review_stars:
				review_stars_final.append(i.get_attribute("aria-label"))

			review_names_list = [a.text for a in review_names]
			review_text_list = [a.text for a in review_text]
			review_dates_list = [a.text for a in review_dates]
			review_stars_list = [a for a in review_stars_final]

			for (a,b,c,d) in zip(review_names_list, review_text_list, review_dates_list, review_stars_list):
				self.location_data["Reviews"].append({"name":a, "review":b, "date":c, "rating":d})

		except Exception as e:
			pass

	def scrape(self, url):
		try:
			self.driver.get(url)
		except Exception as e:
			self.driver.quit()
			continue
		time.sleep(10)

		self.click_open_close_time()
		self.get_location_data()
		self.get_location_open_close_time()
		self.get_popular_times()
		if(self.click_all_reviews_button()==False):
			continue
		time.sleep(5)
		self.scroll_the_page()
		self.expand_all_reviews()
		self.get_reviews_data()
		self.driver.quit()

		return(self.location_data)

url = "your_location_url"
x = WebDriver()
print(x.scrape(url))
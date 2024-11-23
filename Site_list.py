import requests
from bs4 import BeautifulSoup

class SiteManager:
    def __init__(self):
        self.sites = []

    def add_site(self, url):
        self.sites.append(url)

    def get_sites(self):
        return self.sites

    def site_count(self):
        return len(self.sites)

class SiteParser:
    def __init__(self):
        self.timeout = 10

    def fetch_page(self, url):
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении страницы {url}: {e}")
            return None

    def search_on_page(self, page_content, query):
        soup = BeautifulSoup(page_content, 'html.parser')
        text = soup.get_text().lower()
        query = query.lower()
        return text.count(query)

class UserInterface:
    def __init__(self, app):
        self.app = app

    def display_menu(self):
        print("\n1. Добавить сайт")
        print("2. Поиск по запросу")
        print("3. Показать все сайты")
        print("4. Выход")

    def get_user_choice(self):
        while True:
            try:
                choice = int(input("Введите номер команды: "))
                if choice in [1, 2, 3, 4]:
                    return choice
                else:
                    print("Неверный выбор, попробуйте снова.")
            except ValueError:
                print("Неверный выбор, введите число.")

    def get_site_url(self):
        return input("Введите URL сайта: ").strip()

    def get_search_query(self):
        return input("Введите запрос для поиска: ").strip()

    def add_site(self):
        url = self.get_site_url()
        self.app.add_site(url)
        print(f"Сайт {url} добавлен.")

    def search_sites(self):
        query = self.get_search_query()
        results = self.app.search(query)
        if results:
            print("\nРезультаты поиска:")
            index = 1
            for site, count in results:
                print(f"{index}. {site}: найдено {count} совпадений")
                index += 1
        else:
            print("Нет результатов.")

    def show_all_sites(self):
        sites = self.app.site_manager.get_sites()
        if sites:
            print("\nВсе добавленные сайты:")
            index = 1
            for site in sites:
                print(f"{index}. {site}")
                index += 1
        else:
            print("Список сайтов пуст.")

class SearchApp:
    def __init__(self):
        self.site_manager = SiteManager()
        self.site_parser = SiteParser()
        self.ui = UserInterface(self)

    def add_site(self, url):
        self.site_manager.add_site(url)

    def search(self, query):
        sites = self.site_manager.get_sites()
        results = []

        for site in sites:
            content = self.site_parser.fetch_page(site)
            if content:
                matches = self.site_parser.search_on_page(content, query)
                if matches > 0:
                    results.append((site, matches))

        results = self._sort_results_by_matches(results)
        return results

    def _sort_results_by_matches(self, results):
        max_count = max([count for _, count in results], default=0)
        sorted_results = []
        for count in range(max_count, -1, -1):
            for site, site_count in results:
                if site_count == count:
                    sorted_results.append((site, site_count))
        return sorted_results

    def run(self):
        while True:
            self.ui.display_menu()
            choice = self.ui.get_user_choice()

            if choice == 1:
                self.ui.add_site()
            elif choice == 2:
                self.ui.search_sites()
            elif choice == 3:
                self.ui.show_all_sites()
            elif choice == 4:
                print("Выход из программы.")
                break

if __name__ == "__main__":
    app = SearchApp()
    app.run()
import pandas as pd
import requests

url_intervals = []
for i in range(1, 23):
    url_intervals.append(f"https://api.hh.ru/vacancies?specialization=1&query=DevOps&date_from=2022-12-20T{str(i).zfill(2)}:00:00&date_to=2022-12-20T{str(i + 1).zfill(2)}:00:00")

df = pd.DataFrame(columns=["name", "description", "key_skills", "department", "salary_from", "salary_to", "area.name", "published_at"])

for url in url_intervals:
    json_for_pages = requests.get(url).json()
    for p in range(json_for_pages["pages"] + 1):
        if json_for_pages["per_page"] < 100:
            params = {'page': p}
        else:
            params = {'per_page': '100', 'page': p}
        items = requests.get(url, params=params).json()["items"]
        for item in items:
            try:
                df.loc[len(df)] = [item["name"], item["snippet"]["responsibility"], item["snippet"]["requirement"],
                                   item["department"], item["salary"]["from"], item["salary"]["to"], item["area"]["name"], item["published_at"]]
            except TypeError:
                continue

df.to_csv("new_vacancies.csv", index=False)

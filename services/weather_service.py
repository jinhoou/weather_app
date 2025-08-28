import csv
from typing import List, Optional
from models.weather import WeatherStation

class WeatherService:
    def __init__(self, tsv_file_path: str = "export.tsv"):
        self.tsv_file_path = tsv_file_path
        self._data: List[WeatherStation] = []
        self.load_data()
    
    def load_data(self) -> None:
        """TSVファイルからデータを読み込む"""
        try:
            with open(self.tsv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file, delimiter='\t')
                self._data = []
                for row in reader:
                    station = WeatherStation(
                        station_id=row['観測所番号'],
                        prefecture=row['都道府県'],
                        location=row['地点'],
                        current_value=float(row['現在値(mm)']) if row['現在値(mm)'] else 0.0
                    )
                    self._data.append(station)
        except Exception as e:
            print(f"Error loading data: {e}")
            self._data = []
    
    def get_all_stations(self) -> List[WeatherStation]:
        """全観測所データを取得"""
        return self._data
    
    def get_stations_by_prefecture(self, prefecture: str) -> List[WeatherStation]:
        """都道府県別観測所データを取得"""
        return [station for station in self._data if station.prefecture == prefecture]
    
    def get_unique_prefectures(self) -> List[str]:
        """都道府県一覧を取得"""
        prefectures = list(set(station.prefecture for station in self._data))
        return sorted(prefectures)
    
    def search_stations(self, prefecture: Optional[str] = None, location_keyword: Optional[str] = None) -> List[WeatherStation]:
        """検索機能"""
        filtered_data = self._data
        
        if prefecture:
            filtered_data = [station for station in filtered_data if station.prefecture == prefecture]
        
        if location_keyword:
            filtered_data = [station for station in filtered_data 
                           if location_keyword.lower() in station.location.lower()]
        
        return filtered_data
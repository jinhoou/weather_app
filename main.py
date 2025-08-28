from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional, List
from services.weather_service import WeatherService
from models.weather import WeatherStation

app = FastAPI(title="Weather Information Site")

# 静的ファイルとテンプレートの設定
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# WeatherServiceのインスタンス
weather_service = WeatherService()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, prefecture: Optional[str] = Query(None)):
    """メインページ - 観測所データを表形式で表示"""
    prefectures = weather_service.get_unique_prefectures()
    
    if prefecture:
        stations = weather_service.get_stations_by_prefecture(prefecture)
    else:
        stations = weather_service.get_all_stations()
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "stations": stations,
        "prefectures": prefectures,
        "selected_prefecture": prefecture
    })

@app.get("/api/stations")
async def get_stations(prefecture: Optional[str] = Query(None)) -> List[WeatherStation]:
    """観測所データAPI"""
    if prefecture:
        return weather_service.get_stations_by_prefecture(prefecture)
    else:
        return weather_service.get_all_stations()

@app.get("/api/prefectures")
async def get_prefectures() -> List[str]:
    """都道府県一覧API"""
    return weather_service.get_unique_prefectures()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
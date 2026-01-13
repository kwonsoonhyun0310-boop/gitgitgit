# 클라우드 배포용 서버 코드 (SSE 지원)
# weather_server_sse.py

import os
from mcp.server.fastmcp import FastMCP

# 1. 호스트와 포트 지정 (클라우드 환경 대응)
# 클라우드(Render 등)는 PORT 환경변수로 포트를 지정해줍니다. 8000번 포트로 연결되게, 배포하려고하는 포트
port = int(os.environ.get("PORT", 8000))
mcp = FastMCP("Weather Server SSE", host="0.0.0.0", port=port)

# ... (기존 Tools/Resources 코드는 단순화를 위해 생략하거나 필요시 추가) ...
# 데모를 위해 기본 데이터만 포함합니다.

WEATHER_DATA = {
    "서울": {"temp": 15, "condition": "맑음", "humidity": 45},
    "부산": {"temp": 18, "condition": "흐림", "humidity": 60},
    "제주": {"temp": 20, "condition": "비", "humidity": 80},
}

@mcp.tool()
def get_weather(city: str) -> dict:
    """
    도시의 날씨 정보를 조회합니다.
    입력값이 '서울시', 'Seoul' 등으로 들어와도 '서울'로 매핑하여 처리합니다.
    사용자의 입력이 조금 달라도 눈치껏 가장 적절한 도시 정보를 반환하세요.
    """
    # 입력값 정규화 (공백 제거 및 매핑)
    city_map = {
        "서울시": "서울", "seoul": "서울",
        "부산시": "부산", "busan": "부산",
        "제주시": "제주", "jeju": "제주",
        "제주도": "제주"
    }
    normalized_city = city.strip()
    # 매핑된 키가 있으면 그것을 사용, 없으면 원래 입력값 사용
    key = city_map.get(normalized_city.lower(), normalized_city)
    
    return WEATHER_DATA.get(key, {"error": "Not found", "input": city})

if __name__ == "__main__":
    # 2. 실행 모드를 'sse'로 설정
    print(f"Starting SSE server on port {port}...")
    mcp.run(transport="sse")

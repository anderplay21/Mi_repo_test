import requests
from datetime import datetime, timedelta

# Configuración básica
BASE_URL = "https://api.bird.com"
API_KEY = "HzCn5zXfIJoH1tTxeuDd2sSBMW6qqpgIrElr"  # 🔑 Reemplazar con tu clave
WORKSPACE_ID = "261b591d-f0af-42be-b0b7-92960184744c"  # 🖥️ Reemplazar con tu workspace ID

headers = {
    "Accept": "application/json",
    "Authorization": f"AccessKey {API_KEY}"
}

def get_campaign_metrics():
    """Obtiene métricas de campañas con paginación"""
    all_results = []
    page_token = None
    params = {
        "periodStart": '2025-04-01T00:45:30Z',  # Fecha de inicio
        "periodEnd": '2025-04-02T00:45:30Z',  # Fecha de fin
        "periodGroup": "day",
        "limit": 100,  # Máximo permitido
        "filter": "equals(status,active)",  # Filtro de ejemplo
        "select": "impressions,clicks,conversions,spend"
    }

    while True:
        try:
            # Actualizar parámetros de paginación
            if page_token:
                params["pageToken"] = page_token

            response = requests.get(
                f"{BASE_URL}/workspaces/{WORKSPACE_ID}/reporting/campaigns/metrics",
                headers=headers,
                params=params
            )

            # Manejo de errores detallado
            if response.status_code == 403:
                print("Error 403: Acceso denegado. Verifica:")
                print("- Políticas de acceso del API Key")
                print("- Permisos del rol asociado")
                print("- Recursos en la política (deben incluir /reporting/campaigns/**)")
                return

            response.raise_for_status()
            
            data = response.json()
            all_results.extend(data.get("results", []))
            
            # Verificar paginación
            page_token = data.get("nextPageToken")
            if not page_token:
                break

        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP {e.response.status_code}: {e.response.text}")
            return
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            return

    return all_results

def main():
    metrics = get_campaign_metrics()
    
    if metrics:
        print(f"\n📈 Métricas de Campañas ({len(metrics)} registros):")
        for idx, campaign in enumerate(metrics, 1):
            print(f"\n🔹 Campaña #{idx}")
            print(f"ID: {campaign.get('id')}")
            print(f"Nombre: {campaign.get('name')}")
            print(f"Fecha: {campaign.get('periodDate')}")
            print("📊 Métricas:")
            print(f"  - Impresiones: {campaign.get('impressions', 0)}")
            print(f"  - Clics: {campaign.get('clicks', 0)}")
            print(f"  - Conversiones: {campaign.get('conversions', 0)}")
            print(f"  - Inversión: ${campaign.get('spend', 0):.2f}")
    else:
        print("No se encontraron métricas")

if __name__ == "__main__":
    main()
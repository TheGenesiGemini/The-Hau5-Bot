from dataclasses import dataclass
from typing import Union


@dataclass
class BaseConfig:
    CHATS = [
        -1001515379979,  # Binance Crypto Box Code
        -1001813092752,  # Binance Red packet crypto box
        -1001610472708,  # 🐋 Chat Whale Box 🎁
    ]

    CLIENT_NAME: str = "MajaderaBot"  # Client name | Can be left as now or changed
    API_ID: int = 25388732  # Telegram API ID
    API_HASH: str = "f9a7ab46494a09f801e3bde68b93f5c1"  # Telegram API hash

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "bnc-uuid": "bf443f1e-b070-4c44-952b-9873c1d7c7ab",
        "device-info": "eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA4MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA4MCIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoiZXMtNDE5IiwidGltZXpvbmUiOiJHTVQtMDY6MDAiLCJ0aW1lem9uZU9mZnNldCI6MzYwLCJ1c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwibGlzdF9wbHVnaW4iOiJQREYgVmlld2VyLENocm9tZSBQREYgVmlld2VyLENocm9taXVtIFBERiBWaWV3ZXIsTWljcm9zb2Z0IEVkZ2UgUERGIFZpZXdlcixXZWJLaXQgYnVpbHQtaW4gUERGIiwiY2FudmFzX2NvZGUiOiI1NTVmYzQ5YSIsIndlYmdsX3ZlbmRvciI6Ikdvb2dsZSBJbmMuIChOVklESUEpIiwid2ViZ2xfcmVuZGVyZXIiOiJBTkdMRSAoTlZJRElBLCBOVklESUEgR2VGb3JjZSBHVFggMTY1MCAoMHgwMDAwMUY5RCkgRGlyZWN0M0QxMSB2c181XzAgcHNfNV8wLCBEM0QxMSkiLCJhdWRpbyI6IjEyNC4wNDM0NzUyNzUxNjA3NCIsInBsYXRmb3JtIjoiV2luMzIiLCJ3ZWJfdGltZXpvbmUiOiJBbWVyaWNhL01leGljb19DaXR5IiwiZGV2aWNlX25hbWUiOiJDaHJvbWUgVjEzNi4wLjAuMCAoV2luZG93cykiLCJmaW5nZXJwcmludCI6IjgyMTJhNWQwMTdmNWE5YjlmY2UxY2ZlMDkyMTJhMzQ0IiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiIn0=",
        "clienttype": "web",
        "csrftoken": "9370bdf980ae2ba5ab09030a67e15758",
        "fvideo-id": "338e4fde1a3aa6e79e8239a0265d006a551a10b1",
        "fvideo-token": "HCayuTSzPM2GkIlZduVWpwpxdALd/u4XcZsh+ZxsAeTValoQ1vVps9jH9shkOhlyEdnyKHZK/BJyDmjw/M6iOI3mgOUmopjmNGWDRVzuQNvTBm+kRRYnwomukOqTM/h0h4KnUiWuQzx5VqfOHPpj/FjyK8oET8FSeDyMpxgeNY70xGNoIxc3LKAi1KRbZFdSE=01",
        "x-trace-id": "97fd3b0a-e350-4cb7-801f-9af8bcc95fab",
        "x-ui-request-trace": "97fd3b0a-e350-4cb7-801f-9af8bcc95fab",
        "lang": "es-419",
        "Referer": "https://www.binance.com/es/my/wallet/account/payment/cryptobox",
        "Cookie": "aws-waf-token=b4407e00-54de-49a0-9713-7e2f6cf35b3f:EQoAtmIkALcgAAAA:6QhgRb6+jogsLL/Pgcr1XVxND1m2GSJbQFLciZwsx65eyg5vTBwKH9ckacfW4KKViQJbawsxFWQI+Lb54GKroEGHaGsP54qFPFaGrTuIsSWEmy3RcSUMBu+0BKZ8aAvQl6U/+zcOk3nMclBtFpaINEzk3lJH4zEltHi3WF3xXaEsifBrYFf1jmGIkPLQgSRpUCU=; bnc-uuid=bf443f1e-b070-4c44-952b-9873c1d7c7ab; _gid=GA1.2.836030656.1747804368; OptanonAlertBoxClosed=2025-05-21T05:12:49.438Z; lang=es-419; language=es-419; se_gd=VEaFVXBhTGVDlAEAHFQ9gZZARHFcUBWW1McNbVUdlZcUwFFNWV0D1; se_gsd=cyolATNyIzQlIwo3JDI7NCYEBBwbDwELV1RDU1BRV1ZaNFNT1; BNC_FV_KEY=338e4fde1a3aa6e79e8239a0265d006a551a10b1; r30t=1; currentAccount=; logined=y; isAccountsLoggedIn=y; BNC-Location=MX; _gcl_au=1.1.221391765.1747883177; theme=dark; neo-theme=dark; r20t=web.ED0AB012CCF0F3E693EA84D2EB2A776D; cr00=F7F40EFE25877E2AFAFF53858DF3080D; d1og=web.1096314291.A0E734079A67A4C00A2FB079D3A7D404; r2o1=web.1096314291.EA28D5E55E95E6926AF80CCF89AFD354; f30l=web.1096314291.2BD754664E96A32307DFBB63DB3EC6BC; p20t=web.1096314291.6315D633030581603642985615779877; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221096314291%22%2C%22first_id%22%3A%22196f1422c5c1398-0d5a87d4bc81828-26011f51-2073600-196f1422c5d26c3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22Dashboard%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk2ZjE0MjJjNWMxMzk4LTBkNWE4N2Q0YmM4MTgyOC0yNjAxMWY1MS0yMDczNjAwLTE5NmYxNDIyYzVkMjZjMyIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjEwOTYzMTQyOTEifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221096314291%22%7D%2C%22%24device_id%22%3A%22196f1424c151958-04de6db449e2a48-26011f51-2073600-196f1424c161f2f%22%7D; userPreferredCurrency=USD_USD; changeBasisTimeZone=; BNC_FV_KEY_T=101-Vke%2FloazGl40woLhndcuJ0xk22Hx15nXbKA4ivCa7WicoBhjZShpaQkPwKbILuJ1rqP7sBr40hPIJ45mfhUYlA%3D%3D-r3Aoa0r1plGYU9ZjddTtOQ%3D%3D-e5; BNC_FV_KEY_EXPIRE=1747945671872; _uetsid=bab64de036b911f086539348dda43995; _uetvid=bab665a036b911f0a02b6bba8a97ea2d; se_sd=1YBFgRVwLDIGBYMkVBwkgZZCAHA8UESVlRQdaUEBlZdVwBFNWVEI1; OptanonConsent=isGpcEnabled=0&datestamp=Thu+May+22+2025+13%3A00%3A48+GMT-0600+(hora+est%C3%A1ndar+central)&version=202411.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=55f692d9-70f9-4b75-9d94-43f84d5b33ff&interactionCount=2&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&intType=1&geolocation=MX%3BCHH&AwaitingReconsent=false; _ga=GA1.1.1286579042.1747804368; _ga_3WP50LGEEC=GS2.1.s1747937182$o9$g1$t1747940452$j55$l0$h0$dkfRUv30DSahORqIB7YiPBTwtxkvqFJUryw"
    }

    def __getelement__(self, element: str) -> Union[int, float, bool, str]:
        return getattr(self, element, None)


config = BaseConfig()

# TTV

Resource friendly, distraction free feed for Twitch and YouTube livestreams
built with [SafeTwitch](https://codeberg.org/safetwitch) and [Piped](https://github.com/teampiped).

**Config**

```yaml
# ~/.config/ttv/config.yml

twitch:
  - kapitanbombatv

youtube:
  - "@kapitanbomba"

piped:
  - https://pipedapi.kavin.rocks

safetwitch:
  - https://stbackend.drgns.space

timeout: 5
separator: ;
chat-badge-color-mod: 104;157;106
chat-badge-color-vip: 177;98;134
chat-badge-color-sub: 69;133;136
```

**Dependencies**

- python
- python-requests
- python-websockets
- python-yaml

# weather

[Weather Icon](https://github.com/erikflowers/weather-icons) with current temperature from [Open-Meteo](https://open-meteo.com/)

![demo](demo/weather.webm)

#### Dependencies

- python
- python-requests
- nerd-fonts

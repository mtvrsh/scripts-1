# ttv

Twitch and YouTube livestream feed built with
[SafeTwitch](https://codeberg.org/safetwitch) and [Piped](https://github.com/teampiped)

#### Config

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
youtube_chat_cmd: firefox --new-window '%url' &
```

#### Dependencies

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

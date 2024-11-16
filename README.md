# ttv

Twitch and YouTube livestream feed built with
[SafeTwitch](https://codeberg.org/safetwitch) and [Piped](https://github.com/teampiped)

![demo](demo/ttv.webm)

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
```

#### Launcher

```sh
ttvmenu() {
  ttv | sort | column -ts";" | fzf -m | grep -oE "https://[^[:space:]]+" | \

  while read -r url; do
    foot -a hidden -- streamlink --player mpv "$url" best &
  done
}
```

#### Dependencies

- python
- python-requests
- python-websockets
- python-yaml

# weather

[Weather Icon](https://github.com/erikflowers/weather-icons)
with current temperature from [Open-Meteo](https://open-meteo.com/)

![demo](demo/weather.webm)

#### Dependencies

- python
- python-requests
- nerd-fonts

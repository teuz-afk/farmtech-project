library(httr)
library(jsonlite)

cat("===== DADOS CLIMATICOS =====\n")

url <- "https://api.open-meteo.com/v1/forecast?latitude=-22.82&longitude=-47.27&current_weather=true"

resposta <- GET(url)

dados <- fromJSON(content(resposta, "text"))

clima <- dados$current_weather

cat("Temperatura:", clima$temperature, "°C\n")
cat("Velocidade do vento:", clima$windspeed, "km/h\n")
cat("Direcao do vento:", clima$winddirection, "\n")
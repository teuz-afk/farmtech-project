cat("==== ANALISE ESTATISTICA FARMTECH ====\n")

dados <- read.csv("dados_lavoura.csv")

print(dados)

media_area <- mean(dados$Area)
desvio_area <- sd(dados$Area)

media_insumo <- mean(dados$Quantidade_L)
desvio_insumo <- sd(dados$Quantidade_L)

cat("\n--- RESULTADOS ---\n")

cat("Media das areas:", media_area, "\n")
cat("Desvio padrao das areas:", desvio_area, "\n")

cat("Media de insumos:", media_insumo, "\n")
cat("Desvio padrao de insumos:", desvio_insumo, "\n")
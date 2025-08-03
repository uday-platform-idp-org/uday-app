# API de Cadastro de Empresas
Esta API permite registrar e listar empresas utilizando Flask e PostgreSQL via Docker.

---

## Registrar uma empresa via `curl` (POST)

Execute o seguinte comando no terminal:

```bash
curl -X POST http://uday-app.local/api/empresas \
  -H "Content-Type: application/json" \
  -d '{"cnpj": "12.345.678/0001-99", "nome": "Empresa Teste"}'
```

📌 Explicação:
	•	-X POST → envia uma requisição POST
	•	http://uday-app.local/api/empresas → endpoint da API
	•	-H "Content-Type: application/json" → informa que o corpo será JSON
	•	-d '{...}' → os dados da empresa no corpo da requisição


Exemplo de resposta esperada (JSON):
```bash
{
  "id": 1,
  "cnpj": "12.345.678/0001-99",
  "nome": "Empresa Teste"
}
```

📄 Listar todas as empresas (GET)

```bash
curl http://uday-app.local/api/empresas
```

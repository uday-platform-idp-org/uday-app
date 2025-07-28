# API de Cadastro de Empresas

Esta API permite registrar e listar empresas utilizando Flask e PostgreSQL via Docker.

---

## Registrar uma empresa via `curl` (POST)

Execute o seguinte comando no terminal:

```bash
curl -X POST http://localhost:5001/api/empresas \
  -H "Content-Type: application/json" \
  -d '{"cnpj": "12.345.678/0001-99", "nome": "Empresa Teste"}'
```



📌 Explicação:
	•	-X POST → envia uma requisição POST
	•	http://localhost:5001/api/empresas → endpoint da API
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



🔁 Observação sobre ambiente Docker
	•	Se estiver testando a API fora do Docker, use http://localhost:5001.
	•	Se estiver testando de dentro de outro container, use o nome do serviço no Docker Compose:

```bash
curl -X POST http://uday-app:5000/api/empresas \
  -H "Content-Type: application/json" \
  -d '{"cnpj": "12.345.678/0001-99", "nome": "Empresa Teste"}'
```


📄 Listar todas as empresas (GET)

```bash
curl http://localhost:5001/api/empresas
```

Para que seja possivel você testar sua aplicação rode o comando abaixo e teste acessar
```bash
kubectl -n uday-app port-forward service/uday-service 5000:5000
```

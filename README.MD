API criada para um processo seletivo para o cargo de dev python junior na strategi.

#  Desafio
Precisamos criar uma ferramenta para o nosso diretor selecionar os novos membros dos vingadores e criar pequenas equipes.

# Requisitos
* A ferramenta precisa mostrar uma listagem de heróis, mostrando: nome, descricao e fotos.

* O diretor gostaria de ao selecionar o herói poder salvar em uma tabela de possíveis candidatos.

* A partir dos possíveis candidatos, montar as equipes diferenciando entre: VINGADORES e EQUIPE.

# Rodar api localmente
* Entre na pasta do projeto pelo terminal do linux ou pelo CLI mais adequado para seu SO

* Crie um arquivo .env com a url de um banco postgresql

* Execute "python -m venv venv"

* Entre no ambiente virtual do projeto

* Execute "pip install -r requirements.txt"

* Execute "flask db upgrade"

* Execute "flask run"

# Rotas
## Hero
### GET all hero STATUS 200
http://localhost:5000/hero

#### Exemplo de retorno
```
{
    "heros": [
		{
			"id": 1011334,
			"name": "3-D Man",
			"description": "",
			"image": "http://i.annihil.us/u/prod/marvel/i/mg/c/e0/535fecbbb9784/portrait_small.jpg"
		},
		{
			"id": 1017100,
			"name": "A-Bomb (HAS)",
			"description": "Rick Jones has been Hulk's best bud since day one, but now he's more than a friend...he's a teammate! Transformed by a Gamma energy explosion, A-Bomb's thick, armored skin is just as strong and powerful as it is blue. And when he curls into action, he uses it like a giant bowling ball of destruction! ",
			"image": "http://i.annihil.us/u/prod/marvel/i/mg/3/20/5232158de5b16/portrait_small.jpg"
		},
		{
			"id": 1009144,
			"name": "A.I.M.",
			"description": "AIM is a terrorist organization bent on destroying the world.",
			"image": "http://i.annihil.us/u/prod/marvel/i/mg/6/20/52602f21f29ec/portrait_small.jpg"
		},
		{
			"id": 1010699,
			"name": "Aaron Stack",
			"description": "",
			"image": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available/portrait_small.jpg"
		}
    ]
}
```

### GET hero STATUS 200
http://localhost:5000/hero/\<id>

#### Exemplo de retorno
```
{
	"id": 1010699,
	"name": "Aaron Stack",
	"description": "",
	"image": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available/portrait_small.jpg"
}
```

## Candidate
### POST candidate STATUS 201
http://localhost:5000/candidate/\<hero_id><br/>
Use o id de um hero, o novo candidato terá as informações iguais a do hero

#### Exemplo de retorno
```
{
	"id": 1011334,
	"name": "3-D Man",
	"description": "",
	"image": "http://i.annihil.us/u/prod/marvel/i/mg/c/e0/535fecbbb9784/portrait_small.jpg"
}
```
### GET candidate STATUS 200
http://localhost:5000/candidate/\<id>

#### Exemplo de retorno
```
{
	"id": 1011334,
	"name": "3-D Man",
	"description": "",
	"image": "http://i.annihil.us/u/prod/marvel/i/mg/c/e0/535fecbbb9784/portrait_small.jpg"
}
```

### GET all candidates STATUS 200
http://localhost:5000/candidate

#### Exemplo de retorno
```
{
	"candidates": [
		{
			"id": 1011334,
			"name": "3-D Man",
			"description": "",
			"image": "http://i.annihil.us/u/prod/marvel/i/mg/c/e0/535fecbbb9784/portrait_small.jpg",
			"team_id": 2
		},
		{
			"id": 1010699,
			"name": "Aaron Stack",
			"description": "",
			"image": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available/portrait_small.jpg",
			"team_id": null
		}
	]
}
```

### PATCH candidate - remove team STATUS 204
http://localhost:5000/candidate/\<id>/exit<br/>
Remove o candidate de um team

### DELETE candidate STATUS 204
http://localhost:5000/candidate/\<id>/exit

## Team
### POST team STATUS 201
http://localhost:5000/team

#### Exemplo de envio
```
{
	"name": "Alfa"
}
```

#### Exemplo de retorno
```
{
	"id": 6,
	"name": "Alfa",
	"heros": []
}
```

### GET team STATUS 200
http://localhost:5000/team/\<id>

#### Exemplo de retorno
```
{
	"id": 6,
	"name": "Alfa",
	"heros": []
}
```

### GET all teams 200
http://localhost:5000/team

#### Exemplo de retorno
```
{
	"teams": [
		{
			"id": 3,
			"name": "Caroline",
			"teams": []
		},
		{
			"id": 4,
			"name": "Bravo",
			"teams": []
		},
		{
			"id": 5,
			"name": "Delta",
			"teams": []
		},
		{
			"id": 2,
			"name": "Fenix",
			"teams": []
		},
		{
			"id": 6,
			"name": "Alfa",
			"teams": []
		}
	]
}
```

### PATCH team - rename STATUS 204
http://localhost:5000/team/\<id>

#### Exemplo de envio
```
{
	"name": "alfa"
}
```

### PATCH team - add team STATUS 204
http://localhost:5000/team/\<team_id>/\<candidate_id><br/>
Coloca um candidate em um team

### DELETE team STATUS 204
http://localhost:5000/team/\<team_id>
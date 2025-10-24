# Task Manager API

Uma API RESTful robusta e eficiente para gerenciamento de tarefas, construída com **FastAPI** e **SQLAlchemy** (SQLite). Este projeto demonstra a implementação de um backend bem estruturado, seguindo princípios de arquitetura limpa (separação de responsabilidades entre Modelos, Schemas, CRUD e Rotas).

## 🚀 Funcionalidades

*   **CRUD Completo:** Criação, Leitura, Atualização e Deleção (Soft Delete) de tarefas.
*   **Filtragem:** Listagem de tarefas com opção de filtro por status (`pending`, `in_progress`, `completed`).
*   **Validação de Dados:** Utilização de `Pydantic` para garantir a integridade dos dados de entrada e saída.
*   **Documentação Automática:** Acesso à documentação interativa da API (Swagger UI) em `/docs` e ReDoc em `/redoc`.
*   **Boas Práticas:** Uso de *Type Hints* do Python e Injeção de Dependência do FastAPI.

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
| :--- | :--- |
| **Python** | Linguagem de programação principal. |
| **FastAPI** | Framework web de alta performance para construção de APIs. |
| **SQLAlchemy** | ORM (Object-Relational Mapper) para manipulação do banco de dados. |
| **Pydantic** | Biblioteca para validação de dados e gerenciamento de configurações. |
| **SQLite** | Banco de dados leve e sem servidor, ideal para o projeto. |
| **Uvicorn** | Servidor ASGI para rodar a aplicação FastAPI. |

## ⚙️ Instalação e Execução

### Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/SEU_USUARIO/task-manager-api.git
    cd task-manager-api
    ```

2.  **Crie e ative um ambiente virtual (Recomendado):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # venv\Scripts\activate   # No Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    uvicorn app.main:app --reload
    ```
    O servidor estará rodando em `http://127.0.0.1:8000`.

## 📝 Uso da API

Após iniciar o servidor, a documentação interativa estará disponível em:

👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

Você pode usar essa interface para testar todos os endpoints:

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `POST` | `/api/v1/tasks` | Cria uma nova tarefa. |
| `GET` | `/api/v1/tasks` | Lista todas as tarefas (com filtro opcional `?status=`). |
| `GET` | `/api/v1/tasks/{task_id}` | Retorna uma tarefa específica. |
| `PUT` | `/api/v1/tasks/{task_id}` | Atualiza uma tarefa existente. |
| `DELETE` | `/api/v1/tasks/{task_id}` | Deleta (soft delete) uma tarefa. |

## 💡 Estrutura do Projeto

```
task-manager-api/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints.py  # Rotas da API (FastAPI)
│   │       └── __init__.py
│   ├── crud/
│   │   ├── task.py           # Funções CRUD (Database operations)
│   │   └── __init__.py
│   ├── models/
│   │   ├── task.py           # Modelos de dados (SQLAlchemy)
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── task.py           # Schemas de validação (Pydantic)
│   │   └── __init__.py
│   ├── database.py           # Configuração do banco de dados (Engine, SessionLocal)
│   └── main.py               # Ponto de entrada da aplicação (FastAPI)
├── .gitignore
├── requirements.txt          # Dependências do Python
└── README.md                 # Documentação principal
```

---

*Este projeto foi desenvolvido para demonstrar habilidades em desenvolvimento de API RESTful com Python e FastAPI.*

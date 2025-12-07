# SGHSS - Projeto Back-end (Escopo Essencial)
Este repositório contém a implementação mínima do projeto SGHSS (Sistema de Gestão Hospitalar e de Serviços de Saúde)
focada no **Escopo Essencial**: Autenticação (JWT), CRUD de Pacientes e CRUD de Consultas.


## Estrutura
- usuarios/: app de autenticação (User customizado por email)
- pacientes/: app com model Paciente
- consultas/: app com model Consulta
- requirements.txt: dependências

## Instruções rápidas
1. Criar virtualenv e instalar dependências:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Ajustar variáveis de ambiente (DATABASES, SECRET_KEY)
3. Rodar migrations e criar superuser
4. Executar `python manage.py runserver`

## Observações
- Este pacote é uma base para o trabalho acadêmico. Ajuste validações, políticas de LGPD e testes conforme necessário.

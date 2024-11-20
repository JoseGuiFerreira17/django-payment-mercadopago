# Projeto de Pagamentos com Django e Mercado Pago  

Este projeto utiliza **Django** para gerenciar pagamentos com integração ao **Mercado Pago** via API, suportando transações com cartão de crédito.  

## Recursos  
- Gerenciamento de usuários e métodos de pagamento.  
- Integração com o Mercado Pago para processar pagamentos.  
- Suporte para múltiplos métodos de pagamento por usuário.  
- Armazenamento seguro de informações de pagamento.  

---

## Requisitos  
- Python 3.10+  
- Django 4.2+  
- mercadopago
- requests  

---

## Instalação  

1. **Clone o repositório**  
   ```bash
   git clone git@github.com:JoseGuiFerreira17/django-payment-mercadopago.git
   cd django-payment-mercadopago

2. **Configure os arquivos env**
   ```bash
   make prebuild

3. **Configure as variáveis de ambiente**
   ```env
   SECRET_KEY=your-secret-key  
   DEBUG=True  
   MERCADO_PAGO_ACCESS_TOKEN=your-mercado-pago-access-token

4. **Execute**
    ```bash
    make build

## Configuração da API do Mercado Pago

Certifique-se de configurar sua conta do Mercado Pago para obter o ACCESS_TOKEN e habilitar métodos de pagamento.

 - Acesse o dashboard do Mercado Pago.
 - Habilite o Modo Sandbox para testes.
 - Copie o token de acesso e adicione ao .env.
  
## Endpoints Principais  

**Usuários**
- **`POST /users/`**  
  Cadastra um novo usuário no sistema.

**Métodos de Pagamento**
- **`POST /payments-methods/`**  
  Cadastro de novos métodos de pagamento para um usuário.

**Pagamento**
- **`POST /payments/`**  
    Criação de um novo pagamento.
    **Exemplo de payload:**
    ```json
        {
            "amount": 199.90,
            "installments": 3,
            "description": "Compra de produtos"
        }
    ```
    **Exemplo de response:**
    ```json
        {
            "id": "b3993342-403e-4095-9848-e5486d289de0",
            "created_at": "2024-11-15T15:57:03.972022-03:00",
            "modified_at": "2024-11-15T15:57:03.972141-03:00",
            "amount": "199.90",
            "installments": 3,
            "description": "Compra de produtos",
            "transaction_id": "1320282702",
            "status": "rejected",
            "user": "1279767a-3ce9-44c0-a875-6dfab01988d4"
        }

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

#### Termos Principais:

- **Permissões:** Você pode usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e vender cópias do Software.
- **Isenção de Garantia:** O software é fornecido "como está", sem garantias de qualquer tipo. O autor não será responsável por qualquer dano que possa resultar do uso do software.

Para mais detalhes, consulte o arquivo [LICENSE](LICENSE) no repositório.

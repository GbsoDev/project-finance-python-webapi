from domain.model.accounts.account import Account


if __name__ == "__main__":
    account = Account("Cuenta de prueba")
    print(f"cuenta creada con la descripcción {account.description}")
    print(f"la cuenta tiene {len(account.notes)} notas")
    # Usa el servicio aquíc
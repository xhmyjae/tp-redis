import redis


def ajouter_contact(redis_client, nom, numero_telephone):
    redis_client.set(f"annuaire:{nom}", numero_telephone)
    print(f"Le contact {nom} a été ajouté.")


def chercher_contact(redis_client, nom):
    numero_telephone = redis_client.get(f"annuaire:{nom}")
    if numero_telephone:
        print(f"Le numéro de téléphone de {nom} est {numero_telephone.decode()}.")
    else:
        print(f"Le contact {nom} n'est pas dans l'annuaire.")


def supprimer_contact(redis_client, nom):
    if redis_client.delete(f"annuaire:{nom}"):
        print(f"Le contact {nom} a été supprimé.")
    else:
        print(f"Le contact {nom} n'est pas dans l'annuaire.")


def main():
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    ajouter_contact(redis_client, "Alice", "123456789")
    ajouter_contact(redis_client, "Bob", "987654321")
    chercher_contact(redis_client, "Alice")
    chercher_contact(redis_client, "Charlie")
    supprimer_contact(redis_client, "Bob")
    chercher_contact(redis_client, "Bob")


if __name__ == "__main__":
    main()
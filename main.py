from utils import db

def main():
    # Nom de la BD à créer
    db_file = "data/voile.db"
    
    # Créer une connexion à la BD
    conn = db.creer_connexion(db_file)
    
    # Remplir la BD
    print("1. On crée la BD et on l'initialise avec des premières valeurs.")
    db.mise_a_jour_bd(conn, "data/voile_creation.sql")
    db.mise_a_jour_bd(conn, "data/voile_inserts_ok.sql")
    
    # Lire la BD
    print("2. Liste de tous les bateaux")
    select_tous_les_bateaux(conn)

if __name__ == "__main__":
    main()
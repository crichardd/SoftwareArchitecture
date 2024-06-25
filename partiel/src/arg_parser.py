import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="Gestionnaire de tâches")
    subparsers = parser.add_subparsers(dest='command')

    # Commande 'add'
    parser_add = subparsers.add_parser('add', help='Ajouter une nouvelle tâche avec quotes (ex: "Ma super note"')
    parser_add.add_argument('content', type=str, help='Contenu de la tâche')

    # Commande 'finish'
    parser_finish = subparsers.add_parser('finish', help='Marquer une tâche comme terminée')
    parser_finish.add_argument('id', type=int, help='Id de la tâche')

    # Commande 'list'
    parser_list = subparsers.add_parser('list', help='Lister toutes les tâches (de la plus récente à la plus ancienne')

    return parser


def parse_args():
    return create_parser().parse_args()

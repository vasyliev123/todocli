from todocli import commands
import argparse
from todocli import logger
class ToDo:

    def __init__(self):
        self.logger = logger.get_logger()
        self.commands = self.init_commands()
        self.tasks = self.init_tasks()

    
    def init_commands(self):
        self.logger.info('Initializing commands')
        desc = 'ToDo List by @vasyliev123'
        parser = argparse.ArgumentParser(description=desc)
        parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
        subparsers = parser.add_subparsers(dest='command')

        # Add subcommand
        add_parser = subparsers.add_parser('add', help='Add new task')
        add_parser.add_argument('task', help='Task to add')
        add_parser.add_argument('-d', '--due', help='Due date of the task', required=False)
        # add_parser.set_defaults(func=lambda _: commands.add)

        # List subcommand
        list_parser = subparsers.add_parser('list', help='List all tasks')
        # list_parser.set_defaults(func=lambda _: commands.list)

        # Remove subcommand
        remove_parser = subparsers.add_parser('remove', help='Remove task')
        remove_parser.add_argument('pos', help='Position of the task to remove')
        # remove_parser.set_defaults(func=lambda _: commands.remove)
        args = parser.parse_args()
        if args.command == 'add':
            commands.add(args.task, args.due)
        elif args.command == 'list':
            commands.list()
        elif args.command == 'remove':
            commands.remove(args.pos)
        else:
            pass

        return args

    def init_tasks(self):
        pass

    

    def run(self):
        self.logger.info("ToDo is started")

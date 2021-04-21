from journal import Journal
from persistence_manager import PersistenceManager

j = Journal()
j.add_entry('I cried today.')
j.add_entry('I ate a bug.')
print(f'Journal entries:\n{j}')

file = 'temp/journal.txt'
PersistenceManager.save_to_file(j, file)

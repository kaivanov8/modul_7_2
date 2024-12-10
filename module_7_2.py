
def custom_write(file_name,strings):
    file = open (file_name,'w',encoding='utf-8')
    strings_positions = {}
    n=0
    for i in strings:
        n += 1
        strings_positions.update( { (n,file.tell()) : i} )
        file.write(i)
        file.write('\n')
    file.close()
    return strings_positions

info=['Text for tell.',
      'Используйте кодировку utf-8.',
      'Because there are 2 languages!',
      'Спасибо!']
result = custom_write('test.txt',info)
for elem in result.items():
    print(elem)


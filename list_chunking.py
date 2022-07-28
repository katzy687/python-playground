def get_chunks(input_list, chunk_size):
    chunk_size = max(1, chunk_size)
    return (input_list[i:i + chunk_size] for i in xrange(0, len(input_list), chunk_size))

my_list = [1,2,3,4,5,6, 7]

result = get_chunks(my_list, 4)
for chunk in result:
    print(chunk)

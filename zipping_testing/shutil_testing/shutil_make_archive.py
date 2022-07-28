import shutil

target_dir = r"C:\Users\natti.k\code\python-playground\zipping_testing\temp_dir"

# x = shutil.make_archive("my_package", 'zip', target_dir)
package_path = shutil.make_archive(base_name="lol",
                                   format='zip',
                                   root_dir=target_dir)
pass

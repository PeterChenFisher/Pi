import os

excluded_file = 'excluded'
log_path = os.path.join(excluded_file, 'log')


def mk_dirs(dirs):
    for dir in dirs:
        try:
            if not os.path.exists(dir):
                os.mkdir(dir)
        except:
            continue


mk_dirs([excluded_file])

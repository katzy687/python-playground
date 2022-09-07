from logger_stack_level import my_wrapper, logger



def wrapper2(logger):
    my_wrapper(logger)


my_wrapper(logger)
wrapper2(logger)

try:
    # Attempt to execute some code that might throw an exception
    result = some_function()
except SomeSpecificException as e:
    # Perform specific handling for the caught exception (e.g., logging or cleanup)
    log_error(e)
    # Re-raise the exception to ensure it propagates up the call stack,
    # allowing other parts of the program to handle it if necessary
    raise e

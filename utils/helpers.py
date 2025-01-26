import time

def retry_operation(func, retries=3, delay=2, backoff=False, *args, **kwargs):
    """
    Retry a given function multiple times if it fails.

    Args:
        func (callable): The function to retry.
        retries (int): Number of retries before giving up. Default is 3.
        delay (int): Delay (in seconds) between retries. Default is 2 seconds.
        backoff (bool): If True, applies exponential backoff to the delay. Default is False.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        Any: The return value of the function if successful.

    Raises:
        Exception: If all retries fail.
    """
    for attempt in range(1, retries + 1):
        try:
            return func(*args, **kwargs)  # Pass arguments dynamically
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < retries:
                sleep_time = delay * (2 ** (attempt - 1)) if backoff else delay
                print(f"Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                print(f"All {retries} attempts failed. Raising exception.")
                raise

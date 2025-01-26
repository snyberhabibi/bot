import time

def retry_operation(func, retries=3, delay=2):
    """
    Retry a given function multiple times if it fails.

    Args:
        func (callable): The function to retry.
        retries (int): Number of retries before giving up.
        delay (int): Delay (in seconds) between retries.

    Returns:
        Any: The return value of the function if successful.

    Raises:
        Exception: If all retries fail.
    """
    for attempt in range(1, retries + 1):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < retries:
                time.sleep(delay)
            else:
                raise

from typing import (
    Any,
    Union,
    Iterable,
    Callable
)


def get(
    iterable: Iterable,
    check: Callable
) -> Union[None, Any]:
    """
    Find something within a list according to your check.
    
    Parameters
    ----------
    iterable: List[Any]
        The thing you want to iterate through
    check: Any
        The check func you want to use.
        
    Examples
    -------
    Using Lambda:
    ```python
    data = await client.fetch_emojis()
    specific_emoji = client.find(data, check=lambda emoji: emoji.name == 'this')
    ```
    
    Using a check func:
    ```python
    data = await client.fetch_emojis()
    
    def check(emoji):
        return emoji.name == 'this'
        
    specific_emoji = client.find(data, check=check)
    ```
    """
    for iter in iterable:
        if check(iter):
            return iter
    return None
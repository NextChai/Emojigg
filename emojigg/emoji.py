from typing import (
    Dict
)

class Emoji:
    def __init__(
        self, 
        data: dict
        ) -> None:
        self._raw: Dict = data
        self.id: int = data.pop('id')
        self.title: str = data.pop('title')
        self.slug: str = data.pop('slug')
        self.image: str = data.pop('image')
        self.url: str = self.image
        self.description: str = data.pop('description')
        self.category: int = data.pop('category')
        self.license: int = int(data.pop('license'))
        self.source: str = data.pop('source')
        self.faves: int = data.pop('faves')
        self.submitted_by: str = data.pop('submitted_by')
        self.width: int = data.pop('width')
        self.height: int = data.pop('height')
        self.filesize: int = data.pop('filesize')
        
    @property
    def formatted_description(self) -> str:
        """
        Returns
        -------
        str
            The emojis description formatted correctly with caps.
        """
        return self.description.capitalize()

    
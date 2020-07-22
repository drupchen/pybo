from collections import defaultdict
from pathlib import Path


class Config:
    """botok config for Tibetan dialect pack.

    Each dialect pack has two components:
      1. Dictionary:
         - contains all the data required to construct the Trie.
         - It should in the directory called `dictionary` inside the dialect pack directory.
      2. Adjustment:
         - Contains all the data required to adjust the text segmentation rules.
    """

    def __init__(self, dialect_pack_path=None):
        """Create config for dialect_pack from dialect_pack path."""
        self.reset(dialect_pack_path)

    def reset(self, dialect_pack_path=None):
        """Reset the config to default bo_general_pack."""
        if dialect_pack_path:
            self.dialect_pack_path = dialect_pack_path
        else:
            self.dialect_pack_path = (
                Path.home() / "Documents" / "pybo" / "bo_general_pack"
            )
        self.dictionary = self._get_tok_data_paths("dictionary")
        self.adjustments = self._get_tok_data_paths("adjustments")

    def _get_tok_data_paths(self, pack_component):
        """Return all the data_paths of the `pack_component.

        data_paths stored in python `dict` as per the directory
        structure of the pack component.
        """
        data_paths = defaultdict(list)
        for path in (self.dialect_pack_path / pack_component).iterdir():
            if not path.is_dir():
                continue
            data_type = path.name
            data_paths[data_type] = list(path.iterdir())
        return data_paths

    @property
    def profile(self):
        return self.dialect_pack_path.name

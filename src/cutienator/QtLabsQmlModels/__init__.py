"""
The 'cutienator.QtLabsQmlModels' package provides the cute classes of
the part of Qt named QtLabsQmlModels, under the name PySide6 has for it.

  from cutienator.QtLabsQmlModels import QQmlDelegateChoiceForeign, QQmlDelegateChooserForeign

A class is brought in the first time it is asked for, with the files it
needs and no others. So bringing in the package costs nothing, and a
program pays for the classes it uses.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'QQmlDelegateChoiceForeign',
    'QQmlDelegateChooserForeign',
    'QQmlTreeRow',
    'QQmlTableModelColumn',
    'QQmlAbstractColumnModel',
    'QQmlTableModel',
    'QQmlTreeModel',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ._q_qml_delegate_choice_foreign import QQmlDelegateChoiceForeign
  from ._q_qml_delegate_chooser_foreign import QQmlDelegateChooserForeign
  from ._q_qml_tree_row import QQmlTreeRow
  from ._q_qml_table_model_column import QQmlTableModelColumn
  from ._q_qml_abstract_column_model import QQmlAbstractColumnModel
  from ._q_qml_table_model import QQmlTableModel
  from ._q_qml_tree_model import QQmlTreeModel
else:
  #  Where each class is: the file that is brought in the first
  #  time the class is asked for.
  __class_files__ = {
      'QQmlDelegateChoiceForeign': '_q_qml_delegate_choice_foreign',
      'QQmlDelegateChooserForeign': '_q_qml_delegate_chooser_foreign',
      'QQmlTreeRow': '_q_qml_tree_row',
      'QQmlTableModelColumn': '_q_qml_table_model_column',
      'QQmlAbstractColumnModel': '_q_qml_abstract_column_model',
      'QQmlTableModel': '_q_qml_table_model',
      'QQmlTreeModel': '_q_qml_tree_model',
  }


  def __getattr__(name: str) -> Any:
    """
    Brings in a class of this part the first time it is asked for,
    as by 'from cutienator.QtLabsQmlModels import QQmlTreeModel'. Python calls
    this for a name the package does not hold yet. The file of the
    class is brought in, which brings in the files that class needs
    and no others, and the class is kept here for the next time.

    Raises
    ------

    AttributeError
      The part has no class of that name.
    """
    try:
      fileName = __class_files__[name]
    except KeyError:
      infoSpec = """module '%s' has no attribute '%s'"""
      raise AttributeError(infoSpec % (__name__, name)) from None
    module = importlib.import_module('.%s' % fileName, __name__)
    value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names every class of the part, brought in or not."""
    return [*__all__]

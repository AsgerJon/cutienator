"""
qdesigner_internal::TreeWidgetContents binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::TreeWidgetContents to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QTreeWidget, QTreeWidgetItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTreeWidget = WAIT['QTreeWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class TreeWidgetContents(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::TreeWidgetContents: a plain
  Python object standing in front of one C++
  qdesigner_internal::TreeWidgetContents.

  C++ hands a qdesigner_internal::TreeWidgetContents around as a copy, so
  every C++ qdesigner_internal::TreeWidgetContents behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::TreeWidgetContents that has a
  ritual and that Python can call so far, 5 names in all: 'clear',
  'fromTreeWidget', 'applyToTreeWidget', '__eq__', '__ne__'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::TreeWidgetContents::~TreeWidgetContents()': the
    destructor: Python removes its C++ qdesigner_internal::TreeWidgetContents
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::TreeWidgetContents is created at the first
    use, not by 'qdesigner_internal::TreeWidgetContents(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::TreeWidgetContents back gives a
    copy the ritual made for Python, in a new cute
    qdesigner_internal::TreeWidgetContents.
  """

  #  The classes Qt writes inside qdesigner_internal::TreeWidgetContents,
  #  each a class in here as in C++.

  class ItemContents(qdesigner_internal.ListContents):
    """
    The cute side of Qt's
    qdesigner_internal::TreeWidgetContents::ItemContents: a plain Python
    object standing in front of one C++
    qdesigner_internal::TreeWidgetContents::ItemContents.

    It is built on the cute 'qdesigner_internal::ListContents', as Qt's
    qdesigner_internal::TreeWidgetContents::ItemContents is built on Qt's
    qdesigner_internal::ListContents, and has everything that class has.

    C++ hands a qdesigner_internal::TreeWidgetContents::ItemContents around
    as a copy, so every C++
    qdesigner_internal::TreeWidgetContents::ItemContents behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's
    qdesigner_internal::TreeWidgetContents::ItemContents that has a ritual
    and that Python can call so far, 3 names in all: 'createTreeItem',
    '__eq__', '__ne__'. It can be made from Python, in 2 ways; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'qdesigner_internal::TreeWidgetContents::ItemContents::~ItemContents(
      )': the destructor: Python removes its C++
      qdesigner_internal::TreeWidgetContents::ItemContents by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ qdesigner_internal::TreeWidgetContents::ItemContents is created
      at the first use, not by
      'qdesigner_internal::TreeWidgetContents::ItemContents(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      qdesigner_internal::TreeWidgetContents::ItemContents back gives a copy
      the ritual made for Python, in a new cute
      qdesigner_internal::TreeWidgetContents::ItemContents.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QTreeWidgetItem = WAIT['QTreeWidgetItem']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'qdesigner_internal::TreeWidgetContents::ItemContents'

    #  Qt's '~qdesigner_internal::TreeWidgetContents::ItemContents()'. Naming
    #  it makes this a value class: Python owns every C++
    #  qdesigner_internal::TreeWidgetContents::ItemContents behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN18qdesigner_internal18TreeWidgetContents12ItemContentsD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(WAIT['qdesigner_internal.DesignerIconCache'], bool)
    @overload(NoneType, bool)
    def createTreeItem(
        self,
        iconCache: Optional[qdesigner_internal.DesignerIconCache],
        editor: bool,
    ) -> Optional[QTreeWidgetItem]:
      """
      Calls Qt's 'QTreeWidgetItem
      *qdesigner_internal::TreeWidgetContents::ItemContents::createTreeItem(
      DesignerIconCache *iconCache, bool editor) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-treewidgetcontents-itemcontents.html

      Parameters
      ----------

      iconCache : Optional[qdesigner_internal.DesignerIconCache]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      editor : bool
        Passed on as it is.

      Returns
      -------

      Optional[QTreeWidgetItem]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QTreeWidgetItem
      #      *qdesigner_internal::TreeWidgetContents::ItemContents::
      #      createTreeItem(DesignerIconCache *iconCache, bool editor) const
      address = self.uglySide.call(
          'ritual_ZNK18qdesigner_internal18TreeWidgetContents12ItemContents'
          '14createTreeItemEPNS_17DesignerIconCacheEb',
          self._addressOf(iconCache), editor,
      )
      from ..QtWidgets import QTreeWidgetItem
      return QTreeWidgetItem._cuteAt(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __eq__(self, rhs: TreeWidgetContents.ItemContents) -> bool:
      """
      Calls Qt's 'bool operator==(const ItemContents &lhs, const ItemContents
      &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-treewidgetcontents-itemcontents.html

      Parameters
      ----------

      rhs : TreeWidgetContents.ItemContents
        Passed on as a value: Qt reads the C++
        qdesigner_internal::TreeWidgetContents::ItemContents, which stays
        Python's own.
      """
      #  bool operator==(const ItemContents &lhs, const ItemContents &rhs)
      return Rituals.call(
          'ritual_ZN18qdesigner_internaleqERKNS_18TreeWidgetContents12ItemC'
          'ontentsES3_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __ne__(self, rhs: TreeWidgetContents.ItemContents) -> bool:
      """
      Calls Qt's 'bool operator!=(const ItemContents &lhs, const ItemContents
      &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-treewidgetcontents-itemcontents.html

      Parameters
      ----------

      rhs : TreeWidgetContents.ItemContents
        Passed on as a value: Qt reads the C++
        qdesigner_internal::TreeWidgetContents::ItemContents, which stays
        Python's own.
      """
      #  bool operator!=(const ItemContents &lhs, const ItemContents &rhs)
      return Rituals.call(
          'ritual_ZN18qdesigner_internalneERKNS_18TreeWidgetContents12ItemC'
          'ontentsES3_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
      )

    @overload.fallback
    def __ne__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'qdesigner_internal::TreeWidgetContents::ItemContents::ItemContents()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-treewidgetcontents-itemcontents.html
      """
      #  qdesigner_internal::TreeWidgetContents::ItemContents::ItemContents()
      self._noteCreation(
          TreeWidgetContents.ItemContents, lambda: Rituals.call(
              'ritual_ZN18qdesigner_internal18TreeWidgetContents12ItemConte'
              'ntsC1Ev',
          ))

    @overload(QTreeWidgetItem, bool)
    @overload(NoneType, bool)
    def __init__(
        self,
        item: Optional[QTreeWidgetItem],
        editor: bool,
    ) -> None:
      """
      Notes what was given, for Qt's
      'qdesigner_internal::TreeWidgetContents::ItemContents::ItemContents(
      const QTreeWidgetItem *item, bool editor)', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-treewidgetcontents-itemcontents.html

      Parameters
      ----------

      item : Optional[QTreeWidgetItem]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      editor : bool
        Passed on as it is.
      """
      #  qdesigner_internal::TreeWidgetContents::ItemContents::
      #      ItemContents(const QTreeWidgetItem *item, bool editor)
      self._noteCreation(
          TreeWidgetContents.ItemContents, lambda: Rituals.call(
              'ritual_ZN18qdesigner_internal18TreeWidgetContents12ItemConte'
              'ntsC1EPK15QTreeWidgetItemb',
              self._addressOf(item), editor,
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::TreeWidgetContents'

  #  Qt's '~qdesigner_internal::TreeWidgetContents()'. Naming it makes this a
  #  value class: Python owns every C++
  #  qdesigner_internal::TreeWidgetContents behind a cute one, and removes it
  #  by this ritual.
  __delete_ritual__ = 'ritual_ZN18qdesigner_internal18TreeWidgetContentsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: TreeWidgetContents) -> bool:
    """
    Calls Qt's 'bool operator==(const TreeWidgetContents &lhs, const
    TreeWidgetContents &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-treewidgetcontents.html

    Parameters
    ----------

    rhs : TreeWidgetContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::TreeWidgetContents, which stays Python's own.
    """
    #  bool operator==(const TreeWidgetContents &lhs, const
    #      TreeWidgetContents &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_18TreeWidgetContentsES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: TreeWidgetContents) -> bool:
    """
    Calls Qt's 'bool operator!=(const TreeWidgetContents &lhs, const
    TreeWidgetContents &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-treewidgetcontents.html

    Parameters
    ----------

    rhs : TreeWidgetContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::TreeWidgetContents, which stays Python's own.
    """
    #  bool operator!=(const TreeWidgetContents &lhs, const
    #      TreeWidgetContents &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_18TreeWidgetContentsES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clear(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::TreeWidgetContents::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-treewidgetcontents.html#clear
    """
    #  void qdesigner_internal::TreeWidgetContents::clear()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TreeWidgetContents5clearEv',
    )

  @overload(QTreeWidget, bool)
  @overload(NoneType, bool)
  def fromTreeWidget(
      self,
      treeWidget: Optional[QTreeWidget],
      editor: bool,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TreeWidgetContents::fromTreeWidget(const QTreeWidget
    *treeWidget, bool editor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-treewidgetcontents.html

    Parameters
    ----------

    treeWidget : Optional[QTreeWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    editor : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::TreeWidgetContents::fromTreeWidget(const
    #      QTreeWidget *treeWidget, bool editor)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18TreeWidgetContents14fromTreeWidgetE'
        'PK11QTreeWidgetb',
        self._addressOf(treeWidget), editor,
    )

  @overload(QTreeWidget, WAIT['qdesigner_internal.DesignerIconCache'], bool)
  @overload(QTreeWidget, NoneType, bool)
  @overload(NoneType, WAIT['qdesigner_internal.DesignerIconCache'], bool)
  @overload(NoneType, NoneType, bool)
  def applyToTreeWidget(
      self,
      treeWidget: Optional[QTreeWidget],
      iconCache: Optional[qdesigner_internal.DesignerIconCache],
      editor: bool,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::TreeWidgetContents::applyToTreeWidget(QTreeWidget
    *treeWidget, DesignerIconCache *iconCache, bool editor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-treewidgetcontents.html

    Parameters
    ----------

    treeWidget : Optional[QTreeWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iconCache : Optional[qdesigner_internal.DesignerIconCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    editor : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::TreeWidgetContents::applyToTreeWidget(
    #      QTreeWidget *treeWidget, DesignerIconCache *iconCache, bool
    #      editor) const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18TreeWidgetContents17applyToTreeWid'
        'getEP11QTreeWidgetPNS_17DesignerIconCacheEb',
        self._addressOf(treeWidget), self._addressOf(iconCache), editor,
    )

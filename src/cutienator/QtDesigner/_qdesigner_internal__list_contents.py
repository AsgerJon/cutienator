"""
qdesigner_internal::ListContents binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ListContents to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QComboBox, QListWidget, QTreeWidgetItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QComboBox = WAIT['QComboBox']
  QListWidget = WAIT['QListWidget']
  QTreeWidgetItem = WAIT['QTreeWidgetItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ListContents(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::ListContents: a plain Python
  object standing in front of one C++ qdesigner_internal::ListContents.

  C++ hands a qdesigner_internal::ListContents around as a copy, so every C++
  qdesigner_internal::ListContents behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ListContents that has a ritual
  and that Python can call so far, 7 names in all: 'createTreeItem',
  'createFromListWidget', 'applyToListWidget', 'createFromComboBox',
  'applyToComboBox', '__eq__', '__ne__'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::ListContents::~ListContents()': the destructor:
    Python removes its C++ qdesigner_internal::ListContents by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::ListContents is created at the first use, not
    by 'qdesigner_internal::ListContents(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::ListContents back gives a copy
    the ritual made for Python, in a new cute
    qdesigner_internal::ListContents.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ListContents'

  #  Qt's '~qdesigner_internal::ListContents()'. Naming it makes this a value
  #  class: Python owns every C++ qdesigner_internal::ListContents behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18qdesigner_internal12ListContentsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['qdesigner_internal.DesignerIconCache'])
  @overload(NoneType)
  def createTreeItem(
      self,
      iconCache: Optional[qdesigner_internal.DesignerIconCache],
  ) -> Optional[QTreeWidgetItem]:
    """
    Calls Qt's 'QTreeWidgetItem
    *qdesigner_internal::ListContents::createTreeItem(DesignerIconCache
    *iconCache) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-listcontents.html

    Parameters
    ----------

    iconCache : Optional[qdesigner_internal.DesignerIconCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTreeWidgetItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTreeWidgetItem *qdesigner_internal::ListContents::createTreeItem(
    #      DesignerIconCache *iconCache) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12ListContents14createTreeItemEPNS_1'
        '7DesignerIconCacheE',
        self._addressOf(iconCache),
    )
    from ..QtWidgets import QTreeWidgetItem
    return QTreeWidgetItem._cuteAt(address)

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
  def __eq__(self, rhs: ListContents) -> bool:
    """
    Calls Qt's 'bool operator==(const ListContents &lhs, const ListContents
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-listcontents.html#operator==

    Parameters
    ----------

    rhs : ListContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::ListContents, which stays Python's own.
    """
    #  bool operator==(const ListContents &lhs, const ListContents &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_12ListContentsES2_',
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
  def __ne__(self, rhs: ListContents) -> bool:
    """
    Calls Qt's 'bool operator!=(const ListContents &lhs, const ListContents
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-listcontents.html#operator!=

    Parameters
    ----------

    rhs : ListContents
      Passed on as a value: Qt reads the C++
      qdesigner_internal::ListContents, which stays Python's own.
    """
    #  bool operator!=(const ListContents &lhs, const ListContents &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_12ListContentsES2_',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::ListContents::ListContents()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-listcontents.html#ListContents
    """
    #  qdesigner_internal::ListContents::ListContents()
    self._noteCreation(ListContents, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal12ListContentsC1Ev',
    ))

  @overload(QTreeWidgetItem)
  @overload(NoneType)
  def __init__(self, item: Optional[QTreeWidgetItem]) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::ListContents::ListContents(const QTreeWidgetItem
    *item)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-listcontents.html#ListContents

    Parameters
    ----------

    item : Optional[QTreeWidgetItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::ListContents::ListContents(const QTreeWidgetItem
    #      *item)
    self._noteCreation(ListContents, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal12ListContentsC1EPK15QTreeWidgetItem',
        self._addressOf(item),
    ))

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

  @overload(QListWidget, bool)
  @overload(NoneType, bool)
  def createFromListWidget(
      self,
      listWidget: Optional[QListWidget],
      editor: bool,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ListContents::createFromListWidget(const QListWidget
    *listWidget, bool editor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-listcontents.html

    Parameters
    ----------

    listWidget : Optional[QListWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    editor : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::ListContents::createFromListWidget(const
    #      QListWidget *listWidget, bool editor)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ListContents20createFromListWidgetE'
        'PK11QListWidgetb',
        self._addressOf(listWidget), editor,
    )

  @overload(QListWidget, WAIT['qdesigner_internal.DesignerIconCache'], bool)
  @overload(QListWidget, NoneType, bool)
  @overload(NoneType, WAIT['qdesigner_internal.DesignerIconCache'], bool)
  @overload(NoneType, NoneType, bool)
  @overload(
      QListWidget, WAIT['qdesigner_internal.DesignerIconCache'], bool,
      Qt.Alignment,
  )
  @overload(QListWidget, NoneType, bool, Qt.Alignment)
  @overload(
      NoneType, WAIT['qdesigner_internal.DesignerIconCache'], bool,
      Qt.Alignment,
  )
  @overload(NoneType, NoneType, bool, Qt.Alignment)
  def applyToListWidget(
      self,
      listWidget: Optional[QListWidget],
      iconCache: Optional[qdesigner_internal.DesignerIconCache],
      editor: bool,
      alignmentDefault: Qt.Alignment = (
          Qt.Alignment.AlignLeading | Qt.Alignment.AlignVCenter),
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ListContents::applyToListWidget(QListWidget
    *listWidget, DesignerIconCache *iconCache, bool editor, Qt::Alignment
    alignmentDefault) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-listcontents.html

    Parameters
    ----------

    listWidget : Optional[QListWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iconCache : Optional[qdesigner_internal.DesignerIconCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    editor : bool
      Passed on as it is.

    alignmentDefault : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment.AlignLeading | Qt.Alignment.AlignVCenter.
    """
    #  void qdesigner_internal::ListContents::applyToListWidget(QListWidget
    #      *listWidget, DesignerIconCache *iconCache, bool editor,
    #      Qt::Alignment alignmentDefault) const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12ListContents17applyToListWidgetEP1'
        '1QListWidgetPNS_17DesignerIconCacheEb6QFlagsIN2Qt13AlignmentFlagEE',
        self._addressOf(listWidget), self._addressOf(iconCache), editor,
        alignmentDefault.value,
    )

  @overload(QComboBox)
  @overload(NoneType)
  def createFromComboBox(self, listWidget: Optional[QComboBox]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ListContents::createFromComboBox(const QComboBox
    *listWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-listcontents.html

    Parameters
    ----------

    listWidget : Optional[QComboBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ListContents::createFromComboBox(const
    #      QComboBox *listWidget)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ListContents18createFromComboBoxEPK'
        '9QComboBox',
        self._addressOf(listWidget),
    )

  @overload(QComboBox, WAIT['qdesigner_internal.DesignerIconCache'])
  @overload(QComboBox, NoneType)
  @overload(NoneType, WAIT['qdesigner_internal.DesignerIconCache'])
  @overload(NoneType, NoneType)
  def applyToComboBox(
      self,
      listWidget: Optional[QComboBox],
      iconCache: Optional[qdesigner_internal.DesignerIconCache],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ListContents::applyToComboBox(QComboBox *listWidget,
    DesignerIconCache *iconCache) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-listcontents.html

    Parameters
    ----------

    listWidget : Optional[QComboBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iconCache : Optional[qdesigner_internal.DesignerIconCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ListContents::applyToComboBox(QComboBox
    #      *listWidget, DesignerIconCache *iconCache) const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12ListContents15applyToComboBoxEP9QC'
        'omboBoxPNS_17DesignerIconCacheE',
        self._addressOf(listWidget), self._addressOf(iconCache),
    )

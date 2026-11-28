"""
QToolBarAreaLayoutInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtoolbararealayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QToolBarAreaLayoutInfo to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QInternal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QSize
  from . import QLayoutItem, QToolBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLayoutItem = WAIT['QLayoutItem']
  QPoint = WAIT['QPoint']
  QToolBar = WAIT['QToolBar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QToolBarAreaLayoutInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QToolBarAreaLayoutInfo: a plain Python object
  standing in front of one C++ QToolBarAreaLayoutInfo.

  C++ hands a QToolBarAreaLayoutInfo around as a copy, so every C++
  QToolBarAreaLayoutInfo behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QToolBarAreaLayoutInfo that has a ritual and that
  Python can call so far, 9 names in all: 'sizeHint', 'minimumSize',
  'insertToolBar', 'insertItem', 'removeToolBar', 'insertToolBarBreak',
  'removeToolBarBreak', 'clear', 'distance'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<int> QToolBarAreaLayoutInfo::gapIndex(const QPoint &pos, int
    *maxDistance) const': takes a number to change where it is.
  - Qt's 'bool QToolBarAreaLayoutInfo::insertGap(const QList<int> &path,
    QLayoutItem *item)': takes a type Python has no way to hand over yet.
  - Qt's 'QRect QToolBarAreaLayoutInfo::itemRect(const QList<int> &path)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QToolBarAreaLayoutInfo::~QToolBarAreaLayoutInfo()': the destructor:
    Python removes its C++ QToolBarAreaLayoutInfo by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 leans on 'QToolBarLayout.

  What to expect
  --------------

  - The C++ QToolBarAreaLayoutInfo is created at the first use, not by
    'QToolBarAreaLayoutInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QToolBarAreaLayoutInfo back gives a copy the ritual
    made for Python, in a new cute QToolBarAreaLayoutInfo.
  - Each name of Qt's QToolBarAreaLayoutInfo that has no cute function yet,
    'fitLayout', 'gapIndex', 'insertGap', 'itemRect', 'moveToolBar', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QToolBarAreaLayoutInfo'

  #  Qt's '~QToolBarAreaLayoutInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QToolBarAreaLayoutInfo behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QToolBarAreaLayoutInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QToolBarAreaLayoutInfo::sizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutinfo.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBarAreaLayoutInfo::sizeHint() const
    address = self.uglySide.call(
        'ritual_ZNK22QToolBarAreaLayoutInfo8sizeHintEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QToolBarAreaLayoutInfo::minimumSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutinfo.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBarAreaLayoutInfo::minimumSize() const
    address = self.uglySide.call(
        'ritual_ZNK22QToolBarAreaLayoutInfo11minimumSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QPoint)
  def distance(self, pos: QPoint) -> int:
    """
    Calls Qt's 'int QToolBarAreaLayoutInfo::distance(const QPoint &pos)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutinfo.html#distance

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QToolBarAreaLayoutInfo::distance(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK22QToolBarAreaLayoutInfo8distanceERK6QPoint',
        self._valueOf(pos),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QInternal.DockPosition)
  def __init__(
      self,
      pos: QInternal.DockPosition = QInternal.DockPosition.TopDock,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QToolBarAreaLayoutInfo::QToolBarAreaLayoutInfo(QInternal::DockPosition
    pos)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutinfo.html#QToolBarAreaLayoutInfo

    Parameters
    ----------

    pos : QInternal.DockPosition
      Passed on as its number. May be left out, as in Qt: it is then
      QInternal.DockPosition.TopDock.
    """
    #  QToolBarAreaLayoutInfo::QToolBarAreaLayoutInfo(QInternal::DockPosition
    #      pos)
    self._noteCreation(QToolBarAreaLayoutInfo, lambda: Rituals.call(
        'ritual_ZN22QToolBarAreaLayoutInfoC1EN9QInternal12DockPositionE',
        pos.value,
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

  @overload(QToolBar, QToolBar)
  @overload(QToolBar, NoneType)
  @overload(NoneType, QToolBar)
  @overload(NoneType, NoneType)
  def insertToolBar(
      self,
      before: Optional[QToolBar],
      toolBar: Optional[QToolBar],
  ) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QToolBarAreaLayoutInfo::insertToolBar(QToolBar
    *before, QToolBar *toolBar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutinfo.html#insertToolBar

    Parameters
    ----------

    before : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    toolBar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QToolBarAreaLayoutInfo::insertToolBar(QToolBar *before,
    #      QToolBar *toolBar)
    address = self.uglySide.call(
        'ritual_ZN22QToolBarAreaLayoutInfo13insertToolBarEP8QToolBarS1_',
        self._addressOf(before), self._addressOf(toolBar),
    )
    from . import QLayoutItem
    return QLayoutItem._cuteAt(address)

  @overload(QToolBar, QLayoutItem)
  @overload(QToolBar, NoneType)
  @overload(NoneType, QLayoutItem)
  @overload(NoneType, NoneType)
  def insertItem(
      self,
      before: Optional[QToolBar],
      item: Optional[QLayoutItem],
  ) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayoutInfo::insertItem(QToolBar *before,
    QLayoutItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutinfo.html#insertItem

    Parameters
    ----------

    before : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarAreaLayoutInfo::insertItem(QToolBar *before, QLayoutItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN22QToolBarAreaLayoutInfo10insertItemEP8QToolBarP11QLayout'
        'Item',
        self._addressOf(before), self._addressOf(item, 'QLayoutItem'),
    )

  @overload(QToolBar)
  @overload(NoneType)
  def removeToolBar(self, toolBar: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayoutInfo::removeToolBar(QToolBar
    *toolBar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutinfo.html#removeToolBar

    Parameters
    ----------

    toolBar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarAreaLayoutInfo::removeToolBar(QToolBar *toolBar)
    self.uglySide.call(
        'ritual_ZN22QToolBarAreaLayoutInfo13removeToolBarEP8QToolBar',
        self._addressOf(toolBar),
    )

  @overload(QToolBar)
  @overload(NoneType)
  def insertToolBarBreak(self, before: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayoutInfo::insertToolBarBreak(QToolBar
    *before)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutinfo.html#insertToolBarBreak

    Parameters
    ----------

    before : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarAreaLayoutInfo::insertToolBarBreak(QToolBar *before)
    self.uglySide.call(
        'ritual_ZN22QToolBarAreaLayoutInfo18insertToolBarBreakEP8QToolBar',
        self._addressOf(before),
    )

  @overload(QToolBar)
  @overload(NoneType)
  def removeToolBarBreak(self, before: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayoutInfo::removeToolBarBreak(QToolBar
    *before)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayoutinfo.html#removeToolBarBreak

    Parameters
    ----------

    before : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarAreaLayoutInfo::removeToolBarBreak(QToolBar *before)
    self.uglySide.call(
        'ritual_ZN22QToolBarAreaLayoutInfo18removeToolBarBreakEP8QToolBar',
        self._addressOf(before),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayoutInfo::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbararealayoutinfo.html#clear
    """
    #  void QToolBarAreaLayoutInfo::clear()
    self.uglySide.call('ritual_ZN22QToolBarAreaLayoutInfo5clearEv')

  @staticmethod
  def fitLayout(*__, **_) -> Never:
    """
    Qt's 'void QToolBarAreaLayoutInfo::fitLayout()': leans on
    'QToolBarLayout::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayoutInfo.fitLayout' has no cute function yet. Qt's "
        "'void QToolBarAreaLayoutInfo::fitLayout()': leans on "
        "'QToolBarLayout::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def gapIndex(*__, **_) -> Never:
    """
    Qt's 'QList<int> QToolBarAreaLayoutInfo::gapIndex(const QPoint &pos, int
    *maxDistance) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayoutInfo.gapIndex' has no cute function yet. Qt's "
        "'QList<int> QToolBarAreaLayoutInfo::gapIndex(const QPoint &pos, "
        "int *maxDistance) const': takes a number to change where it is.")

  @staticmethod
  def insertGap(*__, **_) -> Never:
    """
    Qt's 'bool QToolBarAreaLayoutInfo::insertGap(const QList<int> &path,
    QLayoutItem *item)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayoutInfo.insertGap' has no cute function yet. Qt's "
        "'bool QToolBarAreaLayoutInfo::insertGap(const QList<int> &path, "
        "QLayoutItem *item)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def itemRect(*__, **_) -> Never:
    """
    Qt's 'QRect QToolBarAreaLayoutInfo::itemRect(const QList<int> &path)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayoutInfo.itemRect' has no cute function yet. Qt's "
        "'QRect QToolBarAreaLayoutInfo::itemRect(const QList<int> &path) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def moveToolBar(*__, **_) -> Never:
    """
    Qt's 'void QToolBarAreaLayoutInfo::moveToolBar(QToolBar *toolbar, int
    pos)': leans on 'QToolBarLayout::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayoutInfo.moveToolBar' has no cute function yet. "
        "Qt's 'void QToolBarAreaLayoutInfo::moveToolBar(QToolBar *toolbar, "
        "int pos)': leans on 'QToolBarLayout::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

"""
QToolBarAreaLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtoolbararealayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QToolBarAreaLayout to be private: it declares the class in a
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

  from ..QtCore import QRect, QSize
  from . import QLayoutItem, QMainWindow, QStyleOptionToolBar, QToolBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLayoutItem = WAIT['QLayoutItem']
  QMainWindow = WAIT['QMainWindow']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QStyleOptionToolBar = WAIT['QStyleOptionToolBar']
  QToolBar = WAIT['QToolBar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QToolBarAreaLayout(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QToolBarAreaLayout: a plain Python object standing in
  front of one C++ QToolBarAreaLayout.

  C++ hands a QToolBarAreaLayout around as a copy, so every C++
  QToolBarAreaLayout behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QToolBarAreaLayout that has a ritual and that Python
  can call so far, 16 names in all: 'minimumSize', 'rectHint', 'sizeHint',
  'deleteAllLayoutItems', 'insertToolBar', 'removeToolBar', 'addToolBar',
  'insertToolBarBreak', 'removeToolBarBreak', 'addToolBarBreak',
  'insertItem', 'toolBarBreak', 'getStyleOptionInfo', 'remove', 'clear',
  'isEmpty'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLayoutItem *QToolBarAreaLayout::itemAt(int *x, int index) const':
    takes a number to change where it is.
  - Qt's 'QLayoutItem *QToolBarAreaLayout::takeAt(int *x, int index)': takes
    a number to change where it is.
  - Qt's 'std::optional<QInternal::DockPosition>
    QToolBarAreaLayout::findToolBar(const QToolBar *toolBar) const': gives a
    type Python has no way to take yet.
  - Qt's 'QList<int> QToolBarAreaLayout::indexOf(QWidget *toolBar) const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<int> QToolBarAreaLayout::gapIndex(const QPoint &pos) const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<int> QToolBarAreaLayout::currentGapIndex() const': gives a
    type Python has no way to take yet.
  - Qt's 'bool QToolBarAreaLayout::insertGap(const QList<int> &path,
    QLayoutItem *item)': takes a type Python has no way to hand over yet.
  - Qt's 'void QToolBarAreaLayout::remove(const QList<int> &path)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QToolBarAreaLayoutItem *QToolBarAreaLayout::item(const QList<int>
    &path)': takes a type Python has no way to hand over yet.
  - Qt's 'QRect QToolBarAreaLayout::itemRect(const QList<int> &path) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QLayoutItem *QToolBarAreaLayout::plug(const QList<int> &path)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QLayoutItem *QToolBarAreaLayout::unplug(const QList<int> &path,
    QToolBarAreaLayout *other)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QToolBarAreaLayout::saveState(QDataStream &stream) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QToolBarAreaLayout::~QToolBarAreaLayout()': the destructor: Python
    removes its C++ QToolBarAreaLayout by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 36 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'QToolBarLayout.

  What to expect
  --------------

  - The C++ QToolBarAreaLayout is created at the first use, not by
    'QToolBarAreaLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QToolBarAreaLayout back gives a copy the ritual made
    for Python, in a new cute QToolBarAreaLayout.
  - Each name of Qt's QToolBarAreaLayout that has no cute function yet,
    'apply', 'currentGapIndex', 'findToolBar', 'fitLayout', 'gapIndex',
    'indexOf', 'insertGap', 'item', 'itemAt', 'itemRect', 'moveToolBar',
    'plug', 'restoreState', 'saveState', 'takeAt', 'unplug', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QToolBarAreaLayout'

  #  Qt's '~QToolBarAreaLayout()'. Naming it makes this a value class: Python
  #  owns every C++ QToolBarAreaLayout behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QToolBarAreaLayoutD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def minimumSize(self, centerMin: QSize) -> QSize:
    """
    Calls Qt's 'QSize QToolBarAreaLayout::minimumSize(const QSize &centerMin)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayout.html#minimumSize

    Parameters
    ----------

    centerMin : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBarAreaLayout::minimumSize(const QSize &centerMin) const
    address = self.uglySide.call(
        'ritual_ZNK18QToolBarAreaLayout11minimumSizeERK5QSize',
        self._valueOf(centerMin),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QRect)
  def rectHint(self, r: QRect) -> QRect:
    """
    Calls Qt's 'QRect QToolBarAreaLayout::rectHint(const QRect &r) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbararealayout.html#rectHint

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QToolBarAreaLayout::rectHint(const QRect &r) const
    address = self.uglySide.call(
        'ritual_ZNK18QToolBarAreaLayout8rectHintERK5QRect', self._valueOf(r),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QSize)
  def sizeHint(self, center: QSize) -> QSize:
    """
    Calls Qt's 'QSize QToolBarAreaLayout::sizeHint(const QSize &center)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbararealayout.html#sizeHint

    Parameters
    ----------

    center : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBarAreaLayout::sizeHint(const QSize &center) const
    address = self.uglySide.call(
        'ritual_ZNK18QToolBarAreaLayout8sizeHintERK5QSize',
        self._valueOf(center),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QToolBar)
  @overload(NoneType)
  def toolBarBreak(self, toolBar: Optional[QToolBar]) -> bool:
    """
    Calls Qt's 'bool QToolBarAreaLayout::toolBarBreak(QToolBar *toolBar)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayout.html#toolBarBreak

    Parameters
    ----------

    toolBar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QToolBarAreaLayout::toolBarBreak(QToolBar *toolBar) const
    return self.uglySide.call(
        'ritual_ZNK18QToolBarAreaLayout12toolBarBreakEP8QToolBar',
        self._addressOf(toolBar),
    )

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QToolBarAreaLayout::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbararealayout.html#isEmpty
    """
    #  bool QToolBarAreaLayout::isEmpty() const
    return self.uglySide.call('ritual_ZNK18QToolBarAreaLayout7isEmptyEv')

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

  @overload(QMainWindow)
  @overload(NoneType)
  def __init__(self, win: Optional[QMainWindow]) -> None:
    """
    Notes what was given, for Qt's
    'QToolBarAreaLayout::QToolBarAreaLayout(const QMainWindow *win)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayout.html#QToolBarAreaLayout

    Parameters
    ----------

    win : Optional[QMainWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QToolBarAreaLayout::QToolBarAreaLayout(const QMainWindow *win)
    self._noteCreation(QToolBarAreaLayout, lambda: Rituals.call(
        'ritual_ZN18QToolBarAreaLayoutC1EPK11QMainWindow',
        self._addressOf(win),
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

  def deleteAllLayoutItems(self) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayout::deleteAllLayoutItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayout.html#deleteAllLayoutItems
    """
    #  void QToolBarAreaLayout::deleteAllLayoutItems()
    self.uglySide.call(
        'ritual_ZN18QToolBarAreaLayout20deleteAllLayoutItemsEv',
    )

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
    Calls Qt's 'QLayoutItem *QToolBarAreaLayout::insertToolBar(QToolBar
    *before, QToolBar *toolBar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayout.html#insertToolBar

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
    #  QLayoutItem *QToolBarAreaLayout::insertToolBar(QToolBar *before,
    #      QToolBar *toolBar)
    address = self.uglySide.call(
        'ritual_ZN18QToolBarAreaLayout13insertToolBarEP8QToolBarS1_',
        self._addressOf(before), self._addressOf(toolBar),
    )
    from . import QLayoutItem
    return QLayoutItem._cuteAt(address)

  @overload(QToolBar)
  @overload(NoneType)
  def removeToolBar(self, toolBar: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayout::removeToolBar(QToolBar *toolBar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayout.html#removeToolBar

    Parameters
    ----------

    toolBar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarAreaLayout::removeToolBar(QToolBar *toolBar)
    self.uglySide.call(
        'ritual_ZN18QToolBarAreaLayout13removeToolBarEP8QToolBar',
        self._addressOf(toolBar),
    )

  @overload(QInternal.DockPosition, QToolBar)
  @overload(QInternal.DockPosition, NoneType)
  def addToolBar(
      self,
      pos: QInternal.DockPosition,
      toolBar: Optional[QToolBar],
  ) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem
    *QToolBarAreaLayout::addToolBar(QInternal::DockPosition pos, QToolBar
    *toolBar)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbararealayout.html#addToolBar

    Parameters
    ----------

    pos : QInternal.DockPosition
      Passed on as its number.

    toolBar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QToolBarAreaLayout::addToolBar(QInternal::DockPosition
    #      pos, QToolBar *toolBar)
    address = self.uglySide.call(
        'ritual_ZN18QToolBarAreaLayout10addToolBarEN9QInternal12DockPositio'
        'nEP8QToolBar',
        pos.value, self._addressOf(toolBar),
    )
    from . import QLayoutItem
    return QLayoutItem._cuteAt(address)

  @overload(QToolBar)
  @overload(NoneType)
  def insertToolBarBreak(self, before: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayout::insertToolBarBreak(QToolBar
    *before)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayout.html#insertToolBarBreak

    Parameters
    ----------

    before : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarAreaLayout::insertToolBarBreak(QToolBar *before)
    self.uglySide.call(
        'ritual_ZN18QToolBarAreaLayout18insertToolBarBreakEP8QToolBar',
        self._addressOf(before),
    )

  @overload(QToolBar)
  @overload(NoneType)
  def removeToolBarBreak(self, before: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayout::removeToolBarBreak(QToolBar
    *before)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayout.html#removeToolBarBreak

    Parameters
    ----------

    before : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarAreaLayout::removeToolBarBreak(QToolBar *before)
    self.uglySide.call(
        'ritual_ZN18QToolBarAreaLayout18removeToolBarBreakEP8QToolBar',
        self._addressOf(before),
    )

  @overload(QInternal.DockPosition)
  def addToolBarBreak(self, pos: QInternal.DockPosition) -> None:
    """
    Calls Qt's 'void
    QToolBarAreaLayout::addToolBarBreak(QInternal::DockPosition pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayout.html#addToolBarBreak

    Parameters
    ----------

    pos : QInternal.DockPosition
      Passed on as its number.
    """
    #  void QToolBarAreaLayout::addToolBarBreak(QInternal::DockPosition pos)
    self.uglySide.call(
        'ritual_ZN18QToolBarAreaLayout15addToolBarBreakEN9QInternal12DockPo'
        'sitionE',
        pos.value,
    )

  @overload(QInternal.DockPosition, QLayoutItem)
  @overload(QInternal.DockPosition, NoneType)
  def insertItem(
      self,
      pos: QInternal.DockPosition,
      item: Optional[QLayoutItem],
  ) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayout::insertItem(QInternal::DockPosition
    pos, QLayoutItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbararealayout.html#insertItem

    Parameters
    ----------

    pos : QInternal.DockPosition
      Passed on as its number.

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarAreaLayout::insertItem(QInternal::DockPosition pos,
    #      QLayoutItem *item)
    self.uglySide.call(
        'ritual_ZN18QToolBarAreaLayout10insertItemEN9QInternal12DockPositio'
        'nEP11QLayoutItem',
        pos.value, self._addressOf(item, 'QLayoutItem'),
    )

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
    Calls Qt's 'void QToolBarAreaLayout::insertItem(QToolBar *before,
    QLayoutItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbararealayout.html#insertItem

    Parameters
    ----------

    before : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarAreaLayout::insertItem(QToolBar *before, QLayoutItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN18QToolBarAreaLayout10insertItemEP8QToolBarP11QLayoutItem',
        self._addressOf(before), self._addressOf(item, 'QLayoutItem'),
    )

  @overload(QStyleOptionToolBar, QToolBar)
  @overload(QStyleOptionToolBar, NoneType)
  @overload(NoneType, QToolBar)
  @overload(NoneType, NoneType)
  def getStyleOptionInfo(
      self,
      option: Optional[QStyleOptionToolBar],
      toolBar: Optional[QToolBar],
  ) -> None:
    """
    Calls Qt's 'void
    QToolBarAreaLayout::getStyleOptionInfo(QStyleOptionToolBar *option,
    QToolBar *toolBar) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbararealayout.html#getStyleOptionInfo

    Parameters
    ----------

    option : Optional[QStyleOptionToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    toolBar : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarAreaLayout::getStyleOptionInfo(QStyleOptionToolBar
    #      *option, QToolBar *toolBar) const
    self.uglySide.call(
        'ritual_ZNK18QToolBarAreaLayout18getStyleOptionInfoEP19QStyleOption'
        'ToolBarP8QToolBar',
        self._addressOf(option), self._addressOf(toolBar),
    )

  @overload(QLayoutItem)
  @overload(NoneType)
  def remove(self, item: Optional[QLayoutItem]) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayout::remove(QLayoutItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbararealayout.html#remove

    Parameters
    ----------

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarAreaLayout::remove(QLayoutItem *item)
    self.uglySide.call(
        'ritual_ZN18QToolBarAreaLayout6removeEP11QLayoutItem',
        self._addressOf(item, 'QLayoutItem'),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QToolBarAreaLayout::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbararealayout.html#clear
    """
    #  void QToolBarAreaLayout::clear()
    self.uglySide.call('ritual_ZN18QToolBarAreaLayout5clearEv')

  @staticmethod
  def apply(*__, **_) -> Never:
    """
    Qt's 'void QToolBarAreaLayout::apply(QWidgetAnimator::AnimationRule
    rule)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'qt_mainwindow_layout'.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.apply' has no cute function yet. Qt's 'void "
        "QToolBarAreaLayout::apply(QWidgetAnimator::AnimationRule rule)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'qt_mainwindow_layout'.")

  @staticmethod
  def currentGapIndex(*__, **_) -> Never:
    """
    Qt's 'QList<int> QToolBarAreaLayout::currentGapIndex() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.currentGapIndex' has no cute function yet. "
        "Qt's 'QList<int> QToolBarAreaLayout::currentGapIndex() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def findToolBar(*__, **_) -> Never:
    """
    Qt's 'std::optional<QInternal::DockPosition>
    QToolBarAreaLayout::findToolBar(const QToolBar *toolBar) const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.findToolBar' has no cute function yet. Qt's "
        "'std::optional<QInternal::DockPosition> "
        "QToolBarAreaLayout::findToolBar(const QToolBar *toolBar) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def fitLayout(*__, **_) -> Never:
    """
    Qt's 'QRect QToolBarAreaLayout::fitLayout()': leans on
    'QToolBarLayout::staticMetaObject', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.fitLayout' has no cute function yet. Qt's "
        "'QRect QToolBarAreaLayout::fitLayout()': leans on "
        "'QToolBarLayout::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def gapIndex(*__, **_) -> Never:
    """
    Qt's 'QList<int> QToolBarAreaLayout::gapIndex(const QPoint &pos) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.gapIndex' has no cute function yet. Qt's "
        "'QList<int> QToolBarAreaLayout::gapIndex(const QPoint &pos) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def indexOf(*__, **_) -> Never:
    """
    Qt's 'QList<int> QToolBarAreaLayout::indexOf(QWidget *toolBar) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.indexOf' has no cute function yet. Qt's "
        "'QList<int> QToolBarAreaLayout::indexOf(QWidget *toolBar) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def insertGap(*__, **_) -> Never:
    """
    Qt's 'bool QToolBarAreaLayout::insertGap(const QList<int> &path,
    QLayoutItem *item)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.insertGap' has no cute function yet. Qt's "
        "'bool QToolBarAreaLayout::insertGap(const QList<int> &path, "
        "QLayoutItem *item)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def item(*__, **_) -> Never:
    """
    Qt's 'QToolBarAreaLayoutItem *QToolBarAreaLayout::item(const QList<int>
    &path)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.item' has no cute function yet. Qt's "
        "'QToolBarAreaLayoutItem *QToolBarAreaLayout::item(const QList<int> "
        "&path)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def itemAt(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QToolBarAreaLayout::itemAt(int *x, int index) const':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.itemAt' has no cute function yet. Qt's "
        "'QLayoutItem *QToolBarAreaLayout::itemAt(int *x, int index) "
        "const': takes a number to change where it is.")

  @staticmethod
  def itemRect(*__, **_) -> Never:
    """
    Qt's 'QRect QToolBarAreaLayout::itemRect(const QList<int> &path) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.itemRect' has no cute function yet. Qt's "
        "'QRect QToolBarAreaLayout::itemRect(const QList<int> &path) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def moveToolBar(*__, **_) -> Never:
    """
    Qt's 'void QToolBarAreaLayout::moveToolBar(QToolBar *toolbar, int pos)':
    leans on 'QToolBarLayout::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.moveToolBar' has no cute function yet. Qt's "
        "'void QToolBarAreaLayout::moveToolBar(QToolBar *toolbar, int "
        "pos)': leans on 'QToolBarLayout::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def plug(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QToolBarAreaLayout::plug(const QList<int> &path)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.plug' has no cute function yet. Qt's "
        "'QLayoutItem *QToolBarAreaLayout::plug(const QList<int> &path)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def restoreState(*__, **_) -> Never:
    """
    Qt's 'bool QToolBarAreaLayout::restoreState(QDataStream &stream, const
    QList<QToolBar *> &toolBars, uchar tmarker, QInternal::CallMode
    callMode)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name 'StateMarkers';
    did you mean 'QMainWindowLayoutState::StateMarkers'?.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.restoreState' has no cute function yet. Qt's "
        "'bool QToolBarAreaLayout::restoreState(QDataStream &stream, const "
        "QList<QToolBar *> &toolBars, uchar tmarker, QInternal::CallMode "
        "callMode)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'StateMarkers'; did you mean "
        "'QMainWindowLayoutState::StateMarkers'?.")

  @staticmethod
  def saveState(*__, **_) -> Never:
    """
    Qt's 'void QToolBarAreaLayout::saveState(QDataStream &stream) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.saveState' has no cute function yet. Qt's "
        "'void QToolBarAreaLayout::saveState(QDataStream &stream) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def takeAt(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QToolBarAreaLayout::takeAt(int *x, int index)': takes
    a number to change where it is.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.takeAt' has no cute function yet. Qt's "
        "'QLayoutItem *QToolBarAreaLayout::takeAt(int *x, int index)': "
        "takes a number to change where it is.")

  @staticmethod
  def unplug(*__, **_) -> Never:
    """
    Qt's 'QLayoutItem *QToolBarAreaLayout::unplug(const QList<int> &path,
    QToolBarAreaLayout *other)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QToolBarAreaLayout.unplug' has no cute function yet. Qt's "
        "'QLayoutItem *QToolBarAreaLayout::unplug(const QList<int> &path, "
        "QToolBarAreaLayout *other)': takes a type Python has no way to "
        "hand over yet.")

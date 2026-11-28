"""
QToolBarLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtoolbarlayout_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QToolBarLayout to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from . import QLayout, QLayoutItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect, QSize
  from ..QtGui import QAction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QToolBarLayout(QLayout):
  """
  The cute side of Qt's QToolBarLayout: a plain Python object standing in
  front of one C++ QToolBarLayout.

  It is built on the cute 'QLayout', as Qt's QToolBarLayout is built on Qt's
  QLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QToolBarLayout that has a ritual and that Python can
  call so far, 22 names in all: 'metaObject', 'addItem', 'itemAt', 'takeAt',
  'count', 'isEmpty', 'invalidate', 'expandingDirections', 'setGeometry',
  'minimumSize', 'sizeHint', 'indexOf', 'layoutActions', 'expandedSize',
  'setUsePopupMenu', 'checkUsePopupMenu', 'movable',
  'updateMarginAndSpacing', 'hasExpandFlag', 'updateMacBorderMetrics',
  'setExpanded', 'updateGeomArray'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QToolBarLayout::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QToolBarLayout::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QToolBarLayout::~QToolBarLayout()': the destructor: Python never
    removes a C++ QToolBarLayout.

  What has no ritual
  ------------------

  6 of the 31 functions Qt declares: 2 not a gap; 2 leans on 'QToolBarLayout;
  2 leans on 'vtable for QToolBarSeparator', which Qt's source does not mark
  for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QToolBarLayout is created at the first use, not by
    'QToolBarLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QToolBarLayout.
  - Qt tells when it has removed the C++ QToolBarLayout. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QToolBarLayout that has no cute function yet,
    '__init__', 'createItem', 'insertAction', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QToolBarLayout'

  #  A C++ QToolBarLayout Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QToolBarLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QToolBarLayout::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QToolBarLayout::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QToolBarLayout10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def itemAt(self, index: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QToolBarLayout::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QToolBarLayout::itemAt(int index) const
    ritual = 'ritual_ZNK14QToolBarLayout6itemAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QToolBarLayout6itemAtEi'
    address = self.uglySide.call(ritual, index)
    return QLayoutItem._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QToolBarLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#count
    """
    #  int QToolBarLayout::count() const
    ritual = 'ritual_ZNK14QToolBarLayout5countEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QToolBarLayout5countEv'
    return self.uglySide.call(ritual)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QToolBarLayout::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#isEmpty
    """
    #  bool QToolBarLayout::isEmpty() const
    ritual = 'ritual_ZNK14QToolBarLayout7isEmptyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QToolBarLayout7isEmptyEv'
    return self.uglySide.call(ritual)

  def expandingDirections(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QToolBarLayout::expandingDirections()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarlayout.html#expandingDirections

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QToolBarLayout::expandingDirections() const
    ritual = 'ritual_ZNK14QToolBarLayout19expandingDirectionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QToolBarLayout19expandingDirectionsEv'
    return Qt.Orientations(self.uglySide.call(ritual))

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QToolBarLayout::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBarLayout::minimumSize() const
    ritual = 'ritual_ZNK14QToolBarLayout11minimumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QToolBarLayout11minimumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QToolBarLayout::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBarLayout::sizeHint() const
    ritual = 'ritual_ZNK14QToolBarLayout8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QToolBarLayout8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QAction)
  @overload(NoneType)
  def indexOf(self, action: Optional[QAction]) -> int:
    """
    Calls Qt's 'int QToolBarLayout::indexOf(const QAction *action) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#indexOf

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QToolBarLayout::indexOf(const QAction *action) const
    return self.uglySide.call(
        'ritual_ZNK14QToolBarLayout7indexOfEPK7QAction',
        self._addressOf(action),
    )

  @overload(QSize)
  def expandedSize(self, size: QSize) -> QSize:
    """
    Calls Qt's 'QSize QToolBarLayout::expandedSize(const QSize &size) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#expandedSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBarLayout::expandedSize(const QSize &size) const
    address = self.uglySide.call(
        'ritual_ZNK14QToolBarLayout12expandedSizeERK5QSize',
        self._valueOf(size),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def movable(self) -> bool:
    """
    Calls Qt's 'bool QToolBarLayout::movable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#movable
    """
    #  bool QToolBarLayout::movable() const
    return self.uglySide.call('ritual_ZNK14QToolBarLayout7movableEv')

  def hasExpandFlag(self) -> bool:
    """
    Calls Qt's 'bool QToolBarLayout::hasExpandFlag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#hasExpandFlag
    """
    #  bool QToolBarLayout::hasExpandFlag() const
    return self.uglySide.call('ritual_ZNK14QToolBarLayout13hasExpandFlagEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setGeometry(self, r: QRect) -> None:
    """
    Calls Qt's 'void QToolBarLayout::setGeometry(const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#setGeometry

    Parameters
    ----------

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QToolBarLayout::setGeometry(const QRect &r)
    ritual = 'ritual_ZN14QToolBarLayout11setGeometryERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QToolBarLayout11setGeometryERK5QRect'
    self.uglySide.call(ritual, self._valueOf(r))

  @overload(bool)
  def setUsePopupMenu(self, set: bool) -> None:
    """
    Calls Qt's 'void QToolBarLayout::setUsePopupMenu(bool set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarlayout.html#setUsePopupMenu

    Parameters
    ----------

    set : bool
      Passed on as it is.
    """
    #  void QToolBarLayout::setUsePopupMenu(bool set)
    self.uglySide.call('ritual_ZN14QToolBarLayout15setUsePopupMenuEb', set)

  @overload(bool)
  def setExpanded(self, b: bool) -> None:
    """
    Calls Qt's 'void QToolBarLayout::setExpanded(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#setExpanded

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QToolBarLayout::setExpanded(bool b)
    self.uglySide.call('ritual_ZN14QToolBarLayout11setExpandedEb', b)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QToolBarLayout::QToolBarLayout(QWidget *parent)': leans on
    'QToolBarLayout::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QToolBarLayout.__init__' has no cute function yet. Qt's "
        "'QToolBarLayout::QToolBarLayout(QWidget *parent)': leans on "
        "'QToolBarLayout::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QLayoutItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QLayoutItem]) -> None:
    """
    Calls Qt's 'void QToolBarLayout::addItem(QLayoutItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#addItem

    Parameters
    ----------

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBarLayout::addItem(QLayoutItem *item)
    ritual = 'ritual_ZN14QToolBarLayout7addItemEP11QLayoutItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QToolBarLayout7addItemEP11QLayoutItem'
    self.uglySide.call(ritual, self._addressOf(item, 'QLayoutItem'))

  @overload(int)
  def takeAt(self, index: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QToolBarLayout::takeAt(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#takeAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QToolBarLayout::takeAt(int index)
    ritual = 'ritual_ZN14QToolBarLayout6takeAtEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QToolBarLayout6takeAtEi'
    address = self.uglySide.call(ritual, index)
    return QLayoutItem._cuteAt(address)

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QToolBarLayout::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#invalidate
    """
    #  void QToolBarLayout::invalidate()
    ritual = 'ritual_ZN14QToolBarLayout10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QToolBarLayout10invalidateEv'
    self.uglySide.call(ritual)

  @overload(QSize)
  def layoutActions(self, size: QSize) -> bool:
    """
    Calls Qt's 'bool QToolBarLayout::layoutActions(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbarlayout.html#layoutActions

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  bool QToolBarLayout::layoutActions(const QSize &size)
    return self.uglySide.call(
        'ritual_ZN14QToolBarLayout13layoutActionsERK5QSize',
        self._valueOf(size),
    )

  def checkUsePopupMenu(self) -> None:
    """
    Calls Qt's 'void QToolBarLayout::checkUsePopupMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarlayout.html#checkUsePopupMenu
    """
    #  void QToolBarLayout::checkUsePopupMenu()
    self.uglySide.call('ritual_ZN14QToolBarLayout17checkUsePopupMenuEv')

  def updateMarginAndSpacing(self) -> None:
    """
    Calls Qt's 'void QToolBarLayout::updateMarginAndSpacing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarlayout.html#updateMarginAndSpacing
    """
    #  void QToolBarLayout::updateMarginAndSpacing()
    self.uglySide.call('ritual_ZN14QToolBarLayout22updateMarginAndSpacingEv')

  def updateMacBorderMetrics(self) -> None:
    """
    Calls Qt's 'void QToolBarLayout::updateMacBorderMetrics()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarlayout.html#updateMacBorderMetrics
    """
    #  void QToolBarLayout::updateMacBorderMetrics()
    self.uglySide.call('ritual_ZN14QToolBarLayout22updateMacBorderMetricsEv')

  def updateGeomArray(self) -> None:
    """
    Calls Qt's 'void QToolBarLayout::updateGeomArray() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbarlayout.html#updateGeomArray
    """
    #  void QToolBarLayout::updateGeomArray() const
    self.uglySide.call('ritual_ZNK14QToolBarLayout15updateGeomArrayEv')

  @staticmethod
  def createItem(*__, **_) -> Never:
    """
    Qt's 'QToolBarItem *QToolBarLayout::createItem(QAction *action)': leans
    on 'vtable for QToolBarSeparator', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QToolBarLayout.createItem' has no cute function yet. Qt's "
        "'QToolBarItem *QToolBarLayout::createItem(QAction *action)': leans "
        "on 'vtable for QToolBarSeparator', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def insertAction(*__, **_) -> Never:
    """
    Qt's 'void QToolBarLayout::insertAction(int index, QAction *action)':
    leans on 'vtable for QToolBarSeparator', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QToolBarLayout.insertAction' has no cute function yet. Qt's 'void "
        "QToolBarLayout::insertAction(int index, QAction *action)': leans "
        "on 'vtable for QToolBarSeparator', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

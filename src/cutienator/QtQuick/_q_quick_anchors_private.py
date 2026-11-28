"""
QQuickAnchorsPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanchors_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickAnchorsPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF, QSizeF
  from . import QQuickAnchors, QQuickGeometryChange, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QQuickAnchors = WAIT['QQuickAnchors']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnchorsPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickAnchorsPrivate: a plain Python object standing
  in front of one C++ QQuickAnchorsPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQuickAnchorsPrivate is
  built on Qt's QObjectPrivate, and has everything that class has. Qt's
  QQuickAnchorsPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickAnchorsPrivate> as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QQuickAnchorsPrivate that has a ritual and that
  Python can call so far, 16 names in all: 'q_func', 'clearItem',
  'addDepend', 'remDepend', 'isItemComplete', 'setItemHeight',
  'setItemWidth', 'setItemX', 'setItemY', 'setItemPos', 'setItemSize',
  'itemGeometryChanged', 'anchorPrivate', 'checkHValid', 'checkVValid',
  'get'. None can be made from Python: one comes out of a function of another
  class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickAnchors *QQuickAnchorsPrivate::q_func() const': takes
    in Python what 'QQuickAnchors *QQuickAnchorsPrivate::q_func()' takes.

  What has no ritual
  ------------------

  13 of the 30 functions Qt declares: 8 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 leans on
  'QQuickAnchorsPrivate; 1 cannot be called and cannot be called through the
  meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickAnchorsPrivate is created at the first use, not by
    'QQuickAnchorsPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnchorsPrivate.
  - Each name of Qt's QQuickAnchorsPrivate that has no cute function yet,
    '__init__', 'calcStretch', 'calculateDependency', 'centerInChanged',
    'checkHAnchorValid', 'checkVAnchorValid', 'fillChanged', 'isMirrored',
    'update', 'updateHorizontalAnchors', 'updateMe', 'updateOnComplete',
    'updateVerticalAnchors', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickAnchors)
  @overload(NoneType)
  def get(o: Optional[QQuickAnchors]) -> Optional[QQuickAnchorsPrivate]:
    """
    Calls Qt's 'QQuickAnchorsPrivate *QQuickAnchorsPrivate::get(QQuickAnchors
    *o)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorsprivate.html#get

    Parameters
    ----------

    o : Optional[QQuickAnchors]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickAnchorsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnchorsPrivate *QQuickAnchorsPrivate::get(QQuickAnchors *o)
    address = Rituals.call(
        'ritual_ZN20QQuickAnchorsPrivate3getEP13QQuickAnchors',
        CuteMixin._addressOf(o),
    )
    return QQuickAnchorsPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnchorsPrivate'

  #  A C++ QQuickAnchorsPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnchorsPrivate'

  #  The functions Qt calls itself that QQuickAnchorsPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN20QQuickAnchorsPrivate19itemGeometryChangedEP10QQuickItem20Q'
           'QuickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'anchorPrivate': (
          ('_ZN20QQuickAnchorsPrivate13anchorPrivateEv',
           ('address', 'address', 'QtQuick:QQuickAnchorsPrivate'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isItemComplete(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnchorsPrivate::isItemComplete() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorsprivate.html#isItemComplete
    """
    #  bool QQuickAnchorsPrivate::isItemComplete() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAnchorsPrivate14isItemCompleteEv',
    )

  def checkHValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnchorsPrivate::checkHValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorsprivate.html#checkHValid
    """
    #  bool QQuickAnchorsPrivate::checkHValid() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAnchorsPrivate11checkHValidEv',
    )

  def checkVValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnchorsPrivate::checkVValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorsprivate.html#checkVValid
    """
    #  bool QQuickAnchorsPrivate::checkVValid() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAnchorsPrivate11checkVValidEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setItemHeight(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickAnchorsPrivate::setItemHeight(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorsprivate.html#setItemHeight

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickAnchorsPrivate::setItemHeight(qreal a0)
    self.uglySide.call(
        'ritual_ZN20QQuickAnchorsPrivate13setItemHeightEd', a0,
    )

  @overload(float)
  def setItemWidth(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickAnchorsPrivate::setItemWidth(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorsprivate.html#setItemWidth

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickAnchorsPrivate::setItemWidth(qreal a0)
    self.uglySide.call('ritual_ZN20QQuickAnchorsPrivate12setItemWidthEd', a0)

  @overload(float)
  def setItemX(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickAnchorsPrivate::setItemX(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorsprivate.html#setItemX

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickAnchorsPrivate::setItemX(qreal a0)
    self.uglySide.call('ritual_ZN20QQuickAnchorsPrivate8setItemXEd', a0)

  @overload(float)
  def setItemY(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickAnchorsPrivate::setItemY(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorsprivate.html#setItemY

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickAnchorsPrivate::setItemY(qreal a0)
    self.uglySide.call('ritual_ZN20QQuickAnchorsPrivate8setItemYEd', a0)

  @overload(QPointF)
  def setItemPos(self, a0: QPointF) -> None:
    """
    Calls Qt's 'void QQuickAnchorsPrivate::setItemPos(const QPointF &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorsprivate.html#setItemPos

    Parameters
    ----------

    a0 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickAnchorsPrivate::setItemPos(const QPointF &a0)
    self.uglySide.call(
        'ritual_ZN20QQuickAnchorsPrivate10setItemPosERK7QPointF',
        self._valueOf(a0, 'QPointF'),
    )

  @overload(QSizeF)
  def setItemSize(self, a0: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickAnchorsPrivate::setItemSize(const QSizeF &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorsprivate.html#setItemSize

    Parameters
    ----------

    a0 : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickAnchorsPrivate::setItemSize(const QSizeF &a0)
    self.uglySide.call(
        'ritual_ZN20QQuickAnchorsPrivate11setItemSizeERK6QSizeF',
        self._valueOf(a0),
    )

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
    Qt's 'QQuickAnchorsPrivate::QQuickAnchorsPrivate(QQuickItem *i)': leans
    on 'QQuickAnchorsPrivate::fillChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickAnchorsPrivate.__init__' has no cute function yet. Qt's "
        "'QQuickAnchorsPrivate::QQuickAnchorsPrivate(QQuickItem *i)': leans "
        "on 'QQuickAnchorsPrivate::fillChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  def q_func(self) -> Optional[QQuickAnchors]:
    """
    Calls Qt's 'QQuickAnchors *QQuickAnchorsPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorsprivate.html#q_func

    Returns
    -------

    Optional[QQuickAnchors]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnchors *QQuickAnchorsPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QQuickAnchorsPrivate6q_funcEv')
    from . import QQuickAnchors
    return QQuickAnchors._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  def clearItem(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAnchorsPrivate::clearItem(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorsprivate.html#clearItem

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnchorsPrivate::clearItem(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN20QQuickAnchorsPrivate9clearItemEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def addDepend(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAnchorsPrivate::addDepend(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorsprivate.html#addDepend

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnchorsPrivate::addDepend(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN20QQuickAnchorsPrivate9addDependEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def remDepend(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAnchorsPrivate::remDepend(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorsprivate.html#remDepend

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnchorsPrivate::remDepend(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN20QQuickAnchorsPrivate9remDependEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      a0: Optional[QQuickItem],
      a1: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickAnchorsPrivate::itemGeometryChanged(QQuickItem
    *a0, QQuickGeometryChange a1, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorsprivate.html#itemGeometryChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    a2 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickAnchorsPrivate::itemGeometryChanged(QQuickItem *a0,
    #      QQuickGeometryChange a1, const QRectF &a2)
    self.uglySide.call(
        'ritual_ZN20QQuickAnchorsPrivate19itemGeometryChangedEP10QQuickItem'
        '20QQuickGeometryChangeRK6QRectF',
        self._addressOf(a0), self._valueOf(a1), self._valueOf(a2),
    )

  def anchorPrivate(self) -> Optional[QQuickAnchorsPrivate]:
    """
    Calls Qt's 'QQuickAnchorsPrivate *QQuickAnchorsPrivate::anchorPrivate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorsprivate.html#anchorPrivate

    Returns
    -------

    Optional[QQuickAnchorsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnchorsPrivate *QQuickAnchorsPrivate::anchorPrivate()
    ritual = 'ritual_ZN20QQuickAnchorsPrivate13anchorPrivateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickAnchorsPrivate13anchorPrivateEv'
    address = self.uglySide.call(ritual)
    return QQuickAnchorsPrivate._cuteAt(address)

  @staticmethod
  def calcStretch(*__, **_) -> Never:
    """
    Qt's 'bool QQuickAnchorsPrivate::calcStretch(QQuickItem *edge1Item,
    QQuickAnchors::Anchor edge1Line, QQuickItem *edge2Item,
    QQuickAnchors::Anchor edge2Line, qreal offset1, qreal offset2,
    QQuickAnchors::Anchor line, qreal &stretch) const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'readParentItem'.
    """
    raise NotImplementedError(
        "'QQuickAnchorsPrivate.calcStretch' has no cute function yet. Qt's "
        "'bool QQuickAnchorsPrivate::calcStretch(QQuickItem *edge1Item, "
        "QQuickAnchors::Anchor edge1Line, QQuickItem *edge2Item, "
        "QQuickAnchors::Anchor edge2Line, qreal offset1, qreal offset2, "
        "QQuickAnchors::Anchor line, qreal &stretch) const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'readParentItem'."
    )

  @staticmethod
  def calculateDependency(*__, **_) -> Never:
    """
    Qt's 'QQuickGeometryChange
    QQuickAnchorsPrivate::calculateDependency(QQuickItem *a0) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'readParentItem'.
    """
    raise NotImplementedError(
        "'QQuickAnchorsPrivate.calculateDependency' has no cute function "
        "yet. Qt's 'QQuickGeometryChange "
        "QQuickAnchorsPrivate::calculateDependency(QQuickItem *a0) const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'readParentItem'.")

  @staticmethod
  def centerInChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnchorsPrivate::centerInChanged()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'readParentItem'.
    """
    raise NotImplementedError(
        "'QQuickAnchorsPrivate.centerInChanged' has no cute function yet. "
        "Qt's 'void QQuickAnchorsPrivate::centerInChanged()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'readParentItem'."
    )

  @staticmethod
  def checkHAnchorValid(*__, **_) -> Never:
    """
    Qt's 'bool QQuickAnchorsPrivate::checkHAnchorValid(QQuickAnchorLine
    anchor) const': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'readParentItem'.
    """
    raise NotImplementedError(
        "'QQuickAnchorsPrivate.checkHAnchorValid' has no cute function yet. "
        "Qt's 'bool "
        "QQuickAnchorsPrivate::checkHAnchorValid(QQuickAnchorLine anchor) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'readParentItem'.")

  @staticmethod
  def checkVAnchorValid(*__, **_) -> Never:
    """
    Qt's 'bool QQuickAnchorsPrivate::checkVAnchorValid(QQuickAnchorLine
    anchor) const': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'readParentItem'.
    """
    raise NotImplementedError(
        "'QQuickAnchorsPrivate.checkVAnchorValid' has no cute function yet. "
        "Qt's 'bool "
        "QQuickAnchorsPrivate::checkVAnchorValid(QQuickAnchorLine anchor) "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'readParentItem'.")

  @staticmethod
  def fillChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnchorsPrivate::fillChanged()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'readParentItem'.
    """
    raise NotImplementedError(
        "'QQuickAnchorsPrivate.fillChanged' has no cute function yet. Qt's "
        "'void QQuickAnchorsPrivate::fillChanged()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'readParentItem'.")

  @staticmethod
  def isMirrored(*__, **_) -> Never:
    """
    Qt's 'bool QQuickAnchorsPrivate::isMirrored() const': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickAnchorsPrivate.isMirrored' has no cute function yet. Qt's "
        "'bool QQuickAnchorsPrivate::isMirrored() const': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

  @staticmethod
  def update(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnchorsPrivate::update()': leans on
    'QQuickAnchorsPrivate::fillChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickAnchorsPrivate.update' has no cute function yet. Qt's 'void "
        "QQuickAnchorsPrivate::update()': leans on "
        "'QQuickAnchorsPrivate::fillChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def updateHorizontalAnchors(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnchorsPrivate::updateHorizontalAnchors()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'reverseAnchorLine'.
    """
    raise NotImplementedError(
        "'QQuickAnchorsPrivate.updateHorizontalAnchors' has no cute "
        "function yet. Qt's 'void "
        "QQuickAnchorsPrivate::updateHorizontalAnchors()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'reverseAnchorLine'.")

  @staticmethod
  def updateMe(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnchorsPrivate::updateMe()': leans on
    'QQuickAnchorsPrivate::fillChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickAnchorsPrivate.updateMe' has no cute function yet. Qt's "
        "'void QQuickAnchorsPrivate::updateMe()': leans on "
        "'QQuickAnchorsPrivate::fillChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def updateOnComplete(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnchorsPrivate::updateOnComplete()': leans on
    'QQuickAnchorsPrivate::fillChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickAnchorsPrivate.updateOnComplete' has no cute function yet. "
        "Qt's 'void QQuickAnchorsPrivate::updateOnComplete()': leans on "
        "'QQuickAnchorsPrivate::fillChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def updateVerticalAnchors(*__, **_) -> Never:
    """
    Qt's 'void QQuickAnchorsPrivate::updateVerticalAnchors()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'readParentItem'.
    """
    raise NotImplementedError(
        "'QQuickAnchorsPrivate.updateVerticalAnchors' has no cute function "
        "yet. Qt's 'void QQuickAnchorsPrivate::updateVerticalAnchors()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'readParentItem'.")

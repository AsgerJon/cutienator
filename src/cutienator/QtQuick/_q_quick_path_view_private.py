"""
QQuickPathViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpathview_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPathViewPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from . import QQuickItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtGui import QInputEvent, QMouseEvent
  from . import QQuickGeometryChange, QQuickItem, QQuickPathView
  from . import QQuickPathViewAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QInputEvent = WAIT['QInputEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPathViewPrivate(QQuickItemPrivate):
  """
  The cute side of Qt's QQuickPathViewPrivate: a plain Python object standing
  in front of one C++ QQuickPathViewPrivate.

  It is built on the cute 'QQuickItemPrivate', as Qt's QQuickPathViewPrivate
  is built on Qt's QQuickItemPrivate, and has everything that class has. Qt's
  QQuickPathViewPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickPathViewPrivate> as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QQuickPathViewPrivate that has a ritual and that
  Python can call so far, 20 names in all: 'q_func', 'init',
  'itemGeometryChanged', 'itemDestroyed', 'scheduleLayout', 'getItem',
  'attached', 'updateMappedRange', 'positionOfIndex', 'isInBound',
  'createHighlight', 'isValid', 'handleMousePressEvent', 'calcCurrentIndex',
  'fixOffset', 'setOffset', 'setAdjustedOffset', 'snapToIndex',
  'computeCurrentTime', 'setDragging'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickPathView *QQuickPathViewPrivate::q_func() const': takes
    in Python what 'QQuickPathView *QQuickPathViewPrivate::q_func()' takes.
  - Qt's 'void QQuickPathViewPrivate::fixOffsetCallback(void *a0)': names
    'void', which has no cute class yet.
  - Qt's 'QPointF QQuickPathViewPrivate::pointNear(const QPointF &point,
    qreal *nearPercent) const': takes a number to change where it is.

  What has no ritual
  ------------------

  15 of the 38 functions Qt declares: 11 leans on 'QQuickPathViewAttached; 3
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file; 1 leans on 'QQuickPathViewPrivate.

  What to expect
  --------------

  - The C++ QQuickPathViewPrivate is created at the first use, not by
    'QQuickPathViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathViewPrivate.
  - Each name of Qt's QQuickPathViewPrivate that has no cute function yet,
    '__init__', 'addVelocitySample', 'attachedType', 'calcVelocity', 'clear',
    'createCurrentItem', 'fixOffsetCallback', 'handleMouseMoveEvent',
    'handleMouseReleaseEvent', 'pointNear', 'regenerate',
    'releaseCurrentItem', 'releaseItem', 'setHighlightPosition',
    'updateCurrent', 'updateHighlight', 'updateItem', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickPathViewPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class MovementReason(CuteNum):
    """
    The enum 'QQuickPathViewPrivate::MovementReason' of Qt, with the 3 names
    Qt gives in it.
    """

    Other = Kee[int](0)
    SetIndex = Kee[int](1)
    Mouse = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathViewPrivate'

  #  A C++ QQuickPathViewPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPathViewPrivate'

  #  The functions Qt calls itself that QQuickPathViewPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN21QQuickPathViewPrivate19itemGeometryChangedEP10QQuickItem20'
           'QQuickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'itemDestroyed': (
          ('_ZN21QQuickPathViewPrivate13itemDestroyedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def positionOfIndex(self, index: float) -> float:
    """
    Calls Qt's 'qreal QQuickPathViewPrivate::positionOfIndex(qreal index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#positionOfIndex

    Parameters
    ----------

    index : float
      Passed on as it is.
    """
    #  qreal QQuickPathViewPrivate::positionOfIndex(qreal index) const
    return self.uglySide.call(
        'ritual_ZNK21QQuickPathViewPrivate15positionOfIndexEd', index,
    )

  @overload(float, float, float)
  @overload(float, float, float, bool)
  def isInBound(
      self,
      position: float,
      lower: float,
      upper: float,
      emptyRangeCheck: bool = True,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPathViewPrivate::isInBound(qreal position, qreal
    lower, qreal upper, bool emptyRangeCheck) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#isInBound

    Parameters
    ----------

    position : float
      Passed on as it is.

    lower : float
      Passed on as it is.

    upper : float
      Passed on as it is.

    emptyRangeCheck : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  bool QQuickPathViewPrivate::isInBound(qreal position, qreal lower,
    #      qreal upper, bool emptyRangeCheck) const
    return self.uglySide.call(
        'ritual_ZNK21QQuickPathViewPrivate9isInBoundEdddb',
        position, lower, upper, emptyRangeCheck,
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathViewPrivate::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathviewprivate.html#isValid
    """
    #  bool QQuickPathViewPrivate::isValid() const
    return self.uglySide.call('ritual_ZNK21QQuickPathViewPrivate7isValidEv')

  @overload(QInputEvent)
  @overload(NoneType)
  def computeCurrentTime(self, event: Optional[QInputEvent]) -> int:
    """
    Calls Qt's 'qint64 QQuickPathViewPrivate::computeCurrentTime(QInputEvent
    *event) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#computeCurrentTime

    Parameters
    ----------

    event : Optional[QInputEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qint64 QQuickPathViewPrivate::computeCurrentTime(QInputEvent *event)
    #      const
    return self.uglySide.call(
        'ritual_ZNK21QQuickPathViewPrivate18computeCurrentTimeEP11QInputEve'
        'nt',
        self._addressOf(event),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickPathViewPrivate::setOffset(qreal offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#setOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickPathViewPrivate::setOffset(qreal offset)
    self.uglySide.call(
        'ritual_ZN21QQuickPathViewPrivate9setOffsetEd', offset,
    )

  @overload(float)
  def setAdjustedOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickPathViewPrivate::setAdjustedOffset(qreal offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#setAdjustedOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickPathViewPrivate::setAdjustedOffset(qreal offset)
    self.uglySide.call(
        'ritual_ZN21QQuickPathViewPrivate17setAdjustedOffsetEd', offset,
    )

  @overload(bool)
  def setDragging(self, d: bool) -> None:
    """
    Calls Qt's 'void QQuickPathViewPrivate::setDragging(bool d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#setDragging

    Parameters
    ----------

    d : bool
      Passed on as it is.
    """
    #  void QQuickPathViewPrivate::setDragging(bool d)
    self.uglySide.call('ritual_ZN21QQuickPathViewPrivate11setDraggingEb', d)

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
    Qt's 'QQuickPathViewPrivate::QQuickPathViewPrivate()': leans on
    'QQuickPathViewAttached::pathChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.__init__' has no cute function yet. Qt's "
        "'QQuickPathViewPrivate::QQuickPathViewPrivate()': leans on "
        "'QQuickPathViewAttached::pathChanged()', which Qt's source does "
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

  def q_func(self) -> Optional[QQuickPathView]:
    """
    Calls Qt's 'QQuickPathView *QQuickPathViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathviewprivate.html#q_func

    Returns
    -------

    Optional[QQuickPathView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPathView *QQuickPathViewPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QQuickPathViewPrivate6q_funcEv')
    from . import QQuickPathView
    return QQuickPathView._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QQuickPathViewPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathviewprivate.html#init
    """
    #  void QQuickPathViewPrivate::init()
    self.uglySide.call('ritual_ZN21QQuickPathViewPrivate4initEv')

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickPathViewPrivate::itemGeometryChanged(QQuickItem
    *item, QQuickGeometryChange change, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    a2 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickPathViewPrivate::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &a2)
    ritual = (
        'ritual_ZN21QQuickPathViewPrivate19itemGeometryChangedEP10QQuickIte'
        'm20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickPathViewPrivate19itemGeometryChangedEP10QQu'
          'ickItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(a2),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickPathViewPrivate::itemDestroyed(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathViewPrivate::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN21QQuickPathViewPrivate13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickPathViewPrivate13itemDestroyedEP10QQuickIte'
          'm')
    self.uglySide.call(ritual, self._addressOf(item))

  def scheduleLayout(self) -> None:
    """
    Calls Qt's 'void QQuickPathViewPrivate::scheduleLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#scheduleLayout
    """
    #  void QQuickPathViewPrivate::scheduleLayout()
    self.uglySide.call('ritual_ZN21QQuickPathViewPrivate14scheduleLayoutEv')

  @overload(int)
  @overload(int, float)
  @overload(int, float, bool)
  def getItem(
      self,
      modelIndex: int,
      z: float = 0.0,
      async_: bool = False,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickPathViewPrivate::getItem(int modelIndex,
    qreal z, bool async)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathviewprivate.html#getItem

    Parameters
    ----------

    modelIndex : int
      Passed on as it is.

    z : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    async_ : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickPathViewPrivate::getItem(int modelIndex, qreal z,
    #      bool async)
    address = self.uglySide.call(
        'ritual_ZN21QQuickPathViewPrivate7getItemEidb',
        modelIndex, z, async_,
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  @overload(QQuickItem)
  @overload(NoneType)
  def attached(
      self,
      item: Optional[QQuickItem],
  ) -> Optional[QQuickPathViewAttached]:
    """
    Calls Qt's 'QQuickPathViewAttached
    *QQuickPathViewPrivate::attached(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#attached

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickPathViewAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPathViewAttached *QQuickPathViewPrivate::attached(QQuickItem
    #      *item)
    address = self.uglySide.call(
        'ritual_ZN21QQuickPathViewPrivate8attachedEP10QQuickItem',
        self._addressOf(item),
    )
    from . import QQuickPathViewAttached
    return QQuickPathViewAttached._cuteAt(address)

  def updateMappedRange(self) -> None:
    """
    Calls Qt's 'void QQuickPathViewPrivate::updateMappedRange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#updateMappedRange
    """
    #  void QQuickPathViewPrivate::updateMappedRange()
    self.uglySide.call(
        'ritual_ZN21QQuickPathViewPrivate17updateMappedRangeEv',
    )

  def createHighlight(self) -> None:
    """
    Calls Qt's 'void QQuickPathViewPrivate::createHighlight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#createHighlight
    """
    #  void QQuickPathViewPrivate::createHighlight()
    self.uglySide.call('ritual_ZN21QQuickPathViewPrivate15createHighlightEv')

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleMousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickPathViewPrivate::handleMousePressEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#handleMousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPathViewPrivate::handleMousePressEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN21QQuickPathViewPrivate21handleMousePressEventEP11QMouseE'
        'vent',
        self._addressOf(event),
    )

  def calcCurrentIndex(self) -> int:
    """
    Calls Qt's 'int QQuickPathViewPrivate::calcCurrentIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#calcCurrentIndex
    """
    #  int QQuickPathViewPrivate::calcCurrentIndex()
    return self.uglySide.call(
        'ritual_ZN21QQuickPathViewPrivate16calcCurrentIndexEv',
    )

  def fixOffset(self) -> None:
    """
    Calls Qt's 'void QQuickPathViewPrivate::fixOffset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#fixOffset
    """
    #  void QQuickPathViewPrivate::fixOffset()
    self.uglySide.call('ritual_ZN21QQuickPathViewPrivate9fixOffsetEv')

  @overload(int, MovementReason)
  def snapToIndex(self, index: int, reason: MovementReason) -> None:
    """
    Calls Qt's 'void QQuickPathViewPrivate::snapToIndex(int index,
    MovementReason reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewprivate.html#snapToIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    reason : MovementReason
      Passed on as its number.
    """
    #  void QQuickPathViewPrivate::snapToIndex(int index, MovementReason
    #      reason)
    self.uglySide.call(
        'ritual_ZN21QQuickPathViewPrivate11snapToIndexEiNS_14MovementReason'
        'E',
        index, reason.value,
    )

  @staticmethod
  def addVelocitySample(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewPrivate::addVelocitySample(qreal v)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'lcPathView'.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.addVelocitySample' has no cute function "
        "yet. Qt's 'void QQuickPathViewPrivate::addVelocitySample(qreal "
        "v)': Qt's library has no name for it, and its code in Qt's source "
        "does not compile apart from its file: use of undeclared identifier "
        "'lcPathView'.")

  @staticmethod
  def attachedType(*__, **_) -> Never:
    """
    Qt's 'QQmlOpenMetaObjectType *QQuickPathViewPrivate::attachedType()':
    leans on 'QQuickPathViewAttached::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.attachedType' has no cute function yet. "
        "Qt's 'QQmlOpenMetaObjectType "
        "*QQuickPathViewPrivate::attachedType()': leans on "
        "'QQuickPathViewAttached::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def calcVelocity(*__, **_) -> Never:
    """
    Qt's 'qreal QQuickPathViewPrivate::calcVelocity() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'lcPathView'.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.calcVelocity' has no cute function yet. "
        "Qt's 'qreal QQuickPathViewPrivate::calcVelocity() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'lcPathView'.")

  @staticmethod
  def clear(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewPrivate::clear()': leans on
    'QQuickPathViewAttached::pathChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.clear' has no cute function yet. Qt's 'void "
        "QQuickPathViewPrivate::clear()': leans on "
        "'QQuickPathViewAttached::pathChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def createCurrentItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewPrivate::createCurrentItem()': leans on
    'QQuickPathViewAttached::pathChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.createCurrentItem' has no cute function "
        "yet. Qt's 'void QQuickPathViewPrivate::createCurrentItem()': leans "
        "on 'QQuickPathViewAttached::pathChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def fixOffsetCallback(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewPrivate::fixOffsetCallback(void *a0)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.fixOffsetCallback' has no cute function "
        "yet. Qt's 'void QQuickPathViewPrivate::fixOffsetCallback(void "
        "*a0)': names 'void', which has no cute class yet.")

  @staticmethod
  def handleMouseMoveEvent(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewPrivate::handleMouseMoveEvent(QMouseEvent
    *event)': leans on 'QQuickPathViewPrivate::addVelocitySample(double)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.handleMouseMoveEvent' has no cute function "
        "yet. Qt's 'void "
        "QQuickPathViewPrivate::handleMouseMoveEvent(QMouseEvent *event)': "
        "leans on 'QQuickPathViewPrivate::addVelocitySample(double)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def handleMouseReleaseEvent(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewPrivate::handleMouseReleaseEvent(QMouseEvent
    *a0)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'lcPathView'.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.handleMouseReleaseEvent' has no cute "
        "function yet. Qt's 'void "
        "QQuickPathViewPrivate::handleMouseReleaseEvent(QMouseEvent *a0)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'lcPathView'.")

  @staticmethod
  def pointNear(*__, **_) -> Never:
    """
    Qt's 'QPointF QQuickPathViewPrivate::pointNear(const QPointF &point,
    qreal *nearPercent) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.pointNear' has no cute function yet. Qt's "
        "'QPointF QQuickPathViewPrivate::pointNear(const QPointF &point, "
        "qreal *nearPercent) const': takes a number to change where it is.")

  @staticmethod
  def regenerate(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewPrivate::regenerate()': leans on
    'QQuickPathViewAttached::pathChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.regenerate' has no cute function yet. Qt's "
        "'void QQuickPathViewPrivate::regenerate()': leans on "
        "'QQuickPathViewAttached::pathChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def releaseCurrentItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewPrivate::releaseCurrentItem()': leans on
    'QQuickPathViewAttached::pathChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.releaseCurrentItem' has no cute function "
        "yet. Qt's 'void QQuickPathViewPrivate::releaseCurrentItem()': "
        "leans on 'QQuickPathViewAttached::pathChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def releaseItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewPrivate::releaseItem(QQuickItem *item)': leans
    on 'QQuickPathViewAttached::pathChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.releaseItem' has no cute function yet. Qt's "
        "'void QQuickPathViewPrivate::releaseItem(QQuickItem *item)': leans "
        "on 'QQuickPathViewAttached::pathChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setHighlightPosition(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewPrivate::setHighlightPosition(qreal pos)': leans
    on 'QQuickPathViewAttached::pathChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.setHighlightPosition' has no cute function "
        "yet. Qt's 'void QQuickPathViewPrivate::setHighlightPosition(qreal "
        "pos)': leans on 'QQuickPathViewAttached::pathChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def updateCurrent(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewPrivate::updateCurrent()': leans on
    'QQuickPathViewAttached::pathChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.updateCurrent' has no cute function yet. "
        "Qt's 'void QQuickPathViewPrivate::updateCurrent()': leans on "
        "'QQuickPathViewAttached::pathChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def updateHighlight(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewPrivate::updateHighlight()': leans on
    'QQuickPathViewAttached::pathChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.updateHighlight' has no cute function yet. "
        "Qt's 'void QQuickPathViewPrivate::updateHighlight()': leans on "
        "'QQuickPathViewAttached::pathChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def updateItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewPrivate::updateItem(QQuickItem *a0, qreal a1)':
    leans on 'QQuickPathViewAttached::pathChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewPrivate.updateItem' has no cute function yet. Qt's "
        "'void QQuickPathViewPrivate::updateItem(QQuickItem *a0, qreal "
        "a1)': leans on 'QQuickPathViewAttached::pathChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

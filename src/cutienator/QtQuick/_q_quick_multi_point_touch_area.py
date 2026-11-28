"""
QQuickMultiPointTouchArea binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickmultipointtoucharea_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickMultiPointTouchArea to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QEventPoint, QMouseEvent, QPointingDevice, QTouchEvent
  from . import QQuickGrabGestureEvent, QQuickTouchPoint, QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QEventPoint = WAIT['QEventPoint']
  QMouseEvent = WAIT['QMouseEvent']
  QPointingDevice = WAIT['QPointingDevice']
  QQuickGrabGestureEvent = WAIT['QQuickGrabGestureEvent']
  QQuickTouchPoint = WAIT['QQuickTouchPoint']
  QSGNode = WAIT['QSGNode']
  QTouchEvent = WAIT['QTouchEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMultiPointTouchArea(QQuickItem):
  """
  The cute side of Qt's QQuickMultiPointTouchArea: a plain Python object
  standing in front of one C++ QQuickMultiPointTouchArea.

  It is built on the cute 'QQuickItem', as Qt's QQuickMultiPointTouchArea is
  built on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMultiPointTouchArea that has a ritual and that
  Python can call so far, 33 names in all: 'metaObject', 'tr',
  'minimumTouchPoints', 'setMinimumTouchPoints', 'maximumTouchPoints',
  'setMaximumTouchPoints', 'mouseEnabled', 'setMouseEnabled', 'pressed',
  'updated', 'released', 'canceled', 'gestureStarted', 'touchUpdated',
  'minimumTouchPointsChanged', 'maximumTouchPointsChanged',
  'mouseEnabledChanged', 'touchEvent', 'childMouseEventFilter',
  'mousePressEvent', 'mouseReleaseEvent', 'mouseMoveEvent',
  'mouseUngrabEvent', 'touchUngrabEvent', 'addTouchPrototype',
  'addTouchPoint', 'clearTouchLists', 'updateTouchPoint', 'sendMouseEvent',
  'shouldFilter', 'grabGesture', 'updatePaintNode', 'ungrab'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMultiPointTouchArea::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickMultiPointTouchArea::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickMultiPointTouchArea::~QQuickMultiPointTouchArea()': the
    destructor: Python never removes a C++ QQuickMultiPointTouchArea.
  - Qt's 'QQmlListProperty<QQuickTouchPoint>
    QQuickMultiPointTouchArea::touchPoints()': gives a type Python has no way
    to take yet.
  - Qt's 'void QQuickMultiPointTouchArea::touchPoint_append(
    QQmlListProperty<QQuickTouchPoint> *list, QQuickTouchPoint *touch)':
    names 'QQmlListProperty<QQuickTouchPoint>', which has no cute class yet.
  - Qt's 'qsizetype QQuickMultiPointTouchArea::touchPoint_count(
    QQmlListProperty<QQuickTouchPoint> *list)': names
    'QQmlListProperty<QQuickTouchPoint>', which has no cute class yet.
  - Qt's 'QQuickTouchPoint *QQuickMultiPointTouchArea::touchPoint_at(
    QQmlListProperty<QQuickTouchPoint> *list, qsizetype index)': names
    'QQmlListProperty<QQuickTouchPoint>', which has no cute class yet.
  - Qt's 'void QQuickMultiPointTouchArea::updateTouchData(QEvent *a0,
    RemapEventPoints remap)': names the enum
    'QQuickMultiPointTouchArea::RemapEventPoints', whose class cannot be
    named here.

  What has no ritual
  ------------------

  6 of the 50 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickMultiPointTouchArea is created at the first use, not by
    'QQuickMultiPointTouchArea(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMultiPointTouchArea.
  - Qt tells when it has removed the C++ QQuickMultiPointTouchArea. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickMultiPointTouchArea that has no cute function
    yet, 'touchPoint_append', 'touchPoint_at', 'touchPoint_count',
    'touchPoints', 'updateTouchData', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickMultiPointTouchArea::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMultiPointTouchArea::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuickMultiPointTouchArea2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMultiPointTouchArea'

  #  A C++ QQuickMultiPointTouchArea Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMultiPointTouchArea'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMultiPointTouchArea::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMultiPointTouchArea::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickMultiPointTouchArea10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def minimumTouchPoints(self) -> int:
    """
    Calls Qt's 'int QQuickMultiPointTouchArea::minimumTouchPoints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#minimumTouchPoints
    """
    #  int QQuickMultiPointTouchArea::minimumTouchPoints() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickMultiPointTouchArea18minimumTouchPointsEv',
    )

  def maximumTouchPoints(self) -> int:
    """
    Calls Qt's 'int QQuickMultiPointTouchArea::maximumTouchPoints() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#maximumTouchPoints
    """
    #  int QQuickMultiPointTouchArea::maximumTouchPoints() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickMultiPointTouchArea18maximumTouchPointsEv',
    )

  def mouseEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickMultiPointTouchArea::mouseEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#mouseEnabled
    """
    #  bool QQuickMultiPointTouchArea::mouseEnabled() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickMultiPointTouchArea12mouseEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setMinimumTouchPoints(self, num: int) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::setMinimumTouchPoints(int
    num)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html

    Parameters
    ----------

    num : int
      Passed on as it is.
    """
    #  void QQuickMultiPointTouchArea::setMinimumTouchPoints(int num)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea21setMinimumTouchPointsEi', num,
    )

  @overload(int)
  def setMaximumTouchPoints(self, num: int) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::setMaximumTouchPoints(int
    num)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html

    Parameters
    ----------

    num : int
      Passed on as it is.
    """
    #  void QQuickMultiPointTouchArea::setMaximumTouchPoints(int num)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea21setMaximumTouchPointsEi', num,
    )

  @overload(bool)
  def setMouseEnabled(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::setMouseEnabled(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#setMouseEnabled

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickMultiPointTouchArea::setMouseEnabled(bool arg)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea15setMouseEnabledEb', arg,
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

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickMultiPointTouchArea::QQuickMultiPointTouchArea(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickMultiPointTouchArea::QQuickMultiPointTouchArea(QQuickItem
    #      *parent)
    self._noteCreation(QQuickMultiPointTouchArea, lambda: Rituals.call(
        'ritual_ZN25QQuickMultiPointTouchAreaC1EP10QQuickItem',
        self._addressOf(parent),
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

  @overload(QList[QObject])
  def pressed(self, touchPoints: QList[QObject]) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::pressed(const QList<QObject
    *> &touchPoints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#pressed

    Parameters
    ----------

    touchPoints : QList[QObject]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickMultiPointTouchArea::pressed(const QList<QObject *>
    #      &touchPoints)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea7pressedERK5QListIP7QObjectE',
        self._valueOf(touchPoints),
    )

  @overload(QList[QObject])
  def updated(self, touchPoints: QList[QObject]) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::updated(const QList<QObject
    *> &touchPoints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#updated

    Parameters
    ----------

    touchPoints : QList[QObject]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickMultiPointTouchArea::updated(const QList<QObject *>
    #      &touchPoints)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea7updatedERK5QListIP7QObjectE',
        self._valueOf(touchPoints),
    )

  @overload(QList[QObject])
  def released(self, touchPoints: QList[QObject]) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::released(const QList<QObject
    *> &touchPoints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#released

    Parameters
    ----------

    touchPoints : QList[QObject]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickMultiPointTouchArea::released(const QList<QObject *>
    #      &touchPoints)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea8releasedERK5QListIP7QObjectE',
        self._valueOf(touchPoints),
    )

  @overload(QList[QObject])
  def canceled(self, touchPoints: QList[QObject]) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::canceled(const QList<QObject
    *> &touchPoints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#canceled

    Parameters
    ----------

    touchPoints : QList[QObject]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickMultiPointTouchArea::canceled(const QList<QObject *>
    #      &touchPoints)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea8canceledERK5QListIP7QObjectE',
        self._valueOf(touchPoints),
    )

  @overload(QQuickGrabGestureEvent)
  @overload(NoneType)
  def gestureStarted(
      self,
      gesture: Optional[QQuickGrabGestureEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickMultiPointTouchArea::gestureStarted(QQuickGrabGestureEvent
    *gesture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#gestureStarted

    Parameters
    ----------

    gesture : Optional[QQuickGrabGestureEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiPointTouchArea::gestureStarted(QQuickGrabGestureEvent
    #      *gesture)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea14gestureStartedEP22QQuickGrab'
        'GestureEvent',
        self._addressOf(gesture),
    )

  @overload(QList[QObject])
  def touchUpdated(self, touchPoints: QList[QObject]) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::touchUpdated(const
    QList<QObject *> &touchPoints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#touchUpdated

    Parameters
    ----------

    touchPoints : QList[QObject]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickMultiPointTouchArea::touchUpdated(const QList<QObject *>
    #      &touchPoints)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea12touchUpdatedERK5QListIP7QObj'
        'ectE',
        self._valueOf(touchPoints),
    )

  def minimumTouchPointsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::minimumTouchPointsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html
    """
    #  void QQuickMultiPointTouchArea::minimumTouchPointsChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea25minimumTouchPointsChangedEv',
    )

  def maximumTouchPointsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::maximumTouchPointsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html
    """
    #  void QQuickMultiPointTouchArea::maximumTouchPointsChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea25maximumTouchPointsChangedEv',
    )

  def mouseEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::mouseEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#mouseEnabledChanged
    """
    #  void QQuickMultiPointTouchArea::mouseEnabledChanged()
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea19mouseEnabledChangedEv',
    )

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, a0: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::touchEvent(QTouchEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#touchEvent

    Parameters
    ----------

    a0 : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiPointTouchArea::touchEvent(QTouchEvent *a0)
    ritual = (
        'ritual_ZN25QQuickMultiPointTouchArea10touchEventEP11QTouchEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickMultiPointTouchArea10touchEventEP11QTouchEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def childMouseEventFilter(
      self,
      receiver: Optional[QQuickItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickMultiPointTouchArea::childMouseEventFilter(QQuickItem *receiver,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html

    Parameters
    ----------

    receiver : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickMultiPointTouchArea::childMouseEventFilter(QQuickItem
    #      *receiver, QEvent *event)
    ritual = (
        'ritual_ZN25QQuickMultiPointTouchArea21childMouseEventFilterEP10QQu'
        'ickItemP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickMultiPointTouchArea21childMouseEventFilterE'
          'P10QQuickItemP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(receiver), self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::mousePressEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiPointTouchArea::mousePressEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN25QQuickMultiPointTouchArea15mousePressEventEP11QMouseEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickMultiPointTouchArea15mousePressEventEP11QMo'
          'useEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::mouseReleaseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiPointTouchArea::mouseReleaseEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN25QQuickMultiPointTouchArea17mouseReleaseEventEP11QMouseE'
        'vent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickMultiPointTouchArea17mouseReleaseEventEP11Q'
          'MouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::mouseMoveEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiPointTouchArea::mouseMoveEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN25QQuickMultiPointTouchArea14mouseMoveEventEP11QMouseEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickMultiPointTouchArea14mouseMoveEventEP11QMou'
          'seEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def mouseUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::mouseUngrabEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#mouseUngrabEvent
    """
    #  void QQuickMultiPointTouchArea::mouseUngrabEvent()
    ritual = 'ritual_ZN25QQuickMultiPointTouchArea16mouseUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QQuickMultiPointTouchArea16mouseUngrabEventEv'
    self.uglySide.call(ritual)

  def touchUngrabEvent(self) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::touchUngrabEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#touchUngrabEvent
    """
    #  void QQuickMultiPointTouchArea::touchUngrabEvent()
    ritual = 'ritual_ZN25QQuickMultiPointTouchArea16touchUngrabEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QQuickMultiPointTouchArea16touchUngrabEventEv'
    self.uglySide.call(ritual)

  @overload(QQuickTouchPoint)
  @overload(NoneType)
  def addTouchPrototype(self, prototype: Optional[QQuickTouchPoint]) -> None:
    """
    Calls Qt's 'void
    QQuickMultiPointTouchArea::addTouchPrototype(QQuickTouchPoint
    *prototype)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#addTouchPrototype

    Parameters
    ----------

    prototype : Optional[QQuickTouchPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiPointTouchArea::addTouchPrototype(QQuickTouchPoint
    #      *prototype)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea17addTouchPrototypeEP16QQuickT'
        'ouchPoint',
        self._addressOf(prototype),
    )

  @overload(QEventPoint)
  @overload(NoneType)
  def addTouchPoint(self, p: Optional[QEventPoint]) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::addTouchPoint(const
    QEventPoint *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#addTouchPoint

    Parameters
    ----------

    p : Optional[QEventPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiPointTouchArea::addTouchPoint(const QEventPoint *p)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea13addTouchPointEPK11QEventPoin'
        't',
        self._addressOf(p),
    )

  @overload(QMouseEvent)
  def addTouchPoint(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::addTouchPoint(const
    QMouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#addTouchPoint

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiPointTouchArea::addTouchPoint(const QMouseEvent *e)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea13addTouchPointEPK11QMouseEven'
        't',
        self._addressOf(e),
    )

  def clearTouchLists(self) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::clearTouchLists()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#clearTouchLists
    """
    #  void QQuickMultiPointTouchArea::clearTouchLists()
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea15clearTouchListsEv',
    )

  @overload(QQuickTouchPoint, QEventPoint)
  @overload(QQuickTouchPoint, NoneType)
  @overload(NoneType, QEventPoint)
  @overload(NoneType, NoneType)
  def updateTouchPoint(
      self,
      a0: Optional[QQuickTouchPoint],
      a1: Optional[QEventPoint],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickMultiPointTouchArea::updateTouchPoint(QQuickTouchPoint *a0, const
    QEventPoint *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#updateTouchPoint

    Parameters
    ----------

    a0 : Optional[QQuickTouchPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEventPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiPointTouchArea::updateTouchPoint(QQuickTouchPoint *a0,
    #      const QEventPoint *a1)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea16updateTouchPointEP16QQuickTo'
        'uchPointPK11QEventPoint',
        self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QQuickTouchPoint, QMouseEvent)
  @overload(NoneType, QMouseEvent)
  def updateTouchPoint(
      self,
      dtp: Optional[QQuickTouchPoint],
      e: Optional[QMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickMultiPointTouchArea::updateTouchPoint(QQuickTouchPoint *dtp, const
    QMouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#updateTouchPoint

    Parameters
    ----------

    dtp : Optional[QQuickTouchPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiPointTouchArea::updateTouchPoint(QQuickTouchPoint
    #      *dtp, const QMouseEvent *e)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea16updateTouchPointEP16QQuickTo'
        'uchPointPK11QMouseEvent',
        self._addressOf(dtp), self._addressOf(e),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def sendMouseEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickMultiPointTouchArea::sendMouseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#sendMouseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickMultiPointTouchArea::sendMouseEvent(QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea14sendMouseEventEP11QMouseEven'
        't',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def shouldFilter(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickMultiPointTouchArea::shouldFilter(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#shouldFilter

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickMultiPointTouchArea::shouldFilter(QEvent *event)
    return self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea12shouldFilterEP6QEvent',
        self._addressOf(event),
    )

  @overload(QPointingDevice)
  @overload(NoneType)
  def grabGesture(self, dev: Optional[QPointingDevice]) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::grabGesture(QPointingDevice
    *dev)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#grabGesture

    Parameters
    ----------

    dev : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMultiPointTouchArea::grabGesture(QPointingDevice *dev)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea11grabGestureEP15QPointingDevi'
        'ce',
        self._addressOf(dev),
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickMultiPointTouchArea::updatePaintNode(QSGNode
    *a0, UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickMultiPointTouchArea::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN25QQuickMultiPointTouchArea15updatePaintNodeEP7QSGNodePN1'
        '0QQuickItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickMultiPointTouchArea15updatePaintNodeEP7QSGN'
          'odePN10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  @overload()
  @overload(bool)
  def ungrab(self, normalRelease: bool = False) -> None:
    """
    Calls Qt's 'void QQuickMultiPointTouchArea::ungrab(bool normalRelease)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmultipointtoucharea.html#ungrab

    Parameters
    ----------

    normalRelease : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickMultiPointTouchArea::ungrab(bool normalRelease)
    self.uglySide.call(
        'ritual_ZN25QQuickMultiPointTouchArea6ungrabEb', normalRelease,
    )

  @staticmethod
  def touchPoint_append(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiPointTouchArea::touchPoint_append(
    QQmlListProperty<QQuickTouchPoint> *list, QQuickTouchPoint *touch)':
    names 'QQmlListProperty<QQuickTouchPoint>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickMultiPointTouchArea.touchPoint_append' has no cute function "
        "yet. Qt's 'void "
        "QQuickMultiPointTouchArea::touchPoint_append(QQmlListProperty<QQuic"
        "kTouchPoint> *list, QQuickTouchPoint *touch)': names "
        "'QQmlListProperty<QQuickTouchPoint>', which has no cute class yet.")

  @staticmethod
  def touchPoint_at(*__, **_) -> Never:
    """
    Qt's 'QQuickTouchPoint *QQuickMultiPointTouchArea::touchPoint_at(
    QQmlListProperty<QQuickTouchPoint> *list, qsizetype index)': names
    'QQmlListProperty<QQuickTouchPoint>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickMultiPointTouchArea.touchPoint_at' has no cute function "
        "yet. Qt's 'QQuickTouchPoint "
        "*QQuickMultiPointTouchArea::touchPoint_at(QQmlListProperty<QQuickTo"
        "uchPoint> *list, qsizetype index)': names "
        "'QQmlListProperty<QQuickTouchPoint>', which has no cute class yet.")

  @staticmethod
  def touchPoint_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQuickMultiPointTouchArea::touchPoint_count(
    QQmlListProperty<QQuickTouchPoint> *list)': names
    'QQmlListProperty<QQuickTouchPoint>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickMultiPointTouchArea.touchPoint_count' has no cute function "
        "yet. Qt's 'qsizetype "
        "QQuickMultiPointTouchArea::touchPoint_count(QQmlListProperty<QQuick"
        "TouchPoint> *list)': names 'QQmlListProperty<QQuickTouchPoint>', "
        "which has no cute class yet.")

  @staticmethod
  def touchPoints(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickTouchPoint>
    QQuickMultiPointTouchArea::touchPoints()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QQuickMultiPointTouchArea.touchPoints' has no cute function yet. "
        "Qt's 'QQmlListProperty<QQuickTouchPoint> "
        "QQuickMultiPointTouchArea::touchPoints()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def updateTouchData(*__, **_) -> Never:
    """
    Qt's 'void QQuickMultiPointTouchArea::updateTouchData(QEvent *a0,
    RemapEventPoints remap)': names the enum
    'QQuickMultiPointTouchArea::RemapEventPoints', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QQuickMultiPointTouchArea.updateTouchData' has no cute function "
        "yet. Qt's 'void QQuickMultiPointTouchArea::updateTouchData(QEvent "
        "*a0, RemapEventPoints remap)': names the enum "
        "'QQuickMultiPointTouchArea::RemapEventPoints', whose class cannot "
        "be named here.")

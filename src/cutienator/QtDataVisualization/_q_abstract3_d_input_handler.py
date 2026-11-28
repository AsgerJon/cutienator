"""
QAbstract3DInputHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qabstract3dinputhandler.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QMouseEvent, QTouchEvent, QWheelEvent
  from . import Q3DScene
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Q3DScene = WAIT['QtDataVisualization:Q3DScene']
  QMouseEvent = WAIT['QMouseEvent']
  QPoint = WAIT['QPoint']
  QTouchEvent = WAIT['QTouchEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstract3DInputHandler(QObject):
  """
  The cute side of Qt's QAbstract3DInputHandler: a plain Python object
  standing in front of one C++ QAbstract3DInputHandler.

  It is built on the cute 'QObject', as Qt's QAbstract3DInputHandler is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstract3DInputHandler that has a ritual and that
  Python can call so far, 21 names in all: 'metaObject', 'tr',
  'mouseDoubleClickEvent', 'touchEvent', 'mousePressEvent',
  'mouseReleaseEvent', 'mouseMoveEvent', 'wheelEvent', 'inputView',
  'setInputView', 'inputPosition', 'setInputPosition', 'scene', 'setScene',
  'positionChanged', 'inputViewChanged', 'sceneChanged', 'setPrevDistance',
  'prevDistance', 'setPreviousInputPos', 'previousInputPos'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstract3DInputHandler::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstract3DInputHandler::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstract3DInputHandler::~QAbstract3DInputHandler()': the
    destructor: Python never removes a C++ QAbstract3DInputHandler.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstract3DInputHandler is created at the first use, not by
    'QAbstract3DInputHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstract3DInputHandler.
  - Qt tells when it has removed the C++ QAbstract3DInputHandler. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAbstract3DInputHandler, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class InputView(CuteNum):
    """
    The enum 'QAbstract3DInputHandler::InputView' of Qt, with the 3 names Qt
    gives in it.
    """

    InputViewNone = Kee[int](0)
    InputViewOnPrimary = Kee[int](1)
    InputViewOnSecondary = Kee[int](2)

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
    Calls Qt's 'QString QAbstract3DInputHandler::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dinputhandler.html#tr

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
    #  QString QAbstract3DInputHandler::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QAbstract3DInputHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstract3DInputHandler'

  #  A C++ QAbstract3DInputHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstract3DInputHandler'

  #  The functions Qt calls itself that QAbstract3DInputHandler is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'mouseDoubleClickEvent': (
          ('_ZN23QAbstract3DInputHandler21mouseDoubleClickEventEP11QMouseEv'
           'ent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
           )),
      ),
      'touchEvent': (
          ('_ZN23QAbstract3DInputHandler10touchEventEP11QTouchEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QTouchEvent'),
           )),
      ),
      'mousePressEvent': (
          ('_ZN23QAbstract3DInputHandler15mousePressEventEP11QMouseEventRK6'
           'QPoint',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'mouseReleaseEvent': (
          ('_ZN23QAbstract3DInputHandler17mouseReleaseEventEP11QMouseEventR'
           'K6QPoint',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'mouseMoveEvent': (
          ('_ZN23QAbstract3DInputHandler14mouseMoveEventEP11QMouseEventRK6Q'
           'Point',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QMouseEvent'),
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'wheelEvent': (
          ('_ZN23QAbstract3DInputHandler10wheelEventEP11QWheelEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QWheelEvent'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstract3DInputHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstract3DInputHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QAbstract3DInputHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def inputView(self) -> InputView:
    """
    Calls Qt's 'InputView QAbstract3DInputHandler::inputView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#inputView

    Returns
    -------

    InputView
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'InputView(number)' gives.
    """
    #  InputView QAbstract3DInputHandler::inputView() const
    return QAbstract3DInputHandler.InputView(self.uglySide.call(
        'ritual_ZNK23QAbstract3DInputHandler9inputViewEv',
    ))

  def inputPosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint QAbstract3DInputHandler::inputPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#inputPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QAbstract3DInputHandler::inputPosition() const
    address = self.uglySide.call(
        'ritual_ZNK23QAbstract3DInputHandler13inputPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def scene(self) -> Optional[Q3DScene]:
    """
    Calls Qt's 'Q3DScene *QAbstract3DInputHandler::scene() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstract3dinputhandler.html#scene

    Returns
    -------

    Optional[Q3DScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DScene *QAbstract3DInputHandler::scene() const
    address = self.uglySide.call(
        'ritual_ZNK23QAbstract3DInputHandler5sceneEv',
    )
    from . import Q3DScene
    return Q3DScene._cuteAt(address)

  def prevDistance(self) -> int:
    """
    Calls Qt's 'int QAbstract3DInputHandler::prevDistance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#prevDistance
    """
    #  int QAbstract3DInputHandler::prevDistance() const
    return self.uglySide.call(
        'ritual_ZNK23QAbstract3DInputHandler12prevDistanceEv',
    )

  def previousInputPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QAbstract3DInputHandler::previousInputPos() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#previousInputPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QAbstract3DInputHandler::previousInputPos() const
    address = self.uglySide.call(
        'ritual_ZNK23QAbstract3DInputHandler16previousInputPosEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(InputView)
  def setInputView(self, inputView: InputView) -> None:
    """
    Calls Qt's 'void QAbstract3DInputHandler::setInputView(InputView
    inputView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#setInputView

    Parameters
    ----------

    inputView : InputView
      Passed on as its number.
    """
    #  void QAbstract3DInputHandler::setInputView(InputView inputView)
    self.uglySide.call(
        'ritual_ZN23QAbstract3DInputHandler12setInputViewENS_9InputViewE',
        inputView.value,
    )

  @overload(QPoint)
  def setInputPosition(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QAbstract3DInputHandler::setInputPosition(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#setInputPosition

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QAbstract3DInputHandler::setInputPosition(const QPoint &position)
    self.uglySide.call(
        'ritual_ZN23QAbstract3DInputHandler16setInputPositionERK6QPoint',
        self._valueOf(position),
    )

  @overload(Q3DScene)
  @overload(NoneType)
  def setScene(self, scene: Optional[Q3DScene]) -> None:
    """
    Calls Qt's 'void QAbstract3DInputHandler::setScene(Q3DScene *scene)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#setScene

    Parameters
    ----------

    scene : Optional[Q3DScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DInputHandler::setScene(Q3DScene *scene)
    self.uglySide.call(
        'ritual_ZN23QAbstract3DInputHandler8setSceneEP8Q3DScene',
        self._addressOf(scene),
    )

  @overload(int)
  def setPrevDistance(self, distance: int) -> None:
    """
    Calls Qt's 'void QAbstract3DInputHandler::setPrevDistance(int distance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#setPrevDistance

    Parameters
    ----------

    distance : int
      Passed on as it is.
    """
    #  void QAbstract3DInputHandler::setPrevDistance(int distance)
    self.uglySide.call(
        'ritual_ZN23QAbstract3DInputHandler15setPrevDistanceEi', distance,
    )

  @overload(QPoint)
  def setPreviousInputPos(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QAbstract3DInputHandler::setPreviousInputPos(const
    QPoint &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#setPreviousInputPos

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QAbstract3DInputHandler::setPreviousInputPos(const QPoint
    #      &position)
    self.uglySide.call(
        'ritual_ZN23QAbstract3DInputHandler19setPreviousInputPosERK6QPoint',
        self._valueOf(position),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QAbstract3DInputHandler::QAbstract3DInputHandler(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstract3DInputHandler::QAbstract3DInputHandler(QObject *parent)
    self._noteCreation(QAbstract3DInputHandler, lambda: Rituals.call(
        'ritual_ZN23QAbstract3DInputHandlerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void
    QAbstract3DInputHandler::mouseDoubleClickEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DInputHandler::mouseDoubleClickEvent(QMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN23QAbstract3DInputHandler21mouseDoubleClickEventEP11QMous'
        'eEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAbstract3DInputHandler21mouseDoubleClickEventEP1'
          '1QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QAbstract3DInputHandler::touchEvent(QTouchEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DInputHandler::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN23QAbstract3DInputHandler10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAbstract3DInputHandler10touchEventEP11QTouchEven'
          't')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent, QPoint)
  @overload(NoneType, QPoint)
  def mousePressEvent(
      self,
      event: Optional[QMouseEvent],
      mousePos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void QAbstract3DInputHandler::mousePressEvent(QMouseEvent
    *event, const QPoint &mousePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QAbstract3DInputHandler::mousePressEvent(QMouseEvent *event,
    #      const QPoint &mousePos)
    ritual = (
        'ritual_ZN23QAbstract3DInputHandler15mousePressEventEP11QMouseEvent'
        'RK6QPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAbstract3DInputHandler15mousePressEventEP11QMous'
          'eEventRK6QPoint')
    self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(mousePos),
    )

  @overload(QMouseEvent, QPoint)
  @overload(NoneType, QPoint)
  def mouseReleaseEvent(
      self,
      event: Optional[QMouseEvent],
      mousePos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void QAbstract3DInputHandler::mouseReleaseEvent(QMouseEvent
    *event, const QPoint &mousePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QAbstract3DInputHandler::mouseReleaseEvent(QMouseEvent *event,
    #      const QPoint &mousePos)
    ritual = (
        'ritual_ZN23QAbstract3DInputHandler17mouseReleaseEventEP11QMouseEve'
        'ntRK6QPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAbstract3DInputHandler17mouseReleaseEventEP11QMo'
          'useEventRK6QPoint')
    self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(mousePos),
    )

  @overload(QMouseEvent, QPoint)
  @overload(NoneType, QPoint)
  def mouseMoveEvent(
      self,
      event: Optional[QMouseEvent],
      mousePos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void QAbstract3DInputHandler::mouseMoveEvent(QMouseEvent
    *event, const QPoint &mousePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QAbstract3DInputHandler::mouseMoveEvent(QMouseEvent *event, const
    #      QPoint &mousePos)
    ritual = (
        'ritual_ZN23QAbstract3DInputHandler14mouseMoveEventEP11QMouseEventR'
        'K6QPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAbstract3DInputHandler14mouseMoveEventEP11QMouse'
          'EventRK6QPoint')
    self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(mousePos),
    )

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QAbstract3DInputHandler::wheelEvent(QWheelEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DInputHandler::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN23QAbstract3DInputHandler10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QAbstract3DInputHandler10wheelEventEP11QWheelEven'
          't')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPoint)
  def positionChanged(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QAbstract3DInputHandler::positionChanged(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#positionChanged

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QAbstract3DInputHandler::positionChanged(const QPoint &position)
    self.uglySide.call(
        'ritual_ZN23QAbstract3DInputHandler15positionChangedERK6QPoint',
        self._valueOf(position),
    )

  @overload(InputView)
  def inputViewChanged(self, view: InputView) -> None:
    """
    Calls Qt's 'void
    QAbstract3DInputHandler::inputViewChanged(QAbstract3DInputHandler::
    InputView view)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#inputViewChanged

    Parameters
    ----------

    view : InputView
      Passed on as its number.
    """
    #  void QAbstract3DInputHandler::inputViewChanged(
    #      QAbstract3DInputHandler::InputView view)
    self.uglySide.call(
        'ritual_ZN23QAbstract3DInputHandler16inputViewChangedENS_9InputView'
        'E',
        view.value,
    )

  @overload(Q3DScene)
  @overload(NoneType)
  def sceneChanged(self, scene: Optional[Q3DScene]) -> None:
    """
    Calls Qt's 'void QAbstract3DInputHandler::sceneChanged(Q3DScene *scene)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstract3dinputhandler.html#sceneChanged

    Parameters
    ----------

    scene : Optional[Q3DScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstract3DInputHandler::sceneChanged(Q3DScene *scene)
    self.uglySide.call(
        'ritual_ZN23QAbstract3DInputHandler12sceneChangedEP8Q3DScene',
        self._addressOf(scene),
    )


#  Qt's 'QList<QAbstract3DInputHandler *>': the list of
#  QAbstract3DInputHandler, which 'QList[QAbstract3DInputHandler]' gives. It
#  is made here, so that there is one as soon as there can be a
#  QAbstract3DInputHandler.
QList.createKind(
    QAbstract3DInputHandler, 'address',
    make='ritual_list_make_QAbstract3DInputHandler_ptr',
    add='ritual_list_add_QAbstract3DInputHandler_ptr',
    size='ritual_list_size_QAbstract3DInputHandler_ptr',
    at='ritual_list_at_QAbstract3DInputHandler_ptr',
    drop='ritual_list_drop_QAbstract3DInputHandler_ptr',
)

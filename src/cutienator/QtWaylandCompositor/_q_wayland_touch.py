"""
QWaylandTouch binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandtouch.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QWaylandObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtGui import QTouchEvent
  from . import QWaylandClient, QWaylandCompositor, QWaylandSeat
  from . import QWaylandSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QTouchEvent = WAIT['QTouchEvent']
  QWaylandClient = WAIT['QWaylandClient']
  QWaylandSeat = WAIT['QWaylandSeat']
  QWaylandSurface = WAIT['QWaylandSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandTouch(QWaylandObject):
  """
  The cute side of Qt's QWaylandTouch: a plain Python object standing in
  front of one C++ QWaylandTouch.

  It is built on the cute 'QWaylandObject', as Qt's QWaylandTouch is built on
  Qt's QWaylandObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandTouch that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'tr', 'seat', 'compositor',
  'sendTouchPointEvent', 'sendFrameEvent', 'sendCancelEvent',
  'sendFullTouchEvent', 'addClient'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandTouch::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QWaylandTouch::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandTouchPrivate *QWaylandTouch::d_func()': gives
    'QWaylandTouchPrivate', which has no cute class yet.
  - Qt's 'const QWaylandTouchPrivate *QWaylandTouch::d_func() const': gives
    'QWaylandTouchPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandTouch is created at the first use, not by
    'QWaylandTouch(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandTouch.
  - Qt tells when it has removed the C++ QWaylandTouch. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QWaylandTouch::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandtouch.html#tr

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
    #  QString QWaylandTouch::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QWaylandTouch2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandTouch'

  #  A C++ QWaylandTouch Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandTouch'

  #  The functions Qt calls itself that QWaylandTouch is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'sendTouchPointEvent': (
          ('_ZN13QWaylandTouch19sendTouchPointEventEP15QWaylandSurfaceiRK7Q'
           'PointFN2Qt15TouchPointStateE',
           ('unsigned int', 'number', ''),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandSurface'),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QPointF'),
               ('int', 'enum', 'QtCore:Qt.TouchPointState'),
           )),
      ),
      'sendFrameEvent': (
          ('_ZN13QWaylandTouch14sendFrameEventEP14QWaylandClient',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandClient'),
           )),
      ),
      'sendCancelEvent': (
          ('_ZN13QWaylandTouch15sendCancelEventEP14QWaylandClient',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandClient'),
           )),
      ),
      'sendFullTouchEvent': (
          ('_ZN13QWaylandTouch18sendFullTouchEventEP15QWaylandSurfaceP11QTo'
           'uchEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandSurface'),
               ('address', 'address', 'QtGui:QTouchEvent'),
           )),
      ),
      'addClient': (
          ('_ZN13QWaylandTouch9addClientEP14QWaylandClientjj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandClient'),
               ('unsigned int', 'number', ''),
               ('unsigned int', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QWaylandTouch::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandtouch.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandTouch::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QWaylandTouch10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def seat(self) -> Optional[QWaylandSeat]:
    """
    Calls Qt's 'QWaylandSeat *QWaylandTouch::seat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandtouch.html#seat

    Returns
    -------

    Optional[QWaylandSeat]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSeat *QWaylandTouch::seat() const
    address = self.uglySide.call('ritual_ZNK13QWaylandTouch4seatEv')
    from . import QWaylandSeat
    return QWaylandSeat._cuteAt(address)

  def compositor(self) -> Optional[QWaylandCompositor]:
    """
    Calls Qt's 'QWaylandCompositor *QWaylandTouch::compositor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandtouch.html#compositor

    Returns
    -------

    Optional[QWaylandCompositor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandCompositor *QWaylandTouch::compositor() const
    address = self.uglySide.call('ritual_ZNK13QWaylandTouch10compositorEv')
    from . import QWaylandCompositor
    return QWaylandCompositor._cuteAt(address)

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

  @overload(QWaylandSeat)
  @overload(NoneType)
  @overload(QWaylandSeat, QObject)
  @overload(QWaylandSeat, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      seat: Optional[QWaylandSeat],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QWaylandTouch::QWaylandTouch(QWaylandSeat
    *seat, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandtouch.html#QWaylandTouch

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandTouch::QWaylandTouch(QWaylandSeat *seat, QObject *parent)
    self._noteCreation(QWaylandTouch, lambda: Rituals.call(
        'ritual_ZN13QWaylandTouchC1EP12QWaylandSeatP7QObject',
        self._addressOf(seat), self._addressOf(parent, 'QObject'),
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

  @overload(QWaylandSurface, int, QPointF, Qt.TouchPointState)
  @overload(NoneType, int, QPointF, Qt.TouchPointState)
  def sendTouchPointEvent(
      self,
      surface: Optional[QWaylandSurface],
      id: int,
      position: QPointF,
      state: Qt.TouchPointState,
  ) -> int:
    """
    Calls Qt's 'uint QWaylandTouch::sendTouchPointEvent(QWaylandSurface
    *surface, int id, const QPointF &position, Qt::TouchPointState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandtouch.html#sendTouchPointEvent

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    state : Qt.TouchPointState
      Passed on as its number.
    """
    #  uint QWaylandTouch::sendTouchPointEvent(QWaylandSurface *surface, int
    #      id, const QPointF &position, Qt::TouchPointState state)
    ritual = (
        'ritual_ZN13QWaylandTouch19sendTouchPointEventEP15QWaylandSurfaceiR'
        'K7QPointFN2Qt15TouchPointStateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QWaylandTouch19sendTouchPointEventEP15QWaylandSur'
          'faceiRK7QPointFN2Qt15TouchPointStateE')
    return self.uglySide.call(
        ritual,
        self._addressOf(surface), id, self._valueOf(position, 'QPointF'),
        state.value,
    )

  @overload(QWaylandClient)
  @overload(NoneType)
  def sendFrameEvent(self, client: Optional[QWaylandClient]) -> None:
    """
    Calls Qt's 'void QWaylandTouch::sendFrameEvent(QWaylandClient *client)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandtouch.html#sendFrameEvent

    Parameters
    ----------

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandTouch::sendFrameEvent(QWaylandClient *client)
    ritual = 'ritual_ZN13QWaylandTouch14sendFrameEventEP14QWaylandClient'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QWaylandTouch14sendFrameEventEP14QWaylandClient')
    self.uglySide.call(ritual, self._addressOf(client))

  @overload(QWaylandClient)
  @overload(NoneType)
  def sendCancelEvent(self, client: Optional[QWaylandClient]) -> None:
    """
    Calls Qt's 'void QWaylandTouch::sendCancelEvent(QWaylandClient *client)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandtouch.html#sendCancelEvent

    Parameters
    ----------

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandTouch::sendCancelEvent(QWaylandClient *client)
    ritual = 'ritual_ZN13QWaylandTouch15sendCancelEventEP14QWaylandClient'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QWaylandTouch15sendCancelEventEP14QWaylandClient')
    self.uglySide.call(ritual, self._addressOf(client))

  @overload(QWaylandSurface, QTouchEvent)
  @overload(QWaylandSurface, NoneType)
  @overload(NoneType, QTouchEvent)
  @overload(NoneType, NoneType)
  def sendFullTouchEvent(
      self,
      surface: Optional[QWaylandSurface],
      event: Optional[QTouchEvent],
  ) -> None:
    """
    Calls Qt's 'void QWaylandTouch::sendFullTouchEvent(QWaylandSurface
    *surface, QTouchEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandtouch.html#sendFullTouchEvent

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandTouch::sendFullTouchEvent(QWaylandSurface *surface,
    #      QTouchEvent *event)
    ritual = (
        'ritual_ZN13QWaylandTouch18sendFullTouchEventEP15QWaylandSurfaceP11'
        'QTouchEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QWaylandTouch18sendFullTouchEventEP15QWaylandSurf'
          'aceP11QTouchEvent')
    self.uglySide.call(
        ritual, self._addressOf(surface), self._addressOf(event),
    )

  @overload(QWaylandClient, int, int)
  @overload(NoneType, int, int)
  def addClient(
      self,
      client: Optional[QWaylandClient],
      id: int,
      version: int,
  ) -> None:
    """
    Calls Qt's 'void QWaylandTouch::addClient(QWaylandClient *client,
    uint32_t id, uint32_t version)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandtouch.html#addClient

    Parameters
    ----------

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is.

    version : int
      Passed on as it is.
    """
    #  void QWaylandTouch::addClient(QWaylandClient *client, uint32_t id,
    #      uint32_t version)
    ritual = 'ritual_ZN13QWaylandTouch9addClientEP14QWaylandClientjj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QWaylandTouch9addClientEP14QWaylandClientjj'
    self.uglySide.call(ritual, self._addressOf(client), id, version)

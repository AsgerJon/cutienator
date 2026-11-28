"""
QWaylandKeyboard binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandkeyboard.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QWaylandObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QWaylandClient, QWaylandCompositor, QWaylandSeat
  from . import QWaylandSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandClient = WAIT['QWaylandClient']
  QWaylandSeat = WAIT['QWaylandSeat']
  QWaylandSurface = WAIT['QWaylandSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandKeyboard(QWaylandObject):
  """
  The cute side of Qt's QWaylandKeyboard: a plain Python object standing in
  front of one C++ QWaylandKeyboard.

  It is built on the cute 'QWaylandObject', as Qt's QWaylandKeyboard is built
  on Qt's QWaylandObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandKeyboard that has a ritual and that Python
  can call so far, 20 names in all: 'metaObject', 'tr', 'seat', 'compositor',
  'repeatRate', 'setRepeatRate', 'repeatDelay', 'setRepeatDelay', 'setFocus',
  'sendKeyModifiers', 'sendKeyPressEvent', 'sendKeyReleaseEvent', 'focus',
  'focusClient', 'addClient', 'keyToScanCode', 'focusChanged',
  'repeatRateChanged', 'repeatDelayChanged', 'updateKeymap'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandKeyboard::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWaylandKeyboard::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandKeyboardPrivate *QWaylandKeyboard::d_func()': gives
    'QWaylandKeyboardPrivate', which has no cute class yet.
  - Qt's 'const QWaylandKeyboardPrivate *QWaylandKeyboard::d_func() const':
    gives 'QWaylandKeyboardPrivate', which has no cute class yet.
  - Qt's 'void QWaylandKeyboard::focusDestroyed(void *data)': names 'void',
    which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandKeyboard is created at the first use, not by
    'QWaylandKeyboard(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandKeyboard.
  - Qt tells when it has removed the C++ QWaylandKeyboard. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandKeyboard that has no cute function yet,
    'focusDestroyed', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QWaylandKeyboard::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeyboard.html#tr

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
    #  QString QWaylandKeyboard::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QWaylandKeyboard2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandKeyboard'

  #  The functions Qt calls itself that QWaylandKeyboard is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setFocus': (
          ('_ZN16QWaylandKeyboard8setFocusEP15QWaylandSurface',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandSurface'),
           )),
      ),
      'sendKeyModifiers': (
          ('_ZN16QWaylandKeyboard16sendKeyModifiersEP14QWaylandClientj',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWaylandCompositor:QWaylandClient'),
               ('unsigned int', 'number', ''),
           )),
      ),
      'sendKeyPressEvent': (
          ('_ZN16QWaylandKeyboard17sendKeyPressEventEj',
           ('nothing', 'nothing', ''),
           (
               ('unsigned int', 'number', ''),
           )),
      ),
      'sendKeyReleaseEvent': (
          ('_ZN16QWaylandKeyboard19sendKeyReleaseEventEj',
           ('nothing', 'nothing', ''),
           (
               ('unsigned int', 'number', ''),
           )),
      ),
      'addClient': (
          ('_ZN16QWaylandKeyboard9addClientEP14QWaylandClientjj',
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
    Calls Qt's 'const QMetaObject *QWaylandKeyboard::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeyboard.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandKeyboard::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QWaylandKeyboard10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def seat(self) -> Optional[QWaylandSeat]:
    """
    Calls Qt's 'QWaylandSeat *QWaylandKeyboard::seat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeyboard.html#seat

    Returns
    -------

    Optional[QWaylandSeat]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSeat *QWaylandKeyboard::seat() const
    address = self.uglySide.call('ritual_ZNK16QWaylandKeyboard4seatEv')
    from . import QWaylandSeat
    return QWaylandSeat._cuteAt(address)

  def compositor(self) -> Optional[QWaylandCompositor]:
    """
    Calls Qt's 'QWaylandCompositor *QWaylandKeyboard::compositor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeyboard.html#compositor

    Returns
    -------

    Optional[QWaylandCompositor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandCompositor *QWaylandKeyboard::compositor() const
    address = self.uglySide.call(
        'ritual_ZNK16QWaylandKeyboard10compositorEv',
    )
    from . import QWaylandCompositor
    return QWaylandCompositor._cuteAt(address)

  def repeatRate(self) -> int:
    """
    Calls Qt's 'quint32 QWaylandKeyboard::repeatRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeyboard.html#repeatRate
    """
    #  quint32 QWaylandKeyboard::repeatRate() const
    return self.uglySide.call('ritual_ZNK16QWaylandKeyboard10repeatRateEv')

  def repeatDelay(self) -> int:
    """
    Calls Qt's 'quint32 QWaylandKeyboard::repeatDelay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeyboard.html#repeatDelay
    """
    #  quint32 QWaylandKeyboard::repeatDelay() const
    return self.uglySide.call('ritual_ZNK16QWaylandKeyboard11repeatDelayEv')

  def focus(self) -> Optional[QWaylandSurface]:
    """
    Calls Qt's 'QWaylandSurface *QWaylandKeyboard::focus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeyboard.html#focus

    Returns
    -------

    Optional[QWaylandSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurface *QWaylandKeyboard::focus() const
    address = self.uglySide.call('ritual_ZNK16QWaylandKeyboard5focusEv')
    from . import QWaylandSurface
    return QWaylandSurface._cuteAt(address)

  def focusClient(self) -> Optional[QWaylandClient]:
    """
    Calls Qt's 'QWaylandClient *QWaylandKeyboard::focusClient() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeyboard.html#focusClient

    Returns
    -------

    Optional[QWaylandClient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandClient *QWaylandKeyboard::focusClient() const
    address = self.uglySide.call(
        'ritual_ZNK16QWaylandKeyboard11focusClientEv',
    )
    from . import QWaylandClient
    return QWaylandClient._cuteAt(address)

  @overload(int)
  def keyToScanCode(self, qtKey: int) -> int:
    """
    Calls Qt's 'uint QWaylandKeyboard::keyToScanCode(int qtKey) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandkeyboard.html#keyToScanCode

    Parameters
    ----------

    qtKey : int
      Passed on as it is.
    """
    #  uint QWaylandKeyboard::keyToScanCode(int qtKey) const
    return self.uglySide.call(
        'ritual_ZNK16QWaylandKeyboard13keyToScanCodeEi', qtKey,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRepeatRate(self, rate: int) -> None:
    """
    Calls Qt's 'void QWaylandKeyboard::setRepeatRate(quint32 rate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandkeyboard.html#setRepeatRate

    Parameters
    ----------

    rate : int
      Passed on as it is.
    """
    #  void QWaylandKeyboard::setRepeatRate(quint32 rate)
    self.uglySide.call('ritual_ZN16QWaylandKeyboard13setRepeatRateEj', rate)

  @overload(int)
  def setRepeatDelay(self, delay: int) -> None:
    """
    Calls Qt's 'void QWaylandKeyboard::setRepeatDelay(quint32 delay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandkeyboard.html#setRepeatDelay

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QWaylandKeyboard::setRepeatDelay(quint32 delay)
    self.uglySide.call(
        'ritual_ZN16QWaylandKeyboard14setRepeatDelayEj', delay,
    )

  @overload(QWaylandSurface)
  @overload(NoneType)
  def setFocus(self, surface: Optional[QWaylandSurface]) -> None:
    """
    Calls Qt's 'void QWaylandKeyboard::setFocus(QWaylandSurface *surface)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeyboard.html#setFocus

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandKeyboard::setFocus(QWaylandSurface *surface)
    ritual = 'ritual_ZN16QWaylandKeyboard8setFocusEP15QWaylandSurface'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QWaylandKeyboard8setFocusEP15QWaylandSurface'
    self.uglySide.call(ritual, self._addressOf(surface))

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
    Notes what was given, for Qt's
    'QWaylandKeyboard::QWaylandKeyboard(QWaylandSeat *seat, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandkeyboard.html#QWaylandKeyboard

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandKeyboard::QWaylandKeyboard(QWaylandSeat *seat, QObject
    #      *parent)
    self._noteCreation(QWaylandKeyboard, lambda: Rituals.call(
        'ritual_ZN16QWaylandKeyboardC1EP12QWaylandSeatP7QObject',
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

  @overload(QWaylandClient, int)
  @overload(NoneType, int)
  def sendKeyModifiers(
      self,
      client: Optional[QWaylandClient],
      serial: int,
  ) -> None:
    """
    Calls Qt's 'void QWaylandKeyboard::sendKeyModifiers(QWaylandClient
    *client, uint32_t serial)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandkeyboard.html#sendKeyModifiers

    Parameters
    ----------

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    serial : int
      Passed on as it is.
    """
    #  void QWaylandKeyboard::sendKeyModifiers(QWaylandClient *client,
    #      uint32_t serial)
    ritual = (
        'ritual_ZN16QWaylandKeyboard16sendKeyModifiersEP14QWaylandClientj')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QWaylandKeyboard16sendKeyModifiersEP14QWaylandCli'
          'entj')
    self.uglySide.call(ritual, self._addressOf(client), serial)

  @overload(int)
  def sendKeyPressEvent(self, code: int) -> None:
    """
    Calls Qt's 'void QWaylandKeyboard::sendKeyPressEvent(uint code)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandkeyboard.html#sendKeyPressEvent

    Parameters
    ----------

    code : int
      Passed on as it is.
    """
    #  void QWaylandKeyboard::sendKeyPressEvent(uint code)
    ritual = 'ritual_ZN16QWaylandKeyboard17sendKeyPressEventEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QWaylandKeyboard17sendKeyPressEventEj'
    self.uglySide.call(ritual, code)

  @overload(int)
  def sendKeyReleaseEvent(self, code: int) -> None:
    """
    Calls Qt's 'void QWaylandKeyboard::sendKeyReleaseEvent(uint code)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandkeyboard.html#sendKeyReleaseEvent

    Parameters
    ----------

    code : int
      Passed on as it is.
    """
    #  void QWaylandKeyboard::sendKeyReleaseEvent(uint code)
    ritual = 'ritual_ZN16QWaylandKeyboard19sendKeyReleaseEventEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QWaylandKeyboard19sendKeyReleaseEventEj'
    self.uglySide.call(ritual, code)

  @overload(QWaylandClient, int, int)
  @overload(NoneType, int, int)
  def addClient(
      self,
      client: Optional[QWaylandClient],
      id: int,
      version: int,
  ) -> None:
    """
    Calls Qt's 'void QWaylandKeyboard::addClient(QWaylandClient *client,
    uint32_t id, uint32_t version)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeyboard.html#addClient

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
    #  void QWaylandKeyboard::addClient(QWaylandClient *client, uint32_t id,
    #      uint32_t version)
    ritual = 'ritual_ZN16QWaylandKeyboard9addClientEP14QWaylandClientjj'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QWaylandKeyboard9addClientEP14QWaylandClientjj')
    self.uglySide.call(ritual, self._addressOf(client), id, version)

  @overload(QWaylandSurface)
  @overload(NoneType)
  def focusChanged(self, surface: Optional[QWaylandSurface]) -> None:
    """
    Calls Qt's 'void QWaylandKeyboard::focusChanged(QWaylandSurface
    *surface)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeyboard.html#focusChanged

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandKeyboard::focusChanged(QWaylandSurface *surface)
    self.uglySide.call(
        'ritual_ZN16QWaylandKeyboard12focusChangedEP15QWaylandSurface',
        self._addressOf(surface),
    )

  @overload(int)
  def repeatRateChanged(self, repeatRate: int) -> None:
    """
    Calls Qt's 'void QWaylandKeyboard::repeatRateChanged(quint32
    repeatRate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandkeyboard.html#repeatRateChanged

    Parameters
    ----------

    repeatRate : int
      Passed on as it is.
    """
    #  void QWaylandKeyboard::repeatRateChanged(quint32 repeatRate)
    self.uglySide.call(
        'ritual_ZN16QWaylandKeyboard17repeatRateChangedEj', repeatRate,
    )

  @overload(int)
  def repeatDelayChanged(self, repeatDelay: int) -> None:
    """
    Calls Qt's 'void QWaylandKeyboard::repeatDelayChanged(quint32
    repeatDelay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandkeyboard.html#repeatDelayChanged

    Parameters
    ----------

    repeatDelay : int
      Passed on as it is.
    """
    #  void QWaylandKeyboard::repeatDelayChanged(quint32 repeatDelay)
    self.uglySide.call(
        'ritual_ZN16QWaylandKeyboard18repeatDelayChangedEj', repeatDelay,
    )

  def updateKeymap(self) -> None:
    """
    Calls Qt's 'void QWaylandKeyboard::updateKeymap()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandkeyboard.html#updateKeymap
    """
    #  void QWaylandKeyboard::updateKeymap()
    self.uglySide.call('ritual_ZN16QWaylandKeyboard12updateKeymapEv')

  @staticmethod
  def focusDestroyed(*__, **_) -> Never:
    """
    Qt's 'void QWaylandKeyboard::focusDestroyed(void *data)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandKeyboard.focusDestroyed' has no cute function yet. Qt's "
        "'void QWaylandKeyboard::focusDestroyed(void *data)': names 'void', "
        "which has no cute class yet.")

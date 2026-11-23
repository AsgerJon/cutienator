"""
QSocketNotifier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsocketnotifier.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSocketNotifier(QObject):
  """
  The cute side of Qt's QSocketNotifier: a plain Python object standing in
  front of one C++ QSocketNotifier.

  It is built on the cute 'QObject', as Qt's QSocketNotifier is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSocketNotifier that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'tr', 'setSocket', 'socket',
  'type', 'isValid', 'isEnabled', 'setEnabled', 'event'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSocketNotifier::~QSocketNotifier()': the destructor: Python never
    removes a C++ QSocketNotifier.

  What has no ritual
  ------------------

  9 of the 21 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found;
  1 a signal.

  What to expect
  --------------

  - The C++ QSocketNotifier is created at the first use, not by
    'QSocketNotifier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSocketNotifier.
  - Qt tells when it has removed the C++ QSocketNotifier. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QSocketNotifier, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QSocketNotifier::Type' of Qt, with the 3 names Qt gives in it.
    """

    Read = Kee[int](0)
    Write = Kee[int](1)
    Exception = Kee[int](2)

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
    Calls Qt's 'QString QSocketNotifier::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsocketnotifier.html#tr

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
    #  QString QSocketNotifier::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QSocketNotifier2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSocketNotifier'

  #  A C++ QSocketNotifier Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSocketNotifier'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSocketNotifier::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsocketnotifier.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSocketNotifier::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QSocketNotifier10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def socket(self) -> int:
    """
    Calls Qt's 'qintptr QSocketNotifier::socket() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsocketnotifier.html#socket
    """
    #  qintptr QSocketNotifier::socket() const
    return self.uglySide.call('ritual_ZNK15QSocketNotifier6socketEv')

  def type(self) -> Type:
    """
    Calls Qt's 'Type QSocketNotifier::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsocketnotifier.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QSocketNotifier::type() const
    return QSocketNotifier.Type(self.uglySide.call(
        'ritual_ZNK15QSocketNotifier4typeEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSocketNotifier::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsocketnotifier.html#isValid
    """
    #  bool QSocketNotifier::isValid() const
    return self.uglySide.call('ritual_ZNK15QSocketNotifier7isValidEv')

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSocketNotifier::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsocketnotifier.html#isEnabled
    """
    #  bool QSocketNotifier::isEnabled() const
    return self.uglySide.call('ritual_ZNK15QSocketNotifier9isEnabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSocket(self, socket: int) -> None:
    """
    Calls Qt's 'void QSocketNotifier::setSocket(qintptr socket)'.

    Qt's own words: https://doc.qt.io/qt-6/qsocketnotifier.html#setSocket

    Parameters
    ----------

    socket : int
      Passed on as it is.
    """
    #  void QSocketNotifier::setSocket(qintptr socket)
    self.uglySide.call('ritual_ZN15QSocketNotifier9setSocketEx', socket)

  @overload(bool)
  def setEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QSocketNotifier::setEnabled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsocketnotifier.html#setEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QSocketNotifier::setEnabled(bool a0)
    self.uglySide.call('ritual_ZN15QSocketNotifier10setEnabledEb', a0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Type)
  @overload(Type, QObject)
  @overload(Type, NoneType)
  def __init__(self, a0: Type, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QSocketNotifier::QSocketNotifier(Type a0,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocketnotifier.html#QSocketNotifier

    Parameters
    ----------

    a0 : Type
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSocketNotifier::QSocketNotifier(Type a0, QObject *parent)
    self._noteCreation(QSocketNotifier, lambda: Rituals.call(
        'ritual_ZN15QSocketNotifierC1ENS_4TypeEP7QObject',
        a0.value, self._addressOf(parent, 'QObject'),
    ))

  @overload(int, Type)
  @overload(int, Type, QObject)
  @overload(int, Type, NoneType)
  def __init__(
      self,
      socket: int,
      a1: Type,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSocketNotifier::QSocketNotifier(qintptr
    socket, Type a1, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocketnotifier.html#QSocketNotifier

    Parameters
    ----------

    socket : int
      Passed on as it is.

    a1 : Type
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSocketNotifier::QSocketNotifier(qintptr socket, Type a1, QObject
    #      *parent)
    self._noteCreation(QSocketNotifier, lambda: Rituals.call(
        'ritual_ZN15QSocketNotifierC1ExNS_4TypeEP7QObject',
        socket, a1.value, self._addressOf(parent, 'QObject'),
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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSocketNotifier::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsocketnotifier.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSocketNotifier::event(QEvent *a0)
    ritual = 'ritual_ZN15QSocketNotifier5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QSocketNotifier5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

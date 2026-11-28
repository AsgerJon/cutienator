"""
QX11Info binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtx11extras_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QX11Info to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QX11Info(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QX11Info: a plain Python object standing in front of
  one C++ QX11Info.

  C++ hands a QX11Info around as a copy, so every C++ QX11Info behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QX11Info that has a ritual and that Python can call
  so far, 15 names in all: 'isPlatformX11', 'appDpiX', 'appDpiY',
  'appRootWindow', 'appScreen', 'appTime', 'appUserTime', 'setAppTime',
  'setAppUserTime', 'getTimestamp', 'nextStartupId', 'setNextStartupId',
  'isCompositingManagerRunning', 'generatePeekerId', 'removePeekerId'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Display *QX11Info::display()': gives 'struct _XDisplay', which has
    no cute class yet.
  - Qt's 'xcb_connection_t *QX11Info::connection()': gives
    'xcb_connection_t', which has no cute class yet.
  - Qt's 'bool QX11Info::peekEventQueue(PeekerCallback peeker, void
    *peekerData, PeekOptions option, qint32 peekerId)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QX11Info::~QX11Info()': the destructor: Python removes its C++
    QX11Info by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QX11Info is created at the first use, not by 'QX11Info(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QX11Info back gives a copy the ritual made for
    Python, in a new cute QX11Info.
  - Each name of Qt's QX11Info that has no cute function yet, 'connection',
    'display', 'peekEventQueue', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QX11Info, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class PeekOption(CuteFlags):
    """
    The flags enum 'QX11Info::PeekOption' of Qt, with the 2 names Qt gives in
    it. Qt names the type of its combinations 'QX11Info::PeekOptions'.
    """

    PeekDefault = 0x0
    PeekFromCachedIndex = 0x1

  PeekOptions = PeekOption

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def isPlatformX11() -> bool:
    """
    Calls Qt's 'bool QX11Info::isPlatformX11()'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#isPlatformX11
    """
    #  bool QX11Info::isPlatformX11()
    return Rituals.call('ritual_ZN8QX11Info13isPlatformX11Ev')

  @staticmethod
  @overload()
  @overload(int)
  def appDpiX(screen: int = -1) -> int:
    """
    Calls Qt's 'int QX11Info::appDpiX(int screen)'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#appDpiX

    Parameters
    ----------

    screen : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QX11Info::appDpiX(int screen)
    return Rituals.call('ritual_ZN8QX11Info7appDpiXEi', screen)

  @staticmethod
  @overload()
  @overload(int)
  def appDpiY(screen: int = -1) -> int:
    """
    Calls Qt's 'int QX11Info::appDpiY(int screen)'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#appDpiY

    Parameters
    ----------

    screen : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QX11Info::appDpiY(int screen)
    return Rituals.call('ritual_ZN8QX11Info7appDpiYEi', screen)

  @staticmethod
  @overload()
  @overload(int)
  def appRootWindow(screen: int = -1) -> int:
    """
    Calls Qt's 'quint32 QX11Info::appRootWindow(int screen)'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#appRootWindow

    Parameters
    ----------

    screen : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  quint32 QX11Info::appRootWindow(int screen)
    return Rituals.call('ritual_ZN8QX11Info13appRootWindowEi', screen)

  @staticmethod
  def appScreen() -> int:
    """
    Calls Qt's 'int QX11Info::appScreen()'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#appScreen
    """
    #  int QX11Info::appScreen()
    return Rituals.call('ritual_ZN8QX11Info9appScreenEv')

  @staticmethod
  def appTime() -> int:
    """
    Calls Qt's 'quint32 QX11Info::appTime()'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#appTime
    """
    #  quint32 QX11Info::appTime()
    return Rituals.call('ritual_ZN8QX11Info7appTimeEv')

  @staticmethod
  def appUserTime() -> int:
    """
    Calls Qt's 'quint32 QX11Info::appUserTime()'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#appUserTime
    """
    #  quint32 QX11Info::appUserTime()
    return Rituals.call('ritual_ZN8QX11Info11appUserTimeEv')

  @staticmethod
  @overload(int)
  def setAppTime(time: int) -> None:
    """
    Calls Qt's 'void QX11Info::setAppTime(quint32 time)'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#setAppTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QX11Info::setAppTime(quint32 time)
    Rituals.call('ritual_ZN8QX11Info10setAppTimeEj', time)

  @staticmethod
  @overload(int)
  def setAppUserTime(time: int) -> None:
    """
    Calls Qt's 'void QX11Info::setAppUserTime(quint32 time)'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#setAppUserTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QX11Info::setAppUserTime(quint32 time)
    Rituals.call('ritual_ZN8QX11Info14setAppUserTimeEj', time)

  @staticmethod
  def getTimestamp() -> int:
    """
    Calls Qt's 'quint32 QX11Info::getTimestamp()'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#getTimestamp
    """
    #  quint32 QX11Info::getTimestamp()
    return Rituals.call('ritual_ZN8QX11Info12getTimestampEv')

  @staticmethod
  def nextStartupId() -> QByteArray:
    """
    Calls Qt's 'QByteArray QX11Info::nextStartupId()'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#nextStartupId

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QX11Info::nextStartupId()
    address = Rituals.call('ritual_ZN8QX11Info13nextStartupIdEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  def setNextStartupId(id: QByteArray) -> None:
    """
    Calls Qt's 'void QX11Info::setNextStartupId(const QByteArray &id)'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#setNextStartupId

    Parameters
    ----------

    id : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QX11Info::setNextStartupId(const QByteArray &id)
    Rituals.call(
        'ritual_ZN8QX11Info16setNextStartupIdERK10QByteArray',
        CuteMixin._valueOf(id),
    )

  @staticmethod
  @overload()
  @overload(int)
  def isCompositingManagerRunning(screen: int = -1) -> bool:
    """
    Calls Qt's 'bool QX11Info::isCompositingManagerRunning(int screen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qx11info.html#isCompositingManagerRunning

    Parameters
    ----------

    screen : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  bool QX11Info::isCompositingManagerRunning(int screen)
    return Rituals.call(
        'ritual_ZN8QX11Info27isCompositingManagerRunningEi', screen,
    )

  @staticmethod
  def generatePeekerId() -> int:
    """
    Calls Qt's 'qint32 QX11Info::generatePeekerId()'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#generatePeekerId
    """
    #  qint32 QX11Info::generatePeekerId()
    return Rituals.call('ritual_ZN8QX11Info16generatePeekerIdEv')

  @staticmethod
  @overload(int)
  def removePeekerId(peekerId: int) -> bool:
    """
    Calls Qt's 'bool QX11Info::removePeekerId(qint32 peekerId)'.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#removePeekerId

    Parameters
    ----------

    peekerId : int
      Passed on as it is.
    """
    #  bool QX11Info::removePeekerId(qint32 peekerId)
    return Rituals.call('ritual_ZN8QX11Info14removePeekerIdEi', peekerId)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QX11Info'

  #  Qt's '~QX11Info()'. Naming it makes this a value class: Python owns
  #  every C++ QX11Info behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QX11InfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QX11Info::QX11Info()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qx11info.html#QX11Info
    """
    #  QX11Info::QX11Info()
    self._noteCreation(QX11Info, lambda: Rituals.call(
        'ritual_ZN8QX11InfoC1Ev',
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

  @staticmethod
  def connection(*__, **_) -> Never:
    """
    Qt's 'xcb_connection_t *QX11Info::connection()': gives
    'xcb_connection_t', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QX11Info.connection' has no cute function yet. Qt's "
        "'xcb_connection_t *QX11Info::connection()': gives "
        "'xcb_connection_t', which has no cute class yet.")

  @staticmethod
  def display(*__, **_) -> Never:
    """
    Qt's 'Display *QX11Info::display()': gives 'struct _XDisplay', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QX11Info.display' has no cute function yet. Qt's 'Display "
        "*QX11Info::display()': gives 'struct _XDisplay', which has no cute "
        "class yet.")

  @staticmethod
  def peekEventQueue(*__, **_) -> Never:
    """
    Qt's 'bool QX11Info::peekEventQueue(PeekerCallback peeker, void
    *peekerData, PeekOptions option, qint32 peekerId)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QX11Info.peekEventQueue' has no cute function yet. Qt's 'bool "
        "QX11Info::peekEventQueue(PeekerCallback peeker, void *peekerData, "
        "PeekOptions option, qint32 peekerId)': takes a type Python has no "
        "way to hand over yet.")

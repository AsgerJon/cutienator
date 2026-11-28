"""
QWaylandPresentationTime binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandpresentationtime_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWaylandPresentationTime to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QWaylandCompositor
  from ..QtQuick import QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickWindow = WAIT['QQuickWindow']
  QWaylandCompositor = WAIT['QWaylandCompositor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandPresentationTime(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandPresentationTime: a plain Python object
  standing in front of one C++ QWaylandPresentationTime.

  What exists
  -----------

  Every function of Qt's QWaylandPresentationTime that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'compositor',
  'initialize', 'sendFeedback', 'interfaceName', 'presented'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandPresentationTime::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QWaylandPresentationTime::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandPresentationTimePrivate
    *QWaylandPresentationTime::d_func()': gives
    'QWaylandPresentationTimePrivate', which has no cute class yet.
  - Qt's 'const QWaylandPresentationTimePrivate
    *QWaylandPresentationTime::d_func() const': gives
    'QWaylandPresentationTimePrivate', which has no cute class yet.
  - Qt's 'const struct wl_interface *QWaylandPresentationTime::interface()':
    gives 'struct wl_interface', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandPresentationTime is created at the first use, not by
    'QWaylandPresentationTime(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandPresentationTime.
  - Each name of Qt's QWaylandPresentationTime that has no cute function yet,
    'd_func', 'interface', holds a function that raises
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
    Calls Qt's 'QString QWaylandPresentationTime::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandpresentationtime.html#tr

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
    #  QString QWaylandPresentationTime::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QWaylandPresentationTime2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def interfaceName() -> QByteArray:
    """
    Calls Qt's 'QByteArray QWaylandPresentationTime::interfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpresentationtime.html#interfaceName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWaylandPresentationTime::interfaceName()
    address = Rituals.call(
        'ritual_ZN24QWaylandPresentationTime13interfaceNameEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandPresentationTime'

  #  A C++ QWaylandPresentationTime Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandPresentationTime'

  #  The functions Qt calls itself that QWaylandPresentationTime is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN24QWaylandPresentationTime10initializeEv',
           ('nothing', 'nothing', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandPresentationTime::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpresentationtime.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandPresentationTime::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QWaylandPresentationTime10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def compositor(self) -> Optional[QWaylandCompositor]:
    """
    Calls Qt's 'QWaylandCompositor *QWaylandPresentationTime::compositor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpresentationtime.html#compositor

    Returns
    -------

    Optional[QWaylandCompositor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandCompositor *QWaylandPresentationTime::compositor() const
    address = self.uglySide.call(
        'ritual_ZNK24QWaylandPresentationTime10compositorEv',
    )
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandPresentationTime::QWaylandPresentationTime()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpresentationtime.html
    """
    #  QWaylandPresentationTime::QWaylandPresentationTime()
    self._noteCreation(QWaylandPresentationTime, lambda: Rituals.call(
        'ritual_ZN24QWaylandPresentationTimeC1Ev',
    ))

  @overload(QWaylandCompositor)
  @overload(NoneType)
  def __init__(self, compositor: Optional[QWaylandCompositor]) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandPresentationTime::QWaylandPresentationTime(QWaylandCompositor
    *compositor)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpresentationtime.html

    Parameters
    ----------

    compositor : Optional[QWaylandCompositor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWaylandPresentationTime::QWaylandPresentationTime(QWaylandCompositor
    #      *compositor)
    self._noteCreation(QWaylandPresentationTime, lambda: Rituals.call(
        'ritual_ZN24QWaylandPresentationTimeC1EP18QWaylandCompositor',
        self._addressOf(compositor),
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

  def initialize(self) -> None:
    """
    Calls Qt's 'void QWaylandPresentationTime::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpresentationtime.html#initialize
    """
    #  void QWaylandPresentationTime::initialize()
    ritual = 'ritual_ZN24QWaylandPresentationTime10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QWaylandPresentationTime10initializeEv'
    self.uglySide.call(ritual)

  @overload(QQuickWindow, int, int, int)
  @overload(NoneType, int, int, int)
  def sendFeedback(
      self,
      window: Optional[QQuickWindow],
      sequence: int,
      tv_sec: int,
      tv_nsec: int,
  ) -> None:
    """
    Calls Qt's 'void QWaylandPresentationTime::sendFeedback(QQuickWindow
    *window, quint64 sequence, quint64 tv_sec, quint32 tv_nsec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpresentationtime.html#sendFeedback

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sequence : int
      Passed on as it is.

    tv_sec : int
      Passed on as it is.

    tv_nsec : int
      Passed on as it is.
    """
    #  void QWaylandPresentationTime::sendFeedback(QQuickWindow *window,
    #      quint64 sequence, quint64 tv_sec, quint32 tv_nsec)
    self.uglySide.call(
        'ritual_ZN24QWaylandPresentationTime12sendFeedbackEP12QQuickWindowy'
        'yj',
        self._addressOf(window), sequence, tv_sec, tv_nsec,
    )

  @overload(int, int, int, int)
  def presented(
      self,
      sequence: int,
      tv_sec: int,
      tv_nsec: int,
      refresh_nsec: int,
  ) -> None:
    """
    Calls Qt's 'void QWaylandPresentationTime::presented(quint64 sequence,
    quint64 tv_sec, quint32 tv_nsec, quint32 refresh_nsec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandpresentationtime.html#presented

    Parameters
    ----------

    sequence : int
      Passed on as it is.

    tv_sec : int
      Passed on as it is.

    tv_nsec : int
      Passed on as it is.

    refresh_nsec : int
      Passed on as it is.
    """
    #  void QWaylandPresentationTime::presented(quint64 sequence, quint64
    #      tv_sec, quint32 tv_nsec, quint32 refresh_nsec)
    self.uglySide.call(
        'ritual_ZN24QWaylandPresentationTime9presentedEyyjj',
        sequence, tv_sec, tv_nsec, refresh_nsec,
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QWaylandPresentationTimePrivate
      *QWaylandPresentationTime::d_func()': gives
      'QWaylandPresentationTimePrivate', which has no cute class yet.
    - Qt's 'const QWaylandPresentationTimePrivate
      *QWaylandPresentationTime::d_func() const': gives
      'QWaylandPresentationTimePrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandPresentationTime.d_func' has no cute function yet. Qt's "
        "'QWaylandPresentationTimePrivate "
        "*QWaylandPresentationTime::d_func()': gives "
        "'QWaylandPresentationTimePrivate', which has no cute class yet. "
        "Qt's 'const QWaylandPresentationTimePrivate "
        "*QWaylandPresentationTime::d_func() const': gives "
        "'QWaylandPresentationTimePrivate', which has no cute class yet.")

  @staticmethod
  def interface(*__, **_) -> Never:
    """
    Qt's 'const struct wl_interface *QWaylandPresentationTime::interface()':
    gives 'struct wl_interface', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandPresentationTime.interface' has no cute function yet. "
        "Qt's 'const struct wl_interface "
        "*QWaylandPresentationTime::interface()': gives 'struct "
        "wl_interface', which has no cute class yet.")

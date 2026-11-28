"""
QTest::QTouchEventSequence binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtestsupport_gui.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QPointF
  from . import QPointingDevice, QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QPointingDevice = WAIT['QPointingDevice']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTouchEventSequence(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTest::QTouchEventSequence: a plain Python object
  standing in front of one C++ QTest::QTouchEventSequence.

  C++ hands a QTest::QTouchEventSequence around as a copy, so every C++
  QTest::QTouchEventSequence behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QTest::QTouchEventSequence that has a ritual and
  that Python can call so far, 3 names in all: 'commit', 'cancel',
  'mapToScreen'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTest::QTouchEventSequence::~QTouchEventSequence()': the
    destructor: Python removes its C++ QTest::QTouchEventSequence by it, and
    has no other use for it.
  - Qt's 'QTouchEventSequence &QTest::QTouchEventSequence::press(int touchId,
    const QPoint &pt, QWindow *window)': gives a type Python has no way to
    take yet.
  - Qt's 'QTouchEventSequence &QTest::QTouchEventSequence::move(int touchId,
    const QPoint &pt, QWindow *window)': gives a type Python has no way to
    take yet.
  - Qt's 'QTouchEventSequence &QTest::QTouchEventSequence::release(int
    touchId, const QPoint &pt, QWindow *window)': gives a type Python has no
    way to take yet.
  - Qt's 'QTouchEventSequence &QTest::QTouchEventSequence::stationary(int
    touchId)': gives a type Python has no way to take yet.
  - Qt's 'QEventPoint &QTest::QTouchEventSequence::point(int touchId)': gives
    a type Python has no way to take yet.
  - Qt's 'QEventPoint &QTest::QTouchEventSequence::pointOrPreviousPoint(int
    touchId)': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QTest::QTouchEventSequence is created at the first use, not by
    'QTest::QTouchEventSequence(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTest::QTouchEventSequence back gives a copy the
    ritual made for Python, in a new cute QTest::QTouchEventSequence.
  - Each name of Qt's QTest::QTouchEventSequence that has no cute function
    yet, 'move', 'point', 'pointOrPreviousPoint', 'press', 'release',
    'stationary', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTest::QTouchEventSequence'

  #  A C++ QTest::QTouchEventSequence Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTest_QTouchEventSequence'

  #  The functions Qt calls itself that QTest::QTouchEventSequence is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'stationary': (
          'QTouchEventSequence &QTest::QTouchEventSequence::stationary(int)',
      ),
  }

  #  The functions Qt calls itself that QTest::QTouchEventSequence is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'commit': (
          ('_ZN5QTest19QTouchEventSequence6commitEb',
           ('bool', 'number', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
  }

  #  Qt's '~QTest::QTouchEventSequence()'. Naming it makes this a value
  #  class: Python owns every C++ QTest::QTouchEventSequence behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QTest19QTouchEventSequenceD1Ev'

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

  @overload(QWindow, QPointingDevice, bool)
  @overload(QWindow, NoneType, bool)
  @overload(NoneType, QPointingDevice, bool)
  @overload(NoneType, NoneType, bool)
  def __init__(
      self,
      window: Optional[QWindow],
      aDevice: Optional[QPointingDevice],
      autoCommit: bool,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QTest::QTouchEventSequence::QTouchEventSequence(QWindow *window,
    QPointingDevice *aDevice, bool autoCommit)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtest-qtoucheventsequence.html#QTouchEventSequence

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    aDevice : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    autoCommit : bool
      Passed on as it is.
    """
    #  QTest::QTouchEventSequence::QTouchEventSequence(QWindow *window,
    #      QPointingDevice *aDevice, bool autoCommit)
    self._noteCreation(QTouchEventSequence, lambda: Rituals.call(
        'ritual_ZN5QTest19QTouchEventSequenceC1EP7QWindowP15QPointingDevice'
        'b',
        self._addressOf(window), self._addressOf(aDevice), autoCommit,
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

  @overload()
  @overload(bool)
  def commit(self, processEvents: bool = True) -> bool:
    """
    Calls Qt's 'bool QTest::QTouchEventSequence::commit(bool processEvents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtest-qtoucheventsequence.html#commit

    Parameters
    ----------

    processEvents : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  bool QTest::QTouchEventSequence::commit(bool processEvents)
    ritual = 'ritual_ZN5QTest19QTouchEventSequence6commitEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QTest19QTouchEventSequence6commitEb'
    return self.uglySide.call(ritual, processEvents)

  @overload()
  @overload(bool)
  def cancel(self, processEvents: bool = True) -> bool:
    """
    Calls Qt's 'bool QTest::QTouchEventSequence::cancel(bool processEvents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtest-qtoucheventsequence.html#cancel

    Parameters
    ----------

    processEvents : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  bool QTest::QTouchEventSequence::cancel(bool processEvents)
    return self.uglySide.call(
        'ritual_ZN5QTest19QTouchEventSequence6cancelEb', processEvents,
    )

  @overload(QWindow, QPoint)
  @overload(NoneType, QPoint)
  def mapToScreen(self, window: Optional[QWindow], pt: QPoint) -> QPointF:
    """
    Calls Qt's 'QPointF QTest::QTouchEventSequence::mapToScreen(QWindow
    *window, const QPoint &pt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtest-qtoucheventsequence.html#mapToScreen

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pt : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QTest::QTouchEventSequence::mapToScreen(QWindow *window, const
    #      QPoint &pt)
    address = self.uglySide.call(
        'ritual_ZN5QTest19QTouchEventSequence11mapToScreenEP7QWindowRK6QPoi'
        'nt',
        self._addressOf(window), self._valueOf(pt),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @staticmethod
  def move(*__, **_) -> Never:
    """
    Qt's 'QTouchEventSequence &QTest::QTouchEventSequence::move(int touchId,
    const QPoint &pt, QWindow *window)': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QTest.QTouchEventSequence.move' has no cute function yet. Qt's "
        "'QTouchEventSequence &QTest::QTouchEventSequence::move(int "
        "touchId, const QPoint &pt, QWindow *window)': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def point(*__, **_) -> Never:
    """
    Qt's 'QEventPoint &QTest::QTouchEventSequence::point(int touchId)': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTest.QTouchEventSequence.point' has no cute function yet. Qt's "
        "'QEventPoint &QTest::QTouchEventSequence::point(int touchId)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def pointOrPreviousPoint(*__, **_) -> Never:
    """
    Qt's 'QEventPoint &QTest::QTouchEventSequence::pointOrPreviousPoint(int
    touchId)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTest.QTouchEventSequence.pointOrPreviousPoint' has no cute "
        "function yet. Qt's 'QEventPoint "
        "&QTest::QTouchEventSequence::pointOrPreviousPoint(int touchId)': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def press(*__, **_) -> Never:
    """
    Qt's 'QTouchEventSequence &QTest::QTouchEventSequence::press(int touchId,
    const QPoint &pt, QWindow *window)': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QTest.QTouchEventSequence.press' has no cute function yet. Qt's "
        "'QTouchEventSequence &QTest::QTouchEventSequence::press(int "
        "touchId, const QPoint &pt, QWindow *window)': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def release(*__, **_) -> Never:
    """
    Qt's 'QTouchEventSequence &QTest::QTouchEventSequence::release(int
    touchId, const QPoint &pt, QWindow *window)': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QTest.QTouchEventSequence.release' has no cute function yet. Qt's "
        "'QTouchEventSequence &QTest::QTouchEventSequence::release(int "
        "touchId, const QPoint &pt, QWindow *window)': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def stationary(*__, **_) -> Never:
    """
    Qt's 'QTouchEventSequence &QTest::QTouchEventSequence::stationary(int
    touchId)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTest.QTouchEventSequence.stationary' has no cute function yet. "
        "Qt's 'QTouchEventSequence "
        "&QTest::QTouchEventSequence::stationary(int touchId)': gives a "
        "type Python has no way to take yet.")

"""
QTimerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qtimer_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QTimerPrivate to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QTimer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTimer = WAIT['QTimer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTimerPrivate(QObjectPrivate):
  """
  The cute side of Qt's QTimerPrivate: a plain Python object standing in
  front of one C++ QTimerPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QTimerPrivate is built on
  Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTimerPrivate that has a ritual and that Python can
  call so far, 7 names in all: 'setInterval', 'isActive',
  '_qt_property_inter_offset', '_qt_property_intervalDuration_offset',
  '_qt_property_single_offset', '_qt_property_type_offset',
  '_qt_property_isActiveData_offset'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTimerPrivate::QTimerPrivate(std::chrono::nanoseconds nsec,
    QChronoTimer *qq)': takes a type Python has no way to hand over yet.
  - Qt's 'QTimerPrivate::~QTimerPrivate()': the destructor: Python never
    removes a C++ QTimerPrivate.
  - Qt's 'void QTimerPrivate::setIntervalDuration(std::chrono::nanoseconds
    nsec)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QTimerPrivate is created at the first use, not by
    'QTimerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTimerPrivate.
  - Each name of Qt's QTimerPrivate that has no cute function yet,
    'setIntervalDuration', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _qt_property_inter_offset() -> int:
    """
    Calls Qt's 'size_t QTimerPrivate::_qt_property_inter_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimerprivate.html#_qt_property_inter_offset
    """
    #  size_t QTimerPrivate::_qt_property_inter_offset()
    return Rituals.call(
        'ritual_ZN13QTimerPrivate25_qt_property_inter_offsetEv',
    )

  @staticmethod
  def _qt_property_intervalDuration_offset() -> int:
    """
    Calls Qt's 'size_t
    QTimerPrivate::_qt_property_intervalDuration_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimerprivate.html
    """
    #  size_t QTimerPrivate::_qt_property_intervalDuration_offset()
    return Rituals.call(
        'ritual_ZN13QTimerPrivate36_qt_property_intervalDuration_offsetEv',
    )

  @staticmethod
  def _qt_property_single_offset() -> int:
    """
    Calls Qt's 'size_t QTimerPrivate::_qt_property_single_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimerprivate.html#_qt_property_single_offset
    """
    #  size_t QTimerPrivate::_qt_property_single_offset()
    return Rituals.call(
        'ritual_ZN13QTimerPrivate26_qt_property_single_offsetEv',
    )

  @staticmethod
  def _qt_property_type_offset() -> int:
    """
    Calls Qt's 'size_t QTimerPrivate::_qt_property_type_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimerprivate.html#_qt_property_type_offset
    """
    #  size_t QTimerPrivate::_qt_property_type_offset()
    return Rituals.call(
        'ritual_ZN13QTimerPrivate24_qt_property_type_offsetEv',
    )

  @staticmethod
  def _qt_property_isActiveData_offset() -> int:
    """
    Calls Qt's 'size_t QTimerPrivate::_qt_property_isActiveData_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtimerprivate.html
    """
    #  size_t QTimerPrivate::_qt_property_isActiveData_offset()
    return Rituals.call(
        'ritual_ZN13QTimerPrivate32_qt_property_isActiveData_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTimerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QTimerPrivate::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimerprivate.html#isActive
    """
    #  bool QTimerPrivate::isActive() const
    return self.uglySide.call('ritual_ZNK13QTimerPrivate8isActiveEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setInterval(self, msec: int) -> None:
    """
    Calls Qt's 'void QTimerPrivate::setInterval(int msec)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimerprivate.html#setInterval

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QTimerPrivate::setInterval(int msec)
    self.uglySide.call('ritual_ZN13QTimerPrivate11setIntervalEi', msec)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTimer)
  @overload(NoneType)
  def __init__(self, qq: Optional[QTimer]) -> None:
    """
    Notes what was given, for Qt's 'QTimerPrivate::QTimerPrivate(QTimer
    *qq)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtimerprivate.html#QTimerPrivate

    Parameters
    ----------

    qq : Optional[QTimer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTimerPrivate::QTimerPrivate(QTimer *qq)
    self._noteCreation(QTimerPrivate, lambda: Rituals.call(
        'ritual_ZN13QTimerPrivateC1EP6QTimer', self._addressOf(qq),
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
  def setIntervalDuration(*__, **_) -> Never:
    """
    Qt's 'void QTimerPrivate::setIntervalDuration(std::chrono::nanoseconds
    nsec)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTimerPrivate.setIntervalDuration' has no cute function yet. Qt's "
        "'void QTimerPrivate::setIntervalDuration(std::chrono::nanoseconds "
        "nsec)': takes a type Python has no way to hand over yet.")

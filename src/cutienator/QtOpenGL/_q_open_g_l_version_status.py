"""
QOpenGLVersionStatus binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglversionfunctions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class QOpenGLVersionStatus(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLVersionStatus: a plain Python object standing
  in front of one C++ QOpenGLVersionStatus.

  C++ hands a QOpenGLVersionStatus around as a copy, so every C++
  QOpenGLVersionStatus behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLVersionStatus that has a ritual and that
  Python can call so far, 2 names in all: '__eq__', '__ne__'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLVersionStatus::~QOpenGLVersionStatus()': the destructor:
    Python removes its C++ QOpenGLVersionStatus by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpenGLVersionStatus is created at the first use, not by
    'QOpenGLVersionStatus(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLVersionStatus back gives a copy the ritual
    made for Python, in a new cute QOpenGLVersionStatus.
  """

  #  The enums Qt writes inside QOpenGLVersionStatus, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class OpenGLStatus(CuteNum):
    """
    The enum 'QOpenGLVersionStatus::OpenGLStatus' of Qt, with the 3 names Qt
    gives in it.
    """

    CoreStatus = Kee[int](0)
    DeprecatedStatus = Kee[int](1)
    InvalidStatus = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLVersionStatus'

  #  Qt's '~QOpenGLVersionStatus()'. Naming it makes this a value class:
  #  Python owns every C++ QOpenGLVersionStatus behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QOpenGLVersionStatusD1Ev'

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

  @overload(THIS)
  def __eq__(self, rhs: QOpenGLVersionStatus) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpenGLVersionStatus &lhs, const
    QOpenGLVersionStatus &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionstatus.html#operator==

    Parameters
    ----------

    rhs : QOpenGLVersionStatus
      Passed on as a value: Qt reads the C++ QOpenGLVersionStatus, which
      stays Python's own.
    """
    #  bool operator==(const QOpenGLVersionStatus &lhs, const
    #      QOpenGLVersionStatus &rhs)
    return Rituals.call(
        'ritual_ZeqRK20QOpenGLVersionStatusS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QOpenGLVersionStatus) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpenGLVersionStatus &lhs, const
    QOpenGLVersionStatus &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionstatus.html#operator!=

    Parameters
    ----------

    rhs : QOpenGLVersionStatus
      Passed on as a value: Qt reads the C++ QOpenGLVersionStatus, which
      stays Python's own.
    """
    #  bool operator!=(const QOpenGLVersionStatus &lhs, const
    #      QOpenGLVersionStatus &rhs)
    return Rituals.call(
        'ritual_ZneRK20QOpenGLVersionStatusS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLVersionStatus::QOpenGLVersionStatus()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionstatus.html#QOpenGLVersionStatus
    """
    #  QOpenGLVersionStatus::QOpenGLVersionStatus()
    self._noteCreation(QOpenGLVersionStatus, lambda: Rituals.call(
        'ritual_ZN20QOpenGLVersionStatusC1Ev',
    ))

  @overload(int, int, OpenGLStatus)
  def __init__(
      self,
      majorVersion: int,
      minorVersion: int,
      functionStatus: OpenGLStatus,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLVersionStatus::QOpenGLVersionStatus(int majorVersion, int
    minorVersion, QOpenGLVersionStatus::OpenGLStatus functionStatus)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglversionstatus.html#QOpenGLVersionStatus

    Parameters
    ----------

    majorVersion : int
      Passed on as it is.

    minorVersion : int
      Passed on as it is.

    functionStatus : OpenGLStatus
      Passed on as its number.
    """
    #  QOpenGLVersionStatus::QOpenGLVersionStatus(int majorVersion, int
    #      minorVersion, QOpenGLVersionStatus::OpenGLStatus functionStatus)
    self._noteCreation(QOpenGLVersionStatus, lambda: Rituals.call(
        'ritual_ZN20QOpenGLVersionStatusC1EiiNS_12OpenGLStatusE',
        majorVersion, minorVersion, functionStatus.value,
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

"""
QQmlSA::LoggerWarningId binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/qqmljsloggingutils.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class LoggerWarningId(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSA::LoggerWarningId: a plain Python object
  standing in front of one C++ QQmlSA::LoggerWarningId.

  C++ hands a QQmlSA::LoggerWarningId around as a copy, so every C++
  QQmlSA::LoggerWarningId behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlSA::LoggerWarningId that has a ritual and that
  Python can call so far, 3 names in all: 'name', '__eq__', '__ne__'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlSA::LoggerWarningId::~LoggerWarningId()': the destructor:
    Python removes its C++ QQmlSA::LoggerWarningId by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QQmlSA::LoggerWarningId is created at the first use, not by
    'QQmlSA::LoggerWarningId(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSA::LoggerWarningId back gives a copy the ritual
    made for Python, in a new cute QQmlSA::LoggerWarningId.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSA::LoggerWarningId'

  #  Qt's '~QQmlSA::LoggerWarningId()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlSA::LoggerWarningId behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlSA15LoggerWarningIdD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QAnyStringView QQmlSA::LoggerWarningId::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlsa-loggerwarningid.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QAnyStringView QQmlSA::LoggerWarningId::name() const
    return self.uglySide.call('ritual_ZNK6QQmlSA15LoggerWarningId4nameEv')

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
  def __eq__(self, b: LoggerWarningId) -> bool:
    """
    Calls Qt's 'bool operator==(const LoggerWarningId &a, const
    LoggerWarningId &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-loggerwarningid.html#operator==

    Parameters
    ----------

    b : LoggerWarningId
      Passed on as a value: Qt reads the C++ QQmlSA::LoggerWarningId, which
      stays Python's own.
    """
    #  bool operator==(const LoggerWarningId &a, const LoggerWarningId &b)
    return Rituals.call(
        'ritual_ZN6QQmlSAeqERKNS_15LoggerWarningIdES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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
  def __ne__(self, b: LoggerWarningId) -> bool:
    """
    Calls Qt's 'bool operator!=(const LoggerWarningId &a, const
    LoggerWarningId &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-loggerwarningid.html#operator!=

    Parameters
    ----------

    b : LoggerWarningId
      Passed on as a value: Qt reads the C++ QQmlSA::LoggerWarningId, which
      stays Python's own.
    """
    #  bool operator!=(const LoggerWarningId &a, const LoggerWarningId &b)
    return Rituals.call(
        'ritual_ZN6QQmlSAneERKNS_15LoggerWarningIdES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
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

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSA::LoggerWarningId::LoggerWarningId(QAnyStringView name)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsa-loggerwarningid.html#LoggerWarningId

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlSA::LoggerWarningId::LoggerWarningId(QAnyStringView name)
    self._noteCreation(LoggerWarningId, lambda: Rituals.call(
        'ritual_ZN6QQmlSA15LoggerWarningIdC1E14QAnyStringView', name,
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

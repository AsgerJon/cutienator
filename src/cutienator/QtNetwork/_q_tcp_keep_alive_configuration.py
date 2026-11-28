"""
QTcpKeepAliveConfiguration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qtcpkeepaliveconfiguration_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QTcpKeepAliveConfiguration to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QTcpKeepAliveConfiguration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTcpKeepAliveConfiguration: a plain Python object
  standing in front of one C++ QTcpKeepAliveConfiguration.

  C++ hands a QTcpKeepAliveConfiguration around as a copy, so every C++
  QTcpKeepAliveConfiguration behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QTcpKeepAliveConfiguration that has a ritual and
  that Python can call so far, 3 names in all: 'isEqual', '__eq__', '__ne__'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTcpKeepAliveConfiguration::~QTcpKeepAliveConfiguration()': the
    destructor: Python removes its C++ QTcpKeepAliveConfiguration by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QTcpKeepAliveConfiguration is created at the first use, not by
    'QTcpKeepAliveConfiguration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTcpKeepAliveConfiguration back gives a copy the
    ritual made for Python, in a new cute QTcpKeepAliveConfiguration.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTcpKeepAliveConfiguration'

  #  Qt's '~QTcpKeepAliveConfiguration()'. Naming it makes this a value
  #  class: Python owns every C++ QTcpKeepAliveConfiguration behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QTcpKeepAliveConfigurationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def isEqual(self, other: QTcpKeepAliveConfiguration) -> bool:
    """
    Calls Qt's 'bool QTcpKeepAliveConfiguration::isEqual(const
    QTcpKeepAliveConfiguration &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpkeepaliveconfiguration.html#isEqual

    Parameters
    ----------

    other : QTcpKeepAliveConfiguration
      Passed on as a value: Qt reads the C++ QTcpKeepAliveConfiguration,
      which stays Python's own.
    """
    #  bool QTcpKeepAliveConfiguration::isEqual(const
    #      QTcpKeepAliveConfiguration &other) const
    return self.uglySide.call(
        'ritual_ZNK26QTcpKeepAliveConfiguration7isEqualERKS_',
        self._valueOf(other),
    )

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
  def __eq__(self, rhs: QTcpKeepAliveConfiguration) -> bool:
    """
    Calls Qt's 'bool operator==(const QTcpKeepAliveConfiguration &lhs, const
    QTcpKeepAliveConfiguration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpkeepaliveconfiguration.html#operator==

    Parameters
    ----------

    rhs : QTcpKeepAliveConfiguration
      Passed on as a value: Qt reads the C++ QTcpKeepAliveConfiguration,
      which stays Python's own.
    """
    #  bool operator==(const QTcpKeepAliveConfiguration &lhs, const
    #      QTcpKeepAliveConfiguration &rhs)
    return Rituals.call(
        'ritual_ZeqRK26QTcpKeepAliveConfigurationS1_',
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
  def __ne__(self, rhs: QTcpKeepAliveConfiguration) -> bool:
    """
    Calls Qt's 'bool operator!=(const QTcpKeepAliveConfiguration &lhs, const
    QTcpKeepAliveConfiguration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtcpkeepaliveconfiguration.html#operator!=

    Parameters
    ----------

    rhs : QTcpKeepAliveConfiguration
      Passed on as a value: Qt reads the C++ QTcpKeepAliveConfiguration,
      which stays Python's own.
    """
    #  bool operator!=(const QTcpKeepAliveConfiguration &lhs, const
    #      QTcpKeepAliveConfiguration &rhs)
    return Rituals.call(
        'ritual_ZneRK26QTcpKeepAliveConfigurationS1_',
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

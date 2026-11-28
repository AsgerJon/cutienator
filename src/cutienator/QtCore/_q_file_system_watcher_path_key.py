"""
QFileSystemWatcherPathKey binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_win_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QFileSystemWatcherPathKey to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from . import QString


class QFileSystemWatcherPathKey(QString):
  """
  The cute side of Qt's QFileSystemWatcherPathKey: a plain Python object
  standing in front of one C++ QFileSystemWatcherPathKey.

  It is built on the cute 'QString', as Qt's QFileSystemWatcherPathKey is
  built on Qt's QString, and has everything that class has.

  C++ hands a QFileSystemWatcherPathKey around as a copy, so every C++
  QFileSystemWatcherPathKey behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFileSystemWatcherPathKey that has a ritual and that
  Python can call so far, 1 name in all: '__eq__'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFileSystemWatcherPathKey::~QFileSystemWatcherPathKey()': the
    destructor: Python removes its C++ QFileSystemWatcherPathKey by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QFileSystemWatcherPathKey is created at the first use, not by
    'QFileSystemWatcherPathKey(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFileSystemWatcherPathKey back gives a copy the
    ritual made for Python, in a new cute QFileSystemWatcherPathKey.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileSystemWatcherPathKey'

  #  Qt's '~QFileSystemWatcherPathKey()'. Naming it makes this a value class:
  #  Python owns every C++ QFileSystemWatcherPathKey behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QFileSystemWatcherPathKeyD1Ev'

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
  def __eq__(self, other: QFileSystemWatcherPathKey) -> bool:
    """
    Calls Qt's 'bool QFileSystemWatcherPathKey::operator==(const
    QFileSystemWatcherPathKey &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcherpathkey.html#operator==

    Parameters
    ----------

    other : QFileSystemWatcherPathKey
      Passed on as a value: Qt reads the C++ QFileSystemWatcherPathKey, which
      stays Python's own.
    """
    #  bool QFileSystemWatcherPathKey::operator==(const
    #      QFileSystemWatcherPathKey &other) const
    return self.uglySide.call(
        'ritual_ZNK25QFileSystemWatcherPathKeyeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
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
    'QFileSystemWatcherPathKey::QFileSystemWatcherPathKey()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcherpathkey.html
    """
    #  QFileSystemWatcherPathKey::QFileSystemWatcherPathKey()
    self._noteCreation(QFileSystemWatcherPathKey, lambda: Rituals.call(
        'ritual_ZN25QFileSystemWatcherPathKeyC1Ev',
    ))

  @overload(str)
  def __init__(self, other: str) -> None:
    """
    Notes what was given, for Qt's
    'QFileSystemWatcherPathKey::QFileSystemWatcherPathKey(const QString
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcherpathkey.html

    Parameters
    ----------

    other : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QFileSystemWatcherPathKey::QFileSystemWatcherPathKey(const QString
    #      &other)
    self._noteCreation(QFileSystemWatcherPathKey, lambda: Rituals.call(
        'ritual_ZN25QFileSystemWatcherPathKeyC1ERK7QString', other,
    ))

  @overload(THIS)
  def __init__(self, other: QFileSystemWatcherPathKey) -> None:
    """
    Notes what was given, for Qt's
    'QFileSystemWatcherPathKey::QFileSystemWatcherPathKey(const
    QFileSystemWatcherPathKey &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemwatcherpathkey.html

    Parameters
    ----------

    other : QFileSystemWatcherPathKey
      Passed on as a value: Qt reads the C++ QFileSystemWatcherPathKey, which
      stays Python's own.
    """
    #  QFileSystemWatcherPathKey::QFileSystemWatcherPathKey(const
    #      QFileSystemWatcherPathKey &other)
    self._noteCreation(QFileSystemWatcherPathKey, lambda: Rituals.call(
        'ritual_ZN25QFileSystemWatcherPathKeyC1ERKS_', self._valueOf(other),
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

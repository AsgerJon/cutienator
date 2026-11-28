"""
QSettingsGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qsettings_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSettingsGroup to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QSettingsGroup(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSettingsGroup: a plain Python object standing in
  front of one C++ QSettingsGroup.

  C++ hands a QSettingsGroup around as a copy, so every C++ QSettingsGroup
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSettingsGroup that has a ritual and that Python can
  call so far, 5 names in all: 'name', 'toString', 'isArray',
  'arraySizeGuess', 'setArrayIndex'. It can be made from Python, in 3 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSettingsGroup::~QSettingsGroup()': the destructor: Python removes
    its C++ QSettingsGroup by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSettingsGroup is created at the first use, not by
    'QSettingsGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSettingsGroup back gives a copy the ritual made for
    Python, in a new cute QSettingsGroup.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSettingsGroup'

  #  Qt's '~QSettingsGroup()'. Naming it makes this a value class: Python
  #  owns every C++ QSettingsGroup behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QSettingsGroupD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QSettingsGroup::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsgroup.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSettingsGroup::name() const
    return self.uglySide.call('ritual_ZNK14QSettingsGroup4nameEv')

  def toString(self) -> str:
    """
    Calls Qt's 'QString QSettingsGroup::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsgroup.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSettingsGroup::toString() const
    return self.uglySide.call('ritual_ZNK14QSettingsGroup8toStringEv')

  def isArray(self) -> bool:
    """
    Calls Qt's 'bool QSettingsGroup::isArray() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsgroup.html#isArray
    """
    #  bool QSettingsGroup::isArray() const
    return self.uglySide.call('ritual_ZNK14QSettingsGroup7isArrayEv')

  def arraySizeGuess(self) -> int:
    """
    Calls Qt's 'qsizetype QSettingsGroup::arraySizeGuess() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsgroup.html#arraySizeGuess
    """
    #  qsizetype QSettingsGroup::arraySizeGuess() const
    return self.uglySide.call('ritual_ZNK14QSettingsGroup14arraySizeGuessEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setArrayIndex(self, i: int) -> None:
    """
    Calls Qt's 'void QSettingsGroup::setArrayIndex(qsizetype i)'.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsgroup.html#setArrayIndex

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QSettingsGroup::setArrayIndex(qsizetype i)
    self.uglySide.call('ritual_ZN14QSettingsGroup13setArrayIndexEx', i)

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
    Notes what was given, for Qt's 'QSettingsGroup::QSettingsGroup()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsgroup.html#QSettingsGroup
    """
    #  QSettingsGroup::QSettingsGroup()
    self._noteCreation(QSettingsGroup, lambda: Rituals.call(
        'ritual_ZN14QSettingsGroupC1Ev',
    ))

  @overload(str)
  def __init__(self, s: str) -> None:
    """
    Notes what was given, for Qt's 'QSettingsGroup::QSettingsGroup(const
    QString &s)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsgroup.html#QSettingsGroup

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QSettingsGroup::QSettingsGroup(const QString &s)
    self._noteCreation(QSettingsGroup, lambda: Rituals.call(
        'ritual_ZN14QSettingsGroupC1ERK7QString', s,
    ))

  @overload(str, bool)
  def __init__(self, s: str, guessArraySize: bool) -> None:
    """
    Notes what was given, for Qt's 'QSettingsGroup::QSettingsGroup(const
    QString &s, bool guessArraySize)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsettingsgroup.html#QSettingsGroup

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    guessArraySize : bool
      Passed on as it is.
    """
    #  QSettingsGroup::QSettingsGroup(const QString &s, bool guessArraySize)
    self._noteCreation(QSettingsGroup, lambda: Rituals.call(
        'ritual_ZN14QSettingsGroupC1ERK7QStringb', s, guessArraySize,
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

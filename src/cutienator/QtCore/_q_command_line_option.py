"""
QCommandLineOption binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcommandlineoption.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QCommandLineOptionFlag


class QCommandLineOption(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCommandLineOption: a plain Python object standing in
  front of one C++ QCommandLineOption.

  C++ hands a QCommandLineOption around as a copy, so every C++
  QCommandLineOption behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCommandLineOption that has a ritual and that Python
  can call so far, 7 names in all: 'setValueName', 'valueName',
  'setDescription', 'description', 'setDefaultValue', 'flags', 'setFlags'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCommandLineOption::~QCommandLineOption()': the destructor: Python
    removes its C++ QCommandLineOption by it, and has no other use for it.

  What has no ritual
  ------------------

  8 of the 19 functions Qt declares: 8 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QCommandLineOption is created at the first use, not by
    'QCommandLineOption(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCommandLineOption back gives a copy the ritual made
    for Python, in a new cute QCommandLineOption.
  """

  #  The enums Qt writes inside QCommandLineOption, and the names Qt has for
  #  the combinations of its flags enums.
  Flag = QCommandLineOptionFlag
  Flags = QCommandLineOptionFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCommandLineOption'

  #  Qt's '~QCommandLineOption()'. Naming it makes this a value class: Python
  #  owns every C++ QCommandLineOption behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QCommandLineOptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def valueName(self) -> str:
    """
    Calls Qt's 'QString QCommandLineOption::valueName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineoption.html#valueName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCommandLineOption::valueName() const
    return self.uglySide.call('ritual_ZNK18QCommandLineOption9valueNameEv')

  def description(self) -> str:
    """
    Calls Qt's 'QString QCommandLineOption::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineoption.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCommandLineOption::description() const
    return self.uglySide.call(
        'ritual_ZNK18QCommandLineOption11descriptionEv',
    )

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QCommandLineOption::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineoption.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QCommandLineOption::flags() const
    return QCommandLineOption.Flags(self.uglySide.call(
        'ritual_ZNK18QCommandLineOption5flagsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setValueName(self, name: str) -> None:
    """
    Calls Qt's 'void QCommandLineOption::setValueName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineoption.html#setValueName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCommandLineOption::setValueName(const QString &name)
    self.uglySide.call(
        'ritual_ZN18QCommandLineOption12setValueNameERK7QString', name,
    )

  @overload(str)
  def setDescription(self, description: str) -> None:
    """
    Calls Qt's 'void QCommandLineOption::setDescription(const QString
    &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineoption.html#setDescription

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCommandLineOption::setDescription(const QString &description)
    self.uglySide.call(
        'ritual_ZN18QCommandLineOption14setDescriptionERK7QString',
        description,
    )

  @overload(str)
  def setDefaultValue(self, defaultValue: str) -> None:
    """
    Calls Qt's 'void QCommandLineOption::setDefaultValue(const QString
    &defaultValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineoption.html#setDefaultValue

    Parameters
    ----------

    defaultValue : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCommandLineOption::setDefaultValue(const QString &defaultValue)
    self.uglySide.call(
        'ritual_ZN18QCommandLineOption15setDefaultValueERK7QString',
        defaultValue,
    )

  @overload(Flags)
  def setFlags(self, aflags: Flags) -> None:
    """
    Calls Qt's 'void QCommandLineOption::setFlags(Flags aflags)'.

    Qt's own words: https://doc.qt.io/qt-6/qcommandlineoption.html#setFlags

    Parameters
    ----------

    aflags : Flags
      Passed on as its number.
    """
    #  void QCommandLineOption::setFlags(Flags aflags)
    self.uglySide.call(
        'ritual_ZN18QCommandLineOption8setFlagsE6QFlagsINS_4FlagEE',
        aflags.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's
    'QCommandLineOption::QCommandLineOption(const QString &name)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineoption.html#QCommandLineOption

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QCommandLineOption::QCommandLineOption(const QString &name)
    self._noteCreation(QCommandLineOption, lambda: Rituals.call(
        'ritual_ZN18QCommandLineOptionC1ERK7QString', name,
    ))

  @overload(str, str)
  @overload(str, str, str)
  @overload(str, str, str, str)
  def __init__(
      self,
      name: str,
      description: str,
      valueName: str = '',
      defaultValue: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCommandLineOption::QCommandLineOption(const QString &name, const
    QString &description, const QString &valueName, const QString
    &defaultValue)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineoption.html#QCommandLineOption

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    description : str
      Passed on as it is: a QString is made of it for the call.

    valueName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    defaultValue : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QCommandLineOption::QCommandLineOption(const QString &name, const
    #      QString &description, const QString &valueName, const QString
    #      &defaultValue)
    self._noteCreation(QCommandLineOption, lambda: Rituals.call(
        'ritual_ZN18QCommandLineOptionC1ERK7QStringS2_S2_S2_',
        name, description, valueName, defaultValue,
    ))

  @overload(THIS)
  def __init__(self, other: QCommandLineOption) -> None:
    """
    Notes what was given, for Qt's
    'QCommandLineOption::QCommandLineOption(const QCommandLineOption
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommandlineoption.html#QCommandLineOption

    Parameters
    ----------

    other : QCommandLineOption
      Passed on as a value: Qt reads the C++ QCommandLineOption, which stays
      Python's own.
    """
    #  QCommandLineOption::QCommandLineOption(const QCommandLineOption
    #      &other)
    self._noteCreation(QCommandLineOption, lambda: Rituals.call(
        'ritual_ZN18QCommandLineOptionC1ERKS_', self._valueOf(other),
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

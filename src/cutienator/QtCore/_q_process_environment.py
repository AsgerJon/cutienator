"""
QProcessEnvironment binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qprocess.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QProcessEnvironmentInitialization


class QProcessEnvironment(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QProcessEnvironment: a plain Python object standing
  in front of one C++ QProcessEnvironment.

  C++ hands a QProcessEnvironment around as a copy, so every C++
  QProcessEnvironment behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QProcessEnvironment that has a ritual and that
  Python can call so far, 8 names in all: 'isEmpty', 'inheritsFromParent',
  'clear', 'contains', 'insert', 'remove', 'value', 'systemEnvironment'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QProcessEnvironment::~QProcessEnvironment()': the destructor:
    Python removes its C++ QProcessEnvironment by it, and has no other use
    for it.

  What has no ritual
  ------------------

  5 of the 18 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QProcessEnvironment is created at the first use, not by
    'QProcessEnvironment(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QProcessEnvironment back gives a copy the ritual made
    for Python, in a new cute QProcessEnvironment.
  """

  #  The enums Qt writes inside QProcessEnvironment, and the names Qt has for
  #  the combinations of its flags enums.
  Initialization = QProcessEnvironmentInitialization

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def systemEnvironment() -> QProcessEnvironment:
    """
    Calls Qt's 'QProcessEnvironment
    QProcessEnvironment::systemEnvironment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironment.html#systemEnvironment

    Returns
    -------

    QProcessEnvironment
      A new cute QProcessEnvironment around the copy Qt gave back. Python
      owns it.
    """
    #  QProcessEnvironment QProcessEnvironment::systemEnvironment()
    address = Rituals.call(
        'ritual_ZN19QProcessEnvironment17systemEnvironmentEv',
    )
    return QProcessEnvironment._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProcessEnvironment'

  #  Qt's '~QProcessEnvironment()'. Naming it makes this a value class:
  #  Python owns every C++ QProcessEnvironment behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QProcessEnvironmentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QProcessEnvironment::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocessenvironment.html#isEmpty
    """
    #  bool QProcessEnvironment::isEmpty() const
    return self.uglySide.call('ritual_ZNK19QProcessEnvironment7isEmptyEv')

  def inheritsFromParent(self) -> bool:
    """
    Calls Qt's 'bool QProcessEnvironment::inheritsFromParent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironment.html#inheritsFromParent
    """
    #  bool QProcessEnvironment::inheritsFromParent() const
    return self.uglySide.call(
        'ritual_ZNK19QProcessEnvironment18inheritsFromParentEv',
    )

  @overload(str)
  def contains(self, name: str) -> bool:
    """
    Calls Qt's 'bool QProcessEnvironment::contains(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocessenvironment.html#contains

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QProcessEnvironment::contains(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK19QProcessEnvironment8containsERK7QString', name,
    )

  @overload(str)
  @overload(str, str)
  def value(self, name: str, defaultValue: str = '') -> str:
    """
    Calls Qt's 'QString QProcessEnvironment::value(const QString &name, const
    QString &defaultValue) const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocessenvironment.html#value

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    defaultValue : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProcessEnvironment::value(const QString &name, const QString
    #      &defaultValue) const
    return self.uglySide.call(
        'ritual_ZNK19QProcessEnvironment5valueERK7QStringS2_',
        name, defaultValue,
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QProcessEnvironment::QProcessEnvironment()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironment.html#QProcessEnvironment
    """
    #  QProcessEnvironment::QProcessEnvironment()
    self._noteCreation(QProcessEnvironment, lambda: Rituals.call(
        'ritual_ZN19QProcessEnvironmentC1Ev',
    ))

  @overload(Initialization)
  def __init__(self, a0: Initialization) -> None:
    """
    Notes what was given, for Qt's
    'QProcessEnvironment::QProcessEnvironment(Initialization a0)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironment.html#QProcessEnvironment

    Parameters
    ----------

    a0 : Initialization
      Passed on as its number.
    """
    #  QProcessEnvironment::QProcessEnvironment(Initialization a0)
    self._noteCreation(QProcessEnvironment, lambda: Rituals.call(
        'ritual_ZN19QProcessEnvironmentC1ENS_14InitializationE', a0.value,
    ))

  @overload(THIS)
  def __init__(self, other: QProcessEnvironment) -> None:
    """
    Notes what was given, for Qt's
    'QProcessEnvironment::QProcessEnvironment(const QProcessEnvironment
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironment.html#QProcessEnvironment

    Parameters
    ----------

    other : QProcessEnvironment
      Passed on as a value: Qt reads the C++ QProcessEnvironment, which stays
      Python's own.
    """
    #  QProcessEnvironment::QProcessEnvironment(const QProcessEnvironment
    #      &other)
    self._noteCreation(QProcessEnvironment, lambda: Rituals.call(
        'ritual_ZN19QProcessEnvironmentC1ERKS_', self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QProcessEnvironment::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qprocessenvironment.html#clear
    """
    #  void QProcessEnvironment::clear()
    self.uglySide.call('ritual_ZN19QProcessEnvironment5clearEv')

  @overload(str, str)
  def insert(self, name: str, value: str) -> None:
    """
    Calls Qt's 'void QProcessEnvironment::insert(const QString &name, const
    QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocessenvironment.html#insert

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QProcessEnvironment::insert(const QString &name, const QString
    #      &value)
    self.uglySide.call(
        'ritual_ZN19QProcessEnvironment6insertERK7QStringS2_', name, value,
    )

  @overload(THIS)
  def insert(self, e: QProcessEnvironment) -> None:
    """
    Calls Qt's 'void QProcessEnvironment::insert(const QProcessEnvironment
    &e)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocessenvironment.html#insert

    Parameters
    ----------

    e : QProcessEnvironment
      Passed on as a value: Qt reads the C++ QProcessEnvironment, which stays
      Python's own.
    """
    #  void QProcessEnvironment::insert(const QProcessEnvironment &e)
    self.uglySide.call(
        'ritual_ZN19QProcessEnvironment6insertERKS_', self._valueOf(e),
    )

  @overload(str)
  def remove(self, name: str) -> None:
    """
    Calls Qt's 'void QProcessEnvironment::remove(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qprocessenvironment.html#remove

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QProcessEnvironment::remove(const QString &name)
    self.uglySide.call(
        'ritual_ZN19QProcessEnvironment6removeERK7QString', name,
    )

"""
QProcEnvValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qprocess_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QProcEnvValue to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QProcEnvValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QProcEnvValue: a plain Python object standing in
  front of one C++ QProcEnvValue.

  C++ hands a QProcEnvValue around as a copy, so every C++ QProcEnvValue
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QProcEnvValue that has a ritual and that Python can
  call so far, 3 names in all: '__eq__', 'bytes', 'string'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QProcEnvValue::~QProcEnvValue()': the destructor: Python removes
    its C++ QProcEnvValue by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QProcEnvValue is created at the first use, not by
    'QProcEnvValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QProcEnvValue back gives a copy the ritual made for
    Python, in a new cute QProcEnvValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProcEnvValue'

  #  Qt's '~QProcEnvValue()'. Naming it makes this a value class: Python owns
  #  every C++ QProcEnvValue behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QProcEnvValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def bytes(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QProcEnvValue::bytes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocenvvalue.html#bytes

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QProcEnvValue::bytes() const
    address = self.uglySide.call('ritual_ZNK13QProcEnvValue5bytesEv')
    from . import QByteArray
    return QByteArray._cuteOwning(address)

  def string(self) -> str:
    """
    Calls Qt's 'QString QProcEnvValue::string() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocenvvalue.html#string

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProcEnvValue::string() const
    return self.uglySide.call('ritual_ZNK13QProcEnvValue6stringEv')

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
  def __eq__(self, other: QProcEnvValue) -> bool:
    """
    Calls Qt's 'bool QProcEnvValue::operator==(const QProcEnvValue &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocenvvalue.html#operator==

    Parameters
    ----------

    other : QProcEnvValue
      Passed on as a value: Qt reads the C++ QProcEnvValue, which stays
      Python's own.
    """
    #  bool QProcEnvValue::operator==(const QProcEnvValue &other) const
    return self.uglySide.call(
        'ritual_ZNK13QProcEnvValueeqERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's 'QProcEnvValue::QProcEnvValue()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qprocenvvalue.html#QProcEnvValue
    """
    #  QProcEnvValue::QProcEnvValue()
    self._noteCreation(QProcEnvValue, lambda: Rituals.call(
        'ritual_ZN13QProcEnvValueC1Ev',
    ))

  @overload(str)
  def __init__(self, value: str) -> None:
    """
    Notes what was given, for Qt's 'QProcEnvValue::QProcEnvValue(const
    QString &value)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qprocenvvalue.html#QProcEnvValue

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QProcEnvValue::QProcEnvValue(const QString &value)
    self._noteCreation(QProcEnvValue, lambda: Rituals.call(
        'ritual_ZN13QProcEnvValueC1ERK7QString', value,
    ))

  @overload(QByteArray)
  def __init__(self, value: QByteArray) -> None:
    """
    Notes what was given, for Qt's 'QProcEnvValue::QProcEnvValue(const
    QByteArray &value)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qprocenvvalue.html#QProcEnvValue

    Parameters
    ----------

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  QProcEnvValue::QProcEnvValue(const QByteArray &value)
    self._noteCreation(QProcEnvValue, lambda: Rituals.call(
        'ritual_ZN13QProcEnvValueC1ERK10QByteArray', self._valueOf(value),
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

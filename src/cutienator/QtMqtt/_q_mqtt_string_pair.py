"""
QMqttStringPair binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMqtt/qmqtttype.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QMqttStringPair(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMqttStringPair: a plain Python object standing in
  front of one C++ QMqttStringPair.

  C++ hands a QMqttStringPair around as a copy, so every C++ QMqttStringPair
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMqttStringPair that has a ritual and that Python
  can call so far, 6 names in all: 'name', 'setName', 'value', 'setValue',
  '__eq__', '__ne__'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMqttStringPair::~QMqttStringPair()': the destructor: Python
    removes its C++ QMqttStringPair by it, and has no other use for it.
  - Qt's 'QMqttStringPair &QMqttStringPair::operator=(const QMqttStringPair
    &a0)': assignment: Python binds a name and has no operator for it.

  What to expect
  --------------

  - The C++ QMqttStringPair is created at the first use, not by
    'QMqttStringPair(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMqttStringPair back gives a copy the ritual made for
    Python, in a new cute QMqttStringPair.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMqttStringPair'

  #  Qt's '~QMqttStringPair()'. Naming it makes this a value class: Python
  #  owns every C++ QMqttStringPair behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QMqttStringPairD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QMqttStringPair::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttstringpair.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttStringPair::name() const
    return self.uglySide.call('ritual_ZNK15QMqttStringPair4nameEv')

  def value(self) -> str:
    """
    Calls Qt's 'QString QMqttStringPair::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttstringpair.html#value

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMqttStringPair::value() const
    return self.uglySide.call('ritual_ZNK15QMqttStringPair5valueEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, n: str) -> None:
    """
    Calls Qt's 'void QMqttStringPair::setName(const QString &n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttstringpair.html#setName

    Parameters
    ----------

    n : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttStringPair::setName(const QString &n)
    self.uglySide.call('ritual_ZN15QMqttStringPair7setNameERK7QString', n)

  @overload(str)
  def setValue(self, v: str) -> None:
    """
    Calls Qt's 'void QMqttStringPair::setValue(const QString &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttstringpair.html#setValue

    Parameters
    ----------

    v : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMqttStringPair::setValue(const QString &v)
    self.uglySide.call('ritual_ZN15QMqttStringPair8setValueERK7QString', v)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QMqttStringPair) -> bool:
    """
    Calls Qt's 'bool QMqttStringPair::operator==(const QMqttStringPair
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttstringpair.html#operator==

    Parameters
    ----------

    other : QMqttStringPair
      Passed on as a value: Qt reads the C++ QMqttStringPair, which stays
      Python's own.
    """
    #  bool QMqttStringPair::operator==(const QMqttStringPair &other) const
    return self.uglySide.call(
        'ritual_ZNK15QMqttStringPaireqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QMqttStringPair) -> bool:
    """
    Calls Qt's 'bool QMqttStringPair::operator!=(const QMqttStringPair
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmqttstringpair.html#operator!=

    Parameters
    ----------

    other : QMqttStringPair
      Passed on as a value: Qt reads the C++ QMqttStringPair, which stays
      Python's own.
    """
    #  bool QMqttStringPair::operator!=(const QMqttStringPair &other) const
    return self.uglySide.call(
        'ritual_ZNK15QMqttStringPairneERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's 'QMqttStringPair::QMqttStringPair()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttstringpair.html#QMqttStringPair
    """
    #  QMqttStringPair::QMqttStringPair()
    self._noteCreation(QMqttStringPair, lambda: Rituals.call(
        'ritual_ZN15QMqttStringPairC1Ev',
    ))

  @overload(str, str)
  def __init__(self, name: str, value: str) -> None:
    """
    Notes what was given, for Qt's 'QMqttStringPair::QMqttStringPair(const
    QString &name, const QString &value)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttstringpair.html#QMqttStringPair

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QMqttStringPair::QMqttStringPair(const QString &name, const QString
    #      &value)
    self._noteCreation(QMqttStringPair, lambda: Rituals.call(
        'ritual_ZN15QMqttStringPairC1ERK7QStringS2_', name, value,
    ))

  @overload(THIS)
  def __init__(self, a0: QMqttStringPair) -> None:
    """
    Notes what was given, for Qt's 'QMqttStringPair::QMqttStringPair(const
    QMqttStringPair &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmqttstringpair.html#QMqttStringPair

    Parameters
    ----------

    a0 : QMqttStringPair
      Passed on as a value: Qt reads the C++ QMqttStringPair, which stays
      Python's own.
    """
    #  QMqttStringPair::QMqttStringPair(const QMqttStringPair &a0)
    self._noteCreation(QMqttStringPair, lambda: Rituals.call(
        'ritual_ZN15QMqttStringPairC1ERKS_', self._valueOf(a0),
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

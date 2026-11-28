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
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals
from . import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


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
  Python can call so far, 12 names in all: 'isEmpty', 'inheritsFromParent',
  'clear', 'contains', 'insert', 'remove', 'value', 'toStringList', 'keys',
  'systemEnvironment', '__eq__', '__ne__'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QProcessEnvironment::~QProcessEnvironment()': the destructor:
    Python removes its C++ QProcessEnvironment by it, and has no other use
    for it.
  - Qt's 'QProcessEnvironment
    &QProcessEnvironment::operator=(QProcessEnvironment &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QProcessEnvironment &QProcessEnvironment::operator=(const
    QProcessEnvironment &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'void QProcessEnvironment::swap(QProcessEnvironment &other)': takes
    a type Python has no way to hand over yet.

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
  - Each name of Qt's QProcessEnvironment that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QProcessEnvironment, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Initialization(CuteNum):
    """
    The enum 'QProcessEnvironment::Initialization' of Qt, with the 1 names Qt
    gives in it.
    """

    InheritFromParent = Kee[int](0)

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

  def toStringList(self) -> QStringList:
    """
    Calls Qt's 'QStringList QProcessEnvironment::toStringList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironment.html#toStringList

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QProcessEnvironment::toStringList() const
    address = self.uglySide.call(
        'ritual_ZNK19QProcessEnvironment12toStringListEv',
    )
    return QStringList._cuteOwning(address)

  def keys(self) -> QStringList:
    """
    Calls Qt's 'QStringList QProcessEnvironment::keys() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprocessenvironment.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QProcessEnvironment::keys() const
    address = self.uglySide.call('ritual_ZNK19QProcessEnvironment4keysEv')
    return QStringList._cuteOwning(address)

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
  def __eq__(self, rhs: QProcessEnvironment) -> bool:
    """
    Calls Qt's 'bool operator==(const QProcessEnvironment &lhs, const
    QProcessEnvironment &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironment.html#operator==

    Parameters
    ----------

    rhs : QProcessEnvironment
      Passed on as a value: Qt reads the C++ QProcessEnvironment, which stays
      Python's own.
    """
    #  bool operator==(const QProcessEnvironment &lhs, const
    #      QProcessEnvironment &rhs)
    return Rituals.call(
        'ritual_ZeqRK19QProcessEnvironmentS1_',
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
  def __ne__(self, rhs: QProcessEnvironment) -> bool:
    """
    Calls Qt's 'bool operator!=(const QProcessEnvironment &lhs, const
    QProcessEnvironment &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprocessenvironment.html#operator!=

    Parameters
    ----------

    rhs : QProcessEnvironment
      Passed on as a value: Qt reads the C++ QProcessEnvironment, which stays
      Python's own.
    """
    #  bool operator!=(const QProcessEnvironment &lhs, const
    #      QProcessEnvironment &rhs)
    return Rituals.call(
        'ritual_ZneRK19QProcessEnvironmentS1_',
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QProcessEnvironment::swap(QProcessEnvironment &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QProcessEnvironment.swap' has no cute function yet. Qt's 'void "
        "QProcessEnvironment::swap(QProcessEnvironment &other)': takes a "
        "type Python has no way to hand over yet.")

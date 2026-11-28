"""
QHttp1Configuration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qhttp1configuration.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QHttp1Configuration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttp1Configuration: a plain Python object standing
  in front of one C++ QHttp1Configuration.

  C++ hands a QHttp1Configuration around as a copy, so every C++
  QHttp1Configuration behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttp1Configuration that has a ritual and that
  Python can call so far, 6 names in all: 'setNumberOfConnectionsPerHost',
  'numberOfConnectionsPerHost', 'equals', 'hash', '__eq__', '__ne__'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttp1Configuration::QHttp1Configuration(QHttp1Configuration
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QHttp1Configuration &QHttp1Configuration::operator=(const
    QHttp1Configuration &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QHttp1Configuration
    &QHttp1Configuration::operator=(QHttp1Configuration &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QHttp1Configuration::~QHttp1Configuration()': the destructor:
    Python removes its C++ QHttp1Configuration by it, and has no other use
    for it.
  - Qt's 'void QHttp1Configuration::swap(QHttp1Configuration &other)': takes
    a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QHttp1Configuration is created at the first use, not by
    'QHttp1Configuration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttp1Configuration back gives a copy the ritual made
    for Python, in a new cute QHttp1Configuration.
  - Each name of Qt's QHttp1Configuration that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttp1Configuration'

  #  Qt's '~QHttp1Configuration()'. Naming it makes this a value class:
  #  Python owns every C++ QHttp1Configuration behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QHttp1ConfigurationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def numberOfConnectionsPerHost(self) -> int:
    """
    Calls Qt's 'qsizetype QHttp1Configuration::numberOfConnectionsPerHost()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp1configuration.html
    """
    #  qsizetype QHttp1Configuration::numberOfConnectionsPerHost() const
    return self.uglySide.call(
        'ritual_ZNK19QHttp1Configuration26numberOfConnectionsPerHostEv',
    )

  @overload(THIS)
  def equals(self, other: QHttp1Configuration) -> bool:
    """
    Calls Qt's 'bool QHttp1Configuration::equals(const QHttp1Configuration
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp1configuration.html#equals

    Parameters
    ----------

    other : QHttp1Configuration
      Passed on as a value: Qt reads the C++ QHttp1Configuration, which stays
      Python's own.
    """
    #  bool QHttp1Configuration::equals(const QHttp1Configuration &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QHttp1Configuration6equalsERKS_', self._valueOf(other),
    )

  @overload(int)
  def hash(self, seed: int) -> int:
    """
    Calls Qt's 'size_t QHttp1Configuration::hash(size_t seed) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp1configuration.html#hash

    Parameters
    ----------

    seed : int
      Passed on as it is.
    """
    #  size_t QHttp1Configuration::hash(size_t seed) const
    return self.uglySide.call('ritual_ZNK19QHttp1Configuration4hashEm', seed)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setNumberOfConnectionsPerHost(self, amount: int) -> None:
    """
    Calls Qt's 'void
    QHttp1Configuration::setNumberOfConnectionsPerHost(qsizetype amount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp1configuration.html

    Parameters
    ----------

    amount : int
      Passed on as it is.
    """
    #  void QHttp1Configuration::setNumberOfConnectionsPerHost(qsizetype
    #      amount)
    self.uglySide.call(
        'ritual_ZN19QHttp1Configuration29setNumberOfConnectionsPerHostEx',
        amount,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QHttp1Configuration) -> bool:
    """
    Calls Qt's 'bool operator==(const QHttp1Configuration &lhs, const
    QHttp1Configuration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp1configuration.html#operator==

    Parameters
    ----------

    rhs : QHttp1Configuration
      Passed on as a value: Qt reads the C++ QHttp1Configuration, which stays
      Python's own.
    """
    #  bool operator==(const QHttp1Configuration &lhs, const
    #      QHttp1Configuration &rhs)
    return Rituals.call(
        'ritual_ZeqRK19QHttp1ConfigurationS1_',
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
  def __ne__(self, rhs: QHttp1Configuration) -> bool:
    """
    Calls Qt's 'bool operator!=(const QHttp1Configuration &lhs, const
    QHttp1Configuration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp1configuration.html#operator!=

    Parameters
    ----------

    rhs : QHttp1Configuration
      Passed on as a value: Qt reads the C++ QHttp1Configuration, which stays
      Python's own.
    """
    #  bool operator!=(const QHttp1Configuration &lhs, const
    #      QHttp1Configuration &rhs)
    return Rituals.call(
        'ritual_ZneRK19QHttp1ConfigurationS1_',
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
    'QHttp1Configuration::QHttp1Configuration()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp1configuration.html#QHttp1Configuration
    """
    #  QHttp1Configuration::QHttp1Configuration()
    self._noteCreation(QHttp1Configuration, lambda: Rituals.call(
        'ritual_ZN19QHttp1ConfigurationC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QHttp1Configuration) -> None:
    """
    Notes what was given, for Qt's
    'QHttp1Configuration::QHttp1Configuration(const QHttp1Configuration
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp1configuration.html#QHttp1Configuration

    Parameters
    ----------

    other : QHttp1Configuration
      Passed on as a value: Qt reads the C++ QHttp1Configuration, which stays
      Python's own.
    """
    #  QHttp1Configuration::QHttp1Configuration(const QHttp1Configuration
    #      &other)
    self._noteCreation(QHttp1Configuration, lambda: Rituals.call(
        'ritual_ZN19QHttp1ConfigurationC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QHttp1Configuration::swap(QHttp1Configuration &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttp1Configuration.swap' has no cute function yet. Qt's 'void "
        "QHttp1Configuration::swap(QHttp1Configuration &other)': takes a "
        "type Python has no way to hand over yet.")

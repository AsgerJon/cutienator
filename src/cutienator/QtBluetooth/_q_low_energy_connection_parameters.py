"""
QLowEnergyConnectionParameters binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qlowenergyconnectionparameters.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QLowEnergyConnectionParameters(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLowEnergyConnectionParameters: a plain Python object
  standing in front of one C++ QLowEnergyConnectionParameters.

  C++ hands a QLowEnergyConnectionParameters around as a copy, so every C++
  QLowEnergyConnectionParameters behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QLowEnergyConnectionParameters that has a ritual and
  that Python can call so far, 10 names in all: '__eq__', '__ne__',
  'setIntervalRange', 'minimumInterval', 'maximumInterval', 'setLatency',
  'latency', 'setSupervisionTimeout', 'supervisionTimeout', 'equals'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLowEnergyConnectionParameters::~QLowEnergyConnectionParameters()':
    the destructor: Python removes its C++ QLowEnergyConnectionParameters by
    it, and has no other use for it.
  - Qt's 'QLowEnergyConnectionParameters
    &QLowEnergyConnectionParameters::operator=(const
    QLowEnergyConnectionParameters &other)': assignment: Python binds a name
    and has no operator for it.
  - Qt's 'void
    QLowEnergyConnectionParameters::swap(QLowEnergyConnectionParameters
    &other)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QLowEnergyConnectionParameters is created at the first use, not
    by 'QLowEnergyConnectionParameters(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLowEnergyConnectionParameters back gives a copy the
    ritual made for Python, in a new cute QLowEnergyConnectionParameters.
  - Each name of Qt's QLowEnergyConnectionParameters that has no cute
    function yet, 'swap', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(
      a: QLowEnergyConnectionParameters,
      b: QLowEnergyConnectionParameters,
  ) -> bool:
    """
    Calls Qt's 'bool QLowEnergyConnectionParameters::equals(const
    QLowEnergyConnectionParameters &a, const QLowEnergyConnectionParameters
    &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyconnectionparameters.html#equals

    Parameters
    ----------

    a : QLowEnergyConnectionParameters
      Passed on as a value: Qt reads the C++ QLowEnergyConnectionParameters,
      which stays Python's own.

    b : QLowEnergyConnectionParameters
      Passed on as a value: Qt reads the C++ QLowEnergyConnectionParameters,
      which stays Python's own.
    """
    #  bool QLowEnergyConnectionParameters::equals(const
    #      QLowEnergyConnectionParameters &a, const
    #      QLowEnergyConnectionParameters &b)
    return Rituals.call(
        'ritual_ZN30QLowEnergyConnectionParameters6equalsERKS_S1_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLowEnergyConnectionParameters'

  #  Qt's '~QLowEnergyConnectionParameters()'. Naming it makes this a value
  #  class: Python owns every C++ QLowEnergyConnectionParameters behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QLowEnergyConnectionParametersD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def minimumInterval(self) -> float:
    """
    Calls Qt's 'double QLowEnergyConnectionParameters::minimumInterval()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyconnectionparameters.html
    """
    #  double QLowEnergyConnectionParameters::minimumInterval() const
    return self.uglySide.call(
        'ritual_ZNK30QLowEnergyConnectionParameters15minimumIntervalEv',
    )

  def maximumInterval(self) -> float:
    """
    Calls Qt's 'double QLowEnergyConnectionParameters::maximumInterval()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyconnectionparameters.html
    """
    #  double QLowEnergyConnectionParameters::maximumInterval() const
    return self.uglySide.call(
        'ritual_ZNK30QLowEnergyConnectionParameters15maximumIntervalEv',
    )

  def latency(self) -> int:
    """
    Calls Qt's 'int QLowEnergyConnectionParameters::latency() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyconnectionparameters.html#latency
    """
    #  int QLowEnergyConnectionParameters::latency() const
    return self.uglySide.call(
        'ritual_ZNK30QLowEnergyConnectionParameters7latencyEv',
    )

  def supervisionTimeout(self) -> int:
    """
    Calls Qt's 'int QLowEnergyConnectionParameters::supervisionTimeout()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyconnectionparameters.html
    """
    #  int QLowEnergyConnectionParameters::supervisionTimeout() const
    return self.uglySide.call(
        'ritual_ZNK30QLowEnergyConnectionParameters18supervisionTimeoutEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float)
  def setIntervalRange(self, minimum: float, maximum: float) -> None:
    """
    Calls Qt's 'void QLowEnergyConnectionParameters::setIntervalRange(double
    minimum, double maximum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyconnectionparameters.html

    Parameters
    ----------

    minimum : float
      Passed on as it is.

    maximum : float
      Passed on as it is.
    """
    #  void QLowEnergyConnectionParameters::setIntervalRange(double minimum,
    #      double maximum)
    self.uglySide.call(
        'ritual_ZN30QLowEnergyConnectionParameters16setIntervalRangeEdd',
        minimum, maximum,
    )

  @overload(int)
  def setLatency(self, latency: int) -> None:
    """
    Calls Qt's 'void QLowEnergyConnectionParameters::setLatency(int
    latency)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyconnectionparameters.html#setLatency

    Parameters
    ----------

    latency : int
      Passed on as it is.
    """
    #  void QLowEnergyConnectionParameters::setLatency(int latency)
    self.uglySide.call(
        'ritual_ZN30QLowEnergyConnectionParameters10setLatencyEi', latency,
    )

  @overload(int)
  def setSupervisionTimeout(self, timeout: int) -> None:
    """
    Calls Qt's 'void
    QLowEnergyConnectionParameters::setSupervisionTimeout(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyconnectionparameters.html

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void QLowEnergyConnectionParameters::setSupervisionTimeout(int
    #      timeout)
    self.uglySide.call(
        'ritual_ZN30QLowEnergyConnectionParameters21setSupervisionTimeoutEi',
        timeout,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QLowEnergyConnectionParameters) -> bool:
    """
    Calls Qt's 'bool operator==(const QLowEnergyConnectionParameters &a,
    const QLowEnergyConnectionParameters &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyconnectionparameters.html#operator==

    Parameters
    ----------

    b : QLowEnergyConnectionParameters
      Passed on as a value: Qt reads the C++ QLowEnergyConnectionParameters,
      which stays Python's own.
    """
    #  bool operator==(const QLowEnergyConnectionParameters &a, const
    #      QLowEnergyConnectionParameters &b)
    return Rituals.call(
        'ritual_ZeqRK30QLowEnergyConnectionParametersS1_',
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
  def __ne__(self, b: QLowEnergyConnectionParameters) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLowEnergyConnectionParameters &a,
    const QLowEnergyConnectionParameters &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyconnectionparameters.html#operator!=

    Parameters
    ----------

    b : QLowEnergyConnectionParameters
      Passed on as a value: Qt reads the C++ QLowEnergyConnectionParameters,
      which stays Python's own.
    """
    #  bool operator!=(const QLowEnergyConnectionParameters &a, const
    #      QLowEnergyConnectionParameters &b)
    return Rituals.call(
        'ritual_ZneRK30QLowEnergyConnectionParametersS1_',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QLowEnergyConnectionParameters::QLowEnergyConnectionParameters()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyconnectionparameters.html
    """
    #  QLowEnergyConnectionParameters::QLowEnergyConnectionParameters()
    self._noteCreation(QLowEnergyConnectionParameters, lambda: Rituals.call(
        'ritual_ZN30QLowEnergyConnectionParametersC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLowEnergyConnectionParameters) -> None:
    """
    Notes what was given, for Qt's
    'QLowEnergyConnectionParameters::QLowEnergyConnectionParameters(const
    QLowEnergyConnectionParameters &other)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyconnectionparameters.html

    Parameters
    ----------

    other : QLowEnergyConnectionParameters
      Passed on as a value: Qt reads the C++ QLowEnergyConnectionParameters,
      which stays Python's own.
    """
    #  QLowEnergyConnectionParameters::QLowEnergyConnectionParameters(const
    #      QLowEnergyConnectionParameters &other)
    self._noteCreation(QLowEnergyConnectionParameters, lambda: Rituals.call(
        'ritual_ZN30QLowEnergyConnectionParametersC1ERKS_',
        self._valueOf(other),
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
    Qt's 'void
    QLowEnergyConnectionParameters::swap(QLowEnergyConnectionParameters
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLowEnergyConnectionParameters.swap' has no cute function yet. "
        "Qt's 'void "
        "QLowEnergyConnectionParameters::swap(QLowEnergyConnectionParameters"
        " &other)': takes a type Python has no way to hand over yet.")

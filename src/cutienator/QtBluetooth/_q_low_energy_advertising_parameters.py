"""
QLowEnergyAdvertisingParameters binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qlowenergyadvertisingparameters.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QLowEnergyController

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QBluetoothAddress


class QLowEnergyAdvertisingParameters(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLowEnergyAdvertisingParameters: a plain Python
  object standing in front of one C++ QLowEnergyAdvertisingParameters.

  C++ hands a QLowEnergyAdvertisingParameters around as a copy, so every C++
  QLowEnergyAdvertisingParameters behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QLowEnergyAdvertisingParameters that has a ritual
  and that Python can call so far, 9 names in all: '__eq__', '__ne__',
  'setMode', 'mode', 'filterPolicy', 'setInterval', 'minimumInterval',
  'maximumInterval', 'equals'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QLowEnergyAdvertisingParameters::~QLowEnergyAdvertisingParameters()':
    the destructor: Python removes its C++ QLowEnergyAdvertisingParameters by
    it, and has no other use for it.
  - Qt's 'QLowEnergyAdvertisingParameters
    &QLowEnergyAdvertisingParameters::operator=(const
    QLowEnergyAdvertisingParameters &other)': assignment: Python binds a name
    and has no operator for it.
  - Qt's 'void QLowEnergyAdvertisingParameters::setWhiteList(const
    QList<AddressInfo> &whiteList, FilterPolicy policy)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QList<AddressInfo> QLowEnergyAdvertisingParameters::whiteList()
    const': gives a type Python has no way to take yet.
  - Qt's 'void
    QLowEnergyAdvertisingParameters::swap(QLowEnergyAdvertisingParameters
    &other)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QLowEnergyAdvertisingParameters is created at the first use, not
    by 'QLowEnergyAdvertisingParameters(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLowEnergyAdvertisingParameters back gives a copy the
    ritual made for Python, in a new cute QLowEnergyAdvertisingParameters.
  - Each name of Qt's QLowEnergyAdvertisingParameters that has no cute
    function yet, 'setWhiteList', 'swap', 'whiteList', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QLowEnergyAdvertisingParameters, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class FilterPolicy(CuteNum):
    """
    The enum 'QLowEnergyAdvertisingParameters::FilterPolicy' of Qt, with the
    4 names Qt gives in it.
    """

    IgnoreWhiteList = Kee[int](0)
    UseWhiteListForScanning = Kee[int](1)
    UseWhiteListForConnecting = Kee[int](2)
    UseWhiteListForScanningAndConnecting = Kee[int](3)

  class Mode(CuteNum):
    """
    The enum 'QLowEnergyAdvertisingParameters::Mode' of Qt, with the 3 names
    Qt gives in it.
    """

    AdvInd = Kee[int](0)
    AdvScanInd = Kee[int](2)
    AdvNonConnInd = Kee[int](3)

  #  The classes Qt writes inside QLowEnergyAdvertisingParameters, each a
  #  class in here as in C++.

  class AddressInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLowEnergyAdvertisingParameters::AddressInfo: a
    plain Python object standing in front of one C++
    QLowEnergyAdvertisingParameters::AddressInfo.

    C++ hands a QLowEnergyAdvertisingParameters::AddressInfo around as a
    copy, so every C++ QLowEnergyAdvertisingParameters::AddressInfo behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QLowEnergyAdvertisingParameters::AddressInfo that
    has a ritual and that Python can call so far, 3 names in all: '__eq__',
    '__ne__', 'equals'. It can be made from Python, in 2 ways; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QLowEnergyAdvertisingParameters::AddressInfo::~AddressInfo()':
      the destructor: Python removes its C++
      QLowEnergyAdvertisingParameters::AddressInfo by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QLowEnergyAdvertisingParameters::AddressInfo is created at the
      first use, not by 'QLowEnergyAdvertisingParameters::AddressInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLowEnergyAdvertisingParameters::AddressInfo back
      gives a copy the ritual made for Python, in a new cute
      QLowEnergyAdvertisingParameters::AddressInfo.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QBluetoothAddress = WAIT['QBluetoothAddress']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(THIS, THIS)
    def equals(
        a: QLowEnergyAdvertisingParameters.AddressInfo,
        b: QLowEnergyAdvertisingParameters.AddressInfo,
    ) -> bool:
      """
      Calls Qt's 'bool
      QLowEnergyAdvertisingParameters::AddressInfo::equals(const AddressInfo
      &a, const AddressInfo &b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlowenergyadvertisingparameters-addressinfo.html

      Parameters
      ----------

      a : QLowEnergyAdvertisingParameters.AddressInfo
        Passed on as a value: Qt reads the C++
        QLowEnergyAdvertisingParameters::AddressInfo, which stays Python's
        own.

      b : QLowEnergyAdvertisingParameters.AddressInfo
        Passed on as a value: Qt reads the C++
        QLowEnergyAdvertisingParameters::AddressInfo, which stays Python's
        own.
      """
      #  bool QLowEnergyAdvertisingParameters::AddressInfo::equals(const
      #      AddressInfo &a, const AddressInfo &b)
      return Rituals.call(
          'ritual_ZN31QLowEnergyAdvertisingParameters11AddressInfo6equalsER'
          'KS0_S2_',
          CuteMixin._valueOf(a), CuteMixin._valueOf(b),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLowEnergyAdvertisingParameters::AddressInfo'

    #  Qt's '~QLowEnergyAdvertisingParameters::AddressInfo()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QLowEnergyAdvertisingParameters::AddressInfo behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN31QLowEnergyAdvertisingParameters11AddressInfoD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __eq__(self, b: QLowEnergyAdvertisingParameters.AddressInfo) -> bool:
      """
      Calls Qt's 'bool operator==(const AddressInfo &a, const AddressInfo
      &b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlowenergyadvertisingparameters-addressinfo.html

      Parameters
      ----------

      b : QLowEnergyAdvertisingParameters.AddressInfo
        Passed on as a value: Qt reads the C++
        QLowEnergyAdvertisingParameters::AddressInfo, which stays Python's
        own.
      """
      #  bool operator==(const AddressInfo &a, const AddressInfo &b)
      return Rituals.call(
          'ritual_ZeqRKN31QLowEnergyAdvertisingParameters11AddressInfoES2_',
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
    def __ne__(self, b: QLowEnergyAdvertisingParameters.AddressInfo) -> bool:
      """
      Calls Qt's 'bool operator!=(const AddressInfo &a, const AddressInfo
      &b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qlowenergyadvertisingparameters-addressinfo.html

      Parameters
      ----------

      b : QLowEnergyAdvertisingParameters.AddressInfo
        Passed on as a value: Qt reads the C++
        QLowEnergyAdvertisingParameters::AddressInfo, which stays Python's
        own.
      """
      #  bool operator!=(const AddressInfo &a, const AddressInfo &b)
      return Rituals.call(
          'ritual_ZneRKN31QLowEnergyAdvertisingParameters11AddressInfoES2_',
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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QBluetoothAddress, QLowEnergyController.RemoteAddressType)
    def __init__(
        self,
        addr: QBluetoothAddress,
        t: QLowEnergyController.RemoteAddressType,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QLowEnergyAdvertisingParameters::AddressInfo::AddressInfo(const
      QBluetoothAddress &addr, QLowEnergyController::RemoteAddressType t)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qlowenergyadvertisingparameters-addressinfo.html

      Parameters
      ----------

      addr : QBluetoothAddress
        Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
        Python's own.

      t : QLowEnergyController.RemoteAddressType
        Passed on as its number.
      """
      #  QLowEnergyAdvertisingParameters::AddressInfo::AddressInfo(const
      #      QBluetoothAddress &addr, QLowEnergyController::RemoteAddressType
      #      t)
      self._noteCreation(
          QLowEnergyAdvertisingParameters.AddressInfo, lambda: Rituals.call(
              'ritual_ZN31QLowEnergyAdvertisingParameters11AddressInfoC1ERK'
              '17QBluetoothAddressN20QLowEnergyController17RemoteAddressTyp'
              'eE',
              self._valueOf(addr), t.value,
          ))

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QLowEnergyAdvertisingParameters::AddressInfo::AddressInfo()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qlowenergyadvertisingparameters-addressinfo.html
      """
      #  QLowEnergyAdvertisingParameters::AddressInfo::AddressInfo()
      self._noteCreation(
          QLowEnergyAdvertisingParameters.AddressInfo, lambda: Rituals.call(
              'ritual_ZN31QLowEnergyAdvertisingParameters11AddressInfoC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(
      a: QLowEnergyAdvertisingParameters,
      b: QLowEnergyAdvertisingParameters,
  ) -> bool:
    """
    Calls Qt's 'bool QLowEnergyAdvertisingParameters::equals(const
    QLowEnergyAdvertisingParameters &a, const QLowEnergyAdvertisingParameters
    &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingparameters.html#equals

    Parameters
    ----------

    a : QLowEnergyAdvertisingParameters
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingParameters,
      which stays Python's own.

    b : QLowEnergyAdvertisingParameters
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingParameters,
      which stays Python's own.
    """
    #  bool QLowEnergyAdvertisingParameters::equals(const
    #      QLowEnergyAdvertisingParameters &a, const
    #      QLowEnergyAdvertisingParameters &b)
    return Rituals.call(
        'ritual_ZN31QLowEnergyAdvertisingParameters6equalsERKS_S1_',
        CuteMixin._valueOf(a), CuteMixin._valueOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLowEnergyAdvertisingParameters'

  #  Qt's '~QLowEnergyAdvertisingParameters()'. Naming it makes this a value
  #  class: Python owns every C++ QLowEnergyAdvertisingParameters behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QLowEnergyAdvertisingParametersD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def mode(self) -> Mode:
    """
    Calls Qt's 'Mode QLowEnergyAdvertisingParameters::mode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingparameters.html#mode

    Returns
    -------

    Mode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Mode(number)' gives.
    """
    #  Mode QLowEnergyAdvertisingParameters::mode() const
    return QLowEnergyAdvertisingParameters.Mode(self.uglySide.call(
        'ritual_ZNK31QLowEnergyAdvertisingParameters4modeEv',
    ))

  def filterPolicy(self) -> FilterPolicy:
    """
    Calls Qt's 'FilterPolicy QLowEnergyAdvertisingParameters::filterPolicy()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingparameters.html#filterPolicy

    Returns
    -------

    FilterPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FilterPolicy(number)'
      gives.
    """
    #  FilterPolicy QLowEnergyAdvertisingParameters::filterPolicy() const
    return QLowEnergyAdvertisingParameters.FilterPolicy(self.uglySide.call(
        'ritual_ZNK31QLowEnergyAdvertisingParameters12filterPolicyEv',
    ))

  def minimumInterval(self) -> int:
    """
    Calls Qt's 'int QLowEnergyAdvertisingParameters::minimumInterval()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingparameters.html
    """
    #  int QLowEnergyAdvertisingParameters::minimumInterval() const
    return self.uglySide.call(
        'ritual_ZNK31QLowEnergyAdvertisingParameters15minimumIntervalEv',
    )

  def maximumInterval(self) -> int:
    """
    Calls Qt's 'int QLowEnergyAdvertisingParameters::maximumInterval()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingparameters.html
    """
    #  int QLowEnergyAdvertisingParameters::maximumInterval() const
    return self.uglySide.call(
        'ritual_ZNK31QLowEnergyAdvertisingParameters15maximumIntervalEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Mode)
  def setMode(self, mode: Mode) -> None:
    """
    Calls Qt's 'void QLowEnergyAdvertisingParameters::setMode(Mode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingparameters.html#setMode

    Parameters
    ----------

    mode : Mode
      Passed on as its number.
    """
    #  void QLowEnergyAdvertisingParameters::setMode(Mode mode)
    self.uglySide.call(
        'ritual_ZN31QLowEnergyAdvertisingParameters7setModeENS_4ModeE',
        mode.value,
    )

  @overload(int, int)
  def setInterval(self, minimum: int, maximum: int) -> None:
    """
    Calls Qt's 'void QLowEnergyAdvertisingParameters::setInterval(quint16
    minimum, quint16 maximum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingparameters.html#setInterval

    Parameters
    ----------

    minimum : int
      Passed on as it is.

    maximum : int
      Passed on as it is.
    """
    #  void QLowEnergyAdvertisingParameters::setInterval(quint16 minimum,
    #      quint16 maximum)
    self.uglySide.call(
        'ritual_ZN31QLowEnergyAdvertisingParameters11setIntervalEtt',
        minimum, maximum,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QLowEnergyAdvertisingParameters) -> bool:
    """
    Calls Qt's 'bool operator==(const QLowEnergyAdvertisingParameters &a,
    const QLowEnergyAdvertisingParameters &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingparameters.html#operator==

    Parameters
    ----------

    b : QLowEnergyAdvertisingParameters
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingParameters,
      which stays Python's own.
    """
    #  bool operator==(const QLowEnergyAdvertisingParameters &a, const
    #      QLowEnergyAdvertisingParameters &b)
    return Rituals.call(
        'ritual_ZeqRK31QLowEnergyAdvertisingParametersS1_',
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
  def __ne__(self, b: QLowEnergyAdvertisingParameters) -> bool:
    """
    Calls Qt's 'bool operator!=(const QLowEnergyAdvertisingParameters &a,
    const QLowEnergyAdvertisingParameters &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingparameters.html#operator!=

    Parameters
    ----------

    b : QLowEnergyAdvertisingParameters
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingParameters,
      which stays Python's own.
    """
    #  bool operator!=(const QLowEnergyAdvertisingParameters &a, const
    #      QLowEnergyAdvertisingParameters &b)
    return Rituals.call(
        'ritual_ZneRK31QLowEnergyAdvertisingParametersS1_',
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
    'QLowEnergyAdvertisingParameters::QLowEnergyAdvertisingParameters()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingparameters.html
    """
    #  QLowEnergyAdvertisingParameters::QLowEnergyAdvertisingParameters()
    self._noteCreation(QLowEnergyAdvertisingParameters, lambda: Rituals.call(
        'ritual_ZN31QLowEnergyAdvertisingParametersC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLowEnergyAdvertisingParameters) -> None:
    """
    Notes what was given, for Qt's
    'QLowEnergyAdvertisingParameters::QLowEnergyAdvertisingParameters(const
    QLowEnergyAdvertisingParameters &other)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyadvertisingparameters.html

    Parameters
    ----------

    other : QLowEnergyAdvertisingParameters
      Passed on as a value: Qt reads the C++ QLowEnergyAdvertisingParameters,
      which stays Python's own.
    """
    #  QLowEnergyAdvertisingParameters::QLowEnergyAdvertisingParameters(const
    #      QLowEnergyAdvertisingParameters &other)
    self._noteCreation(QLowEnergyAdvertisingParameters, lambda: Rituals.call(
        'ritual_ZN31QLowEnergyAdvertisingParametersC1ERKS_',
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
  def setWhiteList(*__, **_) -> Never:
    """
    Qt's 'void QLowEnergyAdvertisingParameters::setWhiteList(const
    QList<AddressInfo> &whiteList, FilterPolicy policy)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLowEnergyAdvertisingParameters.setWhiteList' has no cute "
        "function yet. Qt's 'void "
        "QLowEnergyAdvertisingParameters::setWhiteList(const "
        "QList<AddressInfo> &whiteList, FilterPolicy policy)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void
    QLowEnergyAdvertisingParameters::swap(QLowEnergyAdvertisingParameters
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLowEnergyAdvertisingParameters.swap' has no cute function yet. "
        "Qt's 'void "
        "QLowEnergyAdvertisingParameters::swap(QLowEnergyAdvertisingParamete"
        "rs &other)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def whiteList(*__, **_) -> Never:
    """
    Qt's 'QList<AddressInfo> QLowEnergyAdvertisingParameters::whiteList()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLowEnergyAdvertisingParameters.whiteList' has no cute function "
        "yet. Qt's 'QList<AddressInfo> "
        "QLowEnergyAdvertisingParameters::whiteList() const': gives a type "
        "Python has no way to take yet.")

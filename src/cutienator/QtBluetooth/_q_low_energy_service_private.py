"""
QLowEnergyServicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/qlowenergyserviceprivate_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QLowEnergyServicePrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..QtCore import QObject
from . import QLowEnergyService

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QLowEnergyCharacteristic, QLowEnergyDescriptor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QLowEnergyCharacteristic = WAIT['QLowEnergyCharacteristic']
  QLowEnergyDescriptor = WAIT['QLowEnergyDescriptor']


class QLowEnergyServicePrivate(QObject):
  """
  The cute side of Qt's QLowEnergyServicePrivate: a plain Python object
  standing in front of one C++ QLowEnergyServicePrivate.

  It is built on the cute 'QObject', as Qt's QLowEnergyServicePrivate is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QLowEnergyServicePrivate that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'stateChanged',
  'errorOccurred', 'characteristicChanged', 'characteristicRead',
  'characteristicWritten', 'descriptorRead', 'descriptorWritten'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLowEnergyServicePrivate::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QLowEnergyServicePrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QLowEnergyServicePrivate::~QLowEnergyServicePrivate()': the
    destructor: Python never removes a C++ QLowEnergyServicePrivate.

  What has no ritual
  ------------------

  7 of the 18 functions Qt declares: 5 leans on 'QLowEnergyServicePrivate; 2
  not a gap.

  What to expect
  --------------

  - The C++ QLowEnergyServicePrivate is created at the first use, not by
    'QLowEnergyServicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLowEnergyServicePrivate.
  - Qt tells when it has removed the C++ QLowEnergyServicePrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QLowEnergyServicePrivate that has no cute function yet,
    '__init__', 'setController', 'setError', 'setState', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QLowEnergyServicePrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class GattAttributeTypes(CuteNum):
    """
    The enum 'QLowEnergyServicePrivate::GattAttributeTypes' of Qt, with the 4
    names Qt gives in it.
    """

    PrimaryService = Kee[int](10240)
    SecondaryService = Kee[int](10241)
    IncludeAttribute = Kee[int](10242)
    Characteristic = Kee[int](10243)

  #  The classes Qt writes inside QLowEnergyServicePrivate, each a class in
  #  here as in C++.

  class CharData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLowEnergyServicePrivate::CharData: a plain Python
    object standing in front of one C++ QLowEnergyServicePrivate::CharData.

    C++ hands a QLowEnergyServicePrivate::CharData around as a copy, so every
    C++ QLowEnergyServicePrivate::CharData behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QLowEnergyServicePrivate::CharData yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QLowEnergyServicePrivate::CharData::~CharData()': the destructor:
      Python removes its C++ QLowEnergyServicePrivate::CharData by it, and
      has no other use for it.

    What to expect
    --------------

    - The C++ QLowEnergyServicePrivate::CharData is created at the first use,
      not by 'QLowEnergyServicePrivate::CharData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLowEnergyServicePrivate::CharData back gives a
      copy the ritual made for Python, in a new cute
      QLowEnergyServicePrivate::CharData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLowEnergyServicePrivate::CharData'

    #  Qt's '~QLowEnergyServicePrivate::CharData()'. Naming it makes this a
    #  value class: Python owns every C++ QLowEnergyServicePrivate::CharData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN24QLowEnergyServicePrivate8CharDataD1Ev'

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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  class DescData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLowEnergyServicePrivate::DescData: a plain Python
    object standing in front of one C++ QLowEnergyServicePrivate::DescData.

    C++ hands a QLowEnergyServicePrivate::DescData around as a copy, so every
    C++ QLowEnergyServicePrivate::DescData behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QLowEnergyServicePrivate::DescData yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QLowEnergyServicePrivate::DescData::~DescData()': the destructor:
      Python removes its C++ QLowEnergyServicePrivate::DescData by it, and
      has no other use for it.

    What to expect
    --------------

    - The C++ QLowEnergyServicePrivate::DescData is created at the first use,
      not by 'QLowEnergyServicePrivate::DescData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLowEnergyServicePrivate::DescData back gives a
      copy the ritual made for Python, in a new cute
      QLowEnergyServicePrivate::DescData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLowEnergyServicePrivate::DescData'

    #  Qt's '~QLowEnergyServicePrivate::DescData()'. Naming it makes this a
    #  value class: Python owns every C++ QLowEnergyServicePrivate::DescData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN24QLowEnergyServicePrivate8DescDataD1Ev'

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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLowEnergyServicePrivate'

  #  A C++ QLowEnergyServicePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLowEnergyServicePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QLowEnergyServicePrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyserviceprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLowEnergyServicePrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QLowEnergyServicePrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QLowEnergyServicePrivate::QLowEnergyServicePrivate(QObject
    *parent)': leans on
    'QLowEnergyServicePrivate::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyServicePrivate.__init__' has no cute function yet. Qt's "
        "'QLowEnergyServicePrivate::QLowEnergyServicePrivate(QObject "
        "*parent)': leans on "
        "'QLowEnergyServicePrivate::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(QLowEnergyService.ServiceState)
  def stateChanged(self, newState: QLowEnergyService.ServiceState) -> None:
    """
    Calls Qt's 'void
    QLowEnergyServicePrivate::stateChanged(QLowEnergyService::ServiceState
    newState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyserviceprivate.html#stateChanged

    Parameters
    ----------

    newState : QLowEnergyService.ServiceState
      Passed on as its number.
    """
    #  void QLowEnergyServicePrivate::stateChanged(QLowEnergyService::
    #      ServiceState newState)
    self.uglySide.call(
        'ritual_ZN24QLowEnergyServicePrivate12stateChangedEN17QLowEnergySer'
        'vice12ServiceStateE',
        newState.value,
    )

  @overload(QLowEnergyService.ServiceError)
  def errorOccurred(self, error: QLowEnergyService.ServiceError) -> None:
    """
    Calls Qt's 'void
    QLowEnergyServicePrivate::errorOccurred(QLowEnergyService::ServiceError
    error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyserviceprivate.html#errorOccurred

    Parameters
    ----------

    error : QLowEnergyService.ServiceError
      Passed on as its number.
    """
    #  void QLowEnergyServicePrivate::errorOccurred(QLowEnergyService::
    #      ServiceError error)
    self.uglySide.call(
        'ritual_ZN24QLowEnergyServicePrivate13errorOccurredEN17QLowEnergySe'
        'rvice12ServiceErrorE',
        error.value,
    )

  @overload(QLowEnergyCharacteristic, QByteArray)
  def characteristicChanged(
      self,
      characteristic: QLowEnergyCharacteristic,
      newValue: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyServicePrivate::characteristicChanged(const
    QLowEnergyCharacteristic &characteristic, const QByteArray &newValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyserviceprivate.html

    Parameters
    ----------

    characteristic : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.

    newValue : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyServicePrivate::characteristicChanged(const
    #      QLowEnergyCharacteristic &characteristic, const QByteArray
    #      &newValue)
    self.uglySide.call(
        'ritual_ZN24QLowEnergyServicePrivate21characteristicChangedERK24QLo'
        'wEnergyCharacteristicRK10QByteArray',
        self._valueOf(characteristic), self._valueOf(newValue),
    )

  @overload(QLowEnergyCharacteristic, QByteArray)
  def characteristicRead(
      self,
      info: QLowEnergyCharacteristic,
      value: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyServicePrivate::characteristicRead(const
    QLowEnergyCharacteristic &info, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyserviceprivate.html#characteristicRead

    Parameters
    ----------

    info : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyServicePrivate::characteristicRead(const
    #      QLowEnergyCharacteristic &info, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN24QLowEnergyServicePrivate18characteristicReadERK24QLowEn'
        'ergyCharacteristicRK10QByteArray',
        self._valueOf(info), self._valueOf(value),
    )

  @overload(QLowEnergyCharacteristic, QByteArray)
  def characteristicWritten(
      self,
      characteristic: QLowEnergyCharacteristic,
      newValue: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyServicePrivate::characteristicWritten(const
    QLowEnergyCharacteristic &characteristic, const QByteArray &newValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyserviceprivate.html

    Parameters
    ----------

    characteristic : QLowEnergyCharacteristic
      Passed on as a value: Qt reads the C++ QLowEnergyCharacteristic, which
      stays Python's own.

    newValue : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyServicePrivate::characteristicWritten(const
    #      QLowEnergyCharacteristic &characteristic, const QByteArray
    #      &newValue)
    self.uglySide.call(
        'ritual_ZN24QLowEnergyServicePrivate21characteristicWrittenERK24QLo'
        'wEnergyCharacteristicRK10QByteArray',
        self._valueOf(characteristic), self._valueOf(newValue),
    )

  @overload(QLowEnergyDescriptor, QByteArray)
  def descriptorRead(
      self,
      info: QLowEnergyDescriptor,
      value: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyServicePrivate::descriptorRead(const
    QLowEnergyDescriptor &info, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyserviceprivate.html#descriptorRead

    Parameters
    ----------

    info : QLowEnergyDescriptor
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptor, which
      stays Python's own.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyServicePrivate::descriptorRead(const
    #      QLowEnergyDescriptor &info, const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN24QLowEnergyServicePrivate14descriptorReadERK20QLowEnergy'
        'DescriptorRK10QByteArray',
        self._valueOf(info), self._valueOf(value),
    )

  @overload(QLowEnergyDescriptor, QByteArray)
  def descriptorWritten(
      self,
      descriptor: QLowEnergyDescriptor,
      newValue: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QLowEnergyServicePrivate::descriptorWritten(const
    QLowEnergyDescriptor &descriptor, const QByteArray &newValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlowenergyserviceprivate.html#descriptorWritten

    Parameters
    ----------

    descriptor : QLowEnergyDescriptor
      Passed on as a value: Qt reads the C++ QLowEnergyDescriptor, which
      stays Python's own.

    newValue : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLowEnergyServicePrivate::descriptorWritten(const
    #      QLowEnergyDescriptor &descriptor, const QByteArray &newValue)
    self.uglySide.call(
        'ritual_ZN24QLowEnergyServicePrivate17descriptorWrittenERK20QLowEne'
        'rgyDescriptorRK10QByteArray',
        self._valueOf(descriptor), self._valueOf(newValue),
    )

  @staticmethod
  def setController(*__, **_) -> Never:
    """
    Qt's 'void
    QLowEnergyServicePrivate::setController(QLowEnergyControllerPrivate
    *control)': leans on
    'QLowEnergyServicePrivate::stateChanged(QLowEnergyService::
    ServiceState)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyServicePrivate.setController' has no cute function yet. "
        "Qt's 'void "
        "QLowEnergyServicePrivate::setController(QLowEnergyControllerPrivate"
        " *control)': leans on "
        "'QLowEnergyServicePrivate::stateChanged(QLowEnergyService::ServiceS"
        "tate)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def setError(*__, **_) -> Never:
    """
    Qt's 'void
    QLowEnergyServicePrivate::setError(QLowEnergyService::ServiceError
    newError)': leans on
    'QLowEnergyServicePrivate::errorOccurred(QLowEnergyService::
    ServiceError)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyServicePrivate.setError' has no cute function yet. Qt's "
        "'void "
        "QLowEnergyServicePrivate::setError(QLowEnergyService::ServiceError "
        "newError)': leans on "
        "'QLowEnergyServicePrivate::errorOccurred(QLowEnergyService::Service"
        "Error)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def setState(*__, **_) -> Never:
    """
    Qt's 'void
    QLowEnergyServicePrivate::setState(QLowEnergyService::ServiceState
    newState)': leans on
    'QLowEnergyServicePrivate::stateChanged(QLowEnergyService::
    ServiceState)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QLowEnergyServicePrivate.setState' has no cute function yet. Qt's "
        "'void "
        "QLowEnergyServicePrivate::setState(QLowEnergyService::ServiceState "
        "newState)': leans on "
        "'QLowEnergyServicePrivate::stateChanged(QLowEnergyService::ServiceS"
        "tate)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

"""
QBluetoothServiceInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/qbluetoothserviceinfo.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QBluetoothUuid

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug, QVariant
  from . import QBluetoothAddress, QBluetoothDeviceInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothAddress = WAIT['QBluetoothAddress']
  QBluetoothDeviceInfo = WAIT['QBluetoothDeviceInfo']
  QDebug = WAIT['QDebug']
  QVariant = WAIT['QVariant']


class QBluetoothServiceInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBluetoothServiceInfo: a plain Python object standing
  in front of one C++ QBluetoothServiceInfo.

  C++ hands a QBluetoothServiceInfo around as a copy, so every C++
  QBluetoothServiceInfo behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QBluetoothServiceInfo that has a ritual and that
  Python can call so far, 28 names in all: 'isValid', 'isComplete',
  'setDevice', 'device', 'setAttribute', 'attribute', 'contains',
  'removeAttribute', 'setServiceName', 'serviceName',
  'setServiceDescription', 'serviceDescription', 'setServiceProvider',
  'serviceProvider', 'socketProtocol', 'protocolServiceMultiplexer',
  'serverChannel', 'protocolDescriptor', 'setServiceAvailability',
  'serviceAvailability', 'setServiceUuid', 'serviceUuid',
  'serviceClassUuids', 'isRegistered', 'registerService',
  'unregisterService', '__rlshift__', 'streamingOperator'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBluetoothServiceInfo::~QBluetoothServiceInfo()': the destructor:
    Python removes its C++ QBluetoothServiceInfo by it, and has no other use
    for it.
  - Qt's 'QList<quint16> QBluetoothServiceInfo::attributes() const': gives a
    type Python has no way to take yet.
  - Qt's 'QBluetoothServiceInfo &QBluetoothServiceInfo::operator=(const
    QBluetoothServiceInfo &other)': assignment: Python binds a name and has
    no operator for it.

  What to expect
  --------------

  - The C++ QBluetoothServiceInfo is created at the first use, not by
    'QBluetoothServiceInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QBluetoothServiceInfo back gives a copy the ritual
    made for Python, in a new cute QBluetoothServiceInfo.
  - Each name of Qt's QBluetoothServiceInfo that has no cute function yet,
    'attributes', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QBluetoothServiceInfo, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class AttributeId(CuteNum):
    """
    The enum 'QBluetoothServiceInfo::AttributeId' of Qt, with the 18 names Qt
    gives in it.
    """

    ServiceRecordHandle = Kee[int](0)
    ServiceClassIds = Kee[int](1)
    ServiceRecordState = Kee[int](2)
    ServiceId = Kee[int](3)
    ProtocolDescriptorList = Kee[int](4)
    BrowseGroupList = Kee[int](5)
    LanguageBaseAttributeIdList = Kee[int](6)
    ServiceInfoTimeToLive = Kee[int](7)
    ServiceAvailability = Kee[int](8)
    BluetoothProfileDescriptorList = Kee[int](9)
    DocumentationUrl = Kee[int](10)
    ClientExecutableUrl = Kee[int](11)
    IconUrl = Kee[int](12)
    AdditionalProtocolDescriptorList = Kee[int](13)
    PrimaryLanguageBase = Kee[int](256)
    ServiceName = Kee[int](256)
    ServiceDescription = Kee[int](257)
    ServiceProvider = Kee[int](258)

  class Protocol(CuteNum):
    """
    The enum 'QBluetoothServiceInfo::Protocol' of Qt, with the 3 names Qt
    gives in it.
    """

    UnknownProtocol = Kee[int](0)
    L2capProtocol = Kee[int](1)
    RfcommProtocol = Kee[int](2)

  #  The classes Qt writes inside QBluetoothServiceInfo, each a class in here
  #  as in C++.

  class Alternative(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QBluetoothServiceInfo::Alternative: a plain Python
    object standing in front of one C++ QBluetoothServiceInfo::Alternative.

    C++ hands a QBluetoothServiceInfo::Alternative around as a copy, so every
    C++ QBluetoothServiceInfo::Alternative behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QBluetoothServiceInfo::Alternative yet. It can be
    made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QBluetoothServiceInfo::Alternative::~Alternative()': the
      destructor: Python removes its C++ QBluetoothServiceInfo::Alternative
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QBluetoothServiceInfo::Alternative is created at the first use,
      not by 'QBluetoothServiceInfo::Alternative(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QBluetoothServiceInfo::Alternative back gives a
      copy the ritual made for Python, in a new cute
      QBluetoothServiceInfo::Alternative.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QVariant = WAIT['QVariant']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QBluetoothServiceInfo::Alternative'

    #  Qt's '~QBluetoothServiceInfo::Alternative()'. Naming it makes this a
    #  value class: Python owns every C++ QBluetoothServiceInfo::Alternative
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QBluetoothServiceInfo11AlternativeD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QBluetoothServiceInfo::Alternative::Alternative()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qbluetoothserviceinfo-alternative.html
      """
      #  QBluetoothServiceInfo::Alternative::Alternative()
      self._noteCreation(
          QBluetoothServiceInfo.Alternative, lambda: Rituals.call(
              'ritual_ZN21QBluetoothServiceInfo11AlternativeC1Ev',
          ))

    @overload(QList[QVariant])
    def __init__(self, list: QList[QVariant]) -> None:
      """
      Notes what was given, for Qt's
      'QBluetoothServiceInfo::Alternative::Alternative(const QList<QVariant>
      &list)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qbluetoothserviceinfo-alternative.html

      Parameters
      ----------

      list : QList[QVariant]
        Passed on as a list of Qt: Qt reads the C++ list, which stays
        Python's own. A list or tuple of Python is made into one first, and
        refused when an element does not fit.
      """
      #  QBluetoothServiceInfo::Alternative::Alternative(const
      #      QList<QVariant> &list)
      self._noteCreation(
          QBluetoothServiceInfo.Alternative, lambda: Rituals.call(
              'ritual_ZN21QBluetoothServiceInfo11AlternativeC1ERK5QListI8QV'
              'ariantE',
              self._valueOf(list),
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

  class Sequence(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QBluetoothServiceInfo::Sequence: a plain Python
    object standing in front of one C++ QBluetoothServiceInfo::Sequence.

    C++ hands a QBluetoothServiceInfo::Sequence around as a copy, so every
    C++ QBluetoothServiceInfo::Sequence behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QBluetoothServiceInfo::Sequence yet. It can be made
    from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QBluetoothServiceInfo::Sequence::~Sequence()': the destructor:
      Python removes its C++ QBluetoothServiceInfo::Sequence by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QBluetoothServiceInfo::Sequence is created at the first use,
      not by 'QBluetoothServiceInfo::Sequence(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QBluetoothServiceInfo::Sequence back gives a copy
      the ritual made for Python, in a new cute
      QBluetoothServiceInfo::Sequence.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QVariant = WAIT['QVariant']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QBluetoothServiceInfo::Sequence'

    #  Qt's '~QBluetoothServiceInfo::Sequence()'. Naming it makes this a
    #  value class: Python owns every C++ QBluetoothServiceInfo::Sequence
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QBluetoothServiceInfo8SequenceD1Ev'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QBluetoothServiceInfo::Sequence::Sequence()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qbluetoothserviceinfo-sequence.html#Sequence
      """
      #  QBluetoothServiceInfo::Sequence::Sequence()
      self._noteCreation(
          QBluetoothServiceInfo.Sequence, lambda: Rituals.call(
              'ritual_ZN21QBluetoothServiceInfo8SequenceC1Ev',
          ))

    @overload(QList[QVariant])
    def __init__(self, list: QList[QVariant]) -> None:
      """
      Notes what was given, for Qt's
      'QBluetoothServiceInfo::Sequence::Sequence(const QList<QVariant>
      &list)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qbluetoothserviceinfo-sequence.html#Sequence

      Parameters
      ----------

      list : QList[QVariant]
        Passed on as a list of Qt: Qt reads the C++ list, which stays
        Python's own. A list or tuple of Python is made into one first, and
        refused when an element does not fit.
      """
      #  QBluetoothServiceInfo::Sequence::Sequence(const QList<QVariant>
      #      &list)
      self._noteCreation(
          QBluetoothServiceInfo.Sequence, lambda: Rituals.call(
              'ritual_ZN21QBluetoothServiceInfo8SequenceC1ERK5QListI8QVaria'
              'ntE',
              self._valueOf(list),
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
  @overload(QDebug, THIS)
  def streamingOperator(a0: QDebug, a1: QBluetoothServiceInfo) -> QDebug:
    """
    Calls Qt's 'QDebug QBluetoothServiceInfo::streamingOperator(QDebug a0,
    const QBluetoothServiceInfo &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#streamingOperator

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    a1 : QBluetoothServiceInfo
      Passed on as a value: Qt reads the C++ QBluetoothServiceInfo, which
      stays Python's own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QBluetoothServiceInfo::streamingOperator(QDebug a0, const
    #      QBluetoothServiceInfo &a1)
    address = Rituals.call(
        'ritual_ZN21QBluetoothServiceInfo17streamingOperatorE6QDebugRKS_',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(a1),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothServiceInfo'

  #  Qt's '~QBluetoothServiceInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QBluetoothServiceInfo behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QBluetoothServiceInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothServiceInfo::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#isValid
    """
    #  bool QBluetoothServiceInfo::isValid() const
    return self.uglySide.call('ritual_ZNK21QBluetoothServiceInfo7isValidEv')

  def isComplete(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothServiceInfo::isComplete() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#isComplete
    """
    #  bool QBluetoothServiceInfo::isComplete() const
    return self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo10isCompleteEv',
    )

  def device(self) -> QBluetoothDeviceInfo:
    """
    Calls Qt's 'QBluetoothDeviceInfo QBluetoothServiceInfo::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#device

    Returns
    -------

    QBluetoothDeviceInfo
      A new cute QBluetoothDeviceInfo around the copy Qt gave back. Python
      owns it.
    """
    #  QBluetoothDeviceInfo QBluetoothServiceInfo::device() const
    address = self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo6deviceEv',
    )
    from . import QBluetoothDeviceInfo
    return QBluetoothDeviceInfo._cuteOwning(address)

  @overload(int)
  def attribute(self, attributeId: int) -> QVariant:
    """
    Calls Qt's 'QVariant QBluetoothServiceInfo::attribute(quint16
    attributeId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#attribute

    Parameters
    ----------

    attributeId : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QBluetoothServiceInfo::attribute(quint16 attributeId) const
    address = self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo9attributeEt', attributeId,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def contains(self, attributeId: int) -> bool:
    """
    Calls Qt's 'bool QBluetoothServiceInfo::contains(quint16 attributeId)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#contains

    Parameters
    ----------

    attributeId : int
      Passed on as it is.
    """
    #  bool QBluetoothServiceInfo::contains(quint16 attributeId) const
    return self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo8containsEt', attributeId,
    )

  def serviceName(self) -> str:
    """
    Calls Qt's 'QString QBluetoothServiceInfo::serviceName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serviceName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothServiceInfo::serviceName() const
    return self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo11serviceNameEv',
    )

  def serviceDescription(self) -> str:
    """
    Calls Qt's 'QString QBluetoothServiceInfo::serviceDescription() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serviceDescription

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothServiceInfo::serviceDescription() const
    return self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo18serviceDescriptionEv',
    )

  def serviceProvider(self) -> str:
    """
    Calls Qt's 'QString QBluetoothServiceInfo::serviceProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serviceProvider

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QBluetoothServiceInfo::serviceProvider() const
    return self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo15serviceProviderEv',
    )

  def socketProtocol(self) -> Protocol:
    """
    Calls Qt's 'QBluetoothServiceInfo::Protocol
    QBluetoothServiceInfo::socketProtocol() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#socketProtocol

    Returns
    -------

    Protocol
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Protocol(number)' gives.
    """
    #  QBluetoothServiceInfo::Protocol
    #      QBluetoothServiceInfo::socketProtocol() const
    return QBluetoothServiceInfo.Protocol(self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo14socketProtocolEv',
    ))

  def protocolServiceMultiplexer(self) -> int:
    """
    Calls Qt's 'int QBluetoothServiceInfo::protocolServiceMultiplexer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html
    """
    #  int QBluetoothServiceInfo::protocolServiceMultiplexer() const
    return self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo26protocolServiceMultiplexerEv',
    )

  def serverChannel(self) -> int:
    """
    Calls Qt's 'int QBluetoothServiceInfo::serverChannel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serverChannel
    """
    #  int QBluetoothServiceInfo::serverChannel() const
    return self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo13serverChannelEv',
    )

  @overload(QBluetoothUuid.ProtocolUuid)
  def protocolDescriptor(
      self,
      protocol: QBluetoothUuid.ProtocolUuid,
  ) -> Sequence:
    """
    Calls Qt's 'QBluetoothServiceInfo::Sequence
    QBluetoothServiceInfo::protocolDescriptor(QBluetoothUuid::ProtocolUuid
    protocol) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#protocolDescriptor

    Parameters
    ----------

    protocol : QBluetoothUuid.ProtocolUuid
      Passed on as its number.

    Returns
    -------

    Sequence
      A new cute QBluetoothServiceInfo::Sequence around the copy Qt gave
      back. Python owns it.
    """
    #  QBluetoothServiceInfo::Sequence
    #      QBluetoothServiceInfo::protocolDescriptor(QBluetoothUuid::
    #      ProtocolUuid protocol) const
    address = self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo18protocolDescriptorEN14QBluetoot'
        'hUuid12ProtocolUuidE',
        protocol.value,
    )
    return QBluetoothServiceInfo.Sequence._cuteOwning(address)

  def serviceAvailability(self) -> int:
    """
    Calls Qt's 'quint8 QBluetoothServiceInfo::serviceAvailability() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serviceAvailability
    """
    #  quint8 QBluetoothServiceInfo::serviceAvailability() const
    return self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo19serviceAvailabilityEv',
    )

  def serviceUuid(self) -> QBluetoothUuid:
    """
    Calls Qt's 'QBluetoothUuid QBluetoothServiceInfo::serviceUuid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serviceUuid

    Returns
    -------

    QBluetoothUuid
      A new cute QBluetoothUuid around the copy Qt gave back. Python owns it.
    """
    #  QBluetoothUuid QBluetoothServiceInfo::serviceUuid() const
    address = self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo11serviceUuidEv',
    )
    return QBluetoothUuid._cuteOwning(address)

  def serviceClassUuids(self) -> QList[QBluetoothUuid]:
    """
    Calls Qt's 'QList<QBluetoothUuid>
    QBluetoothServiceInfo::serviceClassUuids() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#serviceClassUuids

    Returns
    -------

    QList[QBluetoothUuid]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QBluetoothUuid> QBluetoothServiceInfo::serviceClassUuids() const
    address = self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo17serviceClassUuidsEv',
    )
    return QList[QBluetoothUuid]._cuteOwning(address)

  def isRegistered(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothServiceInfo::isRegistered() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#isRegistered
    """
    #  bool QBluetoothServiceInfo::isRegistered() const
    return self.uglySide.call(
        'ritual_ZNK21QBluetoothServiceInfo12isRegisteredEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBluetoothDeviceInfo)
  def setDevice(self, info: QBluetoothDeviceInfo) -> None:
    """
    Calls Qt's 'void QBluetoothServiceInfo::setDevice(const
    QBluetoothDeviceInfo &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setDevice

    Parameters
    ----------

    info : QBluetoothDeviceInfo
      Passed on as a value: Qt reads the C++ QBluetoothDeviceInfo, which
      stays Python's own.
    """
    #  void QBluetoothServiceInfo::setDevice(const QBluetoothDeviceInfo
    #      &info)
    self.uglySide.call(
        'ritual_ZN21QBluetoothServiceInfo9setDeviceERK20QBluetoothDeviceInf'
        'o',
        self._valueOf(info),
    )

  @overload(int, QVariant)
  def setAttribute(self, attributeId: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QBluetoothServiceInfo::setAttribute(quint16 attributeId,
    const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setAttribute

    Parameters
    ----------

    attributeId : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QBluetoothServiceInfo::setAttribute(quint16 attributeId, const
    #      QVariant &value)
    self.uglySide.call(
        'ritual_ZN21QBluetoothServiceInfo12setAttributeEtRK8QVariant',
        attributeId, self._valueOf(value),
    )

  @overload(int, QBluetoothUuid)
  def setAttribute(self, attributeId: int, value: QBluetoothUuid) -> None:
    """
    Calls Qt's 'void QBluetoothServiceInfo::setAttribute(quint16 attributeId,
    const QBluetoothUuid &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setAttribute

    Parameters
    ----------

    attributeId : int
      Passed on as it is.

    value : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.
    """
    #  void QBluetoothServiceInfo::setAttribute(quint16 attributeId, const
    #      QBluetoothUuid &value)
    self.uglySide.call(
        'ritual_ZN21QBluetoothServiceInfo12setAttributeEtRK14QBluetoothUuid',
        attributeId, self._valueOf(value),
    )

  @overload(int, Sequence)
  def setAttribute(self, attributeId: int, value: Sequence) -> None:
    """
    Calls Qt's 'void QBluetoothServiceInfo::setAttribute(quint16 attributeId,
    const QBluetoothServiceInfo::Sequence &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setAttribute

    Parameters
    ----------

    attributeId : int
      Passed on as it is.

    value : Sequence
      Passed on as a value: Qt reads the C++ QBluetoothServiceInfo::Sequence,
      which stays Python's own.
    """
    #  void QBluetoothServiceInfo::setAttribute(quint16 attributeId, const
    #      QBluetoothServiceInfo::Sequence &value)
    self.uglySide.call(
        'ritual_ZN21QBluetoothServiceInfo12setAttributeEtRKNS_8SequenceE',
        attributeId, self._valueOf(value),
    )

  @overload(int, Alternative)
  def setAttribute(self, attributeId: int, value: Alternative) -> None:
    """
    Calls Qt's 'void QBluetoothServiceInfo::setAttribute(quint16 attributeId,
    const QBluetoothServiceInfo::Alternative &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setAttribute

    Parameters
    ----------

    attributeId : int
      Passed on as it is.

    value : Alternative
      Passed on as a value: Qt reads the C++
      QBluetoothServiceInfo::Alternative, which stays Python's own.
    """
    #  void QBluetoothServiceInfo::setAttribute(quint16 attributeId, const
    #      QBluetoothServiceInfo::Alternative &value)
    self.uglySide.call(
        'ritual_ZN21QBluetoothServiceInfo12setAttributeEtRKNS_11Alternative'
        'E',
        attributeId, self._valueOf(value),
    )

  @overload(str)
  def setServiceName(self, name: str) -> None:
    """
    Calls Qt's 'void QBluetoothServiceInfo::setServiceName(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setServiceName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBluetoothServiceInfo::setServiceName(const QString &name)
    self.uglySide.call(
        'ritual_ZN21QBluetoothServiceInfo14setServiceNameERK7QString', name,
    )

  @overload(str)
  def setServiceDescription(self, description: str) -> None:
    """
    Calls Qt's 'void QBluetoothServiceInfo::setServiceDescription(const
    QString &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setServiceDescription

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBluetoothServiceInfo::setServiceDescription(const QString
    #      &description)
    self.uglySide.call(
        'ritual_ZN21QBluetoothServiceInfo21setServiceDescriptionERK7QString',
        description,
    )

  @overload(str)
  def setServiceProvider(self, provider: str) -> None:
    """
    Calls Qt's 'void QBluetoothServiceInfo::setServiceProvider(const QString
    &provider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setServiceProvider

    Parameters
    ----------

    provider : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QBluetoothServiceInfo::setServiceProvider(const QString
    #      &provider)
    self.uglySide.call(
        'ritual_ZN21QBluetoothServiceInfo18setServiceProviderERK7QString',
        provider,
    )

  @overload(int)
  def setServiceAvailability(self, availability: int) -> None:
    """
    Calls Qt's 'void QBluetoothServiceInfo::setServiceAvailability(quint8
    availability)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setServiceAvailability

    Parameters
    ----------

    availability : int
      Passed on as it is.
    """
    #  void QBluetoothServiceInfo::setServiceAvailability(quint8
    #      availability)
    self.uglySide.call(
        'ritual_ZN21QBluetoothServiceInfo22setServiceAvailabilityEh',
        availability,
    )

  @overload(QBluetoothUuid)
  def setServiceUuid(self, uuid: QBluetoothUuid) -> None:
    """
    Calls Qt's 'void QBluetoothServiceInfo::setServiceUuid(const
    QBluetoothUuid &uuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#setServiceUuid

    Parameters
    ----------

    uuid : QBluetoothUuid
      Passed on as a value: Qt reads the C++ QBluetoothUuid, which stays
      Python's own.
    """
    #  void QBluetoothServiceInfo::setServiceUuid(const QBluetoothUuid &uuid)
    self.uglySide.call(
        'ritual_ZN21QBluetoothServiceInfo14setServiceUuidERK14QBluetoothUui'
        'd',
        self._valueOf(uuid),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDebug)
  def __rlshift__(self, d: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug d, const QBluetoothServiceInfo &i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#operator<<

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug d, const QBluetoothServiceInfo &i)
    address = Rituals.call(
        'ritual_Zls6QDebugRK21QBluetoothServiceInfo',
        CuteMixin._valueOf(d), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    'QBluetoothServiceInfo::QBluetoothServiceInfo()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#QBluetoothServiceInfo
    """
    #  QBluetoothServiceInfo::QBluetoothServiceInfo()
    self._noteCreation(QBluetoothServiceInfo, lambda: Rituals.call(
        'ritual_ZN21QBluetoothServiceInfoC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QBluetoothServiceInfo) -> None:
    """
    Notes what was given, for Qt's
    'QBluetoothServiceInfo::QBluetoothServiceInfo(const QBluetoothServiceInfo
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#QBluetoothServiceInfo

    Parameters
    ----------

    other : QBluetoothServiceInfo
      Passed on as a value: Qt reads the C++ QBluetoothServiceInfo, which
      stays Python's own.
    """
    #  QBluetoothServiceInfo::QBluetoothServiceInfo(const
    #      QBluetoothServiceInfo &other)
    self._noteCreation(QBluetoothServiceInfo, lambda: Rituals.call(
        'ritual_ZN21QBluetoothServiceInfoC1ERKS_', self._valueOf(other),
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

  @overload(int)
  def removeAttribute(self, attributeId: int) -> None:
    """
    Calls Qt's 'void QBluetoothServiceInfo::removeAttribute(quint16
    attributeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#removeAttribute

    Parameters
    ----------

    attributeId : int
      Passed on as it is.
    """
    #  void QBluetoothServiceInfo::removeAttribute(quint16 attributeId)
    self.uglySide.call(
        'ritual_ZN21QBluetoothServiceInfo15removeAttributeEt', attributeId,
    )

  @overload()
  @overload(QBluetoothAddress)
  def registerService(
      self,
      localAdapter: Optional[QBluetoothAddress] = None,
  ) -> bool:
    """
    Calls Qt's 'bool QBluetoothServiceInfo::registerService(const
    QBluetoothAddress &localAdapter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#registerService

    Parameters
    ----------

    localAdapter : Optional[QBluetoothAddress]
      Passed on as a value: Qt reads the C++ QBluetoothAddress, which stays
      Python's own. May be left out, as in Qt: a new 'QBluetoothAddress()' is
      then passed on.
    """
    #  bool QBluetoothServiceInfo::registerService(const QBluetoothAddress
    #      &localAdapter)
    if localAdapter is None:
      from . import QBluetoothAddress
      localAdapter = QBluetoothAddress()
    return self.uglySide.call(
        'ritual_ZN21QBluetoothServiceInfo15registerServiceERK17QBluetoothAd'
        'dress',
        self._valueOf(localAdapter),
    )

  def unregisterService(self) -> bool:
    """
    Calls Qt's 'bool QBluetoothServiceInfo::unregisterService()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothserviceinfo.html#unregisterService
    """
    #  bool QBluetoothServiceInfo::unregisterService()
    return self.uglySide.call(
        'ritual_ZN21QBluetoothServiceInfo17unregisterServiceEv',
    )

  @staticmethod
  def attributes(*__, **_) -> Never:
    """
    Qt's 'QList<quint16> QBluetoothServiceInfo::attributes() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QBluetoothServiceInfo.attributes' has no cute function yet. Qt's "
        "'QList<quint16> QBluetoothServiceInfo::attributes() const': gives "
        "a type Python has no way to take yet.")


#  Qt's 'QList<QBluetoothServiceInfo>': the list of QBluetoothServiceInfo,
#  which 'QList[QBluetoothServiceInfo]' gives. It is made here, so that there
#  is one as soon as there can be a QBluetoothServiceInfo.
QList.createKind(
    QBluetoothServiceInfo, 'value',
    make='ritual_list_make_QBluetoothServiceInfo',
    add='ritual_list_add_QBluetoothServiceInfo',
    size='ritual_list_size_QBluetoothServiceInfo',
    at='ritual_list_at_QBluetoothServiceInfo',
    drop='ritual_list_drop_QBluetoothServiceInfo',
)

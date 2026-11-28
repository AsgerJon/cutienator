"""
QOpcUaMonitoringParameters binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuamonitoringparameters.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
  from . import QOpcUaContentFilterElement, QOpcUaEventFilterResult
  from . import QOpcUaSimpleAttributeOperand
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaEventFilterResult = WAIT['QOpcUaEventFilterResult']


class QOpcUaMonitoringParameters(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaMonitoringParameters: a plain Python object
  standing in front of one C++ QOpcUaMonitoringParameters.

  C++ hands a QOpcUaMonitoringParameters around as a copy, so every C++
  QOpcUaMonitoringParameters behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpcUaMonitoringParameters that has a ritual and
  that Python can call so far, 36 names in all: 'samplingInterval',
  'setSamplingInterval', 'filter', 'setFilter', 'clearFilter',
  'filterResult', 'setFilterResult', 'clearFilterResult', 'queueSize',
  'setQueueSize', 'discardOldest', 'setDiscardOldest', 'monitoringMode',
  'setMonitoringMode', 'subscriptionId', 'setSubscriptionId',
  'monitoredItemId', 'setMonitoredItemId', 'publishingInterval',
  'setPublishingInterval', 'lifetimeCount', 'setLifetimeCount',
  'maxKeepAliveCount', 'setMaxKeepAliveCount', 'maxNotificationsPerPublish',
  'setMaxNotificationsPerPublish', 'priority', 'setPriority',
  'isPublishingEnabled', 'setPublishingEnabled', 'statusCode',
  'setStatusCode', 'subscriptionType', 'setSubscriptionType', 'indexRange',
  'setIndexRange'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaMonitoringParameters::~QOpcUaMonitoringParameters()': the
    destructor: Python removes its C++ QOpcUaMonitoringParameters by it, and
    has no other use for it.
  - Qt's 'QOpcUaMonitoringParameters
    &QOpcUaMonitoringParameters::operator=(const QOpcUaMonitoringParameters
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QSet<quint32> QOpcUaMonitoringParameters::triggeredItemIds()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QOpcUaMonitoringParameters::setTriggeredItemIds(const
    QSet<quint32> &id)': takes a type Python has no way to hand over yet.
  - Qt's 'QHash<quint32, QOpcUa::UaStatusCode>
    QOpcUaMonitoringParameters::failedTriggeredItemsStatus() const': gives a
    type Python has no way to take yet.
  - Qt's 'void
    QOpcUaMonitoringParameters::setFailedTriggeredItemsStatus(const
    QHash<quint32, QOpcUa::UaStatusCode> &status)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 49 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QOpcUaMonitoringParameters is created at the first use, not by
    'QOpcUaMonitoringParameters(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaMonitoringParameters back gives a copy the
    ritual made for Python, in a new cute QOpcUaMonitoringParameters.
  - Each name of Qt's QOpcUaMonitoringParameters that has no cute function
    yet, 'failedTriggeredItemsStatus', 'setFailedTriggeredItemsStatus',
    'setTriggeredItemIds', 'triggeredItemIds', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpcUaMonitoringParameters, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class MonitoringMode(CuteNum, scoped=True):
    """
    The enum 'QOpcUaMonitoringParameters::MonitoringMode' of Qt, with the 3
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Disabled = Kee[int](0)
    Sampling = Kee[int](1)
    Reporting = Kee[int](2)

  class Parameter(CuteFlags, scoped=True):
    """
    The flags enum 'QOpcUaMonitoringParameters::Parameter' of Qt, with the 12
    names Qt gives in it. Qt names the type of its combinations
    'QOpcUaMonitoringParameters::Parameters'. C++ keeps these names inside
    the enum, so the class that holds the enum does not have them.
    """

    PublishingEnabled = 0x1
    PublishingInterval = 0x2
    LifetimeCount = 0x4
    MaxKeepAliveCount = 0x8
    MaxNotificationsPerPublish = 0x10
    Priority = 0x20
    SamplingInterval = 0x40
    Filter = 0x80
    QueueSize = 0x100
    DiscardOldest = 0x200
    MonitoringMode = 0x400
    TriggeredItemIds = 0x800

  Parameters = Parameter

  class SubscriptionType(CuteNum, scoped=True):
    """
    The enum 'QOpcUaMonitoringParameters::SubscriptionType' of Qt, with the 2
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Shared = Kee[int](0)
    Exclusive = Kee[int](1)

  #  The classes Qt writes inside QOpcUaMonitoringParameters, each a class in
  #  here as in C++.

  class DataChangeFilter(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QOpcUaMonitoringParameters::DataChangeFilter: a
    plain Python object standing in front of one C++
    QOpcUaMonitoringParameters::DataChangeFilter.

    C++ hands a QOpcUaMonitoringParameters::DataChangeFilter around as a
    copy, so every C++ QOpcUaMonitoringParameters::DataChangeFilter behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QOpcUaMonitoringParameters::DataChangeFilter that
    has a ritual and that Python can call so far, 7 names in all: '__eq__',
    'trigger', 'setTrigger', 'deadbandType', 'setDeadbandType',
    'deadbandValue', 'setDeadbandValue'. It can be made from Python, in 3
    ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'DataChangeFilter
      &QOpcUaMonitoringParameters::DataChangeFilter::operator=(const
      DataChangeFilter &a0)': assignment: Python binds a name and has no
      operator for it.
    - Qt's 'QVariant QOpcUaMonitoringParameters::DataChangeFilter::operator
      QVariant() const': an operator Python has no name for.
    - Qt's
      'QOpcUaMonitoringParameters::DataChangeFilter::~DataChangeFilter()':
      the destructor: Python removes its C++
      QOpcUaMonitoringParameters::DataChangeFilter by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QOpcUaMonitoringParameters::DataChangeFilter is created at the
      first use, not by 'QOpcUaMonitoringParameters::DataChangeFilter(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QOpcUaMonitoringParameters::DataChangeFilter back
      gives a copy the ritual made for Python, in a new cute
      QOpcUaMonitoringParameters::DataChangeFilter.
    """

    #  The enums Qt writes inside
    #  QOpcUaMonitoringParameters::DataChangeFilter, each a class in here as
    #  in C++, and the names Qt has for the combinations of its flags enums.

    class DataChangeTrigger(CuteNum, scoped=True):
      """
      The enum
      'QOpcUaMonitoringParameters::DataChangeFilter::DataChangeTrigger' of
      Qt, with the 3 names Qt gives in it. C++ keeps these names inside the
      enum, so the class that holds the enum does not have them.
      """

      Status = Kee[int](0)
      StatusOrValue = Kee[int](1)
      StatusOrValueOrTimestamp = Kee[int](2)

    class DeadbandType(CuteNum, scoped=True):
      """
      The enum 'QOpcUaMonitoringParameters::DataChangeFilter::DeadbandType'
      of Qt, with the 3 names Qt gives in it. C++ keeps these names inside
      the enum, so the class that holds the enum does not have them.
      """

      NULL = Kee[int](0)
      Absolute = Kee[int](1)
      Percent = Kee[int](2)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QOpcUaMonitoringParameters::DataChangeFilter'

    #  Qt's '~QOpcUaMonitoringParameters::DataChangeFilter()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QOpcUaMonitoringParameters::DataChangeFilter behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilterD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def trigger(self) -> DataChangeTrigger:
      """
      Calls Qt's 'DataChangeTrigger
      QOpcUaMonitoringParameters::DataChangeFilter::trigger() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-datachangefilter.html

      Returns
      -------

      DataChangeTrigger
        The member standing for the number Qt gave back. For a number Qt
        gives no name it is the member without a name that
        'DataChangeTrigger(number)' gives.
      """
      #  DataChangeTrigger
      #      QOpcUaMonitoringParameters::DataChangeFilter::trigger() const
      return QOpcUaMonitoringParameters.DataChangeFilter.DataChangeTrigger(
          self.uglySide.call(
              'ritual_ZNK26QOpcUaMonitoringParameters16DataChangeFilter7tri'
              'ggerEv',
          ))

    def deadbandType(self) -> DeadbandType:
      """
      Calls Qt's 'DeadbandType
      QOpcUaMonitoringParameters::DataChangeFilter::deadbandType() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-datachangefilter.html

      Returns
      -------

      DeadbandType
        The member standing for the number Qt gave back. For a number Qt
        gives no name it is the member without a name that
        'DeadbandType(number)' gives.
      """
      #  DeadbandType
      #      QOpcUaMonitoringParameters::DataChangeFilter::deadbandType()
      #      const
      return QOpcUaMonitoringParameters.DataChangeFilter.DeadbandType(
          self.uglySide.call(
              'ritual_ZNK26QOpcUaMonitoringParameters16DataChangeFilter12de'
              'adbandTypeEv',
          ))

    def deadbandValue(self) -> float:
      """
      Calls Qt's 'double
      QOpcUaMonitoringParameters::DataChangeFilter::deadbandValue() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-datachangefilter.html
      """
      #  double QOpcUaMonitoringParameters::DataChangeFilter::deadbandValue()
      #      const
      return self.uglySide.call(
          'ritual_ZNK26QOpcUaMonitoringParameters16DataChangeFilter13deadba'
          'ndValueEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(DataChangeTrigger)
    def setTrigger(self, trigger: DataChangeTrigger) -> None:
      """
      Calls Qt's 'void
      QOpcUaMonitoringParameters::DataChangeFilter::setTrigger(
      DataChangeTrigger trigger)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-datachangefilter.html

      Parameters
      ----------

      trigger : DataChangeTrigger
        Passed on as its number.
      """
      #  void QOpcUaMonitoringParameters::DataChangeFilter::setTrigger(
      #      DataChangeTrigger trigger)
      self.uglySide.call(
          'ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilter10setTrig'
          'gerENS0_17DataChangeTriggerE',
          trigger.value,
      )

    @overload(DeadbandType)
    def setDeadbandType(self, deadbandType: DeadbandType) -> None:
      """
      Calls Qt's 'void
      QOpcUaMonitoringParameters::DataChangeFilter::setDeadbandType(
      DeadbandType deadbandType)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-datachangefilter.html

      Parameters
      ----------

      deadbandType : DeadbandType
        Passed on as its number.
      """
      #  void QOpcUaMonitoringParameters::DataChangeFilter::setDeadbandType(
      #      DeadbandType deadbandType)
      self.uglySide.call(
          'ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilter15setDead'
          'bandTypeENS0_12DeadbandTypeE',
          deadbandType.value,
      )

    @overload(float)
    def setDeadbandValue(self, deadbandValue: float) -> None:
      """
      Calls Qt's 'void
      QOpcUaMonitoringParameters::DataChangeFilter::setDeadbandValue(double
      deadbandValue)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-datachangefilter.html

      Parameters
      ----------

      deadbandValue : float
        Passed on as it is.
      """
      #  void QOpcUaMonitoringParameters::DataChangeFilter::setDeadbandValue(
      #      double deadbandValue)
      self.uglySide.call(
          'ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilter16setDead'
          'bandValueEd',
          deadbandValue,
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __eq__(
        self,
        rhs: QOpcUaMonitoringParameters.DataChangeFilter,
    ) -> bool:
      """
      Calls Qt's 'bool
      QOpcUaMonitoringParameters::DataChangeFilter::operator==(const
      DataChangeFilter &rhs) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-datachangefilter.html

      Parameters
      ----------

      rhs : QOpcUaMonitoringParameters.DataChangeFilter
        Passed on as a value: Qt reads the C++
        QOpcUaMonitoringParameters::DataChangeFilter, which stays Python's
        own.
      """
      #  bool QOpcUaMonitoringParameters::DataChangeFilter::operator==(const
      #      DataChangeFilter &rhs) const
      return self.uglySide.call(
          'ritual_ZNK26QOpcUaMonitoringParameters16DataChangeFiltereqERKS0_',
          self._valueOf(rhs),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QOpcUaMonitoringParameters::DataChangeFilter::DataChangeFilter()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-datachangefilter.html
      """
      #  QOpcUaMonitoringParameters::DataChangeFilter::DataChangeFilter()
      self._noteCreation(
          QOpcUaMonitoringParameters.DataChangeFilter, lambda: Rituals.call(
              'ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilterC1Ev',
          ))

    @overload(THIS)
    def __init__(
        self,
        a0: QOpcUaMonitoringParameters.DataChangeFilter,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QOpcUaMonitoringParameters::DataChangeFilter::DataChangeFilter(const
      DataChangeFilter &a0)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-datachangefilter.html

      Parameters
      ----------

      a0 : QOpcUaMonitoringParameters.DataChangeFilter
        Passed on as a value: Qt reads the C++
        QOpcUaMonitoringParameters::DataChangeFilter, which stays Python's
        own.
      """
      #  QOpcUaMonitoringParameters::DataChangeFilter::DataChangeFilter(const
      #      DataChangeFilter &a0)
      self._noteCreation(
          QOpcUaMonitoringParameters.DataChangeFilter, lambda: Rituals.call(
              'ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilterC1ERK'
              'S0_',
              self._valueOf(a0),
          ))

    @overload(DataChangeTrigger, DeadbandType, float)
    def __init__(
        self,
        trigger: DataChangeTrigger,
        deadbandType: DeadbandType,
        deadbandValue: float,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QOpcUaMonitoringParameters::DataChangeFilter::DataChangeFilter(
      DataChangeTrigger trigger, DeadbandType deadbandType, double
      deadbandValue)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-datachangefilter.html

      Parameters
      ----------

      trigger : DataChangeTrigger
        Passed on as its number.

      deadbandType : DeadbandType
        Passed on as its number.

      deadbandValue : float
        Passed on as it is.
      """
      #  QOpcUaMonitoringParameters::DataChangeFilter::DataChangeFilter(
      #      DataChangeTrigger trigger, DeadbandType deadbandType, double
      #      deadbandValue)
      self._noteCreation(
          QOpcUaMonitoringParameters.DataChangeFilter, lambda: Rituals.call(
              'ritual_ZN26QOpcUaMonitoringParameters16DataChangeFilterC1ENS'
              '0_17DataChangeTriggerENS0_12DeadbandTypeEd',
              trigger.value, deadbandType.value, deadbandValue,
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

  class EventFilter(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QOpcUaMonitoringParameters::EventFilter: a plain
    Python object standing in front of one C++
    QOpcUaMonitoringParameters::EventFilter.

    C++ hands a QOpcUaMonitoringParameters::EventFilter around as a copy, so
    every C++ QOpcUaMonitoringParameters::EventFilter behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QOpcUaMonitoringParameters::EventFilter that has a
    ritual and that Python can call so far, 5 names in all: '__eq__',
    'selectClauses', 'setSelectClauses', 'whereClause', 'setWhereClause'. It
    can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'EventFilter
      &QOpcUaMonitoringParameters::EventFilter::operator=(const EventFilter
      &a0)': assignment: Python binds a name and has no operator for it.
    - Qt's 'EventFilter
      &QOpcUaMonitoringParameters::EventFilter::operator<<(const
      QOpcUaContentFilterElement &whereClauseElement)': gives a type Python
      has no way to take yet.
    - Qt's 'EventFilter
      &QOpcUaMonitoringParameters::EventFilter::operator<<(const
      QOpcUaSimpleAttributeOperand &selectClauseElement)': gives a type
      Python has no way to take yet.
    - Qt's 'QOpcUaMonitoringParameters::EventFilter::~EventFilter()': the
      destructor: Python removes its C++
      QOpcUaMonitoringParameters::EventFilter by it, and has no other use for
      it.
    - Qt's 'QList<QOpcUaSimpleAttributeOperand>
      &QOpcUaMonitoringParameters::EventFilter::selectClausesRef()': gives a
      type Python has no way to take yet.
    - Qt's 'QList<QOpcUaContentFilterElement>
      &QOpcUaMonitoringParameters::EventFilter::whereClauseRef()': gives a
      type Python has no way to take yet.

    What has no ritual
    ------------------

    1 of the 14 functions Qt declares: 1 cannot be called and cannot be
    called through the meta-object and cannot be copied.

    What to expect
    --------------

    - The C++ QOpcUaMonitoringParameters::EventFilter is created at the first
      use, not by 'QOpcUaMonitoringParameters::EventFilter(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QOpcUaMonitoringParameters::EventFilter back gives
      a copy the ritual made for Python, in a new cute
      QOpcUaMonitoringParameters::EventFilter.
    - Each name of Qt's QOpcUaMonitoringParameters::EventFilter that has no
      cute function yet, 'selectClausesRef', 'whereClauseRef', holds a
      function that raises 'NotImplementedError', and its docstring says why.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QOpcUaContentFilterElement = WAIT['QOpcUaContentFilterElement']
      QOpcUaSimpleAttributeOperand = WAIT['QOpcUaSimpleAttributeOperand']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QOpcUaMonitoringParameters::EventFilter'

    #  Qt's '~QOpcUaMonitoringParameters::EventFilter()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QOpcUaMonitoringParameters::EventFilter behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN26QOpcUaMonitoringParameters11EventFilterD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def selectClauses(self) -> QList[QOpcUaSimpleAttributeOperand]:
      """
      Calls Qt's 'QList<QOpcUaSimpleAttributeOperand>
      QOpcUaMonitoringParameters::EventFilter::selectClauses() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-eventfilter.html

      Returns
      -------

      QList[QOpcUaSimpleAttributeOperand]
        A new cute list around the copy Qt gave back. Python owns it.
      """
      #  QList<QOpcUaSimpleAttributeOperand>
      #      QOpcUaMonitoringParameters::EventFilter::selectClauses() const
      address = self.uglySide.call(
          'ritual_ZNK26QOpcUaMonitoringParameters11EventFilter13selectClaus'
          'esEv',
      )
      from . import QOpcUaSimpleAttributeOperand
      return QList[QOpcUaSimpleAttributeOperand]._cuteOwning(address)

    def whereClause(self) -> QList[QOpcUaContentFilterElement]:
      """
      Calls Qt's 'QList<QOpcUaContentFilterElement>
      QOpcUaMonitoringParameters::EventFilter::whereClause() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-eventfilter.html

      Returns
      -------

      QList[QOpcUaContentFilterElement]
        A new cute list around the copy Qt gave back. Python owns it.
      """
      #  QList<QOpcUaContentFilterElement>
      #      QOpcUaMonitoringParameters::EventFilter::whereClause() const
      address = self.uglySide.call(
          'ritual_ZNK26QOpcUaMonitoringParameters11EventFilter11whereClause'
          'Ev',
      )
      from . import QOpcUaContentFilterElement
      return QList[QOpcUaContentFilterElement]._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QList[QOpcUaSimpleAttributeOperand])
    def setSelectClauses(
        self,
        selectClauses: QList[QOpcUaSimpleAttributeOperand],
    ) -> None:
      """
      Calls Qt's 'void
      QOpcUaMonitoringParameters::EventFilter::setSelectClauses(const
      QList<QOpcUaSimpleAttributeOperand> &selectClauses)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-eventfilter.html

      Parameters
      ----------

      selectClauses : QList[QOpcUaSimpleAttributeOperand]
        Passed on as a list of Qt: Qt reads the C++ list, which stays
        Python's own. A list or tuple of Python is made into one first, and
        refused when an element does not fit.
      """
      #  void QOpcUaMonitoringParameters::EventFilter::setSelectClauses(const
      #      QList<QOpcUaSimpleAttributeOperand> &selectClauses)
      self.uglySide.call(
          'ritual_ZN26QOpcUaMonitoringParameters11EventFilter16setSelectCla'
          'usesERK5QListI28QOpcUaSimpleAttributeOperandE',
          self._valueOf(selectClauses),
      )

    @overload(QList[QOpcUaContentFilterElement])
    def setWhereClause(
        self,
        whereClause: QList[QOpcUaContentFilterElement],
    ) -> None:
      """
      Calls Qt's 'void
      QOpcUaMonitoringParameters::EventFilter::setWhereClause(const
      QList<QOpcUaContentFilterElement> &whereClause)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-eventfilter.html

      Parameters
      ----------

      whereClause : QList[QOpcUaContentFilterElement]
        Passed on as a list of Qt: Qt reads the C++ list, which stays
        Python's own. A list or tuple of Python is made into one first, and
        refused when an element does not fit.
      """
      #  void QOpcUaMonitoringParameters::EventFilter::setWhereClause(const
      #      QList<QOpcUaContentFilterElement> &whereClause)
      self.uglySide.call(
          'ritual_ZN26QOpcUaMonitoringParameters11EventFilter14setWhereClau'
          'seERK5QListI26QOpcUaContentFilterElementE',
          self._valueOf(whereClause),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __eq__(self, rhs: QOpcUaMonitoringParameters.EventFilter) -> bool:
      """
      Calls Qt's 'bool
      QOpcUaMonitoringParameters::EventFilter::operator==(const
      QOpcUaMonitoringParameters::EventFilter &rhs) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-eventfilter.html

      Parameters
      ----------

      rhs : QOpcUaMonitoringParameters.EventFilter
        Passed on as a value: Qt reads the C++
        QOpcUaMonitoringParameters::EventFilter, which stays Python's own.
      """
      #  bool QOpcUaMonitoringParameters::EventFilter::operator==(const
      #      QOpcUaMonitoringParameters::EventFilter &rhs) const
      return self.uglySide.call(
          'ritual_ZNK26QOpcUaMonitoringParameters11EventFiltereqERKS0_',
          self._valueOf(rhs),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QOpcUaMonitoringParameters::EventFilter::EventFilter()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-eventfilter.html
      """
      #  QOpcUaMonitoringParameters::EventFilter::EventFilter()
      self._noteCreation(
          QOpcUaMonitoringParameters.EventFilter, lambda: Rituals.call(
              'ritual_ZN26QOpcUaMonitoringParameters11EventFilterC1Ev',
          ))

    @overload(THIS)
    def __init__(self, a0: QOpcUaMonitoringParameters.EventFilter) -> None:
      """
      Notes what was given, for Qt's
      'QOpcUaMonitoringParameters::EventFilter::EventFilter(const EventFilter
      &a0)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qopcuamonitoringparameters-eventfilter.html

      Parameters
      ----------

      a0 : QOpcUaMonitoringParameters.EventFilter
        Passed on as a value: Qt reads the C++
        QOpcUaMonitoringParameters::EventFilter, which stays Python's own.
      """
      #  QOpcUaMonitoringParameters::EventFilter::EventFilter(const
      #      EventFilter &a0)
      self._noteCreation(
          QOpcUaMonitoringParameters.EventFilter, lambda: Rituals.call(
              'ritual_ZN26QOpcUaMonitoringParameters11EventFilterC1ERKS0_',
              self._valueOf(a0),
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

    @staticmethod
    def selectClausesRef(*__, **_) -> Never:
      """
      Qt's 'QList<QOpcUaSimpleAttributeOperand>
      &QOpcUaMonitoringParameters::EventFilter::selectClausesRef()': gives a
      type Python has no way to take yet.
      """
      raise NotImplementedError(
          "'QOpcUaMonitoringParameters.EventFilter.selectClausesRef' has no "
          "cute function yet. Qt's 'QList<QOpcUaSimpleAttributeOperand> "
          "&QOpcUaMonitoringParameters::EventFilter::selectClausesRef()': "
          "gives a type Python has no way to take yet.")

    @staticmethod
    def whereClauseRef(*__, **_) -> Never:
      """
      Qt's 'QList<QOpcUaContentFilterElement>
      &QOpcUaMonitoringParameters::EventFilter::whereClauseRef()': gives a
      type Python has no way to take yet.
      """
      raise NotImplementedError(
          "'QOpcUaMonitoringParameters.EventFilter.whereClauseRef' has no "
          "cute function yet. Qt's 'QList<QOpcUaContentFilterElement> "
          "&QOpcUaMonitoringParameters::EventFilter::whereClauseRef()': "
          "gives a type Python has no way to take yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaMonitoringParameters'

  #  Qt's '~QOpcUaMonitoringParameters()'. Naming it makes this a value
  #  class: Python owns every C++ QOpcUaMonitoringParameters behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QOpcUaMonitoringParametersD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def samplingInterval(self) -> float:
    """
    Calls Qt's 'double QOpcUaMonitoringParameters::samplingInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#samplingInterval
    """
    #  double QOpcUaMonitoringParameters::samplingInterval() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters16samplingIntervalEv',
    )

  def filter(self) -> QVariant:
    """
    Calls Qt's 'QVariant QOpcUaMonitoringParameters::filter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#filter

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QOpcUaMonitoringParameters::filter() const
    address = self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters6filterEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def filterResult(self) -> QVariant:
    """
    Calls Qt's 'QVariant QOpcUaMonitoringParameters::filterResult() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#filterResult

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QOpcUaMonitoringParameters::filterResult() const
    address = self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters12filterResultEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def queueSize(self) -> int:
    """
    Calls Qt's 'quint32 QOpcUaMonitoringParameters::queueSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#queueSize
    """
    #  quint32 QOpcUaMonitoringParameters::queueSize() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters9queueSizeEv',
    )

  def discardOldest(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaMonitoringParameters::discardOldest() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#discardOldest
    """
    #  bool QOpcUaMonitoringParameters::discardOldest() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters13discardOldestEv',
    )

  def monitoringMode(self) -> MonitoringMode:
    """
    Calls Qt's 'QOpcUaMonitoringParameters::MonitoringMode
    QOpcUaMonitoringParameters::monitoringMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#monitoringMode

    Returns
    -------

    MonitoringMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MonitoringMode(number)'
      gives.
    """
    #  QOpcUaMonitoringParameters::MonitoringMode
    #      QOpcUaMonitoringParameters::monitoringMode() const
    return QOpcUaMonitoringParameters.MonitoringMode(self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters14monitoringModeEv',
    ))

  def subscriptionId(self) -> int:
    """
    Calls Qt's 'quint32 QOpcUaMonitoringParameters::subscriptionId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#subscriptionId
    """
    #  quint32 QOpcUaMonitoringParameters::subscriptionId() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters14subscriptionIdEv',
    )

  def monitoredItemId(self) -> int:
    """
    Calls Qt's 'quint32 QOpcUaMonitoringParameters::monitoredItemId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#monitoredItemId
    """
    #  quint32 QOpcUaMonitoringParameters::monitoredItemId() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters15monitoredItemIdEv',
    )

  def publishingInterval(self) -> float:
    """
    Calls Qt's 'double QOpcUaMonitoringParameters::publishingInterval()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#publishingInterval
    """
    #  double QOpcUaMonitoringParameters::publishingInterval() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters18publishingIntervalEv',
    )

  def lifetimeCount(self) -> int:
    """
    Calls Qt's 'quint32 QOpcUaMonitoringParameters::lifetimeCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#lifetimeCount
    """
    #  quint32 QOpcUaMonitoringParameters::lifetimeCount() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters13lifetimeCountEv',
    )

  def maxKeepAliveCount(self) -> int:
    """
    Calls Qt's 'quint32 QOpcUaMonitoringParameters::maxKeepAliveCount()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#maxKeepAliveCount
    """
    #  quint32 QOpcUaMonitoringParameters::maxKeepAliveCount() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters17maxKeepAliveCountEv',
    )

  def maxNotificationsPerPublish(self) -> int:
    """
    Calls Qt's 'quint32
    QOpcUaMonitoringParameters::maxNotificationsPerPublish() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html
    """
    #  quint32 QOpcUaMonitoringParameters::maxNotificationsPerPublish() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters26maxNotificationsPerPublish'
        'Ev',
    )

  def priority(self) -> int:
    """
    Calls Qt's 'quint8 QOpcUaMonitoringParameters::priority() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#priority
    """
    #  quint8 QOpcUaMonitoringParameters::priority() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters8priorityEv',
    )

  def isPublishingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaMonitoringParameters::isPublishingEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html
    """
    #  bool QOpcUaMonitoringParameters::isPublishingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters19isPublishingEnabledEv',
    )

  def statusCode(self) -> QOpcUa.UaStatusCode:
    """
    Calls Qt's 'QOpcUa::UaStatusCode QOpcUaMonitoringParameters::statusCode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#statusCode

    Returns
    -------

    QOpcUa.UaStatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpcUa.UaStatusCode(number)' gives.
    """
    #  QOpcUa::UaStatusCode QOpcUaMonitoringParameters::statusCode() const
    return QOpcUa.UaStatusCode(self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters10statusCodeEv',
    ))

  def subscriptionType(self) -> SubscriptionType:
    """
    Calls Qt's 'QOpcUaMonitoringParameters::SubscriptionType
    QOpcUaMonitoringParameters::subscriptionType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#subscriptionType

    Returns
    -------

    SubscriptionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SubscriptionType(number)'
      gives.
    """
    #  QOpcUaMonitoringParameters::SubscriptionType
    #      QOpcUaMonitoringParameters::subscriptionType() const
    return QOpcUaMonitoringParameters.SubscriptionType(self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters16subscriptionTypeEv',
    ))

  def indexRange(self) -> str:
    """
    Calls Qt's 'QString QOpcUaMonitoringParameters::indexRange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#indexRange

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaMonitoringParameters::indexRange() const
    return self.uglySide.call(
        'ritual_ZNK26QOpcUaMonitoringParameters10indexRangeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setSamplingInterval(self, samplingInterval: float) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setSamplingInterval(double
    samplingInterval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html

    Parameters
    ----------

    samplingInterval : float
      Passed on as it is.
    """
    #  void QOpcUaMonitoringParameters::setSamplingInterval(double
    #      samplingInterval)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters19setSamplingIntervalEd',
        samplingInterval,
    )

  @overload(DataChangeFilter)
  def setFilter(self, filter: DataChangeFilter) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setFilter(const
    QOpcUaMonitoringParameters::DataChangeFilter &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#setFilter

    Parameters
    ----------

    filter : DataChangeFilter
      Passed on as a value: Qt reads the C++
      QOpcUaMonitoringParameters::DataChangeFilter, which stays Python's own.
    """
    #  void QOpcUaMonitoringParameters::setFilter(const
    #      QOpcUaMonitoringParameters::DataChangeFilter &filter)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters9setFilterERKNS_16DataChangeF'
        'ilterE',
        self._valueOf(filter),
    )

  @overload(EventFilter)
  def setFilter(self, eventFilter: EventFilter) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setFilter(const
    QOpcUaMonitoringParameters::EventFilter &eventFilter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#setFilter

    Parameters
    ----------

    eventFilter : EventFilter
      Passed on as a value: Qt reads the C++
      QOpcUaMonitoringParameters::EventFilter, which stays Python's own.
    """
    #  void QOpcUaMonitoringParameters::setFilter(const
    #      QOpcUaMonitoringParameters::EventFilter &eventFilter)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters9setFilterERKNS_11EventFilter'
        'E',
        self._valueOf(eventFilter),
    )

  @overload(QOpcUaEventFilterResult)
  def setFilterResult(
      self,
      eventFilterResult: QOpcUaEventFilterResult,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setFilterResult(const
    QOpcUaEventFilterResult &eventFilterResult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#setFilterResult

    Parameters
    ----------

    eventFilterResult : QOpcUaEventFilterResult
      Passed on as a value: Qt reads the C++ QOpcUaEventFilterResult, which
      stays Python's own.
    """
    #  void QOpcUaMonitoringParameters::setFilterResult(const
    #      QOpcUaEventFilterResult &eventFilterResult)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters15setFilterResultERK23QOpcUaE'
        'ventFilterResult',
        self._valueOf(eventFilterResult),
    )

  @overload(int)
  def setQueueSize(self, queueSize: int) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setQueueSize(quint32
    queueSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#setQueueSize

    Parameters
    ----------

    queueSize : int
      Passed on as it is.
    """
    #  void QOpcUaMonitoringParameters::setQueueSize(quint32 queueSize)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters12setQueueSizeEj', queueSize,
    )

  @overload(bool)
  def setDiscardOldest(self, discardOldest: bool) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setDiscardOldest(bool
    discardOldest)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#setDiscardOldest

    Parameters
    ----------

    discardOldest : bool
      Passed on as it is.
    """
    #  void QOpcUaMonitoringParameters::setDiscardOldest(bool discardOldest)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters16setDiscardOldestEb',
        discardOldest,
    )

  @overload(MonitoringMode)
  def setMonitoringMode(self, monitoringMode: MonitoringMode) -> None:
    """
    Calls Qt's 'void
    QOpcUaMonitoringParameters::setMonitoringMode(MonitoringMode
    monitoringMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#setMonitoringMode

    Parameters
    ----------

    monitoringMode : MonitoringMode
      Passed on as its number.
    """
    #  void QOpcUaMonitoringParameters::setMonitoringMode(MonitoringMode
    #      monitoringMode)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters17setMonitoringModeENS_14Moni'
        'toringModeE',
        monitoringMode.value,
    )

  @overload(int)
  def setSubscriptionId(self, subscriptionId: int) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setSubscriptionId(quint32
    subscriptionId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#setSubscriptionId

    Parameters
    ----------

    subscriptionId : int
      Passed on as it is.
    """
    #  void QOpcUaMonitoringParameters::setSubscriptionId(quint32
    #      subscriptionId)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters17setSubscriptionIdEj',
        subscriptionId,
    )

  @overload(int)
  def setMonitoredItemId(self, monitoredItemId: int) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setMonitoredItemId(quint32
    monitoredItemId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#setMonitoredItemId

    Parameters
    ----------

    monitoredItemId : int
      Passed on as it is.
    """
    #  void QOpcUaMonitoringParameters::setMonitoredItemId(quint32
    #      monitoredItemId)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters18setMonitoredItemIdEj',
        monitoredItemId,
    )

  @overload(float)
  def setPublishingInterval(self, publishingInterval: float) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setPublishingInterval(double
    publishingInterval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html

    Parameters
    ----------

    publishingInterval : float
      Passed on as it is.
    """
    #  void QOpcUaMonitoringParameters::setPublishingInterval(double
    #      publishingInterval)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters21setPublishingIntervalEd',
        publishingInterval,
    )

  @overload(int)
  def setLifetimeCount(self, lifetimeCount: int) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setLifetimeCount(quint32
    lifetimeCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#setLifetimeCount

    Parameters
    ----------

    lifetimeCount : int
      Passed on as it is.
    """
    #  void QOpcUaMonitoringParameters::setLifetimeCount(quint32
    #      lifetimeCount)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters16setLifetimeCountEj',
        lifetimeCount,
    )

  @overload(int)
  def setMaxKeepAliveCount(self, maxKeepAliveCount: int) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setMaxKeepAliveCount(quint32
    maxKeepAliveCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html

    Parameters
    ----------

    maxKeepAliveCount : int
      Passed on as it is.
    """
    #  void QOpcUaMonitoringParameters::setMaxKeepAliveCount(quint32
    #      maxKeepAliveCount)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters20setMaxKeepAliveCountEj',
        maxKeepAliveCount,
    )

  @overload(int)
  def setMaxNotificationsPerPublish(
      self,
      maxNotificationsPerPublish: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpcUaMonitoringParameters::setMaxNotificationsPerPublish(quint32
    maxNotificationsPerPublish)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html

    Parameters
    ----------

    maxNotificationsPerPublish : int
      Passed on as it is.
    """
    #  void QOpcUaMonitoringParameters::setMaxNotificationsPerPublish(quint32
    #      maxNotificationsPerPublish)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters29setMaxNotificationsPerPubli'
        'shEj',
        maxNotificationsPerPublish,
    )

  @overload(int)
  def setPriority(self, priority: int) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setPriority(quint8
    priority)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#setPriority

    Parameters
    ----------

    priority : int
      Passed on as it is.
    """
    #  void QOpcUaMonitoringParameters::setPriority(quint8 priority)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters11setPriorityEh', priority,
    )

  @overload(bool)
  def setPublishingEnabled(self, publishingEnabled: bool) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setPublishingEnabled(bool
    publishingEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html

    Parameters
    ----------

    publishingEnabled : bool
      Passed on as it is.
    """
    #  void QOpcUaMonitoringParameters::setPublishingEnabled(bool
    #      publishingEnabled)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters20setPublishingEnabledEb',
        publishingEnabled,
    )

  @overload(QOpcUa.UaStatusCode)
  def setStatusCode(self, statusCode: QOpcUa.UaStatusCode) -> None:
    """
    Calls Qt's 'void
    QOpcUaMonitoringParameters::setStatusCode(QOpcUa::UaStatusCode
    statusCode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#setStatusCode

    Parameters
    ----------

    statusCode : QOpcUa.UaStatusCode
      Passed on as its number.
    """
    #  void QOpcUaMonitoringParameters::setStatusCode(QOpcUa::UaStatusCode
    #      statusCode)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters13setStatusCodeEN6QOpcUa12UaS'
        'tatusCodeE',
        statusCode.value,
    )

  @overload(SubscriptionType)
  def setSubscriptionType(self, subscriptionType: SubscriptionType) -> None:
    """
    Calls Qt's 'void
    QOpcUaMonitoringParameters::setSubscriptionType(SubscriptionType
    subscriptionType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html

    Parameters
    ----------

    subscriptionType : SubscriptionType
      Passed on as its number.
    """
    #  void QOpcUaMonitoringParameters::setSubscriptionType(SubscriptionType
    #      subscriptionType)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters19setSubscriptionTypeENS_16Su'
        'bscriptionTypeE',
        subscriptionType.value,
    )

  @overload(str)
  def setIndexRange(self, indexRange: str) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::setIndexRange(const QString
    &indexRange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#setIndexRange

    Parameters
    ----------

    indexRange : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaMonitoringParameters::setIndexRange(const QString
    #      &indexRange)
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters13setIndexRangeERK7QString',
        indexRange,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaMonitoringParameters::QOpcUaMonitoringParameters()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html
    """
    #  QOpcUaMonitoringParameters::QOpcUaMonitoringParameters()
    self._noteCreation(QOpcUaMonitoringParameters, lambda: Rituals.call(
        'ritual_ZN26QOpcUaMonitoringParametersC1Ev',
    ))

  @overload(float)
  @overload(float, SubscriptionType)
  @overload(float, SubscriptionType, int)
  def __init__(
      self,
      publishingInterval: float,
      subscriptionType: SubscriptionType = SubscriptionType.Shared,
      subscriptionId: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaMonitoringParameters::QOpcUaMonitoringParameters(double
    publishingInterval, SubscriptionType subscriptionType, quint32
    subscriptionId)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html

    Parameters
    ----------

    publishingInterval : float
      Passed on as it is.

    subscriptionType : SubscriptionType
      Passed on as its number. May be left out, as in Qt: it is then
      SubscriptionType.Shared.

    subscriptionId : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QOpcUaMonitoringParameters::QOpcUaMonitoringParameters(double
    #      publishingInterval, SubscriptionType subscriptionType, quint32
    #      subscriptionId)
    self._noteCreation(QOpcUaMonitoringParameters, lambda: Rituals.call(
        'ritual_ZN26QOpcUaMonitoringParametersC1EdNS_16SubscriptionTypeEj',
        publishingInterval, subscriptionType.value, subscriptionId,
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaMonitoringParameters) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaMonitoringParameters::QOpcUaMonitoringParameters(const
    QOpcUaMonitoringParameters &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html

    Parameters
    ----------

    other : QOpcUaMonitoringParameters
      Passed on as a value: Qt reads the C++ QOpcUaMonitoringParameters,
      which stays Python's own.
    """
    #  QOpcUaMonitoringParameters::QOpcUaMonitoringParameters(const
    #      QOpcUaMonitoringParameters &other)
    self._noteCreation(QOpcUaMonitoringParameters, lambda: Rituals.call(
        'ritual_ZN26QOpcUaMonitoringParametersC1ERKS_', self._valueOf(other),
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

  def clearFilter(self) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::clearFilter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#clearFilter
    """
    #  void QOpcUaMonitoringParameters::clearFilter()
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters11clearFilterEv',
    )

  def clearFilterResult(self) -> None:
    """
    Calls Qt's 'void QOpcUaMonitoringParameters::clearFilterResult()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuamonitoringparameters.html#clearFilterResult
    """
    #  void QOpcUaMonitoringParameters::clearFilterResult()
    self.uglySide.call(
        'ritual_ZN26QOpcUaMonitoringParameters17clearFilterResultEv',
    )

  @staticmethod
  def failedTriggeredItemsStatus(*__, **_) -> Never:
    """
    Qt's 'QHash<quint32, QOpcUa::UaStatusCode>
    QOpcUaMonitoringParameters::failedTriggeredItemsStatus() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaMonitoringParameters.failedTriggeredItemsStatus' has no "
        "cute function yet. Qt's 'QHash<quint32, QOpcUa::UaStatusCode> "
        "QOpcUaMonitoringParameters::failedTriggeredItemsStatus() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setFailedTriggeredItemsStatus(*__, **_) -> Never:
    """
    Qt's 'void
    QOpcUaMonitoringParameters::setFailedTriggeredItemsStatus(const
    QHash<quint32, QOpcUa::UaStatusCode> &status)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaMonitoringParameters.setFailedTriggeredItemsStatus' has no "
        "cute function yet. Qt's 'void "
        "QOpcUaMonitoringParameters::setFailedTriggeredItemsStatus(const "
        "QHash<quint32, QOpcUa::UaStatusCode> &status)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setTriggeredItemIds(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaMonitoringParameters::setTriggeredItemIds(const
    QSet<quint32> &id)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaMonitoringParameters.setTriggeredItemIds' has no cute "
        "function yet. Qt's 'void "
        "QOpcUaMonitoringParameters::setTriggeredItemIds(const "
        "QSet<quint32> &id)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def triggeredItemIds(*__, **_) -> Never:
    """
    Qt's 'QSet<quint32> QOpcUaMonitoringParameters::triggeredItemIds()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaMonitoringParameters.triggeredItemIds' has no cute function "
        "yet. Qt's 'QSet<quint32> "
        "QOpcUaMonitoringParameters::triggeredItemIds() const': gives a "
        "type Python has no way to take yet.")

"""
QModbusClientPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusclient_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QModbusClientPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QModbusDevicePrivate, QModbusReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QModbusClient, QModbusDataUnit, QModbusRequest
  from . import QModbusResponse
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModbusDataUnit = WAIT['QModbusDataUnit']
  QModbusRequest = WAIT['QModbusRequest']
  QModbusResponse = WAIT['QModbusResponse']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QModbusClientPrivate(QModbusDevicePrivate):
  """
  The cute side of Qt's QModbusClientPrivate: a plain Python object standing
  in front of one C++ QModbusClientPrivate.

  It is built on the cute 'QModbusDevicePrivate', as Qt's
  QModbusClientPrivate is built on Qt's QModbusDevicePrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QModbusClientPrivate that has a ritual and that
  Python can call so far, 9 names in all: 'q_func', 'createReadRequest',
  'createWriteRequest', 'createRWRequest', 'processResponse',
  'processReadCoilsResponse', 'enqueueRequest', 'isOpen',
  'processQueueElement'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QModbusClient *QModbusClientPrivate::q_func() const': takes
    in Python what 'QModbusClient *QModbusClientPrivate::q_func()' takes.
  - Qt's 'bool QModbusClientPrivate::collateBits(const QModbusPdu &pdu,
    QModbusDataUnit::RegisterType type, QModbusDataUnit *data)': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QModbusClientPrivate::collateBytes(const QModbusPdu &pdu,
    QModbusDataUnit::RegisterType type, QModbusDataUnit *data)': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QModbusClientPrivate::collateSingleValue(const QModbusPdu
    &pdu, QModbusDataUnit::RegisterType type, QModbusDataUnit *data)': takes
    a type Python has no way to hand over yet.
  - Qt's 'bool QModbusClientPrivate::collateMultipleValues(const QModbusPdu
    &pdu, QModbusDataUnit::RegisterType type, QModbusDataUnit *data)': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  9 of the 23 functions Qt declares: 9 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QModbusClientPrivate is created at the first use, not by
    'QModbusClientPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QModbusClientPrivate.
  - Each name of Qt's QModbusClientPrivate that has no cute function yet,
    'collateBits', 'collateBytes', 'collateMultipleValues',
    'collateSingleValue', 'processReadDiscreteInputsResponse',
    'processReadHoldingRegistersResponse',
    'processReadInputRegistersResponse',
    'processReadWriteMultipleRegistersResponse',
    'processWriteMultipleCoilsResponse',
    'processWriteMultipleRegistersResponse',
    'processWriteSingleCoilResponse', 'processWriteSingleRegisterResponse',
    'sendRequest', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The classes Qt writes inside QModbusClientPrivate, each a class in here
  #  as in C++.

  class QueueElement(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QModbusClientPrivate::QueueElement: a plain Python
    object standing in front of one C++ QModbusClientPrivate::QueueElement.

    C++ hands a QModbusClientPrivate::QueueElement around as a copy, so every
    C++ QModbusClientPrivate::QueueElement behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QModbusClientPrivate::QueueElement that has a
    ritual and that Python can call so far, 1 name in all: '__eq__'. It can
    be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QModbusClientPrivate::QueueElement::~QueueElement()': the
      destructor: Python removes its C++ QModbusClientPrivate::QueueElement
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QModbusClientPrivate::QueueElement is created at the first use,
      not by 'QModbusClientPrivate::QueueElement(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QModbusClientPrivate::QueueElement back gives a
      copy the ritual made for Python, in a new cute
      QModbusClientPrivate::QueueElement.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QModbusDataUnit = WAIT['QModbusDataUnit']
      QModbusReply = WAIT['QModbusReply']
      QModbusRequest = WAIT['QModbusRequest']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QModbusClientPrivate::QueueElement'

    #  Qt's '~QModbusClientPrivate::QueueElement()'. Naming it makes this a
    #  value class: Python owns every C++ QModbusClientPrivate::QueueElement
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN20QModbusClientPrivate12QueueElementD1Ev'

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
    def __eq__(self, other: QModbusClientPrivate.QueueElement) -> bool:
      """
      Calls Qt's 'bool QModbusClientPrivate::QueueElement::operator==(const
      QueueElement &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qmodbusclientprivate-queueelement.html

      Parameters
      ----------

      other : QModbusClientPrivate.QueueElement
        Passed on as a value: Qt reads the C++
        QModbusClientPrivate::QueueElement, which stays Python's own.
      """
      #  bool QModbusClientPrivate::QueueElement::operator==(const
      #      QueueElement &other) const
      return self.uglySide.call(
          'ritual_ZNK20QModbusClientPrivate12QueueElementeqERKS0_',
          self._valueOf(other),
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
      'QModbusClientPrivate::QueueElement::QueueElement()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qmodbusclientprivate-queueelement.html
      """
      #  QModbusClientPrivate::QueueElement::QueueElement()
      self._noteCreation(
          QModbusClientPrivate.QueueElement, lambda: Rituals.call(
              'ritual_ZN20QModbusClientPrivate12QueueElementC1Ev',
          ))

    @overload(QModbusReply, QModbusRequest, QModbusDataUnit, int)
    @overload(NoneType, QModbusRequest, QModbusDataUnit, int)
    @overload(QModbusReply, QModbusRequest, QModbusDataUnit, int, int)
    @overload(NoneType, QModbusRequest, QModbusDataUnit, int, int)
    def __init__(
        self,
        r: Optional[QModbusReply],
        req: QModbusRequest,
        u: QModbusDataUnit,
        num: int,
        timeout: int = -1,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QModbusClientPrivate::QueueElement::QueueElement(QModbusReply *r,
      const QModbusRequest &req, const QModbusDataUnit &u, int num, int
      timeout)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qmodbusclientprivate-queueelement.html

      Parameters
      ----------

      r : Optional[QModbusReply]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      req : QModbusRequest
        Passed on as a value: Qt reads the C++ QModbusRequest, which stays
        Python's own.

      u : QModbusDataUnit
        Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
        Python's own.

      num : int
        Passed on as it is.

      timeout : int
        Passed on as it is. May be left out, as in Qt: it is then -1.
      """
      #  QModbusClientPrivate::QueueElement::QueueElement(QModbusReply *r,
      #      const QModbusRequest &req, const QModbusDataUnit &u, int num,
      #      int timeout)
      self._noteCreation(
          QModbusClientPrivate.QueueElement, lambda: Rituals.call(
              'ritual_ZN20QModbusClientPrivate12QueueElementC1EP12QModbusRe'
              'plyRK14QModbusRequestRK15QModbusDataUnitii',
              self._addressOf(r), self._valueOf(req), self._valueOf(u), num,
              timeout,
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusClientPrivate'

  #  A C++ QModbusClientPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusClientPrivate'

  #  The functions Qt calls itself that QModbusClientPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'enqueueRequest': (
          ('_ZN20QModbusClientPrivate14enqueueRequestERK14QModbusRequestiRK'
           '15QModbusDataUnitN12QModbusReply9ReplyTypeE',
           ('address', 'address', 'QtSerialBus:QModbusReply'),
           (
               ('address', 'value', 'QtSerialBus:QModbusRequest'),
               ('int', 'number', ''),
               ('address', 'value', 'QtSerialBus:QModbusDataUnit'),
               ('int', 'enum', 'QtSerialBus:QModbusReply.ReplyType'),
           )),
      ),
      'isOpen': (
          ('_ZNK20QModbusClientPrivate6isOpenEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModbusDataUnit)
  def createReadRequest(self, data: QModbusDataUnit) -> QModbusRequest:
    """
    Calls Qt's 'QModbusRequest QModbusClientPrivate::createReadRequest(const
    QModbusDataUnit &data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusclientprivate.html#createReadRequest

    Parameters
    ----------

    data : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.

    Returns
    -------

    QModbusRequest
      A new cute QModbusRequest around the copy Qt gave back. Python owns it.
    """
    #  QModbusRequest QModbusClientPrivate::createReadRequest(const
    #      QModbusDataUnit &data) const
    address = self.uglySide.call(
        'ritual_ZNK20QModbusClientPrivate17createReadRequestERK15QModbusDat'
        'aUnit',
        self._valueOf(data),
    )
    from . import QModbusRequest
    return QModbusRequest._cuteOwning(address)

  @overload(QModbusDataUnit)
  def createWriteRequest(self, data: QModbusDataUnit) -> QModbusRequest:
    """
    Calls Qt's 'QModbusRequest QModbusClientPrivate::createWriteRequest(const
    QModbusDataUnit &data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusclientprivate.html#createWriteRequest

    Parameters
    ----------

    data : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.

    Returns
    -------

    QModbusRequest
      A new cute QModbusRequest around the copy Qt gave back. Python owns it.
    """
    #  QModbusRequest QModbusClientPrivate::createWriteRequest(const
    #      QModbusDataUnit &data) const
    address = self.uglySide.call(
        'ritual_ZNK20QModbusClientPrivate18createWriteRequestERK15QModbusDa'
        'taUnit',
        self._valueOf(data),
    )
    from . import QModbusRequest
    return QModbusRequest._cuteOwning(address)

  @overload(QModbusDataUnit, QModbusDataUnit)
  def createRWRequest(
      self,
      read: QModbusDataUnit,
      write: QModbusDataUnit,
  ) -> QModbusRequest:
    """
    Calls Qt's 'QModbusRequest QModbusClientPrivate::createRWRequest(const
    QModbusDataUnit &read, const QModbusDataUnit &write) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusclientprivate.html#createRWRequest

    Parameters
    ----------

    read : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.

    write : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.

    Returns
    -------

    QModbusRequest
      A new cute QModbusRequest around the copy Qt gave back. Python owns it.
    """
    #  QModbusRequest QModbusClientPrivate::createRWRequest(const
    #      QModbusDataUnit &read, const QModbusDataUnit &write) const
    address = self.uglySide.call(
        'ritual_ZNK20QModbusClientPrivate15createRWRequestERK15QModbusDataU'
        'nitS2_',
        self._valueOf(read), self._valueOf(write),
    )
    from . import QModbusRequest
    return QModbusRequest._cuteOwning(address)

  def isOpen(self) -> bool:
    """
    Calls Qt's 'bool QModbusClientPrivate::isOpen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusclientprivate.html#isOpen
    """
    #  bool QModbusClientPrivate::isOpen() const
    ritual = 'ritual_ZNK20QModbusClientPrivate6isOpenEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QModbusClientPrivate6isOpenEv'
    return self.uglySide.call(ritual)

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

  def q_func(self) -> Optional[QModbusClient]:
    """
    Calls Qt's 'QModbusClient *QModbusClientPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusclientprivate.html#q_func

    Returns
    -------

    Optional[QModbusClient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusClient *QModbusClientPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QModbusClientPrivate6q_funcEv')
    from . import QModbusClient
    return QModbusClient._cuteAt(address)

  @overload(QModbusResponse, QModbusDataUnit)
  @overload(QModbusResponse, NoneType)
  def processResponse(
      self,
      response: QModbusResponse,
      data: Optional[QModbusDataUnit],
  ) -> bool:
    """
    Calls Qt's 'bool QModbusClientPrivate::processResponse(const
    QModbusResponse &response, QModbusDataUnit *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusclientprivate.html#processResponse

    Parameters
    ----------

    response : QModbusResponse
      Passed on as a value: Qt reads the C++ QModbusResponse, which stays
      Python's own.

    data : Optional[QModbusDataUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QModbusClientPrivate::processResponse(const QModbusResponse
    #      &response, QModbusDataUnit *data)
    return self.uglySide.call(
        'ritual_ZN20QModbusClientPrivate15processResponseERK15QModbusRespon'
        'seP15QModbusDataUnit',
        self._valueOf(response), self._addressOf(data),
    )

  @overload(QModbusResponse, QModbusDataUnit)
  @overload(QModbusResponse, NoneType)
  def processReadCoilsResponse(
      self,
      response: QModbusResponse,
      data: Optional[QModbusDataUnit],
  ) -> bool:
    """
    Calls Qt's 'bool QModbusClientPrivate::processReadCoilsResponse(const
    QModbusResponse &response, QModbusDataUnit *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusclientprivate.html#processReadCoilsResponse

    Parameters
    ----------

    response : QModbusResponse
      Passed on as a value: Qt reads the C++ QModbusResponse, which stays
      Python's own.

    data : Optional[QModbusDataUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QModbusClientPrivate::processReadCoilsResponse(const
    #      QModbusResponse &response, QModbusDataUnit *data)
    return self.uglySide.call(
        'ritual_ZN20QModbusClientPrivate24processReadCoilsResponseERK15QMod'
        'busResponseP15QModbusDataUnit',
        self._valueOf(response), self._addressOf(data),
    )

  @overload(QModbusRequest, int, QModbusDataUnit, QModbusReply.ReplyType)
  def enqueueRequest(
      self,
      a0: QModbusRequest,
      a1: int,
      a2: QModbusDataUnit,
      a3: QModbusReply.ReplyType,
  ) -> Optional[QModbusReply]:
    """
    Calls Qt's 'QModbusReply *QModbusClientPrivate::enqueueRequest(const
    QModbusRequest &a0, int a1, const QModbusDataUnit &a2,
    QModbusReply::ReplyType a3)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusclientprivate.html#enqueueRequest

    Parameters
    ----------

    a0 : QModbusRequest
      Passed on as a value: Qt reads the C++ QModbusRequest, which stays
      Python's own.

    a1 : int
      Passed on as it is.

    a2 : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.

    a3 : QModbusReply.ReplyType
      Passed on as its number.

    Returns
    -------

    Optional[QModbusReply]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusReply *QModbusClientPrivate::enqueueRequest(const
    #      QModbusRequest &a0, int a1, const QModbusDataUnit &a2,
    #      QModbusReply::ReplyType a3)
    ritual = (
        'ritual_ZN20QModbusClientPrivate14enqueueRequestERK14QModbusRequest'
        'iRK15QModbusDataUnitN12QModbusReply9ReplyTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QModbusClientPrivate14enqueueRequestERK14QModbusR'
          'equestiRK15QModbusDataUnitN12QModbusReply9ReplyTypeE')
    address = self.uglySide.call(
        ritual, self._valueOf(a0), a1, self._valueOf(a2), a3.value,
    )
    return QModbusReply._cuteAt(address)

  @overload(QModbusResponse, QueueElement)
  def processQueueElement(
      self,
      pdu: QModbusResponse,
      element: QueueElement,
  ) -> None:
    """
    Calls Qt's 'void QModbusClientPrivate::processQueueElement(const
    QModbusResponse &pdu, const QueueElement &element)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusclientprivate.html#processQueueElement

    Parameters
    ----------

    pdu : QModbusResponse
      Passed on as a value: Qt reads the C++ QModbusResponse, which stays
      Python's own.

    element : QueueElement
      Passed on as a value: Qt reads the C++
      QModbusClientPrivate::QueueElement, which stays Python's own.
    """
    #  void QModbusClientPrivate::processQueueElement(const QModbusResponse
    #      &pdu, const QueueElement &element)
    self.uglySide.call(
        'ritual_ZN20QModbusClientPrivate19processQueueElementERK15QModbusRe'
        'sponseRKNS_12QueueElementE',
        self._valueOf(pdu), self._valueOf(element),
    )

  @staticmethod
  def collateBits(*__, **_) -> Never:
    """
    Qt's 'bool QModbusClientPrivate::collateBits(const QModbusPdu &pdu,
    QModbusDataUnit::RegisterType type, QModbusDataUnit *data)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QModbusClientPrivate.collateBits' has no cute function yet. Qt's "
        "'bool QModbusClientPrivate::collateBits(const QModbusPdu &pdu, "
        "QModbusDataUnit::RegisterType type, QModbusDataUnit *data)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def collateBytes(*__, **_) -> Never:
    """
    Qt's 'bool QModbusClientPrivate::collateBytes(const QModbusPdu &pdu,
    QModbusDataUnit::RegisterType type, QModbusDataUnit *data)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QModbusClientPrivate.collateBytes' has no cute function yet. Qt's "
        "'bool QModbusClientPrivate::collateBytes(const QModbusPdu &pdu, "
        "QModbusDataUnit::RegisterType type, QModbusDataUnit *data)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def collateMultipleValues(*__, **_) -> Never:
    """
    Qt's 'bool QModbusClientPrivate::collateMultipleValues(const QModbusPdu
    &pdu, QModbusDataUnit::RegisterType type, QModbusDataUnit *data)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QModbusClientPrivate.collateMultipleValues' has no cute function "
        "yet. Qt's 'bool QModbusClientPrivate::collateMultipleValues(const "
        "QModbusPdu &pdu, QModbusDataUnit::RegisterType type, "
        "QModbusDataUnit *data)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def collateSingleValue(*__, **_) -> Never:
    """
    Qt's 'bool QModbusClientPrivate::collateSingleValue(const QModbusPdu
    &pdu, QModbusDataUnit::RegisterType type, QModbusDataUnit *data)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QModbusClientPrivate.collateSingleValue' has no cute function "
        "yet. Qt's 'bool QModbusClientPrivate::collateSingleValue(const "
        "QModbusPdu &pdu, QModbusDataUnit::RegisterType type, "
        "QModbusDataUnit *data)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def processReadDiscreteInputsResponse(*__, **_) -> Never:
    """
    Qt's 'bool QModbusClientPrivate::processReadDiscreteInputsResponse(const
    QModbusResponse &response, QModbusDataUnit *data)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'isValid'.
    """
    raise NotImplementedError(
        "'QModbusClientPrivate.processReadDiscreteInputsResponse' has no "
        "cute function yet. Qt's 'bool "
        "QModbusClientPrivate::processReadDiscreteInputsResponse(const "
        "QModbusResponse &response, QModbusDataUnit *data)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'isValid'.")

  @staticmethod
  def processReadHoldingRegistersResponse(*__, **_) -> Never:
    """
    Qt's 'bool
    QModbusClientPrivate::processReadHoldingRegistersResponse(const
    QModbusResponse &response, QModbusDataUnit *data)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'isValid'.
    """
    raise NotImplementedError(
        "'QModbusClientPrivate.processReadHoldingRegistersResponse' has no "
        "cute function yet. Qt's 'bool "
        "QModbusClientPrivate::processReadHoldingRegistersResponse(const "
        "QModbusResponse &response, QModbusDataUnit *data)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'isValid'.")

  @staticmethod
  def processReadInputRegistersResponse(*__, **_) -> Never:
    """
    Qt's 'bool QModbusClientPrivate::processReadInputRegistersResponse(const
    QModbusResponse &response, QModbusDataUnit *data)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'isValid'.
    """
    raise NotImplementedError(
        "'QModbusClientPrivate.processReadInputRegistersResponse' has no "
        "cute function yet. Qt's 'bool "
        "QModbusClientPrivate::processReadInputRegistersResponse(const "
        "QModbusResponse &response, QModbusDataUnit *data)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'isValid'.")

  @staticmethod
  def processReadWriteMultipleRegistersResponse(*__, **_) -> Never:
    """
    Qt's 'bool
    QModbusClientPrivate::processReadWriteMultipleRegistersResponse(const
    QModbusResponse &response, QModbusDataUnit *data)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'isValid'.
    """
    raise NotImplementedError(
        "'QModbusClientPrivate.processReadWriteMultipleRegistersResponse' "
        "has no cute function yet. Qt's 'bool "
        "QModbusClientPrivate::processReadWriteMultipleRegistersResponse(con"
        "st QModbusResponse &response, QModbusDataUnit *data)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'isValid'.")

  @staticmethod
  def processWriteMultipleCoilsResponse(*__, **_) -> Never:
    """
    Qt's 'bool QModbusClientPrivate::processWriteMultipleCoilsResponse(const
    QModbusResponse &response, QModbusDataUnit *data)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'isValid'.
    """
    raise NotImplementedError(
        "'QModbusClientPrivate.processWriteMultipleCoilsResponse' has no "
        "cute function yet. Qt's 'bool "
        "QModbusClientPrivate::processWriteMultipleCoilsResponse(const "
        "QModbusResponse &response, QModbusDataUnit *data)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'isValid'.")

  @staticmethod
  def processWriteMultipleRegistersResponse(*__, **_) -> Never:
    """
    Qt's 'bool
    QModbusClientPrivate::processWriteMultipleRegistersResponse(const
    QModbusResponse &response, QModbusDataUnit *data)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'isValid'.
    """
    raise NotImplementedError(
        "'QModbusClientPrivate.processWriteMultipleRegistersResponse' has "
        "no cute function yet. Qt's 'bool "
        "QModbusClientPrivate::processWriteMultipleRegistersResponse(const "
        "QModbusResponse &response, QModbusDataUnit *data)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'isValid'.")

  @staticmethod
  def processWriteSingleCoilResponse(*__, **_) -> Never:
    """
    Qt's 'bool QModbusClientPrivate::processWriteSingleCoilResponse(const
    QModbusResponse &response, QModbusDataUnit *data)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'isValid'.
    """
    raise NotImplementedError(
        "'QModbusClientPrivate.processWriteSingleCoilResponse' has no cute "
        "function yet. Qt's 'bool "
        "QModbusClientPrivate::processWriteSingleCoilResponse(const "
        "QModbusResponse &response, QModbusDataUnit *data)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'isValid'.")

  @staticmethod
  def processWriteSingleRegisterResponse(*__, **_) -> Never:
    """
    Qt's 'bool QModbusClientPrivate::processWriteSingleRegisterResponse(const
    QModbusResponse &response, QModbusDataUnit *data)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'isValid'.
    """
    raise NotImplementedError(
        "'QModbusClientPrivate.processWriteSingleRegisterResponse' has no "
        "cute function yet. Qt's 'bool "
        "QModbusClientPrivate::processWriteSingleRegisterResponse(const "
        "QModbusResponse &response, QModbusDataUnit *data)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'isValid'.")

  @staticmethod
  def sendRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusReply *QModbusClientPrivate::sendRequest(const
    QModbusRequest &request, int serverAddress, const QModbusDataUnit *const
    unit)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'QT_MODBUS'.
    """
    raise NotImplementedError(
        "'QModbusClientPrivate.sendRequest' has no cute function yet. Qt's "
        "'QModbusReply *QModbusClientPrivate::sendRequest(const "
        "QModbusRequest &request, int serverAddress, const QModbusDataUnit "
        "*const unit)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QT_MODBUS'.")

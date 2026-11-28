"""
QModbusReply binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qmodbusreply.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QModbusDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QModbusDataUnit, QModbusResponse
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModbusDataUnit = WAIT['QModbusDataUnit']
  QModbusResponse = WAIT['QModbusResponse']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QModbusReply(QObject):
  """
  The cute side of Qt's QModbusReply: a plain Python object standing in front
  of one C++ QModbusReply.

  It is built on the cute 'QObject', as Qt's QModbusReply is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QModbusReply that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'tr', 'type', 'serverAddress',
  'isFinished', 'result', 'rawResult', 'errorString', 'error', 'setResult',
  'setRawResult', 'setFinished', 'setError', 'addIntermediateError',
  'finished', 'errorOccurred', 'intermediateErrorOccurred'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QModbusReply::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QModbusReply::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QModbusReplyPrivate *QModbusReply::d_func()': gives
    'QModbusReplyPrivate', which has no cute class yet.
  - Qt's 'const QModbusReplyPrivate *QModbusReply::d_func() const': gives
    'QModbusReplyPrivate', which has no cute class yet.
  - Qt's 'QList<QModbusDevice::IntermediateError>
    QModbusReply::intermediateErrors() const': gives a type Python has no way
    to take yet.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QModbusReply is created at the first use, not by
    'QModbusReply(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QModbusReply.
  - Qt tells when it has removed the C++ QModbusReply. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QModbusReply that has no cute function yet,
    'intermediateErrors', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QModbusReply, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ReplyType(CuteNum):
    """
    The enum 'QModbusReply::ReplyType' of Qt, with the 3 names Qt gives in
    it.
    """

    Raw = Kee[int](0)
    Common = Kee[int](1)
    Broadcast = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QModbusReply::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QModbusReply::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QModbusReply2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusReply'

  #  A C++ QModbusReply Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusReply'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QModbusReply::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QModbusReply::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QModbusReply10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> ReplyType:
    """
    Calls Qt's 'ReplyType QModbusReply::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#type

    Returns
    -------

    ReplyType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ReplyType(number)' gives.
    """
    #  ReplyType QModbusReply::type() const
    return QModbusReply.ReplyType(self.uglySide.call(
        'ritual_ZNK12QModbusReply4typeEv',
    ))

  def serverAddress(self) -> int:
    """
    Calls Qt's 'int QModbusReply::serverAddress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#serverAddress
    """
    #  int QModbusReply::serverAddress() const
    return self.uglySide.call('ritual_ZNK12QModbusReply13serverAddressEv')

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QModbusReply::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#isFinished
    """
    #  bool QModbusReply::isFinished() const
    return self.uglySide.call('ritual_ZNK12QModbusReply10isFinishedEv')

  def result(self) -> QModbusDataUnit:
    """
    Calls Qt's 'QModbusDataUnit QModbusReply::result() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#result

    Returns
    -------

    QModbusDataUnit
      A new cute QModbusDataUnit around the copy Qt gave back. Python owns
      it.
    """
    #  QModbusDataUnit QModbusReply::result() const
    address = self.uglySide.call('ritual_ZNK12QModbusReply6resultEv')
    from . import QModbusDataUnit
    return QModbusDataUnit._cuteOwning(address)

  def rawResult(self) -> QModbusResponse:
    """
    Calls Qt's 'QModbusResponse QModbusReply::rawResult() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#rawResult

    Returns
    -------

    QModbusResponse
      A new cute QModbusResponse around the copy Qt gave back. Python owns
      it.
    """
    #  QModbusResponse QModbusReply::rawResult() const
    address = self.uglySide.call('ritual_ZNK12QModbusReply9rawResultEv')
    from . import QModbusResponse
    return QModbusResponse._cuteOwning(address)

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QModbusReply::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QModbusReply::errorString() const
    return self.uglySide.call('ritual_ZNK12QModbusReply11errorStringEv')

  def error(self) -> QModbusDevice.Error:
    """
    Calls Qt's 'QModbusDevice::Error QModbusReply::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#error

    Returns
    -------

    QModbusDevice.Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QModbusDevice.Error(number)' gives.
    """
    #  QModbusDevice::Error QModbusReply::error() const
    return QModbusDevice.Error(self.uglySide.call(
        'ritual_ZNK12QModbusReply5errorEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModbusDataUnit)
  def setResult(self, unit: QModbusDataUnit) -> None:
    """
    Calls Qt's 'void QModbusReply::setResult(const QModbusDataUnit &unit)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#setResult

    Parameters
    ----------

    unit : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.
    """
    #  void QModbusReply::setResult(const QModbusDataUnit &unit)
    self.uglySide.call(
        'ritual_ZN12QModbusReply9setResultERK15QModbusDataUnit',
        self._valueOf(unit),
    )

  @overload(QModbusResponse)
  def setRawResult(self, unit: QModbusResponse) -> None:
    """
    Calls Qt's 'void QModbusReply::setRawResult(const QModbusResponse
    &unit)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#setRawResult

    Parameters
    ----------

    unit : QModbusResponse
      Passed on as a value: Qt reads the C++ QModbusResponse, which stays
      Python's own.
    """
    #  void QModbusReply::setRawResult(const QModbusResponse &unit)
    self.uglySide.call(
        'ritual_ZN12QModbusReply12setRawResultERK15QModbusResponse',
        self._valueOf(unit),
    )

  @overload(bool)
  def setFinished(self, isFinished: bool) -> None:
    """
    Calls Qt's 'void QModbusReply::setFinished(bool isFinished)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#setFinished

    Parameters
    ----------

    isFinished : bool
      Passed on as it is.
    """
    #  void QModbusReply::setFinished(bool isFinished)
    self.uglySide.call('ritual_ZN12QModbusReply11setFinishedEb', isFinished)

  @overload(QModbusDevice.Error, str)
  def setError(self, error: QModbusDevice.Error, errorText: str) -> None:
    """
    Calls Qt's 'void QModbusReply::setError(QModbusDevice::Error error, const
    QString &errorText)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#setError

    Parameters
    ----------

    error : QModbusDevice.Error
      Passed on as its number.

    errorText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QModbusReply::setError(QModbusDevice::Error error, const QString
    #      &errorText)
    self.uglySide.call(
        'ritual_ZN12QModbusReply8setErrorEN13QModbusDevice5ErrorERK7QString',
        error.value, errorText,
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

  @overload(ReplyType, int)
  @overload(ReplyType, int, QObject)
  @overload(ReplyType, int, NoneType)
  def __init__(
      self,
      type: ReplyType,
      serverAddress: int,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QModbusReply::QModbusReply(ReplyType
    type, int serverAddress, QObject *parent)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#QModbusReply

    Parameters
    ----------

    type : ReplyType
      Passed on as its number.

    serverAddress : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QModbusReply::QModbusReply(ReplyType type, int serverAddress, QObject
    #      *parent)
    self._noteCreation(QModbusReply, lambda: Rituals.call(
        'ritual_ZN12QModbusReplyC1ENS_9ReplyTypeEiP7QObject',
        type.value, serverAddress, self._addressOf(parent, 'QObject'),
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

  @overload(QModbusDevice.IntermediateError)
  def addIntermediateError(
      self,
      error: QModbusDevice.IntermediateError,
  ) -> None:
    """
    Calls Qt's 'void
    QModbusReply::addIntermediateError(QModbusDevice::IntermediateError
    error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusreply.html#addIntermediateError

    Parameters
    ----------

    error : QModbusDevice.IntermediateError
      Passed on as its number.
    """
    #  void QModbusReply::addIntermediateError(QModbusDevice::
    #      IntermediateError error)
    self.uglySide.call(
        'ritual_ZN12QModbusReply20addIntermediateErrorEN13QModbusDevice17In'
        'termediateErrorE',
        error.value,
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QModbusReply::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#finished
    """
    #  void QModbusReply::finished()
    self.uglySide.call('ritual_ZN12QModbusReply8finishedEv')

  @overload(QModbusDevice.Error)
  def errorOccurred(self, error: QModbusDevice.Error) -> None:
    """
    Calls Qt's 'void QModbusReply::errorOccurred(QModbusDevice::Error
    error)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusreply.html#errorOccurred

    Parameters
    ----------

    error : QModbusDevice.Error
      Passed on as its number.
    """
    #  void QModbusReply::errorOccurred(QModbusDevice::Error error)
    self.uglySide.call(
        'ritual_ZN12QModbusReply13errorOccurredEN13QModbusDevice5ErrorE',
        error.value,
    )

  @overload(QModbusDevice.IntermediateError)
  def intermediateErrorOccurred(
      self,
      error: QModbusDevice.IntermediateError,
  ) -> None:
    """
    Calls Qt's 'void
    QModbusReply::intermediateErrorOccurred(QModbusDevice::IntermediateError
    error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusreply.html#intermediateErrorOccurred

    Parameters
    ----------

    error : QModbusDevice.IntermediateError
      Passed on as its number.
    """
    #  void QModbusReply::intermediateErrorOccurred(QModbusDevice::
    #      IntermediateError error)
    self.uglySide.call(
        'ritual_ZN12QModbusReply25intermediateErrorOccurredEN13QModbusDevic'
        'e17IntermediateErrorE',
        error.value,
    )

  @staticmethod
  def intermediateErrors(*__, **_) -> Never:
    """
    Qt's 'QList<QModbusDevice::IntermediateError>
    QModbusReply::intermediateErrors() const': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QModbusReply.intermediateErrors' has no cute function yet. Qt's "
        "'QList<QModbusDevice::IntermediateError> "
        "QModbusReply::intermediateErrors() const': gives a type Python has "
        "no way to take yet.")

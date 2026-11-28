"""
QCoapMessage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/qcoapmessage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QCoapOption

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QCoapMessagePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QCoapMessage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCoapMessage: a plain Python object standing in front
  of one C++ QCoapMessage.

  C++ hands a QCoapMessage around as a copy, so every C++ QCoapMessage behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCoapMessage that has a ritual and that Python can
  call so far, 20 names in all: 'version', 'type', 'token', 'tokenLength',
  'messageId', 'payload', 'setVersion', 'setToken', 'setMessageId',
  'setPayload', 'setOptions', 'optionAt', 'option', 'hasOption', 'options',
  'optionCount', 'addOption', 'removeOption', 'clearOptions', 'd_func'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoapMessage::~QCoapMessage()': the destructor: Python removes its
    C++ QCoapMessage by it, and has no other use for it.
  - Qt's 'void QCoapMessage::swap(QCoapMessage &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QCoapMessage &QCoapMessage::operator=(const QCoapMessage &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QCoapMessage &QCoapMessage::operator=(QCoapMessage &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCoapMessage::setType(const Type &type)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QCoapMessage::QCoapMessage(QCoapMessagePrivate &dd)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QCoapMessagePrivate *QCoapMessage::d_func() const': takes in
    Python what 'QCoapMessagePrivate *QCoapMessage::d_func()' takes.

  What to expect
  --------------

  - The C++ QCoapMessage is created at the first use, not by
    'QCoapMessage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCoapMessage back gives a copy the ritual made for
    Python, in a new cute QCoapMessage.
  - Each name of Qt's QCoapMessage that has no cute function yet, 'setType',
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QCoapMessage, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum, scoped=True):
    """
    The enum 'QCoapMessage::Type' of Qt, with the 4 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Confirmable = Kee[int](0)
    NonConfirmable = Kee[int](1)
    Acknowledgment = Kee[int](2)
    Reset = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapMessage'

  #  Qt's '~QCoapMessage()'. Naming it makes this a value class: Python owns
  #  every C++ QCoapMessage behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QCoapMessageD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def version(self) -> int:
    """
    Calls Qt's 'quint8 QCoapMessage::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#version
    """
    #  quint8 QCoapMessage::version() const
    return self.uglySide.call('ritual_ZNK12QCoapMessage7versionEv')

  def type(self) -> Type:
    """
    Calls Qt's 'Type QCoapMessage::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QCoapMessage::type() const
    return QCoapMessage.Type(self.uglySide.call(
        'ritual_ZNK12QCoapMessage4typeEv',
    ))

  def token(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCoapMessage::token() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#token

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCoapMessage::token() const
    address = self.uglySide.call('ritual_ZNK12QCoapMessage5tokenEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def tokenLength(self) -> int:
    """
    Calls Qt's 'quint8 QCoapMessage::tokenLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#tokenLength
    """
    #  quint8 QCoapMessage::tokenLength() const
    return self.uglySide.call('ritual_ZNK12QCoapMessage11tokenLengthEv')

  def messageId(self) -> int:
    """
    Calls Qt's 'quint16 QCoapMessage::messageId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#messageId
    """
    #  quint16 QCoapMessage::messageId() const
    return self.uglySide.call('ritual_ZNK12QCoapMessage9messageIdEv')

  def payload(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QCoapMessage::payload() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#payload

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QCoapMessage::payload() const
    address = self.uglySide.call('ritual_ZNK12QCoapMessage7payloadEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(int)
  def optionAt(self, index: int) -> QCoapOption:
    """
    Calls Qt's 'QCoapOption QCoapMessage::optionAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#optionAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QCoapOption
      A new cute QCoapOption around the copy Qt gave back. Python owns it.
    """
    #  QCoapOption QCoapMessage::optionAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK12QCoapMessage8optionAtEi', index,
    )
    return QCoapOption._cuteOwning(address)

  @overload(QCoapOption.OptionName)
  def option(self, name: QCoapOption.OptionName) -> QCoapOption:
    """
    Calls Qt's 'QCoapOption QCoapMessage::option(QCoapOption::OptionName
    name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#option

    Parameters
    ----------

    name : QCoapOption.OptionName
      Passed on as its number.

    Returns
    -------

    QCoapOption
      A new cute QCoapOption around the copy Qt gave back. Python owns it.
    """
    #  QCoapOption QCoapMessage::option(QCoapOption::OptionName name) const
    address = self.uglySide.call(
        'ritual_ZNK12QCoapMessage6optionEN11QCoapOption10OptionNameE',
        name.value,
    )
    return QCoapOption._cuteOwning(address)

  @overload(QCoapOption.OptionName)
  def hasOption(self, name: QCoapOption.OptionName) -> bool:
    """
    Calls Qt's 'bool QCoapMessage::hasOption(QCoapOption::OptionName name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#hasOption

    Parameters
    ----------

    name : QCoapOption.OptionName
      Passed on as its number.
    """
    #  bool QCoapMessage::hasOption(QCoapOption::OptionName name) const
    return self.uglySide.call(
        'ritual_ZNK12QCoapMessage9hasOptionEN11QCoapOption10OptionNameE',
        name.value,
    )

  @overload()
  def options(self) -> QList[QCoapOption]:
    """
    Calls Qt's 'const QList<QCoapOption> &QCoapMessage::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#options

    Returns
    -------

    QList[QCoapOption]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QList<QCoapOption> &QCoapMessage::options() const
    address = self.uglySide.call('ritual_ZNK12QCoapMessage7optionsEv')
    return QList[QCoapOption]._cuteOwning(address)

  @overload(QCoapOption.OptionName)
  def options(self, name: QCoapOption.OptionName) -> QList[QCoapOption]:
    """
    Calls Qt's 'QList<QCoapOption>
    QCoapMessage::options(QCoapOption::OptionName name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#options

    Parameters
    ----------

    name : QCoapOption.OptionName
      Passed on as its number.

    Returns
    -------

    QList[QCoapOption]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCoapOption> QCoapMessage::options(QCoapOption::OptionName name)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK12QCoapMessage7optionsEN11QCoapOption10OptionNameE',
        name.value,
    )
    return QList[QCoapOption]._cuteOwning(address)

  def optionCount(self) -> int:
    """
    Calls Qt's 'int QCoapMessage::optionCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#optionCount
    """
    #  int QCoapMessage::optionCount() const
    return self.uglySide.call('ritual_ZNK12QCoapMessage11optionCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setVersion(self, version: int) -> None:
    """
    Calls Qt's 'void QCoapMessage::setVersion(quint8 version)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#setVersion

    Parameters
    ----------

    version : int
      Passed on as it is.
    """
    #  void QCoapMessage::setVersion(quint8 version)
    self.uglySide.call('ritual_ZN12QCoapMessage10setVersionEh', version)

  @overload(QByteArray)
  def setToken(self, token: QByteArray) -> None:
    """
    Calls Qt's 'void QCoapMessage::setToken(const QByteArray &token)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#setToken

    Parameters
    ----------

    token : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QCoapMessage::setToken(const QByteArray &token)
    self.uglySide.call(
        'ritual_ZN12QCoapMessage8setTokenERK10QByteArray',
        self._valueOf(token),
    )

  @overload(int)
  def setMessageId(self, a0: int) -> None:
    """
    Calls Qt's 'void QCoapMessage::setMessageId(quint16 a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#setMessageId

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QCoapMessage::setMessageId(quint16 a0)
    self.uglySide.call('ritual_ZN12QCoapMessage12setMessageIdEt', a0)

  @overload(QByteArray)
  def setPayload(self, payload: QByteArray) -> None:
    """
    Calls Qt's 'void QCoapMessage::setPayload(const QByteArray &payload)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#setPayload

    Parameters
    ----------

    payload : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QCoapMessage::setPayload(const QByteArray &payload)
    self.uglySide.call(
        'ritual_ZN12QCoapMessage10setPayloadERK10QByteArray',
        self._valueOf(payload),
    )

  @overload(QList[QCoapOption])
  def setOptions(self, options: QList[QCoapOption]) -> None:
    """
    Calls Qt's 'void QCoapMessage::setOptions(const QList<QCoapOption>
    &options)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#setOptions

    Parameters
    ----------

    options : QList[QCoapOption]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCoapMessage::setOptions(const QList<QCoapOption> &options)
    self.uglySide.call(
        'ritual_ZN12QCoapMessage10setOptionsERK5QListI11QCoapOptionE',
        self._valueOf(options),
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
    Notes what was given, for Qt's 'QCoapMessage::QCoapMessage()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#QCoapMessage
    """
    #  QCoapMessage::QCoapMessage()
    self._noteCreation(QCoapMessage, lambda: Rituals.call(
        'ritual_ZN12QCoapMessageC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QCoapMessage) -> None:
    """
    Notes what was given, for Qt's 'QCoapMessage::QCoapMessage(const
    QCoapMessage &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#QCoapMessage

    Parameters
    ----------

    other : QCoapMessage
      Passed on as a value: Qt reads the C++ QCoapMessage, which stays
      Python's own.
    """
    #  QCoapMessage::QCoapMessage(const QCoapMessage &other)
    self._noteCreation(QCoapMessage, lambda: Rituals.call(
        'ritual_ZN12QCoapMessageC1ERKS_', self._valueOf(other),
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

  @overload(QCoapOption.OptionName)
  @overload(QCoapOption.OptionName, QByteArray)
  def addOption(
      self,
      name: QCoapOption.OptionName,
      value: Optional[QByteArray] = None,
  ) -> None:
    """
    Calls Qt's 'void QCoapMessage::addOption(QCoapOption::OptionName name,
    const QByteArray &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#addOption

    Parameters
    ----------

    name : QCoapOption.OptionName
      Passed on as its number.

    value : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  void QCoapMessage::addOption(QCoapOption::OptionName name, const
    #      QByteArray &value)
    if value is None:
      from ..QtCore import QByteArray
      value = QByteArray()
    self.uglySide.call(
        'ritual_ZN12QCoapMessage9addOptionEN11QCoapOption10OptionNameERK10Q'
        'ByteArray',
        name.value, self._valueOf(value),
    )

  @overload(QCoapOption)
  def addOption(self, option: QCoapOption) -> None:
    """
    Calls Qt's 'void QCoapMessage::addOption(const QCoapOption &option)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#addOption

    Parameters
    ----------

    option : QCoapOption
      Passed on as a value: Qt reads the C++ QCoapOption, which stays
      Python's own.
    """
    #  void QCoapMessage::addOption(const QCoapOption &option)
    self.uglySide.call(
        'ritual_ZN12QCoapMessage9addOptionERK11QCoapOption',
        self._valueOf(option),
    )

  @overload(QCoapOption)
  def removeOption(self, option: QCoapOption) -> None:
    """
    Calls Qt's 'void QCoapMessage::removeOption(const QCoapOption &option)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#removeOption

    Parameters
    ----------

    option : QCoapOption
      Passed on as a value: Qt reads the C++ QCoapOption, which stays
      Python's own.
    """
    #  void QCoapMessage::removeOption(const QCoapOption &option)
    self.uglySide.call(
        'ritual_ZN12QCoapMessage12removeOptionERK11QCoapOption',
        self._valueOf(option),
    )

  @overload(QCoapOption.OptionName)
  def removeOption(self, name: QCoapOption.OptionName) -> None:
    """
    Calls Qt's 'void QCoapMessage::removeOption(QCoapOption::OptionName
    name)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#removeOption

    Parameters
    ----------

    name : QCoapOption.OptionName
      Passed on as its number.
    """
    #  void QCoapMessage::removeOption(QCoapOption::OptionName name)
    self.uglySide.call(
        'ritual_ZN12QCoapMessage12removeOptionEN11QCoapOption10OptionNameE',
        name.value,
    )

  def clearOptions(self) -> None:
    """
    Calls Qt's 'void QCoapMessage::clearOptions()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#clearOptions
    """
    #  void QCoapMessage::clearOptions()
    self.uglySide.call('ritual_ZN12QCoapMessage12clearOptionsEv')

  def d_func(self) -> Optional[QCoapMessagePrivate]:
    """
    Calls Qt's 'QCoapMessagePrivate *QCoapMessage::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapmessage.html#d_func

    Returns
    -------

    Optional[QCoapMessagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapMessagePrivate *QCoapMessage::d_func()
    address = self.uglySide.call('ritual_ZN12QCoapMessage6d_funcEv')
    from . import QCoapMessagePrivate
    return QCoapMessagePrivate._cuteAt(address)

  @staticmethod
  def setType(*__, **_) -> Never:
    """
    Qt's 'void QCoapMessage::setType(const Type &type)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCoapMessage.setType' has no cute function yet. Qt's 'void "
        "QCoapMessage::setType(const Type &type)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCoapMessage::swap(QCoapMessage &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCoapMessage.swap' has no cute function yet. Qt's 'void "
        "QCoapMessage::swap(QCoapMessage &other)': takes a type Python has "
        "no way to hand over yet.")

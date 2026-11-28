"""
QCoapInternalMessage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCoap/6.12.0/QtCoap/private/qcoapinternalmessage_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCoapInternalMessage to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QCoapOption

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl
  from . import QCoapInternalMessagePrivate, QCoapMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QUrl = WAIT['QUrl']


class QCoapInternalMessage(QObject):
  """
  The cute side of Qt's QCoapInternalMessage: a plain Python object standing
  in front of one C++ QCoapInternalMessage.

  It is built on the cute 'QObject', as Qt's QCoapInternalMessage is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoapInternalMessage that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'addOption',
  'removeOption', 'message', 'currentBlockNumber', 'hasMoreBlocksToReceive',
  'blockSize', 'isValid', 'isUrlValid', 'setFromDescriptiveBlockOption',
  'd_func'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCoapInternalMessage::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QCoapInternalMessage::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QCoapInternalMessage::~QCoapInternalMessage()': the destructor:
    Python never removes a C++ QCoapInternalMessage.
  - Qt's 'const QCoapMessage *QCoapInternalMessage::message() const': takes
    in Python what 'QCoapMessage *QCoapInternalMessage::message()' takes.
  - Qt's 'const QCoapInternalMessagePrivate *QCoapInternalMessage::d_func()
    const': takes in Python what 'QCoapInternalMessagePrivate
    *QCoapInternalMessage::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 24 functions Qt declares: 4 leans on 'QCoapInternalMessage; 2 not
  a gap.

  What to expect
  --------------

  - The C++ QCoapInternalMessage is created at the first use, not by
    'QCoapInternalMessage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoapInternalMessage.
  - Qt tells when it has removed the C++ QCoapInternalMessage. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCoapInternalMessage that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QUrl)
  def isUrlValid(url: QUrl) -> bool:
    """
    Calls Qt's 'bool QCoapInternalMessage::isUrlValid(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalmessage.html#isUrlValid

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QCoapInternalMessage::isUrlValid(const QUrl &url)
    return Rituals.call(
        'ritual_ZN20QCoapInternalMessage10isUrlValidERK4QUrl',
        CuteMixin._valueOf(url),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoapInternalMessage'

  #  A C++ QCoapInternalMessage Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCoapInternalMessage'

  #  The functions Qt calls itself that QCoapInternalMessage is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'addOption': (
          ('_ZN20QCoapInternalMessage9addOptionERK11QCoapOption',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCoap:QCoapOption'),
           )),
      ),
      'isValid': (
          ('_ZNK20QCoapInternalMessage7isValidEv',
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCoapInternalMessage::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalmessage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCoapInternalMessage::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QCoapInternalMessage10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentBlockNumber(self) -> int:
    """
    Calls Qt's 'uint QCoapInternalMessage::currentBlockNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalmessage.html#currentBlockNumber
    """
    #  uint QCoapInternalMessage::currentBlockNumber() const
    return self.uglySide.call(
        'ritual_ZNK20QCoapInternalMessage18currentBlockNumberEv',
    )

  def hasMoreBlocksToReceive(self) -> bool:
    """
    Calls Qt's 'bool QCoapInternalMessage::hasMoreBlocksToReceive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalmessage.html#hasMoreBlocksToReceive
    """
    #  bool QCoapInternalMessage::hasMoreBlocksToReceive() const
    return self.uglySide.call(
        'ritual_ZNK20QCoapInternalMessage22hasMoreBlocksToReceiveEv',
    )

  def blockSize(self) -> int:
    """
    Calls Qt's 'uint QCoapInternalMessage::blockSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalmessage.html#blockSize
    """
    #  uint QCoapInternalMessage::blockSize() const
    return self.uglySide.call('ritual_ZNK20QCoapInternalMessage9blockSizeEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QCoapInternalMessage::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapinternalmessage.html#isValid
    """
    #  bool QCoapInternalMessage::isValid() const
    ritual = 'ritual_ZNK20QCoapInternalMessage7isValidEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QCoapInternalMessage7isValidEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCoapOption)
  def setFromDescriptiveBlockOption(self, option: QCoapOption) -> None:
    """
    Calls Qt's 'void
    QCoapInternalMessage::setFromDescriptiveBlockOption(const QCoapOption
    &option)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalmessage.html

    Parameters
    ----------

    option : QCoapOption
      Passed on as a value: Qt reads the C++ QCoapOption, which stays
      Python's own.
    """
    #  void QCoapInternalMessage::setFromDescriptiveBlockOption(const
    #      QCoapOption &option)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalMessage29setFromDescriptiveBlockOptionERK1'
        '1QCoapOption',
        self._valueOf(option),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QCoapInternalMessage::QCoapInternalMessage(QObject *parent)':
      leans on 'QCoapInternalMessage::qt_metacall(QMetaObject::Call, int,
      void**)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    - Qt's 'QCoapInternalMessage::QCoapInternalMessage(const QCoapMessage
      &message, QObject *parent)': leans on
      'QCoapInternalMessage::qt_metacall(QMetaObject::Call, int, void**)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    - Qt's
      'QCoapInternalMessage::QCoapInternalMessage(QCoapInternalMessagePrivate
      &dd, QObject *parent)': leans on
      'QCoapInternalMessage::qt_metacall(QMetaObject::Call, int, void**)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QCoapInternalMessage.__init__' has no cute function yet. Qt's "
        "'QCoapInternalMessage::QCoapInternalMessage(QObject *parent)': "
        "leans on 'QCoapInternalMessage::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QCoapInternalMessage::QCoapInternalMessage(const QCoapMessage "
        "&message, QObject *parent)': leans on "
        "'QCoapInternalMessage::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken. Qt's "
        "'QCoapInternalMessage::QCoapInternalMessage(QCoapInternalMessagePri"
        "vate &dd, QObject *parent)': leans on "
        "'QCoapInternalMessage::qt_metacall(QMetaObject::Call, int, "
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

  @overload(QCoapOption.OptionName, QByteArray)
  def addOption(
      self,
      name: QCoapOption.OptionName,
      value: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QCoapInternalMessage::addOption(QCoapOption::OptionName
    name, const QByteArray &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalmessage.html#addOption

    Parameters
    ----------

    name : QCoapOption.OptionName
      Passed on as its number.

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QCoapInternalMessage::addOption(QCoapOption::OptionName name,
    #      const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalMessage9addOptionEN11QCoapOption10OptionNa'
        'meERK10QByteArray',
        name.value, self._valueOf(value),
    )

  @overload(QCoapOption.OptionName, int)
  def addOption(self, name: QCoapOption.OptionName, value: int) -> None:
    """
    Calls Qt's 'void QCoapInternalMessage::addOption(QCoapOption::OptionName
    name, quint32 value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalmessage.html#addOption

    Parameters
    ----------

    name : QCoapOption.OptionName
      Passed on as its number.

    value : int
      Passed on as it is.
    """
    #  void QCoapInternalMessage::addOption(QCoapOption::OptionName name,
    #      quint32 value)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalMessage9addOptionEN11QCoapOption10OptionNa'
        'meEj',
        name.value, value,
    )

  @overload(QCoapOption)
  def addOption(self, option: QCoapOption) -> None:
    """
    Calls Qt's 'void QCoapInternalMessage::addOption(const QCoapOption
    &option)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalmessage.html#addOption

    Parameters
    ----------

    option : QCoapOption
      Passed on as a value: Qt reads the C++ QCoapOption, which stays
      Python's own.
    """
    #  void QCoapInternalMessage::addOption(const QCoapOption &option)
    ritual = 'ritual_ZN20QCoapInternalMessage9addOptionERK11QCoapOption'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QCoapInternalMessage9addOptionERK11QCoapOption')
    self.uglySide.call(ritual, self._valueOf(option))

  @overload(QCoapOption.OptionName)
  def removeOption(self, name: QCoapOption.OptionName) -> None:
    """
    Calls Qt's 'void
    QCoapInternalMessage::removeOption(QCoapOption::OptionName name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoapinternalmessage.html#removeOption

    Parameters
    ----------

    name : QCoapOption.OptionName
      Passed on as its number.
    """
    #  void QCoapInternalMessage::removeOption(QCoapOption::OptionName name)
    self.uglySide.call(
        'ritual_ZN20QCoapInternalMessage12removeOptionEN11QCoapOption10Opti'
        'onNameE',
        name.value,
    )

  def message(self) -> Optional[QCoapMessage]:
    """
    Calls Qt's 'QCoapMessage *QCoapInternalMessage::message()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapinternalmessage.html#message

    Returns
    -------

    Optional[QCoapMessage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapMessage *QCoapInternalMessage::message()
    address = self.uglySide.call('ritual_ZN20QCoapInternalMessage7messageEv')
    from . import QCoapMessage
    return QCoapMessage._cuteAt(address)

  def d_func(self) -> Optional[QCoapInternalMessagePrivate]:
    """
    Calls Qt's 'QCoapInternalMessagePrivate *QCoapInternalMessage::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoapinternalmessage.html#d_func

    Returns
    -------

    Optional[QCoapInternalMessagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCoapInternalMessagePrivate *QCoapInternalMessage::d_func()
    address = self.uglySide.call('ritual_ZN20QCoapInternalMessage6d_funcEv')
    from . import QCoapInternalMessagePrivate
    return QCoapInternalMessagePrivate._cuteAt(address)

"""
QAbstractProtobufSerializer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/qabstractprotobufserializer.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QByteArrayView
  from . import QProtobufMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QProtobufMessage = WAIT['QProtobufMessage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractProtobufSerializer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractProtobufSerializer: a plain Python object
  standing in front of one C++ QAbstractProtobufSerializer.

  What exists
  -----------

  Every function of Qt's QAbstractProtobufSerializer that has a ritual and
  that Python can call so far, 6 names in all: 'serialize', 'deserialize',
  'lastError', 'lastErrorString', 'serializeMessage', 'deserializeMessage'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractProtobufSerializer::~QAbstractProtobufSerializer()': the
    destructor: Python never removes a C++ QAbstractProtobufSerializer.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QAbstractProtobufSerializer is created at the first use, not by
    'QAbstractProtobufSerializer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractProtobufSerializer.
  """

  #  The enums Qt writes inside QAbstractProtobufSerializer, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Error(CuteNum, scoped=True):
    """
    The enum 'QAbstractProtobufSerializer::Error' of Qt, with the 5 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NULL = Kee[int](0)
    InvalidHeader = Kee[int](1)
    UnknownType = Kee[int](2)
    UnexpectedEndOfStream = Kee[int](3)
    InvalidFormat = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractProtobufSerializer'

  #  A C++ QAbstractProtobufSerializer Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractProtobufSerializer'

  #  The functions Qt calls itself that QAbstractProtobufSerializer is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'lastError': (
          ('_ZNK27QAbstractProtobufSerializer9lastErrorEv',
           ('int', 'enum', 'QtProtobuf:QAbstractProtobufSerializer.Error'),
           ()),
      ),
      'lastErrorString': (
          ('_ZNK27QAbstractProtobufSerializer15lastErrorStringEv',
           ('address', 'text', ''),
           ()),
      ),
      'serializeMessage': (
          ('_ZNK27QAbstractProtobufSerializer16serializeMessageEPK16QProtob'
           'ufMessage',
           ('address', 'value', 'QtCore:QByteArray'),
           (
               ('address', 'address', 'QtProtobuf:QProtobufMessage'),
           )),
      ),
      'deserializeMessage': (
          ('_ZNK27QAbstractProtobufSerializer18deserializeMessageEP16QProto'
           'bufMessage14QByteArrayView',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtProtobuf:QProtobufMessage'),
               ('address', 'value', 'QtCore:QByteArrayView'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QProtobufMessage)
  @overload(NoneType)
  def serialize(self, message: Optional[QProtobufMessage]) -> QByteArray:
    """
    Calls Qt's 'QByteArray QAbstractProtobufSerializer::serialize(const
    QProtobufMessage *message) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprotobufserializer.html#serialize

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QAbstractProtobufSerializer::serialize(const
    #      QProtobufMessage *message) const
    address = self.uglySide.call(
        'ritual_ZNK27QAbstractProtobufSerializer9serializeEPK16QProtobufMes'
        'sage',
        self._addressOf(message),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QProtobufMessage, QByteArrayView)
  @overload(NoneType, QByteArrayView)
  def deserialize(
      self,
      message: Optional[QProtobufMessage],
      data: QByteArrayView,
  ) -> bool:
    """
    Calls Qt's 'bool
    QAbstractProtobufSerializer::deserialize(QProtobufMessage *message,
    QByteArrayView data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprotobufserializer.html#deserialize

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QAbstractProtobufSerializer::deserialize(QProtobufMessage
    #      *message, QByteArrayView data) const
    return self.uglySide.call(
        'ritual_ZNK27QAbstractProtobufSerializer11deserializeEP16QProtobufM'
        'essage14QByteArrayView',
        self._addressOf(message), self._valueOf(data),
    )

  def lastError(self) -> Error:
    """
    Calls Qt's 'Error QAbstractProtobufSerializer::lastError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprotobufserializer.html#lastError

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QAbstractProtobufSerializer::lastError() const
    return QAbstractProtobufSerializer.Error(self.uglySide.call(
        'ritual_ZNK27QAbstractProtobufSerializer9lastErrorEv',
    ))

  def lastErrorString(self) -> str:
    """
    Calls Qt's 'QString QAbstractProtobufSerializer::lastErrorString()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprotobufserializer.html#lastErrorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractProtobufSerializer::lastErrorString() const
    return self.uglySide.call(
        'ritual_ZNK27QAbstractProtobufSerializer15lastErrorStringEv',
    )

  @overload(QProtobufMessage)
  @overload(NoneType)
  def serializeMessage(
      self,
      message: Optional[QProtobufMessage],
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QAbstractProtobufSerializer::serializeMessage(const QProtobufMessage
    *message) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprotobufserializer.html#serializeMessage

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QAbstractProtobufSerializer::serializeMessage(const
    #      QProtobufMessage *message) const
    address = self.uglySide.call(
        'ritual_ZNK27QAbstractProtobufSerializer16serializeMessageEPK16QPro'
        'tobufMessage',
        self._addressOf(message),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QProtobufMessage, QByteArrayView)
  @overload(NoneType, QByteArrayView)
  def deserializeMessage(
      self,
      message: Optional[QProtobufMessage],
      data: QByteArrayView,
  ) -> bool:
    """
    Calls Qt's 'bool
    QAbstractProtobufSerializer::deserializeMessage(QProtobufMessage
    *message, QByteArrayView data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprotobufserializer.html

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QAbstractProtobufSerializer::deserializeMessage(QProtobufMessage
    #      *message, QByteArrayView data) const
    return self.uglySide.call(
        'ritual_ZNK27QAbstractProtobufSerializer18deserializeMessageEP16QPr'
        'otobufMessage14QByteArrayView',
        self._addressOf(message), self._valueOf(data),
    )

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractProtobufSerializer::QAbstractProtobufSerializer()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprotobufserializer.html
    """
    #  QAbstractProtobufSerializer::QAbstractProtobufSerializer()
    self._noteCreation(QAbstractProtobufSerializer, lambda: Rituals.call(
        'ritual_ZN27QAbstractProtobufSerializerC1Ev',
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

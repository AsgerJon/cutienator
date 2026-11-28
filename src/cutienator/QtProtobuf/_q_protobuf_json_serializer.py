"""
QProtobufJsonSerializer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/qprotobufjsonserializer.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractProtobufSerializer

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


class QProtobufJsonSerializer(QAbstractProtobufSerializer):
  """
  The cute side of Qt's QProtobufJsonSerializer: a plain Python object
  standing in front of one C++ QProtobufJsonSerializer.

  It is built on the cute 'QAbstractProtobufSerializer', as Qt's
  QProtobufJsonSerializer is built on Qt's QAbstractProtobufSerializer, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QProtobufJsonSerializer that has a ritual and that
  Python can call so far, 4 names in all: 'lastError', 'lastErrorString',
  'serializeMessage', 'deserializeMessage'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QProtobufJsonSerializer::~QProtobufJsonSerializer()': the
    destructor: Python never removes a C++ QProtobufJsonSerializer.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QProtobufJsonSerializer is created at the first use, not by
    'QProtobufJsonSerializer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProtobufJsonSerializer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProtobufJsonSerializer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def lastError(self) -> QAbstractProtobufSerializer.Error:
    """
    Calls Qt's 'Error QProtobufJsonSerializer::lastError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufjsonserializer.html#lastError

    Returns
    -------

    QAbstractProtobufSerializer.Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractProtobufSerializer.Error(number)' gives.
    """
    #  Error QProtobufJsonSerializer::lastError() const
    return QAbstractProtobufSerializer.Error(self.uglySide.call(
        'ritual_ZNK23QProtobufJsonSerializer9lastErrorEv',
    ))

  def lastErrorString(self) -> str:
    """
    Calls Qt's 'QString QProtobufJsonSerializer::lastErrorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufjsonserializer.html#lastErrorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProtobufJsonSerializer::lastErrorString() const
    return self.uglySide.call(
        'ritual_ZNK23QProtobufJsonSerializer15lastErrorStringEv',
    )

  @overload(QProtobufMessage)
  @overload(NoneType)
  def serializeMessage(
      self,
      message: Optional[QProtobufMessage],
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QProtobufJsonSerializer::serializeMessage(const
    QProtobufMessage *message) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufjsonserializer.html#serializeMessage

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
    #  QByteArray QProtobufJsonSerializer::serializeMessage(const
    #      QProtobufMessage *message) const
    address = self.uglySide.call(
        'ritual_ZNK23QProtobufJsonSerializer16serializeMessageEPK16QProtobu'
        'fMessage',
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
    QProtobufJsonSerializer::deserializeMessage(QProtobufMessage *message,
    QByteArrayView data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufjsonserializer.html#deserializeMessage

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QProtobufJsonSerializer::deserializeMessage(QProtobufMessage
    #      *message, QByteArrayView data) const
    return self.uglySide.call(
        'ritual_ZNK23QProtobufJsonSerializer18deserializeMessageEP16QProtob'
        'ufMessage14QByteArrayView',
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
    'QProtobufJsonSerializer::QProtobufJsonSerializer()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufjsonserializer.html
    """
    #  QProtobufJsonSerializer::QProtobufJsonSerializer()
    self._noteCreation(QProtobufJsonSerializer, lambda: Rituals.call(
        'ritual_ZN23QProtobufJsonSerializerC1Ev',
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

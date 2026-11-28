"""
QProtobufSerializer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/qprotobufserializer.h, Qt 6.12.0. Changes made here are lost.
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


class QProtobufSerializer(QAbstractProtobufSerializer):
  """
  The cute side of Qt's QProtobufSerializer: a plain Python object standing
  in front of one C++ QProtobufSerializer.

  It is built on the cute 'QAbstractProtobufSerializer', as Qt's
  QProtobufSerializer is built on Qt's QAbstractProtobufSerializer, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QProtobufSerializer that has a ritual and that
  Python can call so far, 5 names in all: 'lastError', 'lastErrorString',
  'shouldPreserveUnknownFields', 'serializeMessage', 'deserializeMessage'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QProtobufSerializer::~QProtobufSerializer()': the destructor:
    Python never removes a C++ QProtobufSerializer.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QProtobufSerializer is created at the first use, not by
    'QProtobufSerializer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProtobufSerializer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProtobufSerializer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def lastError(self) -> QAbstractProtobufSerializer.Error:
    """
    Calls Qt's 'Error QProtobufSerializer::lastError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprotobufserializer.html#lastError

    Returns
    -------

    QAbstractProtobufSerializer.Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractProtobufSerializer.Error(number)' gives.
    """
    #  Error QProtobufSerializer::lastError() const
    return QAbstractProtobufSerializer.Error(self.uglySide.call(
        'ritual_ZNK19QProtobufSerializer9lastErrorEv',
    ))

  def lastErrorString(self) -> str:
    """
    Calls Qt's 'QString QProtobufSerializer::lastErrorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializer.html#lastErrorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProtobufSerializer::lastErrorString() const
    return self.uglySide.call(
        'ritual_ZNK19QProtobufSerializer15lastErrorStringEv',
    )

  @overload(QProtobufMessage)
  @overload(NoneType)
  def serializeMessage(
      self,
      message: Optional[QProtobufMessage],
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray QProtobufSerializer::serializeMessage(const
    QProtobufMessage *message) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializer.html#serializeMessage

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
    #  QByteArray QProtobufSerializer::serializeMessage(const
    #      QProtobufMessage *message) const
    address = self.uglySide.call(
        'ritual_ZNK19QProtobufSerializer16serializeMessageEPK16QProtobufMes'
        'sage',
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
    Calls Qt's 'bool QProtobufSerializer::deserializeMessage(QProtobufMessage
    *message, QByteArrayView data) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializer.html#deserializeMessage

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QProtobufSerializer::deserializeMessage(QProtobufMessage
    #      *message, QByteArrayView data) const
    return self.uglySide.call(
        'ritual_ZNK19QProtobufSerializer18deserializeMessageEP16QProtobufMe'
        'ssage14QByteArrayView',
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
    'QProtobufSerializer::QProtobufSerializer()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializer.html#QProtobufSerializer
    """
    #  QProtobufSerializer::QProtobufSerializer()
    self._noteCreation(QProtobufSerializer, lambda: Rituals.call(
        'ritual_ZN19QProtobufSerializerC1Ev',
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

  @overload(bool)
  def shouldPreserveUnknownFields(self, preserveUnknownFields: bool) -> None:
    """
    Calls Qt's 'void QProtobufSerializer::shouldPreserveUnknownFields(bool
    preserveUnknownFields)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializer.html

    Parameters
    ----------

    preserveUnknownFields : bool
      Passed on as it is.
    """
    #  void QProtobufSerializer::shouldPreserveUnknownFields(bool
    #      preserveUnknownFields)
    self.uglySide.call(
        'ritual_ZN19QProtobufSerializer27shouldPreserveUnknownFieldsEb',
        preserveUnknownFields,
    )

"""
QProtobufDeserializerBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufdeserializerbase_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QProtobufDeserializerBase to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QAbstractProtobufSerializer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QProtobufMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QProtobufMessage = WAIT['QProtobufMessage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProtobufDeserializerBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QProtobufDeserializerBase: a plain Python object
  standing in front of one C++ QProtobufDeserializerBase.

  What exists
  -----------

  Every function of Qt's QProtobufDeserializerBase that has a ritual and that
  Python can call so far, 4 names in all: 'clearCachedValue', 'setError',
  'deserializeMessageField', 'nextFieldIndex'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QProtobufDeserializerBase::deserializeEnum(QVariant &value,
    const QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QProtobufDeserializerBase::deserializeScalarField(QVariant
    &value, const QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  8 of the 14 functions Qt declares: 4 forbidden; 3 leans on
  'QtProtobufSerializerHelpers; 1 the class is abstract, so C++ cannot make
  one, and the C++ class of ours does not fill in every function it leaves
  open.

  What to expect
  --------------

  - The C++ QProtobufDeserializerBase is created at the first use, not by
    'QProtobufDeserializerBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProtobufDeserializerBase.
  - Each name of Qt's QProtobufDeserializerBase that has no cute function
    yet, '__init__', 'deserializeEnum', 'deserializeMessage',
    'deserializeScalarField', 'storeCachedValue', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProtobufDeserializerBase'

  #  A C++ QProtobufDeserializerBase Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QProtobufDeserializerBase'

  #  The functions Qt calls itself that QProtobufDeserializerBase is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setError': (
          'void '
          'QProtobufDeserializerBase::setError(QAbstractProtobufSerializer:'
          ':Error, QAnyStringView)',
      ),
      'deserializeEnum': (
          'bool QProtobufDeserializerBase::deserializeEnum(QVariant &, '
          'const QtProtobufPrivate::QProtobufFieldInfo &)',
      ),
      'deserializeScalarField': (
          'bool QProtobufDeserializerBase::deserializeScalarField(QVariant '
          '&, const QtProtobufPrivate::QProtobufFieldInfo &)',
      ),
  }

  #  The functions Qt calls itself that QProtobufDeserializerBase is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'deserializeMessageField': (
          ('_ZN25QProtobufDeserializerBase23deserializeMessageFieldEP16QPro'
           'tobufMessage',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtProtobuf:QProtobufMessage'),
           )),
      ),
      'nextFieldIndex': (
          ('_ZN25QProtobufDeserializerBase14nextFieldIndexEP16QProtobufMess'
           'age',
           ('int', 'number', ''),
           (
               ('address', 'address', 'QtProtobuf:QProtobufMessage'),
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractProtobufSerializer.Error, str)
  def setError(
      self,
      error: QAbstractProtobufSerializer.Error,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QProtobufDeserializerBase::setError(QAbstractProtobufSerializer::Error
    error, QAnyStringView errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufdeserializerbase.html#setError

    Parameters
    ----------

    error : QAbstractProtobufSerializer.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QProtobufDeserializerBase::setError(QAbstractProtobufSerializer::
    #      Error error, QAnyStringView errorString)
    self.uglySide.call(
        'ritual_ZN25QProtobufDeserializerBase8setErrorEN27QAbstractProtobuf'
        'Serializer5ErrorE14QAnyStringView',
        error.value, errorString,
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
    Qt's 'QProtobufDeserializerBase::QProtobufDeserializerBase()': the class
    is abstract, so C++ cannot make one, and the C++ class of ours does not
    fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QProtobufDeserializerBase.__init__' has no cute function yet. "
        "Qt's 'QProtobufDeserializerBase::QProtobufDeserializerBase()': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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

  def clearCachedValue(self) -> None:
    """
    Calls Qt's 'void QProtobufDeserializerBase::clearCachedValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufdeserializerbase.html#clearCachedValue
    """
    #  void QProtobufDeserializerBase::clearCachedValue()
    self.uglySide.call(
        'ritual_ZN25QProtobufDeserializerBase16clearCachedValueEv',
    )

  @overload(QProtobufMessage)
  @overload(NoneType)
  def deserializeMessageField(
      self,
      message: Optional[QProtobufMessage],
  ) -> bool:
    """
    Calls Qt's 'bool
    QProtobufDeserializerBase::deserializeMessageField(QProtobufMessage
    *message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufdeserializerbase.html

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QProtobufDeserializerBase::deserializeMessageField(
    #      QProtobufMessage *message)
    return self.uglySide.call(
        'ritual_ZN25QProtobufDeserializerBase23deserializeMessageFieldEP16Q'
        'ProtobufMessage',
        self._addressOf(message),
    )

  @overload(QProtobufMessage)
  @overload(NoneType)
  def nextFieldIndex(self, message: Optional[QProtobufMessage]) -> int:
    """
    Calls Qt's 'int
    QProtobufDeserializerBase::nextFieldIndex(QProtobufMessage *message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufdeserializerbase.html#nextFieldIndex

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QProtobufDeserializerBase::nextFieldIndex(QProtobufMessage
    #      *message)
    return self.uglySide.call(
        'ritual_ZN25QProtobufDeserializerBase14nextFieldIndexEP16QProtobufM'
        'essage',
        self._addressOf(message),
    )

  @staticmethod
  def deserializeEnum(*__, **_) -> Never:
    """
    Qt's 'bool QProtobufDeserializerBase::deserializeEnum(QVariant &value,
    const QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QProtobufDeserializerBase.deserializeEnum' has no cute function "
        "yet. Qt's 'bool "
        "QProtobufDeserializerBase::deserializeEnum(QVariant &value, const "
        "QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def deserializeMessage(*__, **_) -> Never:
    """
    Qt's 'bool QProtobufDeserializerBase::deserializeMessage(QProtobufMessage
    *message)': leans on
    'QtProtobufSerializerHelpers::setMessageProperty(QProtobufMessage*,
    QtProtobufPrivate::QProtobufFieldInfo const&, QVariant const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QProtobufDeserializerBase.deserializeMessage' has no cute "
        "function yet. Qt's 'bool "
        "QProtobufDeserializerBase::deserializeMessage(QProtobufMessage "
        "*message)': leans on "
        "'QtProtobufSerializerHelpers::setMessageProperty(QProtobufMessage*,"
        " QtProtobufPrivate::QProtobufFieldInfo const&, QVariant const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def deserializeScalarField(*__, **_) -> Never:
    """
    Qt's 'bool QProtobufDeserializerBase::deserializeScalarField(QVariant
    &value, const QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QProtobufDeserializerBase.deserializeScalarField' has no cute "
        "function yet. Qt's 'bool "
        "QProtobufDeserializerBase::deserializeScalarField(QVariant &value, "
        "const QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def storeCachedValue(*__, **_) -> Never:
    """
    Qt's 'bool QProtobufDeserializerBase::storeCachedValue(QProtobufMessage
    *message)': leans on
    'QtProtobufSerializerHelpers::setMessageProperty(QProtobufMessage*,
    QtProtobufPrivate::QProtobufFieldInfo const&, QVariant const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QProtobufDeserializerBase.storeCachedValue' has no cute function "
        "yet. Qt's 'bool "
        "QProtobufDeserializerBase::storeCachedValue(QProtobufMessage "
        "*message)': leans on "
        "'QtProtobufSerializerHelpers::setMessageProperty(QProtobufMessage*,"
        " QtProtobufPrivate::QProtobufFieldInfo const&, QVariant const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

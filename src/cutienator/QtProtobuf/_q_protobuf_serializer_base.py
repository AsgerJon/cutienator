"""
QProtobufSerializerBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufserializerbase_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QProtobufSerializerBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtProtobufPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from . import QProtobufMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QProtobufMessage = WAIT['QProtobufMessage']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProtobufSerializerBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QProtobufSerializerBase: a plain Python object
  standing in front of one C++ QProtobufSerializerBase.

  What exists
  -----------

  Every function of Qt's QProtobufSerializerBase that has a ritual and that
  Python can call so far, 6 names in all: 'serializeMessage',
  'isOneofOrOptionalField', 'serializeMessageField', 'serializeScalarField',
  'serializeMessageFieldBegin', 'serializeMessageFieldEnd'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QProtobufSerializerBase::~QProtobufSerializerBase()': the
    destructor: Python never removes a C++ QProtobufSerializerBase.
  - Qt's 'bool QProtobufSerializerBase::serializeEnum(QVariant &value, const
    QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QProtobufSerializerBase is created at the first use, not by
    'QProtobufSerializerBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProtobufSerializerBase.
  - Each name of Qt's QProtobufSerializerBase that has no cute function yet,
    '__init__', 'serializeEnum', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QtProtobufPrivate.FieldFlags)
  def isOneofOrOptionalField(flags: QtProtobufPrivate.FieldFlags) -> bool:
    """
    Calls Qt's 'bool
    QProtobufSerializerBase::isOneofOrOptionalField(QtProtobufPrivate::
    FieldFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializerbase.html

    Parameters
    ----------

    flags : QtProtobufPrivate.FieldFlags
      Passed on as its number.
    """
    #  bool QProtobufSerializerBase::isOneofOrOptionalField(
    #      QtProtobufPrivate::FieldFlags flags)
    return Rituals.call(
        'ritual_ZN23QProtobufSerializerBase22isOneofOrOptionalFieldE6QFlags'
        'IN17QtProtobufPrivate9FieldFlagEE',
        flags.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProtobufSerializerBase'

  #  A C++ QProtobufSerializerBase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QProtobufSerializerBase'

  #  The functions Qt calls itself that QProtobufSerializerBase is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'serializeEnum': (
          'bool QProtobufSerializerBase::serializeEnum(QVariant &, const '
          'QtProtobufPrivate::QProtobufFieldInfo &)',
      ),
  }

  #  The functions Qt calls itself that QProtobufSerializerBase is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'serializeMessageField': (
          ('_ZN23QProtobufSerializerBase21serializeMessageFieldEPK16QProtob'
           'ufMessageRKN17QtProtobufPrivate18QProtobufFieldInfoE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtProtobuf:QProtobufMessage'),
               ('address', 'value',
                'QtProtobuf:QtProtobufPrivate.QProtobufFieldInfo'),
           )),
      ),
      'serializeScalarField': (
          ('_ZN23QProtobufSerializerBase20serializeScalarFieldERK8QVariantR'
           'KN17QtProtobufPrivate18QProtobufFieldInfoE',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QVariant'),
               ('address', 'value',
                'QtProtobuf:QtProtobufPrivate.QProtobufFieldInfo'),
           )),
      ),
      'serializeMessageFieldBegin': (
          ('_ZN23QProtobufSerializerBase26serializeMessageFieldBeginEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'serializeMessageFieldEnd': (
          ('_ZN23QProtobufSerializerBase24serializeMessageFieldEndEPK16QPro'
           'tobufMessageRKN17QtProtobufPrivate18QProtobufFieldInfoE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtProtobuf:QProtobufMessage'),
               ('address', 'value',
                'QtProtobuf:QtProtobufPrivate.QProtobufFieldInfo'),
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
    Qt's 'QProtobufSerializerBase::QProtobufSerializerBase()': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QProtobufSerializerBase.__init__' has no cute function yet. Qt's "
        "'QProtobufSerializerBase::QProtobufSerializerBase()': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  @overload(QProtobufMessage)
  @overload(NoneType)
  def serializeMessage(self, message: Optional[QProtobufMessage]) -> None:
    """
    Calls Qt's 'void QProtobufSerializerBase::serializeMessage(const
    QProtobufMessage *message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializerbase.html#serializeMessage

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProtobufSerializerBase::serializeMessage(const QProtobufMessage
    #      *message)
    self.uglySide.call(
        'ritual_ZN23QProtobufSerializerBase16serializeMessageEPK16QProtobuf'
        'Message',
        self._addressOf(message),
    )

  @overload(QProtobufMessage, WAIT['QtProtobufPrivate.QProtobufFieldInfo'])
  @overload(NoneType, WAIT['QtProtobufPrivate.QProtobufFieldInfo'])
  def serializeMessageField(
      self,
      message: Optional[QProtobufMessage],
      fieldInfo: QtProtobufPrivate.QProtobufFieldInfo,
  ) -> None:
    """
    Calls Qt's 'void QProtobufSerializerBase::serializeMessageField(const
    QProtobufMessage *message, const QtProtobufPrivate::QProtobufFieldInfo
    &fieldInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializerbase.html#serializeMessageField

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fieldInfo : QtProtobufPrivate.QProtobufFieldInfo
      Passed on as a value: Qt reads the C++
      QtProtobufPrivate::QProtobufFieldInfo, which stays Python's own.
    """
    #  void QProtobufSerializerBase::serializeMessageField(const
    #      QProtobufMessage *message, const
    #      QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)
    ritual = (
        'ritual_ZN23QProtobufSerializerBase21serializeMessageFieldEPK16QPro'
        'tobufMessageRKN17QtProtobufPrivate18QProtobufFieldInfoE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QProtobufSerializerBase21serializeMessageFieldEPK'
          '16QProtobufMessageRKN17QtProtobufPrivate18QProtobufFieldInfoE')
    self.uglySide.call(
        ritual, self._addressOf(message), self._valueOf(fieldInfo),
    )

  @overload(QVariant, WAIT['QtProtobufPrivate.QProtobufFieldInfo'])
  def serializeScalarField(
      self,
      value: QVariant,
      fieldInfo: QtProtobufPrivate.QProtobufFieldInfo,
  ) -> bool:
    """
    Calls Qt's 'bool QProtobufSerializerBase::serializeScalarField(const
    QVariant &value, const QtProtobufPrivate::QProtobufFieldInfo
    &fieldInfo)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializerbase.html#serializeScalarField

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    fieldInfo : QtProtobufPrivate.QProtobufFieldInfo
      Passed on as a value: Qt reads the C++
      QtProtobufPrivate::QProtobufFieldInfo, which stays Python's own.
    """
    #  bool QProtobufSerializerBase::serializeScalarField(const QVariant
    #      &value, const QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)
    return self.uglySide.call(
        'ritual_ZN23QProtobufSerializerBase20serializeScalarFieldERK8QVaria'
        'ntRKN17QtProtobufPrivate18QProtobufFieldInfoE',
        self._valueOf(value), self._valueOf(fieldInfo),
    )

  def serializeMessageFieldBegin(self) -> None:
    """
    Calls Qt's 'void QProtobufSerializerBase::serializeMessageFieldBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializerbase.html
    """
    #  void QProtobufSerializerBase::serializeMessageFieldBegin()
    self.uglySide.call(
        'ritual_ZN23QProtobufSerializerBase26serializeMessageFieldBeginEv',
    )

  @overload(QProtobufMessage, WAIT['QtProtobufPrivate.QProtobufFieldInfo'])
  @overload(NoneType, WAIT['QtProtobufPrivate.QProtobufFieldInfo'])
  def serializeMessageFieldEnd(
      self,
      a0: Optional[QProtobufMessage],
      a1: QtProtobufPrivate.QProtobufFieldInfo,
  ) -> None:
    """
    Calls Qt's 'void QProtobufSerializerBase::serializeMessageFieldEnd(const
    QProtobufMessage *a0, const QtProtobufPrivate::QProtobufFieldInfo &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufserializerbase.html

    Parameters
    ----------

    a0 : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QtProtobufPrivate.QProtobufFieldInfo
      Passed on as a value: Qt reads the C++
      QtProtobufPrivate::QProtobufFieldInfo, which stays Python's own.
    """
    #  void QProtobufSerializerBase::serializeMessageFieldEnd(const
    #      QProtobufMessage *a0, const QtProtobufPrivate::QProtobufFieldInfo
    #      &a1)
    self.uglySide.call(
        'ritual_ZN23QProtobufSerializerBase24serializeMessageFieldEndEPK16Q'
        'ProtobufMessageRKN17QtProtobufPrivate18QProtobufFieldInfoE',
        self._addressOf(a0), self._valueOf(a1),
    )

  @staticmethod
  def serializeEnum(*__, **_) -> Never:
    """
    Qt's 'bool QProtobufSerializerBase::serializeEnum(QVariant &value, const
    QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QProtobufSerializerBase.serializeEnum' has no cute function yet. "
        "Qt's 'bool QProtobufSerializerBase::serializeEnum(QVariant &value, "
        "const QtProtobufPrivate::QProtobufFieldInfo &fieldInfo)': takes a "
        "type Python has no way to hand over yet.")

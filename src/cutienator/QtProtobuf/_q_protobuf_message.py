"""
QProtobufMessage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/qprotobufmessage.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QtProtobufPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QByteArrayView, QMetaObject, QVariant
  from . import QAbstractProtobufSerializer, QProtobufMessagePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractProtobufSerializer = WAIT['QAbstractProtobufSerializer']
  QByteArrayView = WAIT['QByteArrayView']
  QMetaObject = WAIT['QMetaObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProtobufMessage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QProtobufMessage: a plain Python object standing in
  front of one C++ QProtobufMessage.

  What exists
  -----------

  Every function of Qt's QProtobufMessage that has a ritual and that Python
  can call so far, 8 names in all: 'property', 'setProperty',
  'unknownFieldData', 'serialize', 'deserialize', 'propertyOrdering',
  'metaObject', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QProtobufMessage::setProperty(QAnyStringView propertyName,
    QVariant &&value)': takes a type Python has no way to hand over yet.
  - Qt's 'QProtobufMessagePointer QProtobufMessage::constructByName(const
    QString &messageType)': gives a type Python has no way to take yet.
  - Qt's 'QList<qint32> QProtobufMessage::unknownFieldNumbers() const': gives
    a type Python has no way to take yet.
  - Qt's 'QProtobufMessage::QProtobufMessage(QProtobufMessagePrivate &dd)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QProtobufMessage::~QProtobufMessage()': the destructor: Python
    never removes a C++ QProtobufMessage.
  - Qt's 'QProtobufMessage::QProtobufMessage(const QProtobufMessage &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QProtobufMessage &QProtobufMessage::operator=(const
    QProtobufMessage &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QProtobufMessage::QProtobufMessage(QProtobufMessage &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QProtobufMessage &QProtobufMessage::operator=(QProtobufMessage
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QProtobufMessage::swap(QProtobufMessage &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool operator==(const QProtobufMessage &lhs, const QProtobufMessage
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'bool operator!=(const QProtobufMessage &lhs, const QProtobufMessage
    &rhs)': an operator between other classes, written inside this one.
  - Qt's 'const QProtobufMessagePrivate *QProtobufMessage::d_func() const':
    takes in Python what 'QProtobufMessagePrivate
    *QProtobufMessage::d_func()' takes.

  What has no ritual
  ------------------

  3 of the 25 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QProtobufMessage is created at the first use, not by
    'QProtobufMessage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProtobufMessage.
  - Each name of Qt's QProtobufMessage that has no cute function yet,
    'constructByName', 'swap', 'unknownFieldNumbers', holds a function that
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
  __qt_class__ = 'QProtobufMessage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def property(self, propertyName: str) -> QVariant:
    """
    Calls Qt's 'QVariant QProtobufMessage::property(QAnyStringView
    propertyName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qprotobufmessage.html#property

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QProtobufMessage::property(QAnyStringView propertyName) const
    address = self.uglySide.call(
        'ritual_ZNK16QProtobufMessage8propertyE14QAnyStringView',
        propertyName,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int)
  def unknownFieldData(self, field: int) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QProtobufMessage::unknownFieldData(qint32
    field) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufmessage.html#unknownFieldData

    Parameters
    ----------

    field : int
      Passed on as it is.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QProtobufMessage::unknownFieldData(qint32 field)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QProtobufMessage16unknownFieldDataEi', field,
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @overload(QAbstractProtobufSerializer)
  @overload(NoneType)
  def serialize(
      self,
      serializer: Optional[QAbstractProtobufSerializer],
  ) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QProtobufMessage::serialize(QAbstractProtobufSerializer *serializer)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qprotobufmessage.html#serialize

    Parameters
    ----------

    serializer : Optional[QAbstractProtobufSerializer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QProtobufMessage::serialize(QAbstractProtobufSerializer
    #      *serializer) const
    address = self.uglySide.call(
        'ritual_ZNK16QProtobufMessage9serializeEP27QAbstractProtobufSeriali'
        'zer',
        self._addressOf(serializer),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def propertyOrdering(
      self,
  ) -> Optional[QtProtobufPrivate.QProtobufPropertyOrdering]:
    """
    Calls Qt's 'const QtProtobufPrivate::QProtobufPropertyOrdering
    *QProtobufMessage::propertyOrdering() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufmessage.html#propertyOrdering

    Returns
    -------

    Optional[QtProtobufPrivate.QProtobufPropertyOrdering]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QtProtobufPrivate::QProtobufPropertyOrdering
    #      *QProtobufMessage::propertyOrdering() const
    address = self.uglySide.call(
        'ritual_ZNK16QProtobufMessage16propertyOrderingEv',
    )
    return QtProtobufPrivate.QProtobufPropertyOrdering._cuteAt(address)

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QProtobufMessage::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprotobufmessage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QProtobufMessage::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QProtobufMessage10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QVariant)
  def setProperty(self, propertyName: str, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QProtobufMessage::setProperty(QAnyStringView
    propertyName, const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qprotobufmessage.html#setProperty

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QProtobufMessage::setProperty(QAnyStringView propertyName, const
    #      QVariant &value)
    return self.uglySide.call(
        'ritual_ZN16QProtobufMessage11setPropertyE14QAnyStringViewRK8QVaria'
        'nt',
        propertyName, self._valueOf(value),
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

  @overload(QMetaObject, WAIT['QtProtobufPrivate.QProtobufPropertyOrdering'])
  @overload(QMetaObject, NoneType)
  @overload(NoneType, WAIT['QtProtobufPrivate.QProtobufPropertyOrdering'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      metaObject: Optional[QMetaObject],
      ordering: Optional[QtProtobufPrivate.QProtobufPropertyOrdering],
  ) -> None:
    """
    Notes what was given, for Qt's 'QProtobufMessage::QProtobufMessage(const
    QMetaObject *metaObject, const
    QtProtobufPrivate::QProtobufPropertyOrdering *ordering)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufmessage.html#QProtobufMessage

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ordering : Optional[QtProtobufPrivate.QProtobufPropertyOrdering]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QProtobufMessage::QProtobufMessage(const QMetaObject *metaObject,
    #      const QtProtobufPrivate::QProtobufPropertyOrdering *ordering)
    self._noteCreation(QProtobufMessage, lambda: Rituals.call(
        'ritual_ZN16QProtobufMessageC1EPK11QMetaObjectPKN17QtProtobufPrivat'
        'e25QProtobufPropertyOrderingE',
        self._addressOf(metaObject, 'QMetaObject'),
        self._addressOf(ordering),
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

  @overload(QAbstractProtobufSerializer, QByteArrayView)
  @overload(NoneType, QByteArrayView)
  def deserialize(
      self,
      serializer: Optional[QAbstractProtobufSerializer],
      data: QByteArrayView,
  ) -> bool:
    """
    Calls Qt's 'bool
    QProtobufMessage::deserialize(QAbstractProtobufSerializer *serializer,
    QByteArrayView data)'.

    Qt's own words: https://doc.qt.io/qt-6/qprotobufmessage.html#deserialize

    Parameters
    ----------

    serializer : Optional[QAbstractProtobufSerializer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  bool QProtobufMessage::deserialize(QAbstractProtobufSerializer
    #      *serializer, QByteArrayView data)
    return self.uglySide.call(
        'ritual_ZN16QProtobufMessage11deserializeEP27QAbstractProtobufSeria'
        'lizer14QByteArrayView',
        self._addressOf(serializer), self._valueOf(data),
    )

  def d_func(self) -> Optional[QProtobufMessagePrivate]:
    """
    Calls Qt's 'QProtobufMessagePrivate *QProtobufMessage::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qprotobufmessage.html#d_func

    Returns
    -------

    Optional[QProtobufMessagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QProtobufMessagePrivate *QProtobufMessage::d_func()
    address = self.uglySide.call('ritual_ZN16QProtobufMessage6d_funcEv')
    from . import QProtobufMessagePrivate
    return QProtobufMessagePrivate._cuteAt(address)

  @staticmethod
  def constructByName(*__, **_) -> Never:
    """
    Qt's 'QProtobufMessagePointer QProtobufMessage::constructByName(const
    QString &messageType)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QProtobufMessage.constructByName' has no cute function yet. Qt's "
        "'QProtobufMessagePointer QProtobufMessage::constructByName(const "
        "QString &messageType)': gives a type Python has no way to take yet."
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QProtobufMessage::swap(QProtobufMessage &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QProtobufMessage.swap' has no cute function yet. Qt's 'void "
        "QProtobufMessage::swap(QProtobufMessage &other)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def unknownFieldNumbers(*__, **_) -> Never:
    """
    Qt's 'QList<qint32> QProtobufMessage::unknownFieldNumbers() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QProtobufMessage.unknownFieldNumbers' has no cute function yet. "
        "Qt's 'QList<qint32> QProtobufMessage::unknownFieldNumbers() "
        "const': gives a type Python has no way to take yet.")

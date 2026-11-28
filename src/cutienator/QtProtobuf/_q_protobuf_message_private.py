"""
QProtobufMessagePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/6.12.0/QtProtobuf/private/qprotobufmessage_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QProtobufMessagePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData
from . import QtProtobufPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArrayView, QMetaObject
  from . import QProtobufMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QMetaObject = WAIT['QMetaObject']
  QProtobufMessage = WAIT['QProtobufMessage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProtobufMessagePrivate(QSharedData):
  """
  The cute side of Qt's QProtobufMessagePrivate: a plain Python object
  standing in front of one C++ QProtobufMessagePrivate.

  It is built on the cute 'QSharedData', as Qt's QProtobufMessagePrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QProtobufMessagePrivate around as a copy, so every C++
  QProtobufMessagePrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QProtobufMessagePrivate that has a ritual and that
  Python can call so far, 3 names in all: 'propertyIndex',
  'storeUnknownEntry', 'get'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QProtobufMessagePrivate::~QProtobufMessagePrivate()': the
    destructor: Python removes its C++ QProtobufMessagePrivate by it, and has
    no other use for it.
  - Qt's 'std::optional<QMetaProperty>
    QProtobufMessagePrivate::metaProperty(QAnyStringView name) const': gives
    a type Python has no way to take yet.
  - Qt's 'std::optional<QMetaProperty>
    QProtobufMessagePrivate::metaProperty(QtProtobufPrivate::
    QProtobufFieldInfo ord) const': gives a type Python has no way to take
    yet.
  - Qt's 'const QProtobufMessagePrivate *QProtobufMessagePrivate::get(const
    QProtobufMessage *message)': takes in Python what
    'QProtobufMessagePrivate *QProtobufMessagePrivate::get(QProtobufMessage
    *message)' takes.

  What has no ritual
  ------------------

  3 of the 13 functions Qt declares: 3 forbidden.

  What to expect
  --------------

  - The C++ QProtobufMessagePrivate is created at the first use, not by
    'QProtobufMessagePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QProtobufMessagePrivate back gives a copy the ritual
    made for Python, in a new cute QProtobufMessagePrivate.
  - Each name of Qt's QProtobufMessagePrivate that has no cute function yet,
    'metaProperty', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QProtobufMessage, QByteArrayView, int)
  @overload(NoneType, QByteArrayView, int)
  def storeUnknownEntry(
      message: Optional[QProtobufMessage],
      entry: QByteArrayView,
      fieldNumber: int,
  ) -> None:
    """
    Calls Qt's 'void
    QProtobufMessagePrivate::storeUnknownEntry(QProtobufMessage *message,
    QByteArrayView entry, int fieldNumber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufmessageprivate.html#storeUnknownEntry

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    entry : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.

    fieldNumber : int
      Passed on as it is.
    """
    #  void QProtobufMessagePrivate::storeUnknownEntry(QProtobufMessage
    #      *message, QByteArrayView entry, int fieldNumber)
    Rituals.call(
        'ritual_ZN23QProtobufMessagePrivate17storeUnknownEntryEP16QProtobuf'
        'Message14QByteArrayViewi',
        CuteMixin._addressOf(message), CuteMixin._valueOf(entry),
        fieldNumber,
    )

  @staticmethod
  @overload(QProtobufMessage)
  @overload(NoneType)
  def get(
      message: Optional[QProtobufMessage],
  ) -> Optional[QProtobufMessagePrivate]:
    """
    Calls Qt's 'QProtobufMessagePrivate
    *QProtobufMessagePrivate::get(QProtobufMessage *message)'.

    Qt's own words: https://doc.qt.io/qt-6/qprotobufmessageprivate.html#get

    Parameters
    ----------

    message : Optional[QProtobufMessage]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QProtobufMessagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QProtobufMessagePrivate *QProtobufMessagePrivate::get(QProtobufMessage
    #      *message)
    address = Rituals.call(
        'ritual_ZN23QProtobufMessagePrivate3getEP16QProtobufMessage',
        CuteMixin._addressOf(message),
    )
    return QProtobufMessagePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProtobufMessagePrivate'

  #  Qt's '~QProtobufMessagePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QProtobufMessagePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QProtobufMessagePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def propertyIndex(self, propertyName: str) -> int:
    """
    Calls Qt's 'int QProtobufMessagePrivate::propertyIndex(QAnyStringView
    propertyName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufmessageprivate.html#propertyIndex

    Parameters
    ----------

    propertyName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int QProtobufMessagePrivate::propertyIndex(QAnyStringView
    #      propertyName) const
    return self.uglySide.call(
        'ritual_ZNK23QProtobufMessagePrivate13propertyIndexE14QAnyStringVie'
        'w',
        propertyName,
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
    'QProtobufMessagePrivate::QProtobufMessagePrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufmessageprivate.html
    """
    #  QProtobufMessagePrivate::QProtobufMessagePrivate()
    self._noteCreation(QProtobufMessagePrivate, lambda: Rituals.call(
        'ritual_ZN23QProtobufMessagePrivateC1Ev',
    ))

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
    Notes what was given, for Qt's
    'QProtobufMessagePrivate::QProtobufMessagePrivate(const QMetaObject
    *metaObject, const QtProtobufPrivate::QProtobufPropertyOrdering
    *ordering)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufmessageprivate.html

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ordering : Optional[QtProtobufPrivate.QProtobufPropertyOrdering]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QProtobufMessagePrivate::QProtobufMessagePrivate(const QMetaObject
    #      *metaObject, const QtProtobufPrivate::QProtobufPropertyOrdering
    #      *ordering)
    self._noteCreation(QProtobufMessagePrivate, lambda: Rituals.call(
        'ritual_ZN23QProtobufMessagePrivateC1EPK11QMetaObjectPKN17QtProtobu'
        'fPrivate25QProtobufPropertyOrderingE',
        self._addressOf(metaObject, 'QMetaObject'),
        self._addressOf(ordering),
    ))

  @overload(THIS)
  def __init__(self, other: QProtobufMessagePrivate) -> None:
    """
    Notes what was given, for Qt's
    'QProtobufMessagePrivate::QProtobufMessagePrivate(const
    QProtobufMessagePrivate &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprotobufmessageprivate.html

    Parameters
    ----------

    other : QProtobufMessagePrivate
      Passed on as a value: Qt reads the C++ QProtobufMessagePrivate, which
      stays Python's own.
    """
    #  QProtobufMessagePrivate::QProtobufMessagePrivate(const
    #      QProtobufMessagePrivate &other)
    self._noteCreation(QProtobufMessagePrivate, lambda: Rituals.call(
        'ritual_ZN23QProtobufMessagePrivateC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def metaProperty(*__, **_) -> Never:
    """
    - Qt's 'std::optional<QMetaProperty>
      QProtobufMessagePrivate::metaProperty(QAnyStringView name) const':
      gives a type Python has no way to take yet.
    - Qt's 'std::optional<QMetaProperty>
      QProtobufMessagePrivate::metaProperty(QtProtobufPrivate::
      QProtobufFieldInfo ord) const': gives a type Python has no way to take
      yet.
    """
    raise NotImplementedError(
        "'QProtobufMessagePrivate.metaProperty' has no cute function yet. "
        "Qt's 'std::optional<QMetaProperty> "
        "QProtobufMessagePrivate::metaProperty(QAnyStringView name) const': "
        "gives a type Python has no way to take yet. Qt's "
        "'std::optional<QMetaProperty> "
        "QProtobufMessagePrivate::metaProperty(QtProtobufPrivate::QProtobufF"
        "ieldInfo ord) const': gives a type Python has no way to take yet.")

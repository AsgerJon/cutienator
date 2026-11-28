"""
QQmlOpenMetaObjectType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlopenmetaobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlOpenMetaObjectType to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMetaObject = WAIT['QMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlOpenMetaObjectType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlOpenMetaObjectType: a plain Python object
  standing in front of one C++ QQmlOpenMetaObjectType.

  What exists
  -----------

  Every function of Qt's QQmlOpenMetaObjectType that has a ritual and that
  Python can call so far, 6 names in all: 'createProperties',
  'createProperty', 'propertyOffset', 'signalOffset', 'propertyCount',
  'propertyName'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlOpenMetaObjectType::~QQmlOpenMetaObjectType()': the destructor:
    Python never removes a C++ QQmlOpenMetaObjectType.
  - Qt's 'QQmlPropertyCache::Ptr QQmlOpenMetaObjectType::cache() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QQmlOpenMetaObjectType::propertyCreated(int a0,
    QMetaPropertyBuilder &a1)': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ QQmlOpenMetaObjectType is created at the first use, not by
    'QQmlOpenMetaObjectType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlOpenMetaObjectType.
  - Each name of Qt's QQmlOpenMetaObjectType that has no cute function yet,
    'cache', 'propertyCreated', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlOpenMetaObjectType'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def propertyOffset(self) -> int:
    """
    Calls Qt's 'int QQmlOpenMetaObjectType::propertyOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobjecttype.html#propertyOffset
    """
    #  int QQmlOpenMetaObjectType::propertyOffset() const
    return self.uglySide.call(
        'ritual_ZNK22QQmlOpenMetaObjectType14propertyOffsetEv',
    )

  def signalOffset(self) -> int:
    """
    Calls Qt's 'int QQmlOpenMetaObjectType::signalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobjecttype.html#signalOffset
    """
    #  int QQmlOpenMetaObjectType::signalOffset() const
    return self.uglySide.call(
        'ritual_ZNK22QQmlOpenMetaObjectType12signalOffsetEv',
    )

  def propertyCount(self) -> int:
    """
    Calls Qt's 'int QQmlOpenMetaObjectType::propertyCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobjecttype.html#propertyCount
    """
    #  int QQmlOpenMetaObjectType::propertyCount() const
    return self.uglySide.call(
        'ritual_ZNK22QQmlOpenMetaObjectType13propertyCountEv',
    )

  @overload(int)
  def propertyName(self, a0: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQmlOpenMetaObjectType::propertyName(int a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobjecttype.html#propertyName

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQmlOpenMetaObjectType::propertyName(int a0) const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlOpenMetaObjectType12propertyNameEi', a0,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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

  @overload(QMetaObject)
  @overload(NoneType)
  def __init__(self, base: Optional[QMetaObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlOpenMetaObjectType::QQmlOpenMetaObjectType(const QMetaObject
    *base)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobjecttype.html#QQmlOpenMetaObjectType

    Parameters
    ----------

    base : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlOpenMetaObjectType::QQmlOpenMetaObjectType(const QMetaObject
    #      *base)
    self._noteCreation(QQmlOpenMetaObjectType, lambda: Rituals.call(
        'ritual_ZN22QQmlOpenMetaObjectTypeC1EPK11QMetaObject',
        self._addressOf(base, 'QMetaObject'),
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

  @overload(QList[QByteArray])
  def createProperties(self, names: QList[QByteArray]) -> None:
    """
    Calls Qt's 'void QQmlOpenMetaObjectType::createProperties(const
    QList<QByteArray> &names)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobjecttype.html#createProperties

    Parameters
    ----------

    names : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlOpenMetaObjectType::createProperties(const QList<QByteArray>
    #      &names)
    self.uglySide.call(
        'ritual_ZN22QQmlOpenMetaObjectType16createPropertiesERK5QListI10QBy'
        'teArrayE',
        self._valueOf(names),
    )

  @overload(QByteArray)
  def createProperty(self, name: QByteArray) -> int:
    """
    Calls Qt's 'int QQmlOpenMetaObjectType::createProperty(const QByteArray
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlopenmetaobjecttype.html#createProperty

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QQmlOpenMetaObjectType::createProperty(const QByteArray &name)
    return self.uglySide.call(
        'ritual_ZN22QQmlOpenMetaObjectType14createPropertyERK10QByteArray',
        self._valueOf(name),
    )

  @staticmethod
  def cache(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyCache::Ptr QQmlOpenMetaObjectType::cache() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlOpenMetaObjectType.cache' has no cute function yet. Qt's "
        "'QQmlPropertyCache::Ptr QQmlOpenMetaObjectType::cache() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def propertyCreated(*__, **_) -> Never:
    """
    Qt's 'void QQmlOpenMetaObjectType::propertyCreated(int a0,
    QMetaPropertyBuilder &a1)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQmlOpenMetaObjectType.propertyCreated' has no cute function yet. "
        "Qt's 'void QQmlOpenMetaObjectType::propertyCreated(int a0, "
        "QMetaPropertyBuilder &a1)': takes a type Python has no way to hand "
        "over yet.")

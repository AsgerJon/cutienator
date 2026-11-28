"""
QQmlProxyMetaObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlproxymetaobject_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlProxyMetaObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QDynamicMetaObjectData, QMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlProxyMetaObject(QDynamicMetaObjectData):
  """
  The cute side of Qt's QQmlProxyMetaObject: a plain Python object standing
  in front of one C++ QQmlProxyMetaObject.

  It is built on the cute 'QDynamicMetaObjectData', as Qt's
  QQmlProxyMetaObject is built on Qt's QDynamicMetaObjectData, and has
  everything that class has.

  C++ hands a QQmlProxyMetaObject around as a copy, so every C++
  QQmlProxyMetaObject behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlProxyMetaObject that has a ritual and that
  Python can call so far, 4 names in all: 'extensionObjectId',
  'toDynamicMetaObject', 'objectDestroyed', 'getProxy'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlProxyMetaObject::QQmlProxyMetaObject(QObject *a0, const
    QList<ProxyData> *a1)': names 'QList<QQmlProxyMetaObject::ProxyData>',
    which has no cute class yet.
  - Qt's 'QQmlProxyMetaObject::~QQmlProxyMetaObject()': the destructor:
    Python removes its C++ QQmlProxyMetaObject by it, and has no other use
    for it.
  - Qt's 'int QQmlProxyMetaObject::metaCall(QObject *o, QMetaObject::Call _c,
    int _id, void **_a)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlProxyMetaObject is created at the first use, not by
    'QQmlProxyMetaObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlProxyMetaObject back gives a copy the ritual made
    for Python, in a new cute QQmlProxyMetaObject.
  - Each name of Qt's QQmlProxyMetaObject that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QQmlProxyMetaObject, each a class in here
  #  as in C++.

  class ProxyData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlProxyMetaObject::ProxyData: a plain Python
    object standing in front of one C++ QQmlProxyMetaObject::ProxyData.

    C++ hands a QQmlProxyMetaObject::ProxyData around as a copy, so every C++
    QQmlProxyMetaObject::ProxyData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlProxyMetaObject::ProxyData yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlProxyMetaObject::ProxyData::~ProxyData()': the destructor:
      Python removes its C++ QQmlProxyMetaObject::ProxyData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQmlProxyMetaObject::ProxyData is created at the first use, not
      by 'QQmlProxyMetaObject::ProxyData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlProxyMetaObject::ProxyData back gives a copy
      the ritual made for Python, in a new cute
      QQmlProxyMetaObject::ProxyData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlProxyMetaObject::ProxyData'

    #  Qt's '~QQmlProxyMetaObject::ProxyData()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlProxyMetaObject::ProxyData behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QQmlProxyMetaObject9ProxyDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def extensionObjectId(id: int) -> int:
    """
    Calls Qt's 'int QQmlProxyMetaObject::extensionObjectId(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlproxymetaobject.html#extensionObjectId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  int QQmlProxyMetaObject::extensionObjectId(int id)
    return Rituals.call(
        'ritual_ZN19QQmlProxyMetaObject17extensionObjectIdEi', id,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlProxyMetaObject'

  #  A C++ QQmlProxyMetaObject Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlProxyMetaObject'

  #  Qt's '~QQmlProxyMetaObject()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlProxyMetaObject behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQmlProxyMetaObjectD1Ev'

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
    Qt's 'QQmlProxyMetaObject::QQmlProxyMetaObject(QObject *a0, const
    QList<ProxyData> *a1)': names 'QList<QQmlProxyMetaObject::ProxyData>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlProxyMetaObject.__init__' has no cute function yet. Qt's "
        "'QQmlProxyMetaObject::QQmlProxyMetaObject(QObject *a0, const "
        "QList<ProxyData> *a1)': names "
        "'QList<QQmlProxyMetaObject::ProxyData>', which has no cute class "
        "yet.")

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

  @overload(QObject)
  @overload(NoneType)
  def toDynamicMetaObject(
      self,
      a0: Optional[QObject],
  ) -> Optional[QMetaObject]:
    """
    Calls Qt's 'QMetaObject *QQmlProxyMetaObject::toDynamicMetaObject(QObject
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlproxymetaobject.html#toDynamicMetaObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMetaObject *QQmlProxyMetaObject::toDynamicMetaObject(QObject *a0)
    ritual = 'ritual_ZN19QQmlProxyMetaObject19toDynamicMetaObjectEP7QObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlProxyMetaObject19toDynamicMetaObjectEP7QObjec'
          't')
    address = self.uglySide.call(ritual, self._addressOf(a0, 'QObject'))
    return QMetaObject._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def objectDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlProxyMetaObject::objectDestroyed(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlproxymetaobject.html#objectDestroyed

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlProxyMetaObject::objectDestroyed(QObject *object)
    ritual = 'ritual_ZN19QQmlProxyMetaObject15objectDestroyedEP7QObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQmlProxyMetaObject15objectDestroyedEP7QObject')
    self.uglySide.call(ritual, self._addressOf(object, 'QObject'))

  @overload(int)
  def getProxy(self, index: int) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlProxyMetaObject::getProxy(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlproxymetaobject.html#getProxy

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlProxyMetaObject::getProxy(int index)
    address = self.uglySide.call(
        'ritual_ZN19QQmlProxyMetaObject8getProxyEi', index,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

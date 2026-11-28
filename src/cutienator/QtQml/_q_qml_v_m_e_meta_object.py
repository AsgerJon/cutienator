"""
QQmlVMEMetaObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvmemetaobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlVMEMetaObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMetaObject
from . import QQmlInterceptorMetaObject, QQmlPropertyCache, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDate, QDateTime, QObject, QPointF, QRectF
  from ..QtCore import QRegularExpression, QSizeF, QTime, QUrl, QVariant
  from . import QQmlVMEVariantQObjectPtr
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlVMEMetaObject(QQmlInterceptorMetaObject):
  """
  The cute side of Qt's QQmlVMEMetaObject: a plain Python object standing in
  front of one C++ QQmlVMEMetaObject.

  It is built on the cute 'QQmlInterceptorMetaObject', as Qt's
  QQmlVMEMetaObject is built on Qt's QQmlInterceptorMetaObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlVMEMetaObject that has a ritual and that Python
  can call so far, 47 names in all: 'vmeMethod', 'setVmeMethod',
  'vmeProperty', 'setVMEProperty', 'connectAliasSignal', 'get',
  'getForProperty', 'getForMethod', 'getForSignal', 'propOffset',
  'propCount', 'aliasOffset', 'aliasCount', 'signalOffset', 'signalCount',
  'methodOffset', 'methodCount', 'propertyAndMethodStorageAsMemberData',
  'readPropertyAsInt', 'readPropertyAsBool', 'readPropertyAsDouble',
  'readPropertyAsString', 'readPropertyAsSizeF', 'readPropertyAsPointF',
  'readPropertyAsUrl', 'readPropertyAsDate', 'readPropertyAsTime',
  'readPropertyAsDateTime', 'readPropertyAsRegularExpression',
  'readPropertyAsRectF', 'readPropertyAsQObject', 'initPropertyAsList',
  'writeProperty', 'ensureQObjectWrapper', 'mark', 'connectAlias', 'method',
  'readVarProperty', 'writeVarProperty', 'readPropertyAsVariant',
  'parentVMEMetaObject', 'setParentVMEMetaObject',
  'getQObjectGuardForProperty', 'engine', 'qmlObjectId',
  'findCompiledObject', 'writeKnownVarProperty'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlVMEMetaObject::QQmlVMEMetaObject(QV4::ExecutionEngine *engine,
    QObject *obj, const QQmlPropertyCache::ConstPtr &cache, const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &qmlCompilationUnit, int
    qmlObjectId)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlVMEMetaObject::~QQmlVMEMetaObject()': the destructor: Python
    never removes a C++ QQmlVMEMetaObject.
  - Qt's 'bool QQmlVMEMetaObject::aliasTarget(int index, QObject **target,
    int *coreIndex, int *valueTypeIndex) const': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QQmlVMEMetaObject::list_append(QQmlListProperty<QObject>
    *prop, QObject *o)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void QQmlVMEMetaObject::list_clear(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'void
    QQmlVMEMetaObject::list_append_nosignal(QQmlListProperty<QObject> *prop,
    QObject *o)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
  - Qt's 'void
    QQmlVMEMetaObject::list_clear_nosignal(QQmlListProperty<QObject> *prop)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'void QQmlVMEMetaObject::activate(QObject *a0, int a1, void **a2)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlRefPointer<QQmlContextData> QQmlVMEMetaObject::contextData()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlRefPointer<QV4::ExecutableCompilationUnit>
    QQmlVMEMetaObject::compilationUnit() const': gives a type Python has no
    way to take yet.
  - Qt's 'void QQmlVMEMetaObject::setCompilationUnit(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit)': takes
    a type Python has no way to hand over yet.
  - Qt's 'int QQmlVMEMetaObject::metaCall(QObject *o, QMetaObject::Call _c,
    int _id, void **_a)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlVMEMetaObject::getListProperty(int id,
    QQmlListProperty<QObject> *target)': names 'QQmlListProperty<QObject>',
    which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 65 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QQmlVMEMetaObject is created at the first use, not by
    'QQmlVMEMetaObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlVMEMetaObject.
  - Each name of Qt's QQmlVMEMetaObject that has no cute function yet,
    '__init__', 'activate', 'aliasTarget', 'compilationUnit', 'contextData',
    'getListProperty', 'list_append', 'list_append_nosignal', 'list_clear',
    'list_clear_nosignal', 'setCompilationUnit', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def get(o: Optional[QObject]) -> Optional[QQmlVMEMetaObject]:
    """
    Calls Qt's 'QQmlVMEMetaObject *QQmlVMEMetaObject::get(QObject *o)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmemetaobject.html#get

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlVMEMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlVMEMetaObject *QQmlVMEMetaObject::get(QObject *o)
    address = Rituals.call(
        'ritual_ZN17QQmlVMEMetaObject3getEP7QObject',
        CuteMixin._addressOf(o, 'QObject'),
    )
    return QQmlVMEMetaObject._cuteAt(address)

  @staticmethod
  @overload(QObject, int)
  @overload(NoneType, int)
  def getForProperty(
      o: Optional[QObject],
      coreIndex: int,
  ) -> Optional[QQmlVMEMetaObject]:
    """
    Calls Qt's 'QQmlVMEMetaObject *QQmlVMEMetaObject::getForProperty(QObject
    *o, int coreIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#getForProperty

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coreIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlVMEMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlVMEMetaObject *QQmlVMEMetaObject::getForProperty(QObject *o, int
    #      coreIndex)
    address = Rituals.call(
        'ritual_ZN17QQmlVMEMetaObject14getForPropertyEP7QObjecti',
        CuteMixin._addressOf(o, 'QObject'), coreIndex,
    )
    return QQmlVMEMetaObject._cuteAt(address)

  @staticmethod
  @overload(QObject, int)
  @overload(NoneType, int)
  def getForMethod(
      o: Optional[QObject],
      coreIndex: int,
  ) -> Optional[QQmlVMEMetaObject]:
    """
    Calls Qt's 'QQmlVMEMetaObject *QQmlVMEMetaObject::getForMethod(QObject
    *o, int coreIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#getForMethod

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coreIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlVMEMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlVMEMetaObject *QQmlVMEMetaObject::getForMethod(QObject *o, int
    #      coreIndex)
    address = Rituals.call(
        'ritual_ZN17QQmlVMEMetaObject12getForMethodEP7QObjecti',
        CuteMixin._addressOf(o, 'QObject'), coreIndex,
    )
    return QQmlVMEMetaObject._cuteAt(address)

  @staticmethod
  @overload(QObject, int)
  @overload(NoneType, int)
  def getForSignal(
      o: Optional[QObject],
      coreIndex: int,
  ) -> Optional[QQmlVMEMetaObject]:
    """
    Calls Qt's 'QQmlVMEMetaObject *QQmlVMEMetaObject::getForSignal(QObject
    *o, int coreIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#getForSignal

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    coreIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlVMEMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlVMEMetaObject *QQmlVMEMetaObject::getForSignal(QObject *o, int
    #      coreIndex)
    address = Rituals.call(
        'ritual_ZN17QQmlVMEMetaObject12getForSignalEP7QObjecti',
        CuteMixin._addressOf(o, 'QObject'), coreIndex,
    )
    return QQmlVMEMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlVMEMetaObject'

  #  A C++ QQmlVMEMetaObject Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlVMEMetaObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def vmeMethod(self, index: int) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQmlVMEMetaObject::vmeMethod(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmemetaobject.html#vmeMethod

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  QV4::ReturnedValue QQmlVMEMetaObject::vmeMethod(int index) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject9vmeMethodEi', index,
    )

  @overload(int)
  def vmeProperty(self, index: int) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQmlVMEMetaObject::vmeProperty(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmemetaobject.html#vmeProperty

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  QV4::ReturnedValue QQmlVMEMetaObject::vmeProperty(int index) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject11vmePropertyEi', index,
    )

  def propOffset(self) -> int:
    """
    Calls Qt's 'int QQmlVMEMetaObject::propOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmemetaobject.html#propOffset
    """
    #  int QQmlVMEMetaObject::propOffset() const
    return self.uglySide.call('ritual_ZNK17QQmlVMEMetaObject10propOffsetEv')

  def propCount(self) -> int:
    """
    Calls Qt's 'int QQmlVMEMetaObject::propCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmemetaobject.html#propCount
    """
    #  int QQmlVMEMetaObject::propCount() const
    return self.uglySide.call('ritual_ZNK17QQmlVMEMetaObject9propCountEv')

  def aliasOffset(self) -> int:
    """
    Calls Qt's 'int QQmlVMEMetaObject::aliasOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmemetaobject.html#aliasOffset
    """
    #  int QQmlVMEMetaObject::aliasOffset() const
    return self.uglySide.call('ritual_ZNK17QQmlVMEMetaObject11aliasOffsetEv')

  def aliasCount(self) -> int:
    """
    Calls Qt's 'int QQmlVMEMetaObject::aliasCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmemetaobject.html#aliasCount
    """
    #  int QQmlVMEMetaObject::aliasCount() const
    return self.uglySide.call('ritual_ZNK17QQmlVMEMetaObject10aliasCountEv')

  def signalOffset(self) -> int:
    """
    Calls Qt's 'int QQmlVMEMetaObject::signalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#signalOffset
    """
    #  int QQmlVMEMetaObject::signalOffset() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject12signalOffsetEv',
    )

  def signalCount(self) -> int:
    """
    Calls Qt's 'int QQmlVMEMetaObject::signalCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmemetaobject.html#signalCount
    """
    #  int QQmlVMEMetaObject::signalCount() const
    return self.uglySide.call('ritual_ZNK17QQmlVMEMetaObject11signalCountEv')

  def methodOffset(self) -> int:
    """
    Calls Qt's 'int QQmlVMEMetaObject::methodOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#methodOffset
    """
    #  int QQmlVMEMetaObject::methodOffset() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject12methodOffsetEv',
    )

  def methodCount(self) -> int:
    """
    Calls Qt's 'int QQmlVMEMetaObject::methodCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmemetaobject.html#methodCount
    """
    #  int QQmlVMEMetaObject::methodCount() const
    return self.uglySide.call('ritual_ZNK17QQmlVMEMetaObject11methodCountEv')

  def propertyAndMethodStorageAsMemberData(self) -> Optional[QV4.MemberData]:
    """
    Calls Qt's 'QV4::MemberData
    *QQmlVMEMetaObject::propertyAndMethodStorageAsMemberData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html

    Returns
    -------

    Optional[QV4.MemberData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::MemberData
    #      *QQmlVMEMetaObject::propertyAndMethodStorageAsMemberData() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject36propertyAndMethodStorageAsMemberDat'
        'aEv',
    )
    return QV4.MemberData._cuteAt(address)

  @overload(int)
  def readPropertyAsInt(self, id: int) -> int:
    """
    Calls Qt's 'int QQmlVMEMetaObject::readPropertyAsInt(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readPropertyAsInt

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  int QQmlVMEMetaObject::readPropertyAsInt(int id) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject17readPropertyAsIntEi', id,
    )

  @overload(int)
  def readPropertyAsBool(self, id: int) -> bool:
    """
    Calls Qt's 'bool QQmlVMEMetaObject::readPropertyAsBool(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readPropertyAsBool

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  bool QQmlVMEMetaObject::readPropertyAsBool(int id) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject18readPropertyAsBoolEi', id,
    )

  @overload(int)
  def readPropertyAsDouble(self, id: int) -> float:
    """
    Calls Qt's 'double QQmlVMEMetaObject::readPropertyAsDouble(int id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readPropertyAsDouble

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  double QQmlVMEMetaObject::readPropertyAsDouble(int id) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject20readPropertyAsDoubleEi', id,
    )

  @overload(int)
  def readPropertyAsString(self, id: int) -> str:
    """
    Calls Qt's 'QString QQmlVMEMetaObject::readPropertyAsString(int id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readPropertyAsString

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlVMEMetaObject::readPropertyAsString(int id) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject20readPropertyAsStringEi', id,
    )

  @overload(int)
  def readPropertyAsSizeF(self, id: int) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQmlVMEMetaObject::readPropertyAsSizeF(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readPropertyAsSizeF

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQmlVMEMetaObject::readPropertyAsSizeF(int id) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject19readPropertyAsSizeFEi', id,
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @overload(int)
  def readPropertyAsPointF(self, id: int) -> QPointF:
    """
    Calls Qt's 'QPointF QQmlVMEMetaObject::readPropertyAsPointF(int id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readPropertyAsPointF

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQmlVMEMetaObject::readPropertyAsPointF(int id) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject20readPropertyAsPointFEi', id,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(int)
  def readPropertyAsUrl(self, id: int) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlVMEMetaObject::readPropertyAsUrl(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readPropertyAsUrl

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlVMEMetaObject::readPropertyAsUrl(int id) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject17readPropertyAsUrlEi', id,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @overload(int)
  def readPropertyAsDate(self, id: int) -> QDate:
    """
    Calls Qt's 'QDate QQmlVMEMetaObject::readPropertyAsDate(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readPropertyAsDate

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QQmlVMEMetaObject::readPropertyAsDate(int id) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject18readPropertyAsDateEi', id,
    )
    from ..QtCore import QDate
    return QDate._cuteOwning(address)

  @overload(int)
  def readPropertyAsTime(self, id: int) -> QTime:
    """
    Calls Qt's 'QTime QQmlVMEMetaObject::readPropertyAsTime(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readPropertyAsTime

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QQmlVMEMetaObject::readPropertyAsTime(int id) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject18readPropertyAsTimeEi', id,
    )
    from ..QtCore import QTime
    return QTime._cuteOwning(address)

  @overload(int)
  def readPropertyAsDateTime(self, id: int) -> QDateTime:
    """
    Calls Qt's 'QDateTime QQmlVMEMetaObject::readPropertyAsDateTime(int id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readPropertyAsDateTime

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QQmlVMEMetaObject::readPropertyAsDateTime(int id) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject22readPropertyAsDateTimeEi', id,
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(int)
  def readPropertyAsRegularExpression(self, id: int) -> QRegularExpression:
    """
    Calls Qt's 'QRegularExpression
    QQmlVMEMetaObject::readPropertyAsRegularExpression(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    QRegularExpression
      A new cute QRegularExpression around the copy Qt gave back. Python owns
      it.
    """
    #  QRegularExpression
    #      QQmlVMEMetaObject::readPropertyAsRegularExpression(int id) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject31readPropertyAsRegularExpressionEi',
        id,
    )
    from ..QtCore import QRegularExpression
    return QRegularExpression._cuteOwning(address)

  @overload(int)
  def readPropertyAsRectF(self, id: int) -> QRectF:
    """
    Calls Qt's 'QRectF QQmlVMEMetaObject::readPropertyAsRectF(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readPropertyAsRectF

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQmlVMEMetaObject::readPropertyAsRectF(int id) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject19readPropertyAsRectFEi', id,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(int)
  def readPropertyAsQObject(self, id: int) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlVMEMetaObject::readPropertyAsQObject(int id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readPropertyAsQObject

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlVMEMetaObject::readPropertyAsQObject(int id) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject21readPropertyAsQObjectEi', id,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(int)
  def method(self, a0: int) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQmlVMEMetaObject::method(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmemetaobject.html#method

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  QV4::ReturnedValue QQmlVMEMetaObject::method(int a0) const
    return self.uglySide.call('ritual_ZNK17QQmlVMEMetaObject6methodEi', a0)

  @overload(int)
  def readVarProperty(self, a0: int) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQmlVMEMetaObject::readVarProperty(int a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readVarProperty

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  QV4::ReturnedValue QQmlVMEMetaObject::readVarProperty(int a0) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject15readVarPropertyEi', a0,
    )

  @overload(int)
  def readPropertyAsVariant(self, a0: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlVMEMetaObject::readPropertyAsVariant(int a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#readPropertyAsVariant

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlVMEMetaObject::readPropertyAsVariant(int a0) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject21readPropertyAsVariantEi', a0,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def parentVMEMetaObject(self) -> Optional[QQmlVMEMetaObject]:
    """
    Calls Qt's 'QQmlVMEMetaObject *QQmlVMEMetaObject::parentVMEMetaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#parentVMEMetaObject

    Returns
    -------

    Optional[QQmlVMEMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlVMEMetaObject *QQmlVMEMetaObject::parentVMEMetaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject19parentVMEMetaObjectEv',
    )
    return QQmlVMEMetaObject._cuteAt(address)

  @overload(int)
  def getQObjectGuardForProperty(
      self,
      a0: int,
  ) -> Optional[QQmlVMEVariantQObjectPtr]:
    """
    Calls Qt's 'QQmlVMEVariantQObjectPtr
    *QQmlVMEMetaObject::getQObjectGuardForProperty(int a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#getQObjectGuardForProperty

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlVMEVariantQObjectPtr]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlVMEVariantQObjectPtr
    #      *QQmlVMEMetaObject::getQObjectGuardForProperty(int a0) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject26getQObjectGuardForPropertyEi', a0,
    )
    from . import QQmlVMEVariantQObjectPtr
    return QQmlVMEVariantQObjectPtr._cuteAt(address)

  def engine(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'QV4::ExecutionEngine *QQmlVMEMetaObject::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmemetaobject.html#engine

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutionEngine *QQmlVMEMetaObject::engine() const
    address = self.uglySide.call('ritual_ZNK17QQmlVMEMetaObject6engineEv')
    return QV4.ExecutionEngine._cuteAt(address)

  def qmlObjectId(self) -> int:
    """
    Calls Qt's 'int QQmlVMEMetaObject::qmlObjectId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmemetaobject.html#qmlObjectId
    """
    #  int QQmlVMEMetaObject::qmlObjectId() const
    return self.uglySide.call('ritual_ZNK17QQmlVMEMetaObject11qmlObjectIdEv')

  def findCompiledObject(self) -> Optional[QV4.CompiledData.Object]:
    """
    Calls Qt's 'const QV4::CompiledData::Object
    *QQmlVMEMetaObject::findCompiledObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#findCompiledObject

    Returns
    -------

    Optional[QV4.CompiledData.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QV4::CompiledData::Object
    #      *QQmlVMEMetaObject::findCompiledObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject18findCompiledObjectEv',
    )
    return QV4.CompiledData.Object._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, WAIT['QV4.Value'])
  def setVmeMethod(self, index: int, function: QV4.Value) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::setVmeMethod(int index, const
    QV4::Value &function)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#setVmeMethod

    Parameters
    ----------

    index : int
      Passed on as it is.

    function : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QQmlVMEMetaObject::setVmeMethod(int index, const QV4::Value
    #      &function)
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject12setVmeMethodEiRKN3QV45ValueE',
        index, self._valueOf(function),
    )

  @overload(int, WAIT['QV4.Value'])
  def setVMEProperty(self, index: int, v: QV4.Value) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::setVMEProperty(int index, const
    QV4::Value &v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#setVMEProperty

    Parameters
    ----------

    index : int
      Passed on as it is.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QQmlVMEMetaObject::setVMEProperty(int index, const QV4::Value &v)
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject14setVMEPropertyEiRKN3QV45ValueE',
        index, self._valueOf(v),
    )

  @overload(THIS)
  @overload(NoneType)
  def setParentVMEMetaObject(
      self,
      newParent: Optional[QQmlVMEMetaObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlVMEMetaObject::setParentVMEMetaObject(QQmlVMEMetaObject *newParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#setParentVMEMetaObject

    Parameters
    ----------

    newParent : Optional[QQmlVMEMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlVMEMetaObject::setParentVMEMetaObject(QQmlVMEMetaObject
    #      *newParent)
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject22setParentVMEMetaObjectEPS_',
        self._addressOf(newParent),
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
    Qt's 'QQmlVMEMetaObject::QQmlVMEMetaObject(QV4::ExecutionEngine *engine,
    QObject *obj, const QQmlPropertyCache::ConstPtr &cache, const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &qmlCompilationUnit, int
    qmlObjectId)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlVMEMetaObject.__init__' has no cute function yet. Qt's "
        "'QQmlVMEMetaObject::QQmlVMEMetaObject(QV4::ExecutionEngine "
        "*engine, QObject *obj, const QQmlPropertyCache::ConstPtr &cache, "
        "const QQmlRefPointer<QV4::ExecutableCompilationUnit> "
        "&qmlCompilationUnit, int qmlObjectId)': takes a type Python has no "
        "way to hand over yet.")

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

  @overload(int, bool)
  def connectAliasSignal(self, index: int, indexInSignalRange: bool) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::connectAliasSignal(int index, bool
    indexInSignalRange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#connectAliasSignal

    Parameters
    ----------

    index : int
      Passed on as it is.

    indexInSignalRange : bool
      Passed on as it is.
    """
    #  void QQmlVMEMetaObject::connectAliasSignal(int index, bool
    #      indexInSignalRange)
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject18connectAliasSignalEib',
        index, indexInSignalRange,
    )

  @overload(int)
  def initPropertyAsList(self, id: int) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::initPropertyAsList(int id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#initPropertyAsList

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QQmlVMEMetaObject::initPropertyAsList(int id) const
    self.uglySide.call(
        'ritual_ZNK17QQmlVMEMetaObject18initPropertyAsListEi', id,
    )

  @overload(int, int)
  def writeProperty(self, id: int, v: int) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::writeProperty(int id, int v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#writeProperty

    Parameters
    ----------

    id : int
      Passed on as it is.

    v : int
      Passed on as it is.
    """
    #  void QQmlVMEMetaObject::writeProperty(int id, int v)
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject13writePropertyEii', id, v,
    )

  @overload(int, bool)
  def writeProperty(self, id: int, v: bool) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::writeProperty(int id, bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#writeProperty

    Parameters
    ----------

    id : int
      Passed on as it is.

    v : bool
      Passed on as it is.
    """
    #  void QQmlVMEMetaObject::writeProperty(int id, bool v)
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject13writePropertyEib', id, v,
    )

  @overload(int, float)
  def writeProperty(self, id: int, v: float) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::writeProperty(int id, double v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#writeProperty

    Parameters
    ----------

    id : int
      Passed on as it is.

    v : float
      Passed on as it is.
    """
    #  void QQmlVMEMetaObject::writeProperty(int id, double v)
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject13writePropertyEid', id, v,
    )

  @overload(int, str)
  def writeProperty(self, id: int, v: str) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::writeProperty(int id, const QString
    &v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#writeProperty

    Parameters
    ----------

    id : int
      Passed on as it is.

    v : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlVMEMetaObject::writeProperty(int id, const QString &v)
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject13writePropertyEiRK7QString', id, v,
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def writeProperty(self, id: int, v: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::writeProperty(int id, QObject *v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#writeProperty

    Parameters
    ----------

    id : int
      Passed on as it is.

    v : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlVMEMetaObject::writeProperty(int id, QObject *v)
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject13writePropertyEiP7QObject',
        id, self._addressOf(v, 'QObject'),
    )

  def ensureQObjectWrapper(self) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::ensureQObjectWrapper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#ensureQObjectWrapper
    """
    #  void QQmlVMEMetaObject::ensureQObjectWrapper()
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject20ensureQObjectWrapperEv',
    )

  @overload(WAIT['QV4.MarkStack'])
  @overload(NoneType)
  def mark(self, markStack: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::mark(QV4::MarkStack *markStack)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvmemetaobject.html#mark

    Parameters
    ----------

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlVMEMetaObject::mark(QV4::MarkStack *markStack)
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject4markEPN3QV49MarkStackE',
        self._addressOf(markStack),
    )

  @overload(WAIT['QV4.CompiledData.Object'], int)
  @overload(NoneType, int)
  def connectAlias(
      self,
      compiledObject: Optional[QV4.CompiledData.Object],
      aliasId: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::connectAlias(const
    QV4::CompiledData::Object *compiledObject, int aliasId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#connectAlias

    Parameters
    ----------

    compiledObject : Optional[QV4.CompiledData.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    aliasId : int
      Passed on as it is.
    """
    #  void QQmlVMEMetaObject::connectAlias(const QV4::CompiledData::Object
    #      *compiledObject, int aliasId)
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject12connectAliasEPKN3QV412CompiledData6O'
        'bjectEi',
        self._addressOf(compiledObject), aliasId,
    )

  @overload(int, WAIT['QV4.Value'])
  def writeVarProperty(self, a0: int, a1: QV4.Value) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::writeVarProperty(int a0, const
    QV4::Value &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#writeVarProperty

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QQmlVMEMetaObject::writeVarProperty(int a0, const QV4::Value &a1)
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject16writeVarPropertyEiRKN3QV45ValueE',
        a0, self._valueOf(a1),
    )

  @overload(int, QVariant)
  def writeKnownVarProperty(self, id: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlVMEMetaObject::writeKnownVarProperty(int id, const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvmemetaobject.html#writeKnownVarProperty

    Parameters
    ----------

    id : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlVMEMetaObject::writeKnownVarProperty(int id, const QVariant
    #      &value)
    self.uglySide.call(
        'ritual_ZN17QQmlVMEMetaObject21writeKnownVarPropertyEiRK8QVariant',
        id, self._valueOf(value),
    )

  @staticmethod
  def activate(*__, **_) -> Never:
    """
    Qt's 'void QQmlVMEMetaObject::activate(QObject *a0, int a1, void **a2)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlVMEMetaObject.activate' has no cute function yet. Qt's 'void "
        "QQmlVMEMetaObject::activate(QObject *a0, int a1, void **a2)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def aliasTarget(*__, **_) -> Never:
    """
    Qt's 'bool QQmlVMEMetaObject::aliasTarget(int index, QObject **target,
    int *coreIndex, int *valueTypeIndex) const': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlVMEMetaObject.aliasTarget' has no cute function yet. Qt's "
        "'bool QQmlVMEMetaObject::aliasTarget(int index, QObject **target, "
        "int *coreIndex, int *valueTypeIndex) const': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def compilationUnit(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QV4::ExecutableCompilationUnit>
    QQmlVMEMetaObject::compilationUnit() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlVMEMetaObject.compilationUnit' has no cute function yet. Qt's "
        "'QQmlRefPointer<QV4::ExecutableCompilationUnit> "
        "QQmlVMEMetaObject::compilationUnit() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def contextData(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData> QQmlVMEMetaObject::contextData()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlVMEMetaObject.contextData' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> QQmlVMEMetaObject::contextData() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def getListProperty(*__, **_) -> Never:
    """
    Qt's 'bool QQmlVMEMetaObject::getListProperty(int id,
    QQmlListProperty<QObject> *target)': names 'QQmlListProperty<QObject>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlVMEMetaObject.getListProperty' has no cute function yet. Qt's "
        "'bool QQmlVMEMetaObject::getListProperty(int id, "
        "QQmlListProperty<QObject> *target)': names "
        "'QQmlListProperty<QObject>', which has no cute class yet.")

  @staticmethod
  def list_append(*__, **_) -> Never:
    """
    Qt's 'void QQmlVMEMetaObject::list_append(QQmlListProperty<QObject>
    *prop, QObject *o)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQmlVMEMetaObject.list_append' has no cute function yet. Qt's "
        "'void QQmlVMEMetaObject::list_append(QQmlListProperty<QObject> "
        "*prop, QObject *o)': names 'QQmlListProperty<QObject>', which has "
        "no cute class yet.")

  @staticmethod
  def list_append_nosignal(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlVMEMetaObject::list_append_nosignal(QQmlListProperty<QObject> *prop,
    QObject *o)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlVMEMetaObject.list_append_nosignal' has no cute function yet. "
        "Qt's 'void "
        "QQmlVMEMetaObject::list_append_nosignal(QQmlListProperty<QObject> "
        "*prop, QObject *o)': names 'QQmlListProperty<QObject>', which has "
        "no cute class yet.")

  @staticmethod
  def list_clear(*__, **_) -> Never:
    """
    Qt's 'void QQmlVMEMetaObject::list_clear(QQmlListProperty<QObject>
    *prop)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlVMEMetaObject.list_clear' has no cute function yet. Qt's "
        "'void QQmlVMEMetaObject::list_clear(QQmlListProperty<QObject> "
        "*prop)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def list_clear_nosignal(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlVMEMetaObject::list_clear_nosignal(QQmlListProperty<QObject> *prop)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlVMEMetaObject.list_clear_nosignal' has no cute function yet. "
        "Qt's 'void "
        "QQmlVMEMetaObject::list_clear_nosignal(QQmlListProperty<QObject> "
        "*prop)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def setCompilationUnit(*__, **_) -> Never:
    """
    Qt's 'void QQmlVMEMetaObject::setCompilationUnit(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlVMEMetaObject.setCompilationUnit' has no cute function yet. "
        "Qt's 'void QQmlVMEMetaObject::setCompilationUnit(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &compilationUnit)': "
        "takes a type Python has no way to hand over yet.")

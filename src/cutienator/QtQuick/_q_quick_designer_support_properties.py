"""
QQuickDesignerSupportProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdesignersupportproperties_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickDesignerSupportProperties to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaProperty, QObject, QVariant
  from ..QtQml import QQmlContext, QQmlEngine, QQmlListReference
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMetaProperty = WAIT['QMetaProperty']
  QObject = WAIT['QObject']
  QQmlContext = WAIT['QQmlContext']
  QQmlEngine = WAIT['QQmlEngine']
  QQmlListReference = WAIT['QQmlListReference']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDesignerSupportProperties(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickDesignerSupportProperties: a plain Python
  object standing in front of one C++ QQuickDesignerSupportProperties.

  C++ hands a QQuickDesignerSupportProperties around as a copy, so every C++
  QQuickDesignerSupportProperties behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQuickDesignerSupportProperties that has a ritual
  and that Python can call so far, 14 names in all:
  'createNewDynamicProperty', 'registerNodeInstanceMetaObject',
  'registerCustomData', 'getResetValue', 'doResetProperty',
  'hasValidResetBinding', 'setPropertyBinding',
  'keepBindingFromGettingDeleted', 'isPropertyQObject',
  'readQObjectProperty', 'getPropertyCache', 'isPropertyBlackListed',
  'propertyNameListForWritableProperties', 'hasFullImplementedListInterface'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QQuickDesignerSupportProperties::hasBindingForProperty(QObject
    *object, QQmlContext *context, const QQuickDesignerSupport::PropertyName
    &propertyName, bool *hasChanged)': takes a number to change where it is.
  - Qt's 'QQuickDesignerSupport::PropertyNameList
    QQuickDesignerSupportProperties::allPropertyNames(QObject *object, const
    QQuickDesignerSupport::PropertyName &baseName, QObjectList
    *inspectedObjects, int depth)': names 'QObjectList', which has no cute
    class yet.
  - Qt's
    'QQuickDesignerSupportProperties::~QQuickDesignerSupportProperties()':
    the destructor: Python removes its C++ QQuickDesignerSupportProperties by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQuickDesignerSupportProperties is created at the first use, not
    by 'QQuickDesignerSupportProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickDesignerSupportProperties back gives a copy the
    ritual made for Python, in a new cute QQuickDesignerSupportProperties.
  - Each name of Qt's QQuickDesignerSupportProperties that has no cute
    function yet, 'allPropertyNames', 'hasBindingForProperty', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QObject, QQmlEngine, str)
  @overload(QObject, NoneType, str)
  @overload(NoneType, QQmlEngine, str)
  @overload(NoneType, NoneType, str)
  def createNewDynamicProperty(
      object: Optional[QObject],
      engine: Optional[QQmlEngine],
      name: str,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupportProperties::createNewDynamicProperty(QObject
    *object, QQmlEngine *engine, const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickDesignerSupportProperties::createNewDynamicProperty(QObject
    #      *object, QQmlEngine *engine, const QString &name)
    Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties24createNewDynamicProper'
        'tyEP7QObjectP10QQmlEngineRK7QString',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._addressOf(engine), name,
    )

  @staticmethod
  @overload(QObject, QQmlEngine)
  @overload(QObject, NoneType)
  @overload(NoneType, QQmlEngine)
  @overload(NoneType, NoneType)
  def registerNodeInstanceMetaObject(
      object: Optional[QObject],
      engine: Optional[QQmlEngine],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupportProperties::registerNodeInstanceMetaObject(QObject
    *object, QQmlEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupportProperties::registerNodeInstanceMetaObject(
    #      QObject *object, QQmlEngine *engine)
    Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties30registerNodeInstanceMe'
        'taObjectEP7QObjectP10QQmlEngine',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._addressOf(engine),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def registerCustomData(object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupportProperties::registerCustomData(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupportProperties::registerCustomData(QObject
    #      *object)
    Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties18registerCustomDataEP7Q'
        'Object',
        CuteMixin._addressOf(object, 'QObject'),
    )

  @staticmethod
  @overload(QObject, QByteArray)
  @overload(NoneType, QByteArray)
  def getResetValue(
      object: Optional[QObject],
      propertyName: QByteArray,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant
    QQuickDesignerSupportProperties::getResetValue(QObject *object, const
    QQuickDesignerSupport::PropertyName &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html#getResetValue

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickDesignerSupportProperties::getResetValue(QObject
    #      *object, const QQuickDesignerSupport::PropertyName &propertyName)
    address = Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties13getResetValueEP7QObjec'
        'tRK10QByteArray',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._valueOf(propertyName),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(QObject, QQmlContext, QByteArray)
  @overload(QObject, NoneType, QByteArray)
  @overload(NoneType, QQmlContext, QByteArray)
  @overload(NoneType, NoneType, QByteArray)
  def doResetProperty(
      object: Optional[QObject],
      context: Optional[QQmlContext],
      propertyName: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupportProperties::doResetProperty(QObject
    *object, QQmlContext *context, const QQuickDesignerSupport::PropertyName
    &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuickDesignerSupportProperties::doResetProperty(QObject *object,
    #      QQmlContext *context, const QQuickDesignerSupport::PropertyName
    #      &propertyName)
    Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties15doResetPropertyEP7QObj'
        'ectP11QQmlContextRK10QByteArray',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._addressOf(context), CuteMixin._valueOf(propertyName),
    )

  @staticmethod
  @overload(QObject, QByteArray)
  @overload(NoneType, QByteArray)
  def hasValidResetBinding(
      object: Optional[QObject],
      propertyName: QByteArray,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickDesignerSupportProperties::hasValidResetBinding(QObject *object,
    const QQuickDesignerSupport::PropertyName &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QQuickDesignerSupportProperties::hasValidResetBinding(QObject
    #      *object, const QQuickDesignerSupport::PropertyName &propertyName)
    return Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties20hasValidResetBindingEP'
        '7QObjectRK10QByteArray',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._valueOf(propertyName),
    )

  @staticmethod
  @overload(QObject, QQmlContext, QByteArray, str)
  @overload(QObject, NoneType, QByteArray, str)
  @overload(NoneType, QQmlContext, QByteArray, str)
  @overload(NoneType, NoneType, QByteArray, str)
  def setPropertyBinding(
      object: Optional[QObject],
      context: Optional[QQmlContext],
      propertyName: QByteArray,
      expression: str,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupportProperties::setPropertyBinding(QObject *object,
    QQmlContext *context, const QQuickDesignerSupport::PropertyName
    &propertyName, const QString &expression)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    expression : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickDesignerSupportProperties::setPropertyBinding(QObject
    #      *object, QQmlContext *context, const
    #      QQuickDesignerSupport::PropertyName &propertyName, const QString
    #      &expression)
    Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties18setPropertyBindingEP7Q'
        'ObjectP11QQmlContextRK10QByteArrayRK7QString',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._addressOf(context), CuteMixin._valueOf(propertyName),
        expression,
    )

  @staticmethod
  @overload(QObject, QQmlContext, QByteArray)
  @overload(QObject, NoneType, QByteArray)
  @overload(NoneType, QQmlContext, QByteArray)
  @overload(NoneType, NoneType, QByteArray)
  def keepBindingFromGettingDeleted(
      object: Optional[QObject],
      context: Optional[QQmlContext],
      propertyName: QByteArray,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupportProperties::keepBindingFromGettingDeleted(QObject
    *object, QQmlContext *context, const QQuickDesignerSupport::PropertyName
    &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuickDesignerSupportProperties::keepBindingFromGettingDeleted(
    #      QObject *object, QQmlContext *context, const
    #      QQuickDesignerSupport::PropertyName &propertyName)
    Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties29keepBindingFromGetting'
        'DeletedEP7QObjectP11QQmlContextRK10QByteArray',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._addressOf(context), CuteMixin._valueOf(propertyName),
    )

  @staticmethod
  @overload(QMetaProperty)
  def isPropertyQObject(metaProperty: QMetaProperty) -> bool:
    """
    Calls Qt's 'bool QQuickDesignerSupportProperties::isPropertyQObject(const
    QMetaProperty &metaProperty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html

    Parameters
    ----------

    metaProperty : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.
    """
    #  bool QQuickDesignerSupportProperties::isPropertyQObject(const
    #      QMetaProperty &metaProperty)
    return Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties17isPropertyQObjectERK13'
        'QMetaProperty',
        CuteMixin._valueOf(metaProperty),
    )

  @staticmethod
  @overload(QMetaProperty, QObject)
  @overload(QMetaProperty, NoneType)
  def readQObjectProperty(
      metaProperty: QMetaProperty,
      object: Optional[QObject],
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject
    *QQuickDesignerSupportProperties::readQObjectProperty(const QMetaProperty
    &metaProperty, QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html

    Parameters
    ----------

    metaProperty : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickDesignerSupportProperties::readQObjectProperty(const
    #      QMetaProperty &metaProperty, QObject *object)
    address = Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties19readQObjectPropertyERK'
        '13QMetaPropertyP7QObject',
        CuteMixin._valueOf(metaProperty), CuteMixin._addressOf(object,
        'QObject'),
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def getPropertyCache(object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupportProperties::getPropertyCache(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupportProperties::getPropertyCache(QObject
    #      *object)
    Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties16getPropertyCacheEP7QOb'
        'ject',
        CuteMixin._addressOf(object, 'QObject'),
    )

  @staticmethod
  @overload(QByteArray)
  def isPropertyBlackListed(propertyName: QByteArray) -> bool:
    """
    Calls Qt's 'bool
    QQuickDesignerSupportProperties::isPropertyBlackListed(const
    QQuickDesignerSupport::PropertyName &propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html

    Parameters
    ----------

    propertyName : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QQuickDesignerSupportProperties::isPropertyBlackListed(const
    #      QQuickDesignerSupport::PropertyName &propertyName)
    return Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties21isPropertyBlackListedE'
        'RK10QByteArray',
        CuteMixin._valueOf(propertyName),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def propertyNameListForWritableProperties(
      object: Optional[QObject],
  ) -> QList[QByteArray]:
    """
    Calls Qt's 'QQuickDesignerSupport::PropertyNameList
    QQuickDesignerSupportProperties::propertyNameListForWritableProperties(
    QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QQuickDesignerSupport::PropertyNameList
    #      QQuickDesignerSupportProperties::
    #      propertyNameListForWritableProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties37propertyNameListForWri'
        'tablePropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @staticmethod
  @overload(QQmlListReference)
  def hasFullImplementedListInterface(list: QQmlListReference) -> bool:
    """
    Calls Qt's 'bool
    QQuickDesignerSupportProperties::hasFullImplementedListInterface(const
    QQmlListReference &list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupportproperties.html

    Parameters
    ----------

    list : QQmlListReference
      Passed on as a value: Qt reads the C++ QQmlListReference, which stays
      Python's own.
    """
    #  bool QQuickDesignerSupportProperties::hasFullImplementedListInterface(
    #      const QQmlListReference &list)
    return Rituals.call(
        'ritual_ZN31QQuickDesignerSupportProperties31hasFullImplementedList'
        'InterfaceERK17QQmlListReference',
        CuteMixin._valueOf(list),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDesignerSupportProperties'

  #  Qt's '~QQuickDesignerSupportProperties()'. Naming it makes this a value
  #  class: Python owns every C++ QQuickDesignerSupportProperties behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QQuickDesignerSupportPropertiesD1Ev'

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
  def allPropertyNames(*__, **_) -> Never:
    """
    Qt's 'QQuickDesignerSupport::PropertyNameList
    QQuickDesignerSupportProperties::allPropertyNames(QObject *object, const
    QQuickDesignerSupport::PropertyName &baseName, QObjectList
    *inspectedObjects, int depth)': names 'QObjectList', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuickDesignerSupportProperties.allPropertyNames' has no cute "
        "function yet. Qt's 'QQuickDesignerSupport::PropertyNameList "
        "QQuickDesignerSupportProperties::allPropertyNames(QObject *object, "
        "const QQuickDesignerSupport::PropertyName &baseName, QObjectList "
        "*inspectedObjects, int depth)': names 'QObjectList', which has no "
        "cute class yet.")

  @staticmethod
  def hasBindingForProperty(*__, **_) -> Never:
    """
    Qt's 'bool QQuickDesignerSupportProperties::hasBindingForProperty(QObject
    *object, QQmlContext *context, const QQuickDesignerSupport::PropertyName
    &propertyName, bool *hasChanged)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQuickDesignerSupportProperties.hasBindingForProperty' has no "
        "cute function yet. Qt's 'bool "
        "QQuickDesignerSupportProperties::hasBindingForProperty(QObject "
        "*object, QQmlContext *context, const "
        "QQuickDesignerSupport::PropertyName &propertyName, bool "
        "*hasChanged)': takes a number to change where it is.")

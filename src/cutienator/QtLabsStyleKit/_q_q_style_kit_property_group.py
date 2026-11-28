"""
QQStyleKitPropertyGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitPropertyGroup to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteFlags
from ..QtCore import QObject
from . import PropertyPathId, QQSK

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQStyleKitControlProperties


class QQStyleKitPropertyGroup(QObject):
  """
  The cute side of Qt's QQStyleKitPropertyGroup: a plain Python object
  standing in front of one C++ QQStyleKitPropertyGroup.

  It is built on the cute 'QObject', as Qt's QQStyleKitPropertyGroup is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitPropertyGroup that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'propertyPathId',
  'isControlProperties', 'controlProperties', 'pathFlags',
  'shouldEmitLocally', 'shouldEmitGlobally'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitPropertyGroup::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQStyleKitPropertyGroup::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  13 of the 22 functions Qt declares: 6 a template; 3 leans on
  'QQStyleKitPropertyGroup; 2 not a gap; 1 leans on 'vtable for
  QQStyleKitPropertyGroup', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 leans on
  'QQStyleKitDebug.

  What to expect
  --------------

  - The C++ QQStyleKitPropertyGroup is created at the first use, not by
    'QQStyleKitPropertyGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitPropertyGroup.
  - Qt tells when it has removed the C++ QQStyleKitPropertyGroup. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitPropertyGroup that has no cute function yet,
    '__init__', 'emitChangedForAllStylePropertiesRecursive',
    'handleStylePropertiesChanged', 'handleStylePropertyChanged',
    'isDefined', 'lazyCreateGroup', 'pathToString', 'setStyleProperty',
    'styleProperty', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QQStyleKitPropertyGroup, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class EmitFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QQStyleKitPropertyGroup::EmitFlag' of Qt, with the 2
    names Qt gives in it. Qt names the type of its combinations
    'QQStyleKitPropertyGroup::EmitFlags'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    AllProperties = 0x0
    Colors = 0x1

  EmitFlags = EmitFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitPropertyGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitPropertyGroup::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpropertygroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitPropertyGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQStyleKitPropertyGroup10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QQSK.Property, PropertyPathId.Flag)
  def propertyPathId(
      self,
      property: QQSK.Property,
      flag: PropertyPathId.Flag,
  ) -> PropertyPathId:
    """
    Calls Qt's 'PropertyPathId
    QQStyleKitPropertyGroup::propertyPathId(QQSK::Property property,
    PropertyPathId::Flag flag) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpropertygroup.html#propertyPathId

    Parameters
    ----------

    property : QQSK.Property
      Passed on as its number.

    flag : PropertyPathId.Flag
      Passed on as its number.

    Returns
    -------

    PropertyPathId
      A new cute PropertyPathId around the copy Qt gave back. Python owns it.
    """
    #  PropertyPathId QQStyleKitPropertyGroup::propertyPathId(QQSK::Property
    #      property, PropertyPathId::Flag flag) const
    address = self.uglySide.call(
        'ritual_ZNK23QQStyleKitPropertyGroup14propertyPathIdEN4QQSK8Propert'
        'yEN14PropertyPathId4FlagE',
        property.value, flag.value,
    )
    return PropertyPathId._cuteOwning(address)

  def isControlProperties(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitPropertyGroup::isControlProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpropertygroup.html#isControlProperties
    """
    #  bool QQStyleKitPropertyGroup::isControlProperties() const
    return self.uglySide.call(
        'ritual_ZNK23QQStyleKitPropertyGroup19isControlPropertiesEv',
    )

  def controlProperties(self) -> Optional[QQStyleKitControlProperties]:
    """
    Calls Qt's 'QQStyleKitControlProperties
    *QQStyleKitPropertyGroup::controlProperties() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpropertygroup.html#controlProperties

    Returns
    -------

    Optional[QQStyleKitControlProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitControlProperties
    #      *QQStyleKitPropertyGroup::controlProperties() const
    address = self.uglySide.call(
        'ritual_ZNK23QQStyleKitPropertyGroup17controlPropertiesEv',
    )
    from . import QQStyleKitControlProperties
    return QQStyleKitControlProperties._cuteAt(address)

  def pathFlags(self) -> QQSK.PropertyPathFlags:
    """
    Calls Qt's 'QQSK::PropertyPathFlags QQStyleKitPropertyGroup::pathFlags()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpropertygroup.html#pathFlags

    Returns
    -------

    QQSK.PropertyPathFlags
      The value standing for the combination Qt gave back.
    """
    #  QQSK::PropertyPathFlags QQStyleKitPropertyGroup::pathFlags() const
    return QQSK.PropertyPathFlags(self.uglySide.call(
        'ritual_ZNK23QQStyleKitPropertyGroup9pathFlagsEv',
    ))

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
    Qt's
    'QQStyleKitPropertyGroup::QQStyleKitPropertyGroup(QQSK::PropertyGroup
    group, QObject *parent)': leans on 'vtable for QQStyleKitPropertyGroup',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyGroup.__init__' has no cute function yet. Qt's "
        "'QQStyleKitPropertyGroup::QQStyleKitPropertyGroup(QQSK::PropertyGro"
        "up group, QObject *parent)': leans on 'vtable for "
        "QQStyleKitPropertyGroup', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

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

  def shouldEmitLocally(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitPropertyGroup::shouldEmitLocally()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpropertygroup.html#shouldEmitLocally
    """
    #  bool QQStyleKitPropertyGroup::shouldEmitLocally()
    return self.uglySide.call(
        'ritual_ZN23QQStyleKitPropertyGroup17shouldEmitLocallyEv',
    )

  def shouldEmitGlobally(self) -> bool:
    """
    Calls Qt's 'bool QQStyleKitPropertyGroup::shouldEmitGlobally()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitpropertygroup.html#shouldEmitGlobally
    """
    #  bool QQStyleKitPropertyGroup::shouldEmitGlobally()
    return self.uglySide.call(
        'ritual_ZN23QQStyleKitPropertyGroup18shouldEmitGloballyEv',
    )

  @staticmethod
  def emitChangedForAllStylePropertiesRecursive(*__, **_) -> Never:
    """
    Qt's 'void
    QQStyleKitPropertyGroup::emitChangedForAllStylePropertiesRecursive(
    EmitFlags emitFlags)': leans on
    'QQStyleKitPropertyGroup::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyGroup.emitChangedForAllStylePropertiesRecursive'"
        " has no cute function yet. Qt's 'void "
        "QQStyleKitPropertyGroup::emitChangedForAllStylePropertiesRecursive("
        "EmitFlags emitFlags)': leans on "
        "'QQStyleKitPropertyGroup::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def handleStylePropertiesChanged(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitPropertyGroup::handleStylePropertiesChanged': a template:
    a pattern and no single function.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyGroup.handleStylePropertiesChanged' has no cute "
        "function yet. Qt's "
        "'QQStyleKitPropertyGroup::handleStylePropertiesChanged': a "
        "template: a pattern and no single function.")

  @staticmethod
  def handleStylePropertyChanged(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitPropertyGroup::handleStylePropertyChanged': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyGroup.handleStylePropertyChanged' has no cute "
        "function yet. Qt's "
        "'QQStyleKitPropertyGroup::handleStylePropertyChanged': a template: "
        "a pattern and no single function.")

  @staticmethod
  def isDefined(*__, **_) -> Never:
    """
    Qt's 'bool QQStyleKitPropertyGroup::isDefined(QQSK::Property property)
    const': leans on 'QQStyleKitDebug::groupBeingRead', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyGroup.isDefined' has no cute function yet. Qt's "
        "'bool QQStyleKitPropertyGroup::isDefined(QQSK::Property property) "
        "const': leans on 'QQStyleKitDebug::groupBeingRead', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def lazyCreateGroup(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitPropertyGroup::lazyCreateGroup': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyGroup.lazyCreateGroup' has no cute function "
        "yet. Qt's 'QQStyleKitPropertyGroup::lazyCreateGroup': a template: "
        "a pattern and no single function.")

  @staticmethod
  def pathToString(*__, **_) -> Never:
    """
    Qt's 'QString QQStyleKitPropertyGroup::pathToString() const': leans on
    'QQStyleKitPropertyGroup::s_pathStrings', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyGroup.pathToString' has no cute function yet. "
        "Qt's 'QString QQStyleKitPropertyGroup::pathToString() const': "
        "leans on 'QQStyleKitPropertyGroup::s_pathStrings', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setStyleProperty(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitPropertyGroup::setStyleProperty': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyGroup.setStyleProperty' has no cute function "
        "yet. Qt's 'QQStyleKitPropertyGroup::setStyleProperty': a template: "
        "a pattern and no single function.")

  @staticmethod
  def styleProperty(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitPropertyGroup::styleProperty': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QQStyleKitPropertyGroup.styleProperty' has no cute function yet. "
        "Qt's 'QQStyleKitPropertyGroup::styleProperty': a template: a "
        "pattern and no single function.")

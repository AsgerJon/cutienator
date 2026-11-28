"""
QQStyleKitDebug binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitdebug_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitDebug to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQSK

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import PropertyPathId, QQStyleKitControlProperties
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  PropertyPathId = WAIT['PropertyPathId']
  QQStyleKitControlProperties = WAIT['QQStyleKitControlProperties']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQStyleKitDebug(QObject):
  """
  The cute side of Qt's QQStyleKitDebug: a plain Python object standing in
  front of one C++ QQStyleKitDebug.

  It is built on the cute 'QObject', as Qt's QQStyleKitDebug is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitDebug that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'controlChanged',
  'filterChanged', 'trace', 'objectName'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitDebug::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQStyleKitDebug::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQStyleKitDebug::notifyPropertyWrite(const
    QQStyleKitPropertyGroup *group, const QQSK::Property property, const
    QQStyleKitControlProperties *storage, const QQSK::State state, const
    PropertyStorageId key, const QVariant &value)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  17 of the 25 functions Qt declares: 8 leans on 'QQStyleKitDebug; 3 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file; 2 not a gap; 2 leans on 'QString QQStyleKitDebug; 1 a
  template; 1 leans on 'QQStyleKitControl.

  What to expect
  --------------

  - The C++ QQStyleKitDebug is created at the first use, not by
    'QQStyleKitDebug(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitDebug.
  - Qt tells when it has removed the C++ QQStyleKitDebug. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitDebug that has no cute function yet,
    'control', 'controlToString', 'enabled', 'enumToString', 'filter',
    'insideControl', 'notifyPropertyNotResolved', 'notifyPropertyRead',
    'notifyPropertyWrite', 'objectPath', 'propertyPath', 'setControl',
    'setFilter', 'stateToString', 'styleReaderToString', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(PropertyPathId, QQStyleKitControlProperties, QQSK.State, int)
  @overload(PropertyPathId, NoneType, QQSK.State, int)
  def trace(
      property: PropertyPathId,
      resolvedControl: Optional[QQStyleKitControlProperties],
      state: QQSK.State,
      key: int,
  ) -> None:
    """
    Calls Qt's 'void QQStyleKitDebug::trace(const PropertyPathId property,
    const QQStyleKitControlProperties *resolvedControl, const QQSK::State
    state, const PropertyStorageId key)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitdebug.html#trace

    Parameters
    ----------

    property : PropertyPathId
      Passed on as a value: Qt reads the C++ PropertyPathId, which stays
      Python's own.

    resolvedControl : Optional[QQStyleKitControlProperties]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    state : QQSK.State
      Passed on as its number.

    key : int
      Passed on as it is.
    """
    #  void QQStyleKitDebug::trace(const PropertyPathId property, const
    #      QQStyleKitControlProperties *resolvedControl, const QQSK::State
    #      state, const PropertyStorageId key)
    Rituals.call(
        'ritual_ZN15QQStyleKitDebug5traceE14PropertyPathIdPK27QQStyleKitCon'
        'trolProperties6QFlagsIN4QQSK9StateFlagEEj',
        CuteMixin._valueOf(property), CuteMixin._addressOf(resolvedControl),
        state.value, key,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def objectName(obj: Optional[QObject]) -> str:
    """
    Calls Qt's 'QString QQStyleKitDebug::objectName(const QObject *obj)'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitdebug.html#objectName

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQStyleKitDebug::objectName(const QObject *obj)
    return Rituals.call(
        'ritual_ZN15QQStyleKitDebug10objectNameEPK7QObject',
        CuteMixin._addressOf(obj, 'QObject'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitDebug'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitDebug::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitdebug.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitDebug::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQStyleKitDebug10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  def controlChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDebug::controlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdebug.html#controlChanged
    """
    #  void QQStyleKitDebug::controlChanged()
    self.uglySide.call('ritual_ZN15QQStyleKitDebug14controlChangedEv')

  def filterChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDebug::filterChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitdebug.html#filterChanged
    """
    #  void QQStyleKitDebug::filterChanged()
    self.uglySide.call('ritual_ZN15QQStyleKitDebug13filterChangedEv')

  @staticmethod
  def control(*__, **_) -> Never:
    """
    Qt's 'QQuickItem *QQStyleKitDebug::control() const': leans on
    'QQStyleKitDebug::m_item', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.control' has no cute function yet. Qt's "
        "'QQuickItem *QQStyleKitDebug::control() const': leans on "
        "'QQStyleKitDebug::m_item', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def controlToString(*__, **_) -> Never:
    """
    Qt's 'QString QQStyleKitDebug::controlToString(const
    QQStyleKitControlProperties *control)': leans on
    'QQStyleKitControl::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.controlToString' has no cute function yet. Qt's "
        "'QString QQStyleKitDebug::controlToString(const "
        "QQStyleKitControlProperties *control)': leans on "
        "'QQStyleKitControl::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def enabled(*__, **_) -> Never:
    """
    Qt's 'bool QQStyleKitDebug::enabled()': leans on
    'QQStyleKitDebug::m_item', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.enabled' has no cute function yet. Qt's 'bool "
        "QQStyleKitDebug::enabled()': leans on 'QQStyleKitDebug::m_item', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def enumToString(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitDebug::enumToString': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.enumToString' has no cute function yet. Qt's "
        "'QQStyleKitDebug::enumToString': a template: a pattern and no "
        "single function.")

  @staticmethod
  def filter(*__, **_) -> Never:
    """
    Qt's 'QString QQStyleKitDebug::filter() const': leans on
    'QQStyleKitDebug::m_filter', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.filter' has no cute function yet. Qt's 'QString "
        "QQStyleKitDebug::filter() const': leans on "
        "'QQStyleKitDebug::m_filter', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def insideControl(*__, **_) -> Never:
    """
    Qt's 'bool QQStyleKitDebug::insideControl(const QObject *child)': leans
    on 'QQStyleKitDebug::m_item', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.insideControl' has no cute function yet. Qt's "
        "'bool QQStyleKitDebug::insideControl(const QObject *child)': leans "
        "on 'QQStyleKitDebug::m_item', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def notifyPropertyNotResolved(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitDebug::notifyPropertyNotResolved(const
    PropertyPathId property)': leans on 'QQStyleKitDebug::m_outputCount',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.notifyPropertyNotResolved' has no cute function "
        "yet. Qt's 'void QQStyleKitDebug::notifyPropertyNotResolved(const "
        "PropertyPathId property)': leans on "
        "'QQStyleKitDebug::m_outputCount', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def notifyPropertyRead(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitDebug::notifyPropertyRead(const PropertyPathId
    property, const QQStyleKitControlProperties *resolvedControl, const
    QQSK::State state, const QVariant &value)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'kDot'.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.notifyPropertyRead' has no cute function yet. "
        "Qt's 'void QQStyleKitDebug::notifyPropertyRead(const "
        "PropertyPathId property, const QQStyleKitControlProperties "
        "*resolvedControl, const QQSK::State state, const QVariant "
        "&value)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'kDot'.")

  @staticmethod
  def notifyPropertyWrite(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitDebug::notifyPropertyWrite(const
    QQStyleKitPropertyGroup *group, const QQSK::Property property, const
    QQStyleKitControlProperties *storage, const QQSK::State state, const
    PropertyStorageId key, const QVariant &value)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.notifyPropertyWrite' has no cute function yet. "
        "Qt's 'void QQStyleKitDebug::notifyPropertyWrite(const "
        "QQStyleKitPropertyGroup *group, const QQSK::Property property, "
        "const QQStyleKitControlProperties *storage, const QQSK::State "
        "state, const PropertyStorageId key, const QVariant &value)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def objectPath(*__, **_) -> Never:
    """
    Qt's 'QString QQStyleKitDebug::objectPath(const
    QQStyleKitControlProperties *properties, QObject *from)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'kDot'.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.objectPath' has no cute function yet. Qt's "
        "'QString QQStyleKitDebug::objectPath(const "
        "QQStyleKitControlProperties *properties, QObject *from)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier 'kDot'.")

  @staticmethod
  def propertyPath(*__, **_) -> Never:
    """
    Qt's 'QString QQStyleKitDebug::propertyPath(const QQStyleKitPropertyGroup
    *group, const PropertyPathId property)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'kDot'.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.propertyPath' has no cute function yet. Qt's "
        "'QString QQStyleKitDebug::propertyPath(const "
        "QQStyleKitPropertyGroup *group, const PropertyPathId property)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'kDot'.")

  @staticmethod
  def setControl(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitDebug::setControl(QQuickItem *item)': leans on
    'QQStyleKitDebug::controlChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.setControl' has no cute function yet. Qt's 'void "
        "QQStyleKitDebug::setControl(QQuickItem *item)': leans on "
        "'QQStyleKitDebug::controlChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setFilter(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitDebug::setFilter(const QString &filter)': leans on
    'QQStyleKitDebug::filterChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.setFilter' has no cute function yet. Qt's 'void "
        "QQStyleKitDebug::setFilter(const QString &filter)': leans on "
        "'QQStyleKitDebug::filterChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def stateToString(*__, **_) -> Never:
    """
    Qt's 'QString QQStyleKitDebug::stateToString(const QQSK::State state)':
    leans on 'QString QQStyleKitDebug::enumToString<QFlags<QQSK::StateFlag>
    >(QFlags<QQSK::StateFlag>)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.stateToString' has no cute function yet. Qt's "
        "'QString QQStyleKitDebug::stateToString(const QQSK::State state)': "
        "leans on 'QString "
        "QQStyleKitDebug::enumToString<QFlags<QQSK::StateFlag> "
        ">(QFlags<QQSK::StateFlag>)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def styleReaderToString(*__, **_) -> Never:
    """
    Qt's 'QString QQStyleKitDebug::styleReaderToString(const QQStyleKitReader
    *reader)': leans on 'QString
    QQStyleKitDebug::enumToString<QFlags<QQSK::StateFlag>
    >(QFlags<QQSK::StateFlag>)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDebug.styleReaderToString' has no cute function yet. "
        "Qt's 'QString QQStyleKitDebug::styleReaderToString(const "
        "QQStyleKitReader *reader)': leans on 'QString "
        "QQStyleKitDebug::enumToString<QFlags<QQSK::StateFlag> "
        ">(QFlags<QQSK::StateFlag>)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

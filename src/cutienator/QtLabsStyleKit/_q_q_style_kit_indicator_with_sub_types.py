"""
QQStyleKitIndicatorWithSubTypes binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitIndicatorWithSubTypes to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QQStyleKitDelegateProperties

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQStyleKitIndicatorWithSubTypes(QQStyleKitDelegateProperties):
  """
  The cute side of Qt's QQStyleKitIndicatorWithSubTypes: a plain Python
  object standing in front of one C++ QQStyleKitIndicatorWithSubTypes.

  It is built on the cute 'QQStyleKitDelegateProperties', as Qt's
  QQStyleKitIndicatorWithSubTypes is built on Qt's
  QQStyleKitDelegateProperties, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitIndicatorWithSubTypes that has a ritual
  and that Python can call so far, 6 names in all: 'metaObject',
  'foregroundChanged', 'upChanged', 'downChanged', 'firstChanged',
  'secondChanged'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitIndicatorWithSubTypes::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQStyleKitIndicatorWithSubTypes::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQStyleKitIndicatorWithSubTypes::qt_qmlMarker_uncreatable()':
    one of Qt's own inner workings.

  What has no ritual
  ------------------

  10 of the 19 functions Qt declares: 4 leans on
  'QQStyleKitIndicatorProperties* QQStyleKitPropertyGroup; 2 not a gap; 1 a
  template; 1 leans on 'QQStyleKitIndicatorWithSubTypes; 1 leans on 'vtable
  for QQStyleKitIndicatorWithSubTypes', which Qt's source does not mark for
  use from outside Qt and has no code for that could be taken; 1 leans on
  'QQStyleKitDelegateProperties* QQStyleKitPropertyGroup.

  What to expect
  --------------

  - The C++ QQStyleKitIndicatorWithSubTypes is created at the first use, not
    by 'QQStyleKitIndicatorWithSubTypes(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitIndicatorWithSubTypes.
  - Qt tells when it has removed the C++ QQStyleKitIndicatorWithSubTypes.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitIndicatorWithSubTypes that has no cute
    function yet, '__init__', 'down', 'first', 'foreground', 'second', 'up',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitIndicatorWithSubTypes'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQStyleKitIndicatorWithSubTypes::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitindicatorwithsubtypes.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitIndicatorWithSubTypes::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK31QQStyleKitIndicatorWithSubTypes10metaObjectEv',
    )
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QQStyleKitIndicatorWithSubTypes::QQStyleKitIndicatorWithSubTypes(QQSK::
    PropertyGroup group, QQStyleKitControlProperties *parent)': leans on
    'vtable for QQStyleKitIndicatorWithSubTypes', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitIndicatorWithSubTypes.__init__' has no cute function "
        "yet. Qt's "
        "'QQStyleKitIndicatorWithSubTypes::QQStyleKitIndicatorWithSubTypes(Q"
        "QSK::PropertyGroup group, QQStyleKitControlProperties *parent)': "
        "leans on 'vtable for QQStyleKitIndicatorWithSubTypes', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def foregroundChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitIndicatorWithSubTypes::foregroundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitindicatorwithsubtypes.html
    """
    #  void QQStyleKitIndicatorWithSubTypes::foregroundChanged()
    self.uglySide.call(
        'ritual_ZN31QQStyleKitIndicatorWithSubTypes17foregroundChangedEv',
    )

  def upChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitIndicatorWithSubTypes::upChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitindicatorwithsubtypes.html#upChanged
    """
    #  void QQStyleKitIndicatorWithSubTypes::upChanged()
    self.uglySide.call(
        'ritual_ZN31QQStyleKitIndicatorWithSubTypes9upChangedEv',
    )

  def downChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitIndicatorWithSubTypes::downChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitindicatorwithsubtypes.html#downChanged
    """
    #  void QQStyleKitIndicatorWithSubTypes::downChanged()
    self.uglySide.call(
        'ritual_ZN31QQStyleKitIndicatorWithSubTypes11downChangedEv',
    )

  def firstChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitIndicatorWithSubTypes::firstChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitindicatorwithsubtypes.html#firstChanged
    """
    #  void QQStyleKitIndicatorWithSubTypes::firstChanged()
    self.uglySide.call(
        'ritual_ZN31QQStyleKitIndicatorWithSubTypes12firstChangedEv',
    )

  def secondChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitIndicatorWithSubTypes::secondChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitindicatorwithsubtypes.html#secondChanged
    """
    #  void QQStyleKitIndicatorWithSubTypes::secondChanged()
    self.uglySide.call(
        'ritual_ZN31QQStyleKitIndicatorWithSubTypes13secondChangedEv',
    )

  @staticmethod
  def down(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitIndicatorProperties
    *QQStyleKitIndicatorWithSubTypes::down() const': leans on
    'QQStyleKitIndicatorProperties*
    QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitIndicatorProperties>(
    QQStyleKitIndicatorProperties* const&, QQSK::PropertyGroup) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitIndicatorWithSubTypes.down' has no cute function yet. "
        "Qt's 'QQStyleKitIndicatorProperties "
        "*QQStyleKitIndicatorWithSubTypes::down() const': leans on "
        "'QQStyleKitIndicatorProperties* "
        "QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitIndicatorPropert"
        "ies>(QQStyleKitIndicatorProperties* const&, QQSK::PropertyGroup) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def first(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitIndicatorProperties
    *QQStyleKitIndicatorWithSubTypes::first() const': leans on
    'QQStyleKitIndicatorProperties*
    QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitIndicatorProperties>(
    QQStyleKitIndicatorProperties* const&, QQSK::PropertyGroup) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitIndicatorWithSubTypes.first' has no cute function yet. "
        "Qt's 'QQStyleKitIndicatorProperties "
        "*QQStyleKitIndicatorWithSubTypes::first() const': leans on "
        "'QQStyleKitIndicatorProperties* "
        "QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitIndicatorPropert"
        "ies>(QQStyleKitIndicatorProperties* const&, QQSK::PropertyGroup) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def foreground(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitDelegateProperties
    *QQStyleKitIndicatorWithSubTypes::foreground() const': leans on
    'QQStyleKitDelegateProperties*
    QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitDelegateProperties>(
    QQStyleKitDelegateProperties* const&, QQSK::PropertyGroup) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitIndicatorWithSubTypes.foreground' has no cute function "
        "yet. Qt's 'QQStyleKitDelegateProperties "
        "*QQStyleKitIndicatorWithSubTypes::foreground() const': leans on "
        "'QQStyleKitDelegateProperties* "
        "QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitDelegateProperti"
        "es>(QQStyleKitDelegateProperties* const&, QQSK::PropertyGroup) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def second(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitIndicatorProperties
    *QQStyleKitIndicatorWithSubTypes::second() const': leans on
    'QQStyleKitIndicatorProperties*
    QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitIndicatorProperties>(
    QQStyleKitIndicatorProperties* const&, QQSK::PropertyGroup) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitIndicatorWithSubTypes.second' has no cute function yet. "
        "Qt's 'QQStyleKitIndicatorProperties "
        "*QQStyleKitIndicatorWithSubTypes::second() const': leans on "
        "'QQStyleKitIndicatorProperties* "
        "QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitIndicatorPropert"
        "ies>(QQStyleKitIndicatorProperties* const&, QQSK::PropertyGroup) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def up(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitIndicatorProperties
    *QQStyleKitIndicatorWithSubTypes::up() const': leans on
    'QQStyleKitIndicatorProperties*
    QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitIndicatorProperties>(
    QQStyleKitIndicatorProperties* const&, QQSK::PropertyGroup) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitIndicatorWithSubTypes.up' has no cute function yet. "
        "Qt's 'QQStyleKitIndicatorProperties "
        "*QQStyleKitIndicatorWithSubTypes::up() const': leans on "
        "'QQStyleKitIndicatorProperties* "
        "QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitIndicatorPropert"
        "ies>(QQStyleKitIndicatorProperties* const&, QQSK::PropertyGroup) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

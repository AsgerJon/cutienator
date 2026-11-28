"""
QQStyleKitIndicatorProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitIndicatorProperties to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QQStyleKitDelegateProperties

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQStyleKitIndicatorProperties(QQStyleKitDelegateProperties):
  """
  The cute side of Qt's QQStyleKitIndicatorProperties: a plain Python object
  standing in front of one C++ QQStyleKitIndicatorProperties.

  It is built on the cute 'QQStyleKitDelegateProperties', as Qt's
  QQStyleKitIndicatorProperties is built on Qt's
  QQStyleKitDelegateProperties, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitIndicatorProperties that has a ritual and
  that Python can call so far, 2 names in all: 'metaObject',
  'foregroundChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitIndicatorProperties::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQStyleKitIndicatorProperties::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQStyleKitIndicatorProperties::qt_qmlMarker_uncreatable()':
    one of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 11 functions Qt declares: 2 not a gap; 1 a template; 1 leans on
  'QQStyleKitIndicatorProperties; 1 leans on 'vtable for
  QQStyleKitIndicatorProperties', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken; 1 leans on
  'QQStyleKitDelegateProperties* QQStyleKitPropertyGroup.

  What to expect
  --------------

  - The C++ QQStyleKitIndicatorProperties is created at the first use, not by
    'QQStyleKitIndicatorProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitIndicatorProperties.
  - Qt tells when it has removed the C++ QQStyleKitIndicatorProperties. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitIndicatorProperties that has no cute function
    yet, '__init__', 'foreground', holds a function that raises
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
  __qt_class__ = 'QQStyleKitIndicatorProperties'

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
    *QQStyleKitIndicatorProperties::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitindicatorproperties.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitIndicatorProperties::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQStyleKitIndicatorProperties10metaObjectEv',
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
    Qt's 'QQStyleKitIndicatorProperties::QQStyleKitIndicatorProperties(QQSK::
    PropertyGroup group, QQStyleKitControlProperties *parent)': leans on
    'vtable for QQStyleKitIndicatorProperties', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitIndicatorProperties.__init__' has no cute function yet. "
        "Qt's "
        "'QQStyleKitIndicatorProperties::QQStyleKitIndicatorProperties(QQSK:"
        ":PropertyGroup group, QQStyleKitControlProperties *parent)': leans "
        "on 'vtable for QQStyleKitIndicatorProperties', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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
    Calls Qt's 'void QQStyleKitIndicatorProperties::foregroundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitindicatorproperties.html
    """
    #  void QQStyleKitIndicatorProperties::foregroundChanged()
    self.uglySide.call(
        'ritual_ZN29QQStyleKitIndicatorProperties17foregroundChangedEv',
    )

  @staticmethod
  def foreground(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitDelegateProperties
    *QQStyleKitIndicatorProperties::foreground() const': leans on
    'QQStyleKitDelegateProperties*
    QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitDelegateProperties>(
    QQStyleKitDelegateProperties* const&, QQSK::PropertyGroup) const', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitIndicatorProperties.foreground' has no cute function "
        "yet. Qt's 'QQStyleKitDelegateProperties "
        "*QQStyleKitIndicatorProperties::foreground() const': leans on "
        "'QQStyleKitDelegateProperties* "
        "QQStyleKitPropertyGroup::lazyCreateGroup<QQStyleKitDelegateProperti"
        "es>(QQStyleKitDelegateProperties* const&, QQSK::PropertyGroup) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

"""
QQuickPositionerAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickPositionerAttached to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuickPositionerAttached(QObject):
  """
  The cute side of Qt's QQuickPositionerAttached: a plain Python object
  standing in front of one C++ QQuickPositionerAttached.

  It is built on the cute 'QObject', as Qt's QQuickPositionerAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPositionerAttached that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'index',
  'isFirstItem', 'isLastItem', 'indexChanged', 'isFirstItemChanged',
  'isLastItemChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPositionerAttached::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickPositionerAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  7 of the 16 functions Qt declares: 4 leans on 'QQuickPositionerAttached; 2
  not a gap; 1 leans on 'vtable for QQuickPositionerAttached', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken.

  What to expect
  --------------

  - The C++ QQuickPositionerAttached is created at the first use, not by
    'QQuickPositionerAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPositionerAttached.
  - Qt tells when it has removed the C++ QQuickPositionerAttached. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickPositionerAttached that has no cute function yet,
    '__init__', 'setIndex', 'setIsFirstItem', 'setIsLastItem', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPositionerAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPositionerAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpositionerattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPositionerAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickPositionerAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def index(self) -> int:
    """
    Calls Qt's 'int QQuickPositionerAttached::index() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpositionerattached.html#index
    """
    #  int QQuickPositionerAttached::index() const
    return self.uglySide.call('ritual_ZNK24QQuickPositionerAttached5indexEv')

  def isFirstItem(self) -> bool:
    """
    Calls Qt's 'bool QQuickPositionerAttached::isFirstItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpositionerattached.html#isFirstItem
    """
    #  bool QQuickPositionerAttached::isFirstItem() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickPositionerAttached11isFirstItemEv',
    )

  def isLastItem(self) -> bool:
    """
    Calls Qt's 'bool QQuickPositionerAttached::isLastItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpositionerattached.html#isLastItem
    """
    #  bool QQuickPositionerAttached::isLastItem() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickPositionerAttached10isLastItemEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickPositionerAttached::QQuickPositionerAttached(QObject
    *parent)': leans on 'vtable for QQuickPositionerAttached', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickPositionerAttached.__init__' has no cute function yet. Qt's "
        "'QQuickPositionerAttached::QQuickPositionerAttached(QObject "
        "*parent)': leans on 'vtable for QQuickPositionerAttached', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def indexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPositionerAttached::indexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpositionerattached.html#indexChanged
    """
    #  void QQuickPositionerAttached::indexChanged()
    self.uglySide.call('ritual_ZN24QQuickPositionerAttached12indexChangedEv')

  def isFirstItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPositionerAttached::isFirstItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpositionerattached.html#isFirstItemChanged
    """
    #  void QQuickPositionerAttached::isFirstItemChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickPositionerAttached18isFirstItemChangedEv',
    )

  def isLastItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPositionerAttached::isLastItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpositionerattached.html#isLastItemChanged
    """
    #  void QQuickPositionerAttached::isLastItemChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickPositionerAttached17isLastItemChangedEv',
    )

  @staticmethod
  def setIndex(*__, **_) -> Never:
    """
    Qt's 'void QQuickPositionerAttached::setIndex(int index)': leans on
    'QQuickPositionerAttached::indexChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPositionerAttached.setIndex' has no cute function yet. Qt's "
        "'void QQuickPositionerAttached::setIndex(int index)': leans on "
        "'QQuickPositionerAttached::indexChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setIsFirstItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickPositionerAttached::setIsFirstItem(bool isFirstItem)':
    leans on 'QQuickPositionerAttached::isFirstItemChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickPositionerAttached.setIsFirstItem' has no cute function "
        "yet. Qt's 'void QQuickPositionerAttached::setIsFirstItem(bool "
        "isFirstItem)': leans on "
        "'QQuickPositionerAttached::isFirstItemChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setIsLastItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickPositionerAttached::setIsLastItem(bool isLastItem)':
    leans on 'QQuickPositionerAttached::isLastItemChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickPositionerAttached.setIsLastItem' has no cute function yet. "
        "Qt's 'void QQuickPositionerAttached::setIsLastItem(bool "
        "isLastItem)': leans on "
        "'QQuickPositionerAttached::isLastItemChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

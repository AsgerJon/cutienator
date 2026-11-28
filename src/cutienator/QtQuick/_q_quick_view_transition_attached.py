"""
QQuickViewTransitionAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickViewTransitionAttached to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from . import QQuickItem


class QQuickViewTransitionAttached(QObject):
  """
  The cute side of Qt's QQuickViewTransitionAttached: a plain Python object
  standing in front of one C++ QQuickViewTransitionAttached.

  It is built on the cute 'QObject', as Qt's QQuickViewTransitionAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickViewTransitionAttached that has a ritual and
  that Python can call so far, 9 names in all: 'metaObject', 'index', 'item',
  'destination', 'indexChanged', 'itemChanged', 'destinationChanged',
  'targetIndexesChanged', 'targetItemsChanged'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickViewTransitionAttached::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickViewTransitionAttached::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickViewTransitionAttached::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.
  - Qt's 'void QQuickViewTransitionAttached::qt_qmlMarker_attached()': one of
    Qt's own inner workings.
  - Qt's 'QList<int> QQuickViewTransitionAttached::targetIndexes() const':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QObject>
    QQuickViewTransitionAttached::targetItems()': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  5 of the 20 functions Qt declares: 2 not a gap; 2 leans on 'vtable for
  QQuickViewTransitionAttached', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken; 1 leans on
  'QQuickViewTransitionAttached.

  What to expect
  --------------

  - The C++ QQuickViewTransitionAttached is created at the first use, not by
    'QQuickViewTransitionAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickViewTransitionAttached.
  - Qt tells when it has removed the C++ QQuickViewTransitionAttached. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickViewTransitionAttached that has no cute function
    yet, '__init__', 'qmlAttachedProperties', 'targetIndexes', 'targetItems',
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
  __qt_class__ = 'QQuickViewTransitionAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickViewTransitionAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewtransitionattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickViewTransitionAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickViewTransitionAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def index(self) -> int:
    """
    Calls Qt's 'int QQuickViewTransitionAttached::index() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewtransitionattached.html#index
    """
    #  int QQuickViewTransitionAttached::index() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickViewTransitionAttached5indexEv',
    )

  def item(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickViewTransitionAttached::item() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewtransitionattached.html#item

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickViewTransitionAttached::item() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickViewTransitionAttached4itemEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def destination(self) -> QPointF:
    """
    Calls Qt's 'QPointF QQuickViewTransitionAttached::destination() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewtransitionattached.html#destination

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QQuickViewTransitionAttached::destination() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickViewTransitionAttached11destinationEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

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
    Qt's 'QQuickViewTransitionAttached::QQuickViewTransitionAttached(QObject
    *parent)': leans on 'vtable for QQuickViewTransitionAttached', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickViewTransitionAttached.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickViewTransitionAttached::QQuickViewTransitionAttached(QObject"
        " *parent)': leans on 'vtable for QQuickViewTransitionAttached', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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
    Calls Qt's 'void QQuickViewTransitionAttached::indexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewtransitionattached.html#indexChanged
    """
    #  void QQuickViewTransitionAttached::indexChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickViewTransitionAttached12indexChangedEv',
    )

  def itemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickViewTransitionAttached::itemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewtransitionattached.html#itemChanged
    """
    #  void QQuickViewTransitionAttached::itemChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickViewTransitionAttached11itemChangedEv',
    )

  def destinationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickViewTransitionAttached::destinationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewtransitionattached.html
    """
    #  void QQuickViewTransitionAttached::destinationChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickViewTransitionAttached18destinationChangedEv',
    )

  def targetIndexesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickViewTransitionAttached::targetIndexesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewtransitionattached.html
    """
    #  void QQuickViewTransitionAttached::targetIndexesChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickViewTransitionAttached20targetIndexesChangedEv',
    )

  def targetItemsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickViewTransitionAttached::targetItemsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewtransitionattached.html
    """
    #  void QQuickViewTransitionAttached::targetItemsChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickViewTransitionAttached18targetItemsChangedEv',
    )

  @staticmethod
  def qmlAttachedProperties(*__, **_) -> Never:
    """
    Qt's 'QQuickViewTransitionAttached
    *QQuickViewTransitionAttached::qmlAttachedProperties(QObject *a0)': leans
    on 'vtable for QQuickViewTransitionAttached', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickViewTransitionAttached.qmlAttachedProperties' has no cute "
        "function yet. Qt's 'QQuickViewTransitionAttached "
        "*QQuickViewTransitionAttached::qmlAttachedProperties(QObject "
        "*a0)': leans on 'vtable for QQuickViewTransitionAttached', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def targetIndexes(*__, **_) -> Never:
    """
    Qt's 'QList<int> QQuickViewTransitionAttached::targetIndexes() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickViewTransitionAttached.targetIndexes' has no cute function "
        "yet. Qt's 'QList<int> "
        "QQuickViewTransitionAttached::targetIndexes() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def targetItems(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject>
    QQuickViewTransitionAttached::targetItems()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQuickViewTransitionAttached.targetItems' has no cute function "
        "yet. Qt's 'QQmlListProperty<QObject> "
        "QQuickViewTransitionAttached::targetItems()': gives a type Python "
        "has no way to take yet.")

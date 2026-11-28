"""
QQuickEnterKeyAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickEnterKeyAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuickEnterKeyAttached(QObject):
  """
  The cute side of Qt's QQuickEnterKeyAttached: a plain Python object
  standing in front of one C++ QQuickEnterKeyAttached.

  It is built on the cute 'QObject', as Qt's QQuickEnterKeyAttached is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickEnterKeyAttached that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'type',
  'typeChanged'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickEnterKeyAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickEnterKeyAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickEnterKeyAttached::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'void QQuickEnterKeyAttached::qt_qmlMarker_attached()': one of Qt's
    own inner workings.

  What has no ritual
  ------------------

  6 of the 13 functions Qt declares: 4 leans on 'QQuickEnterKeyAttached; 2
  not a gap.

  What to expect
  --------------

  - The C++ QQuickEnterKeyAttached is created at the first use, not by
    'QQuickEnterKeyAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickEnterKeyAttached.
  - Qt tells when it has removed the C++ QQuickEnterKeyAttached. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickEnterKeyAttached that has no cute function yet,
    '__init__', 'qmlAttachedProperties', 'setType', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickEnterKeyAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickEnterKeyAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickenterkeyattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickEnterKeyAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickEnterKeyAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> Qt.EnterKeyType:
    """
    Calls Qt's 'Qt::EnterKeyType QQuickEnterKeyAttached::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickenterkeyattached.html#type

    Returns
    -------

    Qt.EnterKeyType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.EnterKeyType(number)'
      gives.
    """
    #  Qt::EnterKeyType QQuickEnterKeyAttached::type() const
    return Qt.EnterKeyType(self.uglySide.call(
        'ritual_ZNK22QQuickEnterKeyAttached4typeEv',
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
    Qt's 'QQuickEnterKeyAttached::QQuickEnterKeyAttached(QObject *parent)':
    leans on 'QQuickEnterKeyAttached::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickEnterKeyAttached.__init__' has no cute function yet. Qt's "
        "'QQuickEnterKeyAttached::QQuickEnterKeyAttached(QObject *parent)': "
        "leans on 'QQuickEnterKeyAttached::staticMetaObject', which Qt's "
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

  def typeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEnterKeyAttached::typeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickenterkeyattached.html#typeChanged
    """
    #  void QQuickEnterKeyAttached::typeChanged()
    self.uglySide.call('ritual_ZN22QQuickEnterKeyAttached11typeChangedEv')

  @staticmethod
  def qmlAttachedProperties(*__, **_) -> Never:
    """
    Qt's 'QQuickEnterKeyAttached
    *QQuickEnterKeyAttached::qmlAttachedProperties(QObject *a0)': leans on
    'QQuickEnterKeyAttached::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickEnterKeyAttached.qmlAttachedProperties' has no cute "
        "function yet. Qt's 'QQuickEnterKeyAttached "
        "*QQuickEnterKeyAttached::qmlAttachedProperties(QObject *a0)': "
        "leans on 'QQuickEnterKeyAttached::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setType(*__, **_) -> Never:
    """
    Qt's 'void QQuickEnterKeyAttached::setType(Qt::EnterKeyType type)': leans
    on 'QQuickEnterKeyAttached::typeChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickEnterKeyAttached.setType' has no cute function yet. Qt's "
        "'void QQuickEnterKeyAttached::setType(Qt::EnterKeyType type)': "
        "leans on 'QQuickEnterKeyAttached::typeChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

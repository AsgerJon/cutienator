"""
QQuickLayoutMirroringAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickLayoutMirroringAttached to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuickLayoutMirroringAttached(QObject):
  """
  The cute side of Qt's QQuickLayoutMirroringAttached: a plain Python object
  standing in front of one C++ QQuickLayoutMirroringAttached.

  It is built on the cute 'QObject', as Qt's QQuickLayoutMirroringAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickLayoutMirroringAttached that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'enabled',
  'setEnabled', 'resetEnabled', 'childrenInherit', 'enabledChanged',
  'childrenInheritChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLayoutMirroringAttached::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickLayoutMirroringAttached::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickLayoutMirroringAttached::qt_qmlMarker_uncreatable()':
    one of Qt's own inner workings.
  - Qt's 'void QQuickLayoutMirroringAttached::qt_qmlMarker_attached()': one
    of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 17 functions Qt declares: 4 leans on
  'QQuickLayoutMirroringAttached; 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickLayoutMirroringAttached is created at the first use, not by
    'QQuickLayoutMirroringAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLayoutMirroringAttached.
  - Qt tells when it has removed the C++ QQuickLayoutMirroringAttached. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLayoutMirroringAttached that has no cute function
    yet, '__init__', 'qmlAttachedProperties', 'setChildrenInherit', holds a
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
  __qt_class__ = 'QQuickLayoutMirroringAttached'

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
    *QQuickLayoutMirroringAttached::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutmirroringattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLayoutMirroringAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickLayoutMirroringAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutMirroringAttached::enabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutmirroringattached.html#enabled
    """
    #  bool QQuickLayoutMirroringAttached::enabled() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickLayoutMirroringAttached7enabledEv',
    )

  def childrenInherit(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutMirroringAttached::childrenInherit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutmirroringattached.html#childrenInherit
    """
    #  bool QQuickLayoutMirroringAttached::childrenInherit() const
    return self.uglySide.call(
        'ritual_ZNK29QQuickLayoutMirroringAttached15childrenInheritEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickLayoutMirroringAttached::setEnabled(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutmirroringattached.html#setEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickLayoutMirroringAttached::setEnabled(bool a0)
    self.uglySide.call(
        'ritual_ZN29QQuickLayoutMirroringAttached10setEnabledEb', a0,
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
    Qt's
    'QQuickLayoutMirroringAttached::QQuickLayoutMirroringAttached(QObject
    *parent)': leans on 'QQuickLayoutMirroringAttached::staticMetaObject',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLayoutMirroringAttached.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickLayoutMirroringAttached::QQuickLayoutMirroringAttached(QObje"
        "ct *parent)': leans on "
        "'QQuickLayoutMirroringAttached::staticMetaObject', which Qt's "
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

  def resetEnabled(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutMirroringAttached::resetEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutmirroringattached.html#resetEnabled
    """
    #  void QQuickLayoutMirroringAttached::resetEnabled()
    self.uglySide.call(
        'ritual_ZN29QQuickLayoutMirroringAttached12resetEnabledEv',
    )

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutMirroringAttached::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutmirroringattached.html#enabledChanged
    """
    #  void QQuickLayoutMirroringAttached::enabledChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickLayoutMirroringAttached14enabledChangedEv',
    )

  def childrenInheritChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickLayoutMirroringAttached::childrenInheritChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutmirroringattached.html
    """
    #  void QQuickLayoutMirroringAttached::childrenInheritChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickLayoutMirroringAttached22childrenInheritChangedEv',
    )

  @staticmethod
  def qmlAttachedProperties(*__, **_) -> Never:
    """
    Qt's 'QQuickLayoutMirroringAttached
    *QQuickLayoutMirroringAttached::qmlAttachedProperties(QObject *a0)':
    leans on 'QQuickLayoutMirroringAttached::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLayoutMirroringAttached.qmlAttachedProperties' has no cute "
        "function yet. Qt's 'QQuickLayoutMirroringAttached "
        "*QQuickLayoutMirroringAttached::qmlAttachedProperties(QObject "
        "*a0)': leans on 'QQuickLayoutMirroringAttached::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setChildrenInherit(*__, **_) -> Never:
    """
    Qt's 'void QQuickLayoutMirroringAttached::setChildrenInherit(bool a0)':
    leans on 'QQuickLayoutMirroringAttached::childrenInheritChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLayoutMirroringAttached.setChildrenInherit' has no cute "
        "function yet. Qt's 'void "
        "QQuickLayoutMirroringAttached::setChildrenInherit(bool a0)': leans "
        "on 'QQuickLayoutMirroringAttached::childrenInheritChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

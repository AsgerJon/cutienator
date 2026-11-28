"""
QQuickPathViewAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpathview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickPathViewAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant
  from . import QQuickPathView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QVariant = WAIT['QVariant']


class QQuickPathViewAttached(QObject):
  """
  The cute side of Qt's QQuickPathViewAttached: a plain Python object
  standing in front of one C++ QQuickPathViewAttached.

  It is built on the cute 'QObject', as Qt's QQuickPathViewAttached is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPathViewAttached that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'view',
  'isCurrentItem', 'value', 'setValue', 'isOnPath', 'currentItemChanged',
  'pathChanged'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPathViewAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickPathViewAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPathViewAttached::~QQuickPathViewAttached()': the destructor:
    Python never removes a C++ QQuickPathViewAttached.

  What has no ritual
  ------------------

  6 of the 17 functions Qt declares: 3 leans on 'QQuickPathViewAttached; 2
  not a gap; 1 Qt's library has no name for it, and its code in Qt's source
  does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickPathViewAttached is created at the first use, not by
    'QQuickPathViewAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathViewAttached.
  - Qt tells when it has removed the C++ QQuickPathViewAttached. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickPathViewAttached that has no cute function yet,
    '__init__', 'setIsCurrentItem', 'setOnPath', holds a function that raises
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
  __qt_class__ = 'QQuickPathViewAttached'

  #  A C++ QQuickPathViewAttached Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPathViewAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPathViewAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPathViewAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickPathViewAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def view(self) -> Optional[QQuickPathView]:
    """
    Calls Qt's 'QQuickPathView *QQuickPathViewAttached::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathviewattached.html#view

    Returns
    -------

    Optional[QQuickPathView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPathView *QQuickPathViewAttached::view() const
    address = self.uglySide.call('ritual_ZNK22QQuickPathViewAttached4viewEv')
    from . import QQuickPathView
    return QQuickPathView._cuteAt(address)

  def isCurrentItem(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathViewAttached::isCurrentItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewattached.html#isCurrentItem
    """
    #  bool QQuickPathViewAttached::isCurrentItem() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickPathViewAttached13isCurrentItemEv',
    )

  @overload(QByteArray)
  def value(self, name: QByteArray) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickPathViewAttached::value(const QByteArray
    &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathviewattached.html#value

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickPathViewAttached::value(const QByteArray &name) const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickPathViewAttached5valueERK10QByteArray',
        self._valueOf(name),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isOnPath(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathViewAttached::isOnPath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewattached.html#isOnPath
    """
    #  bool QQuickPathViewAttached::isOnPath() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickPathViewAttached8isOnPathEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray, QVariant)
  def setValue(self, name: QByteArray, val: QVariant) -> None:
    """
    Calls Qt's 'void QQuickPathViewAttached::setValue(const QByteArray &name,
    const QVariant &val)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewattached.html#setValue

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickPathViewAttached::setValue(const QByteArray &name, const
    #      QVariant &val)
    self.uglySide.call(
        'ritual_ZN22QQuickPathViewAttached8setValueERK10QByteArrayRK8QVaria'
        'nt',
        self._valueOf(name), self._valueOf(val),
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
    Qt's 'QQuickPathViewAttached::QQuickPathViewAttached(QObject *parent)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'qPathViewAttachedType'.
    """
    raise NotImplementedError(
        "'QQuickPathViewAttached.__init__' has no cute function yet. Qt's "
        "'QQuickPathViewAttached::QQuickPathViewAttached(QObject *parent)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'qPathViewAttachedType'.")

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

  def currentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathViewAttached::currentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewattached.html#currentItemChanged
    """
    #  void QQuickPathViewAttached::currentItemChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickPathViewAttached18currentItemChangedEv',
    )

  def pathChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathViewAttached::pathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathviewattached.html#pathChanged
    """
    #  void QQuickPathViewAttached::pathChanged()
    self.uglySide.call('ritual_ZN22QQuickPathViewAttached11pathChangedEv')

  @staticmethod
  def setIsCurrentItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewAttached::setIsCurrentItem(bool c)': leans on
    'QQuickPathViewAttached::currentItemChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewAttached.setIsCurrentItem' has no cute function "
        "yet. Qt's 'void QQuickPathViewAttached::setIsCurrentItem(bool c)': "
        "leans on 'QQuickPathViewAttached::currentItemChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setOnPath(*__, **_) -> Never:
    """
    Qt's 'void QQuickPathViewAttached::setOnPath(bool on)': leans on
    'QQuickPathViewAttached::pathChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickPathViewAttached.setOnPath' has no cute function yet. Qt's "
        "'void QQuickPathViewAttached::setOnPath(bool on)': leans on "
        "'QQuickPathViewAttached::pathChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

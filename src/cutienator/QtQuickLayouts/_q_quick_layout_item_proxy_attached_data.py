"""
QQuickLayoutItemProxyAttachedData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutitemproxy_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickLayoutItemProxyAttachedData to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickLayoutItemProxy


class QQuickLayoutItemProxyAttachedData(QObject):
  """
  The cute side of Qt's QQuickLayoutItemProxyAttachedData: a plain Python
  object standing in front of one C++ QQuickLayoutItemProxyAttachedData.

  It is built on the cute 'QObject', as Qt's
  QQuickLayoutItemProxyAttachedData is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickLayoutItemProxyAttachedData that has a ritual
  and that Python can call so far, 7 names in all: 'metaObject',
  'getControllingProxy', 'proxyHasControl', 'controlTaken',
  'controlReleased', 'controllingProxyChanged', 'proxiesChanged'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLayoutItemProxyAttachedData::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuickLayoutItemProxyAttachedData::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickLayoutItemProxyAttachedData::qt_qmlMarker_anonymous()':
    one of Qt's own inner workings.
  - Qt's
    'QQuickLayoutItemProxyAttachedData::~QQuickLayoutItemProxyAttachedData(
    )': the destructor: Python never removes a C++
    QQuickLayoutItemProxyAttachedData.
  - Qt's 'QQmlListProperty<QQuickLayoutItemProxy>
    QQuickLayoutItemProxyAttachedData::getProxies()': gives a type Python has
    no way to take yet.

  What has no ritual
  ------------------

  8 of the 20 functions Qt declares: 4 leans on
  'QQuickLayoutItemProxyAttachedData; 2 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickLayoutItemProxyAttachedData is created at the first use,
    not by 'QQuickLayoutItemProxyAttachedData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLayoutItemProxyAttachedData.
  - Qt tells when it has removed the C++ QQuickLayoutItemProxyAttachedData.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLayoutItemProxyAttachedData that has no cute
    function yet, '__init__', 'getProxies', 'registerProxy',
    'releaseControl', 'releaseProxy', 'takeControl', holds a function that
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
  __qt_class__ = 'QQuickLayoutItemProxyAttachedData'

  #  A C++ QQuickLayoutItemProxyAttachedData Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLayoutItemProxyAttachedData'

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
    *QQuickLayoutItemProxyAttachedData::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxyattacheddata.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLayoutItemProxyAttachedData::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QQuickLayoutItemProxyAttachedData10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def getControllingProxy(self) -> Optional[QQuickLayoutItemProxy]:
    """
    Calls Qt's 'QQuickLayoutItemProxy
    *QQuickLayoutItemProxyAttachedData::getControllingProxy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxyattacheddata.html

    Returns
    -------

    Optional[QQuickLayoutItemProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLayoutItemProxy
    #      *QQuickLayoutItemProxyAttachedData::getControllingProxy() const
    address = self.uglySide.call(
        'ritual_ZNK33QQuickLayoutItemProxyAttachedData19getControllingProxy'
        'Ev',
    )
    from . import QQuickLayoutItemProxy
    return QQuickLayoutItemProxy._cuteAt(address)

  def proxyHasControl(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutItemProxyAttachedData::proxyHasControl()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxyattacheddata.html
    """
    #  bool QQuickLayoutItemProxyAttachedData::proxyHasControl() const
    return self.uglySide.call(
        'ritual_ZNK33QQuickLayoutItemProxyAttachedData15proxyHasControlEv',
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
    Qt's
    'QQuickLayoutItemProxyAttachedData::QQuickLayoutItemProxyAttachedData(
    QObject *parent)': leans on
    'QQuickLayoutItemProxyAttachedData::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLayoutItemProxyAttachedData.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickLayoutItemProxyAttachedData::QQuickLayoutItemProxyAttachedDa"
        "ta(QObject *parent)': leans on "
        "'QQuickLayoutItemProxyAttachedData::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def controlTaken(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxyAttachedData::controlTaken()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxyattacheddata.html
    """
    #  void QQuickLayoutItemProxyAttachedData::controlTaken()
    self.uglySide.call(
        'ritual_ZN33QQuickLayoutItemProxyAttachedData12controlTakenEv',
    )

  def controlReleased(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxyAttachedData::controlReleased()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxyattacheddata.html
    """
    #  void QQuickLayoutItemProxyAttachedData::controlReleased()
    self.uglySide.call(
        'ritual_ZN33QQuickLayoutItemProxyAttachedData15controlReleasedEv',
    )

  def controllingProxyChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuickLayoutItemProxyAttachedData::controllingProxyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxyattacheddata.html
    """
    #  void QQuickLayoutItemProxyAttachedData::controllingProxyChanged()
    self.uglySide.call(
        'ritual_ZN33QQuickLayoutItemProxyAttachedData23controllingProxyChan'
        'gedEv',
    )

  def proxiesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLayoutItemProxyAttachedData::proxiesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutitemproxyattacheddata.html
    """
    #  void QQuickLayoutItemProxyAttachedData::proxiesChanged()
    self.uglySide.call(
        'ritual_ZN33QQuickLayoutItemProxyAttachedData14proxiesChangedEv',
    )

  @staticmethod
  def getProxies(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickLayoutItemProxy>
    QQuickLayoutItemProxyAttachedData::getProxies()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickLayoutItemProxyAttachedData.getProxies' has no cute "
        "function yet. Qt's 'QQmlListProperty<QQuickLayoutItemProxy> "
        "QQuickLayoutItemProxyAttachedData::getProxies()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def registerProxy(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickLayoutItemProxyAttachedData::registerProxy(QQuickLayoutItemProxy
    *proxy)': leans on 'QQuickLayoutItemProxyAttachedData::proxiesChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLayoutItemProxyAttachedData.registerProxy' has no cute "
        "function yet. Qt's 'void "
        "QQuickLayoutItemProxyAttachedData::registerProxy(QQuickLayoutItemPr"
        "oxy *proxy)': leans on "
        "'QQuickLayoutItemProxyAttachedData::proxiesChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def releaseControl(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickLayoutItemProxyAttachedData::releaseControl(QQuickLayoutItemProxy
    *proxy)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name 'lcLayouts'; did
    you mean 'QLayout'?.
    """
    raise NotImplementedError(
        "'QQuickLayoutItemProxyAttachedData.releaseControl' has no cute "
        "function yet. Qt's 'void "
        "QQuickLayoutItemProxyAttachedData::releaseControl(QQuickLayoutItemP"
        "roxy *proxy)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: unknown type "
        "name 'lcLayouts'; did you mean 'QLayout'?.")

  @staticmethod
  def releaseProxy(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickLayoutItemProxyAttachedData::releaseProxy(QQuickLayoutItemProxy
    *proxy)': leans on 'QQuickLayoutItemProxyAttachedData::proxiesChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLayoutItemProxyAttachedData.releaseProxy' has no cute "
        "function yet. Qt's 'void "
        "QQuickLayoutItemProxyAttachedData::releaseProxy(QQuickLayoutItemPro"
        "xy *proxy)': leans on "
        "'QQuickLayoutItemProxyAttachedData::proxiesChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def takeControl(*__, **_) -> Never:
    """
    Qt's 'bool
    QQuickLayoutItemProxyAttachedData::takeControl(QQuickLayoutItemProxy
    *proxy)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name 'lcLayouts'; did
    you mean 'QLayout'?.
    """
    raise NotImplementedError(
        "'QQuickLayoutItemProxyAttachedData.takeControl' has no cute "
        "function yet. Qt's 'bool "
        "QQuickLayoutItemProxyAttachedData::takeControl(QQuickLayoutItemProx"
        "y *proxy)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'lcLayouts'; did you mean 'QLayout'?.")

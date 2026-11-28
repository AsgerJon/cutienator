"""
QQStyleKitDelegateContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKitImpl/6.12.0/QtLabsStyleKitImpl/private/qqstylekitdelegatecontainer_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitDelegateContainer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject, QRectF
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']


class QQStyleKitDelegateContainer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQStyleKitDelegateContainer: a plain Python object
  standing in front of one C++ QQStyleKitDelegateContainer.

  What exists
  -----------

  Every function of Qt's QQStyleKitDelegateContainer that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'quickControl',
  'delegateInstance', 'delegateStyleChanged', 'quickControlChanged',
  'delegateInstanceChanged', 'componentComplete', 'geometryChange'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitDelegateContainer::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQStyleKitDelegateContainer::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQStyleKitDelegateContainer::~QQStyleKitDelegateContainer()': the
    destructor: Python never removes a C++ QQStyleKitDelegateContainer.

  What has no ritual
  ------------------

  10 of the 21 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 3 leans on
  'QQStyleKitDelegateContainer; 2 not a gap.

  What to expect
  --------------

  - The C++ QQStyleKitDelegateContainer is created at the first use, not by
    'QQStyleKitDelegateContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitDelegateContainer.
  - Qt tells when it has removed the C++ QQStyleKitDelegateContainer. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitDelegateContainer that has no cute function
    yet, '__init__', 'delegateStyle', 'maybeCreateDelegate',
    'maybeCreateShadow', 'setDelegateStyle', 'setQuickControl',
    'updateImplicitSize', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitDelegateContainer'

  #  A C++ QQStyleKitDelegateContainer Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQStyleKitDelegateContainer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitDelegateContainer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegatecontainer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitDelegateContainer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitDelegateContainer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def quickControl(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQStyleKitDelegateContainer::quickControl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegatecontainer.html#quickControl

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQStyleKitDelegateContainer::quickControl() const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitDelegateContainer12quickControlEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def delegateInstance(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQStyleKitDelegateContainer::delegateInstance()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegatecontainer.html#delegateInstance

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQStyleKitDelegateContainer::delegateInstance() const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitDelegateContainer16delegateInstanceEv',
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

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
    Qt's 'QQStyleKitDelegateContainer::QQStyleKitDelegateContainer(QQuickItem
    *parent)': leans on
    'QQStyleKitDelegateContainer::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDelegateContainer.__init__' has no cute function yet. "
        "Qt's "
        "'QQStyleKitDelegateContainer::QQStyleKitDelegateContainer(QQuickIte"
        "m *parent)': leans on "
        "'QQStyleKitDelegateContainer::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def delegateStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateContainer::delegateStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegatecontainer.html
    """
    #  void QQStyleKitDelegateContainer::delegateStyleChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitDelegateContainer20delegateStyleChangedEv',
    )

  def quickControlChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateContainer::quickControlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegatecontainer.html
    """
    #  void QQStyleKitDelegateContainer::quickControlChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitDelegateContainer19quickControlChangedEv',
    )

  def delegateInstanceChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateContainer::delegateInstanceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegatecontainer.html
    """
    #  void QQStyleKitDelegateContainer::delegateInstanceChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitDelegateContainer23delegateInstanceChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateContainer::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegatecontainer.html#componentComplete
    """
    #  void QQStyleKitDelegateContainer::componentComplete()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitDelegateContainer17componentCompleteEv',
    )

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegateContainer::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegatecontainer.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQStyleKitDelegateContainer::geometryChange(const QRectF
    #      &newGeometry, const QRectF &oldGeometry)
    ritual = (
        'ritual_ZN27QQStyleKitDelegateContainer14geometryChangeERK6QRectFS2'
        '_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQStyleKitDelegateContainer14geometryChangeERK6QR'
          'ectFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @staticmethod
  def delegateStyle(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitDelegateProperties
    *QQStyleKitDelegateContainer::delegateStyle() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: static_cast from 'QObject *' to 'QQStyleKitDelegateProperties *',
    which are not related by inheritance, is not allowed.
    """
    raise NotImplementedError(
        "'QQStyleKitDelegateContainer.delegateStyle' has no cute function "
        "yet. Qt's 'QQStyleKitDelegateProperties "
        "*QQStyleKitDelegateContainer::delegateStyle() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: static_cast from 'QObject *' to "
        "'QQStyleKitDelegateProperties *', which are not related by "
        "inheritance, is not allowed.")

  @staticmethod
  def maybeCreateDelegate(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitDelegateContainer::maybeCreateDelegate()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQStyleKitDelegateProperties'.
    """
    raise NotImplementedError(
        "'QQStyleKitDelegateContainer.maybeCreateDelegate' has no cute "
        "function yet. Qt's 'void "
        "QQStyleKitDelegateContainer::maybeCreateDelegate()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QQStyleKitDelegateProperties'.")

  @staticmethod
  def maybeCreateShadow(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitDelegateContainer::maybeCreateShadow()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQStyleKitDelegateProperties'.
    """
    raise NotImplementedError(
        "'QQStyleKitDelegateContainer.maybeCreateShadow' has no cute "
        "function yet. Qt's 'void "
        "QQStyleKitDelegateContainer::maybeCreateShadow()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QQStyleKitDelegateProperties'.")

  @staticmethod
  def setDelegateStyle(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitDelegateContainer::setDelegateStyle(
    QQStyleKitDelegateProperties *delegateProperties)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: static_cast from 'QQStyleKitDelegateProperties *' to 'QObjectType
    *' (aka 'QObject *'), which are not related by inheritance, is not
    allowed.
    """
    raise NotImplementedError(
        "'QQStyleKitDelegateContainer.setDelegateStyle' has no cute "
        "function yet. Qt's 'void "
        "QQStyleKitDelegateContainer::setDelegateStyle(QQStyleKitDelegatePro"
        "perties *delegateProperties)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "static_cast from 'QQStyleKitDelegateProperties *' to 'QObjectType "
        "*' (aka 'QObject *'), which are not related by inheritance, is not "
        "allowed.")

  @staticmethod
  def setQuickControl(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitDelegateContainer::setQuickControl(QObject
    *control)': leans on
    'QQStyleKitDelegateContainer::quickControlChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDelegateContainer.setQuickControl' has no cute function "
        "yet. Qt's 'void "
        "QQStyleKitDelegateContainer::setQuickControl(QObject *control)': "
        "leans on 'QQStyleKitDelegateContainer::quickControlChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def updateImplicitSize(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitDelegateContainer::updateImplicitSize()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQStyleKitDelegateProperties'.
    """
    raise NotImplementedError(
        "'QQStyleKitDelegateContainer.updateImplicitSize' has no cute "
        "function yet. Qt's 'void "
        "QQStyleKitDelegateContainer::updateImplicitSize()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QQStyleKitDelegateProperties'.")

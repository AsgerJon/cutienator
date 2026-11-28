"""
QQStyleKitDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitdelegate_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitDelegate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQStyleKitDelegateProperties


class QQStyleKitDelegate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQStyleKitDelegate: a plain Python object standing in
  front of one C++ QQStyleKitDelegate.

  What exists
  -----------

  Every function of Qt's QQStyleKitDelegate that has a ritual and that Python
  can call so far, 4 names in all: 'metaObject', 'delegateStyle',
  'delegateStyleChanged', 'updateImplicitSize'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitDelegate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQStyleKitDelegate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  8 of the 14 functions Qt declares: 5 leans on 'QQStyleKitDelegate; 2 not a
  gap; 1 leans on 'vtable for QQStyleKitDelegate', which Qt's source does not
  mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQStyleKitDelegate is created at the first use, not by
    'QQStyleKitDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitDelegate.
  - Qt tells when it has removed the C++ QQStyleKitDelegate. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitDelegate that has no cute function yet,
    '__init__', 'maybeCreateColor', 'maybeCreateGradient',
    'maybeCreateImage', 'setDelegateStyle', holds a function that raises
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
  __qt_class__ = 'QQStyleKitDelegate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitDelegate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitdelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQStyleKitDelegate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def delegateStyle(self) -> Optional[QQStyleKitDelegateProperties]:
    """
    Calls Qt's 'QQStyleKitDelegateProperties
    *QQStyleKitDelegate::delegateStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegate.html#delegateStyle

    Returns
    -------

    Optional[QQStyleKitDelegateProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitDelegateProperties *QQStyleKitDelegate::delegateStyle()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QQStyleKitDelegate13delegateStyleEv',
    )
    from . import QQStyleKitDelegateProperties
    return QQStyleKitDelegateProperties._cuteAt(address)

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
    Qt's 'QQStyleKitDelegate::QQStyleKitDelegate(QQuickItem *parent)': leans
    on 'vtable for QQStyleKitDelegate', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDelegate.__init__' has no cute function yet. Qt's "
        "'QQStyleKitDelegate::QQStyleKitDelegate(QQuickItem *parent)': "
        "leans on 'vtable for QQStyleKitDelegate', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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
    Calls Qt's 'void QQStyleKitDelegate::delegateStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegate.html#delegateStyleChanged
    """
    #  void QQStyleKitDelegate::delegateStyleChanged()
    self.uglySide.call(
        'ritual_ZN18QQStyleKitDelegate20delegateStyleChangedEv',
    )

  def updateImplicitSize(self) -> None:
    """
    Calls Qt's 'void QQStyleKitDelegate::updateImplicitSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitdelegate.html#updateImplicitSize
    """
    #  void QQStyleKitDelegate::updateImplicitSize()
    self.uglySide.call('ritual_ZN18QQStyleKitDelegate18updateImplicitSizeEv')

  @staticmethod
  def maybeCreateColor(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitDelegate::maybeCreateColor()': leans on
    'QQStyleKitDelegate::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDelegate.maybeCreateColor' has no cute function yet. "
        "Qt's 'void QQStyleKitDelegate::maybeCreateColor()': leans on "
        "'QQStyleKitDelegate::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def maybeCreateGradient(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitDelegate::maybeCreateGradient()': leans on
    'QQStyleKitDelegate::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDelegate.maybeCreateGradient' has no cute function yet. "
        "Qt's 'void QQStyleKitDelegate::maybeCreateGradient()': leans on "
        "'QQStyleKitDelegate::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def maybeCreateImage(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitDelegate::maybeCreateImage()': leans on
    'QQStyleKitDelegate::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDelegate.maybeCreateImage' has no cute function yet. "
        "Qt's 'void QQStyleKitDelegate::maybeCreateImage()': leans on "
        "'QQStyleKitDelegate::staticMetaObject', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setDelegateStyle(*__, **_) -> Never:
    """
    Qt's 'void
    QQStyleKitDelegate::setDelegateStyle(QQStyleKitDelegateProperties
    *delegateStyle)': leans on 'QQStyleKitDelegate::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitDelegate.setDelegateStyle' has no cute function yet. "
        "Qt's 'void "
        "QQStyleKitDelegate::setDelegateStyle(QQStyleKitDelegateProperties "
        "*delegateStyle)': leans on 'QQStyleKitDelegate::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

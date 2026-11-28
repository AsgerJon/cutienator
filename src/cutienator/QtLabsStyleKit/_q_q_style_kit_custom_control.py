"""
QQStyleKitCustomControl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcustomcontrol_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitCustomControl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QQStyleKitControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQStyleKitCustomControl(QQStyleKitControl):
  """
  The cute side of Qt's QQStyleKitCustomControl: a plain Python object
  standing in front of one C++ QQStyleKitCustomControl.

  It is built on the cute 'QQStyleKitControl', as Qt's
  QQStyleKitCustomControl is built on Qt's QQStyleKitControl, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitCustomControl that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'controlType',
  'controlTypeChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitCustomControl::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQStyleKitCustomControl::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  7 of the 12 functions Qt declares: 2 not a gap; 2 forbidden; 2 leans on
  'QQStyleKitCustomControl; 1 leans on 'vtable for QQStyleKitCustomControl',
  which Qt's source does not mark for use from outside Qt and has no code for
  that could be taken.

  What to expect
  --------------

  - The C++ QQStyleKitCustomControl is created at the first use, not by
    'QQStyleKitCustomControl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitCustomControl.
  - Qt tells when it has removed the C++ QQStyleKitCustomControl. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitCustomControl that has no cute function yet,
    '__init__', 'setControlType', holds a function that raises
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
  __qt_class__ = 'QQStyleKitCustomControl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitCustomControl::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcustomcontrol.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitCustomControl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQStyleKitCustomControl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def controlType(self) -> int:
    """
    Calls Qt's 'int QQStyleKitCustomControl::controlType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcustomcontrol.html#controlType
    """
    #  int QQStyleKitCustomControl::controlType() const
    return self.uglySide.call(
        'ritual_ZNK23QQStyleKitCustomControl11controlTypeEv',
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
    Qt's 'QQStyleKitCustomControl::QQStyleKitCustomControl(QObject *parent)':
    leans on 'vtable for QQStyleKitCustomControl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitCustomControl.__init__' has no cute function yet. Qt's "
        "'QQStyleKitCustomControl::QQStyleKitCustomControl(QObject "
        "*parent)': leans on 'vtable for QQStyleKitCustomControl', which "
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

  def controlTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitCustomControl::controlTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcustomcontrol.html#controlTypeChanged
    """
    #  void QQStyleKitCustomControl::controlTypeChanged()
    self.uglySide.call(
        'ritual_ZN23QQStyleKitCustomControl18controlTypeChangedEv',
    )

  @staticmethod
  def setControlType(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitCustomControl::setControlType(int controlType)':
    leans on 'QQStyleKitCustomControl::controlTypeChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitCustomControl.setControlType' has no cute function yet. "
        "Qt's 'void QQStyleKitCustomControl::setControlType(int "
        "controlType)': leans on "
        "'QQStyleKitCustomControl::controlTypeChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

"""
QQStyleKitVariationAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitvariation_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitVariationAttached to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQStyleKitVariationAttached(QObject):
  """
  The cute side of Qt's QQStyleKitVariationAttached: a plain Python object
  standing in front of one C++ QQStyleKitVariationAttached.

  It is built on the cute 'QObject', as Qt's QQStyleKitVariationAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitVariationAttached that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'variations',
  'controlType', 'variationsChanged', 'controlTypeChanged'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitVariationAttached::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQStyleKitVariationAttached::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 13 functions Qt declares: 3 leans on 'QQStyleKitVariationAttached;
  2 not a gap; 1 leans on 'vtable for QQStyleKitVariationAttached', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QQStyleKitVariationAttached is created at the first use, not by
    'QQStyleKitVariationAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitVariationAttached.
  - Qt tells when it has removed the C++ QQStyleKitVariationAttached. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitVariationAttached that has no cute function
    yet, '__init__', 'setControlType', 'setVariations', holds a function that
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
  __qt_class__ = 'QQStyleKitVariationAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitVariationAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitvariationattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitVariationAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitVariationAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def variations(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQStyleKitVariationAttached::variations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitvariationattached.html#variations

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQStyleKitVariationAttached::variations() const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitVariationAttached10variationsEv',
    )
    return QStringList._cuteOwning(address)

  def controlType(self) -> int:
    """
    Calls Qt's 'QQStyleKitExtendableControlType
    QQStyleKitVariationAttached::controlType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitvariationattached.html#controlType
    """
    #  QQStyleKitExtendableControlType
    #      QQStyleKitVariationAttached::controlType() const
    return self.uglySide.call(
        'ritual_ZNK27QQStyleKitVariationAttached11controlTypeEv',
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
    Qt's 'QQStyleKitVariationAttached::QQStyleKitVariationAttached(QObject
    *parent)': leans on 'vtable for QQStyleKitVariationAttached', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitVariationAttached.__init__' has no cute function yet. "
        "Qt's "
        "'QQStyleKitVariationAttached::QQStyleKitVariationAttached(QObject "
        "*parent)': leans on 'vtable for QQStyleKitVariationAttached', "
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

  def variationsChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitVariationAttached::variationsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitvariationattached.html#variationsChanged
    """
    #  void QQStyleKitVariationAttached::variationsChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitVariationAttached17variationsChangedEv',
    )

  def controlTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitVariationAttached::controlTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitvariationattached.html
    """
    #  void QQStyleKitVariationAttached::controlTypeChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitVariationAttached18controlTypeChangedEv',
    )

  @staticmethod
  def setControlType(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitVariationAttached::setControlType(
    QQStyleKitExtendableControlType type)': leans on
    'QQStyleKitVariationAttached::controlTypeChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitVariationAttached.setControlType' has no cute function "
        "yet. Qt's 'void "
        "QQStyleKitVariationAttached::setControlType(QQStyleKitExtendableCon"
        "trolType type)': leans on "
        "'QQStyleKitVariationAttached::controlTypeChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setVariations(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitVariationAttached::setVariations(const QStringList
    &variations)': leans on
    'QQStyleKitVariationAttached::variationsChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQStyleKitVariationAttached.setVariations' has no cute function "
        "yet. Qt's 'void QQStyleKitVariationAttached::setVariations(const "
        "QStringList &variations)': leans on "
        "'QQStyleKitVariationAttached::variationsChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

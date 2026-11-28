"""
QQStyleKitControl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrol_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitControl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQStyleKitControlState

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QQStyleKitControl(QQStyleKitControlState):
  """
  The cute side of Qt's QQStyleKitControl: a plain Python object standing in
  front of one C++ QQStyleKitControl.

  It is built on the cute 'QQStyleKitControlState', as Qt's QQStyleKitControl
  is built on Qt's QQStyleKitControlState, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitControl that has a ritual and that Python
  can call so far, 3 names in all: 'metaObject', 'readStyleProperty',
  'writeStyleProperty'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitControl::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQStyleKitControl::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  9 of the 14 functions Qt declares: 2 not a gap; 2 forbidden; 2 leans on
  'QQStyleKitControls; 1 leans on 'QQStyleKitControl; 1 leans on 'vtable for
  QQStyleKitControl', which Qt's source does not mark for use from outside Qt
  and has no code for that could be taken; 1 leans on 'QQStyleKitDebug.

  What to expect
  --------------

  - The C++ QQStyleKitControl is created at the first use, not by
    'QQStyleKitControl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitControl.
  - Qt tells when it has removed the C++ QQStyleKitControl. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitControl that has no cute function yet,
    '__init__', 'controlType', 'controls', 'variations', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitControl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitControl::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitcontrol.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitControl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQStyleKitControl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def readStyleProperty(self, key: int) -> QVariant:
    """
    Calls Qt's 'QVariant
    QQStyleKitControl::readStyleProperty(PropertyStorageId key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrol.html#readStyleProperty

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQStyleKitControl::readStyleProperty(PropertyStorageId key)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QQStyleKitControl17readStylePropertyEj', key,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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
    Qt's 'QQStyleKitControl::QQStyleKitControl(QObject *parent)': leans on
    'vtable for QQStyleKitControl', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControl.__init__' has no cute function yet. Qt's "
        "'QQStyleKitControl::QQStyleKitControl(QObject *parent)': leans on "
        "'vtable for QQStyleKitControl', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  @overload(int, QVariant)
  def writeStyleProperty(self, key: int, value: QVariant) -> None:
    """
    Calls Qt's 'void QQStyleKitControl::writeStyleProperty(PropertyStorageId
    key, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrol.html#writeStyleProperty

    Parameters
    ----------

    key : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQStyleKitControl::writeStyleProperty(PropertyStorageId key,
    #      const QVariant &value)
    self.uglySide.call(
        'ritual_ZN17QQStyleKitControl18writeStylePropertyEjRK8QVariant',
        key, self._valueOf(value),
    )

  @staticmethod
  def controlType(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitExtendableControlType QQStyleKitControl::controlType()
    const': leans on 'QQStyleKitControls::staticMetaObject', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControl.controlType' has no cute function yet. Qt's "
        "'QQStyleKitExtendableControlType QQStyleKitControl::controlType() "
        "const': leans on 'QQStyleKitControls::staticMetaObject', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def controls(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControls *QQStyleKitControl::controls() const': leans on
    'QQStyleKitControls::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControl.controls' has no cute function yet. Qt's "
        "'QQStyleKitControls *QQStyleKitControl::controls() const': leans "
        "on 'QQStyleKitControls::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def variations(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQStyleKitVariation>
    QQStyleKitControl::variations()': leans on
    'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitControl.variations' has no cute function yet. Qt's "
        "'QQmlListProperty<QQStyleKitVariation> "
        "QQStyleKitControl::variations()': leans on "
        "'QQStyleKitDebug::groupBeingRead', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

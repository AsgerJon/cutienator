"""
QQStyleKitVariation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitvariation_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitVariation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQStyleKitControls

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQStyleKitStyle
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQStyleKitStyle = WAIT['QQStyleKitStyle']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQStyleKitVariation(QQStyleKitControls):
  """
  The cute side of Qt's QQStyleKitVariation: a plain Python object standing
  in front of one C++ QQStyleKitVariation.

  It is built on the cute 'QQStyleKitControls', as Qt's QQStyleKitVariation
  is built on Qt's QQStyleKitControls, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitVariation that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'componentComplete',
  'name', 'nameChanged', 'resetVariationsForStyle'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitVariation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQStyleKitVariation::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQStyleKitVariation::qt_qmlMarker_attached()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  8 of the 16 functions Qt declares: 2 not a gap; 2 forbidden; 2 leans on
  'QQStyleKitVariation; 1 leans on 'vtable for QQStyleKitVariation', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken; 1 leans on 'vtable for QQStyleKitVariationAttached', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QQStyleKitVariation is created at the first use, not by
    'QQStyleKitVariation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitVariation.
  - Qt tells when it has removed the C++ QQStyleKitVariation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitVariation that has no cute function yet,
    '__init__', 'qmlAttachedProperties', 'setName', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQStyleKitStyle)
  @overload(NoneType)
  def resetVariationsForStyle(style: Optional[QQStyleKitStyle]) -> None:
    """
    Calls Qt's 'void
    QQStyleKitVariation::resetVariationsForStyle(QQStyleKitStyle *style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitvariation.html#resetVariationsForStyle

    Parameters
    ----------

    style : Optional[QQStyleKitStyle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitVariation::resetVariationsForStyle(QQStyleKitStyle
    #      *style)
    Rituals.call(
        'ritual_ZN19QQStyleKitVariation23resetVariationsForStyleEP15QQStyle'
        'KitStyle',
        CuteMixin._addressOf(style),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitVariation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitVariation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitvariation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitVariation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQStyleKitVariation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQStyleKitVariation::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekitvariation.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQStyleKitVariation::name() const
    return self.uglySide.call('ritual_ZNK19QQStyleKitVariation4nameEv')

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
    Qt's 'QQStyleKitVariation::QQStyleKitVariation(QObject *parent)': leans
    on 'vtable for QQStyleKitVariation', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitVariation.__init__' has no cute function yet. Qt's "
        "'QQStyleKitVariation::QQStyleKitVariation(QObject *parent)': leans "
        "on 'vtable for QQStyleKitVariation', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQStyleKitVariation::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitvariation.html#componentComplete
    """
    #  void QQStyleKitVariation::componentComplete()
    self.uglySide.call('ritual_ZN19QQStyleKitVariation17componentCompleteEv')

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitVariation::nameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitvariation.html#nameChanged
    """
    #  void QQStyleKitVariation::nameChanged()
    self.uglySide.call('ritual_ZN19QQStyleKitVariation11nameChangedEv')

  @staticmethod
  def qmlAttachedProperties(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitVariationAttached
    *QQStyleKitVariation::qmlAttachedProperties(QObject *object)': leans on
    'vtable for QQStyleKitVariationAttached', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitVariation.qmlAttachedProperties' has no cute function "
        "yet. Qt's 'QQStyleKitVariationAttached "
        "*QQStyleKitVariation::qmlAttachedProperties(QObject *object)': "
        "leans on 'vtable for QQStyleKitVariationAttached', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setName(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitVariation::setName(const QString &name)': leans on
    'QQStyleKitVariation::nameChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitVariation.setName' has no cute function yet. Qt's 'void "
        "QQStyleKitVariation::setName(const QString &name)': leans on "
        "'QQStyleKitVariation::nameChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

"""
AbstractRenderItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/abstractrenderitem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means AbstractRenderItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QQuaternion, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']


class AbstractRenderItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's AbstractRenderItem: a plain Python object standing in
  front of one C++ AbstractRenderItem.

  C++ hands a AbstractRenderItem around as a copy, so every C++
  AbstractRenderItem behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's AbstractRenderItem that has a ritual and that Python
  can call so far, 4 names in all: 'setTranslation', 'translation',
  'rotation', 'setRotation'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'AbstractRenderItem &AbstractRenderItem::operator=(const
    AbstractRenderItem &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'AbstractRenderItem::~AbstractRenderItem()': the destructor: Python
    removes its C++ AbstractRenderItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ AbstractRenderItem is created at the first use, not by
    'AbstractRenderItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a AbstractRenderItem back gives a copy the ritual made
    for Python, in a new cute AbstractRenderItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'AbstractRenderItem'

  #  Qt's '~AbstractRenderItem()'. Naming it makes this a value class: Python
  #  owns every C++ AbstractRenderItem behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18AbstractRenderItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def translation(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &AbstractRenderItem::translation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractrenderitem.html#translation

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &AbstractRenderItem::translation() const
    address = self.uglySide.call(
        'ritual_ZNK18AbstractRenderItem11translationEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def rotation(self) -> QQuaternion:
    """
    Calls Qt's 'const QQuaternion &AbstractRenderItem::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/abstractrenderitem.html#rotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  const QQuaternion &AbstractRenderItem::rotation() const
    address = self.uglySide.call('ritual_ZNK18AbstractRenderItem8rotationEv')
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setTranslation(self, translation: QVector3D) -> None:
    """
    Calls Qt's 'void AbstractRenderItem::setTranslation(const QVector3D
    &translation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractrenderitem.html#setTranslation

    Parameters
    ----------

    translation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void AbstractRenderItem::setTranslation(const QVector3D &translation)
    self.uglySide.call(
        'ritual_ZN18AbstractRenderItem14setTranslationERK9QVector3D',
        self._valueOf(translation),
    )

  @overload(QQuaternion)
  def setRotation(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void AbstractRenderItem::setRotation(const QQuaternion
    &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractrenderitem.html#setRotation

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void AbstractRenderItem::setRotation(const QQuaternion &rotation)
    self.uglySide.call(
        'ritual_ZN18AbstractRenderItem11setRotationERK11QQuaternion',
        self._valueOf(rotation),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'AbstractRenderItem::AbstractRenderItem()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractrenderitem.html#AbstractRenderItem
    """
    #  AbstractRenderItem::AbstractRenderItem()
    self._noteCreation(AbstractRenderItem, lambda: Rituals.call(
        'ritual_ZN18AbstractRenderItemC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: AbstractRenderItem) -> None:
    """
    Notes what was given, for Qt's
    'AbstractRenderItem::AbstractRenderItem(const AbstractRenderItem
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/abstractrenderitem.html#AbstractRenderItem

    Parameters
    ----------

    other : AbstractRenderItem
      Passed on as a value: Qt reads the C++ AbstractRenderItem, which stays
      Python's own.
    """
    #  AbstractRenderItem::AbstractRenderItem(const AbstractRenderItem
    #      &other)
    self._noteCreation(AbstractRenderItem, lambda: Rituals.call(
        'ritual_ZN18AbstractRenderItemC1ERKS_', self._valueOf(other),
    ))

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

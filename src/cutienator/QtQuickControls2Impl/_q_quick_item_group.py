"""
QQuickItemGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickitemgroup_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickItemGroup to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickImplicitSizeItem, QQuickItem
from ..QtQuick import QQuickItemChangeListener

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF, QSizeF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemGroup(QQuickImplicitSizeItem, QQuickItemChangeListener):
  """
  The cute side of Qt's QQuickItemGroup: a plain Python object standing in
  front of one C++ QQuickItemGroup.

  It is built on the cute 'QQuickImplicitSizeItem', as Qt's QQuickItemGroup
  is built on Qt's QQuickImplicitSizeItem, and has everything that class has.
  It is built on the cute 'QQuickItemChangeListener' as well, as Qt's
  QQuickItemGroup is built on Qt's QQuickItemChangeListener too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickItemGroup that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'watch', 'unwatch',
  'calculateImplicitSize', 'updateImplicitSize', 'itemChange',
  'geometryChange', 'itemImplicitWidthChanged', 'itemImplicitHeightChanged'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickItemGroup::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickItemGroup::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickItemGroup::~QQuickItemGroup()': the destructor: Python never
    removes a C++ QQuickItemGroup.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickItemGroup is created at the first use, not by
    'QQuickItemGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickItemGroup.
  - Qt tells when it has removed the C++ QQuickItemGroup. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickItemGroup::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemgroup.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickItemGroup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickItemGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemGroup'

  #  Qt's QQuickItemGroup is built on more than one class. The part of a C++
  #  QQuickItemGroup that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickItemChangeListener':
          'ritual_cast_QQuickItemGroup_QQuickItemChangeListener',
  }

  #  A C++ QQuickItemGroup Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickItemGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickItemGroup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemgroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickItemGroup::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickItemGroup10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def calculateImplicitSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickItemGroup::calculateImplicitSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemgroup.html#calculateImplicitSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickItemGroup::calculateImplicitSize() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickItemGroup21calculateImplicitSizeEv',
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

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

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickItemGroup::QQuickItemGroup(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemgroup.html#QQuickItemGroup

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickItemGroup::QQuickItemGroup(QQuickItem *parent)
    self._noteCreation(QQuickItemGroup, lambda: Rituals.call(
        'ritual_ZN15QQuickItemGroupC1EP10QQuickItem',
        self._addressOf(parent),
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

  @overload(QQuickItem)
  @overload(NoneType)
  def watch(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemGroup::watch(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemgroup.html#watch

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemGroup::watch(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN15QQuickItemGroup5watchEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def unwatch(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemGroup::unwatch(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemgroup.html#unwatch

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemGroup::unwatch(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN15QQuickItemGroup7unwatchEP10QQuickItem',
        self._addressOf(item),
    )

  def updateImplicitSize(self) -> None:
    """
    Calls Qt's 'void QQuickItemGroup::updateImplicitSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemgroup.html#updateImplicitSize
    """
    #  void QQuickItemGroup::updateImplicitSize()
    self.uglySide.call('ritual_ZN15QQuickItemGroup18updateImplicitSizeEv')

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickItemGroup::itemChange(ItemChange change, const
    ItemChangeData &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemgroup.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickItemGroup::itemChange(ItemChange change, const
    #      ItemChangeData &data)
    ritual = (
        'ritual_ZN15QQuickItemGroup10itemChangeEN10QQuickItem10ItemChangeER'
        'KNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickItemGroup10itemChangeEN10QQuickItem10ItemCh'
          'angeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickItemGroup::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemgroup.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickItemGroup::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickItemGroup14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickItemGroup14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemGroup::itemImplicitWidthChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemgroup.html#itemImplicitWidthChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemGroup::itemImplicitWidthChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN15QQuickItemGroup24itemImplicitWidthChangedEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickItemGroup24itemImplicitWidthChangedEP10QQui'
          'ckItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickItemGroup::itemImplicitHeightChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemgroup.html#itemImplicitHeightChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemGroup::itemImplicitHeightChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN15QQuickItemGroup25itemImplicitHeightChangedEP10QQuickIte'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickItemGroup25itemImplicitHeightChangedEP10QQu'
          'ickItem')
    self.uglySide.call(ritual, self._addressOf(item))

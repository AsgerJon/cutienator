"""
QQuickUniversalBusyIndicator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2UniversalStyleImpl/6.12.0/QtQuickControls2UniversalStyleImpl/private/qquickuniversalbusyindicator_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickUniversalBusyIndicator to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
  from ..QtQuick import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickUniversalBusyIndicator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickUniversalBusyIndicator: a plain Python object
  standing in front of one C++ QQuickUniversalBusyIndicator.

  What exists
  -----------

  Every function of Qt's QQuickUniversalBusyIndicator that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'count',
  'setCount', 'color', 'setColor', 'elapsed', 'itemChange',
  'updatePaintNode'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickUniversalBusyIndicator::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickUniversalBusyIndicator::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickUniversalBusyIndicator; 1 leans on 'vtable for
  QQuickUniversalBusyIndicator', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickUniversalBusyIndicator is created at the first use, not by
    'QQuickUniversalBusyIndicator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickUniversalBusyIndicator.
  - Qt tells when it has removed the C++ QQuickUniversalBusyIndicator. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickUniversalBusyIndicator that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickUniversalBusyIndicator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickUniversalBusyIndicator::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalbusyindicator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickUniversalBusyIndicator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickUniversalBusyIndicator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickUniversalBusyIndicator::count() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalbusyindicator.html#count
    """
    #  int QQuickUniversalBusyIndicator::count() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickUniversalBusyIndicator5countEv',
    )

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalBusyIndicator::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalbusyindicator.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalBusyIndicator::color() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickUniversalBusyIndicator5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def elapsed(self) -> int:
    """
    Calls Qt's 'int QQuickUniversalBusyIndicator::elapsed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalbusyindicator.html#elapsed
    """
    #  int QQuickUniversalBusyIndicator::elapsed() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickUniversalBusyIndicator7elapsedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setCount(self, count: int) -> None:
    """
    Calls Qt's 'void QQuickUniversalBusyIndicator::setCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalbusyindicator.html#setCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQuickUniversalBusyIndicator::setCount(int count)
    self.uglySide.call(
        'ritual_ZN28QQuickUniversalBusyIndicator8setCountEi', count,
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickUniversalBusyIndicator::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalbusyindicator.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickUniversalBusyIndicator::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN28QQuickUniversalBusyIndicator8setColorERK6QColor',
        self._valueOf(color),
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
    Qt's
    'QQuickUniversalBusyIndicator::QQuickUniversalBusyIndicator(QQuickItem
    *parent)': leans on 'vtable for QQuickUniversalBusyIndicator', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickUniversalBusyIndicator.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickUniversalBusyIndicator::QQuickUniversalBusyIndicator(QQuickI"
        "tem *parent)': leans on 'vtable for QQuickUniversalBusyIndicator', "
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

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickUniversalBusyIndicator::itemChange(ItemChange
    change, const ItemChangeData &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalbusyindicator.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickUniversalBusyIndicator::itemChange(ItemChange change, const
    #      ItemChangeData &data)
    ritual = (
        'ritual_ZN28QQuickUniversalBusyIndicator10itemChangeEN10QQuickItem1'
        '0ItemChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuickUniversalBusyIndicator10itemChangeEN10QQuic'
          'kItem10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      oldNode: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode
    *QQuickUniversalBusyIndicator::updatePaintNode(QSGNode *oldNode,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalbusyindicator.html#updatePaintNode

    Parameters
    ----------

    oldNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickUniversalBusyIndicator::updatePaintNode(QSGNode
    #      *oldNode, UpdatePaintNodeData *a1)
    address = self.uglySide.call(
        'ritual_ZN28QQuickUniversalBusyIndicator15updatePaintNodeEP7QSGNode'
        'PN10QQuickItem19UpdatePaintNodeDataE',
        self._addressOf(oldNode, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

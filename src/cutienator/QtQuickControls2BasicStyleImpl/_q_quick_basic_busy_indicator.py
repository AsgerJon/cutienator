"""
QQuickBasicBusyIndicator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2BasicStyleImpl/6.12.0/QtQuickControls2BasicStyleImpl/private/qquickbasicbusyindicator_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickBasicBusyIndicator to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
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


class QQuickBasicBusyIndicator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickBasicBusyIndicator: a plain Python object
  standing in front of one C++ QQuickBasicBusyIndicator.

  What exists
  -----------

  Every function of Qt's QQuickBasicBusyIndicator that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'pen', 'setPen',
  'fill', 'setFill', 'isRunning', 'setRunning', 'elapsed', 'itemChange',
  'updatePaintNode'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickBasicBusyIndicator::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickBasicBusyIndicator::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickBasicBusyIndicator; 1 leans on 'vtable for
  QQuickBasicBusyIndicator', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickBasicBusyIndicator is created at the first use, not by
    'QQuickBasicBusyIndicator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickBasicBusyIndicator.
  - Qt tells when it has removed the C++ QQuickBasicBusyIndicator. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickBasicBusyIndicator that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickBasicBusyIndicator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickBasicBusyIndicator::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasicbusyindicator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickBasicBusyIndicator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickBasicBusyIndicator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pen(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickBasicBusyIndicator::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasicbusyindicator.html#pen

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickBasicBusyIndicator::pen() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickBasicBusyIndicator3penEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def fill(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickBasicBusyIndicator::fill() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasicbusyindicator.html#fill

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickBasicBusyIndicator::fill() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickBasicBusyIndicator4fillEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QQuickBasicBusyIndicator::isRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasicbusyindicator.html#isRunning
    """
    #  bool QQuickBasicBusyIndicator::isRunning() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickBasicBusyIndicator9isRunningEv',
    )

  def elapsed(self) -> int:
    """
    Calls Qt's 'int QQuickBasicBusyIndicator::elapsed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasicbusyindicator.html#elapsed
    """
    #  int QQuickBasicBusyIndicator::elapsed() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickBasicBusyIndicator7elapsedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setPen(self, pen: QColor) -> None:
    """
    Calls Qt's 'void QQuickBasicBusyIndicator::setPen(const QColor &pen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasicbusyindicator.html#setPen

    Parameters
    ----------

    pen : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickBasicBusyIndicator::setPen(const QColor &pen)
    self.uglySide.call(
        'ritual_ZN24QQuickBasicBusyIndicator6setPenERK6QColor',
        self._valueOf(pen),
    )

  @overload(QColor)
  def setFill(self, fill: QColor) -> None:
    """
    Calls Qt's 'void QQuickBasicBusyIndicator::setFill(const QColor &fill)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasicbusyindicator.html#setFill

    Parameters
    ----------

    fill : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickBasicBusyIndicator::setFill(const QColor &fill)
    self.uglySide.call(
        'ritual_ZN24QQuickBasicBusyIndicator7setFillERK6QColor',
        self._valueOf(fill),
    )

  @overload(bool)
  def setRunning(self, running: bool) -> None:
    """
    Calls Qt's 'void QQuickBasicBusyIndicator::setRunning(bool running)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasicbusyindicator.html#setRunning

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QQuickBasicBusyIndicator::setRunning(bool running)
    self.uglySide.call(
        'ritual_ZN24QQuickBasicBusyIndicator10setRunningEb', running,
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
    Qt's 'QQuickBasicBusyIndicator::QQuickBasicBusyIndicator(QQuickItem
    *parent)': leans on 'vtable for QQuickBasicBusyIndicator', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickBasicBusyIndicator.__init__' has no cute function yet. Qt's "
        "'QQuickBasicBusyIndicator::QQuickBasicBusyIndicator(QQuickItem "
        "*parent)': leans on 'vtable for QQuickBasicBusyIndicator', which "
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

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickBasicBusyIndicator::itemChange(ItemChange change,
    const ItemChangeData &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasicbusyindicator.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickBasicBusyIndicator::itemChange(ItemChange change, const
    #      ItemChangeData &data)
    ritual = (
        'ritual_ZN24QQuickBasicBusyIndicator10itemChangeEN10QQuickItem10Ite'
        'mChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickBasicBusyIndicator10itemChangeEN10QQuickIte'
          'm10ItemChangeERKNS0_14ItemChangeDataE')
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
    Calls Qt's 'QSGNode *QQuickBasicBusyIndicator::updatePaintNode(QSGNode
    *oldNode, UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasicbusyindicator.html#updatePaintNode

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
    #  QSGNode *QQuickBasicBusyIndicator::updatePaintNode(QSGNode *oldNode,
    #      UpdatePaintNodeData *a1)
    address = self.uglySide.call(
        'ritual_ZN24QQuickBasicBusyIndicator15updatePaintNodeEP7QSGNodePN10'
        'QQuickItem19UpdatePaintNodeDataE',
        self._addressOf(oldNode, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

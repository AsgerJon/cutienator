"""
QQuickUniversalProgressBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2UniversalStyleImpl/6.12.0/QtQuickControls2UniversalStyleImpl/private/qquickuniversalprogressbar_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickUniversalProgressBar to be private: it declares the class
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


class QQuickUniversalProgressBar(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickUniversalProgressBar: a plain Python object
  standing in front of one C++ QQuickUniversalProgressBar.

  What exists
  -----------

  Every function of Qt's QQuickUniversalProgressBar that has a ritual and
  that Python can call so far, 9 names in all: 'metaObject', 'color',
  'setColor', 'progress', 'setProgress', 'isIndeterminate',
  'setIndeterminate', 'itemChange', 'updatePaintNode'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickUniversalProgressBar::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickUniversalProgressBar::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 not a gap; 1 leans on
  'QQuickUniversalProgressBar; 1 leans on 'vtable for
  QQuickUniversalProgressBar', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickUniversalProgressBar is created at the first use, not by
    'QQuickUniversalProgressBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickUniversalProgressBar.
  - Qt tells when it has removed the C++ QQuickUniversalProgressBar. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickUniversalProgressBar that has no cute function
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
  __qt_class__ = 'QQuickUniversalProgressBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickUniversalProgressBar::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalprogressbar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickUniversalProgressBar::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickUniversalProgressBar10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickUniversalProgressBar::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalprogressbar.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickUniversalProgressBar::color() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickUniversalProgressBar5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def progress(self) -> float:
    """
    Calls Qt's 'qreal QQuickUniversalProgressBar::progress() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalprogressbar.html#progress
    """
    #  qreal QQuickUniversalProgressBar::progress() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickUniversalProgressBar8progressEv',
    )

  def isIndeterminate(self) -> bool:
    """
    Calls Qt's 'bool QQuickUniversalProgressBar::isIndeterminate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalprogressbar.html#isIndeterminate
    """
    #  bool QQuickUniversalProgressBar::isIndeterminate() const
    return self.uglySide.call(
        'ritual_ZNK26QQuickUniversalProgressBar15isIndeterminateEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickUniversalProgressBar::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalprogressbar.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickUniversalProgressBar::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN26QQuickUniversalProgressBar8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setProgress(self, progress: float) -> None:
    """
    Calls Qt's 'void QQuickUniversalProgressBar::setProgress(qreal
    progress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalprogressbar.html#setProgress

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  void QQuickUniversalProgressBar::setProgress(qreal progress)
    self.uglySide.call(
        'ritual_ZN26QQuickUniversalProgressBar11setProgressEd', progress,
    )

  @overload(bool)
  def setIndeterminate(self, indeterminate: bool) -> None:
    """
    Calls Qt's 'void QQuickUniversalProgressBar::setIndeterminate(bool
    indeterminate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalprogressbar.html#setIndeterminate

    Parameters
    ----------

    indeterminate : bool
      Passed on as it is.
    """
    #  void QQuickUniversalProgressBar::setIndeterminate(bool indeterminate)
    self.uglySide.call(
        'ritual_ZN26QQuickUniversalProgressBar16setIndeterminateEb',
        indeterminate,
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
    Qt's 'QQuickUniversalProgressBar::QQuickUniversalProgressBar(QQuickItem
    *parent)': leans on 'vtable for QQuickUniversalProgressBar', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickUniversalProgressBar.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickUniversalProgressBar::QQuickUniversalProgressBar(QQuickItem "
        "*parent)': leans on 'vtable for QQuickUniversalProgressBar', which "
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
    Calls Qt's 'void QQuickUniversalProgressBar::itemChange(ItemChange
    change, const ItemChangeData &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalprogressbar.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickUniversalProgressBar::itemChange(ItemChange change, const
    #      ItemChangeData &data)
    ritual = (
        'ritual_ZN26QQuickUniversalProgressBar10itemChangeEN10QQuickItem10I'
        'temChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickUniversalProgressBar10itemChangeEN10QQuickI'
          'tem10ItemChangeERKNS0_14ItemChangeDataE')
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
    Calls Qt's 'QSGNode *QQuickUniversalProgressBar::updatePaintNode(QSGNode
    *oldNode, UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniversalprogressbar.html#updatePaintNode

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
    #  QSGNode *QQuickUniversalProgressBar::updatePaintNode(QSGNode *oldNode,
    #      UpdatePaintNodeData *a1)
    address = self.uglySide.call(
        'ritual_ZN26QQuickUniversalProgressBar15updatePaintNodeEP7QSGNodePN'
        '10QQuickItem19UpdatePaintNodeDataE',
        self._addressOf(oldNode, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

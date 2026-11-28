"""
QQuickGridLayoutEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquickgridlayoutengine_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickGridLayoutEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickGridLayoutItem
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGridLayoutEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickGridLayoutEngine: a plain Python object
  standing in front of one C++ QQuickGridLayoutEngine.

  C++ hands a QQuickGridLayoutEngine around as a copy, so every C++
  QQuickGridLayoutEngine behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickGridLayoutEngine that has a ritual and that
  Python can call so far, 4 names in all: 'indexOf', 'findLayoutItem',
  'setAlignment', 'setStretchFactor'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickGridLayoutEngine::~QQuickGridLayoutEngine()': the destructor:
    Python removes its C++ QQuickGridLayoutEngine by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQuickGridLayoutEngine is created at the first use, not by
    'QQuickGridLayoutEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickGridLayoutEngine back gives a copy the ritual
    made for Python, in a new cute QQuickGridLayoutEngine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickGridLayoutEngine'

  #  Qt's '~QQuickGridLayoutEngine()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickGridLayoutEngine behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QQuickGridLayoutEngineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def indexOf(self, item: Optional[QQuickItem]) -> int:
    """
    Calls Qt's 'int QQuickGridLayoutEngine::indexOf(QQuickItem *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutengine.html#indexOf

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuickGridLayoutEngine::indexOf(QQuickItem *item) const
    return self.uglySide.call(
        'ritual_ZNK22QQuickGridLayoutEngine7indexOfEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def findLayoutItem(
      self,
      layoutItem: Optional[QQuickItem],
  ) -> Optional[QQuickGridLayoutItem]:
    """
    Calls Qt's 'QQuickGridLayoutItem
    *QQuickGridLayoutEngine::findLayoutItem(QQuickItem *layoutItem) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutengine.html#findLayoutItem

    Parameters
    ----------

    layoutItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickGridLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGridLayoutItem
    #      *QQuickGridLayoutEngine::findLayoutItem(QQuickItem *layoutItem)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickGridLayoutEngine14findLayoutItemEP10QQuickItem',
        self._addressOf(layoutItem),
    )
    from . import QQuickGridLayoutItem
    return QQuickGridLayoutItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def setAlignment(
      self,
      quickItem: Optional[QQuickItem],
      alignment: Qt.Alignment,
  ) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutEngine::setAlignment(QQuickItem
    *quickItem, Qt::Alignment alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutengine.html#setAlignment

    Parameters
    ----------

    quickItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QQuickGridLayoutEngine::setAlignment(QQuickItem *quickItem,
    #      Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN22QQuickGridLayoutEngine12setAlignmentEP10QQuickItem6QFla'
        'gsIN2Qt13AlignmentFlagEE',
        self._addressOf(quickItem), alignment.value,
    )

  @overload(QQuickItem, int, Qt.Orientation)
  @overload(NoneType, int, Qt.Orientation)
  def setStretchFactor(
      self,
      quickItem: Optional[QQuickItem],
      stretch: int,
      orientation: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QQuickGridLayoutEngine::setStretchFactor(QQuickItem
    *quickItem, int stretch, Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutengine.html#setStretchFactor

    Parameters
    ----------

    quickItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretch : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickGridLayoutEngine::setStretchFactor(QQuickItem *quickItem,
    #      int stretch, Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN22QQuickGridLayoutEngine16setStretchFactorEP10QQuickItemi'
        'N2Qt11OrientationE',
        self._addressOf(quickItem), stretch, orientation.value,
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
    'QQuickGridLayoutEngine::QQuickGridLayoutEngine()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridlayoutengine.html#QQuickGridLayoutEngine
    """
    #  QQuickGridLayoutEngine::QQuickGridLayoutEngine()
    self._noteCreation(QQuickGridLayoutEngine, lambda: Rituals.call(
        'ritual_ZN22QQuickGridLayoutEngineC1Ev',
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

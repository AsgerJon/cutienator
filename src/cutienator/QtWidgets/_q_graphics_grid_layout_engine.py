"""
QGraphicsGridLayoutEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsgridlayoutengine_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGraphicsGridLayoutEngine to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from ..QtGui import QGridLayoutEngine

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGraphicsGridLayoutEngineItem, QGraphicsLayoutItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsLayoutItem = WAIT['QGraphicsLayoutItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsGridLayoutEngine(QGridLayoutEngine):
  """
  The cute side of Qt's QGraphicsGridLayoutEngine: a plain Python object
  standing in front of one C++ QGraphicsGridLayoutEngine.

  It is built on the cute 'QGridLayoutEngine', as Qt's
  QGraphicsGridLayoutEngine is built on Qt's QGridLayoutEngine, and has
  everything that class has.

  C++ hands a QGraphicsGridLayoutEngine around as a copy, so every C++
  QGraphicsGridLayoutEngine behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGraphicsGridLayoutEngine that has a ritual and that
  Python can call so far, 6 names in all: 'findLayoutItem', 'indexOf',
  'setAlignment', 'alignment', 'setStretchFactor', 'stretchFactor'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsGridLayoutEngine::~QGraphicsGridLayoutEngine()': the
    destructor: Python removes its C++ QGraphicsGridLayoutEngine by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QGraphicsGridLayoutEngine is created at the first use, not by
    'QGraphicsGridLayoutEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGraphicsGridLayoutEngine back gives a copy the
    ritual made for Python, in a new cute QGraphicsGridLayoutEngine.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsGridLayoutEngine'

  #  Qt's '~QGraphicsGridLayoutEngine()'. Naming it makes this a value class:
  #  Python owns every C++ QGraphicsGridLayoutEngine behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QGraphicsGridLayoutEngineD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def findLayoutItem(
      self,
      layoutItem: Optional[QGraphicsLayoutItem],
  ) -> Optional[QGraphicsGridLayoutEngineItem]:
    """
    Calls Qt's 'QGraphicsGridLayoutEngineItem
    *QGraphicsGridLayoutEngine::findLayoutItem(QGraphicsLayoutItem
    *layoutItem) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengine.html#findLayoutItem

    Parameters
    ----------

    layoutItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGraphicsGridLayoutEngineItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsGridLayoutEngineItem
    #      *QGraphicsGridLayoutEngine::findLayoutItem(QGraphicsLayoutItem
    #      *layoutItem) const
    address = self.uglySide.call(
        'ritual_ZNK25QGraphicsGridLayoutEngine14findLayoutItemEP19QGraphics'
        'LayoutItem',
        self._addressOf(layoutItem, 'QGraphicsLayoutItem'),
    )
    from . import QGraphicsGridLayoutEngineItem
    return QGraphicsGridLayoutEngineItem._cuteAt(address)

  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def indexOf(self, item: Optional[QGraphicsLayoutItem]) -> int:
    """
    Calls Qt's 'int QGraphicsGridLayoutEngine::indexOf(QGraphicsLayoutItem
    *item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengine.html#indexOf

    Parameters
    ----------

    item : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QGraphicsGridLayoutEngine::indexOf(QGraphicsLayoutItem *item)
    #      const
    return self.uglySide.call(
        'ritual_ZNK25QGraphicsGridLayoutEngine7indexOfEP19QGraphicsLayoutIt'
        'em',
        self._addressOf(item, 'QGraphicsLayoutItem'),
    )

  @overload(QGraphicsLayoutItem)
  @overload(NoneType)
  def alignment(
      self,
      graphicsLayoutItem: Optional[QGraphicsLayoutItem],
  ) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment
    QGraphicsGridLayoutEngine::alignment(QGraphicsLayoutItem
    *graphicsLayoutItem) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengine.html#alignment

    Parameters
    ----------

    graphicsLayoutItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QGraphicsGridLayoutEngine::alignment(QGraphicsLayoutItem
    #      *graphicsLayoutItem) const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK25QGraphicsGridLayoutEngine9alignmentEP19QGraphicsLayout'
        'Item',
        self._addressOf(graphicsLayoutItem, 'QGraphicsLayoutItem'),
    ))

  @overload(QGraphicsLayoutItem, Qt.Orientation)
  @overload(NoneType, Qt.Orientation)
  def stretchFactor(
      self,
      layoutItem: Optional[QGraphicsLayoutItem],
      orientation: Qt.Orientation,
  ) -> int:
    """
    Calls Qt's 'int
    QGraphicsGridLayoutEngine::stretchFactor(QGraphicsLayoutItem *layoutItem,
    Qt::Orientation orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengine.html#stretchFactor

    Parameters
    ----------

    layoutItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  int QGraphicsGridLayoutEngine::stretchFactor(QGraphicsLayoutItem
    #      *layoutItem, Qt::Orientation orientation) const
    return self.uglySide.call(
        'ritual_ZNK25QGraphicsGridLayoutEngine13stretchFactorEP19QGraphicsL'
        'ayoutItemN2Qt11OrientationE',
        self._addressOf(layoutItem, 'QGraphicsLayoutItem'),
        orientation.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGraphicsLayoutItem, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def setAlignment(
      self,
      graphicsLayoutItem: Optional[QGraphicsLayoutItem],
      alignment: Qt.Alignment,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsGridLayoutEngine::setAlignment(QGraphicsLayoutItem
    *graphicsLayoutItem, Qt::Alignment alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengine.html#setAlignment

    Parameters
    ----------

    graphicsLayoutItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QGraphicsGridLayoutEngine::setAlignment(QGraphicsLayoutItem
    #      *graphicsLayoutItem, Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN25QGraphicsGridLayoutEngine12setAlignmentEP19QGraphicsLay'
        'outItem6QFlagsIN2Qt13AlignmentFlagEE',
        self._addressOf(graphicsLayoutItem, 'QGraphicsLayoutItem'),
        alignment.value,
    )

  @overload(QGraphicsLayoutItem, int, Qt.Orientation)
  @overload(NoneType, int, Qt.Orientation)
  def setStretchFactor(
      self,
      layoutItem: Optional[QGraphicsLayoutItem],
      stretch: int,
      orientation: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsGridLayoutEngine::setStretchFactor(QGraphicsLayoutItem
    *layoutItem, int stretch, Qt::Orientation orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsgridlayoutengine.html#setStretchFactor

    Parameters
    ----------

    layoutItem : Optional[QGraphicsLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretch : int
      Passed on as it is.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QGraphicsGridLayoutEngine::setStretchFactor(QGraphicsLayoutItem
    #      *layoutItem, int stretch, Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN25QGraphicsGridLayoutEngine16setStretchFactorEP19QGraphic'
        'sLayoutItemiN2Qt11OrientationE',
        self._addressOf(layoutItem, 'QGraphicsLayoutItem'), stretch,
        orientation.value,
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

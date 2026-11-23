"""
QWidgetItemV2 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qlayoutitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QWidgetItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidgetItemV2(QWidgetItem):
  """
  The cute side of Qt's QWidgetItemV2: a plain Python object standing in
  front of one C++ QWidgetItemV2.

  It is built on the cute 'QWidgetItem', as Qt's QWidgetItemV2 is built on
  Qt's QWidgetItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWidgetItemV2 that has a ritual and that Python can
  call so far, 6 names in all: 'sizeHint', 'minimumSize', 'maximumSize',
  'heightForWidth', 'updateCacheIfNecessary', 'invalidateSizeCache'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWidgetItemV2::~QWidgetItemV2()': the destructor: Python never
    removes a C++ QWidgetItemV2.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 2 forbidden; 1 declared and nowhere to
  be found.

  What to expect
  --------------

  - The C++ QWidgetItemV2 is created at the first use, not by
    'QWidgetItemV2(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidgetItemV2.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetItemV2'

  #  A C++ QWidgetItemV2 Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWidgetItemV2'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QWidgetItemV2::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitemv2.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidgetItemV2::sizeHint() const
    ritual = 'ritual_ZNK13QWidgetItemV28sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QWidgetItemV28sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWidgetItemV2::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitemv2.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidgetItemV2::minimumSize() const
    ritual = 'ritual_ZNK13QWidgetItemV211minimumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QWidgetItemV211minimumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def maximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWidgetItemV2::maximumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitemv2.html#maximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWidgetItemV2::maximumSize() const
    ritual = 'ritual_ZNK13QWidgetItemV211maximumSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QWidgetItemV211maximumSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int)
  def heightForWidth(self, width: int) -> int:
    """
    Calls Qt's 'int QWidgetItemV2::heightForWidth(int width) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitemv2.html#heightForWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  int QWidgetItemV2::heightForWidth(int width) const
    ritual = 'ritual_ZNK13QWidgetItemV214heightForWidthEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QWidgetItemV214heightForWidthEi'
    return self.uglySide.call(ritual, width)

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

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, widget: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's 'QWidgetItemV2::QWidgetItemV2(QWidget
    *widget)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetitemv2.html#QWidgetItemV2

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWidgetItemV2::QWidgetItemV2(QWidget *widget)
    self._noteCreation(QWidgetItemV2, lambda: Rituals.call(
        'ritual_ZN13QWidgetItemV2C1EP7QWidget', self._addressOf(widget),
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

  def updateCacheIfNecessary(self) -> None:
    """
    Calls Qt's 'void QWidgetItemV2::updateCacheIfNecessary() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetitemv2.html#updateCacheIfNecessary
    """
    #  void QWidgetItemV2::updateCacheIfNecessary() const
    self.uglySide.call('ritual_ZNK13QWidgetItemV222updateCacheIfNecessaryEv')

  def invalidateSizeCache(self) -> None:
    """
    Calls Qt's 'void QWidgetItemV2::invalidateSizeCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetitemv2.html#invalidateSizeCache
    """
    #  void QWidgetItemV2::invalidateSizeCache()
    self.uglySide.call('ritual_ZN13QWidgetItemV219invalidateSizeCacheEv')

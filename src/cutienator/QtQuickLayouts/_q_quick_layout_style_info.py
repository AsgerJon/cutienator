"""
QQuickLayoutStyleInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayoutstyleinfo_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickLayoutStyleInfo to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import Qt


class QQuickLayoutStyleInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickLayoutStyleInfo: a plain Python object standing
  in front of one C++ QQuickLayoutStyleInfo.

  C++ hands a QQuickLayoutStyleInfo around as a copy, so every C++
  QQuickLayoutStyleInfo behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickLayoutStyleInfo that has a ritual and that
  Python can call so far, 3 names in all: 'spacing', 'windowMargin',
  'hasChangedCore'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickLayoutStyleInfo::~QQuickLayoutStyleInfo()': the destructor:
    Python removes its C++ QQuickLayoutStyleInfo by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQuickLayoutStyleInfo is created at the first use, not by
    'QQuickLayoutStyleInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickLayoutStyleInfo back gives a copy the ritual
    made for Python, in a new cute QQuickLayoutStyleInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLayoutStyleInfo'

  #  A C++ QQuickLayoutStyleInfo Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLayoutStyleInfo'

  #  Qt's '~QQuickLayoutStyleInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickLayoutStyleInfo behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QQuickLayoutStyleInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def spacing(self, orientation: Qt.Orientation) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutStyleInfo::spacing(Qt::Orientation
    orientation) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayoutstyleinfo.html#spacing

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QQuickLayoutStyleInfo::spacing(Qt::Orientation orientation)
    #      const
    ritual = 'ritual_ZNK21QQuickLayoutStyleInfo7spacingEN2Qt11OrientationE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QQuickLayoutStyleInfo7spacingEN2Qt11OrientationE')
    return self.uglySide.call(ritual, orientation.value)

  @overload(Qt.Orientation)
  def windowMargin(self, orientation: Qt.Orientation) -> float:
    """
    Calls Qt's 'qreal QQuickLayoutStyleInfo::windowMargin(Qt::Orientation
    orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutstyleinfo.html#windowMargin

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QQuickLayoutStyleInfo::windowMargin(Qt::Orientation orientation)
    #      const
    ritual = (
        'ritual_ZNK21QQuickLayoutStyleInfo12windowMarginEN2Qt11OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QQuickLayoutStyleInfo12windowMarginEN2Qt11Orient'
          'ationE')
    return self.uglySide.call(ritual, orientation.value)

  def hasChangedCore(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayoutStyleInfo::hasChangedCore() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutstyleinfo.html#hasChangedCore
    """
    #  bool QQuickLayoutStyleInfo::hasChangedCore() const
    ritual = 'ritual_ZNK21QQuickLayoutStyleInfo14hasChangedCoreEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickLayoutStyleInfo14hasChangedCoreEv'
    return self.uglySide.call(ritual)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickLayoutStyleInfo::QQuickLayoutStyleInfo()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayoutstyleinfo.html#QQuickLayoutStyleInfo
    """
    #  QQuickLayoutStyleInfo::QQuickLayoutStyleInfo()
    self._noteCreation(QQuickLayoutStyleInfo, lambda: Rituals.call(
        'ritual_ZN21QQuickLayoutStyleInfoC1Ev',
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

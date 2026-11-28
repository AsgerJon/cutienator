"""
QGraphicsLayoutStyleInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicslayoutstyleinfo_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGraphicsLayoutStyleInfo to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QAbstractLayoutStyleInfo, QLayoutPolicy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QGraphicsLayoutPrivate, QStyle, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsLayoutPrivate = WAIT['QGraphicsLayoutPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsLayoutStyleInfo(QAbstractLayoutStyleInfo):
  """
  The cute side of Qt's QGraphicsLayoutStyleInfo: a plain Python object
  standing in front of one C++ QGraphicsLayoutStyleInfo.

  It is built on the cute 'QAbstractLayoutStyleInfo', as Qt's
  QGraphicsLayoutStyleInfo is built on Qt's QAbstractLayoutStyleInfo, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsLayoutStyleInfo that has a ritual and that
  Python can call so far, 7 names in all: 'combinedLayoutSpacing',
  'perItemSpacing', 'spacing', 'windowMargin', 'invalidate', 'widget',
  'style'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsLayoutStyleInfo::~QGraphicsLayoutStyleInfo()': the
    destructor: Python never removes a C++ QGraphicsLayoutStyleInfo.

  What to expect
  --------------

  - The C++ QGraphicsLayoutStyleInfo is created at the first use, not by
    'QGraphicsLayoutStyleInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsLayoutStyleInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsLayoutStyleInfo'

  #  A C++ QGraphicsLayoutStyleInfo Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsLayoutStyleInfo'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(
      QLayoutPolicy.ControlTypes, QLayoutPolicy.ControlTypes, Qt.Orientation,
  )
  def combinedLayoutSpacing(
      self,
      controls1: QLayoutPolicy.ControlTypes,
      controls2: QLayoutPolicy.ControlTypes,
      orientation: Qt.Orientation,
  ) -> float:
    """
    Calls Qt's 'qreal
    QGraphicsLayoutStyleInfo::combinedLayoutSpacing(QLayoutPolicy::
    ControlTypes controls1, QLayoutPolicy::ControlTypes controls2,
    Qt::Orientation orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutstyleinfo.html

    Parameters
    ----------

    controls1 : QLayoutPolicy.ControlTypes
      Passed on as its number.

    controls2 : QLayoutPolicy.ControlTypes
      Passed on as its number.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QGraphicsLayoutStyleInfo::combinedLayoutSpacing(QLayoutPolicy::
    #      ControlTypes controls1, QLayoutPolicy::ControlTypes controls2,
    #      Qt::Orientation orientation) const
    ritual = (
        'ritual_ZNK24QGraphicsLayoutStyleInfo21combinedLayoutSpacingE6QFlag'
        'sIN13QLayoutPolicy11ControlTypeEES3_N2Qt11OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QGraphicsLayoutStyleInfo21combinedLayoutSpacingE'
          '6QFlagsIN13QLayoutPolicy11ControlTypeEES3_N2Qt11OrientationE')
    return self.uglySide.call(
        ritual, controls1.value, controls2.value, orientation.value,
    )

  @overload(
      QLayoutPolicy.ControlType, QLayoutPolicy.ControlType, Qt.Orientation,
  )
  def perItemSpacing(
      self,
      control1: QLayoutPolicy.ControlType,
      control2: QLayoutPolicy.ControlType,
      orientation: Qt.Orientation,
  ) -> float:
    """
    Calls Qt's 'qreal
    QGraphicsLayoutStyleInfo::perItemSpacing(QLayoutPolicy::ControlType
    control1, QLayoutPolicy::ControlType control2, Qt::Orientation
    orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutstyleinfo.html#perItemSpacing

    Parameters
    ----------

    control1 : QLayoutPolicy.ControlType
      Passed on as its number.

    control2 : QLayoutPolicy.ControlType
      Passed on as its number.

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QGraphicsLayoutStyleInfo::perItemSpacing(QLayoutPolicy::
    #      ControlType control1, QLayoutPolicy::ControlType control2,
    #      Qt::Orientation orientation) const
    ritual = (
        'ritual_ZNK24QGraphicsLayoutStyleInfo14perItemSpacingEN13QLayoutPol'
        'icy11ControlTypeES1_N2Qt11OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QGraphicsLayoutStyleInfo14perItemSpacingEN13QLay'
          'outPolicy11ControlTypeES1_N2Qt11OrientationE')
    return self.uglySide.call(
        ritual, control1.value, control2.value, orientation.value,
    )

  @overload(Qt.Orientation)
  def spacing(self, orientation: Qt.Orientation) -> float:
    """
    Calls Qt's 'qreal QGraphicsLayoutStyleInfo::spacing(Qt::Orientation
    orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutstyleinfo.html#spacing

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QGraphicsLayoutStyleInfo::spacing(Qt::Orientation orientation)
    #      const
    ritual = (
        'ritual_ZNK24QGraphicsLayoutStyleInfo7spacingEN2Qt11OrientationE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QGraphicsLayoutStyleInfo7spacingEN2Qt11Orientati'
          'onE')
    return self.uglySide.call(ritual, orientation.value)

  @overload(Qt.Orientation)
  def windowMargin(self, orientation: Qt.Orientation) -> float:
    """
    Calls Qt's 'qreal QGraphicsLayoutStyleInfo::windowMargin(Qt::Orientation
    orientation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutstyleinfo.html#windowMargin

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  qreal QGraphicsLayoutStyleInfo::windowMargin(Qt::Orientation
    #      orientation) const
    ritual = (
        'ritual_ZNK24QGraphicsLayoutStyleInfo12windowMarginEN2Qt11Orientati'
        'onE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QGraphicsLayoutStyleInfo12windowMarginEN2Qt11Ori'
          'entationE')
    return self.uglySide.call(ritual, orientation.value)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QGraphicsLayoutStyleInfo::widget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutstyleinfo.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QGraphicsLayoutStyleInfo::widget() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsLayoutStyleInfo6widgetEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def style(self) -> Optional[QStyle]:
    """
    Calls Qt's 'QStyle *QGraphicsLayoutStyleInfo::style() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutstyleinfo.html#style

    Returns
    -------

    Optional[QStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStyle *QGraphicsLayoutStyleInfo::style() const
    address = self.uglySide.call(
        'ritual_ZNK24QGraphicsLayoutStyleInfo5styleEv',
    )
    from . import QStyle
    return QStyle._cuteAt(address)

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

  @overload(QGraphicsLayoutPrivate)
  @overload(NoneType)
  def __init__(self, layout: Optional[QGraphicsLayoutPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsLayoutStyleInfo::QGraphicsLayoutStyleInfo(const
    QGraphicsLayoutPrivate *layout)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutstyleinfo.html

    Parameters
    ----------

    layout : Optional[QGraphicsLayoutPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGraphicsLayoutStyleInfo::QGraphicsLayoutStyleInfo(const
    #      QGraphicsLayoutPrivate *layout)
    self._noteCreation(QGraphicsLayoutStyleInfo, lambda: Rituals.call(
        'ritual_ZN24QGraphicsLayoutStyleInfoC1EPK22QGraphicsLayoutPrivate',
        self._addressOf(layout),
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

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QGraphicsLayoutStyleInfo::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicslayoutstyleinfo.html#invalidate
    """
    #  void QGraphicsLayoutStyleInfo::invalidate()
    ritual = 'ritual_ZN24QGraphicsLayoutStyleInfo10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QGraphicsLayoutStyleInfo10invalidateEv'
    self.uglySide.call(ritual)

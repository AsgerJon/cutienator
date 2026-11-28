"""
QQuickAbstractColorPickerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickabstractcolorpicker_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickAbstractColorPickerPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
  from ..QtQuick import QQuickItem
  from . import QQuickAbstractColorPicker
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QQuickAbstractColorPicker = WAIT['QQuickAbstractColorPicker']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAbstractColorPickerPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickAbstractColorPickerPrivate: a plain Python
  object standing in front of one C++ QQuickAbstractColorPickerPrivate.

  What exists
  -----------

  Every function of Qt's QQuickAbstractColorPickerPrivate that has a ritual
  and that Python can call so far, 10 names in all: 'q_func', 'get',
  'handlePress', 'handleMove', 'handleRelease', 'handleUngrab',
  'cancelHandle', 'executeHandle', 'itemImplicitWidthChanged',
  'itemImplicitHeightChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickAbstractColorPicker
    *QQuickAbstractColorPickerPrivate::q_func() const': takes in Python what
    'QQuickAbstractColorPicker *QQuickAbstractColorPickerPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ QQuickAbstractColorPickerPrivate is created at the first use, not
    by 'QQuickAbstractColorPickerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAbstractColorPickerPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickAbstractColorPicker)
  @overload(NoneType)
  def get(
      colorPicker: Optional[QQuickAbstractColorPicker],
  ) -> Optional[QQuickAbstractColorPickerPrivate]:
    """
    Calls Qt's 'QQuickAbstractColorPickerPrivate
    *QQuickAbstractColorPickerPrivate::get(QQuickAbstractColorPicker
    *colorPicker)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpickerprivate.html#get

    Parameters
    ----------

    colorPicker : Optional[QQuickAbstractColorPicker]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickAbstractColorPickerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractColorPickerPrivate
    #      *QQuickAbstractColorPickerPrivate::get(QQuickAbstractColorPicker
    #      *colorPicker)
    address = Rituals.call(
        'ritual_ZN32QQuickAbstractColorPickerPrivate3getEP25QQuickAbstractC'
        'olorPicker',
        CuteMixin._addressOf(colorPicker),
    )
    return QQuickAbstractColorPickerPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAbstractColorPickerPrivate'

  #  A C++ QQuickAbstractColorPickerPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAbstractColorPickerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QQuickAbstractColorPickerPrivate::QQuickAbstractColorPickerPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpickerprivate.html
    """
    #  QQuickAbstractColorPickerPrivate::QQuickAbstractColorPickerPrivate()
    self._noteCreation(
        QQuickAbstractColorPickerPrivate, lambda: Rituals.call(
            'ritual_ZN32QQuickAbstractColorPickerPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickAbstractColorPicker]:
    """
    Calls Qt's 'QQuickAbstractColorPicker
    *QQuickAbstractColorPickerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpickerprivate.html#q_func

    Returns
    -------

    Optional[QQuickAbstractColorPicker]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractColorPicker *QQuickAbstractColorPickerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN32QQuickAbstractColorPickerPrivate6q_funcEv',
    )
    from . import QQuickAbstractColorPicker
    return QQuickAbstractColorPicker._cuteAt(address)

  @overload(QPointF, int)
  def handlePress(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractColorPickerPrivate::handlePress(const
    QPointF &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpickerprivate.html#handlePress

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickAbstractColorPickerPrivate::handlePress(const QPointF
    #      &point, ulong timestamp)
    ritual = (
        'ritual_ZN32QQuickAbstractColorPickerPrivate11handlePressERK7QPoint'
        'Fm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuickAbstractColorPickerPrivate11handlePressERK7'
          'QPointFm')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QPointF, int)
  def handleMove(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractColorPickerPrivate::handleMove(const
    QPointF &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpickerprivate.html#handleMove

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickAbstractColorPickerPrivate::handleMove(const QPointF
    #      &point, ulong timestamp)
    ritual = (
        'ritual_ZN32QQuickAbstractColorPickerPrivate10handleMoveERK7QPointF'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuickAbstractColorPickerPrivate10handleMoveERK7Q'
          'PointFm')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QPointF, int)
  def handleRelease(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractColorPickerPrivate::handleRelease(const
    QPointF &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpickerprivate.html

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickAbstractColorPickerPrivate::handleRelease(const QPointF
    #      &point, ulong timestamp)
    ritual = (
        'ritual_ZN32QQuickAbstractColorPickerPrivate13handleReleaseERK7QPoi'
        'ntFm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuickAbstractColorPickerPrivate13handleReleaseER'
          'K7QPointFm')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  def handleUngrab(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPickerPrivate::handleUngrab()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpickerprivate.html#handleUngrab
    """
    #  void QQuickAbstractColorPickerPrivate::handleUngrab()
    ritual = 'ritual_ZN32QQuickAbstractColorPickerPrivate12handleUngrabEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuickAbstractColorPickerPrivate12handleUngrabEv')
    self.uglySide.call(ritual)

  def cancelHandle(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPickerPrivate::cancelHandle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpickerprivate.html#cancelHandle
    """
    #  void QQuickAbstractColorPickerPrivate::cancelHandle()
    self.uglySide.call(
        'ritual_ZN32QQuickAbstractColorPickerPrivate12cancelHandleEv',
    )

  @overload()
  @overload(bool)
  def executeHandle(self, complete: bool = False) -> None:
    """
    Calls Qt's 'void QQuickAbstractColorPickerPrivate::executeHandle(bool
    complete)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpickerprivate.html

    Parameters
    ----------

    complete : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickAbstractColorPickerPrivate::executeHandle(bool complete)
    self.uglySide.call(
        'ritual_ZN32QQuickAbstractColorPickerPrivate13executeHandleEb',
        complete,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickAbstractColorPickerPrivate::itemImplicitWidthChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpickerprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractColorPickerPrivate::itemImplicitWidthChanged(
    #      QQuickItem *item)
    ritual = (
        'ritual_ZN32QQuickAbstractColorPickerPrivate24itemImplicitWidthChan'
        'gedEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuickAbstractColorPickerPrivate24itemImplicitWid'
          'thChangedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickAbstractColorPickerPrivate::itemImplicitHeightChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractcolorpickerprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractColorPickerPrivate::itemImplicitHeightChanged(
    #      QQuickItem *item)
    ritual = (
        'ritual_ZN32QQuickAbstractColorPickerPrivate25itemImplicitHeightCha'
        'ngedEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QQuickAbstractColorPickerPrivate25itemImplicitHei'
          'ghtChangedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

"""
QQuickScaleGrid binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickscalegrid_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickScaleGrid to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickScaleGrid(QObject):
  """
  The cute side of Qt's QQuickScaleGrid: a plain Python object standing in
  front of one C++ QQuickScaleGrid.

  It is built on the cute 'QObject', as Qt's QQuickScaleGrid is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickScaleGrid that has a ritual and that Python
  can call so far, 16 names in all: 'metaObject', 'tr', 'isNull', 'left',
  'setLeft', 'top', 'setTop', 'right', 'setRight', 'bottom', 'setBottom',
  'borderChanged', 'leftBorderChanged', 'topBorderChanged',
  'rightBorderChanged', 'bottomBorderChanged'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickScaleGrid::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickScaleGrid::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickScaleGrid::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickScaleGrid is created at the first use, not by
    'QQuickScaleGrid(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickScaleGrid.
  - Qt tells when it has removed the C++ QQuickScaleGrid. Every call on the
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
    Calls Qt's 'QString QQuickScaleGrid::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscalegrid.html#tr

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
    #  QString QQuickScaleGrid::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickScaleGrid2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickScaleGrid'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickScaleGrid::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscalegrid.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickScaleGrid::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickScaleGrid10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQuickScaleGrid::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscalegrid.html#isNull
    """
    #  bool QQuickScaleGrid::isNull() const
    return self.uglySide.call('ritual_ZNK15QQuickScaleGrid6isNullEv')

  def left(self) -> int:
    """
    Calls Qt's 'int QQuickScaleGrid::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscalegrid.html#left
    """
    #  int QQuickScaleGrid::left() const
    return self.uglySide.call('ritual_ZNK15QQuickScaleGrid4leftEv')

  def top(self) -> int:
    """
    Calls Qt's 'int QQuickScaleGrid::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscalegrid.html#top
    """
    #  int QQuickScaleGrid::top() const
    return self.uglySide.call('ritual_ZNK15QQuickScaleGrid3topEv')

  def right(self) -> int:
    """
    Calls Qt's 'int QQuickScaleGrid::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscalegrid.html#right
    """
    #  int QQuickScaleGrid::right() const
    return self.uglySide.call('ritual_ZNK15QQuickScaleGrid5rightEv')

  def bottom(self) -> int:
    """
    Calls Qt's 'int QQuickScaleGrid::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscalegrid.html#bottom
    """
    #  int QQuickScaleGrid::bottom() const
    return self.uglySide.call('ritual_ZNK15QQuickScaleGrid6bottomEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLeft(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickScaleGrid::setLeft(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscalegrid.html#setLeft

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickScaleGrid::setLeft(int a0)
    self.uglySide.call('ritual_ZN15QQuickScaleGrid7setLeftEi', a0)

  @overload(int)
  def setTop(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickScaleGrid::setTop(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscalegrid.html#setTop

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickScaleGrid::setTop(int a0)
    self.uglySide.call('ritual_ZN15QQuickScaleGrid6setTopEi', a0)

  @overload(int)
  def setRight(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickScaleGrid::setRight(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscalegrid.html#setRight

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickScaleGrid::setRight(int a0)
    self.uglySide.call('ritual_ZN15QQuickScaleGrid8setRightEi', a0)

  @overload(int)
  def setBottom(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickScaleGrid::setBottom(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscalegrid.html#setBottom

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickScaleGrid::setBottom(int a0)
    self.uglySide.call('ritual_ZN15QQuickScaleGrid9setBottomEi', a0)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickScaleGrid::QQuickScaleGrid(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscalegrid.html#QQuickScaleGrid

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickScaleGrid::QQuickScaleGrid(QObject *parent)
    self._noteCreation(QQuickScaleGrid, lambda: Rituals.call(
        'ritual_ZN15QQuickScaleGridC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def borderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScaleGrid::borderChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscalegrid.html#borderChanged
    """
    #  void QQuickScaleGrid::borderChanged()
    self.uglySide.call('ritual_ZN15QQuickScaleGrid13borderChangedEv')

  def leftBorderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScaleGrid::leftBorderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscalegrid.html#leftBorderChanged
    """
    #  void QQuickScaleGrid::leftBorderChanged()
    self.uglySide.call('ritual_ZN15QQuickScaleGrid17leftBorderChangedEv')

  def topBorderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScaleGrid::topBorderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscalegrid.html#topBorderChanged
    """
    #  void QQuickScaleGrid::topBorderChanged()
    self.uglySide.call('ritual_ZN15QQuickScaleGrid16topBorderChangedEv')

  def rightBorderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScaleGrid::rightBorderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscalegrid.html#rightBorderChanged
    """
    #  void QQuickScaleGrid::rightBorderChanged()
    self.uglySide.call('ritual_ZN15QQuickScaleGrid18rightBorderChangedEv')

  def bottomBorderChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScaleGrid::bottomBorderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscalegrid.html#bottomBorderChanged
    """
    #  void QQuickScaleGrid::bottomBorderChanged()
    self.uglySide.call('ritual_ZN15QQuickScaleGrid19bottomBorderChangedEv')

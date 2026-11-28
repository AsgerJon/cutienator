"""
QQuickMenuBarItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenubaritem_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMenuBarItemPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickAbstractButtonPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
  from ..QtGui import QPalette
  from . import QQuickMenuBar, QQuickMenuBarItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QQuickMenuBar = WAIT['QQuickMenuBar']
  QQuickMenuBarItem = WAIT['QQuickMenuBarItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMenuBarItemPrivate(QQuickAbstractButtonPrivate):
  """
  The cute side of Qt's QQuickMenuBarItemPrivate: a plain Python object
  standing in front of one C++ QQuickMenuBarItemPrivate.

  It is built on the cute 'QQuickAbstractButtonPrivate', as Qt's
  QQuickMenuBarItemPrivate is built on Qt's QQuickAbstractButtonPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMenuBarItemPrivate that has a ritual and that
  Python can call so far, 7 names in all: 'q_func', 'get', 'setMenuBar',
  'handlePress', 'handleRelease', 'defaultPalette', 'accessiblePressAction'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickMenuBarItem *QQuickMenuBarItemPrivate::q_func() const':
    takes in Python what 'QQuickMenuBarItem
    *QQuickMenuBarItemPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickMenuBarItemPrivate is created at the first use, not by
    'QQuickMenuBarItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMenuBarItemPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickMenuBarItem)
  @overload(NoneType)
  def get(
      item: Optional[QQuickMenuBarItem],
  ) -> Optional[QQuickMenuBarItemPrivate]:
    """
    Calls Qt's 'QQuickMenuBarItemPrivate
    *QQuickMenuBarItemPrivate::get(QQuickMenuBarItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenubaritemprivate.html#get

    Parameters
    ----------

    item : Optional[QQuickMenuBarItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickMenuBarItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuBarItemPrivate
    #      *QQuickMenuBarItemPrivate::get(QQuickMenuBarItem *item)
    address = Rituals.call(
        'ritual_ZN24QQuickMenuBarItemPrivate3getEP17QQuickMenuBarItem',
        CuteMixin._addressOf(item),
    )
    return QQuickMenuBarItemPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMenuBarItemPrivate'

  #  A C++ QQuickMenuBarItemPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMenuBarItemPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickMenuBarItemPrivate::defaultPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritemprivate.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickMenuBarItemPrivate::defaultPalette() const
    ritual = 'ritual_ZNK24QQuickMenuBarItemPrivate14defaultPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QQuickMenuBarItemPrivate14defaultPaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickMenuBar)
  @overload(NoneType)
  def setMenuBar(self, menuBar: Optional[QQuickMenuBar]) -> None:
    """
    Calls Qt's 'void QQuickMenuBarItemPrivate::setMenuBar(QQuickMenuBar
    *menuBar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritemprivate.html#setMenuBar

    Parameters
    ----------

    menuBar : Optional[QQuickMenuBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuBarItemPrivate::setMenuBar(QQuickMenuBar *menuBar)
    self.uglySide.call(
        'ritual_ZN24QQuickMenuBarItemPrivate10setMenuBarEP13QQuickMenuBar',
        self._addressOf(menuBar),
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

  def q_func(self) -> Optional[QQuickMenuBarItem]:
    """
    Calls Qt's 'QQuickMenuBarItem *QQuickMenuBarItemPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritemprivate.html#q_func

    Returns
    -------

    Optional[QQuickMenuBarItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuBarItem *QQuickMenuBarItemPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QQuickMenuBarItemPrivate6q_funcEv',
    )
    from . import QQuickMenuBarItem
    return QQuickMenuBarItem._cuteAt(address)

  @overload(QPointF, int)
  def handlePress(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickMenuBarItemPrivate::handlePress(const QPointF
    &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritemprivate.html#handlePress

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickMenuBarItemPrivate::handlePress(const QPointF &point, ulong
    #      timestamp)
    ritual = 'ritual_ZN24QQuickMenuBarItemPrivate11handlePressERK7QPointFm'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickMenuBarItemPrivate11handlePressERK7QPointFm')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  @overload(QPointF, int)
  def handleRelease(self, point: QPointF, timestamp: int) -> bool:
    """
    Calls Qt's 'bool QQuickMenuBarItemPrivate::handleRelease(const QPointF
    &point, ulong timestamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritemprivate.html#handleRelease

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    timestamp : int
      Passed on as it is.
    """
    #  bool QQuickMenuBarItemPrivate::handleRelease(const QPointF &point,
    #      ulong timestamp)
    ritual = 'ritual_ZN24QQuickMenuBarItemPrivate13handleReleaseERK7QPointFm'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickMenuBarItemPrivate13handleReleaseERK7QPoint'
          'Fm')
    return self.uglySide.call(
        ritual, self._valueOf(point, 'QPointF'), timestamp,
    )

  def accessiblePressAction(self) -> None:
    """
    Calls Qt's 'void QQuickMenuBarItemPrivate::accessiblePressAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenubaritemprivate.html
    """
    #  void QQuickMenuBarItemPrivate::accessiblePressAction()
    ritual = 'ritual_ZN24QQuickMenuBarItemPrivate21accessiblePressActionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickMenuBarItemPrivate21accessiblePressActionEv')
    self.uglySide.call(ritual)

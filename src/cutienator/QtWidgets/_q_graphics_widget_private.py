"""
QGraphicsWidgetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicswidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphicsWidgetPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QGraphicsItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QFont, QPalette
  from . import QGraphicsItem, QGraphicsLayout, QGraphicsScene
  from . import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from . import QGraphicsWidget, QStyleOptionTitleBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QGraphicsItem = WAIT['QGraphicsItem']
  QGraphicsLayout = WAIT['QGraphicsLayout']
  QGraphicsScene = WAIT['QGraphicsScene']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QGraphicsWidget = WAIT['QGraphicsWidget']
  QPalette = WAIT['QPalette']
  QStyleOptionTitleBar = WAIT['QStyleOptionTitleBar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsWidgetPrivate(QGraphicsItemPrivate):
  """
  The cute side of Qt's QGraphicsWidgetPrivate: a plain Python object
  standing in front of one C++ QGraphicsWidgetPrivate.

  It is built on the cute 'QGraphicsItemPrivate', as Qt's
  QGraphicsWidgetPrivate is built on Qt's QGraphicsItemPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsWidgetPrivate that has a ritual and that
  Python can call so far, 35 names in all: 'q_func', 'init',
  'titleBarHeight', 'ensureMargins', 'fixFocusChainBeforeReparenting',
  'setLayout_helper', 'setLayoutDirection_helper', 'resolveLayoutDirection',
  'setPalette_helper', 'resolvePalette', 'updatePalette',
  'naturalWidgetPalette', 'setFont_helper', 'resolveFont', 'updateFont',
  'naturalWidgetFont', 'initStyleOptionTitleBar',
  'windowFrameMouseReleaseEvent', 'windowFrameMousePressEvent',
  'windowFrameMouseMoveEvent', 'windowFrameHoverMoveEvent',
  'windowFrameHoverLeaveEvent', 'hasDecoration', 'width', 'setWidth',
  'resetWidth', 'height', 'setHeight', 'resetHeight',
  'setGeometryFromSetPos', 'attributeToBitIndex', 'setAttribute',
  'testAttribute', 'ensureWindowData', 'ensureWindowFrameMargins'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsWidget *QGraphicsWidgetPrivate::q_func() const':
    takes in Python what 'QGraphicsWidget *QGraphicsWidgetPrivate::q_func()'
    takes.
  - Qt's 'QGraphicsWidgetPrivate::~QGraphicsWidgetPrivate()': the destructor:
    Python never removes a C++ QGraphicsWidgetPrivate.
  - Qt's 'void QGraphicsWidgetPrivate::adjustWindowFlags(Qt::WindowFlags
    *wFlags)': names 'Qt::WindowFlags', which has no cute class yet.

  What to expect
  --------------

  - The C++ QGraphicsWidgetPrivate is created at the first use, not by
    'QGraphicsWidgetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsWidgetPrivate.
  - Each name of Qt's QGraphicsWidgetPrivate that has no cute function yet,
    'adjustWindowFlags', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QGraphicsWidgetPrivate, each a class in
  #  here as in C++.

  class WindowData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGraphicsWidgetPrivate::WindowData: a plain Python
    object standing in front of one C++ QGraphicsWidgetPrivate::WindowData.

    C++ hands a QGraphicsWidgetPrivate::WindowData around as a copy, so every
    C++ QGraphicsWidgetPrivate::WindowData behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QGraphicsWidgetPrivate::WindowData yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGraphicsWidgetPrivate::WindowData::~WindowData()': the
      destructor: Python removes its C++ QGraphicsWidgetPrivate::WindowData
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QGraphicsWidgetPrivate::WindowData is created at the first use,
      not by 'QGraphicsWidgetPrivate::WindowData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGraphicsWidgetPrivate::WindowData back gives a
      copy the ritual made for Python, in a new cute
      QGraphicsWidgetPrivate::WindowData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGraphicsWidgetPrivate::WindowData'

    #  Qt's '~QGraphicsWidgetPrivate::WindowData()'. Naming it makes this a
    #  value class: Python owns every C++ QGraphicsWidgetPrivate::WindowData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QGraphicsWidgetPrivate10WindowDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QGraphicsWidgetPrivate::WindowData::WindowData()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qgraphicswidgetprivate-windowdata.html
      """
      #  QGraphicsWidgetPrivate::WindowData::WindowData()
      self._noteCreation(
          QGraphicsWidgetPrivate.WindowData, lambda: Rituals.call(
              'ritual_ZN22QGraphicsWidgetPrivate10WindowDataC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsWidgetPrivate'

  #  A C++ QGraphicsWidgetPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsWidgetPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStyleOptionTitleBar)
  def titleBarHeight(self, options: QStyleOptionTitleBar) -> float:
    """
    Calls Qt's 'qreal QGraphicsWidgetPrivate::titleBarHeight(const
    QStyleOptionTitleBar &options) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#titleBarHeight

    Parameters
    ----------

    options : QStyleOptionTitleBar
      Passed on as a value: Qt reads the C++ QStyleOptionTitleBar, which
      stays Python's own.
    """
    #  qreal QGraphicsWidgetPrivate::titleBarHeight(const
    #      QStyleOptionTitleBar &options) const
    return self.uglySide.call(
        'ritual_ZNK22QGraphicsWidgetPrivate14titleBarHeightERK20QStyleOptio'
        'nTitleBar',
        self._valueOf(options),
    )

  def naturalWidgetPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QGraphicsWidgetPrivate::naturalWidgetPalette()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#naturalWidgetPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QGraphicsWidgetPrivate::naturalWidgetPalette() const
    address = self.uglySide.call(
        'ritual_ZNK22QGraphicsWidgetPrivate20naturalWidgetPaletteEv',
    )
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  def naturalWidgetFont(self) -> QFont:
    """
    Calls Qt's 'QFont QGraphicsWidgetPrivate::naturalWidgetFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#naturalWidgetFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QGraphicsWidgetPrivate::naturalWidgetFont() const
    address = self.uglySide.call(
        'ritual_ZNK22QGraphicsWidgetPrivate17naturalWidgetFontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def hasDecoration(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsWidgetPrivate::hasDecoration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#hasDecoration
    """
    #  bool QGraphicsWidgetPrivate::hasDecoration() const
    return self.uglySide.call(
        'ritual_ZNK22QGraphicsWidgetPrivate13hasDecorationEv',
    )

  def width(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsWidgetPrivate::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#width
    """
    #  qreal QGraphicsWidgetPrivate::width() const
    ritual = 'ritual_ZNK22QGraphicsWidgetPrivate5widthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QGraphicsWidgetPrivate5widthEv'
    return self.uglySide.call(ritual)

  def height(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsWidgetPrivate::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#height
    """
    #  qreal QGraphicsWidgetPrivate::height() const
    ritual = 'ritual_ZNK22QGraphicsWidgetPrivate6heightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QGraphicsWidgetPrivate6heightEv'
    return self.uglySide.call(ritual)

  @overload(Qt.WidgetAttribute)
  def attributeToBitIndex(self, att: Qt.WidgetAttribute) -> int:
    """
    Calls Qt's 'int
    QGraphicsWidgetPrivate::attributeToBitIndex(Qt::WidgetAttribute att)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#attributeToBitIndex

    Parameters
    ----------

    att : Qt.WidgetAttribute
      Passed on as its number.
    """
    #  int QGraphicsWidgetPrivate::attributeToBitIndex(Qt::WidgetAttribute
    #      att) const
    return self.uglySide.call(
        'ritual_ZNK22QGraphicsWidgetPrivate19attributeToBitIndexEN2Qt15Widg'
        'etAttributeE',
        att.value,
    )

  @overload(Qt.WidgetAttribute)
  def testAttribute(self, att: Qt.WidgetAttribute) -> bool:
    """
    Calls Qt's 'bool
    QGraphicsWidgetPrivate::testAttribute(Qt::WidgetAttribute att) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#testAttribute

    Parameters
    ----------

    att : Qt.WidgetAttribute
      Passed on as its number.
    """
    #  bool QGraphicsWidgetPrivate::testAttribute(Qt::WidgetAttribute att)
    #      const
    return self.uglySide.call(
        'ritual_ZNK22QGraphicsWidgetPrivate13testAttributeEN2Qt15WidgetAttr'
        'ibuteE',
        att.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGraphicsLayout)
  @overload(NoneType)
  def setLayout_helper(self, l: Optional[QGraphicsLayout]) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::setLayout_helper(QGraphicsLayout
    *l)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#setLayout_helper

    Parameters
    ----------

    l : Optional[QGraphicsLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidgetPrivate::setLayout_helper(QGraphicsLayout *l)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate16setLayout_helperEP15QGraphicsLa'
        'yout',
        self._addressOf(l),
    )

  @overload(Qt.LayoutDirection)
  def setLayoutDirection_helper(self, direction: Qt.LayoutDirection) -> None:
    """
    Calls Qt's 'void
    QGraphicsWidgetPrivate::setLayoutDirection_helper(Qt::LayoutDirection
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html

    Parameters
    ----------

    direction : Qt.LayoutDirection
      Passed on as its number.
    """
    #  void QGraphicsWidgetPrivate::setLayoutDirection_helper(Qt::
    #      LayoutDirection direction)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate25setLayoutDirection_helperEN2Qt1'
        '5LayoutDirectionE',
        direction.value,
    )

  @overload(QPalette)
  def setPalette_helper(self, palette: QPalette) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::setPalette_helper(const QPalette
    &palette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#setPalette_helper

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QGraphicsWidgetPrivate::setPalette_helper(const QPalette
    #      &palette)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate17setPalette_helperERK8QPalette',
        self._valueOf(palette),
    )

  @overload(QFont)
  def setFont_helper(self, font: QFont) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::setFont_helper(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#setFont_helper

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QGraphicsWidgetPrivate::setFont_helper(const QFont &font)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate14setFont_helperERK5QFont',
        self._valueOf(font),
    )

  @overload(float)
  def setWidth(self, a0: float) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::setWidth(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#setWidth

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QGraphicsWidgetPrivate::setWidth(qreal a0)
    ritual = 'ritual_ZN22QGraphicsWidgetPrivate8setWidthEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QGraphicsWidgetPrivate8setWidthEd'
    self.uglySide.call(ritual, a0)

  @overload(float)
  def setHeight(self, a0: float) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::setHeight(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#setHeight

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QGraphicsWidgetPrivate::setHeight(qreal a0)
    ritual = 'ritual_ZN22QGraphicsWidgetPrivate9setHeightEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QGraphicsWidgetPrivate9setHeightEd'
    self.uglySide.call(ritual, a0)

  def setGeometryFromSetPos(self) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::setGeometryFromSetPos()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#setGeometryFromSetPos
    """
    #  void QGraphicsWidgetPrivate::setGeometryFromSetPos()
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate21setGeometryFromSetPosEv',
    )

  @overload(Qt.WidgetAttribute, bool)
  def setAttribute(self, att: Qt.WidgetAttribute, value: bool) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::setAttribute(Qt::WidgetAttribute
    att, bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#setAttribute

    Parameters
    ----------

    att : Qt.WidgetAttribute
      Passed on as its number.

    value : bool
      Passed on as it is.
    """
    #  void QGraphicsWidgetPrivate::setAttribute(Qt::WidgetAttribute att,
    #      bool value)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate12setAttributeEN2Qt15WidgetAttrib'
        'uteEb',
        att.value, value,
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
    'QGraphicsWidgetPrivate::QGraphicsWidgetPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#QGraphicsWidgetPrivate
    """
    #  QGraphicsWidgetPrivate::QGraphicsWidgetPrivate()
    self._noteCreation(QGraphicsWidgetPrivate, lambda: Rituals.call(
        'ritual_ZN22QGraphicsWidgetPrivateC1Ev',
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

  def q_func(self) -> Optional[QGraphicsWidget]:
    """
    Calls Qt's 'QGraphicsWidget *QGraphicsWidgetPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsWidget *QGraphicsWidgetPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate6q_funcEv',
    )
    from . import QGraphicsWidget
    return QGraphicsWidget._cuteAt(address)

  @overload(QGraphicsItem, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def init(
      self,
      parentItem: Optional[QGraphicsItem],
      wFlags: Qt.WindowFlags,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::init(QGraphicsItem *parentItem,
    Qt::WindowFlags wFlags)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#init

    Parameters
    ----------

    parentItem : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    wFlags : Qt.WindowFlags
      Passed on as its number.
    """
    #  void QGraphicsWidgetPrivate::init(QGraphicsItem *parentItem,
    #      Qt::WindowFlags wFlags)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate4initEP13QGraphicsItem6QFlagsIN2Q'
        't10WindowTypeEE',
        self._addressOf(parentItem, 'QGraphicsItem'), wFlags.value,
    )

  def ensureMargins(self) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::ensureMargins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#ensureMargins
    """
    #  void QGraphicsWidgetPrivate::ensureMargins() const
    self.uglySide.call('ritual_ZNK22QGraphicsWidgetPrivate13ensureMarginsEv')

  @overload(QGraphicsWidget, QGraphicsScene)
  @overload(QGraphicsWidget, NoneType)
  @overload(NoneType, QGraphicsScene)
  @overload(NoneType, NoneType)
  @overload(QGraphicsWidget, QGraphicsScene, QGraphicsScene)
  @overload(QGraphicsWidget, QGraphicsScene, NoneType)
  @overload(QGraphicsWidget, NoneType, QGraphicsScene)
  @overload(QGraphicsWidget, NoneType, NoneType)
  @overload(NoneType, QGraphicsScene, QGraphicsScene)
  @overload(NoneType, QGraphicsScene, NoneType)
  @overload(NoneType, NoneType, QGraphicsScene)
  @overload(NoneType, NoneType, NoneType)
  def fixFocusChainBeforeReparenting(
      self,
      newParent: Optional[QGraphicsWidget],
      oldScene: Optional[QGraphicsScene],
      newScene: Optional[QGraphicsScene] = None,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsWidgetPrivate::fixFocusChainBeforeReparenting(QGraphicsWidget
    *newParent, QGraphicsScene *oldScene, QGraphicsScene *newScene)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html

    Parameters
    ----------

    newParent : Optional[QGraphicsWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldScene : Optional[QGraphicsScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newScene : Optional[QGraphicsScene]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QGraphicsWidgetPrivate::fixFocusChainBeforeReparenting(
    #      QGraphicsWidget *newParent, QGraphicsScene *oldScene,
    #      QGraphicsScene *newScene)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate30fixFocusChainBeforeReparentingE'
        'P15QGraphicsWidgetP14QGraphicsSceneS3_',
        self._addressOf(newParent), self._addressOf(oldScene),
        self._addressOf(newScene),
    )

  def resolveLayoutDirection(self) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::resolveLayoutDirection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#resolveLayoutDirection
    """
    #  void QGraphicsWidgetPrivate::resolveLayoutDirection()
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate22resolveLayoutDirectionEv',
    )

  @overload(int)
  def resolvePalette(self, inheritedMask: int) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::resolvePalette(uint
    inheritedMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#resolvePalette

    Parameters
    ----------

    inheritedMask : int
      Passed on as it is.
    """
    #  void QGraphicsWidgetPrivate::resolvePalette(uint inheritedMask)
    ritual = 'ritual_ZN22QGraphicsWidgetPrivate14resolvePaletteEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QGraphicsWidgetPrivate14resolvePaletteEj'
    self.uglySide.call(ritual, inheritedMask)

  @overload(QPalette)
  def updatePalette(self, palette: QPalette) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::updatePalette(const QPalette
    &palette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#updatePalette

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QGraphicsWidgetPrivate::updatePalette(const QPalette &palette)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate13updatePaletteERK8QPalette',
        self._valueOf(palette),
    )

  @overload(int)
  def resolveFont(self, inheritedMask: int) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::resolveFont(uint
    inheritedMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#resolveFont

    Parameters
    ----------

    inheritedMask : int
      Passed on as it is.
    """
    #  void QGraphicsWidgetPrivate::resolveFont(uint inheritedMask)
    ritual = 'ritual_ZN22QGraphicsWidgetPrivate11resolveFontEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QGraphicsWidgetPrivate11resolveFontEj'
    self.uglySide.call(ritual, inheritedMask)

  @overload(QFont)
  def updateFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::updateFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#updateFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QGraphicsWidgetPrivate::updateFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate10updateFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QStyleOptionTitleBar)
  @overload(NoneType)
  def initStyleOptionTitleBar(
      self,
      option: Optional[QStyleOptionTitleBar],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsWidgetPrivate::initStyleOptionTitleBar(QStyleOptionTitleBar
    *option)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html

    Parameters
    ----------

    option : Optional[QStyleOptionTitleBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidgetPrivate::initStyleOptionTitleBar(
    #      QStyleOptionTitleBar *option)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate23initStyleOptionTitleBarEP20QSty'
        'leOptionTitleBar',
        self._addressOf(option),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def windowFrameMouseReleaseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::windowFrameMouseReleaseEvent(
    QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidgetPrivate::windowFrameMouseReleaseEvent(
    #      QGraphicsSceneMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate28windowFrameMouseReleaseEventEP2'
        '4QGraphicsSceneMouseEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def windowFrameMousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::windowFrameMousePressEvent(
    QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidgetPrivate::windowFrameMousePressEvent(
    #      QGraphicsSceneMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate26windowFrameMousePressEventEP24Q'
        'GraphicsSceneMouseEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def windowFrameMouseMoveEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::windowFrameMouseMoveEvent(
    QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidgetPrivate::windowFrameMouseMoveEvent(
    #      QGraphicsSceneMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate25windowFrameMouseMoveEventEP24QG'
        'raphicsSceneMouseEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def windowFrameHoverMoveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::windowFrameHoverMoveEvent(
    QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidgetPrivate::windowFrameHoverMoveEvent(
    #      QGraphicsSceneHoverEvent *event)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate25windowFrameHoverMoveEventEP24QG'
        'raphicsSceneHoverEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def windowFrameHoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::windowFrameHoverLeaveEvent(
    QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsWidgetPrivate::windowFrameHoverLeaveEvent(
    #      QGraphicsSceneHoverEvent *event)
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate26windowFrameHoverLeaveEventEP24Q'
        'GraphicsSceneHoverEvent',
        self._addressOf(event),
    )

  def resetWidth(self) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::resetWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#resetWidth
    """
    #  void QGraphicsWidgetPrivate::resetWidth()
    ritual = 'ritual_ZN22QGraphicsWidgetPrivate10resetWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QGraphicsWidgetPrivate10resetWidthEv'
    self.uglySide.call(ritual)

  def resetHeight(self) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::resetHeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#resetHeight
    """
    #  void QGraphicsWidgetPrivate::resetHeight()
    ritual = 'ritual_ZN22QGraphicsWidgetPrivate11resetHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QGraphicsWidgetPrivate11resetHeightEv'
    self.uglySide.call(ritual)

  def ensureWindowData(self) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::ensureWindowData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html#ensureWindowData
    """
    #  void QGraphicsWidgetPrivate::ensureWindowData()
    self.uglySide.call(
        'ritual_ZN22QGraphicsWidgetPrivate16ensureWindowDataEv',
    )

  def ensureWindowFrameMargins(self) -> None:
    """
    Calls Qt's 'void QGraphicsWidgetPrivate::ensureWindowFrameMargins()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicswidgetprivate.html
    """
    #  void QGraphicsWidgetPrivate::ensureWindowFrameMargins() const
    self.uglySide.call(
        'ritual_ZNK22QGraphicsWidgetPrivate24ensureWindowFrameMarginsEv',
    )

  @staticmethod
  def adjustWindowFlags(*__, **_) -> Never:
    """
    Qt's 'void QGraphicsWidgetPrivate::adjustWindowFlags(Qt::WindowFlags
    *wFlags)': names 'Qt::WindowFlags', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QGraphicsWidgetPrivate.adjustWindowFlags' has no cute function "
        "yet. Qt's 'void "
        "QGraphicsWidgetPrivate::adjustWindowFlags(Qt::WindowFlags "
        "*wFlags)': names 'Qt::WindowFlags', which has no cute class yet.")

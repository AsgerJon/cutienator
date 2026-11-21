"""
QBoxLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qboxlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QLayout

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect, QSize
  from . import QLayoutItem, QSpacerItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLayoutItem = WAIT['QLayoutItem']
  QRect = WAIT['QRect']
  QSpacerItem = WAIT['QSpacerItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBoxLayout(QLayout):
  """
  The cute side of Qt's QBoxLayout: a plain Python object standing in front
  of one C++ QBoxLayout.

  It is built on the cute 'QLayout', as Qt's QBoxLayout is built on Qt's
  QLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBoxLayout that has a ritual and that Python can
  call so far, 34 names in all: 'metaObject', 'tr', 'direction',
  'setDirection', 'addSpacing', 'addStretch', 'addSpacerItem', 'addWidget',
  'addLayout', 'addStrut', 'addItem', 'insertSpacing', 'insertStretch',
  'insertSpacerItem', 'insertWidget', 'insertLayout', 'insertItem',
  'spacing', 'setSpacing', 'setStretchFactor', 'setStretch', 'stretch',
  'sizeHint', 'minimumSize', 'maximumSize', 'hasHeightForWidth',
  'heightForWidth', 'minimumHeightForWidth', 'expandingDirections',
  'invalidate', 'itemAt', 'takeAt', 'count', 'setGeometry'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBoxLayout::~QBoxLayout()': the destructor: Python never removes a
    C++ QBoxLayout.

  What has no ritual
  ------------------

  8 of the 45 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QBoxLayout is created at the first use, not by 'QBoxLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBoxLayout.
  - Qt tells when it has removed the C++ QBoxLayout. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QBoxLayout, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Direction(CuteNum):
    """
    The enum 'QBoxLayout::Direction' of Qt, with the 6 names Qt gives in it.
    """

    LeftToRight = Kee[int](0)
    RightToLeft = Kee[int](1)
    TopToBottom = Kee[int](2)
    BottomToTop = Kee[int](3)
    Down = Kee[int](2)
    Up = Kee[int](3)

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
    Calls Qt's 'QString QBoxLayout::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#tr

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
    #  QString QBoxLayout::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QBoxLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBoxLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBoxLayout::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBoxLayout::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QBoxLayout10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def direction(self) -> Direction:
    """
    Calls Qt's 'Direction QBoxLayout::direction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#direction

    Returns
    -------

    Direction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Direction(number)' gives.
    """
    #  Direction QBoxLayout::direction() const
    return QBoxLayout.Direction(self.uglySide.call(
        'ritual_ZNK10QBoxLayout9directionEv',
    ))

  def spacing(self) -> int:
    """
    Calls Qt's 'int QBoxLayout::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#spacing
    """
    #  int QBoxLayout::spacing() const
    return self.uglySide.call('ritual_ZNK10QBoxLayout7spacingEv')

  @overload(int)
  def stretch(self, index: int) -> int:
    """
    Calls Qt's 'int QBoxLayout::stretch(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#stretch

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QBoxLayout::stretch(int index) const
    return self.uglySide.call('ritual_ZNK10QBoxLayout7stretchEi', index)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QBoxLayout::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QBoxLayout::sizeHint() const
    address = self.uglySide.call('ritual_ZNK10QBoxLayout8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QBoxLayout::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QBoxLayout::minimumSize() const
    address = self.uglySide.call('ritual_ZNK10QBoxLayout11minimumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def maximumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QBoxLayout::maximumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#maximumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QBoxLayout::maximumSize() const
    address = self.uglySide.call('ritual_ZNK10QBoxLayout11maximumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def hasHeightForWidth(self) -> bool:
    """
    Calls Qt's 'bool QBoxLayout::hasHeightForWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#hasHeightForWidth
    """
    #  bool QBoxLayout::hasHeightForWidth() const
    return self.uglySide.call('ritual_ZNK10QBoxLayout17hasHeightForWidthEv')

  @overload(int)
  def heightForWidth(self, a0: int) -> int:
    """
    Calls Qt's 'int QBoxLayout::heightForWidth(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#heightForWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QBoxLayout::heightForWidth(int a0) const
    return self.uglySide.call('ritual_ZNK10QBoxLayout14heightForWidthEi', a0)

  @overload(int)
  def minimumHeightForWidth(self, a0: int) -> int:
    """
    Calls Qt's 'int QBoxLayout::minimumHeightForWidth(int a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxlayout.html#minimumHeightForWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QBoxLayout::minimumHeightForWidth(int a0) const
    return self.uglySide.call(
        'ritual_ZNK10QBoxLayout21minimumHeightForWidthEi', a0,
    )

  def expandingDirections(self) -> Qt.Orientations:
    """
    Calls Qt's 'Qt::Orientations QBoxLayout::expandingDirections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qboxlayout.html#expandingDirections

    Returns
    -------

    Qt.Orientations
      The value standing for the combination Qt gave back.
    """
    #  Qt::Orientations QBoxLayout::expandingDirections() const
    return Qt.Orientations(self.uglySide.call(
        'ritual_ZNK10QBoxLayout19expandingDirectionsEv',
    ))

  @overload(int)
  def itemAt(self, a0: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QBoxLayout::itemAt(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#itemAt

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QBoxLayout::itemAt(int a0) const
    address = self.uglySide.call('ritual_ZNK10QBoxLayout6itemAtEi', a0)
    from . import QLayoutItem
    return QLayoutItem._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QBoxLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#count
    """
    #  int QBoxLayout::count() const
    return self.uglySide.call('ritual_ZNK10QBoxLayout5countEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Direction)
  def setDirection(self, a0: Direction) -> None:
    """
    Calls Qt's 'void QBoxLayout::setDirection(Direction a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#setDirection

    Parameters
    ----------

    a0 : Direction
      Passed on as its number.
    """
    #  void QBoxLayout::setDirection(Direction a0)
    self.uglySide.call(
        'ritual_ZN10QBoxLayout12setDirectionENS_9DirectionE', a0.value,
    )

  @overload(int)
  def setSpacing(self, spacing: int) -> None:
    """
    Calls Qt's 'void QBoxLayout::setSpacing(int spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#setSpacing

    Parameters
    ----------

    spacing : int
      Passed on as it is.
    """
    #  void QBoxLayout::setSpacing(int spacing)
    self.uglySide.call('ritual_ZN10QBoxLayout10setSpacingEi', spacing)

  @overload(QWidget, int)
  @overload(NoneType, int)
  def setStretchFactor(self, w: Optional[QWidget], stretch: int) -> bool:
    """
    Calls Qt's 'bool QBoxLayout::setStretchFactor(QWidget *w, int stretch)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#setStretchFactor

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretch : int
      Passed on as it is.
    """
    #  bool QBoxLayout::setStretchFactor(QWidget *w, int stretch)
    return self.uglySide.call(
        'ritual_ZN10QBoxLayout16setStretchFactorEP7QWidgeti',
        self._addressOf(w), stretch,
    )

  @overload(QLayout, int)
  def setStretchFactor(self, l: Optional[QLayout], stretch: int) -> bool:
    """
    Calls Qt's 'bool QBoxLayout::setStretchFactor(QLayout *l, int stretch)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#setStretchFactor

    Parameters
    ----------

    l : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretch : int
      Passed on as it is.
    """
    #  bool QBoxLayout::setStretchFactor(QLayout *l, int stretch)
    return self.uglySide.call(
        'ritual_ZN10QBoxLayout16setStretchFactorEP7QLayouti',
        self._addressOf(l), stretch,
    )

  @overload(int, int)
  def setStretch(self, index: int, stretch: int) -> None:
    """
    Calls Qt's 'void QBoxLayout::setStretch(int index, int stretch)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#setStretch

    Parameters
    ----------

    index : int
      Passed on as it is.

    stretch : int
      Passed on as it is.
    """
    #  void QBoxLayout::setStretch(int index, int stretch)
    self.uglySide.call(
        'ritual_ZN10QBoxLayout10setStretchEii', index, stretch,
    )

  @overload(QRect)
  def setGeometry(self, a0: QRect) -> None:
    """
    Calls Qt's 'void QBoxLayout::setGeometry(const QRect &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#setGeometry

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QBoxLayout::setGeometry(const QRect &a0)
    self.uglySide.call(
        'ritual_ZN10QBoxLayout11setGeometryERK5QRect', self._valueOf(a0),
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

  @overload(Direction)
  @overload(Direction, QWidget)
  @overload(Direction, NoneType)
  def __init__(
      self,
      a0: Direction,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QBoxLayout::QBoxLayout(Direction a0,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#QBoxLayout

    Parameters
    ----------

    a0 : Direction
      Passed on as its number.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QBoxLayout::QBoxLayout(Direction a0, QWidget *parent)
    self._noteCreation(QBoxLayout, lambda: Rituals.call(
        'ritual_ZN10QBoxLayoutC1ENS_9DirectionEP7QWidget',
        a0.value, self._addressOf(parent),
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

  @overload(int)
  def addSpacing(self, size: int) -> None:
    """
    Calls Qt's 'void QBoxLayout::addSpacing(int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#addSpacing

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QBoxLayout::addSpacing(int size)
    self.uglySide.call('ritual_ZN10QBoxLayout10addSpacingEi', size)

  @overload()
  @overload(int)
  def addStretch(self, stretch: int = 0) -> None:
    """
    Calls Qt's 'void QBoxLayout::addStretch(int stretch)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#addStretch

    Parameters
    ----------

    stretch : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QBoxLayout::addStretch(int stretch)
    self.uglySide.call('ritual_ZN10QBoxLayout10addStretchEi', stretch)

  @overload(QSpacerItem)
  @overload(NoneType)
  def addSpacerItem(self, spacerItem: Optional[QSpacerItem]) -> None:
    """
    Calls Qt's 'void QBoxLayout::addSpacerItem(QSpacerItem *spacerItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#addSpacerItem

    Parameters
    ----------

    spacerItem : Optional[QSpacerItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxLayout::addSpacerItem(QSpacerItem *spacerItem)
    self.uglySide.call(
        'ritual_ZN10QBoxLayout13addSpacerItemEP11QSpacerItem',
        self._addressOf(spacerItem),
    )

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, int)
  @overload(NoneType, int)
  @overload(QWidget, int, Qt.Alignment)
  @overload(NoneType, int, Qt.Alignment)
  def addWidget(
      self,
      a0: Optional[QWidget],
      stretch: int = 0,
      alignment: Qt.Alignment = Qt.Alignment(),
  ) -> None:
    """
    Calls Qt's 'void QBoxLayout::addWidget(QWidget *a0, int stretch,
    Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#addWidget

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretch : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    alignment : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment().
    """
    #  void QBoxLayout::addWidget(QWidget *a0, int stretch, Qt::Alignment
    #      alignment)
    self.uglySide.call(
        'ritual_ZN10QBoxLayout9addWidgetEP7QWidgeti6QFlagsIN2Qt13AlignmentF'
        'lagEE',
        self._addressOf(a0), stretch, alignment.value,
    )

  @overload(QLayout)
  @overload(NoneType)
  @overload(QLayout, int)
  @overload(NoneType, int)
  def addLayout(self, layout: Optional[QLayout], stretch: int = 0) -> None:
    """
    Calls Qt's 'void QBoxLayout::addLayout(QLayout *layout, int stretch)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#addLayout

    Parameters
    ----------

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretch : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QBoxLayout::addLayout(QLayout *layout, int stretch)
    self.uglySide.call(
        'ritual_ZN10QBoxLayout9addLayoutEP7QLayouti',
        self._addressOf(layout), stretch,
    )

  @overload(int)
  def addStrut(self, a0: int) -> None:
    """
    Calls Qt's 'void QBoxLayout::addStrut(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#addStrut

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QBoxLayout::addStrut(int a0)
    self.uglySide.call('ritual_ZN10QBoxLayout8addStrutEi', a0)

  @overload(QLayoutItem)
  @overload(NoneType)
  def addItem(self, a0: Optional[QLayoutItem]) -> None:
    """
    Calls Qt's 'void QBoxLayout::addItem(QLayoutItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#addItem

    Parameters
    ----------

    a0 : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxLayout::addItem(QLayoutItem *a0)
    self.uglySide.call(
        'ritual_ZN10QBoxLayout7addItemEP11QLayoutItem', self._addressOf(a0),
    )

  @overload(int, int)
  def insertSpacing(self, index: int, size: int) -> None:
    """
    Calls Qt's 'void QBoxLayout::insertSpacing(int index, int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#insertSpacing

    Parameters
    ----------

    index : int
      Passed on as it is.

    size : int
      Passed on as it is.
    """
    #  void QBoxLayout::insertSpacing(int index, int size)
    self.uglySide.call(
        'ritual_ZN10QBoxLayout13insertSpacingEii', index, size,
    )

  @overload(int)
  @overload(int, int)
  def insertStretch(self, index: int, stretch: int = 0) -> None:
    """
    Calls Qt's 'void QBoxLayout::insertStretch(int index, int stretch)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#insertStretch

    Parameters
    ----------

    index : int
      Passed on as it is.

    stretch : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QBoxLayout::insertStretch(int index, int stretch)
    self.uglySide.call(
        'ritual_ZN10QBoxLayout13insertStretchEii', index, stretch,
    )

  @overload(int, QSpacerItem)
  @overload(int, NoneType)
  def insertSpacerItem(
      self,
      index: int,
      spacerItem: Optional[QSpacerItem],
  ) -> None:
    """
    Calls Qt's 'void QBoxLayout::insertSpacerItem(int index, QSpacerItem
    *spacerItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#insertSpacerItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    spacerItem : Optional[QSpacerItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxLayout::insertSpacerItem(int index, QSpacerItem *spacerItem)
    self.uglySide.call(
        'ritual_ZN10QBoxLayout16insertSpacerItemEiP11QSpacerItem',
        index, self._addressOf(spacerItem),
    )

  @overload(int, QWidget)
  @overload(int, NoneType)
  @overload(int, QWidget, int)
  @overload(int, NoneType, int)
  @overload(int, QWidget, int, Qt.Alignment)
  @overload(int, NoneType, int, Qt.Alignment)
  def insertWidget(
      self,
      index: int,
      widget: Optional[QWidget],
      stretch: int = 0,
      alignment: Qt.Alignment = Qt.Alignment(),
  ) -> None:
    """
    Calls Qt's 'void QBoxLayout::insertWidget(int index, QWidget *widget, int
    stretch, Qt::Alignment alignment)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#insertWidget

    Parameters
    ----------

    index : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretch : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    alignment : Qt.Alignment
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Alignment().
    """
    #  void QBoxLayout::insertWidget(int index, QWidget *widget, int stretch,
    #      Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN10QBoxLayout12insertWidgetEiP7QWidgeti6QFlagsIN2Qt13Align'
        'mentFlagEE',
        index, self._addressOf(widget), stretch, alignment.value,
    )

  @overload(int, QLayout)
  @overload(int, NoneType)
  @overload(int, QLayout, int)
  @overload(int, NoneType, int)
  def insertLayout(
      self,
      index: int,
      layout: Optional[QLayout],
      stretch: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QBoxLayout::insertLayout(int index, QLayout *layout, int
    stretch)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#insertLayout

    Parameters
    ----------

    index : int
      Passed on as it is.

    layout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretch : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QBoxLayout::insertLayout(int index, QLayout *layout, int stretch)
    self.uglySide.call(
        'ritual_ZN10QBoxLayout12insertLayoutEiP7QLayouti',
        index, self._addressOf(layout), stretch,
    )

  @overload(int, QLayoutItem)
  @overload(int, NoneType)
  def insertItem(self, index: int, a1: Optional[QLayoutItem]) -> None:
    """
    Calls Qt's 'void QBoxLayout::insertItem(int index, QLayoutItem *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#insertItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    a1 : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBoxLayout::insertItem(int index, QLayoutItem *a1)
    self.uglySide.call(
        'ritual_ZN10QBoxLayout10insertItemEiP11QLayoutItem',
        index, self._addressOf(a1),
    )

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QBoxLayout::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#invalidate
    """
    #  void QBoxLayout::invalidate()
    self.uglySide.call('ritual_ZN10QBoxLayout10invalidateEv')

  @overload(int)
  def takeAt(self, a0: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QBoxLayout::takeAt(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qboxlayout.html#takeAt

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QLayoutItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLayoutItem *QBoxLayout::takeAt(int a0)
    address = self.uglySide.call('ritual_ZN10QBoxLayout6takeAtEi', a0)
    from . import QLayoutItem
    return QLayoutItem._cuteAt(address)

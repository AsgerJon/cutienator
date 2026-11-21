"""
QStackedLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qstackedlayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QLayout

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRect, QSize
  from . import QLayoutItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLayoutItem = WAIT['QLayoutItem']
  QRect = WAIT['QRect']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStackedLayout(QLayout):
  """
  The cute side of Qt's QStackedLayout: a plain Python object standing in
  front of one C++ QStackedLayout.

  It is built on the cute 'QLayout', as Qt's QStackedLayout is built on Qt's
  QLayout, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStackedLayout that has a ritual and that Python can
  call so far, 20 names in all: 'metaObject', 'tr', 'addWidget',
  'insertWidget', 'currentWidget', 'currentIndex', 'widget', 'count',
  'stackingMode', 'setStackingMode', 'addItem', 'sizeHint', 'minimumSize',
  'itemAt', 'takeAt', 'setGeometry', 'hasHeightForWidth', 'heightForWidth',
  'setCurrentIndex', 'setCurrentWidget'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QStackedLayout::~QStackedLayout()': the destructor: Python never
    removes a C++ QStackedLayout.

  What has no ritual
  ------------------

  11 of the 35 functions Qt declares: 3 private; 3 a signal; 2 takes or gives
  a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QStackedLayout is created at the first use, not by
    'QStackedLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStackedLayout.
  - Qt tells when it has removed the C++ QStackedLayout. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QStackedLayout, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class StackingMode(CuteNum):
    """
    The enum 'QStackedLayout::StackingMode' of Qt, with the 2 names Qt gives
    in it.
    """

    StackOne = Kee[int](0)
    StackAll = Kee[int](1)

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
    Calls Qt's 'QString QStackedLayout::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#tr

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
    #  QString QStackedLayout::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QStackedLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStackedLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStackedLayout::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStackedLayout::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QStackedLayout10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QStackedLayout::currentWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#currentWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QStackedLayout::currentWidget() const
    address = self.uglySide.call(
        'ritual_ZNK14QStackedLayout13currentWidgetEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QStackedLayout::currentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#currentIndex
    """
    #  int QStackedLayout::currentIndex() const
    return self.uglySide.call('ritual_ZNK14QStackedLayout12currentIndexEv')

  @overload(int)
  def widget(self, a0: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QStackedLayout::widget(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#widget

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QStackedLayout::widget(int a0) const
    address = self.uglySide.call('ritual_ZNK14QStackedLayout6widgetEi', a0)
    from . import QWidget
    return QWidget._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QStackedLayout::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#count
    """
    #  int QStackedLayout::count() const
    return self.uglySide.call('ritual_ZNK14QStackedLayout5countEv')

  def stackingMode(self) -> StackingMode:
    """
    Calls Qt's 'StackingMode QStackedLayout::stackingMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#stackingMode

    Returns
    -------

    StackingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StackingMode(number)'
      gives.
    """
    #  StackingMode QStackedLayout::stackingMode() const
    return QStackedLayout.StackingMode(self.uglySide.call(
        'ritual_ZNK14QStackedLayout12stackingModeEv',
    ))

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QStackedLayout::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QStackedLayout::sizeHint() const
    address = self.uglySide.call('ritual_ZNK14QStackedLayout8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSize(self) -> QSize:
    """
    Calls Qt's 'QSize QStackedLayout::minimumSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#minimumSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QStackedLayout::minimumSize() const
    address = self.uglySide.call('ritual_ZNK14QStackedLayout11minimumSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int)
  def itemAt(self, a0: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QStackedLayout::itemAt(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#itemAt

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
    #  QLayoutItem *QStackedLayout::itemAt(int a0) const
    address = self.uglySide.call('ritual_ZNK14QStackedLayout6itemAtEi', a0)
    from . import QLayoutItem
    return QLayoutItem._cuteAt(address)

  def hasHeightForWidth(self) -> bool:
    """
    Calls Qt's 'bool QStackedLayout::hasHeightForWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedlayout.html#hasHeightForWidth
    """
    #  bool QStackedLayout::hasHeightForWidth() const
    return self.uglySide.call(
        'ritual_ZNK14QStackedLayout17hasHeightForWidthEv',
    )

  @overload(int)
  def heightForWidth(self, width: int) -> int:
    """
    Calls Qt's 'int QStackedLayout::heightForWidth(int width) const'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#heightForWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  int QStackedLayout::heightForWidth(int width) const
    return self.uglySide.call(
        'ritual_ZNK14QStackedLayout14heightForWidthEi', width,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(StackingMode)
  def setStackingMode(self, stackingMode: StackingMode) -> None:
    """
    Calls Qt's 'void QStackedLayout::setStackingMode(StackingMode
    stackingMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedlayout.html#setStackingMode

    Parameters
    ----------

    stackingMode : StackingMode
      Passed on as its number.
    """
    #  void QStackedLayout::setStackingMode(StackingMode stackingMode)
    self.uglySide.call(
        'ritual_ZN14QStackedLayout15setStackingModeENS_12StackingModeE',
        stackingMode.value,
    )

  @overload(QRect)
  def setGeometry(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QStackedLayout::setGeometry(const QRect &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#setGeometry

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QStackedLayout::setGeometry(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN14QStackedLayout11setGeometryERK5QRect',
        self._valueOf(rect),
    )

  @overload(int)
  def setCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QStackedLayout::setCurrentIndex(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedlayout.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QStackedLayout::setCurrentIndex(int index)
    self.uglySide.call('ritual_ZN14QStackedLayout15setCurrentIndexEi', index)

  @overload(QWidget)
  @overload(NoneType)
  def setCurrentWidget(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QStackedLayout::setCurrentWidget(QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedlayout.html#setCurrentWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStackedLayout::setCurrentWidget(QWidget *w)
    self.uglySide.call(
        'ritual_ZN14QStackedLayout16setCurrentWidgetEP7QWidget',
        self._addressOf(w),
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
    Notes what was given, for Qt's 'QStackedLayout::QStackedLayout()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#QStackedLayout
    """
    #  QStackedLayout::QStackedLayout()
    self._noteCreation(QStackedLayout, lambda: Rituals.call(
        'ritual_ZN14QStackedLayoutC1Ev',
    ))

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's 'QStackedLayout::QStackedLayout(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#QStackedLayout

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QStackedLayout::QStackedLayout(QWidget *parent)
    self._noteCreation(QStackedLayout, lambda: Rituals.call(
        'ritual_ZN14QStackedLayoutC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(QLayout)
  def __init__(self, parentLayout: Optional[QLayout]) -> None:
    """
    Notes what was given, for Qt's 'QStackedLayout::QStackedLayout(QLayout
    *parentLayout)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#QStackedLayout

    Parameters
    ----------

    parentLayout : Optional[QLayout]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QStackedLayout::QStackedLayout(QLayout *parentLayout)
    self._noteCreation(QStackedLayout, lambda: Rituals.call(
        'ritual_ZN14QStackedLayoutC1EP7QLayout',
        self._addressOf(parentLayout),
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

  @overload(QWidget)
  @overload(NoneType)
  def addWidget(self, w: Optional[QWidget]) -> int:
    """
    Calls Qt's 'int QStackedLayout::addWidget(QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#addWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QStackedLayout::addWidget(QWidget *w)
    return self.uglySide.call(
        'ritual_ZN14QStackedLayout9addWidgetEP7QWidget', self._addressOf(w),
    )

  @overload(int, QWidget)
  @overload(int, NoneType)
  def insertWidget(self, index: int, w: Optional[QWidget]) -> int:
    """
    Calls Qt's 'int QStackedLayout::insertWidget(int index, QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#insertWidget

    Parameters
    ----------

    index : int
      Passed on as it is.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QStackedLayout::insertWidget(int index, QWidget *w)
    return self.uglySide.call(
        'ritual_ZN14QStackedLayout12insertWidgetEiP7QWidget',
        index, self._addressOf(w),
    )

  @overload(QLayoutItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QLayoutItem]) -> None:
    """
    Calls Qt's 'void QStackedLayout::addItem(QLayoutItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#addItem

    Parameters
    ----------

    item : Optional[QLayoutItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStackedLayout::addItem(QLayoutItem *item)
    self.uglySide.call(
        'ritual_ZN14QStackedLayout7addItemEP11QLayoutItem',
        self._addressOf(item),
    )

  @overload(int)
  def takeAt(self, a0: int) -> Optional[QLayoutItem]:
    """
    Calls Qt's 'QLayoutItem *QStackedLayout::takeAt(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedlayout.html#takeAt

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
    #  QLayoutItem *QStackedLayout::takeAt(int a0)
    address = self.uglySide.call('ritual_ZN14QStackedLayout6takeAtEi', a0)
    from . import QLayoutItem
    return QLayoutItem._cuteAt(address)

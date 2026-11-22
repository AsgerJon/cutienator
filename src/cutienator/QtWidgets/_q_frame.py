"""
QFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qframe.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRect, QSize
  from ..QtGui import QPaintEvent
  from . import QStyleOptionFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QRect = WAIT['QRect']
  QStyleOptionFrame = WAIT['QStyleOptionFrame']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFrame(QWidget):
  """
  The cute side of Qt's QFrame: a plain Python object standing in front of
  one C++ QFrame.

  It is built on the cute 'QWidget', as Qt's QFrame is built on Qt's QWidget,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFrame that has a ritual and that Python can call so
  far, 20 names in all: 'metaObject', 'tr', 'frameStyle', 'setFrameStyle',
  'frameWidth', 'sizeHint', 'frameShape', 'setFrameShape', 'frameShadow',
  'setFrameShadow', 'lineWidth', 'setLineWidth', 'midLineWidth',
  'setMidLineWidth', 'frameRect', 'setFrameRect', 'event', 'paintEvent',
  'changeEvent', 'initStyleOption'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFrame::~QFrame()': the destructor: Python never removes a C++
    QFrame.

  What has no ritual
  ------------------

  10 of the 32 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 protected; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QFrame is created at the first use, not by 'QFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFrame.
  - Qt tells when it has removed the C++ QFrame. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QFrame, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Shadow(CuteNum):
    """The enum 'QFrame::Shadow' of Qt, with the 3 names Qt gives in it."""

    Plain = Kee[int](16)
    Raised = Kee[int](32)
    Sunken = Kee[int](48)

  class Shape(CuteNum):
    """The enum 'QFrame::Shape' of Qt, with the 7 names Qt gives in it."""

    NoFrame = Kee[int](0)
    Box = Kee[int](1)
    Panel = Kee[int](2)
    WinPanel = Kee[int](3)
    HLine = Kee[int](4)
    VLine = Kee[int](5)
    StyledPanel = Kee[int](6)

  class StyleMask(CuteNum):
    """
    The enum 'QFrame::StyleMask' of Qt, with the 2 names Qt gives in it.
    """

    Shadow_Mask = Kee[int](240)
    Shape_Mask = Kee[int](15)

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
    Calls Qt's 'QString QFrame::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#tr

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
    #  QString QFrame::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN6QFrame2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFrame'

  #  A C++ QFrame Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFrame'

  #  The functions Qt calls itself that QFrame is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initStyleOption': (
          ('_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionFrame'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFrame::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFrame::metaObject() const
    address = self.uglySide.call('ritual_ZNK6QFrame10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def frameStyle(self) -> int:
    """
    Calls Qt's 'int QFrame::frameStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#frameStyle
    """
    #  int QFrame::frameStyle() const
    return self.uglySide.call('ritual_ZNK6QFrame10frameStyleEv')

  def frameWidth(self) -> int:
    """
    Calls Qt's 'int QFrame::frameWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#frameWidth
    """
    #  int QFrame::frameWidth() const
    return self.uglySide.call('ritual_ZNK6QFrame10frameWidthEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QFrame::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QFrame::sizeHint() const
    ritual = 'ritual_ZNK6QFrame8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QFrame8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def frameShape(self) -> Shape:
    """
    Calls Qt's 'Shape QFrame::frameShape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#frameShape

    Returns
    -------

    Shape
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Shape(number)' gives.
    """
    #  Shape QFrame::frameShape() const
    return QFrame.Shape(self.uglySide.call(
        'ritual_ZNK6QFrame10frameShapeEv',
    ))

  def frameShadow(self) -> Shadow:
    """
    Calls Qt's 'Shadow QFrame::frameShadow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#frameShadow

    Returns
    -------

    Shadow
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Shadow(number)' gives.
    """
    #  Shadow QFrame::frameShadow() const
    return QFrame.Shadow(self.uglySide.call(
        'ritual_ZNK6QFrame11frameShadowEv',
    ))

  def lineWidth(self) -> int:
    """
    Calls Qt's 'int QFrame::lineWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#lineWidth
    """
    #  int QFrame::lineWidth() const
    return self.uglySide.call('ritual_ZNK6QFrame9lineWidthEv')

  def midLineWidth(self) -> int:
    """
    Calls Qt's 'int QFrame::midLineWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#midLineWidth
    """
    #  int QFrame::midLineWidth() const
    return self.uglySide.call('ritual_ZNK6QFrame12midLineWidthEv')

  def frameRect(self) -> QRect:
    """
    Calls Qt's 'QRect QFrame::frameRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#frameRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QFrame::frameRect() const
    address = self.uglySide.call('ritual_ZNK6QFrame9frameRectEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setFrameStyle(self, a0: int) -> None:
    """
    Calls Qt's 'void QFrame::setFrameStyle(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#setFrameStyle

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QFrame::setFrameStyle(int a0)
    self.uglySide.call('ritual_ZN6QFrame13setFrameStyleEi', a0)

  @overload(Shape)
  def setFrameShape(self, a0: Shape) -> None:
    """
    Calls Qt's 'void QFrame::setFrameShape(Shape a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#setFrameShape

    Parameters
    ----------

    a0 : Shape
      Passed on as its number.
    """
    #  void QFrame::setFrameShape(Shape a0)
    self.uglySide.call(
        'ritual_ZN6QFrame13setFrameShapeENS_5ShapeE', a0.value,
    )

  @overload(Shadow)
  def setFrameShadow(self, a0: Shadow) -> None:
    """
    Calls Qt's 'void QFrame::setFrameShadow(Shadow a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#setFrameShadow

    Parameters
    ----------

    a0 : Shadow
      Passed on as its number.
    """
    #  void QFrame::setFrameShadow(Shadow a0)
    self.uglySide.call(
        'ritual_ZN6QFrame14setFrameShadowENS_6ShadowE', a0.value,
    )

  @overload(int)
  def setLineWidth(self, a0: int) -> None:
    """
    Calls Qt's 'void QFrame::setLineWidth(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#setLineWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QFrame::setLineWidth(int a0)
    self.uglySide.call('ritual_ZN6QFrame12setLineWidthEi', a0)

  @overload(int)
  def setMidLineWidth(self, a0: int) -> None:
    """
    Calls Qt's 'void QFrame::setMidLineWidth(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#setMidLineWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QFrame::setMidLineWidth(int a0)
    self.uglySide.call('ritual_ZN6QFrame15setMidLineWidthEi', a0)

  @overload(QRect)
  def setFrameRect(self, a0: QRect) -> None:
    """
    Calls Qt's 'void QFrame::setFrameRect(const QRect &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#setFrameRect

    Parameters
    ----------

    a0 : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QFrame::setFrameRect(const QRect &a0)
    self.uglySide.call(
        'ritual_ZN6QFrame12setFrameRectERK5QRect', self._valueOf(a0),
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
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      f: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QFrame::QFrame(QWidget *parent,
    Qt::WindowFlags f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#QFrame

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    f : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QFrame::QFrame(QWidget *parent, Qt::WindowFlags f)
    self._noteCreation(QFrame, lambda: Rituals.call(
        'ritual_ZN6QFrameC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), f.value,
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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QFrame::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFrame::event(QEvent *e)
    return self.uglySide.call(
        'ritual_own_ZN6QFrame5eventEP6QEvent', self._addressOf(e),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QFrame::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFrame::paintEvent(QPaintEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN6QFrame10paintEventEP11QPaintEvent',
        self._addressOf(a0),
    )

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QFrame::changeEvent(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#changeEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFrame::changeEvent(QEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN6QFrame11changeEventEP6QEvent', self._addressOf(a0),
    )

  @overload(QStyleOptionFrame)
  @overload(NoneType)
  def initStyleOption(self, option: Optional[QStyleOptionFrame]) -> None:
    """
    Calls Qt's 'void QFrame::initStyleOption(QStyleOptionFrame *option)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qframe.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFrame::initStyleOption(QStyleOptionFrame *option) const
    self.uglySide.call(
        'ritual_own_ZNK6QFrame15initStyleOptionEP17QStyleOptionFrame',
        self._addressOf(option),
    )

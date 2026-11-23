"""
QSlider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qslider.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QAbstractSlider, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QMouseEvent, QPaintEvent
  from . import QStyleOptionSlider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QStyleOptionSlider = WAIT['QStyleOptionSlider']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSlider(QAbstractSlider):
  """
  The cute side of Qt's QSlider: a plain Python object standing in front of
  one C++ QSlider.

  It is built on the cute 'QAbstractSlider', as Qt's QSlider is built on Qt's
  QAbstractSlider, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSlider that has a ritual and that Python can call
  so far, 14 names in all: 'metaObject', 'tr', 'sizeHint', 'minimumSizeHint',
  'setTickPosition', 'tickPosition', 'setTickInterval', 'tickInterval',
  'event', 'paintEvent', 'mousePressEvent', 'mouseReleaseEvent',
  'mouseMoveEvent', 'initStyleOption'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSlider::~QSlider()': the destructor: Python never removes a C++
    QSlider.

  What has no ritual
  ------------------

  8 of the 25 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QSlider is created at the first use, not by 'QSlider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSlider.
  - Qt tells when it has removed the C++ QSlider. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QSlider, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class TickPosition(CuteNum):
    """
    The enum 'QSlider::TickPosition' of Qt, with the 6 names Qt gives in it.
    """

    NoTicks = Kee[int](0)
    TicksAbove = Kee[int](1)
    TicksLeft = Kee[int](1)
    TicksBelow = Kee[int](2)
    TicksRight = Kee[int](2)
    TicksBothSides = Kee[int](3)

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
    Calls Qt's 'QString QSlider::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#tr

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
    #  QString QSlider::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QSlider2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSlider'

  #  A C++ QSlider Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSlider'

  #  The functions Qt calls itself that QSlider is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initStyleOption': (
          ('_ZNK7QSlider15initStyleOptionEP18QStyleOptionSlider',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionSlider'),
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
    Calls Qt's 'const QMetaObject *QSlider::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSlider::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QSlider10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QSlider::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSlider::sizeHint() const
    ritual = 'ritual_ZNK7QSlider8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QSlider8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QSlider::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSlider::minimumSizeHint() const
    ritual = 'ritual_ZNK7QSlider15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QSlider15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def tickPosition(self) -> TickPosition:
    """
    Calls Qt's 'TickPosition QSlider::tickPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#tickPosition

    Returns
    -------

    TickPosition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TickPosition(number)'
      gives.
    """
    #  TickPosition QSlider::tickPosition() const
    return QSlider.TickPosition(self.uglySide.call(
        'ritual_ZNK7QSlider12tickPositionEv',
    ))

  def tickInterval(self) -> int:
    """
    Calls Qt's 'int QSlider::tickInterval() const'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#tickInterval
    """
    #  int QSlider::tickInterval() const
    return self.uglySide.call('ritual_ZNK7QSlider12tickIntervalEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(TickPosition)
  def setTickPosition(self, position: TickPosition) -> None:
    """
    Calls Qt's 'void QSlider::setTickPosition(TickPosition position)'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#setTickPosition

    Parameters
    ----------

    position : TickPosition
      Passed on as its number.
    """
    #  void QSlider::setTickPosition(TickPosition position)
    self.uglySide.call(
        'ritual_ZN7QSlider15setTickPositionENS_12TickPositionE',
        position.value,
    )

  @overload(int)
  def setTickInterval(self, ti: int) -> None:
    """
    Calls Qt's 'void QSlider::setTickInterval(int ti)'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#setTickInterval

    Parameters
    ----------

    ti : int
      Passed on as it is.
    """
    #  void QSlider::setTickInterval(int ti)
    self.uglySide.call('ritual_ZN7QSlider15setTickIntervalEi', ti)

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
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QSlider::QSlider(QWidget *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#QSlider

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSlider::QSlider(QWidget *parent)
    self._noteCreation(QSlider, lambda: Rituals.call(
        'ritual_ZN7QSliderC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(Qt.Orientation)
  @overload(Qt.Orientation, QWidget)
  @overload(Qt.Orientation, NoneType)
  def __init__(
      self,
      orientation: Qt.Orientation,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSlider::QSlider(Qt::Orientation
    orientation, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#QSlider

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSlider::QSlider(Qt::Orientation orientation, QWidget *parent)
    self._noteCreation(QSlider, lambda: Rituals.call(
        'ritual_ZN7QSliderC1EN2Qt11OrientationEP7QWidget',
        orientation.value, self._addressOf(parent),
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
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSlider::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSlider::event(QEvent *event)
    ritual = 'ritual_ZN7QSlider5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QSlider5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, ev: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QSlider::paintEvent(QPaintEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#paintEvent

    Parameters
    ----------

    ev : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSlider::paintEvent(QPaintEvent *ev)
    ritual = 'ritual_ZN7QSlider10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QSlider10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, ev: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QSlider::mousePressEvent(QMouseEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#mousePressEvent

    Parameters
    ----------

    ev : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSlider::mousePressEvent(QMouseEvent *ev)
    ritual = 'ritual_ZN7QSlider15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QSlider15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, ev: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QSlider::mouseReleaseEvent(QMouseEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#mouseReleaseEvent

    Parameters
    ----------

    ev : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSlider::mouseReleaseEvent(QMouseEvent *ev)
    ritual = 'ritual_ZN7QSlider17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QSlider17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, ev: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QSlider::mouseMoveEvent(QMouseEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#mouseMoveEvent

    Parameters
    ----------

    ev : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSlider::mouseMoveEvent(QMouseEvent *ev)
    ritual = 'ritual_ZN7QSlider14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QSlider14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(ev))

  @overload(QStyleOptionSlider)
  @overload(NoneType)
  def initStyleOption(self, option: Optional[QStyleOptionSlider]) -> None:
    """
    Calls Qt's 'void QSlider::initStyleOption(QStyleOptionSlider *option)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qslider.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionSlider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSlider::initStyleOption(QStyleOptionSlider *option) const
    ritual = 'ritual_ZNK7QSlider15initStyleOptionEP18QStyleOptionSlider'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK7QSlider15initStyleOptionEP18QStyleOptionSlider')
    self.uglySide.call(ritual, self._addressOf(option))

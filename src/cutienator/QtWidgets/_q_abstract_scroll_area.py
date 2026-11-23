"""
QAbstractScrollArea binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qabstractscrollarea.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from . import QFrame, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMargins, QMetaObject, QSize
  from ..QtGui import QContextMenuEvent, QDragEnterEvent, QDragLeaveEvent
  from ..QtGui import QDragMoveEvent, QDropEvent, QKeyEvent, QMouseEvent
  from ..QtGui import QPaintEvent, QResizeEvent, QWheelEvent
  from . import QScrollBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMargins = WAIT['QMargins']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QScrollBar = WAIT['QScrollBar']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractScrollArea(QFrame):
  """
  The cute side of Qt's QAbstractScrollArea: a plain Python object standing
  in front of one C++ QAbstractScrollArea.

  It is built on the cute 'QFrame', as Qt's QAbstractScrollArea is built on
  Qt's QFrame, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractScrollArea that has a ritual and that
  Python can call so far, 42 names in all: 'metaObject', 'tr',
  'verticalScrollBarPolicy', 'setVerticalScrollBarPolicy',
  'verticalScrollBar', 'setVerticalScrollBar', 'horizontalScrollBarPolicy',
  'setHorizontalScrollBarPolicy', 'horizontalScrollBar',
  'setHorizontalScrollBar', 'cornerWidget', 'setCornerWidget',
  'addScrollBarWidget', 'scrollBarWidgets', 'viewport', 'setViewport',
  'maximumViewportSize', 'minimumSizeHint', 'sizeHint', 'setupViewport',
  'sizeAdjustPolicy', 'setSizeAdjustPolicy', 'setViewportMargins',
  'viewportMargins', 'eventFilter', 'event', 'viewportEvent', 'resizeEvent',
  'paintEvent', 'mousePressEvent', 'mouseReleaseEvent',
  'mouseDoubleClickEvent', 'mouseMoveEvent', 'wheelEvent',
  'contextMenuEvent', 'dragEnterEvent', 'dragMoveEvent', 'dragLeaveEvent',
  'dropEvent', 'keyPressEvent', 'scrollContentsBy', 'viewportSizeHint'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractScrollArea::~QAbstractScrollArea()': the destructor:
    Python never removes a C++ QAbstractScrollArea.
  - Qt's 'QAbstractScrollAreaPrivate *QAbstractScrollArea::d_func()': gives
    'QAbstractScrollAreaPrivate', which has no cute class yet.
  - Qt's 'const QAbstractScrollAreaPrivate *QAbstractScrollArea::d_func()
    const': gives 'QAbstractScrollAreaPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  7 of the 54 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QAbstractScrollArea is created at the first use, not by
    'QAbstractScrollArea(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractScrollArea.
  - Qt tells when it has removed the C++ QAbstractScrollArea. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAbstractScrollArea, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class SizeAdjustPolicy(CuteNum):
    """
    The enum 'QAbstractScrollArea::SizeAdjustPolicy' of Qt, with the 3 names
    Qt gives in it.
    """

    AdjustIgnored = Kee[int](0)
    AdjustToContentsOnFirstShow = Kee[int](1)
    AdjustToContents = Kee[int](2)

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
    Calls Qt's 'QString QAbstractScrollArea::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractscrollarea.html#tr

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
    #  QString QAbstractScrollArea::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QAbstractScrollArea2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractScrollArea'

  #  A C++ QAbstractScrollArea Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractScrollArea'

  #  The functions Qt calls itself that QAbstractScrollArea is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setupViewport': (
          ('_ZN19QAbstractScrollArea13setupViewportEP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'viewportEvent': (
          ('_ZN19QAbstractScrollArea13viewportEventEP6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'scrollContentsBy': (
          ('_ZN19QAbstractScrollArea16scrollContentsByEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'viewportSizeHint': (
          ('_ZNK19QAbstractScrollArea16viewportSizeHintEv',
           ('address', 'value', 'QtCore:QSize'),
           ()),
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
    Calls Qt's 'const QMetaObject *QAbstractScrollArea::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractScrollArea::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def verticalScrollBarPolicy(self) -> Qt.ScrollBarPolicy:
    """
    Calls Qt's 'Qt::ScrollBarPolicy
    QAbstractScrollArea::verticalScrollBarPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#verticalScrollBarPolicy

    Returns
    -------

    Qt.ScrollBarPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScrollBarPolicy(number)' gives.
    """
    #  Qt::ScrollBarPolicy QAbstractScrollArea::verticalScrollBarPolicy()
    #      const
    return Qt.ScrollBarPolicy(self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea23verticalScrollBarPolicyEv',
    ))

  def verticalScrollBar(self) -> Optional[QScrollBar]:
    """
    Calls Qt's 'QScrollBar *QAbstractScrollArea::verticalScrollBar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#verticalScrollBar

    Returns
    -------

    Optional[QScrollBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScrollBar *QAbstractScrollArea::verticalScrollBar() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea17verticalScrollBarEv',
    )
    from . import QScrollBar
    return QScrollBar._cuteAt(address)

  def horizontalScrollBarPolicy(self) -> Qt.ScrollBarPolicy:
    """
    Calls Qt's 'Qt::ScrollBarPolicy
    QAbstractScrollArea::horizontalScrollBarPolicy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#horizontalScrollBarPolicy

    Returns
    -------

    Qt.ScrollBarPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScrollBarPolicy(number)' gives.
    """
    #  Qt::ScrollBarPolicy QAbstractScrollArea::horizontalScrollBarPolicy()
    #      const
    return Qt.ScrollBarPolicy(self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea25horizontalScrollBarPolicyEv',
    ))

  def horizontalScrollBar(self) -> Optional[QScrollBar]:
    """
    Calls Qt's 'QScrollBar *QAbstractScrollArea::horizontalScrollBar()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#horizontalScrollBar

    Returns
    -------

    Optional[QScrollBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScrollBar *QAbstractScrollArea::horizontalScrollBar() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea19horizontalScrollBarEv',
    )
    from . import QScrollBar
    return QScrollBar._cuteAt(address)

  def cornerWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QAbstractScrollArea::cornerWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#cornerWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QAbstractScrollArea::cornerWidget() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea12cornerWidgetEv',
    )
    return QWidget._cuteAt(address)

  def viewport(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QAbstractScrollArea::viewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractscrollarea.html#viewport

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QAbstractScrollArea::viewport() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea8viewportEv',
    )
    return QWidget._cuteAt(address)

  def maximumViewportSize(self) -> QSize:
    """
    Calls Qt's 'QSize QAbstractScrollArea::maximumViewportSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#maximumViewportSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractScrollArea::maximumViewportSize() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea19maximumViewportSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QAbstractScrollArea::minimumSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractScrollArea::minimumSizeHint() const
    ritual = 'ritual_ZNK19QAbstractScrollArea15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractScrollArea15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QAbstractScrollArea::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractscrollarea.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractScrollArea::sizeHint() const
    ritual = 'ritual_ZNK19QAbstractScrollArea8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractScrollArea8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeAdjustPolicy(self) -> SizeAdjustPolicy:
    """
    Calls Qt's 'SizeAdjustPolicy QAbstractScrollArea::sizeAdjustPolicy()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#sizeAdjustPolicy

    Returns
    -------

    SizeAdjustPolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SizeAdjustPolicy(number)'
      gives.
    """
    #  SizeAdjustPolicy QAbstractScrollArea::sizeAdjustPolicy() const
    return QAbstractScrollArea.SizeAdjustPolicy(self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea16sizeAdjustPolicyEv',
    ))

  def viewportMargins(self) -> QMargins:
    """
    Calls Qt's 'QMargins QAbstractScrollArea::viewportMargins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#viewportMargins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QAbstractScrollArea::viewportMargins() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractScrollArea15viewportMarginsEv',
    )
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  def viewportSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QAbstractScrollArea::viewportSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#viewportSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractScrollArea::viewportSizeHint() const
    ritual = 'ritual_ZNK19QAbstractScrollArea16viewportSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QAbstractScrollArea16viewportSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.ScrollBarPolicy)
  def setVerticalScrollBarPolicy(self, a0: Qt.ScrollBarPolicy) -> None:
    """
    Calls Qt's 'void
    QAbstractScrollArea::setVerticalScrollBarPolicy(Qt::ScrollBarPolicy a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html

    Parameters
    ----------

    a0 : Qt.ScrollBarPolicy
      Passed on as its number.
    """
    #  void QAbstractScrollArea::setVerticalScrollBarPolicy(Qt::
    #      ScrollBarPolicy a0)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea26setVerticalScrollBarPolicyEN2Qt15S'
        'crollBarPolicyE',
        a0.value,
    )

  @overload(QScrollBar)
  @overload(NoneType)
  def setVerticalScrollBar(self, scrollbar: Optional[QScrollBar]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::setVerticalScrollBar(QScrollBar
    *scrollbar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setVerticalScrollBar

    Parameters
    ----------

    scrollbar : Optional[QScrollBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::setVerticalScrollBar(QScrollBar *scrollbar)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea20setVerticalScrollBarEP10QScrollBar',
        self._addressOf(scrollbar),
    )

  @overload(Qt.ScrollBarPolicy)
  def setHorizontalScrollBarPolicy(self, a0: Qt.ScrollBarPolicy) -> None:
    """
    Calls Qt's 'void
    QAbstractScrollArea::setHorizontalScrollBarPolicy(Qt::ScrollBarPolicy
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html

    Parameters
    ----------

    a0 : Qt.ScrollBarPolicy
      Passed on as its number.
    """
    #  void QAbstractScrollArea::setHorizontalScrollBarPolicy(Qt::
    #      ScrollBarPolicy a0)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea28setHorizontalScrollBarPolicyEN2Qt1'
        '5ScrollBarPolicyE',
        a0.value,
    )

  @overload(QScrollBar)
  @overload(NoneType)
  def setHorizontalScrollBar(self, scrollbar: Optional[QScrollBar]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::setHorizontalScrollBar(QScrollBar
    *scrollbar)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setHorizontalScrollBar

    Parameters
    ----------

    scrollbar : Optional[QScrollBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::setHorizontalScrollBar(QScrollBar
    #      *scrollbar)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea22setHorizontalScrollBarEP10QScrollB'
        'ar',
        self._addressOf(scrollbar),
    )

  @overload(QWidget)
  @overload(NoneType)
  def setCornerWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::setCornerWidget(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setCornerWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::setCornerWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea15setCornerWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def setViewport(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::setViewport(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setViewport

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::setViewport(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea11setViewportEP7QWidget',
        self._addressOf(widget),
    )

  @overload(SizeAdjustPolicy)
  def setSizeAdjustPolicy(self, policy: SizeAdjustPolicy) -> None:
    """
    Calls Qt's 'void
    QAbstractScrollArea::setSizeAdjustPolicy(SizeAdjustPolicy policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setSizeAdjustPolicy

    Parameters
    ----------

    policy : SizeAdjustPolicy
      Passed on as its number.
    """
    #  void QAbstractScrollArea::setSizeAdjustPolicy(SizeAdjustPolicy policy)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea19setSizeAdjustPolicyENS_16SizeAdjus'
        'tPolicyE',
        policy.value,
    )

  @overload(int, int, int, int)
  def setViewportMargins(
      self,
      left: int,
      top: int,
      right: int,
      bottom: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::setViewportMargins(int left, int
    top, int right, int bottom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setViewportMargins

    Parameters
    ----------

    left : int
      Passed on as it is.

    top : int
      Passed on as it is.

    right : int
      Passed on as it is.

    bottom : int
      Passed on as it is.
    """
    #  void QAbstractScrollArea::setViewportMargins(int left, int top, int
    #      right, int bottom)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea18setViewportMarginsEiiii',
        left, top, right, bottom,
    )

  @overload(QMargins)
  def setViewportMargins(self, margins: QMargins) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::setViewportMargins(const QMargins
    &margins)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setViewportMargins

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  void QAbstractScrollArea::setViewportMargins(const QMargins &margins)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea18setViewportMarginsERK8QMargins',
        self._valueOf(margins),
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
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractScrollArea::QAbstractScrollArea(QWidget *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#QAbstractScrollArea

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractScrollArea::QAbstractScrollArea(QWidget *parent)
    self._noteCreation(QAbstractScrollArea, lambda: Rituals.call(
        'ritual_ZN19QAbstractScrollAreaC1EP7QWidget',
        self._addressOf(parent),
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

  @overload(QWidget, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def addScrollBarWidget(
      self,
      widget: Optional[QWidget],
      alignment: Qt.Alignment,
  ) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::addScrollBarWidget(QWidget *widget,
    Qt::Alignment alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#addScrollBarWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QAbstractScrollArea::addScrollBarWidget(QWidget *widget,
    #      Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea18addScrollBarWidgetEP7QWidget6QFlag'
        'sIN2Qt13AlignmentFlagEE',
        self._addressOf(widget), alignment.value,
    )

  @overload(Qt.Alignment)
  def scrollBarWidgets(self, alignment: Qt.Alignment) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList
    QAbstractScrollArea::scrollBarWidgets(Qt::Alignment alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#scrollBarWidgets

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList QAbstractScrollArea::scrollBarWidgets(Qt::Alignment
    #      alignment)
    address = self.uglySide.call(
        'ritual_ZN19QAbstractScrollArea16scrollBarWidgetsE6QFlagsIN2Qt13Ali'
        'gnmentFlagEE',
        alignment.value,
    )
    return QList[QWidget]._cuteOwning(address)

  @overload(QWidget)
  @overload(NoneType)
  def setupViewport(self, viewport: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::setupViewport(QWidget *viewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#setupViewport

    Parameters
    ----------

    viewport : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::setupViewport(QWidget *viewport)
    ritual = 'ritual_ZN19QAbstractScrollArea13setupViewportEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractScrollArea13setupViewportEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(viewport))

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractScrollArea::eventFilter(QObject *a0, QEvent
    *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#eventFilter

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractScrollArea::eventFilter(QObject *a0, QEvent *a1)
    ritual = 'ritual_ZN19QAbstractScrollArea11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractScrollArea11eventFilterEP7QObjectP6QEven'
          't')
    return self.uglySide.call(
        ritual, self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractScrollArea::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractscrollarea.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractScrollArea::event(QEvent *a0)
    ritual = 'ritual_ZN19QAbstractScrollArea5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractScrollArea5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def viewportEvent(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractScrollArea::viewportEvent(QEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#viewportEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractScrollArea::viewportEvent(QEvent *a0)
    ritual = 'ritual_ZN19QAbstractScrollArea13viewportEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractScrollArea13viewportEventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::resizeEvent(QResizeEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::resizeEvent(QResizeEvent *a0)
    ritual = 'ritual_ZN19QAbstractScrollArea11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractScrollArea11resizeEventEP12QResizeEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::paintEvent(QPaintEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN19QAbstractScrollArea10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractScrollArea10paintEventEP11QPaintEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::mousePressEvent(QMouseEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#mousePressEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::mousePressEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN19QAbstractScrollArea15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractScrollArea15mousePressEventEP11QMouseEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::mouseReleaseEvent(QMouseEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#mouseReleaseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::mouseReleaseEvent(QMouseEvent *a0)
    ritual = (
        'ritual_ZN19QAbstractScrollArea17mouseReleaseEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractScrollArea17mouseReleaseEventEP11QMouseE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::mouseDoubleClickEvent(QMouseEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#mouseDoubleClickEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::mouseDoubleClickEvent(QMouseEvent *a0)
    ritual = (
        'ritual_ZN19QAbstractScrollArea21mouseDoubleClickEventEP11QMouseEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractScrollArea21mouseDoubleClickEventEP11QMo'
          'useEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::mouseMoveEvent(QMouseEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#mouseMoveEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::mouseMoveEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN19QAbstractScrollArea14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractScrollArea14mouseMoveEventEP11QMouseEven'
          't')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, a0: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::wheelEvent(QWheelEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#wheelEvent

    Parameters
    ----------

    a0 : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::wheelEvent(QWheelEvent *a0)
    ritual = 'ritual_ZN19QAbstractScrollArea10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractScrollArea10wheelEventEP11QWheelEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(self, a0: Optional[QContextMenuEvent]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#contextMenuEvent

    Parameters
    ----------

    a0 : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::contextMenuEvent(QContextMenuEvent *a0)
    ritual = (
        'ritual_ZN19QAbstractScrollArea16contextMenuEventEP17QContextMenuEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractScrollArea16contextMenuEventEP17QContext'
          'MenuEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, a0: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::dragEnterEvent(QDragEnterEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#dragEnterEvent

    Parameters
    ----------

    a0 : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::dragEnterEvent(QDragEnterEvent *a0)
    ritual = (
        'ritual_ZN19QAbstractScrollArea14dragEnterEventEP15QDragEnterEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractScrollArea14dragEnterEventEP15QDragEnter'
          'Event')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, a0: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::dragMoveEvent(QDragMoveEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#dragMoveEvent

    Parameters
    ----------

    a0 : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::dragMoveEvent(QDragMoveEvent *a0)
    ritual = (
        'ritual_ZN19QAbstractScrollArea13dragMoveEventEP14QDragMoveEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractScrollArea13dragMoveEventEP14QDragMoveEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, a0: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::dragLeaveEvent(QDragLeaveEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#dragLeaveEvent

    Parameters
    ----------

    a0 : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::dragLeaveEvent(QDragLeaveEvent *a0)
    ritual = (
        'ritual_ZN19QAbstractScrollArea14dragLeaveEventEP15QDragLeaveEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractScrollArea14dragLeaveEventEP15QDragLeave'
          'Event')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, a0: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::dropEvent(QDropEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractscrollarea.html#dropEvent

    Parameters
    ----------

    a0 : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::dropEvent(QDropEvent *a0)
    ritual = 'ritual_ZN19QAbstractScrollArea9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractScrollArea9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::keyPressEvent(QKeyEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#keyPressEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractScrollArea::keyPressEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN19QAbstractScrollArea13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QAbstractScrollArea13keyPressEventEP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(int, int)
  def scrollContentsBy(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QAbstractScrollArea::scrollContentsBy(int dx, int dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractscrollarea.html#scrollContentsBy

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QAbstractScrollArea::scrollContentsBy(int dx, int dy)
    ritual = 'ritual_ZN19QAbstractScrollArea16scrollContentsByEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractScrollArea16scrollContentsByEii'
    self.uglySide.call(ritual, dx, dy)

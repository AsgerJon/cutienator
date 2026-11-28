"""
QSplitter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qsplitter.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QFrame, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QChildEvent, QEvent, QMetaObject, QSize
  from ..QtGui import QResizeEvent
  from . import QSplitterHandle, QSplitterPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QChildEvent = WAIT['QChildEvent']
  QEvent = WAIT['QEvent']
  QResizeEvent = WAIT['QResizeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSplitter(QFrame):
  """
  The cute side of Qt's QSplitter: a plain Python object standing in front of
  one C++ QSplitter.

  It is built on the cute 'QFrame', as Qt's QSplitter is built on Qt's
  QFrame, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSplitter that has a ritual and that Python can call
  so far, 35 names in all: 'metaObject', 'tr', 'addWidget', 'insertWidget',
  'replaceWidget', 'setOrientation', 'orientation', 'setChildrenCollapsible',
  'childrenCollapsible', 'setCollapsible', 'isCollapsible',
  'setOpaqueResize', 'opaqueResize', 'refresh', 'sizeHint',
  'minimumSizeHint', 'saveState', 'restoreState', 'handleWidth',
  'setHandleWidth', 'indexOf', 'widget', 'count', 'handle',
  'setStretchFactor', 'splitterMoved', 'createHandle', 'childEvent', 'event',
  'resizeEvent', 'changeEvent', 'moveSplitter', 'setRubberBand',
  'closestLegalPosition', 'd_func'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSplitter::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSplitter::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSplitter::~QSplitter()': the destructor: Python never removes a
    C++ QSplitter.
  - Qt's 'QList<int> QSplitter::sizes() const': gives a type Python has no
    way to take yet.
  - Qt's 'void QSplitter::setSizes(const QList<int> &list)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QSplitter::getRange(int index, int *a1, int *a2) const': takes
    a number to change where it is.
  - Qt's 'const QSplitterPrivate *QSplitter::d_func() const': takes in Python
    what 'QSplitterPrivate *QSplitter::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 48 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSplitter is created at the first use, not by 'QSplitter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSplitter.
  - Qt tells when it has removed the C++ QSplitter. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QSplitter that has no cute function yet, 'getRange',
    'setSizes', 'sizes', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QSplitter::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#tr

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
    #  QString QSplitter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QSplitter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSplitter'

  #  A C++ QSplitter Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSplitter'

  #  The functions Qt calls itself that QSplitter is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'createHandle': (
          ('_ZN9QSplitter12createHandleEv',
           ('address', 'address', 'QtWidgets:QSplitterHandle'),
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
    Calls Qt's 'const QMetaObject *QSplitter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSplitter::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QSplitter10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QSplitter::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QSplitter::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK9QSplitter11orientationEv',
    ))

  def childrenCollapsible(self) -> bool:
    """
    Calls Qt's 'bool QSplitter::childrenCollapsible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#childrenCollapsible
    """
    #  bool QSplitter::childrenCollapsible() const
    return self.uglySide.call('ritual_ZNK9QSplitter19childrenCollapsibleEv')

  @overload(int)
  def isCollapsible(self, index: int) -> bool:
    """
    Calls Qt's 'bool QSplitter::isCollapsible(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#isCollapsible

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QSplitter::isCollapsible(int index) const
    return self.uglySide.call('ritual_ZNK9QSplitter13isCollapsibleEi', index)

  def opaqueResize(self) -> bool:
    """
    Calls Qt's 'bool QSplitter::opaqueResize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#opaqueResize
    """
    #  bool QSplitter::opaqueResize() const
    return self.uglySide.call('ritual_ZNK9QSplitter12opaqueResizeEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QSplitter::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSplitter::sizeHint() const
    ritual = 'ritual_ZNK9QSplitter8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QSplitter8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QSplitter::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSplitter::minimumSizeHint() const
    ritual = 'ritual_ZNK9QSplitter15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QSplitter15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def saveState(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSplitter::saveState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#saveState

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSplitter::saveState() const
    address = self.uglySide.call('ritual_ZNK9QSplitter9saveStateEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def handleWidth(self) -> int:
    """
    Calls Qt's 'int QSplitter::handleWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#handleWidth
    """
    #  int QSplitter::handleWidth() const
    return self.uglySide.call('ritual_ZNK9QSplitter11handleWidthEv')

  @overload(QWidget)
  @overload(NoneType)
  def indexOf(self, w: Optional[QWidget]) -> int:
    """
    Calls Qt's 'int QSplitter::indexOf(QWidget *w) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#indexOf

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSplitter::indexOf(QWidget *w) const
    return self.uglySide.call(
        'ritual_ZNK9QSplitter7indexOfEP7QWidget', self._addressOf(w),
    )

  @overload(int)
  def widget(self, index: int) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QSplitter::widget(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#widget

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QSplitter::widget(int index) const
    address = self.uglySide.call('ritual_ZNK9QSplitter6widgetEi', index)
    return QWidget._cuteAt(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QSplitter::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#count
    """
    #  int QSplitter::count() const
    return self.uglySide.call('ritual_ZNK9QSplitter5countEv')

  @overload(int)
  def handle(self, index: int) -> Optional[QSplitterHandle]:
    """
    Calls Qt's 'QSplitterHandle *QSplitter::handle(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#handle

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QSplitterHandle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSplitterHandle *QSplitter::handle(int index) const
    address = self.uglySide.call('ritual_ZNK9QSplitter6handleEi', index)
    from . import QSplitterHandle
    return QSplitterHandle._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def setOrientation(self, a0: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QSplitter::setOrientation(Qt::Orientation a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#setOrientation

    Parameters
    ----------

    a0 : Qt.Orientation
      Passed on as its number.
    """
    #  void QSplitter::setOrientation(Qt::Orientation a0)
    self.uglySide.call(
        'ritual_ZN9QSplitter14setOrientationEN2Qt11OrientationE', a0.value,
    )

  @overload(bool)
  def setChildrenCollapsible(self, a0: bool) -> None:
    """
    Calls Qt's 'void QSplitter::setChildrenCollapsible(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitter.html#setChildrenCollapsible

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QSplitter::setChildrenCollapsible(bool a0)
    self.uglySide.call('ritual_ZN9QSplitter22setChildrenCollapsibleEb', a0)

  @overload(int, bool)
  def setCollapsible(self, index: int, a1: bool) -> None:
    """
    Calls Qt's 'void QSplitter::setCollapsible(int index, bool a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#setCollapsible

    Parameters
    ----------

    index : int
      Passed on as it is.

    a1 : bool
      Passed on as it is.
    """
    #  void QSplitter::setCollapsible(int index, bool a1)
    self.uglySide.call('ritual_ZN9QSplitter14setCollapsibleEib', index, a1)

  @overload()
  @overload(bool)
  def setOpaqueResize(self, opaque: bool = True) -> None:
    """
    Calls Qt's 'void QSplitter::setOpaqueResize(bool opaque)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#setOpaqueResize

    Parameters
    ----------

    opaque : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QSplitter::setOpaqueResize(bool opaque)
    self.uglySide.call('ritual_ZN9QSplitter15setOpaqueResizeEb', opaque)

  @overload(int)
  def setHandleWidth(self, a0: int) -> None:
    """
    Calls Qt's 'void QSplitter::setHandleWidth(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#setHandleWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSplitter::setHandleWidth(int a0)
    self.uglySide.call('ritual_ZN9QSplitter14setHandleWidthEi', a0)

  @overload(int, int)
  def setStretchFactor(self, index: int, stretch: int) -> None:
    """
    Calls Qt's 'void QSplitter::setStretchFactor(int index, int stretch)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#setStretchFactor

    Parameters
    ----------

    index : int
      Passed on as it is.

    stretch : int
      Passed on as it is.
    """
    #  void QSplitter::setStretchFactor(int index, int stretch)
    self.uglySide.call(
        'ritual_ZN9QSplitter16setStretchFactorEii', index, stretch,
    )

  @overload(int)
  def setRubberBand(self, position: int) -> None:
    """
    Calls Qt's 'void QSplitter::setRubberBand(int position)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#setRubberBand

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QSplitter::setRubberBand(int position)
    self.uglySide.call('ritual_ZN9QSplitter13setRubberBandEi', position)

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
    Notes what was given, for Qt's 'QSplitter::QSplitter(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#QSplitter

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSplitter::QSplitter(QWidget *parent)
    self._noteCreation(QSplitter, lambda: Rituals.call(
        'ritual_ZN9QSplitterC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(Qt.Orientation)
  @overload(Qt.Orientation, QWidget)
  @overload(Qt.Orientation, NoneType)
  def __init__(
      self,
      a0: Qt.Orientation,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSplitter::QSplitter(Qt::Orientation a0,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#QSplitter

    Parameters
    ----------

    a0 : Qt.Orientation
      Passed on as its number.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSplitter::QSplitter(Qt::Orientation a0, QWidget *parent)
    self._noteCreation(QSplitter, lambda: Rituals.call(
        'ritual_ZN9QSplitterC1EN2Qt11OrientationEP7QWidget',
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

  @overload(QWidget)
  @overload(NoneType)
  def addWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QSplitter::addWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#addWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSplitter::addWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN9QSplitter9addWidgetEP7QWidget', self._addressOf(widget),
    )

  @overload(int, QWidget)
  @overload(int, NoneType)
  def insertWidget(self, index: int, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QSplitter::insertWidget(int index, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#insertWidget

    Parameters
    ----------

    index : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSplitter::insertWidget(int index, QWidget *widget)
    self.uglySide.call(
        'ritual_ZN9QSplitter12insertWidgetEiP7QWidget',
        index, self._addressOf(widget),
    )

  @overload(int, QWidget)
  @overload(int, NoneType)
  def replaceWidget(
      self,
      index: int,
      widget: Optional[QWidget],
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QSplitter::replaceWidget(int index, QWidget
    *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#replaceWidget

    Parameters
    ----------

    index : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QSplitter::replaceWidget(int index, QWidget *widget)
    address = self.uglySide.call(
        'ritual_ZN9QSplitter13replaceWidgetEiP7QWidget',
        index, self._addressOf(widget),
    )
    return QWidget._cuteAt(address)

  def refresh(self) -> None:
    """
    Calls Qt's 'void QSplitter::refresh()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#refresh
    """
    #  void QSplitter::refresh()
    self.uglySide.call('ritual_ZN9QSplitter7refreshEv')

  @overload(QByteArray)
  def restoreState(self, state: QByteArray) -> bool:
    """
    Calls Qt's 'bool QSplitter::restoreState(const QByteArray &state)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#restoreState

    Parameters
    ----------

    state : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QSplitter::restoreState(const QByteArray &state)
    return self.uglySide.call(
        'ritual_ZN9QSplitter12restoreStateERK10QByteArray',
        self._valueOf(state),
    )

  @overload(int, int)
  def splitterMoved(self, pos: int, index: int) -> None:
    """
    Calls Qt's 'void QSplitter::splitterMoved(int pos, int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#splitterMoved

    Parameters
    ----------

    pos : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QSplitter::splitterMoved(int pos, int index)
    self.uglySide.call('ritual_ZN9QSplitter13splitterMovedEii', pos, index)

  def createHandle(self) -> Optional[QSplitterHandle]:
    """
    Calls Qt's 'QSplitterHandle *QSplitter::createHandle()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#createHandle

    Returns
    -------

    Optional[QSplitterHandle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSplitterHandle *QSplitter::createHandle()
    ritual = 'ritual_ZN9QSplitter12createHandleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSplitter12createHandleEv'
    address = self.uglySide.call(ritual)
    from . import QSplitterHandle
    return QSplitterHandle._cuteAt(address)

  @overload(QChildEvent)
  @overload(NoneType)
  def childEvent(self, a0: Optional[QChildEvent]) -> None:
    """
    Calls Qt's 'void QSplitter::childEvent(QChildEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#childEvent

    Parameters
    ----------

    a0 : Optional[QChildEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSplitter::childEvent(QChildEvent *a0)
    ritual = 'ritual_ZN9QSplitter10childEventEP11QChildEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSplitter10childEventEP11QChildEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSplitter::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSplitter::event(QEvent *a0)
    ritual = 'ritual_ZN9QSplitter5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSplitter5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QSplitter::resizeEvent(QResizeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSplitter::resizeEvent(QResizeEvent *a0)
    ritual = 'ritual_ZN9QSplitter11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSplitter11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QSplitter::changeEvent(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#changeEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSplitter::changeEvent(QEvent *a0)
    ritual = 'ritual_ZN9QSplitter11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSplitter11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(int, int)
  def moveSplitter(self, pos: int, index: int) -> None:
    """
    Calls Qt's 'void QSplitter::moveSplitter(int pos, int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#moveSplitter

    Parameters
    ----------

    pos : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QSplitter::moveSplitter(int pos, int index)
    self.uglySide.call('ritual_ZN9QSplitter12moveSplitterEii', pos, index)

  @overload(int, int)
  def closestLegalPosition(self, a0: int, a1: int) -> int:
    """
    Calls Qt's 'int QSplitter::closestLegalPosition(int a0, int a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitter.html#closestLegalPosition

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : int
      Passed on as it is.
    """
    #  int QSplitter::closestLegalPosition(int a0, int a1)
    return self.uglySide.call(
        'ritual_ZN9QSplitter20closestLegalPositionEii', a0, a1,
    )

  def d_func(self) -> Optional[QSplitterPrivate]:
    """
    Calls Qt's 'QSplitterPrivate *QSplitter::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitter.html#d_func

    Returns
    -------

    Optional[QSplitterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSplitterPrivate *QSplitter::d_func()
    address = self.uglySide.call('ritual_ZN9QSplitter6d_funcEv')
    from . import QSplitterPrivate
    return QSplitterPrivate._cuteAt(address)

  @staticmethod
  def getRange(*__, **_) -> Never:
    """
    Qt's 'void QSplitter::getRange(int index, int *a1, int *a2) const': takes
    a number to change where it is.
    """
    raise NotImplementedError(
        "'QSplitter.getRange' has no cute function yet. Qt's 'void "
        "QSplitter::getRange(int index, int *a1, int *a2) const': takes a "
        "number to change where it is.")

  @staticmethod
  def setSizes(*__, **_) -> Never:
    """
    Qt's 'void QSplitter::setSizes(const QList<int> &list)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSplitter.setSizes' has no cute function yet. Qt's 'void "
        "QSplitter::setSizes(const QList<int> &list)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def sizes(*__, **_) -> Never:
    """
    Qt's 'QList<int> QSplitter::sizes() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QSplitter.sizes' has no cute function yet. Qt's 'QList<int> "
        "QSplitter::sizes() const': gives a type Python has no way to take "
        "yet.")

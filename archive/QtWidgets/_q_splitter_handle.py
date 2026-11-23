"""
QSplitterHandle binding of the Qt C++
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
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QMouseEvent, QPaintEvent, QResizeEvent
  from . import QSplitter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QSplitter = WAIT['QSplitter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSplitterHandle(QWidget):
  """
  The cute side of Qt's QSplitterHandle: a plain Python object standing in
  front of one C++ QSplitterHandle.

  It is built on the cute 'QWidget', as Qt's QSplitterHandle is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSplitterHandle that has a ritual and that Python
  can call so far, 15 names in all: 'metaObject', 'tr', 'setOrientation',
  'orientation', 'opaqueResize', 'splitter', 'sizeHint', 'paintEvent',
  'mouseMoveEvent', 'mousePressEvent', 'mouseReleaseEvent', 'resizeEvent',
  'event', 'moveSplitter', 'closestLegalPosition'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSplitterHandle::~QSplitterHandle()': the destructor: Python never
    removes a C++ QSplitterHandle.

  What has no ritual
  ------------------

  8 of the 25 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QSplitterHandle is created at the first use, not by
    'QSplitterHandle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSplitterHandle.
  - Qt tells when it has removed the C++ QSplitterHandle. Every call on the
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
    Calls Qt's 'QString QSplitterHandle::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterhandle.html#tr

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
    #  QString QSplitterHandle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QSplitterHandle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSplitterHandle'

  #  A C++ QSplitterHandle Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSplitterHandle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSplitterHandle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterhandle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSplitterHandle::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QSplitterHandle10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QSplitterHandle::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterhandle.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QSplitterHandle::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK15QSplitterHandle11orientationEv',
    ))

  def opaqueResize(self) -> bool:
    """
    Calls Qt's 'bool QSplitterHandle::opaqueResize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterhandle.html#opaqueResize
    """
    #  bool QSplitterHandle::opaqueResize() const
    return self.uglySide.call('ritual_ZNK15QSplitterHandle12opaqueResizeEv')

  def splitter(self) -> Optional[QSplitter]:
    """
    Calls Qt's 'QSplitter *QSplitterHandle::splitter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterhandle.html#splitter

    Returns
    -------

    Optional[QSplitter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSplitter *QSplitterHandle::splitter() const
    address = self.uglySide.call('ritual_ZNK15QSplitterHandle8splitterEv')
    from . import QSplitter
    return QSplitter._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QSplitterHandle::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterhandle.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSplitterHandle::sizeHint() const
    ritual = 'ritual_ZNK15QSplitterHandle8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QSplitterHandle8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def setOrientation(self, o: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QSplitterHandle::setOrientation(Qt::Orientation o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterhandle.html#setOrientation

    Parameters
    ----------

    o : Qt.Orientation
      Passed on as its number.
    """
    #  void QSplitterHandle::setOrientation(Qt::Orientation o)
    self.uglySide.call(
        'ritual_ZN15QSplitterHandle14setOrientationEN2Qt11OrientationE',
        o.value,
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

  @overload(Qt.Orientation, QSplitter)
  @overload(Qt.Orientation, NoneType)
  def __init__(self, o: Qt.Orientation, parent: Optional[QSplitter]) -> None:
    """
    Notes what was given, for Qt's
    'QSplitterHandle::QSplitterHandle(Qt::Orientation o, QSplitter *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterhandle.html#QSplitterHandle

    Parameters
    ----------

    o : Qt.Orientation
      Passed on as its number.

    parent : Optional[QSplitter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSplitterHandle::QSplitterHandle(Qt::Orientation o, QSplitter *parent)
    self._noteCreation(QSplitterHandle, lambda: Rituals.call(
        'ritual_ZN15QSplitterHandleC1EN2Qt11OrientationEP9QSplitter',
        o.value, self._addressOf(parent),
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

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QSplitterHandle::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterhandle.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSplitterHandle::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN15QSplitterHandle10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QSplitterHandle10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QSplitterHandle::mouseMoveEvent(QMouseEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterhandle.html#mouseMoveEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSplitterHandle::mouseMoveEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN15QSplitterHandle14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QSplitterHandle14mouseMoveEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QSplitterHandle::mousePressEvent(QMouseEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterhandle.html#mousePressEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSplitterHandle::mousePressEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN15QSplitterHandle15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QSplitterHandle15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QSplitterHandle::mouseReleaseEvent(QMouseEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterhandle.html#mouseReleaseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSplitterHandle::mouseReleaseEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN15QSplitterHandle17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QSplitterHandle17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QSplitterHandle::resizeEvent(QResizeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterhandle.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSplitterHandle::resizeEvent(QResizeEvent *a0)
    ritual = 'ritual_ZN15QSplitterHandle11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QSplitterHandle11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSplitterHandle::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterhandle.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSplitterHandle::event(QEvent *a0)
    ritual = 'ritual_ZN15QSplitterHandle5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QSplitterHandle5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(int)
  def moveSplitter(self, p: int) -> None:
    """
    Calls Qt's 'void QSplitterHandle::moveSplitter(int p)'.

    Qt's own words: https://doc.qt.io/qt-6/qsplitterhandle.html#moveSplitter

    Parameters
    ----------

    p : int
      Passed on as it is.
    """
    #  void QSplitterHandle::moveSplitter(int p)
    self.uglySide.call('ritual_ZN15QSplitterHandle12moveSplitterEi', p)

  @overload(int)
  def closestLegalPosition(self, p: int) -> int:
    """
    Calls Qt's 'int QSplitterHandle::closestLegalPosition(int p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsplitterhandle.html#closestLegalPosition

    Parameters
    ----------

    p : int
      Passed on as it is.
    """
    #  int QSplitterHandle::closestLegalPosition(int p)
    return self.uglySide.call(
        'ritual_ZN15QSplitterHandle20closestLegalPositionEi', p,
    )

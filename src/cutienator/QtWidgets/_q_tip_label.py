"""
QTipLabel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qtooltip_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTipLabel to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QLabel, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QRect, QTimerEvent
  from ..QtGui import QMouseEvent, QPaintEvent, QResizeEvent, QScreen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QResizeEvent = WAIT['QResizeEvent']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTipLabel(QLabel):
  """
  The cute side of Qt's QTipLabel: a plain Python object standing in front of
  one C++ QTipLabel.

  It is built on the cute 'QLabel', as Qt's QTipLabel is built on Qt's
  QLabel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTipLabel that has a ritual and that Python can call
  so far, 17 names in all: 'metaObject', 'tr', 'updateSize', 'eventFilter',
  'reuseTip', 'hideTip', 'hideTipImmediately', 'setTipRect',
  'restartExpireTimer', 'tipChanged', 'placeTip', 'getTipScreen',
  'timerEvent', 'paintEvent', 'mouseMoveEvent', 'resizeEvent',
  'styleSheetParentDestroyed'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTipLabel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QTipLabel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QTipLabel::~QTipLabel()': the destructor: Python never removes a
    C++ QTipLabel.

  What has no ritual
  ------------------

  3 of the 24 functions Qt declares: 2 not a gap; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QTipLabel is created at the first use, not by 'QTipLabel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTipLabel.
  - Qt tells when it has removed the C++ QTipLabel. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QTipLabel that has no cute function yet,
    'adjustTooltipScreen', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QTipLabel::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#tr

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
    #  QString QTipLabel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QTipLabel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QPoint, QWidget)
  @overload(QPoint, NoneType)
  def getTipScreen(pos: QPoint, w: Optional[QWidget]) -> Optional[QScreen]:
    """
    Calls Qt's 'QScreen *QTipLabel::getTipScreen(const QPoint &pos, QWidget
    *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#getTipScreen

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QScreen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScreen *QTipLabel::getTipScreen(const QPoint &pos, QWidget *w)
    address = Rituals.call(
        'ritual_ZN9QTipLabel12getTipScreenERK6QPointP7QWidget',
        CuteMixin._valueOf(pos), CuteMixin._addressOf(w),
    )
    from ..QtGui import QScreen
    return QScreen._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTipLabel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTipLabel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTipLabel::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QTipLabel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget, QRect)
  @overload(NoneType, QRect)
  def setTipRect(self, w: Optional[QWidget], r: QRect) -> None:
    """
    Calls Qt's 'void QTipLabel::setTipRect(QWidget *w, const QRect &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#setTipRect

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QTipLabel::setTipRect(QWidget *w, const QRect &r)
    self.uglySide.call(
        'ritual_ZN9QTipLabel10setTipRectEP7QWidgetRK5QRect',
        self._addressOf(w), self._valueOf(r),
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

  @overload(str, QPoint, QWidget, int)
  @overload(str, QPoint, NoneType, int)
  def __init__(
      self,
      text: str,
      pos: QPoint,
      w: Optional[QWidget],
      msecDisplayTime: int,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTipLabel::QTipLabel(const QString &text,
    const QPoint &pos, QWidget *w, int msecDisplayTime)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#QTipLabel

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    msecDisplayTime : int
      Passed on as it is.
    """
    #  QTipLabel::QTipLabel(const QString &text, const QPoint &pos, QWidget
    #      *w, int msecDisplayTime)
    self._noteCreation(QTipLabel, lambda: Rituals.call(
        'ritual_ZN9QTipLabelC1ERK7QStringRK6QPointP7QWidgeti',
        text, self._valueOf(pos), self._addressOf(w), msecDisplayTime,
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

  @overload(QPoint)
  def updateSize(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QTipLabel::updateSize(const QPoint &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#updateSize

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QTipLabel::updateSize(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN9QTipLabel10updateSizeERK6QPoint', self._valueOf(pos),
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QTipLabel::eventFilter(QObject *a0, QEvent *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#eventFilter

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTipLabel::eventFilter(QObject *a0, QEvent *a1)
    return self.uglySide.call(
        'ritual_ZN9QTipLabel11eventFilterEP7QObjectP6QEvent',
        self._addressOf(a0, 'QObject'), self._addressOf(a1),
    )

  @overload(str, int, QPoint)
  def reuseTip(self, text: str, msecDisplayTime: int, pos: QPoint) -> None:
    """
    Calls Qt's 'void QTipLabel::reuseTip(const QString &text, int
    msecDisplayTime, const QPoint &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#reuseTip

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    msecDisplayTime : int
      Passed on as it is.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QTipLabel::reuseTip(const QString &text, int msecDisplayTime,
    #      const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN9QTipLabel8reuseTipERK7QStringiRK6QPoint',
        text, msecDisplayTime, self._valueOf(pos),
    )

  def hideTip(self) -> None:
    """
    Calls Qt's 'void QTipLabel::hideTip()'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#hideTip
    """
    #  void QTipLabel::hideTip()
    self.uglySide.call('ritual_ZN9QTipLabel7hideTipEv')

  def hideTipImmediately(self) -> None:
    """
    Calls Qt's 'void QTipLabel::hideTipImmediately()'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#hideTipImmediately
    """
    #  void QTipLabel::hideTipImmediately()
    self.uglySide.call('ritual_ZN9QTipLabel18hideTipImmediatelyEv')

  @overload(int)
  def restartExpireTimer(self, msecDisplayTime: int) -> None:
    """
    Calls Qt's 'void QTipLabel::restartExpireTimer(int msecDisplayTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#restartExpireTimer

    Parameters
    ----------

    msecDisplayTime : int
      Passed on as it is.
    """
    #  void QTipLabel::restartExpireTimer(int msecDisplayTime)
    self.uglySide.call(
        'ritual_ZN9QTipLabel18restartExpireTimerEi', msecDisplayTime,
    )

  @overload(QPoint, str, QObject)
  @overload(QPoint, str, NoneType)
  def tipChanged(self, pos: QPoint, text: str, o: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QTipLabel::tipChanged(const QPoint &pos, const QString
    &text, QObject *o)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#tipChanged

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTipLabel::tipChanged(const QPoint &pos, const QString &text,
    #      QObject *o)
    return self.uglySide.call(
        'ritual_ZN9QTipLabel10tipChangedERK6QPointRK7QStringP7QObject',
        self._valueOf(pos), text, self._addressOf(o, 'QObject'),
    )

  @overload(QPoint, QWidget)
  @overload(QPoint, NoneType)
  def placeTip(self, pos: QPoint, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QTipLabel::placeTip(const QPoint &pos, QWidget *w)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#placeTip

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTipLabel::placeTip(const QPoint &pos, QWidget *w)
    self.uglySide.call(
        'ritual_ZN9QTipLabel8placeTipERK6QPointP7QWidget',
        self._valueOf(pos), self._addressOf(w),
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, e: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QTipLabel::timerEvent(QTimerEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#timerEvent

    Parameters
    ----------

    e : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTipLabel::timerEvent(QTimerEvent *e)
    self.uglySide.call(
        'ritual_ZN9QTipLabel10timerEventEP11QTimerEvent', self._addressOf(e),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, e: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QTipLabel::paintEvent(QPaintEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#paintEvent

    Parameters
    ----------

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTipLabel::paintEvent(QPaintEvent *e)
    self.uglySide.call(
        'ritual_ZN9QTipLabel10paintEventEP11QPaintEvent', self._addressOf(e),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QTipLabel::mouseMoveEvent(QMouseEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#mouseMoveEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTipLabel::mouseMoveEvent(QMouseEvent *e)
    self.uglySide.call(
        'ritual_ZN9QTipLabel14mouseMoveEventEP11QMouseEvent',
        self._addressOf(e),
    )

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, e: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QTipLabel::resizeEvent(QResizeEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qtiplabel.html#resizeEvent

    Parameters
    ----------

    e : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTipLabel::resizeEvent(QResizeEvent *e)
    self.uglySide.call(
        'ritual_ZN9QTipLabel11resizeEventEP12QResizeEvent',
        self._addressOf(e),
    )

  def styleSheetParentDestroyed(self) -> None:
    """
    Calls Qt's 'void QTipLabel::styleSheetParentDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtiplabel.html#styleSheetParentDestroyed
    """
    #  void QTipLabel::styleSheetParentDestroyed()
    self.uglySide.call('ritual_ZN9QTipLabel25styleSheetParentDestroyedEv')

  @staticmethod
  def adjustTooltipScreen(*__, **_) -> Never:
    """
    Qt's 'void QTipLabel::adjustTooltipScreen(const QPoint &pos)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QTipLabel.adjustTooltipScreen' has no cute function yet. Qt's "
        "'void QTipLabel::adjustTooltipScreen(const QPoint &pos)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

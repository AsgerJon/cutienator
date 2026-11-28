"""
QGraphicsProxyWidgetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsproxywidget_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGraphicsProxyWidgetPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QGraphicsWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from ..QtGui import QKeyEvent
  from . import QGraphicsProxyWidget, QGraphicsSceneHoverEvent
  from . import QGraphicsSceneMouseEvent, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QPointF = WAIT['QPointF']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsProxyWidgetPrivate(QGraphicsWidgetPrivate):
  """
  The cute side of Qt's QGraphicsProxyWidgetPrivate: a plain Python object
  standing in front of one C++ QGraphicsProxyWidgetPrivate.

  It is built on the cute 'QGraphicsWidgetPrivate', as Qt's
  QGraphicsProxyWidgetPrivate is built on Qt's QGraphicsWidgetPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsProxyWidgetPrivate that has a ritual and
  that Python can call so far, 14 names in all: 'q_func', 'init',
  'sendWidgetMouseEvent', 'sendWidgetKeyEvent', 'setWidget_helper',
  'removeSubFocusHelper', '_q_removeWidgetSlot', 'embedSubWindow',
  'unembedSubWindow', 'isProxyWidget', 'updateWidgetGeometryFromProxy',
  'updateProxyGeometryFromWidget',
  'updateProxyInputMethodAcceptanceFromWidget', 'mapToReceiver'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsProxyWidget *QGraphicsProxyWidgetPrivate::q_func()
    const': takes in Python what 'QGraphicsProxyWidget
    *QGraphicsProxyWidgetPrivate::q_func()' takes.
  - Qt's 'QGraphicsProxyWidgetPrivate::~QGraphicsProxyWidgetPrivate()': the
    destructor: Python never removes a C++ QGraphicsProxyWidgetPrivate.

  What has no ritual
  ------------------

  1 of the 19 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QGraphicsProxyWidgetPrivate is created at the first use, not by
    'QGraphicsProxyWidgetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsProxyWidgetPrivate.
  - Each name of Qt's QGraphicsProxyWidgetPrivate that has no cute function
    yet, 'findFocusChild', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGraphicsProxyWidgetPrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ChangeMode(CuteNum):
    """
    The enum 'QGraphicsProxyWidgetPrivate::ChangeMode' of Qt, with the 3
    names Qt gives in it.
    """

    NoMode = Kee[int](0)
    ProxyToWidgetMode = Kee[int](1)
    WidgetToProxyMode = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsProxyWidgetPrivate'

  #  A C++ QGraphicsProxyWidgetPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsProxyWidgetPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isProxyWidget(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsProxyWidgetPrivate::isProxyWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html#isProxyWidget
    """
    #  bool QGraphicsProxyWidgetPrivate::isProxyWidget() const
    ritual = 'ritual_ZNK27QGraphicsProxyWidgetPrivate13isProxyWidgetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QGraphicsProxyWidgetPrivate13isProxyWidgetEv'
    return self.uglySide.call(ritual)

  @overload(QPointF, QWidget)
  @overload(QPointF, NoneType)
  def mapToReceiver(
      self,
      pos: QPointF,
      receiver: Optional[QWidget],
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsProxyWidgetPrivate::mapToReceiver(const
    QPointF &pos, const QWidget *receiver) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html#mapToReceiver

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    receiver : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsProxyWidgetPrivate::mapToReceiver(const QPointF &pos,
    #      const QWidget *receiver) const
    address = self.uglySide.call(
        'ritual_ZNK27QGraphicsProxyWidgetPrivate13mapToReceiverERK7QPointFP'
        'K7QWidget',
        self._valueOf(pos, 'QPointF'), self._addressOf(receiver),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget, bool)
  @overload(NoneType, bool)
  def setWidget_helper(
      self,
      widget: Optional[QWidget],
      autoShow: bool,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidgetPrivate::setWidget_helper(QWidget
    *widget, bool autoShow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html#setWidget_helper

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    autoShow : bool
      Passed on as it is.
    """
    #  void QGraphicsProxyWidgetPrivate::setWidget_helper(QWidget *widget,
    #      bool autoShow)
    self.uglySide.call(
        'ritual_ZN27QGraphicsProxyWidgetPrivate16setWidget_helperEP7QWidget'
        'b',
        self._addressOf(widget), autoShow,
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
    'QGraphicsProxyWidgetPrivate::QGraphicsProxyWidgetPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html
    """
    #  QGraphicsProxyWidgetPrivate::QGraphicsProxyWidgetPrivate()
    self._noteCreation(QGraphicsProxyWidgetPrivate, lambda: Rituals.call(
        'ritual_ZN27QGraphicsProxyWidgetPrivateC1Ev',
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

  def q_func(self) -> Optional[QGraphicsProxyWidget]:
    """
    Calls Qt's 'QGraphicsProxyWidget *QGraphicsProxyWidgetPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsProxyWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsProxyWidget *QGraphicsProxyWidgetPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QGraphicsProxyWidgetPrivate6q_funcEv',
    )
    from . import QGraphicsProxyWidget
    return QGraphicsProxyWidget._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidgetPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html#init
    """
    #  void QGraphicsProxyWidgetPrivate::init()
    self.uglySide.call('ritual_ZN27QGraphicsProxyWidgetPrivate4initEv')

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def sendWidgetMouseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidgetPrivate::sendWidgetMouseEvent(
    QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidgetPrivate::sendWidgetMouseEvent(
    #      QGraphicsSceneMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN27QGraphicsProxyWidgetPrivate20sendWidgetMouseEventEP24QG'
        'raphicsSceneMouseEvent',
        self._addressOf(event),
    )

  @overload(QGraphicsSceneHoverEvent)
  def sendWidgetMouseEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidgetPrivate::sendWidgetMouseEvent(
    QGraphicsSceneHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidgetPrivate::sendWidgetMouseEvent(
    #      QGraphicsSceneHoverEvent *event)
    self.uglySide.call(
        'ritual_ZN27QGraphicsProxyWidgetPrivate20sendWidgetMouseEventEP24QG'
        'raphicsSceneHoverEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def sendWidgetKeyEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidgetPrivate::sendWidgetKeyEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidgetPrivate::sendWidgetKeyEvent(QKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN27QGraphicsProxyWidgetPrivate18sendWidgetKeyEventEP9QKeyE'
        'vent',
        self._addressOf(event),
    )

  @overload(QWidget, Qt.FocusReason)
  @overload(NoneType, Qt.FocusReason)
  def removeSubFocusHelper(
      self,
      widget: Optional[QWidget],
      reason: Qt.FocusReason,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidgetPrivate::removeSubFocusHelper(QWidget *widget,
    Qt::FocusReason reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reason : Qt.FocusReason
      Passed on as its number.
    """
    #  void QGraphicsProxyWidgetPrivate::removeSubFocusHelper(QWidget
    #      *widget, Qt::FocusReason reason)
    self.uglySide.call(
        'ritual_ZN27QGraphicsProxyWidgetPrivate20removeSubFocusHelperEP7QWi'
        'dgetN2Qt11FocusReasonE',
        self._addressOf(widget), reason.value,
    )

  def _q_removeWidgetSlot(self) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidgetPrivate::_q_removeWidgetSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html
    """
    #  void QGraphicsProxyWidgetPrivate::_q_removeWidgetSlot()
    self.uglySide.call(
        'ritual_ZN27QGraphicsProxyWidgetPrivate19_q_removeWidgetSlotEv',
    )

  @overload(QWidget)
  @overload(NoneType)
  def embedSubWindow(self, a0: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidgetPrivate::embedSubWindow(QWidget
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html#embedSubWindow

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidgetPrivate::embedSubWindow(QWidget *a0)
    self.uglySide.call(
        'ritual_ZN27QGraphicsProxyWidgetPrivate14embedSubWindowEP7QWidget',
        self._addressOf(a0),
    )

  @overload(QWidget)
  @overload(NoneType)
  def unembedSubWindow(self, a0: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QGraphicsProxyWidgetPrivate::unembedSubWindow(QWidget
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html#unembedSubWindow

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsProxyWidgetPrivate::unembedSubWindow(QWidget *a0)
    self.uglySide.call(
        'ritual_ZN27QGraphicsProxyWidgetPrivate16unembedSubWindowEP7QWidget',
        self._addressOf(a0),
    )

  def updateWidgetGeometryFromProxy(self) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidgetPrivate::updateWidgetGeometryFromProxy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html
    """
    #  void QGraphicsProxyWidgetPrivate::updateWidgetGeometryFromProxy()
    self.uglySide.call(
        'ritual_ZN27QGraphicsProxyWidgetPrivate29updateWidgetGeometryFromPr'
        'oxyEv',
    )

  def updateProxyGeometryFromWidget(self) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidgetPrivate::updateProxyGeometryFromWidget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html
    """
    #  void QGraphicsProxyWidgetPrivate::updateProxyGeometryFromWidget()
    self.uglySide.call(
        'ritual_ZN27QGraphicsProxyWidgetPrivate29updateProxyGeometryFromWid'
        'getEv',
    )

  def updateProxyInputMethodAcceptanceFromWidget(self) -> None:
    """
    Calls Qt's 'void
    QGraphicsProxyWidgetPrivate::updateProxyInputMethodAcceptanceFromWidget(
    )'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsproxywidgetprivate.html
    """
    #  void QGraphicsProxyWidgetPrivate::
    #      updateProxyInputMethodAcceptanceFromWidget()
    self.uglySide.call(
        'ritual_ZN27QGraphicsProxyWidgetPrivate42updateProxyInputMethodAcce'
        'ptanceFromWidgetEv',
    )

  @staticmethod
  def findFocusChild(*__, **_) -> Never:
    """
    Qt's 'QWidget *QGraphicsProxyWidgetPrivate::findFocusChild(QWidget
    *child, bool next) const': Qt's library has no name for it, and its code
    in Qt's source does not compile apart from its file: use of undeclared
    identifier 'qt_tab_all_widgets'.
    """
    raise NotImplementedError(
        "'QGraphicsProxyWidgetPrivate.findFocusChild' has no cute function "
        "yet. Qt's 'QWidget "
        "*QGraphicsProxyWidgetPrivate::findFocusChild(QWidget *child, bool "
        "next) const': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'qt_tab_all_widgets'.")

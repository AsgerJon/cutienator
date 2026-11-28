"""
Q3DInputHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/q3dinputhandler.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstract3DInputHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QMouseEvent, QWheelEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QPoint = WAIT['QPoint']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DInputHandler(QAbstract3DInputHandler):
  """
  The cute side of Qt's Q3DInputHandler: a plain Python object standing in
  front of one C++ Q3DInputHandler.

  It is built on the cute 'QAbstract3DInputHandler', as Qt's Q3DInputHandler
  is built on Qt's QAbstract3DInputHandler, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's Q3DInputHandler that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'setRotationEnabled',
  'isRotationEnabled', 'setZoomEnabled', 'isZoomEnabled',
  'setSelectionEnabled', 'isSelectionEnabled', 'setZoomAtTargetEnabled',
  'isZoomAtTargetEnabled', 'mousePressEvent', 'mouseReleaseEvent',
  'mouseMoveEvent', 'wheelEvent', 'rotationEnabledChanged',
  'zoomEnabledChanged', 'selectionEnabledChanged',
  'zoomAtTargetEnabledChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DInputHandler::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Q3DInputHandler::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DInputHandler::~Q3DInputHandler()': the destructor: Python never
    removes a C++ Q3DInputHandler.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Q3DInputHandler is created at the first use, not by
    'Q3DInputHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DInputHandler.
  - Qt tells when it has removed the C++ Q3DInputHandler. Every call on the
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
    Calls Qt's 'QString Q3DInputHandler::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dinputhandler.html#tr

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
    #  QString Q3DInputHandler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15Q3DInputHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DInputHandler'

  #  A C++ Q3DInputHandler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DInputHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DInputHandler::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dinputhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DInputHandler::metaObject() const
    address = self.uglySide.call('ritual_ZNK15Q3DInputHandler10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRotationEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DInputHandler::isRotationEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#isRotationEnabled
    """
    #  bool Q3DInputHandler::isRotationEnabled() const
    return self.uglySide.call(
        'ritual_ZNK15Q3DInputHandler17isRotationEnabledEv',
    )

  def isZoomEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DInputHandler::isZoomEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dinputhandler.html#isZoomEnabled
    """
    #  bool Q3DInputHandler::isZoomEnabled() const
    return self.uglySide.call('ritual_ZNK15Q3DInputHandler13isZoomEnabledEv')

  def isSelectionEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DInputHandler::isSelectionEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#isSelectionEnabled
    """
    #  bool Q3DInputHandler::isSelectionEnabled() const
    return self.uglySide.call(
        'ritual_ZNK15Q3DInputHandler18isSelectionEnabledEv',
    )

  def isZoomAtTargetEnabled(self) -> bool:
    """
    Calls Qt's 'bool Q3DInputHandler::isZoomAtTargetEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#isZoomAtTargetEnabled
    """
    #  bool Q3DInputHandler::isZoomAtTargetEnabled() const
    return self.uglySide.call(
        'ritual_ZNK15Q3DInputHandler21isZoomAtTargetEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setRotationEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DInputHandler::setRotationEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#setRotationEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DInputHandler::setRotationEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN15Q3DInputHandler18setRotationEnabledEb', enable,
    )

  @overload(bool)
  def setZoomEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DInputHandler::setZoomEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#setZoomEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DInputHandler::setZoomEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN15Q3DInputHandler14setZoomEnabledEb', enable,
    )

  @overload(bool)
  def setSelectionEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DInputHandler::setSelectionEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#setSelectionEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DInputHandler::setSelectionEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN15Q3DInputHandler19setSelectionEnabledEb', enable,
    )

  @overload(bool)
  def setZoomAtTargetEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DInputHandler::setZoomAtTargetEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#setZoomAtTargetEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DInputHandler::setZoomAtTargetEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN15Q3DInputHandler22setZoomAtTargetEnabledEb', enable,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'Q3DInputHandler::Q3DInputHandler(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#Q3DInputHandler

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DInputHandler::Q3DInputHandler(QObject *parent)
    self._noteCreation(Q3DInputHandler, lambda: Rituals.call(
        'ritual_ZN15Q3DInputHandlerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QMouseEvent, QPoint)
  @overload(NoneType, QPoint)
  def mousePressEvent(
      self,
      event: Optional[QMouseEvent],
      mousePos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void Q3DInputHandler::mousePressEvent(QMouseEvent *event,
    const QPoint &mousePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Q3DInputHandler::mousePressEvent(QMouseEvent *event, const QPoint
    #      &mousePos)
    ritual = (
        'ritual_ZN15Q3DInputHandler15mousePressEventEP11QMouseEventRK6QPoin'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15Q3DInputHandler15mousePressEventEP11QMouseEventRK'
          '6QPoint')
    self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(mousePos),
    )

  @overload(QMouseEvent, QPoint)
  @overload(NoneType, QPoint)
  def mouseReleaseEvent(
      self,
      event: Optional[QMouseEvent],
      mousePos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void Q3DInputHandler::mouseReleaseEvent(QMouseEvent *event,
    const QPoint &mousePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Q3DInputHandler::mouseReleaseEvent(QMouseEvent *event, const
    #      QPoint &mousePos)
    ritual = (
        'ritual_ZN15Q3DInputHandler17mouseReleaseEventEP11QMouseEventRK6QPo'
        'int')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15Q3DInputHandler17mouseReleaseEventEP11QMouseEvent'
          'RK6QPoint')
    self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(mousePos),
    )

  @overload(QMouseEvent, QPoint)
  @overload(NoneType, QPoint)
  def mouseMoveEvent(
      self,
      event: Optional[QMouseEvent],
      mousePos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void Q3DInputHandler::mouseMoveEvent(QMouseEvent *event,
    const QPoint &mousePos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mousePos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Q3DInputHandler::mouseMoveEvent(QMouseEvent *event, const QPoint
    #      &mousePos)
    ritual = (
        'ritual_ZN15Q3DInputHandler14mouseMoveEventEP11QMouseEventRK6QPoint')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15Q3DInputHandler14mouseMoveEventEP11QMouseEventRK6'
          'QPoint')
    self.uglySide.call(
        ritual, self._addressOf(event), self._valueOf(mousePos),
    )

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void Q3DInputHandler::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dinputhandler.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Q3DInputHandler::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN15Q3DInputHandler10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15Q3DInputHandler10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(bool)
  def rotationEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DInputHandler::rotationEnabledChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#rotationEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DInputHandler::rotationEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN15Q3DInputHandler22rotationEnabledChangedEb', enable,
    )

  @overload(bool)
  def zoomEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DInputHandler::zoomEnabledChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#zoomEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DInputHandler::zoomEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN15Q3DInputHandler18zoomEnabledChangedEb', enable,
    )

  @overload(bool)
  def selectionEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DInputHandler::selectionEnabledChanged(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#selectionEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DInputHandler::selectionEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN15Q3DInputHandler23selectionEnabledChangedEb', enable,
    )

  @overload(bool)
  def zoomAtTargetEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void Q3DInputHandler::zoomAtTargetEnabledChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dinputhandler.html#zoomAtTargetEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void Q3DInputHandler::zoomAtTargetEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN15Q3DInputHandler26zoomAtTargetEnabledChangedEb', enable,
    )

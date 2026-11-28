"""
QQuickHoverHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickhoverhandler_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickHoverHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickSinglePointHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QPointerEvent
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPointerEvent = WAIT['QPointerEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickHoverHandler(QQuickSinglePointHandler):
  """
  The cute side of Qt's QQuickHoverHandler: a plain Python object standing in
  front of one C++ QQuickHoverHandler.

  It is built on the cute 'QQuickSinglePointHandler', as Qt's
  QQuickHoverHandler is built on Qt's QQuickSinglePointHandler, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickHoverHandler that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'event', 'isHovered',
  'isBlocking', 'setBlocking', 'hoveredChanged', 'blockingChanged',
  'componentComplete', 'wantsPointerEvent', 'setHovered'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickHoverHandler::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickHoverHandler::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickHoverHandler::~QQuickHoverHandler()': the destructor: Python
    never removes a C++ QQuickHoverHandler.
  - Qt's 'void QQuickHoverHandler::handleEventPoint(QPointerEvent *ev,
    QEventPoint &point)': takes a type Python has no way to hand over yet.
  - Qt's 'QQuickHoverHandlerPrivate *QQuickHoverHandler::d_func()': gives
    'QQuickHoverHandlerPrivate', which has no cute class yet.
  - Qt's 'const QQuickHoverHandlerPrivate *QQuickHoverHandler::d_func()
    const': gives 'QQuickHoverHandlerPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickHoverHandler is created at the first use, not by
    'QQuickHoverHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickHoverHandler.
  - Qt tells when it has removed the C++ QQuickHoverHandler. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickHoverHandler::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhoverhandler.html#tr

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
    #  QString QQuickHoverHandler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickHoverHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickHoverHandler'

  #  A C++ QQuickHoverHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickHoverHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickHoverHandler::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhoverhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickHoverHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickHoverHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isHovered(self) -> bool:
    """
    Calls Qt's 'bool QQuickHoverHandler::isHovered() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhoverhandler.html#isHovered
    """
    #  bool QQuickHoverHandler::isHovered() const
    return self.uglySide.call('ritual_ZNK18QQuickHoverHandler9isHoveredEv')

  def isBlocking(self) -> bool:
    """
    Calls Qt's 'bool QQuickHoverHandler::isBlocking() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhoverhandler.html#isBlocking
    """
    #  bool QQuickHoverHandler::isBlocking() const
    return self.uglySide.call('ritual_ZNK18QQuickHoverHandler10isBlockingEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setBlocking(self, blocking: bool) -> None:
    """
    Calls Qt's 'void QQuickHoverHandler::setBlocking(bool blocking)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhoverhandler.html#setBlocking

    Parameters
    ----------

    blocking : bool
      Passed on as it is.
    """
    #  void QQuickHoverHandler::setBlocking(bool blocking)
    self.uglySide.call(
        'ritual_ZN18QQuickHoverHandler11setBlockingEb', blocking,
    )

  @overload(bool)
  def setHovered(self, hovered: bool) -> None:
    """
    Calls Qt's 'void QQuickHoverHandler::setHovered(bool hovered)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhoverhandler.html#setHovered

    Parameters
    ----------

    hovered : bool
      Passed on as it is.
    """
    #  void QQuickHoverHandler::setHovered(bool hovered)
    self.uglySide.call(
        'ritual_ZN18QQuickHoverHandler10setHoveredEb', hovered,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickHoverHandler::QQuickHoverHandler(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhoverhandler.html#QQuickHoverHandler

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickHoverHandler::QQuickHoverHandler(QQuickItem *parent)
    self._noteCreation(QQuickHoverHandler, lambda: Rituals.call(
        'ritual_ZN18QQuickHoverHandlerC1EP10QQuickItem',
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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickHoverHandler::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickhoverhandler.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickHoverHandler::event(QEvent *a0)
    ritual = 'ritual_ZN18QQuickHoverHandler5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickHoverHandler5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  def hoveredChanged(self) -> None:
    """
    Calls Qt's 'void QQuickHoverHandler::hoveredChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhoverhandler.html#hoveredChanged
    """
    #  void QQuickHoverHandler::hoveredChanged()
    self.uglySide.call('ritual_ZN18QQuickHoverHandler14hoveredChangedEv')

  def blockingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickHoverHandler::blockingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhoverhandler.html#blockingChanged
    """
    #  void QQuickHoverHandler::blockingChanged()
    self.uglySide.call('ritual_ZN18QQuickHoverHandler15blockingChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickHoverHandler::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhoverhandler.html#componentComplete
    """
    #  void QQuickHoverHandler::componentComplete()
    ritual = 'ritual_ZN18QQuickHoverHandler17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickHoverHandler17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QPointerEvent)
  @overload(NoneType)
  def wantsPointerEvent(self, event: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickHoverHandler::wantsPointerEvent(QPointerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickhoverhandler.html#wantsPointerEvent

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickHoverHandler::wantsPointerEvent(QPointerEvent *event)
    ritual = (
        'ritual_ZN18QQuickHoverHandler17wantsPointerEventEP13QPointerEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickHoverHandler17wantsPointerEventEP13QPointer'
          'Event')
    return self.uglySide.call(ritual, self._addressOf(event))

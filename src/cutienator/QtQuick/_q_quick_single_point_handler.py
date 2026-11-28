"""
QQuickSinglePointHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicksinglepointhandler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickSinglePointHandler to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QPointingDevice
from . import QQuickPointerDeviceHandler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QPointerEvent
  from . import QQuickHandlerPoint, QQuickItem
  from . import QQuickSinglePointHandlerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointerEvent = WAIT['QPointerEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSinglePointHandler(QQuickPointerDeviceHandler):
  """
  The cute side of Qt's QQuickSinglePointHandler: a plain Python object
  standing in front of one C++ QQuickSinglePointHandler.

  It is built on the cute 'QQuickPointerDeviceHandler', as Qt's
  QQuickSinglePointHandler is built on Qt's QQuickPointerDeviceHandler, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSinglePointHandler that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'point',
  'pointChanged', 'wantsPointerEvent', 'handlePointerEventImpl',
  'setIgnoreAdditionalPoints', 'setPointId', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSinglePointHandler::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickSinglePointHandler::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickSinglePointHandler::QQuickSinglePointHandler(
    QQuickSinglePointHandlerPrivate &dd, QQuickItem *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQuickSinglePointHandler::handleEventPoint(QPointerEvent
    *event, QEventPoint &point)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickSinglePointHandler::onGrabChanged(QQuickPointerHandler
    *grabber, QPointingDevice::GrabTransition transition, QPointerEvent
    *event, QEventPoint &point)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickSinglePointHandler::moveTarget(QPointF pos, QEventPoint
    &point)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickSinglePointHandlerPrivate
    *QQuickSinglePointHandler::d_func() const': takes in Python what
    'QQuickSinglePointHandlerPrivate *QQuickSinglePointHandler::d_func()'
    takes.

  What has no ritual
  ------------------

  3 of the 20 functions Qt declares: 2 not a gap; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickSinglePointHandler is created at the first use, not by
    'QQuickSinglePointHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSinglePointHandler.
  - Qt tells when it has removed the C++ QQuickSinglePointHandler. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickSinglePointHandler that has no cute function yet,
    'currentPoint', 'handleEventPoint', 'moveTarget', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickSinglePointHandler::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksinglepointhandler.html#tr

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
    #  QString QQuickSinglePointHandler::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuickSinglePointHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSinglePointHandler'

  #  A C++ QQuickSinglePointHandler Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSinglePointHandler'

  #  The functions Qt calls itself that QQuickSinglePointHandler is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'handleEventPoint': (
          'void QQuickSinglePointHandler::handleEventPoint(QPointerEvent '
          '*, QEventPoint &)',
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
    Calls Qt's 'const QMetaObject *QQuickSinglePointHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksinglepointhandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSinglePointHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickSinglePointHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def point(self) -> QQuickHandlerPoint:
    """
    Calls Qt's 'QQuickHandlerPoint QQuickSinglePointHandler::point() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksinglepointhandler.html#point

    Returns
    -------

    QQuickHandlerPoint
      A new cute QQuickHandlerPoint around the copy Qt gave back. Python owns
      it.
    """
    #  QQuickHandlerPoint QQuickSinglePointHandler::point() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickSinglePointHandler5pointEv',
    )
    from . import QQuickHandlerPoint
    return QQuickHandlerPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(bool)
  def setIgnoreAdditionalPoints(self, v: bool = True) -> None:
    """
    Calls Qt's 'void QQuickSinglePointHandler::setIgnoreAdditionalPoints(bool
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksinglepointhandler.html

    Parameters
    ----------

    v : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickSinglePointHandler::setIgnoreAdditionalPoints(bool v)
    self.uglySide.call(
        'ritual_ZN24QQuickSinglePointHandler25setIgnoreAdditionalPointsEb',
        v,
    )

  @overload(int)
  def setPointId(self, id: int) -> None:
    """
    Calls Qt's 'void QQuickSinglePointHandler::setPointId(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksinglepointhandler.html#setPointId

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QQuickSinglePointHandler::setPointId(int id)
    self.uglySide.call(
        'ritual_ZN24QQuickSinglePointHandler10setPointIdEi', id,
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
    'QQuickSinglePointHandler::QQuickSinglePointHandler(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksinglepointhandler.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSinglePointHandler::QQuickSinglePointHandler(QQuickItem *parent)
    self._noteCreation(QQuickSinglePointHandler, lambda: Rituals.call(
        'ritual_ZN24QQuickSinglePointHandlerC1EP10QQuickItem',
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

  def pointChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSinglePointHandler::pointChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksinglepointhandler.html#pointChanged
    """
    #  void QQuickSinglePointHandler::pointChanged()
    self.uglySide.call('ritual_ZN24QQuickSinglePointHandler12pointChangedEv')

  @overload(QPointerEvent)
  @overload(NoneType)
  def wantsPointerEvent(self, event: Optional[QPointerEvent]) -> bool:
    """
    Calls Qt's 'bool
    QQuickSinglePointHandler::wantsPointerEvent(QPointerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksinglepointhandler.html#wantsPointerEvent

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickSinglePointHandler::wantsPointerEvent(QPointerEvent *event)
    ritual = (
        'ritual_ZN24QQuickSinglePointHandler17wantsPointerEventEP13QPointer'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickSinglePointHandler17wantsPointerEventEP13QP'
          'ointerEvent')
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPointerEvent)
  @overload(NoneType)
  def handlePointerEventImpl(self, event: Optional[QPointerEvent]) -> None:
    """
    Calls Qt's 'void
    QQuickSinglePointHandler::handlePointerEventImpl(QPointerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksinglepointhandler.html

    Parameters
    ----------

    event : Optional[QPointerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSinglePointHandler::handlePointerEventImpl(QPointerEvent
    #      *event)
    ritual = (
        'ritual_ZN24QQuickSinglePointHandler22handlePointerEventImplEP13QPo'
        'interEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickSinglePointHandler22handlePointerEventImplE'
          'P13QPointerEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QQuickSinglePointHandlerPrivate]:
    """
    Calls Qt's 'QQuickSinglePointHandlerPrivate
    *QQuickSinglePointHandler::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksinglepointhandler.html#d_func

    Returns
    -------

    Optional[QQuickSinglePointHandlerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSinglePointHandlerPrivate *QQuickSinglePointHandler::d_func()
    address = self.uglySide.call(
        'ritual_ZN24QQuickSinglePointHandler6d_funcEv',
    )
    from . import QQuickSinglePointHandlerPrivate
    return QQuickSinglePointHandlerPrivate._cuteAt(address)

  @staticmethod
  def currentPoint(*__, **_) -> Never:
    """
    Qt's 'QEventPoint &QQuickSinglePointHandler::currentPoint(QPointerEvent
    *ev)': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickSinglePointHandler.currentPoint' has no cute function yet. "
        "Qt's 'QEventPoint "
        "&QQuickSinglePointHandler::currentPoint(QPointerEvent *ev)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def handleEventPoint(*__, **_) -> Never:
    """
    Qt's 'void QQuickSinglePointHandler::handleEventPoint(QPointerEvent
    *event, QEventPoint &point)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuickSinglePointHandler.handleEventPoint' has no cute function "
        "yet. Qt's 'void "
        "QQuickSinglePointHandler::handleEventPoint(QPointerEvent *event, "
        "QEventPoint &point)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def moveTarget(*__, **_) -> Never:
    """
    Qt's 'void QQuickSinglePointHandler::moveTarget(QPointF pos, QEventPoint
    &point)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickSinglePointHandler.moveTarget' has no cute function yet. "
        "Qt's 'void QQuickSinglePointHandler::moveTarget(QPointF pos, "
        "QEventPoint &point)': takes a type Python has no way to hand over "
        "yet.")

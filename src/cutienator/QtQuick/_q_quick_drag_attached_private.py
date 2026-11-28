"""
QQuickDragAttachedPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdrag_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickDragAttachedPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMimeData, QRectF
  from ..QtGui import QPixmap
  from . import QQuickDragAttached, QQuickGeometryChange, QQuickItem
  from . import QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPixmap = WAIT['QPixmap']
  QQuickDragAttached = WAIT['QQuickDragAttached']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickWindow = WAIT['QQuickWindow']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDragAttachedPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickDragAttachedPrivate: a plain Python object
  standing in front of one C++ QQuickDragAttachedPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQuickDragAttachedPrivate
  is built on Qt's QObjectPrivate, and has everything that class has. Qt's
  QQuickDragAttachedPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickDragAttachedPrivate> as well, which is
  not reflected.

  What exists
  -----------

  Every function of Qt's QQuickDragAttachedPrivate that has a ritual and that
  Python can call so far, 13 names in all: 'q_func', 'get',
  'itemGeometryChanged', 'itemParentChanged', 'updatePosition',
  'restartDrag', 'deliverEnterEvent', 'deliverMoveEvent',
  'deliverLeaveEvent', 'deliverEvent', 'startDrag', 'createMimeData',
  'loadPixmap'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickDragAttached *QQuickDragAttachedPrivate::q_func()
    const': takes in Python what 'QQuickDragAttached
    *QQuickDragAttachedPrivate::q_func()' takes.
  - Qt's 'void QQuickDragAttachedPrivate::qt_qmlMarker_anonymous()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 leans on 'vtable for
  QQuickDragMimeData', which Qt's source does not mark for use from outside
  Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickDragAttachedPrivate is created at the first use, not by
    'QQuickDragAttachedPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDragAttachedPrivate.
  - Each name of Qt's QQuickDragAttachedPrivate that has no cute function
    yet, 'setTarget', 'start', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickDragAttached)
  @overload(NoneType)
  def get(
      attached: Optional[QQuickDragAttached],
  ) -> Optional[QQuickDragAttachedPrivate]:
    """
    Calls Qt's 'QQuickDragAttachedPrivate
    *QQuickDragAttachedPrivate::get(QQuickDragAttached *attached)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdragattachedprivate.html#get

    Parameters
    ----------

    attached : Optional[QQuickDragAttached]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickDragAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDragAttachedPrivate
    #      *QQuickDragAttachedPrivate::get(QQuickDragAttached *attached)
    address = Rituals.call(
        'ritual_ZN25QQuickDragAttachedPrivate3getEP18QQuickDragAttached',
        CuteMixin._addressOf(attached),
    )
    return QQuickDragAttachedPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDragAttachedPrivate'

  #  A C++ QQuickDragAttachedPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickDragAttachedPrivate'

  #  The functions Qt calls itself that QQuickDragAttachedPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN25QQuickDragAttachedPrivate19itemGeometryChangedEP10QQuickIt'
           'em20QQuickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'itemParentChanged': (
          ('_ZN25QQuickDragAttachedPrivate17itemParentChangedEP10QQuickItem'
           'S1_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'address', 'QtQuick:QQuickItem'),
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

  def createMimeData(self) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QQuickDragAttachedPrivate::createMimeData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattachedprivate.html#createMimeData

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QQuickDragAttachedPrivate::createMimeData() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickDragAttachedPrivate14createMimeDataEv',
    )
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QQuickDragAttachedPrivate::QQuickDragAttachedPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattachedprivate.html
    """
    #  QQuickDragAttachedPrivate::QQuickDragAttachedPrivate()
    self._noteCreation(QQuickDragAttachedPrivate, lambda: Rituals.call(
        'ritual_ZN25QQuickDragAttachedPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickDragAttached]:
    """
    Calls Qt's 'QQuickDragAttached *QQuickDragAttachedPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattachedprivate.html#q_func

    Returns
    -------

    Optional[QQuickDragAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDragAttached *QQuickDragAttachedPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QQuickDragAttachedPrivate6q_funcEv',
    )
    from . import QQuickDragAttached
    return QQuickDragAttached._cuteAt(address)

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      a0: Optional[QQuickItem],
      a1: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDragAttachedPrivate::itemGeometryChanged(QQuickItem *a0,
    QQuickGeometryChange a1, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattachedprivate.html#itemGeometryChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    a2 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickDragAttachedPrivate::itemGeometryChanged(QQuickItem *a0,
    #      QQuickGeometryChange a1, const QRectF &a2)
    ritual = (
        'ritual_ZN25QQuickDragAttachedPrivate19itemGeometryChangedEP10QQuic'
        'kItem20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickDragAttachedPrivate19itemGeometryChangedEP1'
          '0QQuickItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual, self._addressOf(a0), self._valueOf(a1), self._valueOf(a2),
    )

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemParentChanged(
      self,
      a0: Optional[QQuickItem],
      parent: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickDragAttachedPrivate::itemParentChanged(QQuickItem
    *a0, QQuickItem *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattachedprivate.html#itemParentChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDragAttachedPrivate::itemParentChanged(QQuickItem *a0,
    #      QQuickItem *parent)
    ritual = (
        'ritual_ZN25QQuickDragAttachedPrivate17itemParentChangedEP10QQuickI'
        'temS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickDragAttachedPrivate17itemParentChangedEP10Q'
          'QuickItemS1_')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(parent))

  def updatePosition(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttachedPrivate::updatePosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattachedprivate.html#updatePosition
    """
    #  void QQuickDragAttachedPrivate::updatePosition()
    self.uglySide.call(
        'ritual_ZN25QQuickDragAttachedPrivate14updatePositionEv',
    )

  def restartDrag(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttachedPrivate::restartDrag()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattachedprivate.html#restartDrag
    """
    #  void QQuickDragAttachedPrivate::restartDrag()
    self.uglySide.call('ritual_ZN25QQuickDragAttachedPrivate11restartDragEv')

  def deliverEnterEvent(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttachedPrivate::deliverEnterEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattachedprivate.html#deliverEnterEvent
    """
    #  void QQuickDragAttachedPrivate::deliverEnterEvent()
    self.uglySide.call(
        'ritual_ZN25QQuickDragAttachedPrivate17deliverEnterEventEv',
    )

  def deliverMoveEvent(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttachedPrivate::deliverMoveEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattachedprivate.html#deliverMoveEvent
    """
    #  void QQuickDragAttachedPrivate::deliverMoveEvent()
    self.uglySide.call(
        'ritual_ZN25QQuickDragAttachedPrivate16deliverMoveEventEv',
    )

  def deliverLeaveEvent(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttachedPrivate::deliverLeaveEvent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattachedprivate.html#deliverLeaveEvent
    """
    #  void QQuickDragAttachedPrivate::deliverLeaveEvent()
    self.uglySide.call(
        'ritual_ZN25QQuickDragAttachedPrivate17deliverLeaveEventEv',
    )

  @overload(QQuickWindow, QEvent)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def deliverEvent(
      self,
      window: Optional[QQuickWindow],
      event: Optional[QEvent],
  ) -> None:
    """
    Calls Qt's 'void QQuickDragAttachedPrivate::deliverEvent(QQuickWindow
    *window, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattachedprivate.html#deliverEvent

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDragAttachedPrivate::deliverEvent(QQuickWindow *window,
    #      QEvent *event)
    self.uglySide.call(
        'ritual_ZN25QQuickDragAttachedPrivate12deliverEventEP12QQuickWindow'
        'P6QEvent',
        self._addressOf(window), self._addressOf(event),
    )

  @overload(Qt.DropActions)
  @overload(Qt.DropActions, QPixmap)
  def startDrag(
      self,
      supportedActions: Qt.DropActions,
      pixmap: Optional[QPixmap] = None,
  ) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction
    QQuickDragAttachedPrivate::startDrag(Qt::DropActions supportedActions,
    QPixmap pixmap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattachedprivate.html#startDrag

    Parameters
    ----------

    supportedActions : Qt.DropActions
      Passed on as its number.

    pixmap : Optional[QPixmap]
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own. May be left out, as in Qt: a new 'QPixmap()' is then passed on.

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QQuickDragAttachedPrivate::startDrag(Qt::DropActions
    #      supportedActions, QPixmap pixmap)
    if pixmap is None:
      from ..QtGui import QPixmap
      pixmap = QPixmap()
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZN25QQuickDragAttachedPrivate9startDragE6QFlagsIN2Qt10DropA'
        'ctionEE7QPixmap',
        supportedActions.value, self._valueOf(pixmap),
    ))

  def loadPixmap(self) -> None:
    """
    Calls Qt's 'void QQuickDragAttachedPrivate::loadPixmap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdragattachedprivate.html#loadPixmap
    """
    #  void QQuickDragAttachedPrivate::loadPixmap()
    self.uglySide.call('ritual_ZN25QQuickDragAttachedPrivate10loadPixmapEv')

  @staticmethod
  def setTarget(*__, **_) -> Never:
    """
    Qt's 'void QQuickDragAttachedPrivate::setTarget(QQuickItem *item)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickDragAttachedPrivate.setTarget' has no cute function yet. "
        "Qt's 'void QQuickDragAttachedPrivate::setTarget(QQuickItem "
        "*item)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def start(*__, **_) -> Never:
    """
    Qt's 'void QQuickDragAttachedPrivate::start(Qt::DropActions
    supportedActions)': leans on 'vtable for QQuickDragMimeData', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickDragAttachedPrivate.start' has no cute function yet. Qt's "
        "'void QQuickDragAttachedPrivate::start(Qt::DropActions "
        "supportedActions)': leans on 'vtable for QQuickDragMimeData', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

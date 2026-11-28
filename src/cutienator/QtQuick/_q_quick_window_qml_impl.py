"""
QQuickWindowQmlImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickwindowmodule_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickWindowQmlImpl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QWindow
from ..QtQml import QQmlParserStatus
from . import QQuickWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QQuickScreenInfo, QQuickWindowAttached
  from . import QQuickWindowQmlImplPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QQuickScreenInfo = WAIT['QQuickScreenInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWindowQmlImpl(QQuickWindow, QQmlParserStatus):
  """
  The cute side of Qt's QQuickWindowQmlImpl: a plain Python object standing
  in front of one C++ QQuickWindowQmlImpl.

  It is built on the cute 'QQuickWindow', as Qt's QQuickWindowQmlImpl is
  built on Qt's QQuickWindow, and has everything that class has. It is built
  on the cute 'QQmlParserStatus' as well, as Qt's QQuickWindowQmlImpl is
  built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWindowQmlImpl that has a ritual and that
  Python can call so far, 30 names in all: 'metaObject', 'tr', 'setVisible',
  'setVisibility', 'screen', 'setScreen', 'visualParent', 'setVisualParent',
  'visualParentChanged', 'setX', 'x', 'setY', 'y', 'setZ', 'z', 'zChanged',
  'qmlAttachedProperties', 'visibleChanged', 'visibilityChanged',
  'screenChanged', 'xChanged', 'yChanged', 'classBegin', 'componentComplete',
  'event', 'applyWindowVisibility', 'updateTransientParent',
  'transientParentVisible', 'applyVisualParent', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWindowQmlImpl::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickWindowQmlImpl::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWindowQmlImpl::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQuickWindowQmlImpl::~QQuickWindowQmlImpl()': the destructor:
    Python never removes a C++ QQuickWindowQmlImpl.
  - Qt's 'QQuickWindowQmlImpl::QQuickWindowQmlImpl(QQuickWindowQmlImplPrivate
    &dd, QWindow *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickWindowQmlImplPrivate *QQuickWindowQmlImpl::d_func()
    const': takes in Python what 'QQuickWindowQmlImplPrivate
    *QQuickWindowQmlImpl::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 41 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickWindowQmlImpl is created at the first use, not by
    'QQuickWindowQmlImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWindowQmlImpl.
  - Qt tells when it has removed the C++ QQuickWindowQmlImpl. Every call on
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
    Calls Qt's 'QString QQuickWindowQmlImpl::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#tr

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
    #  QString QQuickWindowQmlImpl::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickWindowQmlImpl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickWindowAttached]:
    """
    Calls Qt's 'QQuickWindowAttached
    *QQuickWindowQmlImpl::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickWindowAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindowAttached
    #      *QQuickWindowQmlImpl::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN19QQuickWindowQmlImpl21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickWindowAttached
    return QQuickWindowAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWindowQmlImpl'

  #  Qt's QQuickWindowQmlImpl is built on more than one class. The part of a
  #  C++ QQuickWindowQmlImpl that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickWindowQmlImpl_QQmlParserStatus',
  }

  #  A C++ QQuickWindowQmlImpl Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWindowQmlImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWindowQmlImpl::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWindowQmlImpl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWindowQmlImpl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def screen(self) -> Optional[QQuickScreenInfo]:
    """
    Calls Qt's 'QQuickScreenInfo *QQuickWindowQmlImpl::screen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#screen

    Returns
    -------

    Optional[QQuickScreenInfo]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScreenInfo *QQuickWindowQmlImpl::screen() const
    address = self.uglySide.call('ritual_ZNK19QQuickWindowQmlImpl6screenEv')
    from . import QQuickScreenInfo
    return QQuickScreenInfo._cuteAt(address)

  def visualParent(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickWindowQmlImpl::visualParent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#visualParent

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickWindowQmlImpl::visualParent() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickWindowQmlImpl12visualParentEv',
    )
    return QObject._cuteAt(address)

  def x(self) -> int:
    """
    Calls Qt's 'int QQuickWindowQmlImpl::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#x
    """
    #  int QQuickWindowQmlImpl::x() const
    return self.uglySide.call('ritual_ZNK19QQuickWindowQmlImpl1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QQuickWindowQmlImpl::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#y
    """
    #  int QQuickWindowQmlImpl::y() const
    return self.uglySide.call('ritual_ZNK19QQuickWindowQmlImpl1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'qreal QQuickWindowQmlImpl::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#z
    """
    #  qreal QQuickWindowQmlImpl::z() const
    return self.uglySide.call('ritual_ZNK19QQuickWindowQmlImpl1zEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::setVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickWindowQmlImpl::setVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowQmlImpl10setVisibleEb', visible,
    )

  @overload(QWindow.Visibility)
  def setVisibility(self, visibility: QWindow.Visibility) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::setVisibility(QWindow::Visibility
    visibility)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#setVisibility

    Parameters
    ----------

    visibility : QWindow.Visibility
      Passed on as its number.
    """
    #  void QQuickWindowQmlImpl::setVisibility(QWindow::Visibility
    #      visibility)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowQmlImpl13setVisibilityEN7QWindow10Visibilit'
        'yE',
        visibility.value,
    )

  @overload(QQuickScreenInfo)
  @overload(NoneType)
  def setScreen(self, screen: Optional[QQuickScreenInfo]) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::setScreen(QQuickScreenInfo
    *screen)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#setScreen

    Parameters
    ----------

    screen : Optional[QQuickScreenInfo]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowQmlImpl::setScreen(QQuickScreenInfo *screen)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowQmlImpl9setScreenEP16QQuickScreenInfo',
        self._addressOf(screen),
    )

  @overload(QObject)
  @overload(NoneType)
  def setVisualParent(self, parent: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::setVisualParent(QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#setVisualParent

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowQmlImpl::setVisualParent(QObject *parent)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowQmlImpl15setVisualParentEP7QObject',
        self._addressOf(parent, 'QObject'),
    )

  @overload(int)
  def setX(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::setX(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#setX

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickWindowQmlImpl::setX(int arg)
    self.uglySide.call('ritual_ZN19QQuickWindowQmlImpl4setXEi', arg)

  @overload(int)
  def setY(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::setY(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#setY

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickWindowQmlImpl::setY(int arg)
    self.uglySide.call('ritual_ZN19QQuickWindowQmlImpl4setYEi', arg)

  @overload(float)
  def setZ(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::setZ(qreal arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#setZ

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickWindowQmlImpl::setZ(qreal arg)
    self.uglySide.call('ritual_ZN19QQuickWindowQmlImpl4setZEd', arg)

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
  @overload(QWindow)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWindow] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWindowQmlImpl::QQuickWindowQmlImpl(QWindow *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#QQuickWindowQmlImpl

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickWindowQmlImpl::QQuickWindowQmlImpl(QWindow *parent)
    self._noteCreation(QQuickWindowQmlImpl, lambda: Rituals.call(
        'ritual_ZN19QQuickWindowQmlImplC1EP7QWindow',
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

  @overload(QObject)
  @overload(NoneType)
  def visualParentChanged(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::visualParentChanged(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#visualParentChanged

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowQmlImpl::visualParentChanged(QObject *a0)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowQmlImpl19visualParentChangedEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  def zChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::zChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#zChanged
    """
    #  void QQuickWindowQmlImpl::zChanged()
    self.uglySide.call('ritual_ZN19QQuickWindowQmlImpl8zChangedEv')

  @overload(bool)
  def visibleChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::visibleChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#visibleChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickWindowQmlImpl::visibleChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowQmlImpl14visibleChangedEb', arg,
    )

  @overload(QWindow.Visibility)
  def visibilityChanged(self, visibility: QWindow.Visibility) -> None:
    """
    Calls Qt's 'void
    QQuickWindowQmlImpl::visibilityChanged(QWindow::Visibility visibility)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#visibilityChanged

    Parameters
    ----------

    visibility : QWindow.Visibility
      Passed on as its number.
    """
    #  void QQuickWindowQmlImpl::visibilityChanged(QWindow::Visibility
    #      visibility)
    self.uglySide.call(
        'ritual_ZN19QQuickWindowQmlImpl17visibilityChangedEN7QWindow10Visib'
        'ilityE',
        visibility.value,
    )

  def screenChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::screenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#screenChanged
    """
    #  void QQuickWindowQmlImpl::screenChanged()
    self.uglySide.call('ritual_ZN19QQuickWindowQmlImpl13screenChangedEv')

  @overload(int)
  def xChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::xChanged(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#xChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickWindowQmlImpl::xChanged(int arg)
    self.uglySide.call('ritual_ZN19QQuickWindowQmlImpl8xChangedEi', arg)

  @overload(int)
  def yChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::yChanged(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#yChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickWindowQmlImpl::yChanged(int arg)
    self.uglySide.call('ritual_ZN19QQuickWindowQmlImpl8yChangedEi', arg)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#classBegin
    """
    #  void QQuickWindowQmlImpl::classBegin()
    ritual = 'ritual_ZN19QQuickWindowQmlImpl10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickWindowQmlImpl10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#componentComplete
    """
    #  void QQuickWindowQmlImpl::componentComplete()
    ritual = 'ritual_ZN19QQuickWindowQmlImpl17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickWindowQmlImpl17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickWindowQmlImpl::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickWindowQmlImpl::event(QEvent *a0)
    ritual = 'ritual_ZN19QQuickWindowQmlImpl5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickWindowQmlImpl5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  def applyWindowVisibility(self) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::applyWindowVisibility()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#applyWindowVisibility
    """
    #  void QQuickWindowQmlImpl::applyWindowVisibility()
    self.uglySide.call(
        'ritual_ZN19QQuickWindowQmlImpl21applyWindowVisibilityEv',
    )

  def updateTransientParent(self) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::updateTransientParent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#updateTransientParent
    """
    #  void QQuickWindowQmlImpl::updateTransientParent()
    self.uglySide.call(
        'ritual_ZN19QQuickWindowQmlImpl21updateTransientParentEv',
    )

  def transientParentVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickWindowQmlImpl::transientParentVisible()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#transientParentVisible
    """
    #  bool QQuickWindowQmlImpl::transientParentVisible()
    return self.uglySide.call(
        'ritual_ZN19QQuickWindowQmlImpl22transientParentVisibleEv',
    )

  def applyVisualParent(self) -> None:
    """
    Calls Qt's 'void QQuickWindowQmlImpl::applyVisualParent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#applyVisualParent
    """
    #  void QQuickWindowQmlImpl::applyVisualParent()
    self.uglySide.call('ritual_ZN19QQuickWindowQmlImpl17applyVisualParentEv')

  def d_func(self) -> Optional[QQuickWindowQmlImplPrivate]:
    """
    Calls Qt's 'QQuickWindowQmlImplPrivate *QQuickWindowQmlImpl::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowqmlimpl.html#d_func

    Returns
    -------

    Optional[QQuickWindowQmlImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindowQmlImplPrivate *QQuickWindowQmlImpl::d_func()
    address = self.uglySide.call('ritual_ZN19QQuickWindowQmlImpl6d_funcEv')
    from . import QQuickWindowQmlImplPrivate
    return QQuickWindowQmlImplPrivate._cuteAt(address)

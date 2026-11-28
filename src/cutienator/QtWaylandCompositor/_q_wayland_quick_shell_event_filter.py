"""
QWaylandQuickShellEventFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandquickshellsurfaceitem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWaylandQuickShellEventFilter to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QTimerEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandQuickShellEventFilter(QObject):
  """
  The cute side of Qt's QWaylandQuickShellEventFilter: a plain Python object
  standing in front of one C++ QWaylandQuickShellEventFilter.

  It is built on the cute 'QObject', as Qt's QWaylandQuickShellEventFilter is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandQuickShellEventFilter that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'cancelFilter', 'timerEvent', 'stopFilter', 'eventFilter'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandQuickShellEventFilter::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QWaylandQuickShellEventFilter::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QWaylandQuickShellEventFilter::startFilter(QWaylandClient
    *client, CallbackFunction closePopupCallback)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandQuickShellEventFilter is created at the first use, not by
    'QWaylandQuickShellEventFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandQuickShellEventFilter.
  - Qt tells when it has removed the C++ QWaylandQuickShellEventFilter. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandQuickShellEventFilter that has no cute function
    yet, 'startFilter', holds a function that raises 'NotImplementedError',
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
    Calls Qt's 'QString QWaylandQuickShellEventFilter::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshelleventfilter.html#tr

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
    #  QString QWaylandQuickShellEventFilter::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QWaylandQuickShellEventFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def cancelFilter() -> None:
    """
    Calls Qt's 'void QWaylandQuickShellEventFilter::cancelFilter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshelleventfilter.html#cancelFilter
    """
    #  void QWaylandQuickShellEventFilter::cancelFilter()
    Rituals.call('ritual_ZN29QWaylandQuickShellEventFilter12cancelFilterEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandQuickShellEventFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QWaylandQuickShellEventFilter::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshelleventfilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandQuickShellEventFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QWaylandQuickShellEventFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandQuickShellEventFilter::QWaylandQuickShellEventFilter(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshelleventfilter.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandQuickShellEventFilter::QWaylandQuickShellEventFilter(QObject
    #      *parent)
    self._noteCreation(QWaylandQuickShellEventFilter, lambda: Rituals.call(
        'ritual_ZN29QWaylandQuickShellEventFilterC1EP7QObject',
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

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QWaylandQuickShellEventFilter::timerEvent(QTimerEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshelleventfilter.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickShellEventFilter::timerEvent(QTimerEvent *event)
    ritual = (
        'ritual_ZN29QWaylandQuickShellEventFilter10timerEventEP11QTimerEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QWaylandQuickShellEventFilter10timerEventEP11QTim'
          'erEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def stopFilter(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickShellEventFilter::stopFilter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshelleventfilter.html#stopFilter
    """
    #  void QWaylandQuickShellEventFilter::stopFilter()
    self.uglySide.call(
        'ritual_ZN29QWaylandQuickShellEventFilter10stopFilterEv',
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickShellEventFilter::eventFilter(QObject *a0,
    QEvent *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshelleventfilter.html#eventFilter

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWaylandQuickShellEventFilter::eventFilter(QObject *a0, QEvent
    #      *a1)
    ritual = (
        'ritual_ZN29QWaylandQuickShellEventFilter11eventFilterEP7QObjectP6Q'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QWaylandQuickShellEventFilter11eventFilterEP7QObj'
          'ectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(a0, 'QObject'), self._addressOf(a1),
    )

  @staticmethod
  def startFilter(*__, **_) -> Never:
    """
    Qt's 'void QWaylandQuickShellEventFilter::startFilter(QWaylandClient
    *client, CallbackFunction closePopupCallback)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWaylandQuickShellEventFilter.startFilter' has no cute function "
        "yet. Qt's 'void "
        "QWaylandQuickShellEventFilter::startFilter(QWaylandClient *client, "
        "CallbackFunction closePopupCallback)': takes a type Python has no "
        "way to hand over yet.")

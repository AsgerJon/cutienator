"""
QWindowContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwindowcontainer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QWindowContainer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWindowContainer(QWidget):
  """
  The cute side of Qt's QWindowContainer: a plain Python object standing in
  front of one C++ QWindowContainer.

  It is built on the cute 'QWidget', as Qt's QWindowContainer is built on
  Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWindowContainer that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'containedWindow',
  'minimumSizeHint', 'toplevelAboutToBeDestroyed', 'parentWasChanged',
  'parentWasMoved', 'parentWasRaised', 'parentWasLowered', 'event',
  'eventFilter'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWindowContainer::~QWindowContainer()': the destructor: Python
    never removes a C++ QWindowContainer.

  What has no ritual
  ------------------

  6 of the 19 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QWindowContainer is created at the first use, not by
    'QWindowContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWindowContainer.
  - Qt tells when it has removed the C++ QWindowContainer. Every call on the
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
    Calls Qt's 'QString QWindowContainer::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcontainer.html#tr

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
    #  QString QWindowContainer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QWindowContainer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def toplevelAboutToBeDestroyed(parent: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWindowContainer::toplevelAboutToBeDestroyed(QWidget
    *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowcontainer.html#toplevelAboutToBeDestroyed

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowContainer::toplevelAboutToBeDestroyed(QWidget *parent)
    Rituals.call(
        'ritual_ZN16QWindowContainer26toplevelAboutToBeDestroyedEP7QWidget',
        CuteMixin._addressOf(parent),
    )

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def parentWasChanged(parent: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWindowContainer::parentWasChanged(QWidget *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowcontainer.html#parentWasChanged

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowContainer::parentWasChanged(QWidget *parent)
    Rituals.call(
        'ritual_ZN16QWindowContainer16parentWasChangedEP7QWidget',
        CuteMixin._addressOf(parent),
    )

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def parentWasMoved(parent: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWindowContainer::parentWasMoved(QWidget *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowcontainer.html#parentWasMoved

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowContainer::parentWasMoved(QWidget *parent)
    Rituals.call(
        'ritual_ZN16QWindowContainer14parentWasMovedEP7QWidget',
        CuteMixin._addressOf(parent),
    )

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def parentWasRaised(parent: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWindowContainer::parentWasRaised(QWidget *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowcontainer.html#parentWasRaised

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowContainer::parentWasRaised(QWidget *parent)
    Rituals.call(
        'ritual_ZN16QWindowContainer15parentWasRaisedEP7QWidget',
        CuteMixin._addressOf(parent),
    )

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  def parentWasLowered(parent: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWindowContainer::parentWasLowered(QWidget *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowcontainer.html#parentWasLowered

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWindowContainer::parentWasLowered(QWidget *parent)
    Rituals.call(
        'ritual_ZN16QWindowContainer16parentWasLoweredEP7QWidget',
        CuteMixin._addressOf(parent),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWindowContainer'

  #  A C++ QWindowContainer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWindowContainer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWindowContainer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcontainer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWindowContainer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QWindowContainer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def containedWindow(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QWindowContainer::containedWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowcontainer.html#containedWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QWindowContainer::containedWindow() const
    address = self.uglySide.call(
        'ritual_ZNK16QWindowContainer15containedWindowEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QWindowContainer::minimumSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowcontainer.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWindowContainer::minimumSizeHint() const
    ritual = 'ritual_ZNK16QWindowContainer15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QWindowContainer15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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

  @overload(QWindow)
  @overload(NoneType)
  @overload(QWindow, QWidget)
  @overload(QWindow, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  @overload(QWindow, QWidget, Qt.WindowFlags)
  @overload(QWindow, NoneType, Qt.WindowFlags)
  @overload(NoneType, QWidget, Qt.WindowFlags)
  @overload(NoneType, NoneType, Qt.WindowFlags)
  def __init__(
      self,
      embeddedWindow: Optional[QWindow],
      parent: Optional[QWidget] = None,
      f: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWindowContainer::QWindowContainer(QWindow *embeddedWindow, QWidget
    *parent, Qt::WindowFlags f)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwindowcontainer.html#QWindowContainer

    Parameters
    ----------

    embeddedWindow : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    f : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QWindowContainer::QWindowContainer(QWindow *embeddedWindow, QWidget
    #      *parent, Qt::WindowFlags f)
    self._noteCreation(QWindowContainer, lambda: Rituals.call(
        'ritual_ZN16QWindowContainerC1EP7QWindowP7QWidget6QFlagsIN2Qt10Wind'
        'owTypeEE',
        self._addressOf(embeddedWindow), self._addressOf(parent), f.value,
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
  def event(self, ev: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWindowContainer::event(QEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcontainer.html#event

    Parameters
    ----------

    ev : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWindowContainer::event(QEvent *ev)
    ritual = 'ritual_ZN16QWindowContainer5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QWindowContainer5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(ev))

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, a0: Optional[QObject], ev: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWindowContainer::eventFilter(QObject *a0, QEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qwindowcontainer.html#eventFilter

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ev : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWindowContainer::eventFilter(QObject *a0, QEvent *ev)
    ritual = 'ritual_ZN16QWindowContainer11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QWindowContainer11eventFilterEP7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(a0, 'QObject'), self._addressOf(ev),
    )

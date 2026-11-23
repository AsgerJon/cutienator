"""
QWidgetAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qwidgetaction.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtGui import QAction

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidgetAction(QAction):
  """
  The cute side of Qt's QWidgetAction: a plain Python object standing in
  front of one C++ QWidgetAction.

  It is built on the cute 'QAction', as Qt's QWidgetAction is built on Qt's
  QAction, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWidgetAction that has a ritual and that Python can
  call so far, 11 names in all: 'metaObject', 'tr', 'setDefaultWidget',
  'defaultWidget', 'requestWidget', 'releaseWidget', 'event', 'eventFilter',
  'createWidget', 'deleteWidget', 'createdWidgets'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWidgetActionPrivate *QWidgetAction::d_func()': gives
    'QWidgetActionPrivate', which has no cute class yet.
  - Qt's 'const QWidgetActionPrivate *QWidgetAction::d_func() const': gives
    'QWidgetActionPrivate', which has no cute class yet.
  - Qt's 'QWidgetAction::~QWidgetAction()': the destructor: Python never
    removes a C++ QWidgetAction.

  What has no ritual
  ------------------

  6 of the 21 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QWidgetAction is created at the first use, not by
    'QWidgetAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidgetAction.
  - Qt tells when it has removed the C++ QWidgetAction. Every call on the
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
    Calls Qt's 'QString QWidgetAction::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#tr

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
    #  QString QWidgetAction::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QWidgetAction2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetAction'

  #  A C++ QWidgetAction Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWidgetAction'

  #  The functions Qt calls itself that QWidgetAction is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createWidget': (
          ('_ZN13QWidgetAction12createWidgetEP7QWidget',
           ('address', 'address', 'QtWidgets:QWidget'),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'deleteWidget': (
          ('_ZN13QWidgetAction12deleteWidgetEP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWidgetAction::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWidgetAction::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QWidgetAction10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def defaultWidget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetAction::defaultWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#defaultWidget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetAction::defaultWidget() const
    address = self.uglySide.call(
        'ritual_ZNK13QWidgetAction13defaultWidgetEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def createdWidgets(self) -> QList[QWidget]:
    """
    Calls Qt's 'QList<QWidget *> QWidgetAction::createdWidgets() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#createdWidgets

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWidget *> QWidgetAction::createdWidgets() const
    address = self.uglySide.call(
        'ritual_ZNK13QWidgetAction14createdWidgetsEv',
    )
    from . import QWidget
    return QList[QWidget]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def setDefaultWidget(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidgetAction::setDefaultWidget(QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetaction.html#setDefaultWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetAction::setDefaultWidget(QWidget *w)
    self.uglySide.call(
        'ritual_ZN13QWidgetAction16setDefaultWidgetEP7QWidget',
        self._addressOf(w),
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QWidgetAction::QWidgetAction(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#QWidgetAction

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWidgetAction::QWidgetAction(QObject *parent)
    self._noteCreation(QWidgetAction, lambda: Rituals.call(
        'ritual_ZN13QWidgetActionC1EP7QObject', self._addressOf(parent),
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

  @overload(QWidget)
  @overload(NoneType)
  def requestWidget(self, parent: Optional[QWidget]) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetAction::requestWidget(QWidget *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#requestWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetAction::requestWidget(QWidget *parent)
    address = self.uglySide.call(
        'ritual_ZN13QWidgetAction13requestWidgetEP7QWidget',
        self._addressOf(parent),
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def releaseWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidgetAction::releaseWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#releaseWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetAction::releaseWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN13QWidgetAction13releaseWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWidgetAction::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetAction::event(QEvent *a0)
    ritual = 'ritual_ZN13QWidgetAction5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QWidgetAction5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QWidgetAction::eventFilter(QObject *a0, QEvent *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#eventFilter

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetAction::eventFilter(QObject *a0, QEvent *a1)
    ritual = 'ritual_ZN13QWidgetAction11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QWidgetAction11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QWidget)
  @overload(NoneType)
  def createWidget(self, parent: Optional[QWidget]) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QWidgetAction::createWidget(QWidget *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#createWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QWidgetAction::createWidget(QWidget *parent)
    ritual = 'ritual_ZN13QWidgetAction12createWidgetEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QWidgetAction12createWidgetEP7QWidget'
    address = self.uglySide.call(ritual, self._addressOf(parent))
    from . import QWidget
    return QWidget._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def deleteWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidgetAction::deleteWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetaction.html#deleteWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetAction::deleteWidget(QWidget *widget)
    ritual = 'ritual_ZN13QWidgetAction12deleteWidgetEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QWidgetAction12deleteWidgetEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(widget))

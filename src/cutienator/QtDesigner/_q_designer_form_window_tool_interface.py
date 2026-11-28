"""
QDesignerFormWindowToolInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractformwindowtool.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QAction
  from ..QtWidgets import QWidget
  from . import DomUI, QDesignerFormEditorInterface
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomUI = WAIT['DomUI']
  QEvent = WAIT['QEvent']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerFormWindowToolInterface(QObject):
  """
  The cute side of Qt's QDesignerFormWindowToolInterface: a plain Python
  object standing in front of one C++ QDesignerFormWindowToolInterface.

  It is built on the cute 'QObject', as Qt's QDesignerFormWindowToolInterface
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerFormWindowToolInterface that has a ritual
  and that Python can call so far, 11 names in all: 'metaObject', 'tr',
  'core', 'formWindow', 'editor', 'action', 'activated', 'deactivated',
  'saveToDom', 'loadFromDom', 'handleEvent'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerFormWindowToolInterface::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QDesignerFormWindowToolInterface::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QDesignerFormWindowToolInterface::~QDesignerFormWindowToolInterface()':
    the destructor: Python never removes a C++
    QDesignerFormWindowToolInterface.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerFormWindowToolInterface is created at the first use, not
    by 'QDesignerFormWindowToolInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerFormWindowToolInterface.
  - Qt tells when it has removed the C++ QDesignerFormWindowToolInterface.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QDesignerFormWindowToolInterface::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowtoolinterface.html#tr

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
    #  QString QDesignerFormWindowToolInterface::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN32QDesignerFormWindowToolInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerFormWindowToolInterface'

  #  A C++ QDesignerFormWindowToolInterface Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerFormWindowToolInterface'

  #  The functions Qt calls itself that QDesignerFormWindowToolInterface is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'core': (
          ('_ZNK32QDesignerFormWindowToolInterface4coreEv',
           ('address', 'address', 'QtDesigner:QDesignerFormEditorInterface'),
           ()),
      ),
      'formWindow': (
          ('_ZNK32QDesignerFormWindowToolInterface10formWindowEv',
           ('address', 'address', 'QtDesigner:QDesignerFormWindowInterface'),
           ()),
      ),
      'editor': (
          ('_ZNK32QDesignerFormWindowToolInterface6editorEv',
           ('address', 'address', 'QtWidgets:QWidget'),
           ()),
      ),
      'action': (
          ('_ZNK32QDesignerFormWindowToolInterface6actionEv',
           ('address', 'address', 'QtGui:QAction'),
           ()),
      ),
      'activated': (
          ('_ZN32QDesignerFormWindowToolInterface9activatedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'deactivated': (
          ('_ZN32QDesignerFormWindowToolInterface11deactivatedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'saveToDom': (
          ('_ZN32QDesignerFormWindowToolInterface9saveToDomEP5DomUIP7QWidge'
           't',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDesigner:DomUI'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'loadFromDom': (
          ('_ZN32QDesignerFormWindowToolInterface11loadFromDomEP5DomUIP7QWi'
           'dget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtDesigner:DomUI'),
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'handleEvent': (
          ('_ZN32QDesignerFormWindowToolInterface11handleEventEP7QWidgetS1_'
           'P6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtWidgets:QWidget'),
               ('address', 'address', 'QtCore:QEvent'),
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
    Calls Qt's 'const QMetaObject
    *QDesignerFormWindowToolInterface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowtoolinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerFormWindowToolInterface::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QDesignerFormWindowToolInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *QDesignerFormWindowToolInterface::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowtoolinterface.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface *QDesignerFormWindowToolInterface::core()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QDesignerFormWindowToolInterface4coreEv',
    )
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  def formWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *QDesignerFormWindowToolInterface::formWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowtoolinterface.html#formWindow

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *QDesignerFormWindowToolInterface::formWindow() const
    address = self.uglySide.call(
        'ritual_ZNK32QDesignerFormWindowToolInterface10formWindowEv',
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  def editor(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QDesignerFormWindowToolInterface::editor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowtoolinterface.html#editor

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QDesignerFormWindowToolInterface::editor() const
    address = self.uglySide.call(
        'ritual_ZNK32QDesignerFormWindowToolInterface6editorEv',
    )
    from ..QtWidgets import QWidget
    return QWidget._cuteAt(address)

  def action(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerFormWindowToolInterface::action() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowtoolinterface.html#action

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerFormWindowToolInterface::action() const
    address = self.uglySide.call(
        'ritual_ZNK32QDesignerFormWindowToolInterface6actionEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

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
    'QDesignerFormWindowToolInterface::QDesignerFormWindowToolInterface(
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowtoolinterface.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerFormWindowToolInterface::
    #      QDesignerFormWindowToolInterface(QObject *parent)
    self._noteCreation(
        QDesignerFormWindowToolInterface, lambda: Rituals.call(
            'ritual_ZN32QDesignerFormWindowToolInterfaceC1EP7QObject',
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

  def activated(self) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowToolInterface::activated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowtoolinterface.html#activated
    """
    #  void QDesignerFormWindowToolInterface::activated()
    self.uglySide.call(
        'ritual_ZN32QDesignerFormWindowToolInterface9activatedEv',
    )

  def deactivated(self) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowToolInterface::deactivated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowtoolinterface.html#deactivated
    """
    #  void QDesignerFormWindowToolInterface::deactivated()
    self.uglySide.call(
        'ritual_ZN32QDesignerFormWindowToolInterface11deactivatedEv',
    )

  @overload(DomUI, QWidget)
  @overload(DomUI, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def saveToDom(self, a0: Optional[DomUI], a1: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowToolInterface::saveToDom(DomUI *a0,
    QWidget *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowtoolinterface.html#saveToDom

    Parameters
    ----------

    a0 : Optional[DomUI]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowToolInterface::saveToDom(DomUI *a0, QWidget
    #      *a1)
    ritual = (
        'ritual_ZN32QDesignerFormWindowToolInterface9saveToDomEP5DomUIP7QWi'
        'dget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QDesignerFormWindowToolInterface9saveToDomEP5DomU'
          'IP7QWidget')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(a1))

  @overload(DomUI, QWidget)
  @overload(DomUI, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def loadFromDom(self, a0: Optional[DomUI], a1: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDesignerFormWindowToolInterface::loadFromDom(DomUI *a0,
    QWidget *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowtoolinterface.html#loadFromDom

    Parameters
    ----------

    a0 : Optional[DomUI]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerFormWindowToolInterface::loadFromDom(DomUI *a0, QWidget
    #      *a1)
    ritual = (
        'ritual_ZN32QDesignerFormWindowToolInterface11loadFromDomEP5DomUIP7'
        'QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QDesignerFormWindowToolInterface11loadFromDomEP5D'
          'omUIP7QWidget')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(a1))

  @overload(QWidget, QWidget, QEvent)
  @overload(QWidget, QWidget, NoneType)
  @overload(QWidget, NoneType, QEvent)
  @overload(QWidget, NoneType, NoneType)
  @overload(NoneType, QWidget, QEvent)
  @overload(NoneType, QWidget, NoneType)
  @overload(NoneType, NoneType, QEvent)
  @overload(NoneType, NoneType, NoneType)
  def handleEvent(
      self,
      widget: Optional[QWidget],
      managedWidget: Optional[QWidget],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QDesignerFormWindowToolInterface::handleEvent(QWidget
    *widget, QWidget *managedWidget, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerformwindowtoolinterface.html#handleEvent

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    managedWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerFormWindowToolInterface::handleEvent(QWidget *widget,
    #      QWidget *managedWidget, QEvent *event)
    return self.uglySide.call(
        'ritual_ZN32QDesignerFormWindowToolInterface11handleEventEP7QWidget'
        'S1_P6QEvent',
        self._addressOf(widget), self._addressOf(managedWidget),
        self._addressOf(event),
    )

"""
QToolBoxHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_toolbox_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QToolBoxHelper to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QPalette

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtWidgets import QMenu, QToolBox
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMenu = WAIT['QMenu']
  QToolBox = WAIT['QToolBox']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QToolBoxHelper(QObject):
  """
  The cute side of Qt's QToolBoxHelper: a plain Python object standing in
  front of one C++ QToolBoxHelper.

  It is built on the cute 'QObject', as Qt's QToolBoxHelper is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QToolBoxHelper that has a ritual and that Python can
  call so far, 13 names in all: 'metaObject', 'tr', 'install', 'helperOf',
  'addToolBoxContextMenuActions', 'currentItemBackgroundRole',
  'setCurrentItemBackgroundRole', 'eventFilter', 'addContextMenuActions',
  'removeCurrentPage', 'addPage', 'addPageAfter', 'changeOrder'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QToolBoxHelper::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QToolBoxHelper::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QToolBoxHelper is created at the first use, not by
    'QToolBoxHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QToolBoxHelper.
  - Qt tells when it has removed the C++ QToolBoxHelper. Every call on the
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
    Calls Qt's 'QString QToolBoxHelper::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolboxhelper.html#tr

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
    #  QString QToolBoxHelper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QToolBoxHelper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QToolBox)
  @overload(NoneType)
  def install(toolbox: Optional[QToolBox]) -> None:
    """
    Calls Qt's 'void QToolBoxHelper::install(QToolBox *toolbox)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolboxhelper.html#install

    Parameters
    ----------

    toolbox : Optional[QToolBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBoxHelper::install(QToolBox *toolbox)
    Rituals.call(
        'ritual_ZN14QToolBoxHelper7installEP8QToolBox',
        CuteMixin._addressOf(toolbox),
    )

  @staticmethod
  @overload(QToolBox)
  @overload(NoneType)
  def helperOf(toolbox: Optional[QToolBox]) -> Optional[QToolBoxHelper]:
    """
    Calls Qt's 'QToolBoxHelper *QToolBoxHelper::helperOf(const QToolBox
    *toolbox)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolboxhelper.html#helperOf

    Parameters
    ----------

    toolbox : Optional[QToolBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QToolBoxHelper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QToolBoxHelper *QToolBoxHelper::helperOf(const QToolBox *toolbox)
    address = Rituals.call(
        'ritual_ZN14QToolBoxHelper8helperOfEPK8QToolBox',
        CuteMixin._addressOf(toolbox),
    )
    return QToolBoxHelper._cuteAt(address)

  @staticmethod
  @overload(QToolBox, QMenu)
  @overload(QToolBox, NoneType)
  @overload(NoneType, QMenu)
  @overload(NoneType, NoneType)
  def addToolBoxContextMenuActions(
      toolbox: Optional[QToolBox],
      popup: Optional[QMenu],
  ) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QToolBoxHelper::addToolBoxContextMenuActions(const
    QToolBox *toolbox, QMenu *popup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolboxhelper.html#addToolBoxContextMenuActions

    Parameters
    ----------

    toolbox : Optional[QToolBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    popup : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QToolBoxHelper::addToolBoxContextMenuActions(const QToolBox
    #      *toolbox, QMenu *popup)
    address = Rituals.call(
        'ritual_ZN14QToolBoxHelper28addToolBoxContextMenuActionsEPK8QToolBo'
        'xP5QMenu',
        CuteMixin._addressOf(toolbox), CuteMixin._addressOf(popup),
    )
    from ..QtWidgets import QMenu
    return QMenu._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QToolBoxHelper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QToolBoxHelper::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolboxhelper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QToolBoxHelper::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QToolBoxHelper10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentItemBackgroundRole(self) -> QPalette.ColorRole:
    """
    Calls Qt's 'QPalette::ColorRole
    QToolBoxHelper::currentItemBackgroundRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolboxhelper.html#currentItemBackgroundRole

    Returns
    -------

    QPalette.ColorRole
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPalette.ColorRole(number)' gives.
    """
    #  QPalette::ColorRole QToolBoxHelper::currentItemBackgroundRole() const
    return QPalette.ColorRole(self.uglySide.call(
        'ritual_ZNK14QToolBoxHelper25currentItemBackgroundRoleEv',
    ))

  @overload(QMenu)
  @overload(NoneType)
  def addContextMenuActions(self, popup: Optional[QMenu]) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QToolBoxHelper::addContextMenuActions(QMenu *popup)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolboxhelper.html#addContextMenuActions

    Parameters
    ----------

    popup : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QToolBoxHelper::addContextMenuActions(QMenu *popup) const
    address = self.uglySide.call(
        'ritual_ZNK14QToolBoxHelper21addContextMenuActionsEP5QMenu',
        self._addressOf(popup),
    )
    from ..QtWidgets import QMenu
    return QMenu._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPalette.ColorRole)
  def setCurrentItemBackgroundRole(self, role: QPalette.ColorRole) -> None:
    """
    Calls Qt's 'void
    QToolBoxHelper::setCurrentItemBackgroundRole(QPalette::ColorRole role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolboxhelper.html#setCurrentItemBackgroundRole

    Parameters
    ----------

    role : QPalette.ColorRole
      Passed on as its number.
    """
    #  void QToolBoxHelper::setCurrentItemBackgroundRole(QPalette::ColorRole
    #      role)
    self.uglySide.call(
        'ritual_ZN14QToolBoxHelper28setCurrentItemBackgroundRoleEN8QPalette'
        '9ColorRoleE',
        role.value,
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

  @overload(QToolBox)
  @overload(NoneType)
  def __init__(self, toolbox: Optional[QToolBox]) -> None:
    """
    Notes what was given, for Qt's 'QToolBoxHelper::QToolBoxHelper(QToolBox
    *toolbox)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtoolboxhelper.html#QToolBoxHelper

    Parameters
    ----------

    toolbox : Optional[QToolBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QToolBoxHelper::QToolBoxHelper(QToolBox *toolbox)
    self._noteCreation(QToolBoxHelper, lambda: Rituals.call(
        'ritual_ZN14QToolBoxHelperC1EP8QToolBox', self._addressOf(toolbox),
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

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QToolBoxHelper::eventFilter(QObject *watched, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolboxhelper.html#eventFilter

    Parameters
    ----------

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QToolBoxHelper::eventFilter(QObject *watched, QEvent *event)
    ritual = 'ritual_ZN14QToolBoxHelper11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QToolBoxHelper11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(watched, 'QObject'), self._addressOf(event),
    )

  def removeCurrentPage(self) -> None:
    """
    Calls Qt's 'void QToolBoxHelper::removeCurrentPage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolboxhelper.html#removeCurrentPage
    """
    #  void QToolBoxHelper::removeCurrentPage()
    self.uglySide.call('ritual_ZN14QToolBoxHelper17removeCurrentPageEv')

  def addPage(self) -> None:
    """
    Calls Qt's 'void QToolBoxHelper::addPage()'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolboxhelper.html#addPage
    """
    #  void QToolBoxHelper::addPage()
    self.uglySide.call('ritual_ZN14QToolBoxHelper7addPageEv')

  def addPageAfter(self) -> None:
    """
    Calls Qt's 'void QToolBoxHelper::addPageAfter()'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolboxhelper.html#addPageAfter
    """
    #  void QToolBoxHelper::addPageAfter()
    self.uglySide.call('ritual_ZN14QToolBoxHelper12addPageAfterEv')

  def changeOrder(self) -> None:
    """
    Calls Qt's 'void QToolBoxHelper::changeOrder()'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolboxhelper.html#changeOrder
    """
    #  void QToolBoxHelper::changeOrder()
    self.uglySide.call('ritual_ZN14QToolBoxHelper11changeOrderEv')

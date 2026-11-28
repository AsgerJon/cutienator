"""
qdesigner_internal::ZoomMenu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::ZoomMenu to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QAction
  from ..QtWidgets import QMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QMenu = WAIT['QMenu']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ZoomMenu(QObject):
  """
  The cute side of Qt's qdesigner_internal::ZoomMenu: a plain Python object
  standing in front of one C++ qdesigner_internal::ZoomMenu.

  It is built on the cute 'QObject', as Qt's qdesigner_internal::ZoomMenu is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ZoomMenu that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'addActions', 'zoom', 'setZoom', 'zoomChanged', 'slotZoomMenu', 'zoomOf'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::ZoomMenu::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::ZoomMenu::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QList<int> qdesigner_internal::ZoomMenu::zoomValues()': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  6 of the 18 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::ZoomMenu is created at the first use, not by
    'qdesigner_internal::ZoomMenu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::ZoomMenu.
  - Qt tells when it has removed the C++ qdesigner_internal::ZoomMenu. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::ZoomMenu that has no cute function
    yet, 'zoomValues', holds a function that raises 'NotImplementedError',
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
    Calls Qt's 'QString qdesigner_internal::ZoomMenu::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoommenu.html#tr

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
    #  QString qdesigner_internal::ZoomMenu::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal8ZoomMenu2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QAction)
  @overload(NoneType)
  def zoomOf(a: Optional[QAction]) -> int:
    """
    Calls Qt's 'int qdesigner_internal::ZoomMenu::zoomOf(const QAction *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoommenu.html#zoomOf

    Parameters
    ----------

    a : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int qdesigner_internal::ZoomMenu::zoomOf(const QAction *a)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal8ZoomMenu6zoomOfEPK7QAction',
        CuteMixin._addressOf(a),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ZoomMenu'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *qdesigner_internal::ZoomMenu::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoommenu.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::ZoomMenu::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal8ZoomMenu10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def zoom(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::ZoomMenu::zoom() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoommenu.html#zoom
    """
    #  int qdesigner_internal::ZoomMenu::zoom() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal8ZoomMenu4zoomEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setZoom(self, percent: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomMenu::setZoom(int percent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoommenu.html#setZoom

    Parameters
    ----------

    percent : int
      Passed on as it is.
    """
    #  void qdesigner_internal::ZoomMenu::setZoom(int percent)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal8ZoomMenu7setZoomEi', percent,
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
    Notes what was given, for Qt's
    'qdesigner_internal::ZoomMenu::ZoomMenu(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoommenu.html#ZoomMenu

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::ZoomMenu::ZoomMenu(QObject *parent)
    self._noteCreation(ZoomMenu, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal8ZoomMenuC1EP7QObject',
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

  @overload(QMenu)
  @overload(NoneType)
  def addActions(self, m: Optional[QMenu]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomMenu::addActions(QMenu *m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoommenu.html#addActions

    Parameters
    ----------

    m : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ZoomMenu::addActions(QMenu *m)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal8ZoomMenu10addActionsEP5QMenu',
        self._addressOf(m),
    )

  @overload(int)
  def zoomChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomMenu::zoomChanged(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoommenu.html#zoomChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void qdesigner_internal::ZoomMenu::zoomChanged(int a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal8ZoomMenu11zoomChangedEi', a0,
    )

  @overload(QAction)
  @overload(NoneType)
  def slotZoomMenu(self, a0: Optional[QAction]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomMenu::slotZoomMenu(QAction
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoommenu.html#slotZoomMenu

    Parameters
    ----------

    a0 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ZoomMenu::slotZoomMenu(QAction *a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal8ZoomMenu12slotZoomMenuEP7QAction',
        self._addressOf(a0),
    )

  @staticmethod
  def zoomValues(*__, **_) -> Never:
    """
    Qt's 'QList<int> qdesigner_internal::ZoomMenu::zoomValues()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ZoomMenu.zoomValues' has no cute function yet. "
        "Qt's 'QList<int> qdesigner_internal::ZoomMenu::zoomValues()': "
        "gives a type Python has no way to take yet.")

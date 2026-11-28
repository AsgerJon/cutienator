"""
qdesigner_internal::FormLayoutMenu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/formlayoutmenu_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::FormLayoutMenu to be private: it declares the
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

  from ..QtCore import QMetaObject
  from ..QtGui import QAction
  from ..QtWidgets import QWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FormLayoutMenu(QObject):
  """
  The cute side of Qt's qdesigner_internal::FormLayoutMenu: a plain Python
  object standing in front of one C++ qdesigner_internal::FormLayoutMenu.

  It is built on the cute 'QObject', as Qt's
  qdesigner_internal::FormLayoutMenu is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::FormLayoutMenu that has a ritual
  and that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'preferredEditAction', 'slotAddRow'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::FormLayoutMenu::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::FormLayoutMenu::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void qdesigner_internal::FormLayoutMenu::populate(QWidget *w,
    QDesignerFormWindowInterface *fw, ActionList &actions)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  6 of the 14 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::FormLayoutMenu is created at the first use,
    not by 'qdesigner_internal::FormLayoutMenu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::FormLayoutMenu.
  - Qt tells when it has removed the C++ qdesigner_internal::FormLayoutMenu.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::FormLayoutMenu that has no cute
    function yet, 'populate', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString qdesigner_internal::FormLayoutMenu::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formlayoutmenu.html#tr

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
    #  QString qdesigner_internal::FormLayoutMenu::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal14FormLayoutMenu2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::FormLayoutMenu'

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
    *qdesigner_internal::FormLayoutMenu::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formlayoutmenu.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::FormLayoutMenu::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14FormLayoutMenu10metaObjectEv',
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::FormLayoutMenu::FormLayoutMenu(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formlayoutmenu.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::FormLayoutMenu::FormLayoutMenu(QObject *parent)
    self._noteCreation(FormLayoutMenu, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal14FormLayoutMenuC1EP7QObject',
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

  @overload(QWidget, QDesignerFormWindowInterface)
  @overload(QWidget, NoneType)
  @overload(NoneType, QDesignerFormWindowInterface)
  @overload(NoneType, NoneType)
  def preferredEditAction(
      self,
      w: Optional[QWidget],
      fw: Optional[QDesignerFormWindowInterface],
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *qdesigner_internal::FormLayoutMenu::preferredEditAction(QWidget *w,
    QDesignerFormWindowInterface *fw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formlayoutmenu.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction
    #      *qdesigner_internal::FormLayoutMenu::preferredEditAction(QWidget
    #      *w, QDesignerFormWindowInterface *fw)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormLayoutMenu19preferredEditAction'
        'EP7QWidgetP28QDesignerFormWindowInterface',
        self._addressOf(w), self._addressOf(fw),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def slotAddRow(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::FormLayoutMenu::slotAddRow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formlayoutmenu.html#slotAddRow
    """
    #  void qdesigner_internal::FormLayoutMenu::slotAddRow()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14FormLayoutMenu10slotAddRowEv',
    )

  @staticmethod
  def populate(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::FormLayoutMenu::populate(QWidget *w,
    QDesignerFormWindowInterface *fw, ActionList &actions)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.FormLayoutMenu.populate' has no cute function "
        "yet. Qt's 'void "
        "qdesigner_internal::FormLayoutMenu::populate(QWidget *w, "
        "QDesignerFormWindowInterface *fw, ActionList &actions)': takes a "
        "type Python has no way to hand over yet.")

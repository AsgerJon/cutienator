"""
qdesigner_internal::MorphMenu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/morphmenu_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::MorphMenu to be private: it declares the
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


class MorphMenu(QObject):
  """
  The cute side of Qt's qdesigner_internal::MorphMenu: a plain Python object
  standing in front of one C++ qdesigner_internal::MorphMenu.

  It is built on the cute 'QObject', as Qt's qdesigner_internal::MorphMenu is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::MorphMenu that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr',
  'slotMorph', 'populateMenu'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::MorphMenu::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::MorphMenu::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void qdesigner_internal::MorphMenu::populate(QWidget *w,
    QDesignerFormWindowInterface *fw, ActionList &al)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void qdesigner_internal::MorphMenu::populate(QWidget *w,
    QDesignerFormWindowInterface *fw, QMenu &m)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  6 of the 15 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::MorphMenu is created at the first use, not by
    'qdesigner_internal::MorphMenu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::MorphMenu.
  - Qt tells when it has removed the C++ qdesigner_internal::MorphMenu. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::MorphMenu that has no cute function
    yet, 'populate', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString qdesigner_internal::MorphMenu::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-morphmenu.html#tr

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
    #  QString qdesigner_internal::MorphMenu::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal9MorphMenu2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::MorphMenu'

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
    *qdesigner_internal::MorphMenu::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-morphmenu.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::MorphMenu::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal9MorphMenu10metaObjectEv',
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
    'qdesigner_internal::MorphMenu::MorphMenu(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-morphmenu.html#MorphMenu

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::MorphMenu::MorphMenu(QObject *parent)
    self._noteCreation(MorphMenu, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal9MorphMenuC1EP7QObject',
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

  @overload(str)
  def slotMorph(self, newClassName: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::MorphMenu::slotMorph(const QString
    &newClassName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-morphmenu.html#slotMorph

    Parameters
    ----------

    newClassName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::MorphMenu::slotMorph(const QString
    #      &newClassName)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal9MorphMenu9slotMorphERK7QString',
        newClassName,
    )

  @overload(QWidget, QDesignerFormWindowInterface)
  @overload(QWidget, NoneType)
  @overload(NoneType, QDesignerFormWindowInterface)
  @overload(NoneType, NoneType)
  def populateMenu(
      self,
      w: Optional[QWidget],
      fw: Optional[QDesignerFormWindowInterface],
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::MorphMenu::populateMenu(QWidget *w,
    QDesignerFormWindowInterface *fw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-morphmenu.html#populateMenu

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::MorphMenu::populateMenu(QWidget *w,
    #      QDesignerFormWindowInterface *fw)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal9MorphMenu12populateMenuEP7QWidgetP28'
        'QDesignerFormWindowInterface',
        self._addressOf(w), self._addressOf(fw),
    )

  @staticmethod
  def populate(*__, **_) -> Never:
    """
    - Qt's 'void qdesigner_internal::MorphMenu::populate(QWidget *w,
      QDesignerFormWindowInterface *fw, ActionList &al)': takes a type Python
      has no way to hand over yet.
    - Qt's 'void qdesigner_internal::MorphMenu::populate(QWidget *w,
      QDesignerFormWindowInterface *fw, QMenu &m)': takes a type Python has
      no way to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.MorphMenu.populate' has no cute function yet. "
        "Qt's 'void qdesigner_internal::MorphMenu::populate(QWidget *w, "
        "QDesignerFormWindowInterface *fw, ActionList &al)': takes a type "
        "Python has no way to hand over yet. Qt's 'void "
        "qdesigner_internal::MorphMenu::populate(QWidget *w, "
        "QDesignerFormWindowInterface *fw, QMenu &m)': takes a type Python "
        "has no way to hand over yet.")

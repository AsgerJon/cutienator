"""
qdesigner_internal::PromotionTaskMenu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/promotiontaskmenu_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PromotionTaskMenu to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtWidgets import QMenu, QWidget
  from . import QDesignerFormEditorInterface, QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QMenu = WAIT['QMenu']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PromotionTaskMenu(QObject):
  """
  The cute side of Qt's qdesigner_internal::PromotionTaskMenu: a plain Python
  object standing in front of one C++ qdesigner_internal::PromotionTaskMenu.

  It is built on the cute 'QObject', as Qt's
  qdesigner_internal::PromotionTaskMenu is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::PromotionTaskMenu that has a
  ritual and that Python can call so far, 17 names in all: 'metaObject',
  'tr', 'mode', 'setMode', 'setWidget', 'setPromoteLabel',
  'setEditPromoteToLabel', 'setDemoteLabel', 'addActions',
  'editPromotedWidgets', 'slotPromoteToCustomWidget',
  'slotDemoteFromCustomWidget', 'slotEditPromotedWidgets',
  'slotEditPromoteTo', 'slotEditSignalsSlots', 'promoteTo', 'formWindow'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::PromotionTaskMenu::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::PromotionTaskMenu::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void qdesigner_internal::PromotionTaskMenu::addActions(
    QDesignerFormWindowInterface *fw, unsigned int flags, ActionList
    &actionList)': takes a type Python has no way to hand over yet.
  - Qt's 'void qdesigner_internal::PromotionTaskMenu::addActions(unsigned int
    flags, ActionList &actionList)': takes a type Python has no way to hand
    over yet.
  - Qt's 'PromotionState
    qdesigner_internal::PromotionTaskMenu::createPromotionActions(
    QDesignerFormWindowInterface *formWindow)': gives the enum
    'qdesigner_internal::PromotionTaskMenu::PromotionState', whose class
    cannot be named here.
  - Qt's 'PromotionSelectionList
    qdesigner_internal::PromotionTaskMenu::promotionSelectionList(
    QDesignerFormWindowInterface *formWindow) const': gives a type Python has
    no way to take yet.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::PromotionTaskMenu is created at the first
    use, not by 'qdesigner_internal::PromotionTaskMenu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::PromotionTaskMenu.
  - Qt tells when it has removed the C++
    qdesigner_internal::PromotionTaskMenu. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's qdesigner_internal::PromotionTaskMenu that has no cute
    function yet, 'createPromotionActions', 'promotionSelectionList', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside qdesigner_internal::PromotionTaskMenu, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class AddFlags(CuteNum):
    """
    The enum 'qdesigner_internal::PromotionTaskMenu::AddFlags' of Qt, with
    the 3 names Qt gives in it.
    """

    LeadingSeparator = Kee[int](1)
    TrailingSeparator = Kee[int](2)
    SuppressGlobalEdit = Kee[int](4)

  class Mode(CuteNum):
    """
    The enum 'qdesigner_internal::PromotionTaskMenu::Mode' of Qt, with the 3
    names Qt gives in it.
    """

    ModeSingleWidget = Kee[int](0)
    ModeManagedMultiSelection = Kee[int](1)
    ModeUnmanagedMultiSelection = Kee[int](2)

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
    Calls Qt's 'QString qdesigner_internal::PromotionTaskMenu::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html#tr

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
    #  QString qdesigner_internal::PromotionTaskMenu::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def editPromotedWidgets(
      core: Optional[QDesignerFormEditorInterface],
      parent: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromotionTaskMenu::editPromotedWidgets(
    QDesignerFormEditorInterface *core, QWidget *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::PromotionTaskMenu::editPromotedWidgets(
    #      QDesignerFormEditorInterface *core, QWidget *parent)
    Rituals.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu19editPromotedWidg'
        'etsEP28QDesignerFormEditorInterfaceP7QWidget',
        CuteMixin._addressOf(core), CuteMixin._addressOf(parent),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::PromotionTaskMenu'

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
    *qdesigner_internal::PromotionTaskMenu::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::PromotionTaskMenu::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17PromotionTaskMenu10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mode(self) -> Mode:
    """
    Calls Qt's 'Mode qdesigner_internal::PromotionTaskMenu::mode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html#mode

    Returns
    -------

    Mode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Mode(number)' gives.
    """
    #  Mode qdesigner_internal::PromotionTaskMenu::mode() const
    return PromotionTaskMenu.Mode(self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17PromotionTaskMenu4modeEv',
    ))

  def formWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *qdesigner_internal::PromotionTaskMenu::formWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *qdesigner_internal::PromotionTaskMenu::formWindow() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17PromotionTaskMenu10formWindowEv',
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Mode)
  def setMode(self, m: Mode) -> None:
    """
    Calls Qt's 'void qdesigner_internal::PromotionTaskMenu::setMode(Mode m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html#setMode

    Parameters
    ----------

    m : Mode
      Passed on as its number.
    """
    #  void qdesigner_internal::PromotionTaskMenu::setMode(Mode m)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu7setModeENS0_4Mode'
        'E',
        m.value,
    )

  @overload(QWidget)
  @overload(NoneType)
  def setWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::PromotionTaskMenu::setWidget(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::PromotionTaskMenu::setWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu9setWidgetEP7QWidg'
        'et',
        self._addressOf(widget),
    )

  @overload(str)
  def setPromoteLabel(self, promoteLabel: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromotionTaskMenu::setPromoteLabel(const QString
    &promoteLabel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html

    Parameters
    ----------

    promoteLabel : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PromotionTaskMenu::setPromoteLabel(const
    #      QString &promoteLabel)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu15setPromoteLabelE'
        'RK7QString',
        promoteLabel,
    )

  @overload(str)
  def setEditPromoteToLabel(self, promoteEditLabel: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromotionTaskMenu::setEditPromoteToLabel(const
    QString &promoteEditLabel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html

    Parameters
    ----------

    promoteEditLabel : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void
    #      qdesigner_internal::PromotionTaskMenu::setEditPromoteToLabel(const
    #      QString &promoteEditLabel)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu21setEditPromoteTo'
        'LabelERK7QString',
        promoteEditLabel,
    )

  @overload(str)
  def setDemoteLabel(self, demoteLabel: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromotionTaskMenu::setDemoteLabel(const QString
    &demoteLabel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html

    Parameters
    ----------

    demoteLabel : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PromotionTaskMenu::setDemoteLabel(const
    #      QString &demoteLabel)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu14setDemoteLabelER'
        'K7QString',
        demoteLabel,
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

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Mode)
  @overload(NoneType, Mode)
  @overload(QWidget, Mode, QObject)
  @overload(QWidget, Mode, NoneType)
  @overload(NoneType, Mode, QObject)
  @overload(NoneType, Mode, NoneType)
  def __init__(
      self,
      widget: Optional[QWidget],
      mode: Mode = Mode.ModeManagedMultiSelection,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PromotionTaskMenu::PromotionTaskMenu(QWidget
    *widget, Mode mode, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.ModeManagedMultiSelection.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::PromotionTaskMenu::PromotionTaskMenu(QWidget
    #      *widget, Mode mode, QObject *parent)
    self._noteCreation(PromotionTaskMenu, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenuC1EP7QWidgetNS0_4M'
        'odeEP7QObject',
        self._addressOf(widget), mode.value, self._addressOf(parent,
        'QObject'),
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

  @overload(QDesignerFormWindowInterface, int, QMenu)
  @overload(QDesignerFormWindowInterface, int, NoneType)
  @overload(NoneType, int, QMenu)
  @overload(NoneType, int, NoneType)
  def addActions(
      self,
      fw: Optional[QDesignerFormWindowInterface],
      flags: int,
      menu: Optional[QMenu],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::PromotionTaskMenu::addActions(
    QDesignerFormWindowInterface *fw, unsigned int flags, QMenu *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : int
      Passed on as it is.

    menu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::PromotionTaskMenu::addActions(
    #      QDesignerFormWindowInterface *fw, unsigned int flags, QMenu *menu)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu10addActionsEP28QD'
        'esignerFormWindowInterfacejP5QMenu',
        self._addressOf(fw), flags, self._addressOf(menu),
    )

  @overload(int, QMenu)
  @overload(int, NoneType)
  def addActions(self, flags: int, menu: Optional[QMenu]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromotionTaskMenu::addActions(unsigned int flags,
    QMenu *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html

    Parameters
    ----------

    flags : int
      Passed on as it is.

    menu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::PromotionTaskMenu::addActions(unsigned int
    #      flags, QMenu *menu)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu10addActionsEjP5QM'
        'enu',
        flags, self._addressOf(menu),
    )

  @overload(str)
  def slotPromoteToCustomWidget(self, customClassName: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromotionTaskMenu::slotPromoteToCustomWidget(const
    QString &customClassName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html

    Parameters
    ----------

    customClassName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PromotionTaskMenu::slotPromoteToCustomWidget(
    #      const QString &customClassName)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu25slotPromoteToCus'
        'tomWidgetERK7QString',
        customClassName,
    )

  def slotDemoteFromCustomWidget(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromotionTaskMenu::slotDemoteFromCustomWidget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html
    """
    #  void
    #      qdesigner_internal::PromotionTaskMenu::slotDemoteFromCustomWidget(
    #      )
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu26slotDemoteFromCu'
        'stomWidgetEv',
    )

  def slotEditPromotedWidgets(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromotionTaskMenu::slotEditPromotedWidgets()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html
    """
    #  void qdesigner_internal::PromotionTaskMenu::slotEditPromotedWidgets()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu23slotEditPromoted'
        'WidgetsEv',
    )

  def slotEditPromoteTo(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromotionTaskMenu::slotEditPromoteTo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html
    """
    #  void qdesigner_internal::PromotionTaskMenu::slotEditPromoteTo()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu17slotEditPromoteT'
        'oEv',
    )

  def slotEditSignalsSlots(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PromotionTaskMenu::slotEditSignalsSlots()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html
    """
    #  void qdesigner_internal::PromotionTaskMenu::slotEditSignalsSlots()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu20slotEditSignalsS'
        'lotsEv',
    )

  @overload(QDesignerFormWindowInterface, str)
  @overload(NoneType, str)
  def promoteTo(
      self,
      fw: Optional[QDesignerFormWindowInterface],
      customClassName: str,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::PromotionTaskMenu::promoteTo(
    QDesignerFormWindowInterface *fw, const QString &customClassName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-promotiontaskmenu.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    customClassName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PromotionTaskMenu::promoteTo(
    #      QDesignerFormWindowInterface *fw, const QString &customClassName)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal17PromotionTaskMenu9promoteToEP28QDes'
        'ignerFormWindowInterfaceRK7QString',
        self._addressOf(fw), customClassName,
    )

  @staticmethod
  def createPromotionActions(*__, **_) -> Never:
    """
    Qt's 'PromotionState
    qdesigner_internal::PromotionTaskMenu::createPromotionActions(
    QDesignerFormWindowInterface *formWindow)': gives the enum
    'qdesigner_internal::PromotionTaskMenu::PromotionState', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'qdesigner_internal.PromotionTaskMenu.createPromotionActions' has "
        "no cute function yet. Qt's 'PromotionState "
        "qdesigner_internal::PromotionTaskMenu::createPromotionActions(QDesi"
        "gnerFormWindowInterface *formWindow)': gives the enum "
        "'qdesigner_internal::PromotionTaskMenu::PromotionState', whose "
        "class cannot be named here.")

  @staticmethod
  def promotionSelectionList(*__, **_) -> Never:
    """
    Qt's 'PromotionSelectionList
    qdesigner_internal::PromotionTaskMenu::promotionSelectionList(
    QDesignerFormWindowInterface *formWindow) const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.PromotionTaskMenu.promotionSelectionList' has "
        "no cute function yet. Qt's 'PromotionSelectionList "
        "qdesigner_internal::PromotionTaskMenu::promotionSelectionList(QDesi"
        "gnerFormWindowInterface *formWindow) const': gives a type Python "
        "has no way to take yet.")

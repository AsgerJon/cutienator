"""
qdesigner_internal::ActionEditor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/actioneditor_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::ActionEditor to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from ..QtWidgets import QWidget
from . import qdesigner_internal, QDesignerActionEditorInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QItemSelection, QMetaObject
  from ..QtGui import QAction, QContextMenuEvent
  from ..QtWidgets import QMenu
  from . import QDesignerFormEditorInterface, QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QItemSelection = WAIT['QItemSelection']
  QMenu = WAIT['QMenu']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ActionEditor(QDesignerActionEditorInterface):
  """
  The cute side of Qt's qdesigner_internal::ActionEditor: a plain Python
  object standing in front of one C++ qdesigner_internal::ActionEditor.

  It is built on the cute 'QDesignerActionEditorInterface', as Qt's
  qdesigner_internal::ActionEditor is built on Qt's
  QDesignerActionEditorInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ActionEditor that has a ritual
  and that Python can call so far, 39 names in all: 'metaObject', 'tr',
  'formWindow', 'setFormWindow', 'core', 'actionNew', 'actionDelete',
  'filter', 'manageAction', 'unmanageAction', 'objectNamingMode',
  'setObjectNamingMode', 'actionTextToName', 'setFilter',
  'mainContainerChanged', 'clearSelection', 'selectAction',
  'slotCurrentItemChanged', 'slotSelectionChanged', 'editAction',
  'editCurrentAction', 'navigateToSlotCurrentAction', 'slotActionChanged',
  'slotNewAction', 'slotDelete', 'resourceImageDropped',
  'slotContextMenuRequested', 'slotViewMode', 'slotSelectAssociatedWidget',
  'slotCopy', 'slotCut', 'slotPaste', 'itemActivated',
  'contextMenuRequested', 'deleteActions', 'copyActions', 'restoreSettings',
  'saveSettings', 'updateViewModeActions'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::ActionEditor::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::ActionEditor::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::ActionEditor::~ActionEditor()': the destructor:
    Python never removes a C++ qdesigner_internal::ActionEditor.
  - Qt's 'QToolButton
    *qdesigner_internal::ActionEditor::createConfigureMenuButton(const
    QString &t, QMenu **ptrToMenu)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  2 of the 46 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::ActionEditor is created at the first use, not
    by 'qdesigner_internal::ActionEditor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::ActionEditor.
  - Qt tells when it has removed the C++ qdesigner_internal::ActionEditor.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::ActionEditor that has no cute
    function yet, 'createConfigureMenuButton', holds a function that raises
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
    Calls Qt's 'QString qdesigner_internal::ActionEditor::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#tr

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
    #  QString qdesigner_internal::ActionEditor::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal12ActionEditor2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def objectNamingMode() -> qdesigner_internal.ObjectNamingMode:
    """
    Calls Qt's 'ObjectNamingMode
    qdesigner_internal::ActionEditor::objectNamingMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html

    Returns
    -------

    qdesigner_internal.ObjectNamingMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'qdesigner_internal.ObjectNamingMode(number)' gives.
    """
    #  ObjectNamingMode qdesigner_internal::ActionEditor::objectNamingMode()
    return qdesigner_internal.ObjectNamingMode(Rituals.call(
        'ritual_ZN18qdesigner_internal12ActionEditor16objectNamingModeEv',
    ))

  @staticmethod
  @overload(qdesigner_internal.ObjectNamingMode)
  def setObjectNamingMode(n: qdesigner_internal.ObjectNamingMode) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionEditor::setObjectNamingMode(ObjectNamingMode
    n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html

    Parameters
    ----------

    n : qdesigner_internal.ObjectNamingMode
      Passed on as its number.
    """
    #  void qdesigner_internal::ActionEditor::setObjectNamingMode(
    #      ObjectNamingMode n)
    Rituals.call(
        'ritual_ZN18qdesigner_internal12ActionEditor19setObjectNamingModeEN'
        'S_16ObjectNamingModeE',
        n.value,
    )

  @staticmethod
  @overload(str, str)
  def actionTextToName(text: str, prefix: str) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::ActionEditor::actionTextToName(const QString &text,
    const QString &prefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::ActionEditor::actionTextToName(const
    #      QString &text, const QString &prefix)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal12ActionEditor16actionTextToNameERK7Q'
        'StringS3_',
        text, prefix,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ActionEditor'

  #  A C++ qdesigner_internal::ActionEditor Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_ActionEditor'

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
    *qdesigner_internal::ActionEditor::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::ActionEditor::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12ActionEditor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def formWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *qdesigner_internal::ActionEditor::formWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#formWindow

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *qdesigner_internal::ActionEditor::formWindow() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12ActionEditor10formWindowEv',
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  def core(self) -> Optional[QDesignerFormEditorInterface]:
    """
    Calls Qt's 'QDesignerFormEditorInterface
    *qdesigner_internal::ActionEditor::core() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#core

    Returns
    -------

    Optional[QDesignerFormEditorInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormEditorInterface *qdesigner_internal::ActionEditor::core()
    #      const
    ritual = 'ritual_ZNK18qdesigner_internal12ActionEditor4coreEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18qdesigner_internal12ActionEditor4coreEv'
    address = self.uglySide.call(ritual)
    from . import QDesignerFormEditorInterface
    return QDesignerFormEditorInterface._cuteAt(address)

  def actionNew(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *qdesigner_internal::ActionEditor::actionNew()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#actionNew

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *qdesigner_internal::ActionEditor::actionNew() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12ActionEditor9actionNewEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def actionDelete(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *qdesigner_internal::ActionEditor::actionDelete()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#actionDelete

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *qdesigner_internal::ActionEditor::actionDelete() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12ActionEditor12actionDeleteEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def filter(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::ActionEditor::filter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#filter

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::ActionEditor::filter() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal12ActionEditor6filterEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDesignerFormWindowInterface)
  @overload(NoneType)
  def setFormWindow(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::setFormWindow(
    QDesignerFormWindowInterface *formWindow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#setFormWindow

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionEditor::setFormWindow(
    #      QDesignerFormWindowInterface *formWindow)
    ritual = (
        'ritual_ZN18qdesigner_internal12ActionEditor13setFormWindowEP28QDes'
        'ignerFormWindowInterface')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal12ActionEditor13setFormWindowEP'
          '28QDesignerFormWindowInterface')
    self.uglySide.call(ritual, self._addressOf(formWindow))

  @overload(str)
  def setFilter(self, filter: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::setFilter(const
    QString &filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#setFilter

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::ActionEditor::setFilter(const QString
    #      &filter)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor9setFilterERK7QString',
        filter,
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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  @overload(QDesignerFormEditorInterface, QWidget, Qt.WindowFlags)
  @overload(QDesignerFormEditorInterface, NoneType, Qt.WindowFlags)
  @overload(NoneType, QWidget, Qt.WindowFlags)
  @overload(NoneType, NoneType, Qt.WindowFlags)
  def __init__(
      self,
      core: Optional[QDesignerFormEditorInterface],
      parent: Optional[QWidget] = None,
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::ActionEditor::ActionEditor(
    QDesignerFormEditorInterface *core, QWidget *parent, Qt::WindowFlags
    flags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#ActionEditor

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  qdesigner_internal::ActionEditor::ActionEditor(
    #      QDesignerFormEditorInterface *core, QWidget *parent,
    #      Qt::WindowFlags flags)
    self._noteCreation(ActionEditor, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal12ActionEditorC1EP28QDesignerFormEdit'
        'orInterfaceP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(core), self._addressOf(parent), flags.value,
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

  @overload(QAction)
  @overload(NoneType)
  def manageAction(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::manageAction(QAction
    *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#manageAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionEditor::manageAction(QAction *action)
    ritual = (
        'ritual_ZN18qdesigner_internal12ActionEditor12manageActionEP7QActio'
        'n')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal12ActionEditor12manageActionEP7'
          'QAction')
    self.uglySide.call(ritual, self._addressOf(action))

  @overload(QAction)
  @overload(NoneType)
  def unmanageAction(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::unmanageAction(QAction
    *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionEditor::unmanageAction(QAction *action)
    ritual = (
        'ritual_ZN18qdesigner_internal12ActionEditor14unmanageActionEP7QAct'
        'ion')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal12ActionEditor14unmanageActionE'
          'P7QAction')
    self.uglySide.call(ritual, self._addressOf(action))

  def mainContainerChanged(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionEditor::mainContainerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html
    """
    #  void qdesigner_internal::ActionEditor::mainContainerChanged()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor20mainContainerChangedE'
        'v',
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html
    """
    #  void qdesigner_internal::ActionEditor::clearSelection()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor14clearSelectionEv',
    )

  @overload(QAction)
  @overload(NoneType)
  def selectAction(self, a: Optional[QAction]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::selectAction(QAction
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#selectAction

    Parameters
    ----------

    a : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionEditor::selectAction(QAction *a)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor12selectActionEP7QActio'
        'n',
        self._addressOf(a),
    )

  @overload(QAction)
  @overload(NoneType)
  def slotCurrentItemChanged(self, item: Optional[QAction]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionEditor::slotCurrentItemChanged(QAction *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html

    Parameters
    ----------

    item : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionEditor::slotCurrentItemChanged(QAction
    #      *item)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor22slotCurrentItemChange'
        'dEP7QAction',
        self._addressOf(item),
    )

  @overload(QItemSelection, QItemSelection)
  def slotSelectionChanged(
      self,
      selected: QItemSelection,
      deselected: QItemSelection,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionEditor::slotSelectionChanged(const
    QItemSelection &selected, const QItemSelection &deselected)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html

    Parameters
    ----------

    selected : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    deselected : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.
    """
    #  void qdesigner_internal::ActionEditor::slotSelectionChanged(const
    #      QItemSelection &selected, const QItemSelection &deselected)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor20slotSelectionChangedE'
        'RK14QItemSelectionS3_',
        self._valueOf(selected), self._valueOf(deselected),
    )

  @overload(QAction)
  @overload(NoneType)
  @overload(QAction, int)
  @overload(NoneType, int)
  def editAction(self, item: Optional[QAction], column: int = -1) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::editAction(QAction
    *item, int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#editAction

    Parameters
    ----------

    item : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void qdesigner_internal::ActionEditor::editAction(QAction *item, int
    #      column)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor10editActionEP7QActioni',
        self._addressOf(item), column,
    )

  def editCurrentAction(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::editCurrentAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html
    """
    #  void qdesigner_internal::ActionEditor::editCurrentAction()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor17editCurrentActionEv',
    )

  def navigateToSlotCurrentAction(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionEditor::navigateToSlotCurrentAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html
    """
    #  void qdesigner_internal::ActionEditor::navigateToSlotCurrentAction()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor27navigateToSlotCurrent'
        'ActionEv',
    )

  def slotActionChanged(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::slotActionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html
    """
    #  void qdesigner_internal::ActionEditor::slotActionChanged()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor17slotActionChangedEv',
    )

  def slotNewAction(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::slotNewAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#slotNewAction
    """
    #  void qdesigner_internal::ActionEditor::slotNewAction()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor13slotNewActionEv',
    )

  def slotDelete(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::slotDelete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#slotDelete
    """
    #  void qdesigner_internal::ActionEditor::slotDelete()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor10slotDeleteEv',
    )

  @overload(str, QAction)
  @overload(str, NoneType)
  def resourceImageDropped(
      self,
      path: str,
      action: Optional[QAction],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionEditor::resourceImageDropped(const QString
    &path, QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionEditor::resourceImageDropped(const
    #      QString &path, QAction *action)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor20resourceImageDroppedE'
        'RK7QStringP7QAction',
        path, self._addressOf(action),
    )

  @overload(QContextMenuEvent, QAction)
  @overload(QContextMenuEvent, NoneType)
  @overload(NoneType, QAction)
  @overload(NoneType, NoneType)
  def slotContextMenuRequested(
      self,
      a0: Optional[QContextMenuEvent],
      a1: Optional[QAction],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionEditor::slotContextMenuRequested(
    QContextMenuEvent *a0, QAction *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html

    Parameters
    ----------

    a0 : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionEditor::slotContextMenuRequested(
    #      QContextMenuEvent *a0, QAction *a1)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor24slotContextMenuReques'
        'tedEP17QContextMenuEventP7QAction',
        self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QAction)
  @overload(NoneType)
  def slotViewMode(self, a: Optional[QAction]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::slotViewMode(QAction
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#slotViewMode

    Parameters
    ----------

    a : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionEditor::slotViewMode(QAction *a)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor12slotViewModeEP7QActio'
        'n',
        self._addressOf(a),
    )

  @overload(QWidget)
  @overload(NoneType)
  def slotSelectAssociatedWidget(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionEditor::slotSelectAssociatedWidget(QWidget
    *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionEditor::slotSelectAssociatedWidget(
    #      QWidget *w)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor26slotSelectAssociatedW'
        'idgetEP7QWidget',
        self._addressOf(w),
    )

  def slotCopy(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::slotCopy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#slotCopy
    """
    #  void qdesigner_internal::ActionEditor::slotCopy()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor8slotCopyEv',
    )

  def slotCut(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::slotCut()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#slotCut
    """
    #  void qdesigner_internal::ActionEditor::slotCut()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor7slotCutEv',
    )

  def slotPaste(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::slotPaste()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#slotPaste
    """
    #  void qdesigner_internal::ActionEditor::slotPaste()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor9slotPasteEv',
    )

  @overload(QAction, int)
  @overload(NoneType, int)
  def itemActivated(self, item: Optional[QAction], column: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::itemActivated(QAction
    *item, int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#itemActivated

    Parameters
    ----------

    item : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is.
    """
    #  void qdesigner_internal::ActionEditor::itemActivated(QAction *item,
    #      int column)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor13itemActivatedEP7QActi'
        'oni',
        self._addressOf(item), column,
    )

  @overload(QMenu, QAction)
  @overload(QMenu, NoneType)
  @overload(NoneType, QAction)
  @overload(NoneType, NoneType)
  def contextMenuRequested(
      self,
      menu: Optional[QMenu],
      item: Optional[QAction],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionEditor::contextMenuRequested(QMenu *menu,
    QAction *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html

    Parameters
    ----------

    menu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionEditor::contextMenuRequested(QMenu
    #      *menu, QAction *item)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor20contextMenuRequestedE'
        'P5QMenuP7QAction',
        self._addressOf(menu), self._addressOf(item),
    )

  @overload(QDesignerFormWindowInterface, QList[QAction])
  @overload(NoneType, QList[QAction])
  def deleteActions(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
      a1: QList[QAction],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::deleteActions(
    QDesignerFormWindowInterface *formWindow, const ActionList &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#deleteActions

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QList[QAction]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::ActionEditor::deleteActions(
    #      QDesignerFormWindowInterface *formWindow, const ActionList &a1)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor13deleteActionsEP28QDes'
        'ignerFormWindowInterfaceRK5QListIP7QActionE',
        self._addressOf(formWindow), self._valueOf(a1),
    )

  @overload(QDesignerFormWindowInterface, QList[QAction])
  @overload(NoneType, QList[QAction])
  def copyActions(
      self,
      formWindow: Optional[QDesignerFormWindowInterface],
      a1: QList[QAction],
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::copyActions(
    QDesignerFormWindowInterface *formWindow, const ActionList &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#copyActions

    Parameters
    ----------

    formWindow : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QList[QAction]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::ActionEditor::copyActions(
    #      QDesignerFormWindowInterface *formWindow, const ActionList &a1)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor11copyActionsEP28QDesig'
        'nerFormWindowInterfaceRK5QListIP7QActionE',
        self._addressOf(formWindow), self._valueOf(a1),
    )

  def restoreSettings(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::restoreSettings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html
    """
    #  void qdesigner_internal::ActionEditor::restoreSettings()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor15restoreSettingsEv',
    )

  def saveSettings(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionEditor::saveSettings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html#saveSettings
    """
    #  void qdesigner_internal::ActionEditor::saveSettings()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor12saveSettingsEv',
    )

  def updateViewModeActions(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionEditor::updateViewModeActions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actioneditor.html
    """
    #  void qdesigner_internal::ActionEditor::updateViewModeActions()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal12ActionEditor21updateViewModeActions'
        'Ev',
    )

  @staticmethod
  def createConfigureMenuButton(*__, **_) -> Never:
    """
    Qt's 'QToolButton
    *qdesigner_internal::ActionEditor::createConfigureMenuButton(const
    QString &t, QMenu **ptrToMenu)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ActionEditor.createConfigureMenuButton' has no "
        "cute function yet. Qt's 'QToolButton "
        "*qdesigner_internal::ActionEditor::createConfigureMenuButton(const "
        "QString &t, QMenu **ptrToMenu)': takes a type Python has no way to "
        "hand over yet.")

"""
qdesigner_internal::NewActionDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/newactiondialog_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::NewActionDialog to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtWidgets import QDialog

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class NewActionDialog(QDialog):
  """
  The cute side of Qt's qdesigner_internal::NewActionDialog: a plain Python
  object standing in front of one C++ qdesigner_internal::NewActionDialog.

  It is built on the cute 'QDialog', as Qt's
  qdesigner_internal::NewActionDialog is built on Qt's QDialog, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::NewActionDialog that has a
  ritual and that Python can call so far, 11 names in all: 'metaObject',
  'focusName', 'focusText', 'focusTooltip', 'focusShortcut',
  'focusCheckable', 'focusMenuRole', 'onEditActionTextTextEdited',
  'onEditObjectNameTextEdited', 'slotEditToolTip', 'slotResetKeySequence'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::NewActionDialog::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::NewActionDialog::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::NewActionDialog::~NewActionDialog()': the
    destructor: Python never removes a C++
    qdesigner_internal::NewActionDialog.

  What has no ritual
  ------------------

  9 of the 23 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  1 leans on 'qdesigner_internal.

  What to expect
  --------------

  - The C++ qdesigner_internal::NewActionDialog is created at the first use,
    not by 'qdesigner_internal::NewActionDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::NewActionDialog.
  - Qt tells when it has removed the C++ qdesigner_internal::NewActionDialog.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::NewActionDialog that has no cute
    function yet, '__init__', 'actionData', 'actionName', 'actionText',
    'setActionData', 'updateButtons', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::NewActionDialog'

  #  A C++ qdesigner_internal::NewActionDialog Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_NewActionDialog'

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
    *qdesigner_internal::NewActionDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newactiondialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::NewActionDialog::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal15NewActionDialog10metaObjectEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'qdesigner_internal::NewActionDialog::NewActionDialog(ActionEditor
    *parent)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: allocation of incomplete type
    '::qdesigner_internal::Ui::NewActionDialog'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.NewActionDialog.__init__' has no cute function "
        "yet. Qt's "
        "'qdesigner_internal::NewActionDialog::NewActionDialog(ActionEditor "
        "*parent)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: allocation of "
        "incomplete type '::qdesigner_internal::Ui::NewActionDialog'.")

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

  def focusName(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::NewActionDialog::focusName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newactiondialog.html#focusName
    """
    #  void qdesigner_internal::NewActionDialog::focusName()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal15NewActionDialog9focusNameEv',
    )

  def focusText(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::NewActionDialog::focusText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newactiondialog.html#focusText
    """
    #  void qdesigner_internal::NewActionDialog::focusText()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal15NewActionDialog9focusTextEv',
    )

  def focusTooltip(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::NewActionDialog::focusTooltip()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newactiondialog.html
    """
    #  void qdesigner_internal::NewActionDialog::focusTooltip()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal15NewActionDialog12focusTooltipEv',
    )

  def focusShortcut(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::NewActionDialog::focusShortcut()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newactiondialog.html
    """
    #  void qdesigner_internal::NewActionDialog::focusShortcut()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal15NewActionDialog13focusShortcutEv',
    )

  def focusCheckable(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::NewActionDialog::focusCheckable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newactiondialog.html
    """
    #  void qdesigner_internal::NewActionDialog::focusCheckable()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal15NewActionDialog14focusCheckableEv',
    )

  def focusMenuRole(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::NewActionDialog::focusMenuRole()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newactiondialog.html
    """
    #  void qdesigner_internal::NewActionDialog::focusMenuRole()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal15NewActionDialog13focusMenuRoleEv',
    )

  @overload(str)
  def onEditActionTextTextEdited(self, text: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewActionDialog::onEditActionTextTextEdited(const
    QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newactiondialog.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::NewActionDialog::onEditActionTextTextEdited(
    #      const QString &text)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal15NewActionDialog26onEditActionTextTe'
        'xtEditedERK7QString',
        text,
    )

  @overload(str)
  def onEditObjectNameTextEdited(self, text: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewActionDialog::onEditObjectNameTextEdited(const
    QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newactiondialog.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::NewActionDialog::onEditObjectNameTextEdited(
    #      const QString &text)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal15NewActionDialog26onEditObjectNameTe'
        'xtEditedERK7QString',
        text,
    )

  def slotEditToolTip(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::NewActionDialog::slotEditToolTip()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newactiondialog.html
    """
    #  void qdesigner_internal::NewActionDialog::slotEditToolTip()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal15NewActionDialog15slotEditToolTipEv',
    )

  def slotResetKeySequence(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::NewActionDialog::slotResetKeySequence()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-newactiondialog.html
    """
    #  void qdesigner_internal::NewActionDialog::slotResetKeySequence()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal15NewActionDialog20slotResetKeySequen'
        'ceEv',
    )

  @staticmethod
  def actionData(*__, **_) -> Never:
    """
    Qt's 'ActionData qdesigner_internal::NewActionDialog::actionData()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'Ui::NewActionDialog'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.NewActionDialog.actionData' has no cute "
        "function yet. Qt's 'ActionData "
        "qdesigner_internal::NewActionDialog::actionData() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'Ui::NewActionDialog'.")

  @staticmethod
  def actionName(*__, **_) -> Never:
    """
    Qt's 'QString qdesigner_internal::NewActionDialog::actionName() const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'Ui::NewActionDialog'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.NewActionDialog.actionName' has no cute "
        "function yet. Qt's 'QString "
        "qdesigner_internal::NewActionDialog::actionName() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'Ui::NewActionDialog'.")

  @staticmethod
  def actionText(*__, **_) -> Never:
    """
    Qt's 'QString qdesigner_internal::NewActionDialog::actionText() const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'Ui::NewActionDialog'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.NewActionDialog.actionText' has no cute "
        "function yet. Qt's 'QString "
        "qdesigner_internal::NewActionDialog::actionText() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'Ui::NewActionDialog'.")

  @staticmethod
  def setActionData(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::NewActionDialog::setActionData(const
    ActionData &d)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type 'Ui::NewActionDialog'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.NewActionDialog.setActionData' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::NewActionDialog::setActionData(const "
        "ActionData &d)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: member access "
        "into incomplete type 'Ui::NewActionDialog'.")

  @staticmethod
  def updateButtons(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::NewActionDialog::updateButtons()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'Ui::NewActionDialog'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.NewActionDialog.updateButtons' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::NewActionDialog::updateButtons()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'Ui::NewActionDialog'.")

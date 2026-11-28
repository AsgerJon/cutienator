"""
qdesigner_internal::QDesignerPromotionDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_promotiondialog_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerPromotionDialog to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..QtWidgets import QDialog

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QItemSelection, QMetaObject, QPoint
  from . import QDesignerPromotionInterface
  from . import QDesignerWidgetDataBaseItemInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerPromotionInterface = WAIT['QDesignerPromotionInterface']
  QDesignerWidgetDataBaseItemInterface = WAIT['QDesignerWidgetDataBaseItemInterface']
  QItemSelection = WAIT['QItemSelection']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerPromotionDialog(QDialog):
  """
  The cute side of Qt's qdesigner_internal::QDesignerPromotionDialog: a plain
  Python object standing in front of one C++
  qdesigner_internal::QDesignerPromotionDialog.

  It is built on the cute 'QDialog', as Qt's
  qdesigner_internal::QDesignerPromotionDialog is built on Qt's QDialog, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerPromotionDialog that
  has a ritual and that Python can call so far, 11 names in all:
  'metaObject', 'baseClassNames', 'selectedBaseClassChanged', 'slotRemove',
  'slotAcceptPromoteTo', 'slotSelectionChanged', 'slotIncludeFileChanged',
  'slotClassNameChanged', 'slotUpdateFromWidgetDatabase',
  'slotTreeViewContextMenu', 'slotEditSignalsSlots'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *qdesigner_internal::QDesignerPromotionDialog::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::QDesignerPromotionDialog::qt_metacall(QMetaObject::
    Call a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  9 of the 22 functions Qt declares: 6 leans on 'qdesigner_internal; 2 not a
  gap; 1 the compiler refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerPromotionDialog is created at the
    first use, not by 'qdesigner_internal::QDesignerPromotionDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::QDesignerPromotionDialog.
  - Qt tells when it has removed the C++
    qdesigner_internal::QDesignerPromotionDialog. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::QDesignerPromotionDialog that has
    no cute function yet, '__init__', 'createButtonBox', 'databaseItemAt',
    'delayedUpdateFromWidgetDatabase', 'displayError',
    'slotNewPromotedClass', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside qdesigner_internal::QDesignerPromotionDialog,
  #  each a class in here as in C++, and the names Qt has for the
  #  combinations of its flags enums.

  class Mode(CuteNum):
    """
    The enum 'qdesigner_internal::QDesignerPromotionDialog::Mode' of Qt, with
    the 2 names Qt gives in it.
    """

    ModeEdit = Kee[int](0)
    ModeEditChooseClass = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDesignerPromotionInterface)
  @overload(NoneType)
  def baseClassNames(
      promotion: Optional[QDesignerPromotionInterface],
  ) -> QStringList:
    """
    Calls Qt's 'const QStringList
    &qdesigner_internal::QDesignerPromotionDialog::baseClassNames(const
    QDesignerPromotionInterface *promotion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotiondialog.html

    Parameters
    ----------

    promotion : Optional[QDesignerPromotionInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const QStringList
    #      &qdesigner_internal::QDesignerPromotionDialog::baseClassNames(
    #      const QDesignerPromotionInterface *promotion)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal24QDesignerPromotionDialog14baseClass'
        'NamesEPK27QDesignerPromotionInterface',
        CuteMixin._addressOf(promotion),
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerPromotionDialog'

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
    *qdesigner_internal::QDesignerPromotionDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotiondialog.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::QDesignerPromotionDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal24QDesignerPromotionDialog10metaObje'
        'ctEv',
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
    Qt's
    'qdesigner_internal::QDesignerPromotionDialog::QDesignerPromotionDialog(
    QDesignerFormEditorInterface *core, QWidget *parent, const QString
    &promotableWidgetClassName, QString *promoteTo)': leans on
    'qdesigner_internal::PromotionModel::classNameChanged(
    QDesignerWidgetDataBaseItemInterface*, QString const&)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerPromotionDialog.__init__' has no cute "
        "function yet. Qt's "
        "'qdesigner_internal::QDesignerPromotionDialog::QDesignerPromotionDi"
        "alog(QDesignerFormEditorInterface *core, QWidget *parent, const "
        "QString &promotableWidgetClassName, QString *promoteTo)': leans on "
        "'qdesigner_internal::PromotionModel::classNameChanged(QDesignerWidg"
        "etDataBaseItemInterface*, QString const&)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

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
  def selectedBaseClassChanged(self, a0: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPromotionDialog::selectedBaseClassChanged(
    const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotiondialog.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::QDesignerPromotionDialog::
    #      selectedBaseClassChanged(const QString &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24QDesignerPromotionDialog24selectedB'
        'aseClassChangedERK7QString',
        a0,
    )

  def slotRemove(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPromotionDialog::slotRemove()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotiondialog.html
    """
    #  void qdesigner_internal::QDesignerPromotionDialog::slotRemove()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24QDesignerPromotionDialog10slotRemov'
        'eEv',
    )

  def slotAcceptPromoteTo(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPromotionDialog::slotAcceptPromoteTo()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotiondialog.html
    """
    #  void
    #      qdesigner_internal::QDesignerPromotionDialog::slotAcceptPromoteTo(
    #      )
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24QDesignerPromotionDialog19slotAccep'
        'tPromoteToEv',
    )

  @overload(QItemSelection, QItemSelection)
  def slotSelectionChanged(
      self,
      a0: QItemSelection,
      a1: QItemSelection,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPromotionDialog::slotSelectionChanged(const
    QItemSelection &a0, const QItemSelection &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotiondialog.html

    Parameters
    ----------

    a0 : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    a1 : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.
    """
    #  void qdesigner_internal::QDesignerPromotionDialog::
    #      slotSelectionChanged(const QItemSelection &a0, const
    #      QItemSelection &a1)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24QDesignerPromotionDialog20slotSelec'
        'tionChangedERK14QItemSelectionS3_',
        self._valueOf(a0), self._valueOf(a1),
    )

  @overload(QDesignerWidgetDataBaseItemInterface, str)
  @overload(NoneType, str)
  def slotIncludeFileChanged(
      self,
      a0: Optional[QDesignerWidgetDataBaseItemInterface],
      includeFile: str,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPromotionDialog::slotIncludeFileChanged(
    QDesignerWidgetDataBaseItemInterface *a0, const QString &includeFile)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotiondialog.html

    Parameters
    ----------

    a0 : Optional[QDesignerWidgetDataBaseItemInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    includeFile : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::QDesignerPromotionDialog::
    #      slotIncludeFileChanged(QDesignerWidgetDataBaseItemInterface *a0,
    #      const QString &includeFile)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24QDesignerPromotionDialog22slotInclu'
        'deFileChangedEP36QDesignerWidgetDataBaseItemInterfaceRK7QString',
        self._addressOf(a0), includeFile,
    )

  @overload(QDesignerWidgetDataBaseItemInterface, str)
  @overload(NoneType, str)
  def slotClassNameChanged(
      self,
      a0: Optional[QDesignerWidgetDataBaseItemInterface],
      newName: str,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPromotionDialog::slotClassNameChanged(
    QDesignerWidgetDataBaseItemInterface *a0, const QString &newName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotiondialog.html

    Parameters
    ----------

    a0 : Optional[QDesignerWidgetDataBaseItemInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::QDesignerPromotionDialog::
    #      slotClassNameChanged(QDesignerWidgetDataBaseItemInterface *a0,
    #      const QString &newName)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24QDesignerPromotionDialog20slotClass'
        'NameChangedEP36QDesignerWidgetDataBaseItemInterfaceRK7QString',
        self._addressOf(a0), newName,
    )

  def slotUpdateFromWidgetDatabase(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::QDesignerPromotionDialog::
    slotUpdateFromWidgetDatabase()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotiondialog.html
    """
    #  void qdesigner_internal::QDesignerPromotionDialog::
    #      slotUpdateFromWidgetDatabase()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24QDesignerPromotionDialog28slotUpdat'
        'eFromWidgetDatabaseEv',
    )

  @overload(QPoint)
  def slotTreeViewContextMenu(self, a0: QPoint) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPromotionDialog::slotTreeViewContextMenu(
    const QPoint &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotiondialog.html

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::QDesignerPromotionDialog::
    #      slotTreeViewContextMenu(const QPoint &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24QDesignerPromotionDialog23slotTreeV'
        'iewContextMenuERK6QPoint',
        self._valueOf(a0),
    )

  def slotEditSignalsSlots(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerPromotionDialog::slotEditSignalsSlots()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerpromotiondialog.html
    """
    #  void qdesigner_internal::QDesignerPromotionDialog::
    #      slotEditSignalsSlots()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24QDesignerPromotionDialog20slotEditS'
        'ignalsSlotsEv',
    )

  @staticmethod
  def createButtonBox(*__, **_) -> Never:
    """
    Qt's 'QDialogButtonBox
    *qdesigner_internal::QDesignerPromotionDialog::createButtonBox()': leans
    on 'qdesigner_internal::QDesignerPromotionDialog::staticMetaObject',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerPromotionDialog.createButtonBox' has "
        "no cute function yet. Qt's 'QDialogButtonBox "
        "*qdesigner_internal::QDesignerPromotionDialog::createButtonBox()': "
        "leans on "
        "'qdesigner_internal::QDesignerPromotionDialog::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def databaseItemAt(*__, **_) -> Never:
    """
    Qt's 'QDesignerWidgetDataBaseItemInterface
    *qdesigner_internal::QDesignerPromotionDialog::databaseItemAt(const
    QItemSelection &a0, unsigned int &flags) const': leans on
    'qdesigner_internal::PromotionModel::modelData(QModelIndex const&)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerPromotionDialog.databaseItemAt' has "
        "no cute function yet. Qt's 'QDesignerWidgetDataBaseItemInterface "
        "*qdesigner_internal::QDesignerPromotionDialog::databaseItemAt(const"
        " QItemSelection &a0, unsigned int &flags) const': leans on "
        "'qdesigner_internal::PromotionModel::modelData(QModelIndex const&) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def delayedUpdateFromWidgetDatabase(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::QDesignerPromotionDialog::
    delayedUpdateFromWidgetDatabase()': leans on
    'qdesigner_internal::QDesignerPromotionDialog::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerPromotionDialog.delayedUpdateFromWidge"
        "tDatabase' has no cute function yet. Qt's 'void "
        "qdesigner_internal::QDesignerPromotionDialog::delayedUpdateFromWidg"
        "etDatabase()': leans on "
        "'qdesigner_internal::QDesignerPromotionDialog::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def displayError(*__, **_) -> Never:
    """
    Qt's 'void
    qdesigner_internal::QDesignerPromotionDialog::displayError(const QString
    &message)': leans on
    'qdesigner_internal::QDesignerPromotionDialog::staticMetaObject', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerPromotionDialog.displayError' has no "
        "cute function yet. Qt's 'void "
        "qdesigner_internal::QDesignerPromotionDialog::displayError(const "
        "QString &message)': leans on "
        "'qdesigner_internal::QDesignerPromotionDialog::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def slotNewPromotedClass(*__, **_) -> Never:
    """
    Qt's 'void
    qdesigner_internal::QDesignerPromotionDialog::slotNewPromotedClass(const
    PromotionParameters &a0, bool *ok)': the compiler refuses its ritual as
    it would be written here: unknown type name 'PromotionParameters'; did
    you mean 'qdesigner_internal::PromotionParameters'?.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerPromotionDialog.slotNewPromotedClass' "
        "has no cute function yet. Qt's 'void "
        "qdesigner_internal::QDesignerPromotionDialog::slotNewPromotedClass("
        "const PromotionParameters &a0, bool *ok)': the compiler refuses "
        "its ritual as it would be written here: unknown type name "
        "'PromotionParameters'; did you mean "
        "'qdesigner_internal::PromotionParameters'?.")

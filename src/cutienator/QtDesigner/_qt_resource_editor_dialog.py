"""
QtResourceEditorDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qtresourceeditordialog_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QtResourceEditorDialog to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtWidgets import QDialog

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QtResourceEditorDialog(QDialog):
  """
  The cute side of Qt's QtResourceEditorDialog: a plain Python object
  standing in front of one C++ QtResourceEditorDialog.

  It is built on the cute 'QDialog', as Qt's QtResourceEditorDialog is built
  on Qt's QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtResourceEditorDialog that has a ritual and that
  Python can call so far, 2 names in all: 'metaObject', 'accept'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtResourceEditorDialog::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QtResourceEditorDialog::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QtResourceEditorDialog::~QtResourceEditorDialog()': the destructor:
    Python never removes a C++ QtResourceEditorDialog.
  - Qt's 'QtResourceEditorDialogPrivate *QtResourceEditorDialog::d_func()':
    gives 'QtResourceEditorDialogPrivate', which has no cute class yet.
  - Qt's 'const QtResourceEditorDialogPrivate
    *QtResourceEditorDialog::d_func() const': gives
    'QtResourceEditorDialogPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  13 of the 20 functions Qt declares: 4 forbidden; 4 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 3
  leans on 'QtResourceEditorDialog; 2 not a gap.

  What to expect
  --------------

  - The C++ QtResourceEditorDialog is created at the first use, not by
    'QtResourceEditorDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtResourceEditorDialog.
  - Qt tells when it has removed the C++ QtResourceEditorDialog. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QtResourceEditorDialog that has no cute function yet,
    '__init__', 'displayResourceFailures', 'editResources', 'model',
    'selectedResource', 'setResourceModel', holds a function that raises
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
  __qt_class__ = 'QtResourceEditorDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtResourceEditorDialog::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceeditordialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtResourceEditorDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QtResourceEditorDialog10metaObjectEv',
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
    Qt's 'QtResourceEditorDialog::QtResourceEditorDialog(
    QDesignerFormEditorInterface *core, QDesignerDialogGuiInterface *dlgGui,
    QWidget *parent)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: allocation of incomplete
    type 'QtResourceEditorDialogPrivate'.
    """
    raise NotImplementedError(
        "'QtResourceEditorDialog.__init__' has no cute function yet. Qt's "
        "'QtResourceEditorDialog::QtResourceEditorDialog(QDesignerFormEditor"
        "Interface *core, QDesignerDialogGuiInterface *dlgGui, QWidget "
        "*parent)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: allocation of "
        "incomplete type 'QtResourceEditorDialogPrivate'.")

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

  def accept(self) -> None:
    """
    Calls Qt's 'void QtResourceEditorDialog::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceeditordialog.html#accept
    """
    #  void QtResourceEditorDialog::accept()
    self.uglySide.call('ritual_ZN22QtResourceEditorDialog6acceptEv')

  @staticmethod
  def displayResourceFailures(*__, **_) -> Never:
    """
    Qt's 'void QtResourceEditorDialog::displayResourceFailures(const QString
    &logOutput, QDesignerDialogGuiInterface *dlgGui, QWidget *parent)': leans
    on 'QtResourceEditorDialog::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtResourceEditorDialog.displayResourceFailures' has no cute "
        "function yet. Qt's 'void "
        "QtResourceEditorDialog::displayResourceFailures(const QString "
        "&logOutput, QDesignerDialogGuiInterface *dlgGui, QWidget "
        "*parent)': leans on 'QtResourceEditorDialog::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def editResources(*__, **_) -> Never:
    """
    Qt's 'QString
    QtResourceEditorDialog::editResources(QDesignerFormEditorInterface *core,
    QtResourceModel *model, QDesignerDialogGuiInterface *dlgGui, QWidget
    *parent)': leans on
    'QtResourceEditorDialog::setResourceModel(QtResourceModel*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QtResourceEditorDialog.editResources' has no cute function yet. "
        "Qt's 'QString "
        "QtResourceEditorDialog::editResources(QDesignerFormEditorInterface "
        "*core, QtResourceModel *model, QDesignerDialogGuiInterface "
        "*dlgGui, QWidget *parent)': leans on "
        "'QtResourceEditorDialog::setResourceModel(QtResourceModel*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def model(*__, **_) -> Never:
    """
    Qt's 'QtResourceModel *QtResourceEditorDialog::model() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QtResourceEditorDialogPrivate'.
    """
    raise NotImplementedError(
        "'QtResourceEditorDialog.model' has no cute function yet. Qt's "
        "'QtResourceModel *QtResourceEditorDialog::model() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QtResourceEditorDialogPrivate'.")

  @staticmethod
  def selectedResource(*__, **_) -> Never:
    """
    Qt's 'QString QtResourceEditorDialog::selectedResource() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: no member named 'prefix' in 'QtResourceSet'.
    """
    raise NotImplementedError(
        "'QtResourceEditorDialog.selectedResource' has no cute function "
        "yet. Qt's 'QString QtResourceEditorDialog::selectedResource() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: no member named "
        "'prefix' in 'QtResourceSet'.")

  @staticmethod
  def setResourceModel(*__, **_) -> Never:
    """
    Qt's 'void QtResourceEditorDialog::setResourceModel(QtResourceModel
    *model)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'QtResourceEditorDialogPrivate'.
    """
    raise NotImplementedError(
        "'QtResourceEditorDialog.setResourceModel' has no cute function "
        "yet. Qt's 'void "
        "QtResourceEditorDialog::setResourceModel(QtResourceModel *model)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QtResourceEditorDialogPrivate'.")

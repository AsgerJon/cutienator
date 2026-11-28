"""
qdesigner_internal::SignaturePanel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/signalslotdialog_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::SignaturePanel to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject, QStringList
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QItemSelection, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QItemSelection = WAIT['QItemSelection']


class SignaturePanel(QObject):
  """
  The cute side of Qt's qdesigner_internal::SignaturePanel: a plain Python
  object standing in front of one C++ qdesigner_internal::SignaturePanel.

  It is built on the cute 'QObject', as Qt's
  qdesigner_internal::SignaturePanel is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::SignaturePanel that has a ritual
  and that Python can call so far, 8 names in all: 'metaObject',
  'fakeMethods', 'setData', 'count', 'slotAdd', 'slotRemove',
  'slotSelectionChanged', 'closeEditor'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::SignaturePanel::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::SignaturePanel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void qdesigner_internal::SignaturePanel::checkSignature(const
    QString &signature, bool *ok)': takes a number to change where it is.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 2 not a gap; 2 leans on
  'qdesigner_internal.

  What to expect
  --------------

  - The C++ qdesigner_internal::SignaturePanel is created at the first use,
    not by 'qdesigner_internal::SignaturePanel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::SignaturePanel.
  - Qt tells when it has removed the C++ qdesigner_internal::SignaturePanel.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::SignaturePanel that has no cute
    function yet, '__init__', 'checkSignature', holds a function that raises
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
  __qt_class__ = 'qdesigner_internal::SignaturePanel'

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
    *qdesigner_internal::SignaturePanel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signaturepanel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::SignaturePanel::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14SignaturePanel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fakeMethods(self) -> QStringList:
    """
    Calls Qt's 'QStringList qdesigner_internal::SignaturePanel::fakeMethods()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signaturepanel.html#fakeMethods

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList qdesigner_internal::SignaturePanel::fakeMethods() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14SignaturePanel11fakeMethodsEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def count(self, signature: str) -> int:
    """
    Calls Qt's 'int qdesigner_internal::SignaturePanel::count(const QString
    &signature) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signaturepanel.html#count

    Parameters
    ----------

    signature : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  int qdesigner_internal::SignaturePanel::count(const QString
    #      &signature) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14SignaturePanel5countERK7QString',
        signature,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['qdesigner_internal.SignalSlotDialogData'])
  def setData(self, d: qdesigner_internal.SignalSlotDialogData) -> None:
    """
    Calls Qt's 'void qdesigner_internal::SignaturePanel::setData(const
    SignalSlotDialogData &d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signaturepanel.html#setData

    Parameters
    ----------

    d : qdesigner_internal.SignalSlotDialogData
      Passed on as a value: Qt reads the C++
      qdesigner_internal::SignalSlotDialogData, which stays Python's own.
    """
    #  void qdesigner_internal::SignaturePanel::setData(const
    #      SignalSlotDialogData &d)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14SignaturePanel7setDataERKNS_20Signa'
        'lSlotDialogDataE',
        self._valueOf(d),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'qdesigner_internal::SignaturePanel::SignaturePanel(QObject *parent,
    QListView *listView, QToolButton *addButton, QToolButton *removeButton,
    const QString &newPrefix)': leans on
    'qdesigner_internal::SignatureModel::checkSignature(QString const&,
    bool*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.SignaturePanel.__init__' has no cute function "
        "yet. Qt's "
        "'qdesigner_internal::SignaturePanel::SignaturePanel(QObject "
        "*parent, QListView *listView, QToolButton *addButton, QToolButton "
        "*removeButton, const QString &newPrefix)': leans on "
        "'qdesigner_internal::SignatureModel::checkSignature(QString "
        "const&, bool*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def slotAdd(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::SignaturePanel::slotAdd()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signaturepanel.html#slotAdd
    """
    #  void qdesigner_internal::SignaturePanel::slotAdd()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14SignaturePanel7slotAddEv',
    )

  def slotRemove(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::SignaturePanel::slotRemove()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signaturepanel.html#slotRemove
    """
    #  void qdesigner_internal::SignaturePanel::slotRemove()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14SignaturePanel10slotRemoveEv',
    )

  @overload(QItemSelection, QItemSelection)
  def slotSelectionChanged(
      self,
      a0: QItemSelection,
      a1: QItemSelection,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::SignaturePanel::slotSelectionChanged(const
    QItemSelection &a0, const QItemSelection &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signaturepanel.html

    Parameters
    ----------

    a0 : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    a1 : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.
    """
    #  void qdesigner_internal::SignaturePanel::slotSelectionChanged(const
    #      QItemSelection &a0, const QItemSelection &a1)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14SignaturePanel20slotSelectionChange'
        'dERK14QItemSelectionS3_',
        self._valueOf(a0), self._valueOf(a1),
    )

  def closeEditor(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::SignaturePanel::closeEditor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-signaturepanel.html#closeEditor
    """
    #  void qdesigner_internal::SignaturePanel::closeEditor()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14SignaturePanel11closeEditorEv',
    )

  @staticmethod
  def checkSignature(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::SignaturePanel::checkSignature(const
    QString &signature, bool *ok)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'qdesigner_internal.SignaturePanel.checkSignature' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::SignaturePanel::checkSignature(const QString "
        "&signature, bool *ok)': takes a number to change where it is.")

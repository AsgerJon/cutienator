"""
qdesigner_internal::SelectSignalDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/selectsignaldialog_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::SelectSignalDialog to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..QtWidgets import QDialog

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QModelIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']


class SelectSignalDialog(QDialog):
  """
  The cute side of Qt's qdesigner_internal::SelectSignalDialog: a plain
  Python object standing in front of one C++
  qdesigner_internal::SelectSignalDialog.

  It is built on the cute 'QDialog', as Qt's
  qdesigner_internal::SelectSignalDialog is built on Qt's QDialog, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::SelectSignalDialog that has a
  ritual and that Python can call so far, 4 names in all: 'metaObject',
  'currentChanged', 'activated', 'methodFromIndex'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::SelectSignalDialog::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::SelectSignalDialog::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::SelectSignalDialog::~SelectSignalDialog()': the
    destructor: Python never removes a C++
    qdesigner_internal::SelectSignalDialog.

  What has no ritual
  ------------------

  7 of the 14 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  1 leans on 'qdesigner_internal.

  What to expect
  --------------

  - The C++ qdesigner_internal::SelectSignalDialog is created at the first
    use, not by 'qdesigner_internal::SelectSignalDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::SelectSignalDialog.
  - Qt tells when it has removed the C++
    qdesigner_internal::SelectSignalDialog. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's qdesigner_internal::SelectSignalDialog that has no cute
    function yet, '__init__', 'populate', 'populateModel', 'selectedMethod',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The classes Qt writes inside qdesigner_internal::SelectSignalDialog,
  #  each a class in here as in C++.

  class Method(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's qdesigner_internal::SelectSignalDialog::Method: a
    plain Python object standing in front of one C++
    qdesigner_internal::SelectSignalDialog::Method.

    C++ hands a qdesigner_internal::SelectSignalDialog::Method around as a
    copy, so every C++ qdesigner_internal::SelectSignalDialog::Method behind
    a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's qdesigner_internal::SelectSignalDialog::Method
    that has a ritual and that Python can call so far, 1 name in all:
    'isValid'. It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'qdesigner_internal::SelectSignalDialog::Method::~Method()': the
      destructor: Python removes its C++
      qdesigner_internal::SelectSignalDialog::Method by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ qdesigner_internal::SelectSignalDialog::Method is created at
      the first use, not by
      'qdesigner_internal::SelectSignalDialog::Method(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a qdesigner_internal::SelectSignalDialog::Method back
      gives a copy the ritual made for Python, in a new cute
      qdesigner_internal::SelectSignalDialog::Method.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'qdesigner_internal::SelectSignalDialog::Method'

    #  Qt's '~qdesigner_internal::SelectSignalDialog::Method()'. Naming it
    #  makes this a value class: Python owns every C++
    #  qdesigner_internal::SelectSignalDialog::Method behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN18qdesigner_internal18SelectSignalDialog6MethodD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool
      qdesigner_internal::SelectSignalDialog::Method::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-selectsignaldialog-method.html
      """
      #  bool qdesigner_internal::SelectSignalDialog::Method::isValid() const
      return self.uglySide.call(
          'ritual_ZNK18qdesigner_internal18SelectSignalDialog6Method7isVali'
          'dEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'qdesigner_internal::SelectSignalDialog::Method::Method()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-selectsignaldialog-method.html
      """
      #  qdesigner_internal::SelectSignalDialog::Method::Method()
      self._noteCreation(SelectSignalDialog.Method, lambda: Rituals.call(
          'ritual_ZN18qdesigner_internal18SelectSignalDialog6MethodC1Ev',
      ))

    @overload(str, str, QStringList)
    def __init__(self, c: str, s: str, p: QStringList) -> None:
      """
      Notes what was given, for Qt's
      'qdesigner_internal::SelectSignalDialog::Method::Method(const QString
      &c, const QString &s, const QStringList &p)', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdesigner_internal-selectsignaldialog-method.html

      Parameters
      ----------

      c : str
        Passed on as it is: a QString is made of it for the call.

      s : str
        Passed on as it is: a QString is made of it for the call.

      p : QStringList
        Passed on as a list of Qt: Qt reads the C++ list, which stays
        Python's own. A list or tuple of Python is made into one first, and
        refused when an element does not fit.
      """
      #  qdesigner_internal::SelectSignalDialog::Method::Method(const QString
      #      &c, const QString &s, const QStringList &p)
      self._noteCreation(SelectSignalDialog.Method, lambda: Rituals.call(
          'ritual_ZN18qdesigner_internal18SelectSignalDialog6MethodC1ERK7QS'
          'tringS4_RK5QListIS2_E',
          c, s, self._valueOf(p),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::SelectSignalDialog'

  #  A C++ qdesigner_internal::SelectSignalDialog Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_SelectSignalDialog'

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
    *qdesigner_internal::SelectSignalDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-selectsignaldialog.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::SelectSignalDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18SelectSignalDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex)
  def methodFromIndex(self, a0: QModelIndex) -> Method:
    """
    Calls Qt's 'Method
    qdesigner_internal::SelectSignalDialog::methodFromIndex(const QModelIndex
    &a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-selectsignaldialog.html

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Method
      A new cute qdesigner_internal::SelectSignalDialog::Method around the
      copy Qt gave back. Python owns it.
    """
    #  Method qdesigner_internal::SelectSignalDialog::methodFromIndex(const
    #      QModelIndex &a0) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18SelectSignalDialog15methodFromInde'
        'xERK11QModelIndex',
        self._valueOf(a0),
    )
    return qdesigner_internal.SelectSignalDialog.Method._cuteOwning(address)

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
    Qt's 'qdesigner_internal::SelectSignalDialog::SelectSignalDialog(QWidget
    *parent)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: allocation of incomplete type
    '::Ui::SelectSignalDialog'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.SelectSignalDialog.__init__' has no cute "
        "function yet. Qt's "
        "'qdesigner_internal::SelectSignalDialog::SelectSignalDialog(QWidget"
        " *parent)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: allocation of "
        "incomplete type '::Ui::SelectSignalDialog'.")

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

  @overload(QModelIndex, QModelIndex)
  def currentChanged(self, a0: QModelIndex, a1: QModelIndex) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::SelectSignalDialog::currentChanged(const QModelIndex
    &a0, const QModelIndex &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-selectsignaldialog.html

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void qdesigner_internal::SelectSignalDialog::currentChanged(const
    #      QModelIndex &a0, const QModelIndex &a1)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18SelectSignalDialog14currentChangedE'
        'RK11QModelIndexS3_',
        self._valueOf(a0), self._valueOf(a1),
    )

  @overload(QModelIndex)
  def activated(self, a0: QModelIndex) -> None:
    """
    Calls Qt's 'void qdesigner_internal::SelectSignalDialog::activated(const
    QModelIndex &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-selectsignaldialog.html

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void qdesigner_internal::SelectSignalDialog::activated(const
    #      QModelIndex &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18SelectSignalDialog9activatedERK11QM'
        'odelIndex',
        self._valueOf(a0),
    )

  @staticmethod
  def populate(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::SelectSignalDialog::populate(
    QDesignerFormEditorInterface *core, QObject *object, const QString
    &defaultSignal)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: member access into
    incomplete type '::Ui::SelectSignalDialog'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.SelectSignalDialog.populate' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::SelectSignalDialog::populate(QDesignerFormEdito"
        "rInterface *core, QObject *object, const QString &defaultSignal)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type '::Ui::SelectSignalDialog'.")

  @staticmethod
  def populateModel(*__, **_) -> Never:
    """
    Qt's 'void qdesigner_internal::SelectSignalDialog::populateModel(
    QDesignerFormEditorInterface *core, QObject *object)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: no member named 'append' in
    'qdesigner_internal::SelectSignalDialog::Method'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.SelectSignalDialog.populateModel' has no cute "
        "function yet. Qt's 'void "
        "qdesigner_internal::SelectSignalDialog::populateModel(QDesignerForm"
        "EditorInterface *core, QObject *object)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: no member named 'append' in "
        "'qdesigner_internal::SelectSignalDialog::Method'.")

  @staticmethod
  def selectedMethod(*__, **_) -> Never:
    """
    Qt's 'Method qdesigner_internal::SelectSignalDialog::selectedMethod()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    '::Ui::SelectSignalDialog'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.SelectSignalDialog.selectedMethod' has no cute "
        "function yet. Qt's 'Method "
        "qdesigner_internal::SelectSignalDialog::selectedMethod() const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type '::Ui::SelectSignalDialog'.")

"""
QPrintDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/qprintdialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtWidgets import QWidget
from . import QAbstractPrintDialog

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QPrinter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPrinter = WAIT['QPrinter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPrintDialog(QAbstractPrintDialog):
  """
  The cute side of Qt's QPrintDialog: a plain Python object standing in front
  of one C++ QPrintDialog.

  It is built on the cute 'QAbstractPrintDialog', as Qt's QPrintDialog is
  built on Qt's QAbstractPrintDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPrintDialog that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'exec', 'accept', 'done',
  'setOption', 'testOption', 'setOptions', 'options', 'setVisible', 'open',
  'accepted'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPrintDialog::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPrintDialog::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPrintDialogPrivate *QPrintDialog::d_func()': gives
    'QPrintDialogPrivate', which has no cute class yet.
  - Qt's 'const QPrintDialogPrivate *QPrintDialog::d_func() const': gives
    'QPrintDialogPrivate', which has no cute class yet.
  - Qt's 'QPrintDialog::~QPrintDialog()': the destructor: Python never
    removes a C++ QPrintDialog.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPrintDialog is created at the first use, not by
    'QPrintDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPrintDialog.
  - Qt tells when it has removed the C++ QPrintDialog. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QPrintDialog::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#tr

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
    #  QString QPrintDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QPrintDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPrintDialog'

  #  A C++ QPrintDialog Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPrintDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPrintDialog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPrintDialog::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QPrintDialog10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QAbstractPrintDialog.PrintDialogOption)
  def testOption(
      self,
      option: QAbstractPrintDialog.PrintDialogOption,
  ) -> bool:
    """
    Calls Qt's 'bool QPrintDialog::testOption(PrintDialogOption option)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#testOption

    Parameters
    ----------

    option : QAbstractPrintDialog.PrintDialogOption
      Passed on as its number.
    """
    #  bool QPrintDialog::testOption(PrintDialogOption option) const
    return self.uglySide.call(
        'ritual_ZNK12QPrintDialog10testOptionEN20QAbstractPrintDialog17Prin'
        'tDialogOptionE',
        option.value,
    )

  def options(self) -> QAbstractPrintDialog.PrintDialogOptions:
    """
    Calls Qt's 'PrintDialogOptions QPrintDialog::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#options

    Returns
    -------

    QAbstractPrintDialog.PrintDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  PrintDialogOptions QPrintDialog::options() const
    return QAbstractPrintDialog.PrintDialogOptions(self.uglySide.call(
        'ritual_ZNK12QPrintDialog7optionsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractPrintDialog.PrintDialogOption)
  @overload(QAbstractPrintDialog.PrintDialogOption, bool)
  def setOption(
      self,
      option: QAbstractPrintDialog.PrintDialogOption,
      on: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QPrintDialog::setOption(PrintDialogOption option, bool
    on)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#setOption

    Parameters
    ----------

    option : QAbstractPrintDialog.PrintDialogOption
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QPrintDialog::setOption(PrintDialogOption option, bool on)
    self.uglySide.call(
        'ritual_ZN12QPrintDialog9setOptionEN20QAbstractPrintDialog17PrintDi'
        'alogOptionEb',
        option.value, on,
    )

  @overload(QAbstractPrintDialog.PrintDialogOptions)
  def setOptions(
      self,
      options: QAbstractPrintDialog.PrintDialogOptions,
  ) -> None:
    """
    Calls Qt's 'void QPrintDialog::setOptions(PrintDialogOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#setOptions

    Parameters
    ----------

    options : QAbstractPrintDialog.PrintDialogOptions
      Passed on as its number.
    """
    #  void QPrintDialog::setOptions(PrintDialogOptions options)
    self.uglySide.call(
        'ritual_ZN12QPrintDialog10setOptionsE6QFlagsIN20QAbstractPrintDialo'
        'g17PrintDialogOptionEE',
        options.value,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QPrintDialog::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QPrintDialog::setVisible(bool visible)
    ritual = 'ritual_ZN12QPrintDialog10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPrintDialog10setVisibleEb'
    self.uglySide.call(ritual, visible)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPrinter)
  @overload(NoneType)
  @overload(QPrinter, QWidget)
  @overload(QPrinter, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      printer: Optional[QPrinter],
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPrintDialog::QPrintDialog(QPrinter
    *printer, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#QPrintDialog

    Parameters
    ----------

    printer : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPrintDialog::QPrintDialog(QPrinter *printer, QWidget *parent)
    self._noteCreation(QPrintDialog, lambda: Rituals.call(
        'ritual_ZN12QPrintDialogC1EP8QPrinterP7QWidget',
        self._addressOf(printer), self._addressOf(parent),
    ))

  @overload()
  @overload(QWidget)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QPrintDialog::QPrintDialog(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#QPrintDialog

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPrintDialog::QPrintDialog(QWidget *parent)
    self._noteCreation(QPrintDialog, lambda: Rituals.call(
        'ritual_ZN12QPrintDialogC1EP7QWidget', self._addressOf(parent),
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

  def exec(self) -> int:
    """
    Calls Qt's 'int QPrintDialog::exec()'.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#exec
    """
    #  int QPrintDialog::exec()
    ritual = 'ritual_ZN12QPrintDialog4execEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPrintDialog4execEv'
    return self.uglySide.call(ritual)

  def accept(self) -> None:
    """
    Calls Qt's 'void QPrintDialog::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#accept
    """
    #  void QPrintDialog::accept()
    ritual = 'ritual_ZN12QPrintDialog6acceptEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPrintDialog6acceptEv'
    self.uglySide.call(ritual)

  @overload(int)
  def done(self, result: int) -> None:
    """
    Calls Qt's 'void QPrintDialog::done(int result)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#done

    Parameters
    ----------

    result : int
      Passed on as it is.
    """
    #  void QPrintDialog::done(int result)
    ritual = 'ritual_ZN12QPrintDialog4doneEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QPrintDialog4doneEi'
    self.uglySide.call(ritual, result)

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def open(self, receiver: Optional[QObject], member: Optional[str]) -> None:
    """
    Calls Qt's 'void QPrintDialog::open(QObject *receiver, const char
    *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#open

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QPrintDialog::open(QObject *receiver, const char *member)
    self.uglySide.call(
        'ritual_ZN12QPrintDialog4openEP7QObjectPKc',
        self._addressOf(receiver, 'QObject'), self._bytesOf(member),
    )

  @overload(QPrinter)
  @overload(NoneType)
  def accepted(self, printer: Optional[QPrinter]) -> None:
    """
    Calls Qt's 'void QPrintDialog::accepted(QPrinter *printer)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintdialog.html#accepted

    Parameters
    ----------

    printer : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPrintDialog::accepted(QPrinter *printer)
    self.uglySide.call(
        'ritual_ZN12QPrintDialog8acceptedEP8QPrinter',
        self._addressOf(printer),
    )

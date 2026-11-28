"""
QAbstractPrintDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/qabstractprintdialog.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtWidgets import QDialog, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAbstractPrintDialogPrivate, QPrinter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPrinter = WAIT['QPrinter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractPrintDialog(QDialog):
  """
  The cute side of Qt's QAbstractPrintDialog: a plain Python object standing
  in front of one C++ QAbstractPrintDialog.

  It is built on the cute 'QDialog', as Qt's QAbstractPrintDialog is built on
  Qt's QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractPrintDialog that has a ritual and that
  Python can call so far, 13 names in all: 'd_func', 'metaObject', 'tr',
  'setOptionTabs', 'setPrintRange', 'printRange', 'setMinMax', 'minPage',
  'maxPage', 'setFromTo', 'fromPage', 'toPage', 'printer'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractPrintDialogPrivate *QAbstractPrintDialog::d_func()
    const': takes in Python what 'QAbstractPrintDialogPrivate
    *QAbstractPrintDialog::d_func()' takes.
  - Qt's 'void *QAbstractPrintDialog::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstractPrintDialog::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractPrintDialog::~QAbstractPrintDialog()': the destructor:
    Python never removes a C++ QAbstractPrintDialog.
  - Qt's
    'QAbstractPrintDialog::QAbstractPrintDialog(QAbstractPrintDialogPrivate
    &ptr, QPrinter *printer, QWidget *parent)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstractPrintDialog is created at the first use, not by
    'QAbstractPrintDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractPrintDialog.
  - Qt tells when it has removed the C++ QAbstractPrintDialog. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAbstractPrintDialog, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class PrintDialogOption(CuteFlags):
    """
    The flags enum 'QAbstractPrintDialog::PrintDialogOption' of Qt, with the
    6 names Qt gives in it. Qt names the type of its combinations
    'QAbstractPrintDialog::PrintDialogOptions'.
    """

    PrintToFile = 0x1
    PrintSelection = 0x2
    PrintPageRange = 0x4
    PrintShowPageSize = 0x8
    PrintCollateCopies = 0x10
    PrintCurrentPage = 0x40

  PrintDialogOptions = PrintDialogOption

  class PrintRange(CuteNum):
    """
    The enum 'QAbstractPrintDialog::PrintRange' of Qt, with the 4 names Qt
    gives in it.
    """

    AllPages = Kee[int](0)
    Selection = Kee[int](1)
    PageRange = Kee[int](2)
    CurrentPage = Kee[int](3)

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
    Calls Qt's 'QString QAbstractPrintDialog::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractprintdialog.html#tr

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
    #  QString QAbstractPrintDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QAbstractPrintDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractPrintDialog'

  #  A C++ QAbstractPrintDialog Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractPrintDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractPrintDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprintdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractPrintDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QAbstractPrintDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def printRange(self) -> PrintRange:
    """
    Calls Qt's 'PrintRange QAbstractPrintDialog::printRange() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprintdialog.html#printRange

    Returns
    -------

    PrintRange
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PrintRange(number)'
      gives.
    """
    #  PrintRange QAbstractPrintDialog::printRange() const
    return QAbstractPrintDialog.PrintRange(self.uglySide.call(
        'ritual_ZNK20QAbstractPrintDialog10printRangeEv',
    ))

  def minPage(self) -> int:
    """
    Calls Qt's 'int QAbstractPrintDialog::minPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractprintdialog.html#minPage
    """
    #  int QAbstractPrintDialog::minPage() const
    return self.uglySide.call('ritual_ZNK20QAbstractPrintDialog7minPageEv')

  def maxPage(self) -> int:
    """
    Calls Qt's 'int QAbstractPrintDialog::maxPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractprintdialog.html#maxPage
    """
    #  int QAbstractPrintDialog::maxPage() const
    return self.uglySide.call('ritual_ZNK20QAbstractPrintDialog7maxPageEv')

  def fromPage(self) -> int:
    """
    Calls Qt's 'int QAbstractPrintDialog::fromPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractprintdialog.html#fromPage
    """
    #  int QAbstractPrintDialog::fromPage() const
    return self.uglySide.call('ritual_ZNK20QAbstractPrintDialog8fromPageEv')

  def toPage(self) -> int:
    """
    Calls Qt's 'int QAbstractPrintDialog::toPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractprintdialog.html#toPage
    """
    #  int QAbstractPrintDialog::toPage() const
    return self.uglySide.call('ritual_ZNK20QAbstractPrintDialog6toPageEv')

  def printer(self) -> Optional[QPrinter]:
    """
    Calls Qt's 'QPrinter *QAbstractPrintDialog::printer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractprintdialog.html#printer

    Returns
    -------

    Optional[QPrinter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPrinter *QAbstractPrintDialog::printer() const
    address = self.uglySide.call(
        'ritual_ZNK20QAbstractPrintDialog7printerEv',
    )
    from . import QPrinter
    return QPrinter._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QWidget])
  def setOptionTabs(self, tabs: QList[QWidget]) -> None:
    """
    Calls Qt's 'void QAbstractPrintDialog::setOptionTabs(const QList<QWidget
    *> &tabs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprintdialog.html#setOptionTabs

    Parameters
    ----------

    tabs : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QAbstractPrintDialog::setOptionTabs(const QList<QWidget *> &tabs)
    self.uglySide.call(
        'ritual_ZN20QAbstractPrintDialog13setOptionTabsERK5QListIP7QWidgetE',
        self._valueOf(tabs),
    )

  @overload(PrintRange)
  def setPrintRange(self, range: PrintRange) -> None:
    """
    Calls Qt's 'void QAbstractPrintDialog::setPrintRange(PrintRange range)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprintdialog.html#setPrintRange

    Parameters
    ----------

    range : PrintRange
      Passed on as its number.
    """
    #  void QAbstractPrintDialog::setPrintRange(PrintRange range)
    self.uglySide.call(
        'ritual_ZN20QAbstractPrintDialog13setPrintRangeENS_10PrintRangeE',
        range.value,
    )

  @overload(int, int)
  def setMinMax(self, min: int, max: int) -> None:
    """
    Calls Qt's 'void QAbstractPrintDialog::setMinMax(int min, int max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprintdialog.html#setMinMax

    Parameters
    ----------

    min : int
      Passed on as it is.

    max : int
      Passed on as it is.
    """
    #  void QAbstractPrintDialog::setMinMax(int min, int max)
    self.uglySide.call(
        'ritual_ZN20QAbstractPrintDialog9setMinMaxEii', min, max,
    )

  @overload(int, int)
  def setFromTo(self, fromPage: int, toPage: int) -> None:
    """
    Calls Qt's 'void QAbstractPrintDialog::setFromTo(int fromPage, int
    toPage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprintdialog.html#setFromTo

    Parameters
    ----------

    fromPage : int
      Passed on as it is.

    toPage : int
      Passed on as it is.
    """
    #  void QAbstractPrintDialog::setFromTo(int fromPage, int toPage)
    self.uglySide.call(
        'ritual_ZN20QAbstractPrintDialog9setFromToEii', fromPage, toPage,
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
    Notes what was given, for Qt's
    'QAbstractPrintDialog::QAbstractPrintDialog(QPrinter *printer, QWidget
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprintdialog.html#QAbstractPrintDialog

    Parameters
    ----------

    printer : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractPrintDialog::QAbstractPrintDialog(QPrinter *printer, QWidget
    #      *parent)
    self._noteCreation(QAbstractPrintDialog, lambda: Rituals.call(
        'ritual_ZN20QAbstractPrintDialogC1EP8QPrinterP7QWidget',
        self._addressOf(printer), self._addressOf(parent),
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

  def d_func(self) -> Optional[QAbstractPrintDialogPrivate]:
    """
    Calls Qt's 'QAbstractPrintDialogPrivate *QAbstractPrintDialog::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractprintdialog.html#d_func

    Returns
    -------

    Optional[QAbstractPrintDialogPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPrintDialogPrivate *QAbstractPrintDialog::d_func()
    address = self.uglySide.call('ritual_ZN20QAbstractPrintDialog6d_funcEv')
    from . import QAbstractPrintDialogPrivate
    return QAbstractPrintDialogPrivate._cuteAt(address)

"""
QPrintPreviewDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/qprintpreviewdialog.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtWidgets import QDialog, QWidget

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


class QPrintPreviewDialog(QDialog):
  """
  The cute side of Qt's QPrintPreviewDialog: a plain Python object standing
  in front of one C++ QPrintPreviewDialog.

  It is built on the cute 'QDialog', as Qt's QPrintPreviewDialog is built on
  Qt's QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPrintPreviewDialog that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'open',
  'printer', 'setVisible', 'done', 'paintRequested'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPrintPreviewDialog::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPrintPreviewDialog::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPrintPreviewDialogPrivate *QPrintPreviewDialog::d_func()': gives
    'QPrintPreviewDialogPrivate', which has no cute class yet.
  - Qt's 'const QPrintPreviewDialogPrivate *QPrintPreviewDialog::d_func()
    const': gives 'QPrintPreviewDialogPrivate', which has no cute class yet.
  - Qt's 'QPrintPreviewDialog::~QPrintPreviewDialog()': the destructor:
    Python never removes a C++ QPrintPreviewDialog.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPrintPreviewDialog is created at the first use, not by
    'QPrintPreviewDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPrintPreviewDialog.
  - Qt tells when it has removed the C++ QPrintPreviewDialog. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QPrintPreviewDialog::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintpreviewdialog.html#tr

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
    #  QString QPrintPreviewDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QPrintPreviewDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPrintPreviewDialog'

  #  A C++ QPrintPreviewDialog Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPrintPreviewDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPrintPreviewDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPrintPreviewDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QPrintPreviewDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QPrintPreviewDialog::setVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewdialog.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QPrintPreviewDialog::setVisible(bool visible)
    ritual = 'ritual_ZN19QPrintPreviewDialog10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPrintPreviewDialog10setVisibleEb'
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

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.WindowFlags)
  @overload(NoneType, Qt.WindowFlags)
  def __init__(
      self,
      parent: Optional[QWidget] = None,
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPrintPreviewDialog::QPrintPreviewDialog(QWidget *parent,
    Qt::WindowFlags flags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewdialog.html#QPrintPreviewDialog

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QPrintPreviewDialog::QPrintPreviewDialog(QWidget *parent,
    #      Qt::WindowFlags flags)
    self._noteCreation(QPrintPreviewDialog, lambda: Rituals.call(
        'ritual_ZN19QPrintPreviewDialogC1EP7QWidget6QFlagsIN2Qt10WindowType'
        'EE',
        self._addressOf(parent), flags.value,
    ))

  @overload(QPrinter)
  @overload(QPrinter, QWidget)
  @overload(QPrinter, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  @overload(QPrinter, QWidget, Qt.WindowFlags)
  @overload(QPrinter, NoneType, Qt.WindowFlags)
  @overload(NoneType, QWidget, Qt.WindowFlags)
  @overload(NoneType, NoneType, Qt.WindowFlags)
  def __init__(
      self,
      printer: Optional[QPrinter],
      parent: Optional[QWidget] = None,
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPrintPreviewDialog::QPrintPreviewDialog(QPrinter *printer, QWidget
    *parent, Qt::WindowFlags flags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewdialog.html#QPrintPreviewDialog

    Parameters
    ----------

    printer : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QPrintPreviewDialog::QPrintPreviewDialog(QPrinter *printer, QWidget
    #      *parent, Qt::WindowFlags flags)
    self._noteCreation(QPrintPreviewDialog, lambda: Rituals.call(
        'ritual_ZN19QPrintPreviewDialogC1EP8QPrinterP7QWidget6QFlagsIN2Qt10'
        'WindowTypeEE',
        self._addressOf(printer), self._addressOf(parent), flags.value,
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

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def open(self, receiver: Optional[QObject], member: Optional[str]) -> None:
    """
    Calls Qt's 'void QPrintPreviewDialog::open(QObject *receiver, const char
    *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintpreviewdialog.html#open

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QPrintPreviewDialog::open(QObject *receiver, const char *member)
    self.uglySide.call(
        'ritual_ZN19QPrintPreviewDialog4openEP7QObjectPKc',
        self._addressOf(receiver, 'QObject'), self._bytesOf(member),
    )

  def printer(self) -> Optional[QPrinter]:
    """
    Calls Qt's 'QPrinter *QPrintPreviewDialog::printer()'.

    Qt's own words: https://doc.qt.io/qt-6/qprintpreviewdialog.html#printer

    Returns
    -------

    Optional[QPrinter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPrinter *QPrintPreviewDialog::printer()
    address = self.uglySide.call('ritual_ZN19QPrintPreviewDialog7printerEv')
    from . import QPrinter
    return QPrinter._cuteAt(address)

  @overload(int)
  def done(self, result: int) -> None:
    """
    Calls Qt's 'void QPrintPreviewDialog::done(int result)'.

    Qt's own words: https://doc.qt.io/qt-6/qprintpreviewdialog.html#done

    Parameters
    ----------

    result : int
      Passed on as it is.
    """
    #  void QPrintPreviewDialog::done(int result)
    ritual = 'ritual_ZN19QPrintPreviewDialog4doneEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPrintPreviewDialog4doneEi'
    self.uglySide.call(ritual, result)

  @overload(QPrinter)
  @overload(NoneType)
  def paintRequested(self, printer: Optional[QPrinter]) -> None:
    """
    Calls Qt's 'void QPrintPreviewDialog::paintRequested(QPrinter *printer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprintpreviewdialog.html#paintRequested

    Parameters
    ----------

    printer : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPrintPreviewDialog::paintRequested(QPrinter *printer)
    self.uglySide.call(
        'ritual_ZN19QPrintPreviewDialog14paintRequestedEP8QPrinter',
        self._addressOf(printer),
    )

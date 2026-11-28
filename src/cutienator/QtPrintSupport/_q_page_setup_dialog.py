"""
QPageSetupDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/qpagesetupdialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtWidgets import QDialog, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QPageSetupDialogPrivate, QPrinter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPrinter = WAIT['QPrinter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPageSetupDialog(QDialog):
  """
  The cute side of Qt's QPageSetupDialog: a plain Python object standing in
  front of one C++ QPageSetupDialog.

  It is built on the cute 'QDialog', as Qt's QPageSetupDialog is built on
  Qt's QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPageSetupDialog that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'tr', 'd_func', 'exec',
  'open', 'done', 'printer'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPageSetupDialog::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPageSetupDialog::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QPageSetupDialogPrivate *QPageSetupDialog::d_func() const':
    takes in Python what 'QPageSetupDialogPrivate
    *QPageSetupDialog::d_func()' takes.
  - Qt's 'QPageSetupDialog::~QPageSetupDialog()': the destructor: Python
    never removes a C++ QPageSetupDialog.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPageSetupDialog is created at the first use, not by
    'QPageSetupDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPageSetupDialog.
  - Qt tells when it has removed the C++ QPageSetupDialog. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QPageSetupDialog::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesetupdialog.html#tr

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
    #  QString QPageSetupDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QPageSetupDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPageSetupDialog'

  #  A C++ QPageSetupDialog Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPageSetupDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPageSetupDialog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesetupdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPageSetupDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QPageSetupDialog10metaObjectEv',
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
    'QPageSetupDialog::QPageSetupDialog(QPrinter *printer, QWidget *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagesetupdialog.html#QPageSetupDialog

    Parameters
    ----------

    printer : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPageSetupDialog::QPageSetupDialog(QPrinter *printer, QWidget *parent)
    self._noteCreation(QPageSetupDialog, lambda: Rituals.call(
        'ritual_ZN16QPageSetupDialogC1EP8QPrinterP7QWidget',
        self._addressOf(printer), self._addressOf(parent),
    ))

  @overload()
  @overload(QWidget)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'QPageSetupDialog::QPageSetupDialog(QWidget *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagesetupdialog.html#QPageSetupDialog

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPageSetupDialog::QPageSetupDialog(QWidget *parent)
    self._noteCreation(QPageSetupDialog, lambda: Rituals.call(
        'ritual_ZN16QPageSetupDialogC1EP7QWidget', self._addressOf(parent),
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

  def d_func(self) -> Optional[QPageSetupDialogPrivate]:
    """
    Calls Qt's 'QPageSetupDialogPrivate *QPageSetupDialog::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesetupdialog.html#d_func

    Returns
    -------

    Optional[QPageSetupDialogPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPageSetupDialogPrivate *QPageSetupDialog::d_func()
    address = self.uglySide.call('ritual_ZN16QPageSetupDialog6d_funcEv')
    from . import QPageSetupDialogPrivate
    return QPageSetupDialogPrivate._cuteAt(address)

  def exec(self) -> int:
    """
    Calls Qt's 'int QPageSetupDialog::exec()'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesetupdialog.html#exec
    """
    #  int QPageSetupDialog::exec()
    ritual = 'ritual_ZN16QPageSetupDialog4execEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QPageSetupDialog4execEv'
    return self.uglySide.call(ritual)

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def open(self, receiver: Optional[QObject], member: Optional[str]) -> None:
    """
    Calls Qt's 'void QPageSetupDialog::open(QObject *receiver, const char
    *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesetupdialog.html#open

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QPageSetupDialog::open(QObject *receiver, const char *member)
    self.uglySide.call(
        'ritual_ZN16QPageSetupDialog4openEP7QObjectPKc',
        self._addressOf(receiver, 'QObject'), self._bytesOf(member),
    )

  @overload(int)
  def done(self, result: int) -> None:
    """
    Calls Qt's 'void QPageSetupDialog::done(int result)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesetupdialog.html#done

    Parameters
    ----------

    result : int
      Passed on as it is.
    """
    #  void QPageSetupDialog::done(int result)
    ritual = 'ritual_ZN16QPageSetupDialog4doneEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QPageSetupDialog4doneEi'
    self.uglySide.call(ritual, result)

  def printer(self) -> Optional[QPrinter]:
    """
    Calls Qt's 'QPrinter *QPageSetupDialog::printer()'.

    Qt's own words: https://doc.qt.io/qt-6/qpagesetupdialog.html#printer

    Returns
    -------

    Optional[QPrinter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPrinter *QPageSetupDialog::printer()
    address = self.uglySide.call('ritual_ZN16QPageSetupDialog7printerEv')
    from . import QPrinter
    return QPrinter._cuteAt(address)

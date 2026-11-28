"""
QProgressDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qprogressdialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QDialog, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QCloseEvent, QResizeEvent, QShowEvent
  from . import QLabel, QProgressBar, QPushButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCloseEvent = WAIT['QCloseEvent']
  QEvent = WAIT['QEvent']
  QLabel = WAIT['QLabel']
  QProgressBar = WAIT['QProgressBar']
  QPushButton = WAIT['QPushButton']
  QResizeEvent = WAIT['QResizeEvent']
  QShowEvent = WAIT['QShowEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QProgressDialog(QDialog):
  """
  The cute side of Qt's QProgressDialog: a plain Python object standing in
  front of one C++ QProgressDialog.

  It is built on the cute 'QDialog', as Qt's QProgressDialog is built on Qt's
  QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QProgressDialog that has a ritual and that Python
  can call so far, 32 names in all: 'metaObject', 'tr', 'setLabel',
  'setCancelButton', 'setBar', 'wasCanceled', 'minimum', 'maximum', 'value',
  'sizeHint', 'labelText', 'minimumDuration', 'setAutoReset', 'autoReset',
  'setAutoClose', 'autoClose', 'open', 'cancel', 'reset', 'setMaximum',
  'setMinimum', 'setRange', 'setValue', 'setLabelText',
  'setCancelButtonText', 'setMinimumDuration', 'canceled', 'resizeEvent',
  'closeEvent', 'changeEvent', 'showEvent', 'forceShow'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QProgressDialog::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QProgressDialog::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QProgressDialogPrivate *QProgressDialog::d_func()': gives
    'QProgressDialogPrivate', which has no cute class yet.
  - Qt's 'const QProgressDialogPrivate *QProgressDialog::d_func() const':
    gives 'QProgressDialogPrivate', which has no cute class yet.
  - Qt's 'QProgressDialog::~QProgressDialog()': the destructor: Python never
    removes a C++ QProgressDialog.

  What has no ritual
  ------------------

  4 of the 43 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QProgressDialog is created at the first use, not by
    'QProgressDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QProgressDialog.
  - Qt tells when it has removed the C++ QProgressDialog. Every call on the
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
    Calls Qt's 'QString QProgressDialog::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#tr

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
    #  QString QProgressDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QProgressDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QProgressDialog'

  #  A C++ QProgressDialog Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QProgressDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QProgressDialog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QProgressDialog::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QProgressDialog10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def wasCanceled(self) -> bool:
    """
    Calls Qt's 'bool QProgressDialog::wasCanceled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#wasCanceled
    """
    #  bool QProgressDialog::wasCanceled() const
    return self.uglySide.call('ritual_ZNK15QProgressDialog11wasCanceledEv')

  def minimum(self) -> int:
    """
    Calls Qt's 'int QProgressDialog::minimum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#minimum
    """
    #  int QProgressDialog::minimum() const
    return self.uglySide.call('ritual_ZNK15QProgressDialog7minimumEv')

  def maximum(self) -> int:
    """
    Calls Qt's 'int QProgressDialog::maximum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#maximum
    """
    #  int QProgressDialog::maximum() const
    return self.uglySide.call('ritual_ZNK15QProgressDialog7maximumEv')

  def value(self) -> int:
    """
    Calls Qt's 'int QProgressDialog::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#value
    """
    #  int QProgressDialog::value() const
    return self.uglySide.call('ritual_ZNK15QProgressDialog5valueEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QProgressDialog::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QProgressDialog::sizeHint() const
    ritual = 'ritual_ZNK15QProgressDialog8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QProgressDialog8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def labelText(self) -> str:
    """
    Calls Qt's 'QString QProgressDialog::labelText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#labelText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QProgressDialog::labelText() const
    return self.uglySide.call('ritual_ZNK15QProgressDialog9labelTextEv')

  def minimumDuration(self) -> int:
    """
    Calls Qt's 'int QProgressDialog::minimumDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprogressdialog.html#minimumDuration
    """
    #  int QProgressDialog::minimumDuration() const
    return self.uglySide.call(
        'ritual_ZNK15QProgressDialog15minimumDurationEv',
    )

  def autoReset(self) -> bool:
    """
    Calls Qt's 'bool QProgressDialog::autoReset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#autoReset
    """
    #  bool QProgressDialog::autoReset() const
    return self.uglySide.call('ritual_ZNK15QProgressDialog9autoResetEv')

  def autoClose(self) -> bool:
    """
    Calls Qt's 'bool QProgressDialog::autoClose() const'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#autoClose
    """
    #  bool QProgressDialog::autoClose() const
    return self.uglySide.call('ritual_ZNK15QProgressDialog9autoCloseEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLabel)
  @overload(NoneType)
  def setLabel(self, label: Optional[QLabel]) -> None:
    """
    Calls Qt's 'void QProgressDialog::setLabel(QLabel *label)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#setLabel

    Parameters
    ----------

    label : Optional[QLabel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProgressDialog::setLabel(QLabel *label)
    self.uglySide.call(
        'ritual_ZN15QProgressDialog8setLabelEP6QLabel',
        self._addressOf(label),
    )

  @overload(QPushButton)
  @overload(NoneType)
  def setCancelButton(self, button: Optional[QPushButton]) -> None:
    """
    Calls Qt's 'void QProgressDialog::setCancelButton(QPushButton *button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprogressdialog.html#setCancelButton

    Parameters
    ----------

    button : Optional[QPushButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProgressDialog::setCancelButton(QPushButton *button)
    self.uglySide.call(
        'ritual_ZN15QProgressDialog15setCancelButtonEP11QPushButton',
        self._addressOf(button),
    )

  @overload(QProgressBar)
  @overload(NoneType)
  def setBar(self, bar: Optional[QProgressBar]) -> None:
    """
    Calls Qt's 'void QProgressDialog::setBar(QProgressBar *bar)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#setBar

    Parameters
    ----------

    bar : Optional[QProgressBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProgressDialog::setBar(QProgressBar *bar)
    self.uglySide.call(
        'ritual_ZN15QProgressDialog6setBarEP12QProgressBar',
        self._addressOf(bar),
    )

  @overload(bool)
  def setAutoReset(self, reset: bool) -> None:
    """
    Calls Qt's 'void QProgressDialog::setAutoReset(bool reset)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#setAutoReset

    Parameters
    ----------

    reset : bool
      Passed on as it is.
    """
    #  void QProgressDialog::setAutoReset(bool reset)
    self.uglySide.call('ritual_ZN15QProgressDialog12setAutoResetEb', reset)

  @overload(bool)
  def setAutoClose(self, close: bool) -> None:
    """
    Calls Qt's 'void QProgressDialog::setAutoClose(bool close)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#setAutoClose

    Parameters
    ----------

    close : bool
      Passed on as it is.
    """
    #  void QProgressDialog::setAutoClose(bool close)
    self.uglySide.call('ritual_ZN15QProgressDialog12setAutoCloseEb', close)

  @overload(int)
  def setMaximum(self, maximum: int) -> None:
    """
    Calls Qt's 'void QProgressDialog::setMaximum(int maximum)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#setMaximum

    Parameters
    ----------

    maximum : int
      Passed on as it is.
    """
    #  void QProgressDialog::setMaximum(int maximum)
    self.uglySide.call('ritual_ZN15QProgressDialog10setMaximumEi', maximum)

  @overload(int)
  def setMinimum(self, minimum: int) -> None:
    """
    Calls Qt's 'void QProgressDialog::setMinimum(int minimum)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#setMinimum

    Parameters
    ----------

    minimum : int
      Passed on as it is.
    """
    #  void QProgressDialog::setMinimum(int minimum)
    self.uglySide.call('ritual_ZN15QProgressDialog10setMinimumEi', minimum)

  @overload(int, int)
  def setRange(self, minimum: int, maximum: int) -> None:
    """
    Calls Qt's 'void QProgressDialog::setRange(int minimum, int maximum)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#setRange

    Parameters
    ----------

    minimum : int
      Passed on as it is.

    maximum : int
      Passed on as it is.
    """
    #  void QProgressDialog::setRange(int minimum, int maximum)
    self.uglySide.call(
        'ritual_ZN15QProgressDialog8setRangeEii', minimum, maximum,
    )

  @overload(int)
  def setValue(self, progress: int) -> None:
    """
    Calls Qt's 'void QProgressDialog::setValue(int progress)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#setValue

    Parameters
    ----------

    progress : int
      Passed on as it is.
    """
    #  void QProgressDialog::setValue(int progress)
    self.uglySide.call('ritual_ZN15QProgressDialog8setValueEi', progress)

  @overload(str)
  def setLabelText(self, text: str) -> None:
    """
    Calls Qt's 'void QProgressDialog::setLabelText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#setLabelText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QProgressDialog::setLabelText(const QString &text)
    self.uglySide.call(
        'ritual_ZN15QProgressDialog12setLabelTextERK7QString', text,
    )

  @overload(str)
  def setCancelButtonText(self, text: str) -> None:
    """
    Calls Qt's 'void QProgressDialog::setCancelButtonText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprogressdialog.html#setCancelButtonText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QProgressDialog::setCancelButtonText(const QString &text)
    self.uglySide.call(
        'ritual_ZN15QProgressDialog19setCancelButtonTextERK7QString', text,
    )

  @overload(int)
  def setMinimumDuration(self, ms: int) -> None:
    """
    Calls Qt's 'void QProgressDialog::setMinimumDuration(int ms)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qprogressdialog.html#setMinimumDuration

    Parameters
    ----------

    ms : int
      Passed on as it is.
    """
    #  void QProgressDialog::setMinimumDuration(int ms)
    self.uglySide.call(
        'ritual_ZN15QProgressDialog18setMinimumDurationEi', ms,
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
    Notes what was given, for Qt's 'QProgressDialog::QProgressDialog(QWidget
    *parent, Qt::WindowFlags flags)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprogressdialog.html#QProgressDialog

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QProgressDialog::QProgressDialog(QWidget *parent, Qt::WindowFlags
    #      flags)
    self._noteCreation(QProgressDialog, lambda: Rituals.call(
        'ritual_ZN15QProgressDialogC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), flags.value,
    ))

  @overload(str, str, int, int)
  @overload(str, str, int, int, QWidget)
  @overload(str, str, int, int, NoneType)
  @overload(str, str, int, int, QWidget, Qt.WindowFlags)
  @overload(str, str, int, int, NoneType, Qt.WindowFlags)
  def __init__(
      self,
      labelText: str,
      cancelButtonText: str,
      minimum: int,
      maximum: int,
      parent: Optional[QWidget] = None,
      flags: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QProgressDialog::QProgressDialog(const
    QString &labelText, const QString &cancelButtonText, int minimum, int
    maximum, QWidget *parent, Qt::WindowFlags flags)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qprogressdialog.html#QProgressDialog

    Parameters
    ----------

    labelText : str
      Passed on as it is: a QString is made of it for the call.

    cancelButtonText : str
      Passed on as it is: a QString is made of it for the call.

    minimum : int
      Passed on as it is.

    maximum : int
      Passed on as it is.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QProgressDialog::QProgressDialog(const QString &labelText, const
    #      QString &cancelButtonText, int minimum, int maximum, QWidget
    #      *parent, Qt::WindowFlags flags)
    self._noteCreation(QProgressDialog, lambda: Rituals.call(
        'ritual_ZN15QProgressDialogC1ERK7QStringS2_iiP7QWidget6QFlagsIN2Qt1'
        '0WindowTypeEE',
        labelText, cancelButtonText, minimum, maximum,
        self._addressOf(parent), flags.value,
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
    Calls Qt's 'void QProgressDialog::open(QObject *receiver, const char
    *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#open

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QProgressDialog::open(QObject *receiver, const char *member)
    self.uglySide.call(
        'ritual_ZN15QProgressDialog4openEP7QObjectPKc',
        self._addressOf(receiver, 'QObject'), self._bytesOf(member),
    )

  def cancel(self) -> None:
    """
    Calls Qt's 'void QProgressDialog::cancel()'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#cancel
    """
    #  void QProgressDialog::cancel()
    self.uglySide.call('ritual_ZN15QProgressDialog6cancelEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QProgressDialog::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#reset
    """
    #  void QProgressDialog::reset()
    self.uglySide.call('ritual_ZN15QProgressDialog5resetEv')

  def canceled(self) -> None:
    """
    Calls Qt's 'void QProgressDialog::canceled()'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#canceled
    """
    #  void QProgressDialog::canceled()
    self.uglySide.call('ritual_ZN15QProgressDialog8canceledEv')

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QProgressDialog::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProgressDialog::resizeEvent(QResizeEvent *event)
    ritual = 'ritual_ZN15QProgressDialog11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QProgressDialog11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QCloseEvent)
  @overload(NoneType)
  def closeEvent(self, event: Optional[QCloseEvent]) -> None:
    """
    Calls Qt's 'void QProgressDialog::closeEvent(QCloseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#closeEvent

    Parameters
    ----------

    event : Optional[QCloseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProgressDialog::closeEvent(QCloseEvent *event)
    ritual = 'ritual_ZN15QProgressDialog10closeEventEP11QCloseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QProgressDialog10closeEventEP11QCloseEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QProgressDialog::changeEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#changeEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProgressDialog::changeEvent(QEvent *event)
    ritual = 'ritual_ZN15QProgressDialog11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QProgressDialog11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, event: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QProgressDialog::showEvent(QShowEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#showEvent

    Parameters
    ----------

    event : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QProgressDialog::showEvent(QShowEvent *event)
    ritual = 'ritual_ZN15QProgressDialog9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QProgressDialog9showEventEP10QShowEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def forceShow(self) -> None:
    """
    Calls Qt's 'void QProgressDialog::forceShow()'.

    Qt's own words: https://doc.qt.io/qt-6/qprogressdialog.html#forceShow
    """
    #  void QProgressDialog::forceShow()
    self.uglySide.call('ritual_ZN15QProgressDialog9forceShowEv')

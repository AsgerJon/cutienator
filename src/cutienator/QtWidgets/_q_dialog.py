"""
QDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qdialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from . import QDialogDialogCode, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDialog(QWidget):
  """
  The cute side of Qt's QDialog: a plain Python object standing in front of
  one C++ QDialog.

  It is built on the cute 'QWidget', as Qt's QDialog is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDialog that has a ritual and that Python can call
  so far, 15 names in all: 'metaObject', 'tr', 'result', 'setVisible',
  'sizeHint', 'minimumSizeHint', 'setSizeGripEnabled', 'isSizeGripEnabled',
  'setModal', 'setResult', 'open', 'exec', 'done', 'accept', 'reject'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDialog::~QDialog()': the destructor: Python never removes a C++
    QDialog.

  What has no ritual
  ------------------

  19 of the 36 functions Qt declares: 8 protected; 3 private; 3 a signal; 2
  takes or gives a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QDialog is created at the first use, not by 'QDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDialog.
  - Qt tells when it has removed the C++ QDialog. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QDialog, and the names Qt has for the
  #  combinations of its flags enums.
  DialogCode = QDialogDialogCode

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
    Calls Qt's 'QString QDialog::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#tr

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
    #  QString QDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDialog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDialog::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QDialog10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def result(self) -> int:
    """
    Calls Qt's 'int QDialog::result() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#result
    """
    #  int QDialog::result() const
    return self.uglySide.call('ritual_ZNK7QDialog6resultEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QDialog::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDialog::sizeHint() const
    address = self.uglySide.call('ritual_ZNK7QDialog8sizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QDialog::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDialog::minimumSizeHint() const
    address = self.uglySide.call('ritual_ZNK7QDialog15minimumSizeHintEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isSizeGripEnabled(self) -> bool:
    """
    Calls Qt's 'bool QDialog::isSizeGripEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#isSizeGripEnabled
    """
    #  bool QDialog::isSizeGripEnabled() const
    return self.uglySide.call('ritual_ZNK7QDialog17isSizeGripEnabledEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QDialog::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QDialog::setVisible(bool visible)
    self.uglySide.call('ritual_ZN7QDialog10setVisibleEb', visible)

  @overload(bool)
  def setSizeGripEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QDialog::setSizeGripEnabled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#setSizeGripEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QDialog::setSizeGripEnabled(bool a0)
    self.uglySide.call('ritual_ZN7QDialog18setSizeGripEnabledEb', a0)

  @overload(bool)
  def setModal(self, modal: bool) -> None:
    """
    Calls Qt's 'void QDialog::setModal(bool modal)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#setModal

    Parameters
    ----------

    modal : bool
      Passed on as it is.
    """
    #  void QDialog::setModal(bool modal)
    self.uglySide.call('ritual_ZN7QDialog8setModalEb', modal)

  @overload(int)
  def setResult(self, r: int) -> None:
    """
    Calls Qt's 'void QDialog::setResult(int r)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#setResult

    Parameters
    ----------

    r : int
      Passed on as it is.
    """
    #  void QDialog::setResult(int r)
    self.uglySide.call('ritual_ZN7QDialog9setResultEi', r)

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
      f: Qt.WindowFlags = Qt.WindowFlags(),
  ) -> None:
    """
    Notes what was given, for Qt's 'QDialog::QDialog(QWidget *parent,
    Qt::WindowFlags f)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#QDialog

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    f : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags().
    """
    #  QDialog::QDialog(QWidget *parent, Qt::WindowFlags f)
    self._noteCreation(QDialog, lambda: Rituals.call(
        'ritual_ZN7QDialogC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE',
        self._addressOf(parent), f.value,
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

  def open(self) -> None:
    """
    Calls Qt's 'void QDialog::open()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#open
    """
    #  void QDialog::open()
    self.uglySide.call('ritual_ZN7QDialog4openEv')

  def exec(self) -> int:
    """
    Calls Qt's 'int QDialog::exec()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#exec
    """
    #  int QDialog::exec()
    return self.uglySide.call('ritual_ZN7QDialog4execEv')

  @overload(int)
  def done(self, a0: int) -> None:
    """
    Calls Qt's 'void QDialog::done(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#done

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QDialog::done(int a0)
    self.uglySide.call('ritual_ZN7QDialog4doneEi', a0)

  def accept(self) -> None:
    """
    Calls Qt's 'void QDialog::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#accept
    """
    #  void QDialog::accept()
    self.uglySide.call('ritual_ZN7QDialog6acceptEv')

  def reject(self) -> None:
    """
    Calls Qt's 'void QDialog::reject()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#reject
    """
    #  void QDialog::reject()
    self.uglySide.call('ritual_ZN7QDialog6rejectEv')

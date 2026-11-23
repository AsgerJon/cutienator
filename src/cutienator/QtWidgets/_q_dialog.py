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
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QCloseEvent, QContextMenuEvent, QKeyEvent, QResizeEvent
  from ..QtGui import QShowEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCloseEvent = WAIT['QCloseEvent']
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QEvent = WAIT['QEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QShowEvent = WAIT['QShowEvent']

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
  so far, 22 names in all: 'metaObject', 'tr', 'result', 'setVisible',
  'sizeHint', 'minimumSizeHint', 'setSizeGripEnabled', 'isSizeGripEnabled',
  'setModal', 'setResult', 'open', 'exec', 'done', 'accept', 'reject',
  'keyPressEvent', 'closeEvent', 'showEvent', 'resizeEvent',
  'contextMenuEvent', 'eventFilter', 'adjustPosition'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDialog::~QDialog()': the destructor: Python never removes a C++
    QDialog.

  What has no ritual
  ------------------

  12 of the 36 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 3 a signal; 2 forbidden; 1 a template; 1 declared and nowhere
  to be found.

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

  #  The enums Qt writes inside QDialog, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class DialogCode(CuteNum):
    """
    The enum 'QDialog::DialogCode' of Qt, with the 2 names Qt gives in it.
    """

    Rejected = Kee[int](0)
    Accepted = Kee[int](1)

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

  #  A C++ QDialog Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDialog'

  #  The functions Qt calls itself that QDialog is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'open': (
          ('_ZN7QDialog4openEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'exec': (
          ('_ZN7QDialog4execEv',
           ('int', 'number', ''),
           ()),
      ),
      'done': (
          ('_ZN7QDialog4doneEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'accept': (
          ('_ZN7QDialog6acceptEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'reject': (
          ('_ZN7QDialog6rejectEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

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
    ritual = 'ritual_ZNK7QDialog8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QDialog8sizeHintEv'
    address = self.uglySide.call(ritual)
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
    ritual = 'ritual_ZNK7QDialog15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QDialog15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
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
    ritual = 'ritual_ZN7QDialog10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QDialog10setVisibleEb'
    self.uglySide.call(ritual, visible)

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
    ritual = 'ritual_ZN7QDialog4openEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QDialog4openEv'
    self.uglySide.call(ritual)

  def exec(self) -> int:
    """
    Calls Qt's 'int QDialog::exec()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#exec
    """
    #  int QDialog::exec()
    ritual = 'ritual_ZN7QDialog4execEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QDialog4execEv'
    return self.uglySide.call(ritual)

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
    ritual = 'ritual_ZN7QDialog4doneEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QDialog4doneEi'
    self.uglySide.call(ritual, a0)

  def accept(self) -> None:
    """
    Calls Qt's 'void QDialog::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#accept
    """
    #  void QDialog::accept()
    ritual = 'ritual_ZN7QDialog6acceptEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QDialog6acceptEv'
    self.uglySide.call(ritual)

  def reject(self) -> None:
    """
    Calls Qt's 'void QDialog::reject()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#reject
    """
    #  void QDialog::reject()
    ritual = 'ritual_ZN7QDialog6rejectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QDialog6rejectEv'
    self.uglySide.call(ritual)

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QDialog::keyPressEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#keyPressEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialog::keyPressEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN7QDialog13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QDialog13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QCloseEvent)
  @overload(NoneType)
  def closeEvent(self, a0: Optional[QCloseEvent]) -> None:
    """
    Calls Qt's 'void QDialog::closeEvent(QCloseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#closeEvent

    Parameters
    ----------

    a0 : Optional[QCloseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialog::closeEvent(QCloseEvent *a0)
    ritual = 'ritual_ZN7QDialog10closeEventEP11QCloseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QDialog10closeEventEP11QCloseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, a0: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QDialog::showEvent(QShowEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#showEvent

    Parameters
    ----------

    a0 : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialog::showEvent(QShowEvent *a0)
    ritual = 'ritual_ZN7QDialog9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QDialog9showEventEP10QShowEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QDialog::resizeEvent(QResizeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialog::resizeEvent(QResizeEvent *a0)
    ritual = 'ritual_ZN7QDialog11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QDialog11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(self, a0: Optional[QContextMenuEvent]) -> None:
    """
    Calls Qt's 'void QDialog::contextMenuEvent(QContextMenuEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#contextMenuEvent

    Parameters
    ----------

    a0 : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialog::contextMenuEvent(QContextMenuEvent *a0)
    ritual = 'ritual_ZN7QDialog16contextMenuEventEP17QContextMenuEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QDialog16contextMenuEventEP17QContextMenuEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QDialog::eventFilter(QObject *a0, QEvent *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#eventFilter

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDialog::eventFilter(QObject *a0, QEvent *a1)
    ritual = 'ritual_ZN7QDialog11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QDialog11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(a0, 'QObject'), self._addressOf(a1),
    )

  @overload(QWidget)
  @overload(NoneType)
  def adjustPosition(self, a0: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QDialog::adjustPosition(QWidget *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialog.html#adjustPosition

    Parameters
    ----------

    a0 : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialog::adjustPosition(QWidget *a0)
    self.uglySide.call(
        'ritual_ZN7QDialog14adjustPositionEP7QWidget', self._addressOf(a0),
    )

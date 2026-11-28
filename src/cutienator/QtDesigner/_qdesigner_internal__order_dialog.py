"""
qdesigner_internal::OrderDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/orderdialog_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::OrderDialog to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtWidgets import QDialog, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class OrderDialog(QDialog):
  """
  The cute side of Qt's qdesigner_internal::OrderDialog: a plain Python
  object standing in front of one C++ qdesigner_internal::OrderDialog.

  It is built on the cute 'QDialog', as Qt's qdesigner_internal::OrderDialog
  is built on Qt's QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::OrderDialog that has a ritual
  and that Python can call so far, 15 names in all: 'metaObject', 'tr',
  'pagesOfContainer', 'setPageList', 'pageList', 'setDescription',
  'setFormat', 'format', 'upButtonClicked', 'downButtonClicked',
  'pageListCurrentRowChanged', 'slotEnableButtonsAfterDnD', 'slotReset',
  'buildList', 'enableButtons'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::OrderDialog::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::OrderDialog::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::OrderDialog::~OrderDialog()': the destructor:
    Python never removes a C++ qdesigner_internal::OrderDialog.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::OrderDialog is created at the first use, not
    by 'qdesigner_internal::OrderDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::OrderDialog.
  - Qt tells when it has removed the C++ qdesigner_internal::OrderDialog.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside qdesigner_internal::OrderDialog, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class Format(CuteNum):
    """
    The enum 'qdesigner_internal::OrderDialog::Format' of Qt, with the 2
    names Qt gives in it.
    """

    PageOrderFormat = Kee[int](0)
    TabOrderFormat = Kee[int](1)

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
    Calls Qt's 'QString qdesigner_internal::OrderDialog::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html#tr

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
    #  QString qdesigner_internal::OrderDialog::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal11OrderDialog2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def pagesOfContainer(
      core: Optional[QDesignerFormEditorInterface],
      container: Optional[QWidget],
  ) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList
    qdesigner_internal::OrderDialog::pagesOfContainer(const
    QDesignerFormEditorInterface *core, QWidget *container)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    container : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList qdesigner_internal::OrderDialog::pagesOfContainer(const
    #      QDesignerFormEditorInterface *core, QWidget *container)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal11OrderDialog16pagesOfContainerEPK28Q'
        'DesignerFormEditorInterfaceP7QWidget',
        CuteMixin._addressOf(core), CuteMixin._addressOf(container),
    )
    return QList[QWidget]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::OrderDialog'

  #  A C++ qdesigner_internal::OrderDialog Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_OrderDialog'

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
    *qdesigner_internal::OrderDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::OrderDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal11OrderDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pageList(self) -> QList[QWidget]:
    """
    Calls Qt's 'QWidgetList qdesigner_internal::OrderDialog::pageList()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html#pageList

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QWidgetList qdesigner_internal::OrderDialog::pageList() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal11OrderDialog8pageListEv',
    )
    return QList[QWidget]._cuteOwning(address)

  def format(self) -> Format:
    """
    Calls Qt's 'Format qdesigner_internal::OrderDialog::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html#format

    Returns
    -------

    Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Format(number)' gives.
    """
    #  Format qdesigner_internal::OrderDialog::format() const
    return OrderDialog.Format(self.uglySide.call(
        'ritual_ZNK18qdesigner_internal11OrderDialog6formatEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QWidget])
  def setPageList(self, pages: QList[QWidget]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::OrderDialog::setPageList(const
    QWidgetList &pages)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html#setPageList

    Parameters
    ----------

    pages : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::OrderDialog::setPageList(const QWidgetList
    #      &pages)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11OrderDialog11setPageListERK5QListIP'
        '7QWidgetE',
        self._valueOf(pages),
    )

  @overload(str)
  def setDescription(self, d: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::OrderDialog::setDescription(const
    QString &d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html#setDescription

    Parameters
    ----------

    d : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::OrderDialog::setDescription(const QString &d)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11OrderDialog14setDescriptionERK7QStr'
        'ing',
        d,
    )

  @overload(Format)
  def setFormat(self, f: Format) -> None:
    """
    Calls Qt's 'void qdesigner_internal::OrderDialog::setFormat(Format f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html#setFormat

    Parameters
    ----------

    f : Format
      Passed on as its number.
    """
    #  void qdesigner_internal::OrderDialog::setFormat(Format f)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11OrderDialog9setFormatENS0_6FormatE',
        f.value,
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

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::OrderDialog::OrderDialog(QWidget *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html#OrderDialog

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::OrderDialog::OrderDialog(QWidget *parent)
    self._noteCreation(OrderDialog, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal11OrderDialogC1EP7QWidget',
        self._addressOf(parent),
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

  def upButtonClicked(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::OrderDialog::upButtonClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html
    """
    #  void qdesigner_internal::OrderDialog::upButtonClicked()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11OrderDialog15upButtonClickedEv',
    )

  def downButtonClicked(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::OrderDialog::downButtonClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html
    """
    #  void qdesigner_internal::OrderDialog::downButtonClicked()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11OrderDialog17downButtonClickedEv',
    )

  @overload(int)
  def pageListCurrentRowChanged(self, row: int) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::OrderDialog::pageListCurrentRowChanged(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void qdesigner_internal::OrderDialog::pageListCurrentRowChanged(int
    #      row)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11OrderDialog25pageListCurrentRowChan'
        'gedEi',
        row,
    )

  def slotEnableButtonsAfterDnD(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::OrderDialog::slotEnableButtonsAfterDnD()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html
    """
    #  void qdesigner_internal::OrderDialog::slotEnableButtonsAfterDnD()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11OrderDialog25slotEnableButtonsAfter'
        'DnDEv',
    )

  def slotReset(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::OrderDialog::slotReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html#slotReset
    """
    #  void qdesigner_internal::OrderDialog::slotReset()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11OrderDialog9slotResetEv',
    )

  def buildList(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::OrderDialog::buildList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html#buildList
    """
    #  void qdesigner_internal::OrderDialog::buildList()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11OrderDialog9buildListEv',
    )

  @overload(int)
  def enableButtons(self, r: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::OrderDialog::enableButtons(int r)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-orderdialog.html#enableButtons

    Parameters
    ----------

    r : int
      Passed on as it is.
    """
    #  void qdesigner_internal::OrderDialog::enableButtons(int r)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal11OrderDialog13enableButtonsEi', r,
    )

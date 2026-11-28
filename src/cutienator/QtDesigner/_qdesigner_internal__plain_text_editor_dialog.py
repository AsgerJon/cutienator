"""
qdesigner_internal::PlainTextEditorDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/plaintexteditor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PlainTextEditorDialog to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QDialog, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QFont = WAIT['QFont']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PlainTextEditorDialog(QDialog):
  """
  The cute side of Qt's qdesigner_internal::PlainTextEditorDialog: a plain
  Python object standing in front of one C++
  qdesigner_internal::PlainTextEditorDialog.

  It is built on the cute 'QDialog', as Qt's
  qdesigner_internal::PlainTextEditorDialog is built on Qt's QDialog, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::PlainTextEditorDialog that has a
  ritual and that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'showDialog', 'setDefaultFont', 'setText', 'text'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::PlainTextEditorDialog::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::PlainTextEditorDialog::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'qdesigner_internal::PlainTextEditorDialog::~PlainTextEditorDialog()':
    the destructor: Python never removes a C++
    qdesigner_internal::PlainTextEditorDialog.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::PlainTextEditorDialog is created at the first
    use, not by 'qdesigner_internal::PlainTextEditorDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::PlainTextEditorDialog.
  - Qt tells when it has removed the C++
    qdesigner_internal::PlainTextEditorDialog. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
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
    Calls Qt's 'QString qdesigner_internal::PlainTextEditorDialog::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-plaintexteditordialog.html#tr

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
    #  QString qdesigner_internal::PlainTextEditorDialog::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal21PlainTextEditorDialog2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::PlainTextEditorDialog'

  #  A C++ qdesigner_internal::PlainTextEditorDialog Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_PlainTextEditorDialog'

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
    *qdesigner_internal::PlainTextEditorDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-plaintexteditordialog.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::PlainTextEditorDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal21PlainTextEditorDialog10metaObjectE'
        'v',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::PlainTextEditorDialog::text()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-plaintexteditordialog.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::PlainTextEditorDialog::text() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal21PlainTextEditorDialog4textEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setDefaultFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PlainTextEditorDialog::setDefaultFont(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-plaintexteditordialog.html

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void qdesigner_internal::PlainTextEditorDialog::setDefaultFont(const
    #      QFont &font)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal21PlainTextEditorDialog14setDefaultFo'
        'ntERK5QFont',
        self._valueOf(font),
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::PlainTextEditorDialog::setText(const
    QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-plaintexteditordialog.html

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PlainTextEditorDialog::setText(const QString
    #      &text)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal21PlainTextEditorDialog7setTextERK7QS'
        'tring',
        text,
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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      core: Optional[QDesignerFormEditorInterface],
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PlainTextEditorDialog::PlainTextEditorDialog(
    QDesignerFormEditorInterface *core, QWidget *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-plaintexteditordialog.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::PlainTextEditorDialog::PlainTextEditorDialog(
    #      QDesignerFormEditorInterface *core, QWidget *parent)
    self._noteCreation(PlainTextEditorDialog, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal21PlainTextEditorDialogC1EP28QDesigne'
        'rFormEditorInterfaceP7QWidget',
        self._addressOf(core), self._addressOf(parent),
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

  def showDialog(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::PlainTextEditorDialog::showDialog()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-plaintexteditordialog.html
    """
    #  int qdesigner_internal::PlainTextEditorDialog::showDialog()
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal21PlainTextEditorDialog10showDialogEv',
    )

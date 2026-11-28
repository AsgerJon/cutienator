"""
qdesigner_internal::StyleSheetEditorDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/stylesheeteditor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::StyleSheetEditorDialog to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtWidgets import QDialog, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QKeyEvent
  from ..QtWidgets import QDialogButtonBox
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QKeyEvent = WAIT['QKeyEvent']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class StyleSheetEditorDialog(QDialog):
  """
  The cute side of Qt's qdesigner_internal::StyleSheetEditorDialog: a plain
  Python object standing in front of one C++
  qdesigner_internal::StyleSheetEditorDialog.

  It is built on the cute 'QDialog', as Qt's
  qdesigner_internal::StyleSheetEditorDialog is built on Qt's QDialog, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::StyleSheetEditorDialog that has
  a ritual and that Python can call so far, 16 names in all: 'metaObject',
  'tr', 'text', 'setText', 'isStyleSheetValid', 'validateStyleSheet',
  'slotContextMenuRequested', 'slotAddResource', 'slotAddGradient',
  'slotAddColor', 'slotAddFont', 'slotRequestHelp', 'keyPressEvent',
  'buttonBox', 'setOkButtonEnabled', 'insertCssProperty'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::StyleSheetEditorDialog::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::StyleSheetEditorDialog::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'qdesigner_internal::StyleSheetEditorDialog::~StyleSheetEditorDialog()':
    the destructor: Python never removes a C++
    qdesigner_internal::StyleSheetEditorDialog.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::StyleSheetEditorDialog is created at the
    first use, not by 'qdesigner_internal::StyleSheetEditorDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::StyleSheetEditorDialog.
  - Qt tells when it has removed the C++
    qdesigner_internal::StyleSheetEditorDialog. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside qdesigner_internal::StyleSheetEditorDialog,
  #  each a class in here as in C++, and the names Qt has for the
  #  combinations of its flags enums.

  class Mode(CuteNum):
    """
    The enum 'qdesigner_internal::StyleSheetEditorDialog::Mode' of Qt, with
    the 2 names Qt gives in it.
    """

    ModeGlobal = Kee[int](0)
    ModePerForm = Kee[int](1)

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
    Calls Qt's 'QString qdesigner_internal::StyleSheetEditorDialog::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html#tr

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
    #  QString qdesigner_internal::StyleSheetEditorDialog::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialog2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  def isStyleSheetValid(styleSheet: str) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::StyleSheetEditorDialog::isStyleSheetValid(const
    QString &styleSheet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html

    Parameters
    ----------

    styleSheet : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool qdesigner_internal::StyleSheetEditorDialog::isStyleSheetValid(
    #      const QString &styleSheet)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialog17isStyleShee'
        'tValidERK7QString',
        styleSheet,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::StyleSheetEditorDialog'

  #  A C++ qdesigner_internal::StyleSheetEditorDialog Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_StyleSheetEditorDialog'

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
    *qdesigner_internal::StyleSheetEditorDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::StyleSheetEditorDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22StyleSheetEditorDialog10metaObject'
        'Ev',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::StyleSheetEditorDialog::text()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::StyleSheetEditorDialog::text() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22StyleSheetEditorDialog4textEv',
    )

  def buttonBox(self) -> Optional[QDialogButtonBox]:
    """
    Calls Qt's 'QDialogButtonBox
    *qdesigner_internal::StyleSheetEditorDialog::buttonBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html

    Returns
    -------

    Optional[QDialogButtonBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDialogButtonBox
    #      *qdesigner_internal::StyleSheetEditorDialog::buttonBox() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22StyleSheetEditorDialog9buttonBoxEv',
    )
    from ..QtWidgets import QDialogButtonBox
    return QDialogButtonBox._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, t: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::StyleSheetEditorDialog::setText(const QString &t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html

    Parameters
    ----------

    t : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::StyleSheetEditorDialog::setText(const QString
    #      &t)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialog7setTextERK7Q'
        'String',
        t,
    )

  @overload(bool)
  def setOkButtonEnabled(self, v: bool) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::StyleSheetEditorDialog::setOkButtonEnabled(bool v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::StyleSheetEditorDialog::setOkButtonEnabled(
    #      bool v)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialog18setOkButton'
        'EnabledEb',
        v,
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

  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  @overload(QDesignerFormEditorInterface, QWidget, Mode)
  @overload(QDesignerFormEditorInterface, NoneType, Mode)
  @overload(NoneType, QWidget, Mode)
  @overload(NoneType, NoneType, Mode)
  def __init__(
      self,
      core: Optional[QDesignerFormEditorInterface],
      parent: Optional[QWidget],
      mode: Mode = Mode.ModePerForm,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::StyleSheetEditorDialog::StyleSheetEditorDialog(
    QDesignerFormEditorInterface *core, QWidget *parent, Mode mode)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.ModePerForm.
    """
    #  qdesigner_internal::StyleSheetEditorDialog::
    #      StyleSheetEditorDialog(QDesignerFormEditorInterface *core, QWidget
    #      *parent, Mode mode)
    self._noteCreation(StyleSheetEditorDialog, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialogC1EP28QDesign'
        'erFormEditorInterfaceP7QWidgetNS0_4ModeE',
        self._addressOf(core), self._addressOf(parent), mode.value,
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

  def validateStyleSheet(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::StyleSheetEditorDialog::validateStyleSheet()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html
    """
    #  void qdesigner_internal::StyleSheetEditorDialog::validateStyleSheet()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialog18validateSty'
        'leSheetEv',
    )

  @overload(QPoint)
  def slotContextMenuRequested(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::StyleSheetEditorDialog::slotContextMenuRequested(
    const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::StyleSheetEditorDialog::
    #      slotContextMenuRequested(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialog24slotContext'
        'MenuRequestedERK6QPoint',
        self._valueOf(pos),
    )

  @overload(str)
  def slotAddResource(self, property: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::StyleSheetEditorDialog::slotAddResource(const QString
    &property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html

    Parameters
    ----------

    property : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::StyleSheetEditorDialog::slotAddResource(const
    #      QString &property)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialog15slotAddReso'
        'urceERK7QString',
        property,
    )

  @overload(str)
  def slotAddGradient(self, property: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::StyleSheetEditorDialog::slotAddGradient(const QString
    &property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html

    Parameters
    ----------

    property : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::StyleSheetEditorDialog::slotAddGradient(const
    #      QString &property)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialog15slotAddGrad'
        'ientERK7QString',
        property,
    )

  @overload(str)
  def slotAddColor(self, property: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::StyleSheetEditorDialog::slotAddColor(const QString
    &property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html

    Parameters
    ----------

    property : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::StyleSheetEditorDialog::slotAddColor(const
    #      QString &property)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialog12slotAddColo'
        'rERK7QString',
        property,
    )

  def slotAddFont(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::StyleSheetEditorDialog::slotAddFont()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html
    """
    #  void qdesigner_internal::StyleSheetEditorDialog::slotAddFont()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialog11slotAddFont'
        'Ev',
    )

  def slotRequestHelp(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::StyleSheetEditorDialog::slotRequestHelp()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html
    """
    #  void qdesigner_internal::StyleSheetEditorDialog::slotRequestHelp()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialog15slotRequest'
        'HelpEv',
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::StyleSheetEditorDialog::keyPressEvent(QKeyEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::StyleSheetEditorDialog::keyPressEvent(
    #      QKeyEvent *a0)
    ritual = (
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialog13keyPressEve'
        'ntEP9QKeyEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal22StyleSheetEditorDialog13keyPr'
          'essEventEP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(str, str)
  def insertCssProperty(self, name: str, value: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::StyleSheetEditorDialog::insertCssProperty(const
    QString &name, const QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-stylesheeteditordialog.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::StyleSheetEditorDialog::insertCssProperty(
    #      const QString &name, const QString &value)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22StyleSheetEditorDialog17insertCssPr'
        'opertyERK7QStringS3_',
        name, value,
    )

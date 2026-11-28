"""
qdesigner_internal::CodeDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/codedialog_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::CodeDialog to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QDialog, QWidget
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QString
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CodeDialog(QDialog):
  """
  The cute side of Qt's qdesigner_internal::CodeDialog: a plain Python object
  standing in front of one C++ qdesigner_internal::CodeDialog.

  It is built on the cute 'QDialog', as Qt's qdesigner_internal::CodeDialog
  is built on Qt's QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::CodeDialog that has a ritual and
  that Python can call so far, 12 names in all: 'metaObject', 'tr',
  'generateCode', 'showCodeDialog', 'slotSaveAs', 'copyAll', 'setCode',
  'code', 'setFormFileName', 'formFileName', 'setMimeType', 'warning'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::CodeDialog::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::CodeDialog::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'qdesigner_internal::CodeDialog::~CodeDialog()': the destructor:
    Python never removes a C++ qdesigner_internal::CodeDialog.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::CodeDialog is created at the first use, not
    by 'qdesigner_internal::CodeDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::CodeDialog.
  - Qt tells when it has removed the C++ qdesigner_internal::CodeDialog.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString qdesigner_internal::CodeDialog::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-codedialog.html#tr

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
    #  QString qdesigner_internal::CodeDialog::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal10CodeDialog2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(
      QDesignerFormWindowInterface, qdesigner_internal.UicLanguage, QString,
      QString,
  )
  @overload(
      QDesignerFormWindowInterface, qdesigner_internal.UicLanguage, QString,
      NoneType,
  )
  @overload(
      QDesignerFormWindowInterface, qdesigner_internal.UicLanguage, NoneType,
      QString,
  )
  @overload(
      QDesignerFormWindowInterface, qdesigner_internal.UicLanguage, NoneType,
      NoneType,
  )
  @overload(NoneType, qdesigner_internal.UicLanguage, QString, QString)
  @overload(NoneType, qdesigner_internal.UicLanguage, QString, NoneType)
  @overload(NoneType, qdesigner_internal.UicLanguage, NoneType, QString)
  @overload(NoneType, qdesigner_internal.UicLanguage, NoneType, NoneType)
  def generateCode(
      fw: Optional[QDesignerFormWindowInterface],
      language: qdesigner_internal.UicLanguage,
      code: Optional[QString],
      errorMessage: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::CodeDialog::generateCode(const
    QDesignerFormWindowInterface *fw, UicLanguage language, QString *code,
    QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-codedialog.html#generateCode

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    language : qdesigner_internal.UicLanguage
      Passed on as its number.

    code : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::CodeDialog::generateCode(const
    #      QDesignerFormWindowInterface *fw, UicLanguage language, QString
    #      *code, QString *errorMessage)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal10CodeDialog12generateCodeEPK28QDesig'
        'nerFormWindowInterfaceNS_11UicLanguageEP7QStringS6_',
        CuteMixin._addressOf(fw), language.value, CuteMixin._addressOf(code),
        CuteMixin._addressOf(errorMessage),
    )

  @staticmethod
  @overload(
      QDesignerFormWindowInterface, qdesigner_internal.UicLanguage, QWidget,
      QString,
  )
  @overload(
      QDesignerFormWindowInterface, qdesigner_internal.UicLanguage, QWidget,
      NoneType,
  )
  @overload(
      QDesignerFormWindowInterface, qdesigner_internal.UicLanguage, NoneType,
      QString,
  )
  @overload(
      QDesignerFormWindowInterface, qdesigner_internal.UicLanguage, NoneType,
      NoneType,
  )
  @overload(NoneType, qdesigner_internal.UicLanguage, QWidget, QString)
  @overload(NoneType, qdesigner_internal.UicLanguage, QWidget, NoneType)
  @overload(NoneType, qdesigner_internal.UicLanguage, NoneType, QString)
  @overload(NoneType, qdesigner_internal.UicLanguage, NoneType, NoneType)
  def showCodeDialog(
      fw: Optional[QDesignerFormWindowInterface],
      language: qdesigner_internal.UicLanguage,
      parent: Optional[QWidget],
      errorMessage: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::CodeDialog::showCodeDialog(const
    QDesignerFormWindowInterface *fw, UicLanguage language, QWidget *parent,
    QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-codedialog.html#showCodeDialog

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    language : qdesigner_internal.UicLanguage
      Passed on as its number.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::CodeDialog::showCodeDialog(const
    #      QDesignerFormWindowInterface *fw, UicLanguage language, QWidget
    #      *parent, QString *errorMessage)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal10CodeDialog14showCodeDialogEPK28QDes'
        'ignerFormWindowInterfaceNS_11UicLanguageEP7QWidgetP7QString',
        CuteMixin._addressOf(fw), language.value,
        CuteMixin._addressOf(parent), CuteMixin._addressOf(errorMessage),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::CodeDialog'

  #  A C++ qdesigner_internal::CodeDialog Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_CodeDialog'

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
    *qdesigner_internal::CodeDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-codedialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::CodeDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10CodeDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def code(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::CodeDialog::code() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-codedialog.html#code

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::CodeDialog::code() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10CodeDialog4codeEv',
    )

  def formFileName(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::CodeDialog::formFileName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-codedialog.html#formFileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::CodeDialog::formFileName() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10CodeDialog12formFileNameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setCode(self, code: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::CodeDialog::setCode(const QString
    &code)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-codedialog.html#setCode

    Parameters
    ----------

    code : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::CodeDialog::setCode(const QString &code)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10CodeDialog7setCodeERK7QString', code,
    )

  @overload(str)
  def setFormFileName(self, f: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::CodeDialog::setFormFileName(const
    QString &f)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-codedialog.html#setFormFileName

    Parameters
    ----------

    f : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::CodeDialog::setFormFileName(const QString &f)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10CodeDialog15setFormFileNameERK7QStr'
        'ing',
        f,
    )

  @overload(str)
  def setMimeType(self, m: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::CodeDialog::setMimeType(const
    QString &m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-codedialog.html#setMimeType

    Parameters
    ----------

    m : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::CodeDialog::setMimeType(const QString &m)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10CodeDialog11setMimeTypeERK7QString',
        m,
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
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::CodeDialog::CodeDialog(QWidget *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-codedialog.html#CodeDialog

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::CodeDialog::CodeDialog(QWidget *parent)
    self._noteCreation(CodeDialog, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal10CodeDialogC1EP7QWidget',
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

  def slotSaveAs(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::CodeDialog::slotSaveAs()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-codedialog.html#slotSaveAs
    """
    #  void qdesigner_internal::CodeDialog::slotSaveAs()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10CodeDialog10slotSaveAsEv',
    )

  def copyAll(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::CodeDialog::copyAll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-codedialog.html#copyAll
    """
    #  void qdesigner_internal::CodeDialog::copyAll()
    self.uglySide.call('ritual_ZN18qdesigner_internal10CodeDialog7copyAllEv')

  @overload(str)
  def warning(self, msg: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::CodeDialog::warning(const QString
    &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-codedialog.html#warning

    Parameters
    ----------

    msg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::CodeDialog::warning(const QString &msg)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10CodeDialog7warningERK7QString', msg,
    )

"""
qdesigner_internal::LanguageResourceDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/iconselector_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::LanguageResourceDialog to be private: it
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
  from . import QDesignerFormEditorInterface
  from . import QDesignerResourceBrowserInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QDesignerResourceBrowserInterface = WAIT['QDesignerResourceBrowserInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LanguageResourceDialog(QDialog):
  """
  The cute side of Qt's qdesigner_internal::LanguageResourceDialog: a plain
  Python object standing in front of one C++
  qdesigner_internal::LanguageResourceDialog.

  It is built on the cute 'QDialog', as Qt's
  qdesigner_internal::LanguageResourceDialog is built on Qt's QDialog, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::LanguageResourceDialog that has
  a ritual and that Python can call so far, 5 names in all: 'metaObject',
  'tr', 'create', 'setCurrentPath', 'currentPath'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::LanguageResourceDialog::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::LanguageResourceDialog::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'qdesigner_internal::LanguageResourceDialog::~LanguageResourceDialog()':
    the destructor: Python never removes a C++
    qdesigner_internal::LanguageResourceDialog.

  What has no ritual
  ------------------

  8 of the 17 functions Qt declares: 4 forbidden; 2 not a gap; 2 the compiler
  refuses its ritual as it would be written here.

  What to expect
  --------------

  - The C++ qdesigner_internal::LanguageResourceDialog is created at the
    first use, not by 'qdesigner_internal::LanguageResourceDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::LanguageResourceDialog.
  - Qt tells when it has removed the C++
    qdesigner_internal::LanguageResourceDialog. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString qdesigner_internal::LanguageResourceDialog::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-languageresourcedialog.html#tr

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
    #  QString qdesigner_internal::LanguageResourceDialog::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal22LanguageResourceDialog2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QDesignerFormEditorInterface, QWidget)
  @overload(QDesignerFormEditorInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def create(
      core: Optional[QDesignerFormEditorInterface],
      parent: Optional[QWidget],
  ) -> Optional[LanguageResourceDialog]:
    """
    Calls Qt's 'LanguageResourceDialog
    *qdesigner_internal::LanguageResourceDialog::create(
    QDesignerFormEditorInterface *core, QWidget *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-languageresourcedialog.html

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[LanguageResourceDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  LanguageResourceDialog
    #      *qdesigner_internal::LanguageResourceDialog::create(
    #      QDesignerFormEditorInterface *core, QWidget *parent)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal22LanguageResourceDialog6createEP28QD'
        'esignerFormEditorInterfaceP7QWidget',
        CuteMixin._addressOf(core), CuteMixin._addressOf(parent),
    )
    return LanguageResourceDialog._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::LanguageResourceDialog'

  #  A C++ qdesigner_internal::LanguageResourceDialog Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_LanguageResourceDialog'

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
    *qdesigner_internal::LanguageResourceDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-languageresourcedialog.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::LanguageResourceDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22LanguageResourceDialog10metaObject'
        'Ev',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentPath(self) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::LanguageResourceDialog::currentPath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-languageresourcedialog.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::LanguageResourceDialog::currentPath()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22LanguageResourceDialog11currentPat'
        'hEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setCurrentPath(self, filePath: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::LanguageResourceDialog::setCurrentPath(const QString
    &filePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-languageresourcedialog.html

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::LanguageResourceDialog::setCurrentPath(const
    #      QString &filePath)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22LanguageResourceDialog14setCurrentP'
        'athERK7QString',
        filePath,
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

  @overload(QDesignerResourceBrowserInterface)
  @overload(NoneType)
  @overload(QDesignerResourceBrowserInterface, QWidget)
  @overload(QDesignerResourceBrowserInterface, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      rb: Optional[QDesignerResourceBrowserInterface],
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::LanguageResourceDialog::LanguageResourceDialog(
    QDesignerResourceBrowserInterface *rb, QWidget *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-languageresourcedialog.html

    Parameters
    ----------

    rb : Optional[QDesignerResourceBrowserInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::LanguageResourceDialog::
    #      LanguageResourceDialog(QDesignerResourceBrowserInterface *rb,
    #      QWidget *parent)
    self._noteCreation(LanguageResourceDialog, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal22LanguageResourceDialogC1EP33QDesign'
        'erResourceBrowserInterfaceP7QWidget',
        self._addressOf(rb), self._addressOf(parent),
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

"""
QtResourceViewDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qtresourceview_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QtResourceViewDialog to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QtResourceViewDialog(QDialog):
  """
  The cute side of Qt's QtResourceViewDialog: a plain Python object standing
  in front of one C++ QtResourceViewDialog.

  It is built on the cute 'QDialog', as Qt's QtResourceViewDialog is built on
  Qt's QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtResourceViewDialog that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr',
  'selectedResource', 'selectResource', 'isResourceEditingEnabled',
  'setResourceEditingEnabled'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QtResourceViewDialog::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QtResourceViewDialog::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QtResourceViewDialog::~QtResourceViewDialog()': the destructor:
    Python never removes a C++ QtResourceViewDialog.
  - Qt's 'QtResourceViewDialogPrivate *QtResourceViewDialog::d_func()': gives
    'QtResourceViewDialogPrivate', which has no cute class yet.
  - Qt's 'const QtResourceViewDialogPrivate *QtResourceViewDialog::d_func()
    const': gives 'QtResourceViewDialogPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  6 of the 18 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QtResourceViewDialog is created at the first use, not by
    'QtResourceViewDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtResourceViewDialog.
  - Qt tells when it has removed the C++ QtResourceViewDialog. Every call on
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
    Calls Qt's 'QString QtResourceViewDialog::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtresourceviewdialog.html#tr

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
    #  QString QtResourceViewDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QtResourceViewDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtResourceViewDialog'

  #  A C++ QtResourceViewDialog Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtResourceViewDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QtResourceViewDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceviewdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QtResourceViewDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QtResourceViewDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def selectedResource(self) -> str:
    """
    Calls Qt's 'QString QtResourceViewDialog::selectedResource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceviewdialog.html#selectedResource

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QtResourceViewDialog::selectedResource() const
    return self.uglySide.call(
        'ritual_ZNK20QtResourceViewDialog16selectedResourceEv',
    )

  def isResourceEditingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QtResourceViewDialog::isResourceEditingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceviewdialog.html#isResourceEditingEnabled
    """
    #  bool QtResourceViewDialog::isResourceEditingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK20QtResourceViewDialog24isResourceEditingEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setResourceEditingEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QtResourceViewDialog::setResourceEditingEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceviewdialog.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QtResourceViewDialog::setResourceEditingEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN20QtResourceViewDialog25setResourceEditingEnabledEb',
        enable,
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
    'QtResourceViewDialog::QtResourceViewDialog(QDesignerFormEditorInterface
    *core, QWidget *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceviewdialog.html#QtResourceViewDialog

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QtResourceViewDialog::QtResourceViewDialog(
    #      QDesignerFormEditorInterface *core, QWidget *parent)
    self._noteCreation(QtResourceViewDialog, lambda: Rituals.call(
        'ritual_ZN20QtResourceViewDialogC1EP28QDesignerFormEditorInterfaceP'
        '7QWidget',
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

  @overload(str)
  def selectResource(self, path: str) -> None:
    """
    Calls Qt's 'void QtResourceViewDialog::selectResource(const QString
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtresourceviewdialog.html#selectResource

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QtResourceViewDialog::selectResource(const QString &path)
    self.uglySide.call(
        'ritual_ZN20QtResourceViewDialog14selectResourceERK7QString', path,
    )

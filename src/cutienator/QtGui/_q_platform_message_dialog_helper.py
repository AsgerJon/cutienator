"""
QPlatformMessageDialogHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from . import QPlatformDialogHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformMessageDialogHelper(QPlatformDialogHelper):
  """
  The cute side of Qt's QPlatformMessageDialogHelper: a plain Python object
  standing in front of one C++ QPlatformMessageDialogHelper.

  It is built on the cute 'QPlatformDialogHelper', as Qt's
  QPlatformMessageDialogHelper is built on Qt's QPlatformDialogHelper, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformMessageDialogHelper that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr', 'clicked',
  'checkBoxStateChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformMessageDialogHelper::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QPlatformMessageDialogHelper::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QSharedPointer<QMessageDialogOptions>
    &QPlatformMessageDialogHelper::options() const': gives a type Python has
    no way to take yet.
  - Qt's 'void QPlatformMessageDialogHelper::setOptions(const
    QSharedPointer<QMessageDialogOptions> &options)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformMessageDialogHelper is created at the first use, not by
    'QPlatformMessageDialogHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformMessageDialogHelper.
  - Qt tells when it has removed the C++ QPlatformMessageDialogHelper. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformMessageDialogHelper that has no cute function
    yet, 'options', 'setOptions', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QPlatformMessageDialogHelper::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmessagedialoghelper.html#tr

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
    #  QString QPlatformMessageDialogHelper::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QPlatformMessageDialogHelper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformMessageDialogHelper'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPlatformMessageDialogHelper::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmessagedialoghelper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformMessageDialogHelper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QPlatformMessageDialogHelper10metaObjectEv',
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

  @overload(
      QPlatformDialogHelper.StandardButton, QPlatformDialogHelper.ButtonRole,
  )
  def clicked(
      self,
      button: QPlatformDialogHelper.StandardButton,
      role: QPlatformDialogHelper.ButtonRole,
  ) -> None:
    """
    Calls Qt's 'void
    QPlatformMessageDialogHelper::clicked(QPlatformDialogHelper::
    StandardButton button, QPlatformDialogHelper::ButtonRole role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmessagedialoghelper.html#clicked

    Parameters
    ----------

    button : QPlatformDialogHelper.StandardButton
      Passed on as its number.

    role : QPlatformDialogHelper.ButtonRole
      Passed on as its number.
    """
    #  void QPlatformMessageDialogHelper::clicked(QPlatformDialogHelper::
    #      StandardButton button, QPlatformDialogHelper::ButtonRole role)
    self.uglySide.call(
        'ritual_ZN28QPlatformMessageDialogHelper7clickedEN21QPlatformDialog'
        'Helper14StandardButtonENS0_10ButtonRoleE',
        button.value, role.value,
    )

  @overload(Qt.CheckState)
  def checkBoxStateChanged(self, state: Qt.CheckState) -> None:
    """
    Calls Qt's 'void
    QPlatformMessageDialogHelper::checkBoxStateChanged(Qt::CheckState
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformmessagedialoghelper.html

    Parameters
    ----------

    state : Qt.CheckState
      Passed on as its number.
    """
    #  void QPlatformMessageDialogHelper::checkBoxStateChanged(Qt::CheckState
    #      state)
    self.uglySide.call(
        'ritual_ZN28QPlatformMessageDialogHelper20checkBoxStateChangedEN2Qt'
        '10CheckStateE',
        state.value,
    )

  @staticmethod
  def options(*__, **_) -> Never:
    """
    Qt's 'const QSharedPointer<QMessageDialogOptions>
    &QPlatformMessageDialogHelper::options() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformMessageDialogHelper.options' has no cute function yet. "
        "Qt's 'const QSharedPointer<QMessageDialogOptions> "
        "&QPlatformMessageDialogHelper::options() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void QPlatformMessageDialogHelper::setOptions(const
    QSharedPointer<QMessageDialogOptions> &options)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformMessageDialogHelper.setOptions' has no cute function "
        "yet. Qt's 'void QPlatformMessageDialogHelper::setOptions(const "
        "QSharedPointer<QMessageDialogOptions> &options)': takes a type "
        "Python has no way to hand over yet.")

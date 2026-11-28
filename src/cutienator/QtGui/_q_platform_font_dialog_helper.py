"""
QPlatformFontDialogHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QPlatformDialogHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformFontDialogHelper(QPlatformDialogHelper):
  """
  The cute side of Qt's QPlatformFontDialogHelper: a plain Python object
  standing in front of one C++ QPlatformFontDialogHelper.

  It is built on the cute 'QPlatformDialogHelper', as Qt's
  QPlatformFontDialogHelper is built on Qt's QPlatformDialogHelper, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformFontDialogHelper that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr',
  'setCurrentFont', 'currentFont', 'currentFontChanged', 'fontSelected'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformFontDialogHelper::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QPlatformFontDialogHelper::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QSharedPointer<QFontDialogOptions>
    &QPlatformFontDialogHelper::options() const': gives a type Python has no
    way to take yet.
  - Qt's 'void QPlatformFontDialogHelper::setOptions(const
    QSharedPointer<QFontDialogOptions> &options)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformFontDialogHelper is created at the first use, not by
    'QPlatformFontDialogHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformFontDialogHelper.
  - Qt tells when it has removed the C++ QPlatformFontDialogHelper. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformFontDialogHelper that has no cute function
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
    Calls Qt's 'QString QPlatformFontDialogHelper::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformfontdialoghelper.html#tr

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
    #  QString QPlatformFontDialogHelper::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QPlatformFontDialogHelper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformFontDialogHelper'

  #  The functions Qt calls itself that QPlatformFontDialogHelper is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setCurrentFont': (
          ('_ZN25QPlatformFontDialogHelper14setCurrentFontERK5QFont',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QFont'),
           )),
      ),
      'currentFont': (
          ('_ZNK25QPlatformFontDialogHelper11currentFontEv',
           ('address', 'value', 'QtGui:QFont'),
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
    Calls Qt's 'const QMetaObject *QPlatformFontDialogHelper::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdialoghelper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformFontDialogHelper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QPlatformFontDialogHelper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentFont(self) -> QFont:
    """
    Calls Qt's 'QFont QPlatformFontDialogHelper::currentFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdialoghelper.html#currentFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QPlatformFontDialogHelper::currentFont() const
    address = self.uglySide.call(
        'ritual_ZNK25QPlatformFontDialogHelper11currentFontEv',
    )
    from . import QFont
    return QFont._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setCurrentFont(self, a0: QFont) -> None:
    """
    Calls Qt's 'void QPlatformFontDialogHelper::setCurrentFont(const QFont
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdialoghelper.html#setCurrentFont

    Parameters
    ----------

    a0 : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QPlatformFontDialogHelper::setCurrentFont(const QFont &a0)
    self.uglySide.call(
        'ritual_ZN25QPlatformFontDialogHelper14setCurrentFontERK5QFont',
        self._valueOf(a0),
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

  @overload(QFont)
  def currentFontChanged(self, font: QFont) -> None:
    """
    Calls Qt's 'void QPlatformFontDialogHelper::currentFontChanged(const
    QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdialoghelper.html#currentFontChanged

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QPlatformFontDialogHelper::currentFontChanged(const QFont &font)
    self.uglySide.call(
        'ritual_ZN25QPlatformFontDialogHelper18currentFontChangedERK5QFont',
        self._valueOf(font),
    )

  @overload(QFont)
  def fontSelected(self, font: QFont) -> None:
    """
    Calls Qt's 'void QPlatformFontDialogHelper::fontSelected(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformfontdialoghelper.html#fontSelected

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QPlatformFontDialogHelper::fontSelected(const QFont &font)
    self.uglySide.call(
        'ritual_ZN25QPlatformFontDialogHelper12fontSelectedERK5QFont',
        self._valueOf(font),
    )

  @staticmethod
  def options(*__, **_) -> Never:
    """
    Qt's 'const QSharedPointer<QFontDialogOptions>
    &QPlatformFontDialogHelper::options() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformFontDialogHelper.options' has no cute function yet. Qt's "
        "'const QSharedPointer<QFontDialogOptions> "
        "&QPlatformFontDialogHelper::options() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void QPlatformFontDialogHelper::setOptions(const
    QSharedPointer<QFontDialogOptions> &options)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformFontDialogHelper.setOptions' has no cute function yet. "
        "Qt's 'void QPlatformFontDialogHelper::setOptions(const "
        "QSharedPointer<QFontDialogOptions> &options)': takes a type Python "
        "has no way to hand over yet.")

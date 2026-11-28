"""
QPlatformColorDialogHelper binding of the Qt C++
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
  from . import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformColorDialogHelper(QPlatformDialogHelper):
  """
  The cute side of Qt's QPlatformColorDialogHelper: a plain Python object
  standing in front of one C++ QPlatformColorDialogHelper.

  It is built on the cute 'QPlatformDialogHelper', as Qt's
  QPlatformColorDialogHelper is built on Qt's QPlatformDialogHelper, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformColorDialogHelper that has a ritual and
  that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'setCurrentColor', 'currentColor', 'currentColorChanged', 'colorSelected'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformColorDialogHelper::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QPlatformColorDialogHelper::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QSharedPointer<QColorDialogOptions>
    &QPlatformColorDialogHelper::options() const': gives a type Python has no
    way to take yet.
  - Qt's 'void QPlatformColorDialogHelper::setOptions(const
    QSharedPointer<QColorDialogOptions> &options)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformColorDialogHelper is created at the first use, not by
    'QPlatformColorDialogHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformColorDialogHelper.
  - Qt tells when it has removed the C++ QPlatformColorDialogHelper. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformColorDialogHelper that has no cute function
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
    Calls Qt's 'QString QPlatformColorDialogHelper::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformcolordialoghelper.html#tr

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
    #  QString QPlatformColorDialogHelper::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QPlatformColorDialogHelper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformColorDialogHelper'

  #  The functions Qt calls itself that QPlatformColorDialogHelper is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setCurrentColor': (
          ('_ZN26QPlatformColorDialogHelper15setCurrentColorERK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'currentColor': (
          ('_ZNK26QPlatformColorDialogHelper12currentColorEv',
           ('address', 'value', 'QtGui:QColor'),
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
    Calls Qt's 'const QMetaObject *QPlatformColorDialogHelper::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformcolordialoghelper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformColorDialogHelper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QPlatformColorDialogHelper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentColor(self) -> QColor:
    """
    Calls Qt's 'QColor QPlatformColorDialogHelper::currentColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformcolordialoghelper.html#currentColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QPlatformColorDialogHelper::currentColor() const
    address = self.uglySide.call(
        'ritual_ZNK26QPlatformColorDialogHelper12currentColorEv',
    )
    from . import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setCurrentColor(self, a0: QColor) -> None:
    """
    Calls Qt's 'void QPlatformColorDialogHelper::setCurrentColor(const QColor
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformcolordialoghelper.html#setCurrentColor

    Parameters
    ----------

    a0 : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPlatformColorDialogHelper::setCurrentColor(const QColor &a0)
    self.uglySide.call(
        'ritual_ZN26QPlatformColorDialogHelper15setCurrentColorERK6QColor',
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

  @overload(QColor)
  def currentColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QPlatformColorDialogHelper::currentColorChanged(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformcolordialoghelper.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPlatformColorDialogHelper::currentColorChanged(const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN26QPlatformColorDialogHelper19currentColorChangedERK6QCol'
        'or',
        self._valueOf(color),
    )

  @overload(QColor)
  def colorSelected(self, color: QColor) -> None:
    """
    Calls Qt's 'void QPlatformColorDialogHelper::colorSelected(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformcolordialoghelper.html#colorSelected

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPlatformColorDialogHelper::colorSelected(const QColor &color)
    self.uglySide.call(
        'ritual_ZN26QPlatformColorDialogHelper13colorSelectedERK6QColor',
        self._valueOf(color),
    )

  @staticmethod
  def options(*__, **_) -> Never:
    """
    Qt's 'const QSharedPointer<QColorDialogOptions>
    &QPlatformColorDialogHelper::options() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformColorDialogHelper.options' has no cute function yet. "
        "Qt's 'const QSharedPointer<QColorDialogOptions> "
        "&QPlatformColorDialogHelper::options() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void QPlatformColorDialogHelper::setOptions(const
    QSharedPointer<QColorDialogOptions> &options)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformColorDialogHelper.setOptions' has no cute function yet. "
        "Qt's 'void QPlatformColorDialogHelper::setOptions(const "
        "QSharedPointer<QColorDialogOptions> &options)': takes a type "
        "Python has no way to hand over yet.")

"""
QQStyleKitTheme binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekittheme_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitTheme to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QQStyleKitStyleAndThemeBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QPalette
  from . import QQStyleKitStyle


class QQStyleKitTheme(QQStyleKitStyleAndThemeBase):
  """
  The cute side of Qt's QQStyleKitTheme: a plain Python object standing in
  front of one C++ QQStyleKitTheme.

  It is built on the cute 'QQStyleKitStyleAndThemeBase', as Qt's
  QQStyleKitTheme is built on Qt's QQStyleKitStyleAndThemeBase, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitTheme that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'style',
  'paletteForControlType', 'componentComplete', 'updateThemeFonts'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitTheme::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQStyleKitTheme::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  8 of the 15 functions Qt declares: 2 not a gap; 2 forbidden; 1 Qt's library
  has no name for it, and its code in Qt's source does not compile apart from
  its file; 1 leans on 'QQStyleKitTheme; 1 leans on 'vtable for
  QQStyleKitFont', which Qt's source does not mark for use from outside Qt
  and has no code for that could be taken; 1 leans on 'QQStyleKitPalette.

  What to expect
  --------------

  - The C++ QQStyleKitTheme is created at the first use, not by
    'QQStyleKitTheme(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitTheme.
  - Qt tells when it has removed the C++ QQStyleKitTheme. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitTheme that has no cute function yet,
    '__init__', 'fontForControlType', 'updateThemePalettes', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitTheme'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitTheme::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekittheme.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitTheme::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQStyleKitTheme10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def style(self) -> Optional[QQStyleKitStyle]:
    """
    Calls Qt's 'QQStyleKitStyle *QQStyleKitTheme::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqstylekittheme.html#style

    Returns
    -------

    Optional[QQStyleKitStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitStyle *QQStyleKitTheme::style() const
    address = self.uglySide.call('ritual_ZNK15QQStyleKitTheme5styleEv')
    from . import QQStyleKitStyle
    return QQStyleKitStyle._cuteAt(address)

  @overload(int)
  def paletteForControlType(self, type: int) -> QPalette:
    """
    Calls Qt's 'QPalette
    QQStyleKitTheme::paletteForControlType(QQStyleKitExtendableControlType
    type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittheme.html#paletteForControlType

    Parameters
    ----------

    type : int
      Passed on as it is.

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQStyleKitTheme::paletteForControlType(
    #      QQStyleKitExtendableControlType type) const
    address = self.uglySide.call(
        'ritual_ZNK15QQStyleKitTheme21paletteForControlTypeEj', type,
    )
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitTheme::QQStyleKitTheme(QObject *parent)': leans on
    'vtable for QQStyleKitFont', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTheme.__init__' has no cute function yet. Qt's "
        "'QQStyleKitTheme::QQStyleKitTheme(QObject *parent)': leans on "
        "'vtable for QQStyleKitFont', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTheme::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittheme.html#componentComplete
    """
    #  void QQStyleKitTheme::componentComplete()
    self.uglySide.call('ritual_ZN15QQStyleKitTheme17componentCompleteEv')

  def updateThemeFonts(self) -> None:
    """
    Calls Qt's 'void QQStyleKitTheme::updateThemeFonts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekittheme.html#updateThemeFonts
    """
    #  void QQStyleKitTheme::updateThemeFonts()
    self.uglySide.call('ritual_ZN15QQStyleKitTheme16updateThemeFontsEv')

  @staticmethod
  def fontForControlType(*__, **_) -> Never:
    """
    Qt's 'QFont
    QQStyleKitTheme::fontForControlType(QQStyleKitExtendableControlType type)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'scopeForType'.
    """
    raise NotImplementedError(
        "'QQStyleKitTheme.fontForControlType' has no cute function yet. "
        "Qt's 'QFont "
        "QQStyleKitTheme::fontForControlType(QQStyleKitExtendableControlType"
        " type) const': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'scopeForType'.")

  @staticmethod
  def updateThemePalettes(*__, **_) -> Never:
    """
    Qt's 'void QQStyleKitTheme::updateThemePalettes()': leans on
    'QQStyleKitPalette::labelChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitTheme.updateThemePalettes' has no cute function yet. "
        "Qt's 'void QQStyleKitTheme::updateThemePalettes()': leans on "
        "'QQStyleKitPalette::labelChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

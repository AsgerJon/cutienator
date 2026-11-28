"""
QQStyleKitStyleAndThemeBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitstyleandthemebase_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitStyleAndThemeBase to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QQStyleKitControls

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQStyleKitFont, QQStyleKitPalette


class QQStyleKitStyleAndThemeBase(QQStyleKitControls):
  """
  The cute side of Qt's QQStyleKitStyleAndThemeBase: a plain Python object
  standing in front of one C++ QQStyleKitStyleAndThemeBase.

  It is built on the cute 'QQStyleKitControls', as Qt's
  QQStyleKitStyleAndThemeBase is built on Qt's QQStyleKitControls, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitStyleAndThemeBase that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'fonts',
  'palettes', 'fontsChanged', 'palettesChanged'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitStyleAndThemeBase::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQStyleKitStyleAndThemeBase::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQStyleKitStyleAndThemeBase::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 14 functions Qt declares: 2 not a gap; 2 forbidden; 1 leans on
  'QQStyleKitStyleAndThemeBase; 1 leans on 'vtable for QQStyleKitFont', which
  Qt's source does not mark for use from outside Qt and has no code for that
  could be taken.

  What to expect
  --------------

  - The C++ QQStyleKitStyleAndThemeBase is created at the first use, not by
    'QQStyleKitStyleAndThemeBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitStyleAndThemeBase.
  - Qt tells when it has removed the C++ QQStyleKitStyleAndThemeBase. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitStyleAndThemeBase that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitStyleAndThemeBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitStyleAndThemeBase::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyleandthemebase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitStyleAndThemeBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitStyleAndThemeBase10metaObjectEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitStyleAndThemeBase::QQStyleKitStyleAndThemeBase(QObject
    *parent)': leans on 'vtable for QQStyleKitFont', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQStyleKitStyleAndThemeBase.__init__' has no cute function yet. "
        "Qt's "
        "'QQStyleKitStyleAndThemeBase::QQStyleKitStyleAndThemeBase(QObject "
        "*parent)': leans on 'vtable for QQStyleKitFont', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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

  def fonts(self) -> Optional[QQStyleKitFont]:
    """
    Calls Qt's 'QQStyleKitFont *QQStyleKitStyleAndThemeBase::fonts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyleandthemebase.html#fonts

    Returns
    -------

    Optional[QQStyleKitFont]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitFont *QQStyleKitStyleAndThemeBase::fonts()
    address = self.uglySide.call(
        'ritual_ZN27QQStyleKitStyleAndThemeBase5fontsEv',
    )
    from . import QQStyleKitFont
    return QQStyleKitFont._cuteAt(address)

  def palettes(self) -> Optional[QQStyleKitPalette]:
    """
    Calls Qt's 'QQStyleKitPalette *QQStyleKitStyleAndThemeBase::palettes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyleandthemebase.html#palettes

    Returns
    -------

    Optional[QQStyleKitPalette]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitPalette *QQStyleKitStyleAndThemeBase::palettes()
    address = self.uglySide.call(
        'ritual_ZN27QQStyleKitStyleAndThemeBase8palettesEv',
    )
    from . import QQStyleKitPalette
    return QQStyleKitPalette._cuteAt(address)

  def fontsChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyleAndThemeBase::fontsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyleandthemebase.html#fontsChanged
    """
    #  void QQStyleKitStyleAndThemeBase::fontsChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitStyleAndThemeBase12fontsChangedEv',
    )

  def palettesChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitStyleAndThemeBase::palettesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitstyleandthemebase.html#palettesChanged
    """
    #  void QQStyleKitStyleAndThemeBase::palettesChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitStyleAndThemeBase15palettesChangedEv',
    )

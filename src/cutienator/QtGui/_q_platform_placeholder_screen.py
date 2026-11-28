"""
QPlatformPlaceholderScreen binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformscreen.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QList
from . import QImage, QPlatformScreen

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRect


class QPlatformPlaceholderScreen(QPlatformScreen):
  """
  The cute side of Qt's QPlatformPlaceholderScreen: a plain Python object
  standing in front of one C++ QPlatformPlaceholderScreen.

  It is built on the cute 'QPlatformScreen', as Qt's
  QPlatformPlaceholderScreen is built on Qt's QPlatformScreen, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformPlaceholderScreen that has a ritual and
  that Python can call so far, 6 names in all: 'isPlaceholder', 'geometry',
  'availableGeometry', 'depth', 'format', 'virtualSiblings'. It can be made
  from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QPlatformPlaceholderScreen is created at the first use, not by
    'QPlatformPlaceholderScreen(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformPlaceholderScreen.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformPlaceholderScreen'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isPlaceholder(self) -> bool:
    """
    Calls Qt's 'bool QPlatformPlaceholderScreen::isPlaceholder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformplaceholderscreen.html#isPlaceholder
    """
    #  bool QPlatformPlaceholderScreen::isPlaceholder() const
    ritual = 'ritual_ZNK26QPlatformPlaceholderScreen13isPlaceholderEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QPlatformPlaceholderScreen13isPlaceholderEv'
    return self.uglySide.call(ritual)

  def geometry(self) -> QRect:
    """
    Calls Qt's 'QRect QPlatformPlaceholderScreen::geometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformplaceholderscreen.html#geometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlatformPlaceholderScreen::geometry() const
    ritual = 'ritual_ZNK26QPlatformPlaceholderScreen8geometryEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QPlatformPlaceholderScreen8geometryEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def availableGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QPlatformPlaceholderScreen::availableGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformplaceholderscreen.html#availableGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPlatformPlaceholderScreen::availableGeometry() const
    ritual = 'ritual_ZNK26QPlatformPlaceholderScreen17availableGeometryEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QPlatformPlaceholderScreen17availableGeometryEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def depth(self) -> int:
    """
    Calls Qt's 'int QPlatformPlaceholderScreen::depth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformplaceholderscreen.html#depth
    """
    #  int QPlatformPlaceholderScreen::depth() const
    ritual = 'ritual_ZNK26QPlatformPlaceholderScreen5depthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QPlatformPlaceholderScreen5depthEv'
    return self.uglySide.call(ritual)

  def format(self) -> QImage.Format:
    """
    Calls Qt's 'QImage::Format QPlatformPlaceholderScreen::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformplaceholderscreen.html#format

    Returns
    -------

    QImage.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QImage.Format(number)'
      gives.
    """
    #  QImage::Format QPlatformPlaceholderScreen::format() const
    ritual = 'ritual_ZNK26QPlatformPlaceholderScreen6formatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QPlatformPlaceholderScreen6formatEv'
    return QImage.Format(self.uglySide.call(ritual))

  def virtualSiblings(self) -> QList[QPlatformScreen]:
    """
    Calls Qt's 'QList<QPlatformScreen *>
    QPlatformPlaceholderScreen::virtualSiblings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformplaceholderscreen.html#virtualSiblings

    Returns
    -------

    QList[QPlatformScreen]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPlatformScreen *> QPlatformPlaceholderScreen::virtualSiblings()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QPlatformPlaceholderScreen15virtualSiblingsEv',
    )
    return QList[QPlatformScreen]._cuteOwning(address)

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

  @overload()
  @overload(bool)
  def __init__(self, virtualSibling: bool = True) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformPlaceholderScreen::QPlatformPlaceholderScreen(bool
    virtualSibling)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformplaceholderscreen.html

    Parameters
    ----------

    virtualSibling : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  QPlatformPlaceholderScreen::QPlatformPlaceholderScreen(bool
    #      virtualSibling)
    self._noteCreation(QPlatformPlaceholderScreen, lambda: Rituals.call(
        'ritual_ZN26QPlatformPlaceholderScreenC1Eb', virtualSibling,
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

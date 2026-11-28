"""
QQuickNativeIconLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicknativeiconloader_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickNativeIconLoader to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtQuick import QQuickPixmap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from ..QtGui import QIcon
  from . import QQuickIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickIcon = WAIT['QQuickIcon']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickNativeIconLoader(QQuickPixmap):
  """
  The cute side of Qt's QQuickNativeIconLoader: a plain Python object
  standing in front of one C++ QQuickNativeIconLoader.

  It is built on the cute 'QQuickPixmap', as Qt's QQuickNativeIconLoader is
  built on Qt's QQuickPixmap, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickNativeIconLoader that has a ritual and that
  Python can call so far, 6 names in all: 'isEnabled', 'setEnabled',
  'toQIcon', 'icon', 'setIcon', 'loadIcon'. It can be made from Python, in 1
  way; see '__init__'.

  What to expect
  --------------

  - The C++ QQuickNativeIconLoader is created at the first use, not by
    'QQuickNativeIconLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickNativeIconLoader.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickNativeIconLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickNativeIconLoader::isEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativeiconloader.html#isEnabled
    """
    #  bool QQuickNativeIconLoader::isEnabled() const
    return self.uglySide.call(
        'ritual_ZNK22QQuickNativeIconLoader9isEnabledEv',
    )

  def toQIcon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QQuickNativeIconLoader::toQIcon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativeiconloader.html#toQIcon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QQuickNativeIconLoader::toQIcon() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickNativeIconLoader7toQIconEv',
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def icon(self) -> QQuickIcon:
    """
    Calls Qt's 'QQuickIcon QQuickNativeIconLoader::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicknativeiconloader.html#icon

    Returns
    -------

    QQuickIcon
      A new cute QQuickIcon around the copy Qt gave back. Python owns it.
    """
    #  QQuickIcon QQuickNativeIconLoader::icon() const
    address = self.uglySide.call('ritual_ZNK22QQuickNativeIconLoader4iconEv')
    from . import QQuickIcon
    return QQuickIcon._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickNativeIconLoader::setEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativeiconloader.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickNativeIconLoader::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN22QQuickNativeIconLoader10setEnabledEb', enabled,
    )

  @overload(QQuickIcon)
  def setIcon(self, icon: QQuickIcon) -> None:
    """
    Calls Qt's 'void QQuickNativeIconLoader::setIcon(const QQuickIcon
    &icon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativeiconloader.html#setIcon

    Parameters
    ----------

    icon : QQuickIcon
      Passed on as a value: Qt reads the C++ QQuickIcon, which stays Python's
      own.
    """
    #  void QQuickNativeIconLoader::setIcon(const QQuickIcon &icon)
    self.uglySide.call(
        'ritual_ZN22QQuickNativeIconLoader7setIconERK10QQuickIcon',
        self._valueOf(icon),
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

  @overload(int, QObject)
  @overload(int, NoneType)
  def __init__(self, slot: int, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickNativeIconLoader::QQuickNativeIconLoader(int slot, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativeiconloader.html#QQuickNativeIconLoader

    Parameters
    ----------

    slot : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickNativeIconLoader::QQuickNativeIconLoader(int slot, QObject
    #      *parent)
    self._noteCreation(QQuickNativeIconLoader, lambda: Rituals.call(
        'ritual_ZN22QQuickNativeIconLoaderC1EiP7QObject',
        slot, self._addressOf(parent, 'QObject'),
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

  def loadIcon(self) -> None:
    """
    Calls Qt's 'void QQuickNativeIconLoader::loadIcon()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicknativeiconloader.html#loadIcon
    """
    #  void QQuickNativeIconLoader::loadIcon()
    self.uglySide.call('ritual_ZN22QQuickNativeIconLoader8loadIconEv')

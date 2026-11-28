"""
QQuickLabsPlatformIconLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformiconloader_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformIconLoader to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickLabsPlatformIcon
  from ..QtCore import QObject
  from ..QtGui import QIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickLabsPlatformIcon = WAIT['QQuickLabsPlatformIcon']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLabsPlatformIconLoader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickLabsPlatformIconLoader: a plain Python object
  standing in front of one C++ QQuickLabsPlatformIconLoader.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformIconLoader that has a ritual and
  that Python can call so far, 6 names in all: 'isEnabled', 'setEnabled',
  'toQIcon', 'icon', 'setIcon', 'loadIcon'. It can be made from Python, in 1
  way; see '__init__'.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformIconLoader is created at the first use, not by
    'QQuickLabsPlatformIconLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformIconLoader.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabsPlatformIconLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformIconLoader::isEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformiconloader.html#isEnabled
    """
    #  bool QQuickLabsPlatformIconLoader::isEnabled() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformIconLoader9isEnabledEv',
    )

  def toQIcon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QQuickLabsPlatformIconLoader::toQIcon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformiconloader.html#toQIcon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QQuickLabsPlatformIconLoader::toQIcon() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformIconLoader7toQIconEv',
    )
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def icon(self) -> QQuickLabsPlatformIcon:
    """
    Calls Qt's 'QQuickLabsPlatformIcon QQuickLabsPlatformIconLoader::icon()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformiconloader.html#icon

    Returns
    -------

    QQuickLabsPlatformIcon
      A new cute QQuickLabsPlatformIcon around the copy Qt gave back. Python
      owns it.
    """
    #  QQuickLabsPlatformIcon QQuickLabsPlatformIconLoader::icon() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformIconLoader4iconEv',
    )
    from . import QQuickLabsPlatformIcon
    return QQuickLabsPlatformIcon._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformIconLoader::setEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformiconloader.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickLabsPlatformIconLoader::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformIconLoader10setEnabledEb', enabled,
    )

  @overload(QQuickLabsPlatformIcon)
  def setIcon(self, icon: QQuickLabsPlatformIcon) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformIconLoader::setIcon(const
    QQuickLabsPlatformIcon &icon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformiconloader.html#setIcon

    Parameters
    ----------

    icon : QQuickLabsPlatformIcon
      Passed on as a value: Qt reads the C++ QQuickLabsPlatformIcon, which
      stays Python's own.
    """
    #  void QQuickLabsPlatformIconLoader::setIcon(const
    #      QQuickLabsPlatformIcon &icon)
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformIconLoader7setIconERK22QQuickLabsPlat'
        'formIcon',
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
    'QQuickLabsPlatformIconLoader::QQuickLabsPlatformIconLoader(int slot,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformiconloader.html

    Parameters
    ----------

    slot : int
      Passed on as it is.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickLabsPlatformIconLoader::QQuickLabsPlatformIconLoader(int slot,
    #      QObject *parent)
    self._noteCreation(QQuickLabsPlatformIconLoader, lambda: Rituals.call(
        'ritual_ZN28QQuickLabsPlatformIconLoaderC1EiP7QObject',
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
    Calls Qt's 'void QQuickLabsPlatformIconLoader::loadIcon()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformiconloader.html#loadIcon
    """
    #  void QQuickLabsPlatformIconLoader::loadIcon()
    self.uglySide.call('ritual_ZN28QQuickLabsPlatformIconLoader8loadIconEv')

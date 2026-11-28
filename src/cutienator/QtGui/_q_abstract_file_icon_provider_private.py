"""
QAbstractFileIconProviderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qabstractfileiconprovider_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractFileIconProviderPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QAbstractFileIconProvider

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QFileInfo
  from . import QIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileInfo = WAIT['QFileInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractFileIconProviderPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractFileIconProviderPrivate: a plain Python
  object standing in front of one C++ QAbstractFileIconProviderPrivate.

  What exists
  -----------

  Every function of Qt's QAbstractFileIconProviderPrivate that has a ritual
  and that Python can call so far, 5 names in all: 'q_func',
  'getPlatformThemeIcon', 'getIconThemeIcon', 'clearIconTypeCache',
  'getFileType'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractFileIconProvider
    *QAbstractFileIconProviderPrivate::q_func() const': takes in Python what
    'QAbstractFileIconProvider *QAbstractFileIconProviderPrivate::q_func()'
    takes.
  - Qt's
    'QAbstractFileIconProviderPrivate::~QAbstractFileIconProviderPrivate()':
    the destructor: Python never removes a C++
    QAbstractFileIconProviderPrivate.

  What to expect
  --------------

  - The C++ QAbstractFileIconProviderPrivate is created at the first use, not
    by 'QAbstractFileIconProviderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractFileIconProviderPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def clearIconTypeCache() -> None:
    """
    Calls Qt's 'void QAbstractFileIconProviderPrivate::clearIconTypeCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconproviderprivate.html
    """
    #  void QAbstractFileIconProviderPrivate::clearIconTypeCache()
    Rituals.call(
        'ritual_ZN32QAbstractFileIconProviderPrivate18clearIconTypeCacheEv',
    )

  @staticmethod
  @overload(QFileInfo)
  def getFileType(info: QFileInfo) -> str:
    """
    Calls Qt's 'QString QAbstractFileIconProviderPrivate::getFileType(const
    QFileInfo &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconproviderprivate.html#getFileType

    Parameters
    ----------

    info : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractFileIconProviderPrivate::getFileType(const QFileInfo
    #      &info)
    return Rituals.call(
        'ritual_ZN32QAbstractFileIconProviderPrivate11getFileTypeERK9QFileI'
        'nfo',
        CuteMixin._valueOf(info),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractFileIconProviderPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractFileIconProvider.IconType)
  def getPlatformThemeIcon(
      self,
      type: QAbstractFileIconProvider.IconType,
  ) -> QIcon:
    """
    Calls Qt's 'QIcon QAbstractFileIconProviderPrivate::getPlatformThemeIcon(
    QAbstractFileIconProvider::IconType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconproviderprivate.html

    Parameters
    ----------

    type : QAbstractFileIconProvider.IconType
      Passed on as its number.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QAbstractFileIconProviderPrivate::getPlatformThemeIcon(
    #      QAbstractFileIconProvider::IconType type) const
    address = self.uglySide.call(
        'ritual_ZNK32QAbstractFileIconProviderPrivate20getPlatformThemeIcon'
        'EN25QAbstractFileIconProvider8IconTypeE',
        type.value,
    )
    from . import QIcon
    return QIcon._cuteOwning(address)

  @overload(QFileInfo)
  def getPlatformThemeIcon(self, info: QFileInfo) -> QIcon:
    """
    Calls Qt's 'QIcon
    QAbstractFileIconProviderPrivate::getPlatformThemeIcon(const QFileInfo
    &info) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconproviderprivate.html

    Parameters
    ----------

    info : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QAbstractFileIconProviderPrivate::getPlatformThemeIcon(const
    #      QFileInfo &info) const
    address = self.uglySide.call(
        'ritual_ZNK32QAbstractFileIconProviderPrivate20getPlatformThemeIcon'
        'ERK9QFileInfo',
        self._valueOf(info),
    )
    from . import QIcon
    return QIcon._cuteOwning(address)

  @overload(QAbstractFileIconProvider.IconType)
  def getIconThemeIcon(
      self,
      type: QAbstractFileIconProvider.IconType,
  ) -> QIcon:
    """
    Calls Qt's 'QIcon QAbstractFileIconProviderPrivate::getIconThemeIcon(
    QAbstractFileIconProvider::IconType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconproviderprivate.html

    Parameters
    ----------

    type : QAbstractFileIconProvider.IconType
      Passed on as its number.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QAbstractFileIconProviderPrivate::getIconThemeIcon(
    #      QAbstractFileIconProvider::IconType type) const
    address = self.uglySide.call(
        'ritual_ZNK32QAbstractFileIconProviderPrivate16getIconThemeIconEN25'
        'QAbstractFileIconProvider8IconTypeE',
        type.value,
    )
    from . import QIcon
    return QIcon._cuteOwning(address)

  @overload(QFileInfo)
  def getIconThemeIcon(self, info: QFileInfo) -> QIcon:
    """
    Calls Qt's 'QIcon
    QAbstractFileIconProviderPrivate::getIconThemeIcon(const QFileInfo &info)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconproviderprivate.html

    Parameters
    ----------

    info : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QAbstractFileIconProviderPrivate::getIconThemeIcon(const
    #      QFileInfo &info) const
    address = self.uglySide.call(
        'ritual_ZNK32QAbstractFileIconProviderPrivate16getIconThemeIconERK9'
        'QFileInfo',
        self._valueOf(info),
    )
    from . import QIcon
    return QIcon._cuteOwning(address)

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

  @overload(QAbstractFileIconProvider)
  @overload(NoneType)
  def __init__(self, q: Optional[QAbstractFileIconProvider]) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractFileIconProviderPrivate::QAbstractFileIconProviderPrivate(
    QAbstractFileIconProvider *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconproviderprivate.html

    Parameters
    ----------

    q : Optional[QAbstractFileIconProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAbstractFileIconProviderPrivate::
    #      QAbstractFileIconProviderPrivate(QAbstractFileIconProvider *q)
    self._noteCreation(
        QAbstractFileIconProviderPrivate, lambda: Rituals.call(
            'ritual_ZN32QAbstractFileIconProviderPrivateC1EP25QAbstractFile'
            'IconProvider',
            self._addressOf(q),
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

  def q_func(self) -> Optional[QAbstractFileIconProvider]:
    """
    Calls Qt's 'QAbstractFileIconProvider
    *QAbstractFileIconProviderPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconproviderprivate.html#q_func

    Returns
    -------

    Optional[QAbstractFileIconProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractFileIconProvider *QAbstractFileIconProviderPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN32QAbstractFileIconProviderPrivate6q_funcEv',
    )
    return QAbstractFileIconProvider._cuteAt(address)

"""
QPlatformIntegrationFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformintegrationfactory_p.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPlatformIntegration


class QPlatformIntegrationFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformIntegrationFactory: a plain Python object
  standing in front of one C++ QPlatformIntegrationFactory.

  C++ hands a QPlatformIntegrationFactory around as a copy, so every C++
  QPlatformIntegrationFactory behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QPlatformIntegrationFactory that has a ritual and
  that Python can call so far, 2 names in all: 'keys', 'create'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformIntegrationFactory::~QPlatformIntegrationFactory()': the
    destructor: Python removes its C++ QPlatformIntegrationFactory by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QPlatformIntegrationFactory is created at the first use, not by
    'QPlatformIntegrationFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformIntegrationFactory back gives a copy the
    ritual made for Python, in a new cute QPlatformIntegrationFactory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload()
  @overload(str)
  def keys(platformPluginPath: str = '') -> QStringList:
    """
    Calls Qt's 'QStringList QPlatformIntegrationFactory::keys(const QString
    &platformPluginPath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegrationfactory.html#keys

    Parameters
    ----------

    platformPluginPath : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlatformIntegrationFactory::keys(const QString
    #      &platformPluginPath)
    address = Rituals.call(
        'ritual_ZN27QPlatformIntegrationFactory4keysERK7QString',
        platformPluginPath,
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(str, QStringList, list)
  @overload(str, QStringList, list, str)
  def create(
      name: str,
      args: QStringList,
      argv: list,
      platformPluginPath: str = '',
  ) -> Optional[QPlatformIntegration]:
    """
    Calls Qt's 'QPlatformIntegration
    *QPlatformIntegrationFactory::create(const QString &name, const
    QStringList &args, int &argc, char **argv, const QString
    &platformPluginPath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformintegrationfactory.html#create

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    args : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    argv : list
      The texts the program was started with, as 'sys.argv'. Passed on as Qt
      takes them: how many they are, and where the first one is.

    platformPluginPath : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QPlatformIntegration]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformIntegration *QPlatformIntegrationFactory::create(const
    #      QString &name, const QStringList &args, int &argc, char **argv,
    #      const QString &platformPluginPath)
    address = Rituals.call(
        'ritual_ZN27QPlatformIntegrationFactory6createERK7QStringRK5QListIS'
        '0_ERiPPcS2_',
        name, CuteMixin._valueOf(args), *CuteMixin._startTextsOf(argv),
        platformPluginPath,
    )
    from . import QPlatformIntegration
    return QPlatformIntegration._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformIntegrationFactory'

  #  Qt's '~QPlatformIntegrationFactory()'. Naming it makes this a value
  #  class: Python owns every C++ QPlatformIntegrationFactory behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QPlatformIntegrationFactoryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

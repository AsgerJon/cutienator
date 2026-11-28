"""
QPlatformInputContextFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatforminputcontextfactory_p.h, Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPlatformInputContext


class QPlatformInputContextFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformInputContextFactory: a plain Python object
  standing in front of one C++ QPlatformInputContextFactory.

  C++ hands a QPlatformInputContextFactory around as a copy, so every C++
  QPlatformInputContextFactory behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QPlatformInputContextFactory that has a ritual and
  that Python can call so far, 3 names in all: 'keys', 'requested', 'create'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformInputContextFactory::~QPlatformInputContextFactory()': the
    destructor: Python removes its C++ QPlatformInputContextFactory by it,
    and has no other use for it.

  What to expect
  --------------

  - The C++ QPlatformInputContextFactory is created at the first use, not by
    'QPlatformInputContextFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformInputContextFactory back gives a copy the
    ritual made for Python, in a new cute QPlatformInputContextFactory.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def keys() -> QStringList:
    """
    Calls Qt's 'QStringList QPlatformInputContextFactory::keys()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontextfactory.html#keys

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlatformInputContextFactory::keys()
    address = Rituals.call('ritual_ZN28QPlatformInputContextFactory4keysEv')
    return QStringList._cuteOwning(address)

  @staticmethod
  def requested() -> QStringList:
    """
    Calls Qt's 'QStringList QPlatformInputContextFactory::requested()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontextfactory.html#requested

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QPlatformInputContextFactory::requested()
    address = Rituals.call(
        'ritual_ZN28QPlatformInputContextFactory9requestedEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(QStringList)
  def create(keys: QStringList) -> Optional[QPlatformInputContext]:
    """
    Calls Qt's 'QPlatformInputContext
    *QPlatformInputContextFactory::create(const QStringList &keys)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontextfactory.html#create

    Parameters
    ----------

    keys : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QPlatformInputContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformInputContext *QPlatformInputContextFactory::create(const
    #      QStringList &keys)
    address = Rituals.call(
        'ritual_ZN28QPlatformInputContextFactory6createERK5QListI7QStringE',
        CuteMixin._valueOf(keys),
    )
    from . import QPlatformInputContext
    return QPlatformInputContext._cuteAt(address)

  @staticmethod
  @overload(str)
  def create(key: str) -> Optional[QPlatformInputContext]:
    """
    Calls Qt's 'QPlatformInputContext
    *QPlatformInputContextFactory::create(const QString &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontextfactory.html#create

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QPlatformInputContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformInputContext *QPlatformInputContextFactory::create(const
    #      QString &key)
    address = Rituals.call(
        'ritual_ZN28QPlatformInputContextFactory6createERK7QString', key,
    )
    from . import QPlatformInputContext
    return QPlatformInputContext._cuteAt(address)

  @staticmethod
  @overload()
  def create() -> Optional[QPlatformInputContext]:
    """
    Calls Qt's 'QPlatformInputContext
    *QPlatformInputContextFactory::create()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatforminputcontextfactory.html#create

    Returns
    -------

    Optional[QPlatformInputContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformInputContext *QPlatformInputContextFactory::create()
    address = Rituals.call(
        'ritual_ZN28QPlatformInputContextFactory6createEv',
    )
    from . import QPlatformInputContext
    return QPlatformInputContext._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformInputContextFactory'

  #  Qt's '~QPlatformInputContextFactory()'. Naming it makes this a value
  #  class: Python owns every C++ QPlatformInputContextFactory behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN28QPlatformInputContextFactoryD1Ev'

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

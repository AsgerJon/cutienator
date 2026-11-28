"""
QtROClientFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/qconnectionfactories.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QUrl
  from . import QtROClientIoDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QtROClientFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtROClientFactory: a plain Python object standing in
  front of one C++ QtROClientFactory.

  C++ hands a QtROClientFactory around as a copy, so every C++
  QtROClientFactory behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtROClientFactory that has a ritual and that Python
  can call so far, 3 names in all: 'instance', 'create', 'isValid'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtROClientFactory::~QtROClientFactory()': the destructor: Python
    removes its C++ QtROClientFactory by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 1 a template; 1 leans on 'TcpClientIo.

  What to expect
  --------------

  - The C++ QtROClientFactory is created at the first use, not by
    'QtROClientFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtROClientFactory back gives a copy the ritual made
    for Python, in a new cute QtROClientFactory.
  - Each name of Qt's QtROClientFactory that has no cute function yet,
    '__init__', 'registerType', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def instance() -> Optional[QtROClientFactory]:
    """
    Calls Qt's 'QtROClientFactory *QtROClientFactory::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qtroclientfactory.html#instance

    Returns
    -------

    Optional[QtROClientFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtROClientFactory *QtROClientFactory::instance()
    address = Rituals.call('ritual_ZN17QtROClientFactory8instanceEv')
    return QtROClientFactory._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtROClientFactory'

  #  Qt's '~QtROClientFactory()'. Naming it makes this a value class: Python
  #  owns every C++ QtROClientFactory behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QtROClientFactoryD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QtROClientFactory::QtROClientFactory()': leans on
    'TcpClientIo::staticMetaObject', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtROClientFactory.__init__' has no cute function yet. Qt's "
        "'QtROClientFactory::QtROClientFactory()': leans on "
        "'TcpClientIo::staticMetaObject', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  @overload(QUrl)
  @overload(QUrl, QObject)
  @overload(QUrl, NoneType)
  def create(
      self,
      url: QUrl,
      parent: Optional[QObject] = None,
  ) -> Optional[QtROClientIoDevice]:
    """
    Calls Qt's 'QtROClientIoDevice *QtROClientFactory::create(const QUrl
    &url, QObject *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtroclientfactory.html#create

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QtROClientIoDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtROClientIoDevice *QtROClientFactory::create(const QUrl &url, QObject
    #      *parent)
    address = self.uglySide.call(
        'ritual_ZN17QtROClientFactory6createERK4QUrlP7QObject',
        self._valueOf(url), self._addressOf(parent, 'QObject'),
    )
    from . import QtROClientIoDevice
    return QtROClientIoDevice._cuteAt(address)

  @overload(QUrl)
  def isValid(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QtROClientFactory::isValid(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qtroclientfactory.html#isValid

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QtROClientFactory::isValid(const QUrl &url)
    return self.uglySide.call(
        'ritual_ZN17QtROClientFactory7isValidERK4QUrl', self._valueOf(url),
    )

  @staticmethod
  def registerType(*__, **_) -> Never:
    """
    Qt's 'QtROClientFactory::registerType': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QtROClientFactory.registerType' has no cute function yet. Qt's "
        "'QtROClientFactory::registerType': a template: a pattern and no "
        "single function.")

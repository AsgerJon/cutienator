"""
QtROServerFactory binding of the Qt C++
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
  from . import QConnectionAbstractServer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QtROServerFactory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtROServerFactory: a plain Python object standing in
  front of one C++ QtROServerFactory.

  C++ hands a QtROServerFactory around as a copy, so every C++
  QtROServerFactory behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtROServerFactory that has a ritual and that Python
  can call so far, 3 names in all: 'instance', 'create', 'isValid'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtROServerFactory::~QtROServerFactory()': the destructor: Python
    removes its C++ QtROServerFactory by it, and has no other use for it.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 1 a template; 1 leans on 'vtable for
  TcpServerImpl', which Qt's source does not mark for use from outside Qt and
  has no code for that could be taken.

  What to expect
  --------------

  - The C++ QtROServerFactory is created at the first use, not by
    'QtROServerFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtROServerFactory back gives a copy the ritual made
    for Python, in a new cute QtROServerFactory.
  - Each name of Qt's QtROServerFactory that has no cute function yet,
    '__init__', 'registerType', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def instance() -> Optional[QtROServerFactory]:
    """
    Calls Qt's 'QtROServerFactory *QtROServerFactory::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qtroserverfactory.html#instance

    Returns
    -------

    Optional[QtROServerFactory]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtROServerFactory *QtROServerFactory::instance()
    address = Rituals.call('ritual_ZN17QtROServerFactory8instanceEv')
    return QtROServerFactory._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtROServerFactory'

  #  Qt's '~QtROServerFactory()'. Naming it makes this a value class: Python
  #  owns every C++ QtROServerFactory behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QtROServerFactoryD1Ev'

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
    Qt's 'QtROServerFactory::QtROServerFactory()': leans on 'vtable for
    TcpServerImpl', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QtROServerFactory.__init__' has no cute function yet. Qt's "
        "'QtROServerFactory::QtROServerFactory()': leans on 'vtable for "
        "TcpServerImpl', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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
  ) -> Optional[QConnectionAbstractServer]:
    """
    Calls Qt's 'QConnectionAbstractServer *QtROServerFactory::create(const
    QUrl &url, QObject *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtroserverfactory.html#create

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QConnectionAbstractServer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QConnectionAbstractServer *QtROServerFactory::create(const QUrl &url,
    #      QObject *parent)
    address = self.uglySide.call(
        'ritual_ZN17QtROServerFactory6createERK4QUrlP7QObject',
        self._valueOf(url), self._addressOf(parent, 'QObject'),
    )
    from . import QConnectionAbstractServer
    return QConnectionAbstractServer._cuteAt(address)

  @overload(QUrl)
  def isValid(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QtROServerFactory::isValid(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qtroserverfactory.html#isValid

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QtROServerFactory::isValid(const QUrl &url)
    return self.uglySide.call(
        'ritual_ZN17QtROServerFactory7isValidERK4QUrl', self._valueOf(url),
    )

  @staticmethod
  def registerType(*__, **_) -> Never:
    """
    Qt's 'QtROServerFactory::registerType': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QtROServerFactory.registerType' has no cute function yet. Qt's "
        "'QtROServerFactory::registerType': a template: a pattern and no "
        "single function.")

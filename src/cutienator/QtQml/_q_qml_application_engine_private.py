"""
QQmlApplicationEnginePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlapplicationengine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlApplicationEnginePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQmlEnginePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QUrl
  from . import QQmlApplicationEngine, QQmlComponent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QQmlComponent = WAIT['QQmlComponent']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlApplicationEnginePrivate(QQmlEnginePrivate):
  """
  The cute side of Qt's QQmlApplicationEnginePrivate: a plain Python object
  standing in front of one C++ QQmlApplicationEnginePrivate.

  It is built on the cute 'QQmlEnginePrivate', as Qt's
  QQmlApplicationEnginePrivate is built on Qt's QQmlEnginePrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlApplicationEnginePrivate that has a ritual and
  that Python can call so far, 9 names in all: 'q_func', 'ensureInitialized',
  'init', 'cleanUp', 'startLoad', '_q_loadTranslations', 'finishLoad',
  'ensureLoadingFinishes', 'updateTranslationDirectory'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQmlApplicationEngine *QQmlApplicationEnginePrivate::q_func()
    const': takes in Python what 'QQmlApplicationEngine
    *QQmlApplicationEnginePrivate::q_func()' takes.
  - Qt's 'QQmlApplicationEnginePrivate::~QQmlApplicationEnginePrivate()': the
    destructor: Python never removes a C++ QQmlApplicationEnginePrivate.

  What to expect
  --------------

  - The C++ QQmlApplicationEnginePrivate is created at the first use, not by
    'QQmlApplicationEnginePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlApplicationEnginePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlApplicationEnginePrivate'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlApplicationEnginePrivate::QQmlApplicationEnginePrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengineprivate.html
    """
    #  QQmlApplicationEnginePrivate::QQmlApplicationEnginePrivate()
    self._noteCreation(QQmlApplicationEnginePrivate, lambda: Rituals.call(
        'ritual_ZN28QQmlApplicationEnginePrivateC1Ev',
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

  def q_func(self) -> Optional[QQmlApplicationEngine]:
    """
    Calls Qt's 'QQmlApplicationEngine
    *QQmlApplicationEnginePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengineprivate.html#q_func

    Returns
    -------

    Optional[QQmlApplicationEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlApplicationEngine *QQmlApplicationEnginePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QQmlApplicationEnginePrivate6q_funcEv',
    )
    from . import QQmlApplicationEngine
    return QQmlApplicationEngine._cuteAt(address)

  def ensureInitialized(self) -> None:
    """
    Calls Qt's 'void QQmlApplicationEnginePrivate::ensureInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengineprivate.html
    """
    #  void QQmlApplicationEnginePrivate::ensureInitialized()
    self.uglySide.call(
        'ritual_ZN28QQmlApplicationEnginePrivate17ensureInitializedEv',
    )

  def init(self) -> None:
    """
    Calls Qt's 'void QQmlApplicationEnginePrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengineprivate.html#init
    """
    #  void QQmlApplicationEnginePrivate::init()
    self.uglySide.call('ritual_ZN28QQmlApplicationEnginePrivate4initEv')

  def cleanUp(self) -> None:
    """
    Calls Qt's 'void QQmlApplicationEnginePrivate::cleanUp()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengineprivate.html#cleanUp
    """
    #  void QQmlApplicationEnginePrivate::cleanUp()
    self.uglySide.call('ritual_ZN28QQmlApplicationEnginePrivate7cleanUpEv')

  @overload(QUrl)
  @overload(QUrl, QByteArray)
  @overload(QUrl, QByteArray, bool)
  def startLoad(
      self,
      url: QUrl,
      data: Optional[QByteArray] = None,
      dataFlag: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QQmlApplicationEnginePrivate::startLoad(const QUrl &url,
    const QByteArray &data, bool dataFlag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengineprivate.html#startLoad

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    data : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.

    dataFlag : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQmlApplicationEnginePrivate::startLoad(const QUrl &url, const
    #      QByteArray &data, bool dataFlag)
    if data is None:
      from ..QtCore import QByteArray
      data = QByteArray()
    self.uglySide.call(
        'ritual_ZN28QQmlApplicationEnginePrivate9startLoadERK4QUrlRK10QByte'
        'Arrayb',
        self._valueOf(url), self._valueOf(data), dataFlag,
    )

  @overload(str, str)
  def startLoad(self, uri: str, type: str) -> None:
    """
    Calls Qt's 'void QQmlApplicationEnginePrivate::startLoad(QAnyStringView
    uri, QAnyStringView type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengineprivate.html#startLoad

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    type : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlApplicationEnginePrivate::startLoad(QAnyStringView uri,
    #      QAnyStringView type)
    self.uglySide.call(
        'ritual_ZN28QQmlApplicationEnginePrivate9startLoadE14QAnyStringView'
        'S0_',
        uri, type,
    )

  def _q_loadTranslations(self) -> None:
    """
    Calls Qt's 'void QQmlApplicationEnginePrivate::_q_loadTranslations()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengineprivate.html
    """
    #  void QQmlApplicationEnginePrivate::_q_loadTranslations()
    self.uglySide.call(
        'ritual_ZN28QQmlApplicationEnginePrivate19_q_loadTranslationsEv',
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def finishLoad(self, component: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQmlApplicationEnginePrivate::finishLoad(QQmlComponent
    *component)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengineprivate.html#finishLoad

    Parameters
    ----------

    component : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlApplicationEnginePrivate::finishLoad(QQmlComponent
    #      *component)
    self.uglySide.call(
        'ritual_ZN28QQmlApplicationEnginePrivate10finishLoadEP13QQmlCompone'
        'nt',
        self._addressOf(component),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def ensureLoadingFinishes(
      self,
      component: Optional[QQmlComponent],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlApplicationEnginePrivate::ensureLoadingFinishes(QQmlComponent
    *component)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengineprivate.html

    Parameters
    ----------

    component : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlApplicationEnginePrivate::ensureLoadingFinishes(QQmlComponent
    #      *component)
    self.uglySide.call(
        'ritual_ZN28QQmlApplicationEnginePrivate21ensureLoadingFinishesEP13'
        'QQmlComponent',
        self._addressOf(component),
    )

  @overload(QUrl)
  def updateTranslationDirectory(self, url: QUrl) -> None:
    """
    Calls Qt's 'void
    QQmlApplicationEnginePrivate::updateTranslationDirectory(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlapplicationengineprivate.html

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlApplicationEnginePrivate::updateTranslationDirectory(const
    #      QUrl &url)
    self.uglySide.call(
        'ritual_ZN28QQmlApplicationEnginePrivate26updateTranslationDirector'
        'yERK4QUrl',
        self._valueOf(url),
    )

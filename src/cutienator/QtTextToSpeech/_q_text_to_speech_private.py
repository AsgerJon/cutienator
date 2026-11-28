"""
QTextToSpeechPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTextToSpeech/6.12.0/QtTextToSpeech/private/qtexttospeech_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QTextToSpeechPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QTextToSpeech

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextToSpeechPrivate(QObjectPrivate):
  """
  The cute side of Qt's QTextToSpeechPrivate: a plain Python object standing
  in front of one C++ QTextToSpeechPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QTextToSpeechPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextToSpeechPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'q_func', 'updateState',
  'disconnectSynthesizeFunctor'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTextToSpeech *QTextToSpeechPrivate::q_func() const': takes
    in Python what 'QTextToSpeech *QTextToSpeechPrivate::q_func()' takes.
  - Qt's 'QTextToSpeechPrivate::~QTextToSpeechPrivate()': the destructor:
    Python never removes a C++ QTextToSpeechPrivate.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 3 leans on 'QTextToSpeechPrivate; 2 Qt's
  library has no name for it, and its code in Qt's source does not compile
  apart from its file.

  What to expect
  --------------

  - The C++ QTextToSpeechPrivate is created at the first use, not by
    'QTextToSpeechPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextToSpeechPrivate.
  - Each name of Qt's QTextToSpeechPrivate that has no cute function yet,
    'loadMeta', 'loadPlugin', 'loadPluginMetadata', 'plugins',
    'setEngineProvider', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextToSpeechPrivate'

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

  @overload(QTextToSpeech)
  @overload(NoneType)
  def __init__(self, speech: Optional[QTextToSpeech]) -> None:
    """
    Notes what was given, for Qt's
    'QTextToSpeechPrivate::QTextToSpeechPrivate(QTextToSpeech *speech)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechprivate.html#QTextToSpeechPrivate

    Parameters
    ----------

    speech : Optional[QTextToSpeech]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextToSpeechPrivate::QTextToSpeechPrivate(QTextToSpeech *speech)
    self._noteCreation(QTextToSpeechPrivate, lambda: Rituals.call(
        'ritual_ZN20QTextToSpeechPrivateC1EP13QTextToSpeech',
        self._addressOf(speech),
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

  def q_func(self) -> Optional[QTextToSpeech]:
    """
    Calls Qt's 'QTextToSpeech *QTextToSpeechPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechprivate.html#q_func

    Returns
    -------

    Optional[QTextToSpeech]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextToSpeech *QTextToSpeechPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QTextToSpeechPrivate6q_funcEv')
    return QTextToSpeech._cuteAt(address)

  @overload(QTextToSpeech.State)
  def updateState(self, newState: QTextToSpeech.State) -> None:
    """
    Calls Qt's 'void QTextToSpeechPrivate::updateState(QTextToSpeech::State
    newState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechprivate.html#updateState

    Parameters
    ----------

    newState : QTextToSpeech.State
      Passed on as its number.
    """
    #  void QTextToSpeechPrivate::updateState(QTextToSpeech::State newState)
    self.uglySide.call(
        'ritual_ZN20QTextToSpeechPrivate11updateStateEN13QTextToSpeech5Stat'
        'eE',
        newState.value,
    )

  def disconnectSynthesizeFunctor(self) -> None:
    """
    Calls Qt's 'void QTextToSpeechPrivate::disconnectSynthesizeFunctor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechprivate.html
    """
    #  void QTextToSpeechPrivate::disconnectSynthesizeFunctor()
    self.uglySide.call(
        'ritual_ZN20QTextToSpeechPrivate27disconnectSynthesizeFunctorEv',
    )

  @staticmethod
  def loadMeta(*__, **_) -> Never:
    """
    Qt's 'bool QTextToSpeechPrivate::loadMeta()': leans on
    'QTextToSpeechPrivate::m_mutex', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTextToSpeechPrivate.loadMeta' has no cute function yet. Qt's "
        "'bool QTextToSpeechPrivate::loadMeta()': leans on "
        "'QTextToSpeechPrivate::m_mutex', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def loadPlugin(*__, **_) -> Never:
    """
    Qt's 'void QTextToSpeechPrivate::loadPlugin()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'loader'.
    """
    raise NotImplementedError(
        "'QTextToSpeechPrivate.loadPlugin' has no cute function yet. Qt's "
        "'void QTextToSpeechPrivate::loadPlugin()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'loader'.")

  @staticmethod
  def loadPluginMetadata(*__, **_) -> Never:
    """
    Qt's 'void QTextToSpeechPrivate::loadPluginMetadata(QMultiHash<QString,
    QCborMap> &list)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'loader'.
    """
    raise NotImplementedError(
        "'QTextToSpeechPrivate.loadPluginMetadata' has no cute function "
        "yet. Qt's 'void "
        "QTextToSpeechPrivate::loadPluginMetadata(QMultiHash<QString, "
        "QCborMap> &list)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'loader'.")

  @staticmethod
  def plugins(*__, **_) -> Never:
    """
    Qt's 'QMultiHash<QString, QCborMap> QTextToSpeechPrivate::plugins(bool
    reload)': leans on 'QTextToSpeechPrivate::m_mutex', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QTextToSpeechPrivate.plugins' has no cute function yet. Qt's "
        "'QMultiHash<QString, QCborMap> QTextToSpeechPrivate::plugins(bool "
        "reload)': leans on 'QTextToSpeechPrivate::m_mutex', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setEngineProvider(*__, **_) -> Never:
    """
    Qt's 'void QTextToSpeechPrivate::setEngineProvider(const QString &engine,
    const QVariantMap &params)': leans on 'QTextToSpeechPrivate::m_mutex',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QTextToSpeechPrivate.setEngineProvider' has no cute function yet. "
        "Qt's 'void QTextToSpeechPrivate::setEngineProvider(const QString "
        "&engine, const QVariantMap &params)': leans on "
        "'QTextToSpeechPrivate::m_mutex', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

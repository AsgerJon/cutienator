"""
Qt3DCore::QSystemInformationService binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qsysteminformationservice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::QSystemInformationService to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSystemInformationService(Qt3DCore.QAbstractServiceProvider):
  """
  The cute side of Qt's Qt3DCore::QSystemInformationService: a plain Python
  object standing in front of one C++ Qt3DCore::QSystemInformationService.

  It is built on the cute 'Qt3DCore::QAbstractServiceProvider', as Qt's
  Qt3DCore::QSystemInformationService is built on Qt's
  Qt3DCore::QAbstractServiceProvider, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QSystemInformationService that has a
  ritual and that Python can call so far, 16 names in all: 'metaObject',
  'tr', 'isTraceEnabled', 'isGraphicsTraceEnabled', 'isCommandServerEnabled',
  'aspectNames', 'threadPoolThreadCount', 'writePreviousFrameTraces',
  'revealLogFolder', 'setTraceEnabled', 'setGraphicsTraceEnabled',
  'executeCommand', 'dumpCommand', 'traceEnabledChanged',
  'graphicsTraceEnabledChanged', 'd_func'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QSystemInformationService::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DCore::QSystemInformationService::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QSystemInformationServicePrivate
    *Qt3DCore::QSystemInformationService::d_func() const': takes in Python
    what 'QSystemInformationServicePrivate
    *Qt3DCore::QSystemInformationService::d_func()' takes.
  - Qt's 'Qt3DCore::QSystemInformationService::QSystemInformationService(
    QSystemInformationServicePrivate &dd)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QSystemInformationService is created at the first use,
    not by 'Qt3DCore::QSystemInformationService(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QSystemInformationService.
  - Qt tells when it has removed the C++ Qt3DCore::QSystemInformationService.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DCore::QSystemInformationService::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::QSystemInformationService::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore25QSystemInformationService2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QSystemInformationService'

  #  A C++ Qt3DCore::QSystemInformationService Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QSystemInformationService'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DCore::QSystemInformationService::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QSystemInformationService::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore25QSystemInformationService10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isTraceEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QSystemInformationService::isTraceEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html
    """
    #  bool Qt3DCore::QSystemInformationService::isTraceEnabled() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore25QSystemInformationService14isTraceEnabledEv',
    )

  def isGraphicsTraceEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DCore::QSystemInformationService::isGraphicsTraceEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html
    """
    #  bool Qt3DCore::QSystemInformationService::isGraphicsTraceEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore25QSystemInformationService22isGraphicsTraceEna'
        'bledEv',
    )

  def isCommandServerEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DCore::QSystemInformationService::isCommandServerEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html
    """
    #  bool Qt3DCore::QSystemInformationService::isCommandServerEnabled()
    #      const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore25QSystemInformationService22isCommandServerEna'
        'bledEv',
    )

  def aspectNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    Qt3DCore::QSystemInformationService::aspectNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DCore::QSystemInformationService::aspectNames() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore25QSystemInformationService11aspectNamesEv',
    )
    return QStringList._cuteOwning(address)

  def threadPoolThreadCount(self) -> int:
    """
    Calls Qt's 'int
    Qt3DCore::QSystemInformationService::threadPoolThreadCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html
    """
    #  int Qt3DCore::QSystemInformationService::threadPoolThreadCount() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore25QSystemInformationService21threadPoolThreadCo'
        'untEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setTraceEnabled(self, traceEnabled: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QSystemInformationService::setTraceEnabled(bool traceEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html

    Parameters
    ----------

    traceEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QSystemInformationService::setTraceEnabled(bool
    #      traceEnabled)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore25QSystemInformationService15setTraceEnabledEb',
        traceEnabled,
    )

  @overload(bool)
  def setGraphicsTraceEnabled(self, graphicsTraceEnabled: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QSystemInformationService::setGraphicsTraceEnabled(bool
    graphicsTraceEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html

    Parameters
    ----------

    graphicsTraceEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QSystemInformationService::setGraphicsTraceEnabled(bool
    #      graphicsTraceEnabled)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore25QSystemInformationService23setGraphicsTraceEna'
        'bledEb',
        graphicsTraceEnabled,
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

  @overload(WAIT['Qt3DCore.QAspectEngine'])
  @overload(NoneType)
  def __init__(self, aspectEngine: Optional[Qt3DCore.QAspectEngine]) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QSystemInformationService::QSystemInformationService(
    QAspectEngine *aspectEngine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html

    Parameters
    ----------

    aspectEngine : Optional[Qt3DCore.QAspectEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DCore::QSystemInformationService::QSystemInformationService(
    #      QAspectEngine *aspectEngine)
    self._noteCreation(QSystemInformationService, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore25QSystemInformationServiceC1EPNS_13QAspectEngin'
        'eE',
        self._addressOf(aspectEngine),
    ))

  @overload(WAIT['Qt3DCore.QAspectEngine'], str)
  @overload(NoneType, str)
  def __init__(
      self,
      aspectEngine: Optional[Qt3DCore.QAspectEngine],
      description: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QSystemInformationService::QSystemInformationService(
    QAspectEngine *aspectEngine, const QString &description)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html

    Parameters
    ----------

    aspectEngine : Optional[Qt3DCore.QAspectEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  Qt3DCore::QSystemInformationService::QSystemInformationService(
    #      QAspectEngine *aspectEngine, const QString &description)
    self._noteCreation(QSystemInformationService, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore25QSystemInformationServiceC1EPNS_13QAspectEngin'
        'eERK7QString',
        self._addressOf(aspectEngine), description,
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

  def writePreviousFrameTraces(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QSystemInformationService::writePreviousFrameTraces()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html
    """
    #  void Qt3DCore::QSystemInformationService::writePreviousFrameTraces()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore25QSystemInformationService24writePreviousFrameT'
        'racesEv',
    )

  def revealLogFolder(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QSystemInformationService::revealLogFolder()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html
    """
    #  void Qt3DCore::QSystemInformationService::revealLogFolder()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore25QSystemInformationService15revealLogFolderEv',
    )

  @overload(str)
  def executeCommand(self, command: str) -> QVariant:
    """
    Calls Qt's 'QVariant
    Qt3DCore::QSystemInformationService::executeCommand(const QString
    &command)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html

    Parameters
    ----------

    command : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DCore::QSystemInformationService::executeCommand(const
    #      QString &command)
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore25QSystemInformationService14executeCommandERK7Q'
        'String',
        command,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  def dumpCommand(self, command: str) -> None:
    """
    Calls Qt's 'void Qt3DCore::QSystemInformationService::dumpCommand(const
    QString &command)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html

    Parameters
    ----------

    command : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DCore::QSystemInformationService::dumpCommand(const QString
    #      &command)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore25QSystemInformationService11dumpCommandERK7QStr'
        'ing',
        command,
    )

  @overload(bool)
  def traceEnabledChanged(self, traceEnabled: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QSystemInformationService::traceEnabledChanged(bool
    traceEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html

    Parameters
    ----------

    traceEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QSystemInformationService::traceEnabledChanged(bool
    #      traceEnabled)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore25QSystemInformationService19traceEnabledChanged'
        'Eb',
        traceEnabled,
    )

  @overload(bool)
  def graphicsTraceEnabledChanged(self, graphicsTraceEnabled: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QSystemInformationService::graphicsTraceEnabledChanged(bool
    graphicsTraceEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html

    Parameters
    ----------

    graphicsTraceEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QSystemInformationService::graphicsTraceEnabledChanged(
    #      bool graphicsTraceEnabled)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore25QSystemInformationService27graphicsTraceEnable'
        'dChangedEb',
        graphicsTraceEnabled,
    )

  def d_func(self) -> Optional[Qt3DCore.QSystemInformationServicePrivate]:
    """
    Calls Qt's 'QSystemInformationServicePrivate
    *Qt3DCore::QSystemInformationService::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationservice.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QSystemInformationServicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSystemInformationServicePrivate
    #      *Qt3DCore::QSystemInformationService::d_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore25QSystemInformationService6d_funcEv',
    )
    return Qt3DCore.QSystemInformationServicePrivate._cuteAt(address)

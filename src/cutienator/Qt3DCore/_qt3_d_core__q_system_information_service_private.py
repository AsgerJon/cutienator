"""
Qt3DCore::QSystemInformationServicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qsysteminformationservice_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DCore::QSystemInformationServicePrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSystemInformationServicePrivate(Qt3DCore.QAbstractServiceProviderPrivate):
  """
  The cute side of Qt's Qt3DCore::QSystemInformationServicePrivate: a plain
  Python object standing in front of one C++
  Qt3DCore::QSystemInformationServicePrivate.

  It is built on the cute 'Qt3DCore::QAbstractServiceProviderPrivate', as
  Qt's Qt3DCore::QSystemInformationServicePrivate is built on Qt's
  Qt3DCore::QAbstractServiceProviderPrivate, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QSystemInformationServicePrivate that has
  a ritual and that Python can call so far, 4 names in all: 'get',
  'writeFrameJobLogStats', 'updateTracing', 'q_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QSystemInformationServicePrivate::
    ~QSystemInformationServicePrivate()': the destructor: Python never
    removes a C++ Qt3DCore::QSystemInformationServicePrivate.
  - Qt's 'void
    Qt3DCore::QSystemInformationServicePrivate::addJobLogStatsEntry(
    JobRunStats &stats)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    Qt3DCore::QSystemInformationServicePrivate::addSubmissionLogStatsEntry(
    JobRunStats &stats)': takes a type Python has no way to hand over yet.
  - Qt's 'const QSystemInformationService
    *Qt3DCore::QSystemInformationServicePrivate::q_func() const': takes in
    Python what 'QSystemInformationService
    *Qt3DCore::QSystemInformationServicePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DCore::QSystemInformationServicePrivate is created at the
    first use, not by 'Qt3DCore::QSystemInformationServicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QSystemInformationServicePrivate.
  - Each name of Qt's Qt3DCore::QSystemInformationServicePrivate that has no
    cute function yet, 'addJobLogStatsEntry', 'addSubmissionLogStatsEntry',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The classes Qt writes inside Qt3DCore::QSystemInformationServicePrivate,
  #  each a class in here as in C++.

  class JobRunStats(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's
    Qt3DCore::QSystemInformationServicePrivate::JobRunStats: a plain Python
    object standing in front of one C++
    Qt3DCore::QSystemInformationServicePrivate::JobRunStats.

    C++ hands a Qt3DCore::QSystemInformationServicePrivate::JobRunStats
    around as a copy, so every C++
    Qt3DCore::QSystemInformationServicePrivate::JobRunStats behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's
    Qt3DCore::QSystemInformationServicePrivate::JobRunStats yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'Qt3DCore::QSystemInformationServicePrivate::JobRunStats::~JobRunStats(
      )': the destructor: Python removes its C++
      Qt3DCore::QSystemInformationServicePrivate::JobRunStats by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ Qt3DCore::QSystemInformationServicePrivate::JobRunStats is
      created at the first use, not by
      'Qt3DCore::QSystemInformationServicePrivate::JobRunStats(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a
      Qt3DCore::QSystemInformationServicePrivate::JobRunStats back gives a
      copy the ritual made for Python, in a new cute
      Qt3DCore::QSystemInformationServicePrivate::JobRunStats.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'Qt3DCore::QSystemInformationServicePrivate::JobRunStats'

    #  Qt's '~Qt3DCore::QSystemInformationServicePrivate::JobRunStats()'.
    #  Naming it makes this a value class: Python owns every C++
    #  Qt3DCore::QSystemInformationServicePrivate::JobRunStats behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN8Qt3DCore32QSystemInformationServicePrivate11JobRunStatsD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'Qt3DCore::QSystemInformationServicePrivate::JobRunStats::JobRunStats(
      )', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qt3dcore-qsysteminformationserviceprivate-jobrunstats.html
      """
      #  Qt3DCore::QSystemInformationServicePrivate::JobRunStats::
      #      JobRunStats()
      self._noteCreation(
          QSystemInformationServicePrivate.JobRunStats, lambda: Rituals.call(
              'ritual_ZN8Qt3DCore32QSystemInformationServicePrivate11JobRun'
              'StatsC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.QSystemInformationService'])
  @overload(NoneType)
  def get(
      q: Optional[Qt3DCore.QSystemInformationService],
  ) -> Optional[QSystemInformationServicePrivate]:
    """
    Calls Qt's 'QSystemInformationServicePrivate
    *Qt3DCore::QSystemInformationServicePrivate::get(
    QSystemInformationService *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationserviceprivate.html#get

    Parameters
    ----------

    q : Optional[Qt3DCore.QSystemInformationService]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSystemInformationServicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSystemInformationServicePrivate
    #      *Qt3DCore::QSystemInformationServicePrivate::get(
    #      QSystemInformationService *q)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore32QSystemInformationServicePrivate3getEPNS_25QSy'
        'stemInformationServiceE',
        CuteMixin._addressOf(q),
    )
    return QSystemInformationServicePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QSystemInformationServicePrivate'

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

  @overload(WAIT['Qt3DCore.QAspectEngine'], str)
  @overload(NoneType, str)
  def __init__(
      self,
      aspectEngine: Optional[Qt3DCore.QAspectEngine],
      description: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QSystemInformationServicePrivate::
    QSystemInformationServicePrivate(QAspectEngine *aspectEngine, const
    QString &description)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationserviceprivate.html

    Parameters
    ----------

    aspectEngine : Optional[Qt3DCore.QAspectEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  Qt3DCore::QSystemInformationServicePrivate::
    #      QSystemInformationServicePrivate(QAspectEngine *aspectEngine,
    #      const QString &description)
    self._noteCreation(
        QSystemInformationServicePrivate, lambda: Rituals.call(
            'ritual_ZN8Qt3DCore32QSystemInformationServicePrivateC1EPNS_13Q'
            'AspectEngineERK7QString',
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

  def writeFrameJobLogStats(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QSystemInformationServicePrivate::writeFrameJobLogStats()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationserviceprivate.html
    """
    #  void
    #      Qt3DCore::QSystemInformationServicePrivate::writeFrameJobLogStats(
    #      )
    self.uglySide.call(
        'ritual_ZN8Qt3DCore32QSystemInformationServicePrivate21writeFrameJo'
        'bLogStatsEv',
    )

  def updateTracing(self) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QSystemInformationServicePrivate::updateTracing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationserviceprivate.html
    """
    #  void Qt3DCore::QSystemInformationServicePrivate::updateTracing()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore32QSystemInformationServicePrivate13updateTracin'
        'gEv',
    )

  def q_func(self) -> Optional[Qt3DCore.QSystemInformationService]:
    """
    Calls Qt's 'QSystemInformationService
    *Qt3DCore::QSystemInformationServicePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qsysteminformationserviceprivate.html

    Returns
    -------

    Optional[Qt3DCore.QSystemInformationService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSystemInformationService
    #      *Qt3DCore::QSystemInformationServicePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore32QSystemInformationServicePrivate6q_funcEv',
    )
    return Qt3DCore.QSystemInformationService._cuteAt(address)

  @staticmethod
  def addJobLogStatsEntry(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DCore::QSystemInformationServicePrivate::addJobLogStatsEntry(
    JobRunStats &stats)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QSystemInformationServicePrivate.addJobLogStatsEntry' "
        "has no cute function yet. Qt's 'void "
        "Qt3DCore::QSystemInformationServicePrivate::addJobLogStatsEntry(Job"
        "RunStats &stats)': takes a type Python has no way to hand over yet."
    )

  @staticmethod
  def addSubmissionLogStatsEntry(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DCore::QSystemInformationServicePrivate::addSubmissionLogStatsEntry(
    JobRunStats &stats)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QSystemInformationServicePrivate.addSubmissionLogStatsEnt"
        "ry' has no cute function yet. Qt's 'void "
        "Qt3DCore::QSystemInformationServicePrivate::addSubmissionLogStatsEn"
        "try(JobRunStats &stats)': takes a type Python has no way to hand "
        "over yet.")

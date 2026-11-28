"""
Qt3DCore::QTaskLogger binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qsysteminformationservice_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DCore::QTaskLogger to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTaskLogger(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QTaskLogger: a plain Python object standing
  in front of one C++ Qt3DCore::QTaskLogger.

  C++ hands a Qt3DCore::QTaskLogger around as a copy, so every C++
  Qt3DCore::QTaskLogger behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QTaskLogger that has a ritual and that
  Python can call so far, 2 names in all: 'end', 'restart'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QTaskLogger::~QTaskLogger()': the destructor: Python
    removes its C++ Qt3DCore::QTaskLogger by it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DCore::QTaskLogger is created at the first use, not by
    'Qt3DCore::QTaskLogger(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DCore::QTaskLogger back gives a copy the ritual
    made for Python, in a new cute Qt3DCore::QTaskLogger.
  """

  #  The enums Qt writes inside Qt3DCore::QTaskLogger, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'Qt3DCore::QTaskLogger::Type' of Qt, with the 2 names Qt gives
    in it.
    """

    AspectJob = Kee[int](0)
    Submission = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QTaskLogger'

  #  Qt's '~Qt3DCore::QTaskLogger()'. Naming it makes this a value class:
  #  Python owns every C++ Qt3DCore::QTaskLogger behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8Qt3DCore11QTaskLoggerD1Ev'

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

  @overload(
      WAIT['Qt3DCore.QSystemInformationService'], WAIT['Qt3DCore.JobId'],
      Type,
  )
  @overload(NoneType, WAIT['Qt3DCore.JobId'], Type)
  def __init__(
      self,
      service: Optional[Qt3DCore.QSystemInformationService],
      jobId: Qt3DCore.JobId,
      type: Type,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QTaskLogger::QTaskLogger(QSystemInformationService *service,
    const JobId &jobId, Type type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtasklogger.html#QTaskLogger

    Parameters
    ----------

    service : Optional[Qt3DCore.QSystemInformationService]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    jobId : Qt3DCore.JobId
      Passed on as a value: Qt reads the C++ Qt3DCore::JobId, which stays
      Python's own.

    type : Type
      Passed on as its number.
    """
    #  Qt3DCore::QTaskLogger::QTaskLogger(QSystemInformationService *service,
    #      const JobId &jobId, Type type)
    self._noteCreation(QTaskLogger, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore11QTaskLoggerC1EPNS_25QSystemInformationServiceE'
        'RKNS_5JobIdENS0_4TypeE',
        self._addressOf(service), self._valueOf(jobId), type.value,
    ))

  @overload(WAIT['Qt3DCore.QSystemInformationService'], int, int)
  @overload(NoneType, int, int)
  @overload(WAIT['Qt3DCore.QSystemInformationService'], int, int, Type)
  @overload(NoneType, int, int, Type)
  def __init__(
      self,
      service: Optional[Qt3DCore.QSystemInformationService],
      jobType: int,
      instance: int,
      type: Type = Type.Submission,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QTaskLogger::QTaskLogger(QSystemInformationService *service,
    const quint32 jobType, const quint32 instance, Type type)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qtasklogger.html#QTaskLogger

    Parameters
    ----------

    service : Optional[Qt3DCore.QSystemInformationService]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    jobType : int
      Passed on as it is.

    instance : int
      Passed on as it is.

    type : Type
      Passed on as its number. May be left out, as in Qt: it is then
      Type.Submission.
    """
    #  Qt3DCore::QTaskLogger::QTaskLogger(QSystemInformationService *service,
    #      const quint32 jobType, const quint32 instance, Type type)
    self._noteCreation(QTaskLogger, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore11QTaskLoggerC1EPNS_25QSystemInformationServiceE'
        'jjNS0_4TypeE',
        self._addressOf(service), jobType, instance, type.value,
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

  @overload()
  @overload(int)
  def end(self, t: int = 0) -> None:
    """
    Calls Qt's 'void Qt3DCore::QTaskLogger::end(qint64 t)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtasklogger.html#end

    Parameters
    ----------

    t : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void Qt3DCore::QTaskLogger::end(qint64 t)
    self.uglySide.call('ritual_ZN8Qt3DCore11QTaskLogger3endEx', t)

  def restart(self) -> int:
    """
    Calls Qt's 'qint64 Qt3DCore::QTaskLogger::restart()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qtasklogger.html#restart
    """
    #  qint64 Qt3DCore::QTaskLogger::restart()
    return self.uglySide.call('ritual_ZN8Qt3DCore11QTaskLogger7restartEv')

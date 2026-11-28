"""
Qt3DCore::QAspectJobManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qaspectjobmanager_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::QAspectJobManager to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAspectJobManager(Qt3DCore.QAbstractAspectJobManager):
  """
  The cute side of Qt's Qt3DCore::QAspectJobManager: a plain Python object
  standing in front of one C++ Qt3DCore::QAspectJobManager.

  It is built on the cute 'Qt3DCore::QAbstractAspectJobManager', as Qt's
  Qt3DCore::QAspectJobManager is built on Qt's
  Qt3DCore::QAbstractAspectJobManager, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAspectJobManager that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'initialize', 'waitForAllJobs', 'idealThreadCount'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QAspectJobManager::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DCore::QAspectJobManager::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QAspectJobManager::~QAspectJobManager()': the destructor:
    Python never removes a C++ Qt3DCore::QAspectJobManager.
  - Qt's 'void Qt3DCore::QAspectJobManager::enqueueJobs(const
    std::vector<QAspectJobPtr> &jobQueue)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void
    Qt3DCore::QAspectJobManager::waitForPerThreadFunction(JobFunction func,
    void *arg)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QAspectJobManager is created at the first use, not by
    'Qt3DCore::QAspectJobManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAspectJobManager.
  - Qt tells when it has removed the C++ Qt3DCore::QAspectJobManager. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DCore::QAspectJobManager::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qaspectjobmanager.html#tr

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
    #  QString Qt3DCore::QAspectJobManager::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore17QAspectJobManager2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def idealThreadCount() -> int:
    """
    Calls Qt's 'int Qt3DCore::QAspectJobManager::idealThreadCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjobmanager.html#idealThreadCount
    """
    #  int Qt3DCore::QAspectJobManager::idealThreadCount()
    return Rituals.call(
        'ritual_ZN8Qt3DCore17QAspectJobManager16idealThreadCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAspectJobManager'

  #  A C++ Qt3DCore::QAspectJobManager Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAspectJobManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QAspectJobManager::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjobmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QAspectJobManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore17QAspectJobManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
  @overload(WAIT['Qt3DCore.QAspectManager'])
  @overload(NoneType)
  def __init__(
      self,
      parent: Optional[Qt3DCore.QAspectManager] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QAspectJobManager::QAspectJobManager(QAspectManager *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjobmanager.html#QAspectJobManager

    Parameters
    ----------

    parent : Optional[Qt3DCore.QAspectManager]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QAspectJobManager::QAspectJobManager(QAspectManager *parent)
    self._noteCreation(QAspectJobManager, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore17QAspectJobManagerC1EPNS_14QAspectManagerE',
        self._addressOf(parent),
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

  def initialize(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectJobManager::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjobmanager.html#initialize
    """
    #  void Qt3DCore::QAspectJobManager::initialize()
    ritual = 'ritual_ZN8Qt3DCore17QAspectJobManager10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore17QAspectJobManager10initializeEv'
    self.uglySide.call(ritual)

  def waitForAllJobs(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QAspectJobManager::waitForAllJobs()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjobmanager.html#waitForAllJobs
    """
    #  int Qt3DCore::QAspectJobManager::waitForAllJobs()
    ritual = 'ritual_ZN8Qt3DCore17QAspectJobManager14waitForAllJobsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore17QAspectJobManager14waitForAllJobsEv'
    return self.uglySide.call(ritual)

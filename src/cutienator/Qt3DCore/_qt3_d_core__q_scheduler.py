"""
Qt3DCore::QScheduler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qscheduler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DCore::QScheduler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScheduler(QObject):
  """
  The cute side of Qt's Qt3DCore::QScheduler: a plain Python object standing
  in front of one C++ Qt3DCore::QScheduler.

  It is built on the cute 'QObject', as Qt's Qt3DCore::QScheduler is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QScheduler that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'setAspectManager',
  'aspectManager', 'scheduleAndWaitForFrameAspectJobs'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QScheduler::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DCore::QScheduler::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QScheduler::~QScheduler()': the destructor: Python never
    removes a C++ Qt3DCore::QScheduler.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 not a gap; 2 leans on 'Qt3DCore.

  What to expect
  --------------

  - The C++ Qt3DCore::QScheduler is created at the first use, not by
    'Qt3DCore::QScheduler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QScheduler.
  - Qt tells when it has removed the C++ Qt3DCore::QScheduler. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QScheduler that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QScheduler'

  #  A C++ Qt3DCore::QScheduler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QScheduler'

  #  The functions Qt calls itself that Qt3DCore::QScheduler is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'scheduleAndWaitForFrameAspectJobs': (
          ('_ZN8Qt3DCore10QScheduler33scheduleAndWaitForFrameAspectJobsExb',
           ('int', 'number', ''),
           (
               ('long long', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QScheduler::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qscheduler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QScheduler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QScheduler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def aspectManager(self) -> Optional[Qt3DCore.QAspectManager]:
    """
    Calls Qt's 'QAspectManager *Qt3DCore::QScheduler::aspectManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qscheduler.html#aspectManager

    Returns
    -------

    Optional[Qt3DCore.QAspectManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAspectManager *Qt3DCore::QScheduler::aspectManager() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore10QScheduler13aspectManagerEv',
    )
    return Qt3DCore.QAspectManager._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QAspectManager'])
  @overload(NoneType)
  def setAspectManager(
      self,
      aspectManager: Optional[Qt3DCore.QAspectManager],
  ) -> None:
    """
    Calls Qt's 'void Qt3DCore::QScheduler::setAspectManager(QAspectManager
    *aspectManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qscheduler.html#setAspectManager

    Parameters
    ----------

    aspectManager : Optional[Qt3DCore.QAspectManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QScheduler::setAspectManager(QAspectManager
    #      *aspectManager)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore10QScheduler16setAspectManagerEPNS_14QAspectMana'
        'gerE',
        self._addressOf(aspectManager),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QScheduler::QScheduler(QObject *parent)': leans on
    'Qt3DCore::QScheduler::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DCore.QScheduler.__init__' has no cute function yet. Qt's "
        "'Qt3DCore::QScheduler::QScheduler(QObject *parent)': leans on "
        "'Qt3DCore::QScheduler::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(int, bool)
  def scheduleAndWaitForFrameAspectJobs(
      self,
      time: int,
      dumpJobs: bool,
  ) -> int:
    """
    Calls Qt's 'int
    Qt3DCore::QScheduler::scheduleAndWaitForFrameAspectJobs(qint64 time, bool
    dumpJobs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qscheduler.html

    Parameters
    ----------

    time : int
      Passed on as it is.

    dumpJobs : bool
      Passed on as it is.
    """
    #  int Qt3DCore::QScheduler::scheduleAndWaitForFrameAspectJobs(qint64
    #      time, bool dumpJobs)
    return self.uglySide.call(
        'ritual_ZN8Qt3DCore10QScheduler33scheduleAndWaitForFrameAspectJobsE'
        'xb',
        time, dumpJobs,
    )

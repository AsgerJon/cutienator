"""
Qt3DCore::QAspectJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qaspectjob.h, Qt 6.12.0. Changes made here are lost.
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


class QAspectJob(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QAspectJob: a plain Python object standing
  in front of one C++ Qt3DCore::QAspectJob.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAspectJob that has a ritual and that
  Python can call so far, 4 names in all: 'run', 'postFrame', 'isRequired',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QAspectJob::~QAspectJob()': the destructor: Python never
    removes a C++ Qt3DCore::QAspectJob.
  - Qt's 'void Qt3DCore::QAspectJob::addDependency(QWeakPointer<QAspectJob>
    dependency)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    Qt3DCore::QAspectJob::removeDependency(QWeakPointer<QAspectJob>
    dependency)': takes a type Python has no way to hand over yet.
  - Qt's 'const std::vector<QWeakPointer<QAspectJob>>
    &Qt3DCore::QAspectJob::dependencies() const': gives a type Python has no
    way to take yet.
  - Qt's 'Qt3DCore::QAspectJob::QAspectJob(QAspectJobPrivate &dd)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QAspectJobPrivate *Qt3DCore::QAspectJob::d_func() const':
    takes in Python what 'QAspectJobPrivate *Qt3DCore::QAspectJob::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ Qt3DCore::QAspectJob is created at the first use, not by
    'Qt3DCore::QAspectJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAspectJob.
  - Each name of Qt's Qt3DCore::QAspectJob that has no cute function yet,
    'addDependency', 'dependencies', 'removeDependency', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAspectJob'

  #  A C++ Qt3DCore::QAspectJob Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAspectJob'

  #  The functions Qt calls itself that Qt3DCore::QAspectJob is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'run': (
          ('_ZN8Qt3DCore10QAspectJob3runEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'postFrame': (
          ('_ZN8Qt3DCore10QAspectJob9postFrameEPNS_13QAspectEngineE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QAspectEngine'),
           )),
      ),
      'isRequired': (
          ('_ZN8Qt3DCore10QAspectJob10isRequiredEv',
           ('bool', 'number', ''),
           ()),
      ),
  }

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
    Notes what was given, for Qt's 'Qt3DCore::QAspectJob::QAspectJob()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjob.html#QAspectJob
    """
    #  Qt3DCore::QAspectJob::QAspectJob()
    self._noteCreation(QAspectJob, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore10QAspectJobC1Ev',
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

  def run(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectJob::run()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qaspectjob.html#run
    """
    #  void Qt3DCore::QAspectJob::run()
    self.uglySide.call('ritual_ZN8Qt3DCore10QAspectJob3runEv')

  @overload(WAIT['Qt3DCore.QAspectEngine'])
  @overload(NoneType)
  def postFrame(
      self,
      aspectEngine: Optional[Qt3DCore.QAspectEngine],
  ) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectJob::postFrame(QAspectEngine
    *aspectEngine)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qaspectjob.html#postFrame

    Parameters
    ----------

    aspectEngine : Optional[Qt3DCore.QAspectEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAspectJob::postFrame(QAspectEngine *aspectEngine)
    ritual = 'ritual_ZN8Qt3DCore10QAspectJob9postFrameEPNS_13QAspectEngineE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore10QAspectJob9postFrameEPNS_13QAspectEngine'
          'E')
    self.uglySide.call(ritual, self._addressOf(aspectEngine))

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QAspectJob::isRequired()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjob.html#isRequired
    """
    #  bool Qt3DCore::QAspectJob::isRequired()
    ritual = 'ritual_ZN8Qt3DCore10QAspectJob10isRequiredEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8Qt3DCore10QAspectJob10isRequiredEv'
    return self.uglySide.call(ritual)

  def d_func(self) -> Optional[Qt3DCore.QAspectJobPrivate]:
    """
    Calls Qt's 'QAspectJobPrivate *Qt3DCore::QAspectJob::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qaspectjob.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QAspectJobPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAspectJobPrivate *Qt3DCore::QAspectJob::d_func()
    address = self.uglySide.call('ritual_ZN8Qt3DCore10QAspectJob6d_funcEv')
    return Qt3DCore.QAspectJobPrivate._cuteAt(address)

  @staticmethod
  def addDependency(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QAspectJob::addDependency(QWeakPointer<QAspectJob>
    dependency)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAspectJob.addDependency' has no cute function yet. Qt's "
        "'void Qt3DCore::QAspectJob::addDependency(QWeakPointer<QAspectJob> "
        "dependency)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def dependencies(*__, **_) -> Never:
    """
    Qt's 'const std::vector<QWeakPointer<QAspectJob>>
    &Qt3DCore::QAspectJob::dependencies() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAspectJob.dependencies' has no cute function yet. Qt's "
        "'const std::vector<QWeakPointer<QAspectJob>> "
        "&Qt3DCore::QAspectJob::dependencies() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def removeDependency(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DCore::QAspectJob::removeDependency(QWeakPointer<QAspectJob>
    dependency)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAspectJob.removeDependency' has no cute function yet. "
        "Qt's 'void "
        "Qt3DCore::QAspectJob::removeDependency(QWeakPointer<QAspectJob> "
        "dependency)': takes a type Python has no way to hand over yet.")

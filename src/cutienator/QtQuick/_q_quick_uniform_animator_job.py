"""
QQuickUniformAnimatorJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickUniformAnimatorJob to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickAnimatorJob

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickUniformAnimatorJob(QQuickAnimatorJob):
  """
  The cute side of Qt's QQuickUniformAnimatorJob: a plain Python object
  standing in front of one C++ QQuickUniformAnimatorJob.

  It is built on the cute 'QQuickAnimatorJob', as Qt's
  QQuickUniformAnimatorJob is built on Qt's QQuickAnimatorJob, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickUniformAnimatorJob that has a ritual and that
  Python can call so far, 7 names in all: 'setTarget', 'setUniform',
  'uniform', 'updateCurrentTime', 'writeBack', 'postSync', 'invalidate'. It
  can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QQuickUniformAnimatorJob is created at the first use, not by
    'QQuickUniformAnimatorJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickUniformAnimatorJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickUniformAnimatorJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def uniform(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQuickUniformAnimatorJob::uniform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimatorjob.html#uniform

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQuickUniformAnimatorJob::uniform() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickUniformAnimatorJob7uniformEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setTarget(self, target: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickUniformAnimatorJob::setTarget(QQuickItem
    *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimatorjob.html#setTarget

    Parameters
    ----------

    target : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickUniformAnimatorJob::setTarget(QQuickItem *target)
    ritual = 'ritual_ZN24QQuickUniformAnimatorJob9setTargetEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickUniformAnimatorJob9setTargetEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(target))

  @overload(QByteArray)
  def setUniform(self, uniform: QByteArray) -> None:
    """
    Calls Qt's 'void QQuickUniformAnimatorJob::setUniform(const QByteArray
    &uniform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimatorjob.html#setUniform

    Parameters
    ----------

    uniform : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QQuickUniformAnimatorJob::setUniform(const QByteArray &uniform)
    self.uglySide.call(
        'ritual_ZN24QQuickUniformAnimatorJob10setUniformERK10QByteArray',
        self._valueOf(uniform),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickUniformAnimatorJob::QQuickUniformAnimatorJob()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimatorjob.html
    """
    #  QQuickUniformAnimatorJob::QQuickUniformAnimatorJob()
    self._noteCreation(QQuickUniformAnimatorJob, lambda: Rituals.call(
        'ritual_ZN24QQuickUniformAnimatorJobC1Ev',
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

  @overload(int)
  def updateCurrentTime(self, time: int) -> None:
    """
    Calls Qt's 'void QQuickUniformAnimatorJob::updateCurrentTime(int time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimatorjob.html#updateCurrentTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QQuickUniformAnimatorJob::updateCurrentTime(int time)
    ritual = 'ritual_ZN24QQuickUniformAnimatorJob17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickUniformAnimatorJob17updateCurrentTimeEi'
    self.uglySide.call(ritual, time)

  def writeBack(self) -> None:
    """
    Calls Qt's 'void QQuickUniformAnimatorJob::writeBack()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimatorjob.html#writeBack
    """
    #  void QQuickUniformAnimatorJob::writeBack()
    ritual = 'ritual_ZN24QQuickUniformAnimatorJob9writeBackEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickUniformAnimatorJob9writeBackEv'
    self.uglySide.call(ritual)

  def postSync(self) -> None:
    """
    Calls Qt's 'void QQuickUniformAnimatorJob::postSync()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimatorjob.html#postSync
    """
    #  void QQuickUniformAnimatorJob::postSync()
    ritual = 'ritual_ZN24QQuickUniformAnimatorJob8postSyncEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickUniformAnimatorJob8postSyncEv'
    self.uglySide.call(ritual)

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QQuickUniformAnimatorJob::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickuniformanimatorjob.html#invalidate
    """
    #  void QQuickUniformAnimatorJob::invalidate()
    ritual = 'ritual_ZN24QQuickUniformAnimatorJob10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickUniformAnimatorJob10invalidateEv'
    self.uglySide.call(ritual)

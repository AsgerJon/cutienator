"""
QQuickTransformAnimatorJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTransformAnimatorJob to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQuickAnimatorJob

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTransformAnimatorJob(QQuickAnimatorJob):
  """
  The cute side of Qt's QQuickTransformAnimatorJob: a plain Python object
  standing in front of one C++ QQuickTransformAnimatorJob.

  It is built on the cute 'QQuickAnimatorJob', as Qt's
  QQuickTransformAnimatorJob is built on Qt's QQuickAnimatorJob, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTransformAnimatorJob that has a ritual and
  that Python can call so far, 4 names in all: 'commit', 'preSync',
  'setTarget', 'invalidate'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QQuickTransformAnimatorJob.

  What to expect
  --------------

  - The C++ QQuickTransformAnimatorJob is created at the first use, not by
    'QQuickTransformAnimatorJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTransformAnimatorJob.
  - Each name of Qt's QQuickTransformAnimatorJob that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The classes Qt writes inside QQuickTransformAnimatorJob, each a class in
  #  here as in C++.

  class Helper(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickTransformAnimatorJob::Helper: a plain Python
    object standing in front of one C++ QQuickTransformAnimatorJob::Helper.

    C++ hands a QQuickTransformAnimatorJob::Helper around as a copy, so every
    C++ QQuickTransformAnimatorJob::Helper behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QQuickTransformAnimatorJob::Helper that has a
    ritual and that Python can call so far, 2 names in all: 'sync', 'commit'.
    It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickTransformAnimatorJob::Helper::~Helper()': the destructor:
      Python removes its C++ QQuickTransformAnimatorJob::Helper by it, and
      has no other use for it.

    What to expect
    --------------

    - The C++ QQuickTransformAnimatorJob::Helper is created at the first use,
      not by 'QQuickTransformAnimatorJob::Helper(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickTransformAnimatorJob::Helper back gives a
      copy the ritual made for Python, in a new cute
      QQuickTransformAnimatorJob::Helper.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickTransformAnimatorJob::Helper'

    #  Qt's '~QQuickTransformAnimatorJob::Helper()'. Naming it makes this a
    #  value class: Python owns every C++ QQuickTransformAnimatorJob::Helper
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN26QQuickTransformAnimatorJob6HelperD1Ev'

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
      'QQuickTransformAnimatorJob::Helper::Helper()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktransformanimatorjob-helper.html#Helper
      """
      #  QQuickTransformAnimatorJob::Helper::Helper()
      self._noteCreation(
          QQuickTransformAnimatorJob.Helper, lambda: Rituals.call(
              'ritual_ZN26QQuickTransformAnimatorJob6HelperC1Ev',
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

    def sync(self) -> None:
      """
      Calls Qt's 'void QQuickTransformAnimatorJob::Helper::sync()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktransformanimatorjob-helper.html#sync
      """
      #  void QQuickTransformAnimatorJob::Helper::sync()
      self.uglySide.call(
          'ritual_ZN26QQuickTransformAnimatorJob6Helper4syncEv',
      )

    def commit(self) -> None:
      """
      Calls Qt's 'void QQuickTransformAnimatorJob::Helper::commit()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquicktransformanimatorjob-helper.html#commit
      """
      #  void QQuickTransformAnimatorJob::Helper::commit()
      self.uglySide.call(
          'ritual_ZN26QQuickTransformAnimatorJob6Helper6commitEv',
      )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTransformAnimatorJob'

  #  A C++ QQuickTransformAnimatorJob Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTransformAnimatorJob'

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

  @overload(QQuickItem)
  @overload(NoneType)
  def setTarget(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickTransformAnimatorJob::setTarget(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransformanimatorjob.html#setTarget

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTransformAnimatorJob::setTarget(QQuickItem *item)
    ritual = 'ritual_ZN26QQuickTransformAnimatorJob9setTargetEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickTransformAnimatorJob9setTargetEP10QQuickIte'
          'm')
    self.uglySide.call(ritual, self._addressOf(item))

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
    Qt's 'QQuickTransformAnimatorJob::QQuickTransformAnimatorJob()': leans on
    'QQuickTransformAnimatorJob::preSync()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTransformAnimatorJob.__init__' has no cute function yet. "
        "Qt's 'QQuickTransformAnimatorJob::QQuickTransformAnimatorJob()': "
        "leans on 'QQuickTransformAnimatorJob::preSync()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def commit(self) -> None:
    """
    Calls Qt's 'void QQuickTransformAnimatorJob::commit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransformanimatorjob.html#commit
    """
    #  void QQuickTransformAnimatorJob::commit()
    ritual = 'ritual_ZN26QQuickTransformAnimatorJob6commitEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QQuickTransformAnimatorJob6commitEv'
    self.uglySide.call(ritual)

  def preSync(self) -> None:
    """
    Calls Qt's 'void QQuickTransformAnimatorJob::preSync()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransformanimatorjob.html#preSync
    """
    #  void QQuickTransformAnimatorJob::preSync()
    self.uglySide.call('ritual_ZN26QQuickTransformAnimatorJob7preSyncEv')

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QQuickTransformAnimatorJob::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransformanimatorjob.html#invalidate
    """
    #  void QQuickTransformAnimatorJob::invalidate()
    ritual = 'ritual_ZN26QQuickTransformAnimatorJob10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QQuickTransformAnimatorJob10invalidateEv'
    self.uglySide.call(ritual)

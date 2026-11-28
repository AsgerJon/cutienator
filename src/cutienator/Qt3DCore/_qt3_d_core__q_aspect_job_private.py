"""
Qt3DCore::QAspectJobPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qaspectjob_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DCore::QAspectJobPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAspectJobPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QAspectJobPrivate: a plain Python object
  standing in front of one C++ Qt3DCore::QAspectJobPrivate.

  C++ hands a Qt3DCore::QAspectJobPrivate around as a copy, so every C++
  Qt3DCore::QAspectJobPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAspectJobPrivate that has a ritual and
  that Python can call so far, 4 names in all: 'get', 'isRequired',
  'postFrame', 'clearDependencies'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QAspectJobPrivate::~QAspectJobPrivate()': the destructor:
    Python removes its C++ Qt3DCore::QAspectJobPrivate by it, and has no
    other use for it.

  What to expect
  --------------

  - The C++ Qt3DCore::QAspectJobPrivate is created at the first use, not by
    'Qt3DCore::QAspectJobPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DCore::QAspectJobPrivate back gives a copy the
    ritual made for Python, in a new cute Qt3DCore::QAspectJobPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.QAspectJob'])
  @overload(NoneType)
  def get(job: Optional[Qt3DCore.QAspectJob]) -> Optional[QAspectJobPrivate]:
    """
    Calls Qt's 'QAspectJobPrivate
    *Qt3DCore::QAspectJobPrivate::get(QAspectJob *job)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjobprivate.html#get

    Parameters
    ----------

    job : Optional[Qt3DCore.QAspectJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAspectJobPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAspectJobPrivate *Qt3DCore::QAspectJobPrivate::get(QAspectJob *job)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore17QAspectJobPrivate3getEPNS_10QAspectJobE',
        CuteMixin._addressOf(job),
    )
    return QAspectJobPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAspectJobPrivate'

  #  A C++ Qt3DCore::QAspectJobPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAspectJobPrivate'

  #  The functions Qt calls itself that Qt3DCore::QAspectJobPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'isRequired': (
          ('_ZNK8Qt3DCore17QAspectJobPrivate10isRequiredEv',
           ('bool', 'number', ''),
           ()),
      ),
      'postFrame': (
          ('_ZN8Qt3DCore17QAspectJobPrivate9postFrameEPNS_14QAspectManagerE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QAspectManager'),
           )),
      ),
  }

  #  Qt's '~Qt3DCore::QAspectJobPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ Qt3DCore::QAspectJobPrivate behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8Qt3DCore17QAspectJobPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QAspectJobPrivate::isRequired() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjobprivate.html#isRequired
    """
    #  bool Qt3DCore::QAspectJobPrivate::isRequired() const
    ritual = 'ritual_ZNK8Qt3DCore17QAspectJobPrivate10isRequiredEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8Qt3DCore17QAspectJobPrivate10isRequiredEv'
    return self.uglySide.call(ritual)

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
    'Qt3DCore::QAspectJobPrivate::QAspectJobPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjobprivate.html#QAspectJobPrivate
    """
    #  Qt3DCore::QAspectJobPrivate::QAspectJobPrivate()
    self._noteCreation(QAspectJobPrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore17QAspectJobPrivateC1Ev',
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

  @overload(WAIT['Qt3DCore.QAspectManager'])
  @overload(NoneType)
  def postFrame(
      self,
      aspectManager: Optional[Qt3DCore.QAspectManager],
  ) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectJobPrivate::postFrame(QAspectManager
    *aspectManager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjobprivate.html#postFrame

    Parameters
    ----------

    aspectManager : Optional[Qt3DCore.QAspectManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAspectJobPrivate::postFrame(QAspectManager
    #      *aspectManager)
    ritual = (
        'ritual_ZN8Qt3DCore17QAspectJobPrivate9postFrameEPNS_14QAspectManag'
        'erE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore17QAspectJobPrivate9postFrameEPNS_14QAspec'
          'tManagerE')
    self.uglySide.call(ritual, self._addressOf(aspectManager))

  def clearDependencies(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectJobPrivate::clearDependencies()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectjobprivate.html#clearDependencies
    """
    #  void Qt3DCore::QAspectJobPrivate::clearDependencies()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore17QAspectJobPrivate17clearDependenciesEv',
    )

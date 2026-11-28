"""
Qt3DRender::QAbstractRayCasterPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qabstractraycaster_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QAbstractRayCasterPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractRayCasterPrivate(Qt3DCore.QComponentPrivate):
  """
  The cute side of Qt's Qt3DRender::QAbstractRayCasterPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QAbstractRayCasterPrivate.

  It is built on the cute 'Qt3DCore::QComponentPrivate', as Qt's
  Qt3DRender::QAbstractRayCasterPrivate is built on Qt's
  Qt3DCore::QComponentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QAbstractRayCasterPrivate that has a
  ritual and that Python can call so far, 2 names in all: 'get', 'q_func'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractRayCasterPrivate
    *Qt3DRender::QAbstractRayCasterPrivate::get(const QAbstractRayCaster
    *obj)': takes in Python what 'QAbstractRayCasterPrivate
    *Qt3DRender::QAbstractRayCasterPrivate::get(QAbstractRayCaster *obj)'
    takes.
  - Qt's 'void Qt3DRender::QAbstractRayCasterPrivate::updateHitEntites(
    QAbstractRayCaster::Hits &hits, Qt3DCore::QScene *scene)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QAbstractRayCaster::Hits
    Qt3DRender::QAbstractRayCasterPrivate::pick()': gives a type Python has
    no way to take yet.
  - Qt's 'void Qt3DRender::QAbstractRayCasterPrivate::dispatchHits(const
    QAbstractRayCaster::Hits &hits)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QAbstractRayCaster
    *Qt3DRender::QAbstractRayCasterPrivate::q_func() const': takes in Python
    what 'QAbstractRayCaster
    *Qt3DRender::QAbstractRayCasterPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QAbstractRayCasterPrivate is created at the first
    use, not by 'Qt3DRender::QAbstractRayCasterPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QAbstractRayCasterPrivate.
  - Each name of Qt's Qt3DRender::QAbstractRayCasterPrivate that has no cute
    function yet, 'dispatchHits', 'pick', 'updateHitEntites', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::QAbstractRayCasterPrivate, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class RayCasterType(CuteNum):
    """
    The enum 'Qt3DRender::QAbstractRayCasterPrivate::RayCasterType' of Qt,
    with the 2 names Qt gives in it.
    """

    WorldSpaceRayCaster = Kee[int](0)
    ScreenScapeRayCaster = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DRender.QAbstractRayCaster'])
  @overload(NoneType)
  def get(
      obj: Optional[Qt3DRender.QAbstractRayCaster],
  ) -> Optional[QAbstractRayCasterPrivate]:
    """
    Calls Qt's 'QAbstractRayCasterPrivate
    *Qt3DRender::QAbstractRayCasterPrivate::get(QAbstractRayCaster *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycasterprivate.html#get

    Parameters
    ----------

    obj : Optional[Qt3DRender.QAbstractRayCaster]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractRayCasterPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractRayCasterPrivate
    #      *Qt3DRender::QAbstractRayCasterPrivate::get(QAbstractRayCaster
    #      *obj)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender25QAbstractRayCasterPrivate3getEPNS_18QAbstra'
        'ctRayCasterE',
        CuteMixin._addressOf(obj),
    )
    return QAbstractRayCasterPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QAbstractRayCasterPrivate'

  #  A C++ Qt3DRender::QAbstractRayCasterPrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QAbstractRayCasterPrivate'

  #  The functions Qt calls itself that Qt3DRender::QAbstractRayCasterPrivate
  #  is the first to declare and that cannot be handed to Python yet, each as
  #  Qt declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'dispatchHits': (
          'void Qt3DRender::QAbstractRayCasterPrivate::dispatchHits(const '
          'QAbstractRayCaster::Hits &)',
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
    Notes what was given, for Qt's
    'Qt3DRender::QAbstractRayCasterPrivate::QAbstractRayCasterPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycasterprivate.html
    """
    #  Qt3DRender::QAbstractRayCasterPrivate::QAbstractRayCasterPrivate()
    self._noteCreation(QAbstractRayCasterPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender25QAbstractRayCasterPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QAbstractRayCaster]:
    """
    Calls Qt's 'QAbstractRayCaster
    *Qt3DRender::QAbstractRayCasterPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractraycasterprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QAbstractRayCaster]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractRayCaster *Qt3DRender::QAbstractRayCasterPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender25QAbstractRayCasterPrivate6q_funcEv',
    )
    return Qt3DRender.QAbstractRayCaster._cuteAt(address)

  @staticmethod
  def dispatchHits(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QAbstractRayCasterPrivate::dispatchHits(const
    QAbstractRayCaster::Hits &hits)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAbstractRayCasterPrivate.dispatchHits' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::QAbstractRayCasterPrivate::dispatchHits(const "
        "QAbstractRayCaster::Hits &hits)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def pick(*__, **_) -> Never:
    """
    Qt's 'QAbstractRayCaster::Hits
    Qt3DRender::QAbstractRayCasterPrivate::pick()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAbstractRayCasterPrivate.pick' has no cute function "
        "yet. Qt's 'QAbstractRayCaster::Hits "
        "Qt3DRender::QAbstractRayCasterPrivate::pick()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def updateHitEntites(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QAbstractRayCasterPrivate::updateHitEntites(
    QAbstractRayCaster::Hits &hits, Qt3DCore::QScene *scene)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QAbstractRayCasterPrivate.updateHitEntites' has no "
        "cute function yet. Qt's 'void "
        "Qt3DRender::QAbstractRayCasterPrivate::updateHitEntites(QAbstractRa"
        "yCaster::Hits &hits, Qt3DCore::QScene *scene)': takes a type "
        "Python has no way to hand over yet.")

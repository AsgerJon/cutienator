"""
Qt3DCore::Quick::Quick3DEntityLoaderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dentityloader_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DCore::Quick::Quick3DEntityLoaderPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Quick3DEntityLoaderPrivate(Qt3DCore.QEntityPrivate):
  """
  The cute side of Qt's Qt3DCore::Quick::Quick3DEntityLoaderPrivate: a plain
  Python object standing in front of one C++
  Qt3DCore::Quick::Quick3DEntityLoaderPrivate.

  It is built on the cute 'Qt3DCore::QEntityPrivate', as Qt's
  Qt3DCore::Quick::Quick3DEntityLoaderPrivate is built on Qt's
  Qt3DCore::QEntityPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Quick::Quick3DEntityLoaderPrivate that has
  a ritual and that Python can call so far, 3 names in all: 'q_func',
  'setStatus', 'get'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const Quick3DEntityLoader
    *Qt3DCore::Quick::Quick3DEntityLoaderPrivate::q_func() const': takes in
    Python what 'Quick3DEntityLoader
    *Qt3DCore::Quick::Quick3DEntityLoaderPrivate::q_func()' takes.

  What has no ritual
  ------------------

  5 of the 10 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'Qt3DCore.

  What to expect
  --------------

  - The C++ Qt3DCore::Quick::Quick3DEntityLoaderPrivate is created at the
    first use, not by 'Qt3DCore::Quick::Quick3DEntityLoaderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::Quick::Quick3DEntityLoaderPrivate.
  - Each name of Qt's Qt3DCore::Quick::Quick3DEntityLoaderPrivate that has no
    cute function yet, '_q_componentStatusChanged', 'clear', 'loadComponent',
    'loadFromSource', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.Quick.Quick3DEntityLoader'])
  @overload(NoneType)
  def get(
      q: Optional[Qt3DCore.Quick.Quick3DEntityLoader],
  ) -> Optional[Quick3DEntityLoaderPrivate]:
    """
    Calls Qt's 'Quick3DEntityLoaderPrivate
    *Qt3DCore::Quick::Quick3DEntityLoaderPrivate::get(Quick3DEntityLoader
    *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloaderprivate.html#get

    Parameters
    ----------

    q : Optional[Qt3DCore.Quick.Quick3DEntityLoader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[Quick3DEntityLoaderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Quick3DEntityLoaderPrivate
    #      *Qt3DCore::Quick::Quick3DEntityLoaderPrivate::get(
    #      Quick3DEntityLoader *q)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore5Quick26Quick3DEntityLoaderPrivate3getEPNS0_19Qu'
        'ick3DEntityLoaderE',
        CuteMixin._addressOf(q),
    )
    return Quick3DEntityLoaderPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Quick::Quick3DEntityLoaderPrivate'

  #  A C++ Qt3DCore::Quick::Quick3DEntityLoaderPrivate Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_Quick_Quick3DEntityLoaderPrivate'

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

  @overload(Qt3DCore.Quick.Quick3DEntityLoader.Status)
  def setStatus(
      self,
      status: Qt3DCore.Quick.Quick3DEntityLoader.Status,
  ) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::Quick3DEntityLoaderPrivate::setStatus(
    Quick3DEntityLoader::Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloaderprivate.html

    Parameters
    ----------

    status : Qt3DCore.Quick.Quick3DEntityLoader.Status
      Passed on as its number.
    """
    #  void Qt3DCore::Quick::Quick3DEntityLoaderPrivate::setStatus(
    #      Quick3DEntityLoader::Status status)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26Quick3DEntityLoaderPrivate9setStatusENS0'
        '_19Quick3DEntityLoader6StatusE',
        status.value,
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
    'Qt3DCore::Quick::Quick3DEntityLoaderPrivate::Quick3DEntityLoaderPrivate(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloaderprivate.html
    """
    #  Qt3DCore::Quick::Quick3DEntityLoaderPrivate::
    #      Quick3DEntityLoaderPrivate()
    self._noteCreation(Quick3DEntityLoaderPrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore5Quick26Quick3DEntityLoaderPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DCore.Quick.Quick3DEntityLoader]:
    """
    Calls Qt's 'Quick3DEntityLoader
    *Qt3DCore::Quick::Quick3DEntityLoaderPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dentityloaderprivate.html

    Returns
    -------

    Optional[Qt3DCore.Quick.Quick3DEntityLoader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Quick3DEntityLoader
    #      *Qt3DCore::Quick::Quick3DEntityLoaderPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick26Quick3DEntityLoaderPrivate6q_funcEv',
    )
    return Qt3DCore.Quick.Quick3DEntityLoader._cuteAt(address)

  @staticmethod
  def _q_componentStatusChanged(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DCore::Quick::Quick3DEntityLoaderPrivate::_q_componentStatusChanged(
    QQmlComponent::Status status)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: use of
    undeclared identifier '_q_findQmlOwner'.
    """
    raise NotImplementedError(
        "'Qt3DCore.Quick.Quick3DEntityLoaderPrivate._q_componentStatusChange"
        "d' has no cute function yet. Qt's 'void "
        "Qt3DCore::Quick::Quick3DEntityLoaderPrivate::_q_componentStatusChan"
        "ged(QQmlComponent::Status status)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: use of undeclared identifier '_q_findQmlOwner'.")

  @staticmethod
  def clear(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::Quick::Quick3DEntityLoaderPrivate::clear()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'Quick3DEntityLoaderIncubator'.
    """
    raise NotImplementedError(
        "'Qt3DCore.Quick.Quick3DEntityLoaderPrivate.clear' has no cute "
        "function yet. Qt's 'void "
        "Qt3DCore::Quick::Quick3DEntityLoaderPrivate::clear()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'Quick3DEntityLoaderIncubator'.")

  @staticmethod
  def loadComponent(*__, **_) -> Never:
    """
    - Qt's 'void
      Qt3DCore::Quick::Quick3DEntityLoaderPrivate::loadComponent(const QUrl
      &source)': Qt's library has no name for it, and its code in Qt's source
      does not compile apart from its file: use of undeclared identifier
      '_q_findQmlOwner'.
    - Qt's 'void Qt3DCore::Quick::Quick3DEntityLoaderPrivate::loadComponent(
      QQmlComponent *component)': leans on
      'Qt3DCore::Quick::Quick3DEntityLoaderPrivate::
      _q_componentStatusChanged(QQmlComponent::Status)', which Qt's source
      does not mark for use from outside Qt and has no code for that could be
      taken.
    """
    raise NotImplementedError(
        "'Qt3DCore.Quick.Quick3DEntityLoaderPrivate.loadComponent' has no "
        "cute function yet. Qt's 'void "
        "Qt3DCore::Quick::Quick3DEntityLoaderPrivate::loadComponent(const "
        "QUrl &source)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier '_q_findQmlOwner'. Qt's 'void "
        "Qt3DCore::Quick::Quick3DEntityLoaderPrivate::loadComponent(QQmlComp"
        "onent *component)': leans on "
        "'Qt3DCore::Quick::Quick3DEntityLoaderPrivate::_q_componentStatusCha"
        "nged(QQmlComponent::Status)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def loadFromSource(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DCore::Quick::Quick3DEntityLoaderPrivate::loadFromSource()': leans on
    'Qt3DCore::Quick::Quick3DEntityLoaderPrivate::loadComponent(QUrl
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DCore.Quick.Quick3DEntityLoaderPrivate.loadFromSource' has no "
        "cute function yet. Qt's 'void "
        "Qt3DCore::Quick::Quick3DEntityLoaderPrivate::loadFromSource()': "
        "leans on "
        "'Qt3DCore::Quick::Quick3DEntityLoaderPrivate::loadComponent(QUrl "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

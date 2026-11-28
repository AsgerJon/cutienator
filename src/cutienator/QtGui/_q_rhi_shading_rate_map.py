"""
QRhiShadingRateMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QRhiResource

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QRhiImplementation, QRhiTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']
  QRhiTexture = WAIT['QRhiTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiShadingRateMap(QRhiResource):
  """
  The cute side of Qt's QRhiShadingRateMap: a plain Python object standing in
  front of one C++ QRhiShadingRateMap.

  It is built on the cute 'QRhiResource', as Qt's QRhiShadingRateMap is built
  on Qt's QRhiResource, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiShadingRateMap that has a ritual and that Python
  can call so far, 2 names in all: 'resourceType', 'createFrom'. It can be
  made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QRhiShadingRateMap is created at the first use, not by
    'QRhiShadingRateMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiShadingRateMap.
  """

  #  The classes Qt writes inside QRhiShadingRateMap, each a class in here as
  #  in C++.

  class NativeShadingRateMap(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QRhiShadingRateMap::NativeShadingRateMap: a plain
    Python object standing in front of one C++
    QRhiShadingRateMap::NativeShadingRateMap.

    C++ hands a QRhiShadingRateMap::NativeShadingRateMap around as a copy, so
    every C++ QRhiShadingRateMap::NativeShadingRateMap behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QRhiShadingRateMap::NativeShadingRateMap yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QRhiShadingRateMap::NativeShadingRateMap::~NativeShadingRateMap()':
      the destructor: Python removes its C++
      QRhiShadingRateMap::NativeShadingRateMap by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QRhiShadingRateMap::NativeShadingRateMap is created at the
      first use, not by 'QRhiShadingRateMap::NativeShadingRateMap(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QRhiShadingRateMap::NativeShadingRateMap back gives
      a copy the ritual made for Python, in a new cute
      QRhiShadingRateMap::NativeShadingRateMap.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QRhiShadingRateMap::NativeShadingRateMap'

    #  Qt's '~QRhiShadingRateMap::NativeShadingRateMap()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QRhiShadingRateMap::NativeShadingRateMap behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN18QRhiShadingRateMap20NativeShadingRateMapD1Ev')

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiShadingRateMap'

  #  A C++ QRhiShadingRateMap Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiShadingRateMap'

  #  The functions Qt calls itself that QRhiShadingRateMap is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createFrom': (
          ('_ZN18QRhiShadingRateMap10createFromENS_20NativeShadingRateMapE',
           ('bool', 'number', ''),
           (
               ('address', 'value',
                'QtGui:QRhiShadingRateMap.NativeShadingRateMap'),
           )),
          ('_ZN18QRhiShadingRateMap10createFromEP11QRhiTexture',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QRhiTexture'),
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

  def resourceType(self) -> QRhiResource.Type:
    """
    Calls Qt's 'QRhiResource::Type QRhiShadingRateMap::resourceType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishadingratemap.html#resourceType

    Returns
    -------

    QRhiResource.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiResource.Type(number)' gives.
    """
    #  QRhiResource::Type QRhiShadingRateMap::resourceType() const
    ritual = 'ritual_ZNK18QRhiShadingRateMap12resourceTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QRhiShadingRateMap12resourceTypeEv'
    return QRhiResource.Type(self.uglySide.call(ritual))

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

  @overload(QRhiImplementation)
  @overload(NoneType)
  def __init__(self, rhi: Optional[QRhiImplementation]) -> None:
    """
    Notes what was given, for Qt's
    'QRhiShadingRateMap::QRhiShadingRateMap(QRhiImplementation *rhi)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhishadingratemap.html#QRhiShadingRateMap

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiShadingRateMap::QRhiShadingRateMap(QRhiImplementation *rhi)
    self._noteCreation(QRhiShadingRateMap, lambda: Rituals.call(
        'ritual_ZN18QRhiShadingRateMapC1EP18QRhiImplementation',
        self._addressOf(rhi),
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

  @overload(NativeShadingRateMap)
  def createFrom(self, src: NativeShadingRateMap) -> bool:
    """
    Calls Qt's 'bool QRhiShadingRateMap::createFrom(NativeShadingRateMap
    src)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhishadingratemap.html#createFrom

    Parameters
    ----------

    src : NativeShadingRateMap
      Passed on as a value: Qt reads the C++
      QRhiShadingRateMap::NativeShadingRateMap, which stays Python's own.
    """
    #  bool QRhiShadingRateMap::createFrom(NativeShadingRateMap src)
    ritual = (
        'ritual_ZN18QRhiShadingRateMap10createFromENS_20NativeShadingRateMa'
        'pE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QRhiShadingRateMap10createFromENS_20NativeShading'
          'RateMapE')
    return self.uglySide.call(ritual, self._valueOf(src))

  @overload(QRhiTexture)
  @overload(NoneType)
  def createFrom(self, src: Optional[QRhiTexture]) -> bool:
    """
    Calls Qt's 'bool QRhiShadingRateMap::createFrom(QRhiTexture *src)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhishadingratemap.html#createFrom

    Parameters
    ----------

    src : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QRhiShadingRateMap::createFrom(QRhiTexture *src)
    ritual = 'ritual_ZN18QRhiShadingRateMap10createFromEP11QRhiTexture'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QRhiShadingRateMap10createFromEP11QRhiTexture'
    return self.uglySide.call(ritual, self._addressOf(src))

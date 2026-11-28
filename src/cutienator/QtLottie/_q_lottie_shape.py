"""
QLottieShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottieshape_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLottieShape to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QLottieBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QLottieTrimPath
  from ..QtCore import QJsonObject
  from ..QtGui import QPainterPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']
  QLottieTrimPath = WAIT['QLottieTrimPath']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieShape(QLottieBase):
  """
  The cute side of Qt's QLottieShape: a plain Python object standing in front
  of one C++ QLottieShape.

  It is built on the cute 'QLottieBase', as Qt's QLottieShape is built on
  Qt's QLottieBase, and has everything that class has.

  C++ hands a QLottieShape around as a copy, so every C++ QLottieShape behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieShape that has a ritual and that Python can
  call so far, 10 names in all: 'clone', 'construct', 'isAnimated', 'path',
  'acceptsTrim', 'applyTrim', 'currentTrim', 'fallbackPath', 'direction',
  'hasReversedDirection'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLottieShape::~QLottieShape()': the destructor: Python removes its
    C++ QLottieShape by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieShape is created at the first use, not by
    'QLottieShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieShape back gives a copy the ritual made for
    Python, in a new cute QLottieShape.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJsonObject)
  @overload(QJsonObject, QLottieBase)
  @overload(QJsonObject, NoneType)
  def construct(
      definition: QJsonObject,
      parent: Optional[QLottieBase] = None,
  ) -> Optional[QLottieShape]:
    """
    Calls Qt's 'QLottieShape *QLottieShape::construct(QJsonObject definition,
    QLottieBase *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshape.html#construct

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QLottieShape]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieShape *QLottieShape::construct(QJsonObject definition,
    #      QLottieBase *parent)
    address = Rituals.call(
        'ritual_ZN12QLottieShape9constructE11QJsonObjectP11QLottieBase',
        CuteMixin._valueOf(definition), CuteMixin._addressOf(parent),
    )
    return QLottieShape._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieShape'

  #  A C++ QLottieShape Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieShape'

  #  The functions Qt calls itself that QLottieShape is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'isAnimated': (
          ('_ZNK12QLottieShape10isAnimatedEv',
           ('bool', 'number', ''),
           ()),
      ),
      'path': (
          ('_ZNK12QLottieShape4pathEv',
           ('address', 'value', 'QtGui:QPainterPath'),
           ()),
      ),
      'acceptsTrim': (
          ('_ZNK12QLottieShape11acceptsTrimEv',
           ('bool', 'number', ''),
           ()),
      ),
      'applyTrim': (
          ('_ZN12QLottieShape9applyTrimERK15QLottieTrimPath',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLottie:QLottieTrimPath'),
           )),
      ),
      'fallbackPath': (
          ('_ZNK12QLottieShape12fallbackPathEv',
           ('address', 'value', 'QtGui:QPainterPath'),
           ()),
      ),
  }

  #  Qt's '~QLottieShape()'. Naming it makes this a value class: Python owns
  #  every C++ QLottieShape behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QLottieShapeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieShape::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshape.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieShape::clone() const
    ritual = 'ritual_ZNK12QLottieShape5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieShape5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def isAnimated(self) -> bool:
    """
    Calls Qt's 'bool QLottieShape::isAnimated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshape.html#isAnimated
    """
    #  bool QLottieShape::isAnimated() const
    ritual = 'ritual_ZNK12QLottieShape10isAnimatedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieShape10isAnimatedEv'
    return self.uglySide.call(ritual)

  def path(self) -> QPainterPath:
    """
    Calls Qt's 'const QPainterPath &QLottieShape::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshape.html#path

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  const QPainterPath &QLottieShape::path() const
    ritual = 'ritual_ZNK12QLottieShape4pathEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieShape4pathEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def acceptsTrim(self) -> bool:
    """
    Calls Qt's 'bool QLottieShape::acceptsTrim() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshape.html#acceptsTrim
    """
    #  bool QLottieShape::acceptsTrim() const
    ritual = 'ritual_ZNK12QLottieShape11acceptsTrimEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieShape11acceptsTrimEv'
    return self.uglySide.call(ritual)

  def currentTrim(self) -> Optional[QLottieTrimPath]:
    """
    Calls Qt's 'const QLottieTrimPath *QLottieShape::currentTrim() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshape.html#currentTrim

    Returns
    -------

    Optional[QLottieTrimPath]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QLottieTrimPath *QLottieShape::currentTrim() const
    address = self.uglySide.call('ritual_ZNK12QLottieShape11currentTrimEv')
    from . import QLottieTrimPath
    return QLottieTrimPath._cuteAt(address)

  def fallbackPath(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QLottieShape::fallbackPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshape.html#fallbackPath

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QLottieShape::fallbackPath() const
    ritual = 'ritual_ZNK12QLottieShape12fallbackPathEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieShape12fallbackPathEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def direction(self) -> int:
    """
    Calls Qt's 'int QLottieShape::direction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshape.html#direction
    """
    #  int QLottieShape::direction() const
    return self.uglySide.call('ritual_ZNK12QLottieShape9directionEv')

  def hasReversedDirection(self) -> bool:
    """
    Calls Qt's 'bool QLottieShape::hasReversedDirection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieshape.html#hasReversedDirection
    """
    #  bool QLottieShape::hasReversedDirection() const
    return self.uglySide.call(
        'ritual_ZNK12QLottieShape20hasReversedDirectionEv',
    )

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
    Notes what was given, for Qt's 'QLottieShape::QLottieShape()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshape.html#QLottieShape
    """
    #  QLottieShape::QLottieShape()
    self._noteCreation(QLottieShape, lambda: Rituals.call(
        'ritual_ZN12QLottieShapeC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLottieShape) -> None:
    """
    Notes what was given, for Qt's 'QLottieShape::QLottieShape(const
    QLottieShape &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshape.html#QLottieShape

    Parameters
    ----------

    other : QLottieShape
      Passed on as a value: Qt reads the C++ QLottieShape, which stays
      Python's own.
    """
    #  QLottieShape::QLottieShape(const QLottieShape &other)
    self._noteCreation(QLottieShape, lambda: Rituals.call(
        'ritual_ZN12QLottieShapeC1ERKS_', self._valueOf(other),
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

  @overload(QLottieTrimPath)
  def applyTrim(self, trimmer: QLottieTrimPath) -> None:
    """
    Calls Qt's 'void QLottieShape::applyTrim(const QLottieTrimPath
    &trimmer)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieshape.html#applyTrim

    Parameters
    ----------

    trimmer : QLottieTrimPath
      Passed on as a value: Qt reads the C++ QLottieTrimPath, which stays
      Python's own.
    """
    #  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
    ritual = 'ritual_ZN12QLottieShape9applyTrimERK15QLottieTrimPath'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLottieShape9applyTrimERK15QLottieTrimPath'
    self.uglySide.call(ritual, self._valueOf(trimmer))

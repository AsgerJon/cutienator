"""
QLottieGStroke binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottiegstroke_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottieGStroke to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLottieBase
  from ..QtCore import QJsonObject
  from ..QtGui import QPen
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']
  QLottieBase = WAIT['QLottieBase']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieGStroke(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLottieGStroke: a plain Python object standing in
  front of one C++ QLottieGStroke.

  C++ hands a QLottieGStroke around as a copy, so every C++ QLottieGStroke
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieGStroke that has a ritual and that Python can
  call so far, 4 names in all: 'clone', 'updateProperties', 'parse', 'pen'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieGStroke::render(QLottieRenderer &renderer) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QLottieGStroke::~QLottieGStroke()': the destructor: Python removes
    its C++ QLottieGStroke by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieGStroke is created at the first use, not by
    'QLottieGStroke(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieGStroke back gives a copy the ritual made for
    Python, in a new cute QLottieGStroke.
  - Each name of Qt's QLottieGStroke that has no cute function yet, 'render',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieGStroke'

  #  A C++ QLottieGStroke Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieGStroke'

  #  The functions Qt calls itself that QLottieGStroke is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'render': (
          'void QLottieGStroke::render(QLottieRenderer &) const',
      ),
  }

  #  The functions Qt calls itself that QLottieGStroke is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'clone': (
          ('_ZNK14QLottieGStroke5cloneEv',
           ('address', 'address', 'QtLottie:QLottieBase'),
           ()),
      ),
      'updateProperties': (
          ('_ZN14QLottieGStroke16updatePropertiesEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'parse': (
          ('_ZN14QLottieGStroke5parseERK11QJsonObject',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QJsonObject'),
           )),
      ),
      'pen': (
          ('_ZNK14QLottieGStroke3penEv',
           ('address', 'value', 'QtGui:QPen'),
           ()),
      ),
  }

  #  Qt's '~QLottieGStroke()'. Naming it makes this a value class: Python
  #  owns every C++ QLottieGStroke behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QLottieGStrokeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieGStroke::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegstroke.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieGStroke::clone() const
    ritual = 'ritual_ZNK14QLottieGStroke5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QLottieGStroke5cloneEv'
    address = self.uglySide.call(ritual)
    from . import QLottieBase
    return QLottieBase._cuteAt(address)

  def pen(self) -> QPen:
    """
    Calls Qt's 'QPen QLottieGStroke::pen() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegstroke.html#pen

    Returns
    -------

    QPen
      A new cute QPen around the copy Qt gave back. Python owns it.
    """
    #  QPen QLottieGStroke::pen() const
    ritual = 'ritual_ZNK14QLottieGStroke3penEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QLottieGStroke3penEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPen
    return QPen._cuteOwning(address)

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

  @overload(THIS)
  def __init__(self, other: QLottieGStroke) -> None:
    """
    Notes what was given, for Qt's 'QLottieGStroke::QLottieGStroke(const
    QLottieGStroke &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegstroke.html#QLottieGStroke

    Parameters
    ----------

    other : QLottieGStroke
      Passed on as a value: Qt reads the C++ QLottieGStroke, which stays
      Python's own.
    """
    #  QLottieGStroke::QLottieGStroke(const QLottieGStroke &other)
    self._noteCreation(QLottieGStroke, lambda: Rituals.call(
        'ritual_ZN14QLottieGStrokeC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's
    'QLottieGStroke::QLottieGStroke(QLottieBase *parent)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegstroke.html#QLottieGStroke

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieGStroke::QLottieGStroke(QLottieBase *parent)
    self._noteCreation(QLottieGStroke, lambda: Rituals.call(
        'ritual_ZN14QLottieGStrokeC1EP11QLottieBase',
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

  @overload(int)
  def updateProperties(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieGStroke::updateProperties(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottiegstroke.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieGStroke::updateProperties(int frame)
    ritual = 'ritual_ZN14QLottieGStroke16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QLottieGStroke16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieGStroke::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegstroke.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieGStroke::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN14QLottieGStroke5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QLottieGStroke5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @staticmethod
  def render(*__, **_) -> Never:
    """
    Qt's 'void QLottieGStroke::render(QLottieRenderer &renderer) const':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLottieGStroke.render' has no cute function yet. Qt's 'void "
        "QLottieGStroke::render(QLottieRenderer &renderer) const': takes a "
        "type Python has no way to hand over yet.")

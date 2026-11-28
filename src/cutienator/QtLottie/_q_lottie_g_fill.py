"""
QLottieGFill binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottiegfill_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QLottieGFill to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLottieBase
  from ..QtCore import QJsonObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']
  QLottieBase = WAIT['QLottieBase']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieGFill(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLottieGFill: a plain Python object standing in front
  of one C++ QLottieGFill.

  C++ hands a QLottieGFill around as a copy, so every C++ QLottieGFill behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieGFill that has a ritual and that Python can
  call so far, 4 names in all: 'clone', 'updateProperties', 'parse',
  'fillRule'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLottieGFill::~QLottieGFill()': the destructor: Python removes its
    C++ QLottieGFill by it, and has no other use for it.
  - Qt's 'void QLottieGFill::render(QLottieRenderer &renderer) const': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QLottieGFill is created at the first use, not by
    'QLottieGFill(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieGFill back gives a copy the ritual made for
    Python, in a new cute QLottieGFill.
  - Each name of Qt's QLottieGFill that has no cute function yet, 'opacity',
    'render', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QLottieGFill'

  #  A C++ QLottieGFill Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieGFill'

  #  The functions Qt calls itself that QLottieGFill is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'render': (
          'void QLottieGFill::render(QLottieRenderer &) const',
      ),
  }

  #  The functions Qt calls itself that QLottieGFill is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'clone': (
          ('_ZNK12QLottieGFill5cloneEv',
           ('address', 'address', 'QtLottie:QLottieBase'),
           ()),
      ),
      'updateProperties': (
          ('_ZN12QLottieGFill16updatePropertiesEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'parse': (
          ('_ZN12QLottieGFill5parseERK11QJsonObject',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QJsonObject'),
           )),
      ),
  }

  #  Qt's '~QLottieGFill()'. Naming it makes this a value class: Python owns
  #  every C++ QLottieGFill behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QLottieGFillD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieGFill::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegfill.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieGFill::clone() const
    ritual = 'ritual_ZNK12QLottieGFill5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QLottieGFill5cloneEv'
    address = self.uglySide.call(ritual)
    from . import QLottieBase
    return QLottieBase._cuteAt(address)

  def fillRule(self) -> Qt.FillRule:
    """
    Calls Qt's 'Qt::FillRule QLottieGFill::fillRule() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegfill.html#fillRule

    Returns
    -------

    Qt.FillRule
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FillRule(number)'
      gives.
    """
    #  Qt::FillRule QLottieGFill::fillRule() const
    return Qt.FillRule(self.uglySide.call(
        'ritual_ZNK12QLottieGFill8fillRuleEv',
    ))

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
  def __init__(self, other: QLottieGFill) -> None:
    """
    Notes what was given, for Qt's 'QLottieGFill::QLottieGFill(const
    QLottieGFill &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegfill.html#QLottieGFill

    Parameters
    ----------

    other : QLottieGFill
      Passed on as a value: Qt reads the C++ QLottieGFill, which stays
      Python's own.
    """
    #  QLottieGFill::QLottieGFill(const QLottieGFill &other)
    self._noteCreation(QLottieGFill, lambda: Rituals.call(
        'ritual_ZN12QLottieGFillC1ERKS_', self._valueOf(other),
    ))

  @overload()
  @overload(QLottieBase)
  @overload(NoneType)
  def __init__(self, parent: Optional[QLottieBase] = None) -> None:
    """
    Notes what was given, for Qt's 'QLottieGFill::QLottieGFill(QLottieBase
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegfill.html#QLottieGFill

    Parameters
    ----------

    parent : Optional[QLottieBase]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieGFill::QLottieGFill(QLottieBase *parent)
    self._noteCreation(QLottieGFill, lambda: Rituals.call(
        'ritual_ZN12QLottieGFillC1EP11QLottieBase', self._addressOf(parent),
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
    Calls Qt's 'void QLottieGFill::updateProperties(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegfill.html#updateProperties

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieGFill::updateProperties(int frame)
    ritual = 'ritual_ZN12QLottieGFill16updatePropertiesEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLottieGFill16updatePropertiesEi'
    self.uglySide.call(ritual, frame)

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieGFill::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottiegfill.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieGFill::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN12QLottieGFill5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QLottieGFill5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

  @staticmethod
  def opacity(*__, **_) -> Never:
    """
    Qt's 'qreal QLottieGFill::opacity() const': cannot be called and cannot
    be called through the meta-object and cannot be copied: no header file
    has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QLottieGFill.opacity' has no cute function yet. Qt's 'qreal "
        "QLottieGFill::opacity() const': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def render(*__, **_) -> Never:
    """
    Qt's 'void QLottieGFill::render(QLottieRenderer &renderer) const': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QLottieGFill.render' has no cute function yet. Qt's 'void "
        "QLottieGFill::render(QLottieRenderer &renderer) const': takes a "
        "type Python has no way to hand over yet.")

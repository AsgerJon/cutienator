"""
QLottiePrecomposition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottieprecomposition_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QLottiePrecomposition to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QLottieBase
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QJsonObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']


class QLottiePrecomposition(QLottieBase):
  """
  The cute side of Qt's QLottiePrecomposition: a plain Python object standing
  in front of one C++ QLottiePrecomposition.

  It is built on the cute 'QLottieBase', as Qt's QLottiePrecomposition is
  built on Qt's QLottieBase, and has everything that class has.

  C++ hands a QLottiePrecomposition around as a copy, so every C++
  QLottiePrecomposition behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottiePrecomposition that has a ritual and that
  Python can call so far, 4 names in all: 'clone', 'construct', 'parse',
  'refId'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottiePrecomposition::render(QLottieRenderer &renderer)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QLottiePrecomposition::~QLottiePrecomposition()': the destructor:
    Python removes its C++ QLottiePrecomposition by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QLottiePrecomposition is created at the first use, not by
    'QLottiePrecomposition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottiePrecomposition back gives a copy the ritual
    made for Python, in a new cute QLottiePrecomposition.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QJsonObject, QMap[str, QJsonObject])
  def construct(
      definition: QJsonObject,
      assets: QMap[str, QJsonObject],
  ) -> Optional[QLottiePrecomposition]:
    """
    Calls Qt's 'QLottiePrecomposition *QLottiePrecomposition::construct(const
    QJsonObject &definition, const QMap<QString, QJsonObject> &assets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieprecomposition.html#construct

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.

    assets : QMap[str, QJsonObject]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    Returns
    -------

    Optional[QLottiePrecomposition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottiePrecomposition *QLottiePrecomposition::construct(const
    #      QJsonObject &definition, const QMap<QString, QJsonObject> &assets)
    address = Rituals.call(
        'ritual_ZN21QLottiePrecomposition9constructERK11QJsonObjectRK4QMapI'
        '7QStringS0_E',
        CuteMixin._valueOf(definition), CuteMixin._valueOf(assets),
    )
    return QLottiePrecomposition._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottiePrecomposition'

  #  A C++ QLottiePrecomposition Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottiePrecomposition'

  #  Qt's '~QLottiePrecomposition()'. Naming it makes this a value class:
  #  Python owns every C++ QLottiePrecomposition behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QLottiePrecompositionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottiePrecomposition::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieprecomposition.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottiePrecomposition::clone() const
    ritual = 'ritual_ZNK21QLottiePrecomposition5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QLottiePrecomposition5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def refId(self) -> str:
    """
    Calls Qt's 'QString QLottiePrecomposition::refId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieprecomposition.html#refId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLottiePrecomposition::refId() const
    return self.uglySide.call('ritual_ZNK21QLottiePrecomposition5refIdEv')

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
    'QLottiePrecomposition::QLottiePrecomposition()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieprecomposition.html#QLottiePrecomposition
    """
    #  QLottiePrecomposition::QLottiePrecomposition()
    self._noteCreation(QLottiePrecomposition, lambda: Rituals.call(
        'ritual_ZN21QLottiePrecompositionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLottiePrecomposition) -> None:
    """
    Notes what was given, for Qt's
    'QLottiePrecomposition::QLottiePrecomposition(const QLottiePrecomposition
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieprecomposition.html#QLottiePrecomposition

    Parameters
    ----------

    other : QLottiePrecomposition
      Passed on as a value: Qt reads the C++ QLottiePrecomposition, which
      stays Python's own.
    """
    #  QLottiePrecomposition::QLottiePrecomposition(const
    #      QLottiePrecomposition &other)
    self._noteCreation(QLottiePrecomposition, lambda: Rituals.call(
        'ritual_ZN21QLottiePrecompositionC1ERKS_', self._valueOf(other),
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

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottiePrecomposition::parse(const QJsonObject
    &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieprecomposition.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottiePrecomposition::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN21QLottiePrecomposition5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QLottiePrecomposition5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))


#  Qt's 'QMap<QString, QLottiePrecomposition *>': the QMap from text to
#  QLottiePrecomposition, which 'QMap[str, QLottiePrecomposition]' gives. It
#  is completed here, in the file of the class of its values.
QMap.createKind(
    str, QLottiePrecomposition, 'address',
    make='ritual_map_make_QMap_QString_QLottiePrecomposition_ptr',
    put='ritual_map_put_QMap_QString_QLottiePrecomposition_ptr',
    size='ritual_map_size_QMap_QString_QLottiePrecomposition_ptr',
    key='ritual_map_key_QMap_QString_QLottiePrecomposition_ptr',
    value='ritual_map_value_QMap_QString_QLottiePrecomposition_ptr',
    has='ritual_map_has_QMap_QString_QLottiePrecomposition_ptr',
    get='ritual_map_get_QMap_QString_QLottiePrecomposition_ptr',
    drop='ritual_map_drop_QMap_QString_QLottiePrecomposition_ptr',
)

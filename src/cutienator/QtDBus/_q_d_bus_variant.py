"""
QDBusVariant binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusextratypes.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QDBusVariant(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusVariant: a plain Python object standing in front
  of one C++ QDBusVariant.

  C++ hands a QDBusVariant around as a copy, so every C++ QDBusVariant behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusVariant that has a ritual and that Python can
  call so far, 2 names in all: 'setVariant', 'variant'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusVariant::QDBusVariant(QVariant &&v)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QDBusVariant::swap(QDBusVariant &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QDBusVariant::~QDBusVariant()': the destructor: Python removes its
    C++ QDBusVariant by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QDBusVariant is created at the first use, not by
    'QDBusVariant(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusVariant back gives a copy the ritual made for
    Python, in a new cute QDBusVariant.
  - Each name of Qt's QDBusVariant that has no cute function yet, 'swap',
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
  __qt_class__ = 'QDBusVariant'

  #  Qt's '~QDBusVariant()'. Naming it makes this a value class: Python owns
  #  every C++ QDBusVariant behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QDBusVariantD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def variant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QDBusVariant::variant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusvariant.html#variant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDBusVariant::variant() const
    address = self.uglySide.call('ritual_ZNK12QDBusVariant7variantEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setVariant(self, variant: QVariant) -> None:
    """
    Calls Qt's 'void QDBusVariant::setVariant(const QVariant &variant)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusvariant.html#setVariant

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDBusVariant::setVariant(const QVariant &variant)
    self.uglySide.call(
        'ritual_ZN12QDBusVariant10setVariantERK8QVariant',
        self._valueOf(variant),
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
    Notes what was given, for Qt's 'QDBusVariant::QDBusVariant()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbusvariant.html#QDBusVariant
    """
    #  QDBusVariant::QDBusVariant()
    self._noteCreation(QDBusVariant, lambda: Rituals.call(
        'ritual_ZN12QDBusVariantC1Ev',
    ))

  @overload(QVariant)
  def __init__(self, variant: QVariant) -> None:
    """
    Notes what was given, for Qt's 'QDBusVariant::QDBusVariant(const QVariant
    &variant)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbusvariant.html#QDBusVariant

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  QDBusVariant::QDBusVariant(const QVariant &variant)
    self._noteCreation(QDBusVariant, lambda: Rituals.call(
        'ritual_ZN12QDBusVariantC1ERK8QVariant', self._valueOf(variant),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QDBusVariant::swap(QDBusVariant &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusVariant.swap' has no cute function yet. Qt's 'void "
        "QDBusVariant::swap(QDBusVariant &other)': takes a type Python has "
        "no way to hand over yet.")


#  Qt's 'QMap<QString, QDBusVariant>': the QMap from text to QDBusVariant,
#  which 'QMap[str, QDBusVariant]' gives. It is completed here, in the file
#  of the class of its values. Qt has a name of its own for it.
ServiceDataList = QMap.createKind(
    str, QDBusVariant, 'value',
    name='ServiceDataList',
    make='ritual_map_make_QMap_QString_QDBusVariant',
    put='ritual_map_put_QMap_QString_QDBusVariant',
    size='ritual_map_size_QMap_QString_QDBusVariant',
    key='ritual_map_key_QMap_QString_QDBusVariant',
    value='ritual_map_value_QMap_QString_QDBusVariant',
    has='ritual_map_has_QMap_QString_QDBusVariant',
    get='ritual_map_get_QMap_QString_QDBusVariant',
    drop='ritual_map_drop_QMap_QString_QDBusVariant',
)

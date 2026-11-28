"""
qdesigner_internal::PropertySheetIconValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PropertySheetIconValue to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QIcon
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class PropertySheetIconValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::PropertySheetIconValue: a plain
  Python object standing in front of one C++
  qdesigner_internal::PropertySheetIconValue.

  C++ hands a qdesigner_internal::PropertySheetIconValue around as a copy, so
  every C++ qdesigner_internal::PropertySheetIconValue behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::PropertySheetIconValue that has
  a ritual and that Python can call so far, 14 names in all: 'isEmpty',
  'theme', 'setTheme', 'themeEnum', 'setThemeEnum', 'pixmap', 'setPixmap',
  'mask', 'compare', 'assign', 'themed', 'unthemed', '__eq__', '__ne__'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'qdesigner_internal::PropertySheetIconValue::~PropertySheetIconValue()':
    the destructor: Python removes its C++
    qdesigner_internal::PropertySheetIconValue by it, and has no other use
    for it.
  - Qt's 'PropertySheetIconValue
    &qdesigner_internal::PropertySheetIconValue::operator=(const
    PropertySheetIconValue &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'qdesigner_internal::PropertySheetIconValue::PropertySheetIconValue(
    PropertySheetIconValue &&a0)': takes a type Python has no way to hand
    over yet.
  - Qt's 'PropertySheetIconValue
    &qdesigner_internal::PropertySheetIconValue::operator=(
    PropertySheetIconValue &&a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'const ModeStateToPixmapMap
    &qdesigner_internal::PropertySheetIconValue::paths() const': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ qdesigner_internal::PropertySheetIconValue is created at the
    first use, not by 'qdesigner_internal::PropertySheetIconValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::PropertySheetIconValue back gives
    a copy the ritual made for Python, in a new cute
    qdesigner_internal::PropertySheetIconValue.
  - Each name of Qt's qdesigner_internal::PropertySheetIconValue that has no
    cute function yet, 'paths', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::PropertySheetIconValue'

  #  Qt's '~qdesigner_internal::PropertySheetIconValue()'. Naming it makes
  #  this a value class: Python owns every C++
  #  qdesigner_internal::PropertySheetIconValue behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN18qdesigner_internal22PropertySheetIconValueD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::PropertySheetIconValue::isEmpty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html
    """
    #  bool qdesigner_internal::PropertySheetIconValue::isEmpty() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22PropertySheetIconValue7isEmptyEv',
    )

  def theme(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::PropertySheetIconValue::theme()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::PropertySheetIconValue::theme() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22PropertySheetIconValue5themeEv',
    )

  def themeEnum(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::PropertySheetIconValue::themeEnum()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html
    """
    #  int qdesigner_internal::PropertySheetIconValue::themeEnum() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22PropertySheetIconValue9themeEnumEv',
    )

  @overload(QIcon.Mode, QIcon.State)
  def pixmap(
      self,
      mode: QIcon.Mode,
      state: QIcon.State,
  ) -> qdesigner_internal.PropertySheetPixmapValue:
    """
    Calls Qt's 'PropertySheetPixmapValue
    qdesigner_internal::PropertySheetIconValue::pixmap(QIcon::Mode mode,
    QIcon::State state) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html

    Parameters
    ----------

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.

    Returns
    -------

    qdesigner_internal.PropertySheetPixmapValue
      A new cute qdesigner_internal::PropertySheetPixmapValue around the copy
      Qt gave back. Python owns it.
    """
    #  PropertySheetPixmapValue
    #      qdesigner_internal::PropertySheetIconValue::pixmap(QIcon::Mode
    #      mode, QIcon::State state) const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22PropertySheetIconValue6pixmapEN5QI'
        'con4ModeENS1_5StateE',
        mode.value, state.value,
    )
    return qdesigner_internal.PropertySheetPixmapValue._cuteOwning(address)

  def mask(self) -> int:
    """
    Calls Qt's 'uint qdesigner_internal::PropertySheetIconValue::mask()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html
    """
    #  uint qdesigner_internal::PropertySheetIconValue::mask() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22PropertySheetIconValue4maskEv',
    )

  @overload(THIS)
  def compare(self, other: PropertySheetIconValue) -> int:
    """
    Calls Qt's 'uint
    qdesigner_internal::PropertySheetIconValue::compare(const
    PropertySheetIconValue &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html

    Parameters
    ----------

    other : PropertySheetIconValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetIconValue, which stays Python's own.
    """
    #  uint qdesigner_internal::PropertySheetIconValue::compare(const
    #      PropertySheetIconValue &other) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22PropertySheetIconValue7compareERKS'
        '0_',
        self._valueOf(other),
    )

  def themed(self) -> PropertySheetIconValue:
    """
    Calls Qt's 'PropertySheetIconValue
    qdesigner_internal::PropertySheetIconValue::themed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html

    Returns
    -------

    PropertySheetIconValue
      A new cute qdesigner_internal::PropertySheetIconValue around the copy
      Qt gave back. Python owns it.
    """
    #  PropertySheetIconValue
    #      qdesigner_internal::PropertySheetIconValue::themed() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22PropertySheetIconValue6themedEv',
    )
    return PropertySheetIconValue._cuteOwning(address)

  def unthemed(self) -> PropertySheetIconValue:
    """
    Calls Qt's 'PropertySheetIconValue
    qdesigner_internal::PropertySheetIconValue::unthemed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html

    Returns
    -------

    PropertySheetIconValue
      A new cute qdesigner_internal::PropertySheetIconValue around the copy
      Qt gave back. Python owns it.
    """
    #  PropertySheetIconValue
    #      qdesigner_internal::PropertySheetIconValue::unthemed() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal22PropertySheetIconValue8unthemedEv',
    )
    return PropertySheetIconValue._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTheme(self, a0: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PropertySheetIconValue::setTheme(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PropertySheetIconValue::setTheme(const
    #      QString &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22PropertySheetIconValue8setThemeERK7'
        'QString',
        a0,
    )

  @overload(int)
  def setThemeEnum(self, e: int) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PropertySheetIconValue::setThemeEnum(int e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html

    Parameters
    ----------

    e : int
      Passed on as it is.
    """
    #  void qdesigner_internal::PropertySheetIconValue::setThemeEnum(int e)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22PropertySheetIconValue12setThemeEnu'
        'mEi',
        e,
    )

  @overload(
      QIcon.Mode, QIcon.State,
      WAIT['qdesigner_internal.PropertySheetPixmapValue'],
  )
  def setPixmap(
      self,
      mode: QIcon.Mode,
      state: QIcon.State,
      path: qdesigner_internal.PropertySheetPixmapValue,
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PropertySheetIconValue::setPixmap(QIcon::Mode mode,
    QIcon::State state, const PropertySheetPixmapValue &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html

    Parameters
    ----------

    mode : QIcon.Mode
      Passed on as its number.

    state : QIcon.State
      Passed on as its number.

    path : qdesigner_internal.PropertySheetPixmapValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetPixmapValue, which stays Python's own.
    """
    #  void qdesigner_internal::PropertySheetIconValue::setPixmap(QIcon::Mode
    #      mode, QIcon::State state, const PropertySheetPixmapValue &path)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22PropertySheetIconValue9setPixmapEN5'
        'QIcon4ModeENS1_5StateERKNS_24PropertySheetPixmapValueE',
        mode.value, state.value, self._valueOf(path),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: PropertySheetIconValue) -> bool:
    """
    Calls Qt's 'bool operator==(const PropertySheetIconValue &lhs, const
    PropertySheetIconValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html

    Parameters
    ----------

    rhs : PropertySheetIconValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetIconValue, which stays Python's own.
    """
    #  bool operator==(const PropertySheetIconValue &lhs, const
    #      PropertySheetIconValue &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_22PropertySheetIconValueES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: PropertySheetIconValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const PropertySheetIconValue &lhs, const
    PropertySheetIconValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html

    Parameters
    ----------

    rhs : PropertySheetIconValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetIconValue, which stays Python's own.
    """
    #  bool operator!=(const PropertySheetIconValue &lhs, const
    #      PropertySheetIconValue &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_22PropertySheetIconValueES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['qdesigner_internal.PropertySheetPixmapValue'])
  def __init__(
      self,
      pixmap: qdesigner_internal.PropertySheetPixmapValue,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PropertySheetIconValue::PropertySheetIconValue(const
    PropertySheetPixmapValue &pixmap)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html

    Parameters
    ----------

    pixmap : qdesigner_internal.PropertySheetPixmapValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetPixmapValue, which stays Python's own.
    """
    #  qdesigner_internal::PropertySheetIconValue::
    #      PropertySheetIconValue(const PropertySheetPixmapValue &pixmap)
    self._noteCreation(PropertySheetIconValue, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal22PropertySheetIconValueC1ERKNS_24Pro'
        'pertySheetPixmapValueE',
        self._valueOf(pixmap),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PropertySheetIconValue::PropertySheetIconValue()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html
    """
    #  qdesigner_internal::PropertySheetIconValue::PropertySheetIconValue()
    self._noteCreation(PropertySheetIconValue, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal22PropertySheetIconValueC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: PropertySheetIconValue) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PropertySheetIconValue::PropertySheetIconValue(const
    PropertySheetIconValue &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html

    Parameters
    ----------

    a0 : PropertySheetIconValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetIconValue, which stays Python's own.
    """
    #  qdesigner_internal::PropertySheetIconValue::
    #      PropertySheetIconValue(const PropertySheetIconValue &a0)
    self._noteCreation(PropertySheetIconValue, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal22PropertySheetIconValueC1ERKS0_',
        self._valueOf(a0),
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

  @overload(THIS, int)
  def assign(self, other: PropertySheetIconValue, mask: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::PropertySheetIconValue::assign(const
    PropertySheetIconValue &other, uint mask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheeticonvalue.html

    Parameters
    ----------

    other : PropertySheetIconValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetIconValue, which stays Python's own.

    mask : int
      Passed on as it is.
    """
    #  void qdesigner_internal::PropertySheetIconValue::assign(const
    #      PropertySheetIconValue &other, uint mask)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal22PropertySheetIconValue6assignERKS0_'
        'j',
        self._valueOf(other), mask,
    )

  @staticmethod
  def paths(*__, **_) -> Never:
    """
    Qt's 'const ModeStateToPixmapMap
    &qdesigner_internal::PropertySheetIconValue::paths() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.PropertySheetIconValue.paths' has no cute "
        "function yet. Qt's 'const ModeStateToPixmapMap "
        "&qdesigner_internal::PropertySheetIconValue::paths() const': gives "
        "a type Python has no way to take yet.")

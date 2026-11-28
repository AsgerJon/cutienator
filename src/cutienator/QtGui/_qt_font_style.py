"""
QtFontStyle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfontdatabase_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QtFontStyle to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QtFontSize


class QtFontStyle(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtFontStyle: a plain Python object standing in front
  of one C++ QtFontStyle.

  C++ hands a QtFontStyle around as a copy, so every C++ QtFontStyle behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtFontStyle that has a ritual and that Python can
  call so far, 1 name in all: 'pixelSize'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtFontStyle::~QtFontStyle()': the destructor: Python removes its
    C++ QtFontStyle by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtFontStyle is created at the first use, not by
    'QtFontStyle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtFontStyle back gives a copy the ritual made for
    Python, in a new cute QtFontStyle.
  """

  #  The classes Qt writes inside QtFontStyle, each a class in here as in
  #  C++.

  class Key(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QtFontStyle::Key: a plain Python object standing in
    front of one C++ QtFontStyle::Key.

    C++ hands a QtFontStyle::Key around as a copy, so every C++
    QtFontStyle::Key behind a cute one is Python's own: it is removed, by the
    ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QtFontStyle::Key that has a ritual and that Python
    can call so far, 2 names in all: '__eq__', '__ne__'. It can be made from
    Python, in 3 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QtFontStyle::Key::~Key()': the destructor: Python removes its C++
      QtFontStyle::Key by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QtFontStyle::Key is created at the first use, not by
      'QtFontStyle::Key(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QtFontStyle::Key back gives a copy the ritual made
      for Python, in a new cute QtFontStyle::Key.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QtFontStyle::Key'

    #  Qt's '~QtFontStyle::Key()'. Naming it makes this a value class: Python
    #  owns every C++ QtFontStyle::Key behind a cute one, and removes it by
    #  this ritual.
    __delete_ritual__ = 'ritual_ZN11QtFontStyle3KeyD1Ev'

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

    @overload(THIS)
    def __eq__(self, other: QtFontStyle.Key) -> bool:
      """
      Calls Qt's 'bool QtFontStyle::Key::operator==(const Key &other) const'.

      Qt's own words: https://doc.qt.io/qt-6/qtfontstyle-key.html#operator==

      Parameters
      ----------

      other : QtFontStyle.Key
        Passed on as a value: Qt reads the C++ QtFontStyle::Key, which stays
        Python's own.
      """
      #  bool QtFontStyle::Key::operator==(const Key &other) const
      return self.uglySide.call(
          'ritual_ZNK11QtFontStyle3KeyeqERKS0_', self._valueOf(other),
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
    def __ne__(self, other: QtFontStyle.Key) -> bool:
      """
      Calls Qt's 'bool QtFontStyle::Key::operator!=(const Key &other) const'.

      Qt's own words: https://doc.qt.io/qt-6/qtfontstyle-key.html#operator!=

      Parameters
      ----------

      other : QtFontStyle.Key
        Passed on as a value: Qt reads the C++ QtFontStyle::Key, which stays
        Python's own.
      """
      #  bool QtFontStyle::Key::operator!=(const Key &other) const
      return self.uglySide.call(
          'ritual_ZNK11QtFontStyle3KeyneERKS0_', self._valueOf(other),
      )

    @overload.fallback
    def __ne__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(str)
    def __init__(self, styleString: str) -> None:
      """
      Notes what was given, for Qt's 'QtFontStyle::Key::Key(const QString
      &styleString)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qtfontstyle-key.html#Key

      Parameters
      ----------

      styleString : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  QtFontStyle::Key::Key(const QString &styleString)
      self._noteCreation(QtFontStyle.Key, lambda: Rituals.call(
          'ritual_ZN11QtFontStyle3KeyC1ERK7QString', styleString,
      ))

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QtFontStyle::Key::Key()', which is
      called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qtfontstyle-key.html#Key
      """
      #  QtFontStyle::Key::Key()
      self._noteCreation(QtFontStyle.Key, lambda: Rituals.call(
          'ritual_ZN11QtFontStyle3KeyC1Ev',
      ))

    @overload(THIS)
    def __init__(self, o: QtFontStyle.Key) -> None:
      """
      Notes what was given, for Qt's 'QtFontStyle::Key::Key(const Key &o)',
      which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qtfontstyle-key.html#Key

      Parameters
      ----------

      o : QtFontStyle.Key
        Passed on as a value: Qt reads the C++ QtFontStyle::Key, which stays
        Python's own.
      """
      #  QtFontStyle::Key::Key(const Key &o)
      self._noteCreation(QtFontStyle.Key, lambda: Rituals.call(
          'ritual_ZN11QtFontStyle3KeyC1ERKS0_', self._valueOf(o),
      ))

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
  __qt_class__ = 'QtFontStyle'

  #  Qt's '~QtFontStyle()'. Naming it makes this a value class: Python owns
  #  every C++ QtFontStyle behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QtFontStyleD1Ev'

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

  @overload(Key)
  def __init__(self, k: Key) -> None:
    """
    Notes what was given, for Qt's 'QtFontStyle::QtFontStyle(const Key &k)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtfontstyle.html#QtFontStyle

    Parameters
    ----------

    k : Key
      Passed on as a value: Qt reads the C++ QtFontStyle::Key, which stays
      Python's own.
    """
    #  QtFontStyle::QtFontStyle(const Key &k)
    self._noteCreation(QtFontStyle, lambda: Rituals.call(
        'ritual_ZN11QtFontStyleC1ERKNS_3KeyE', self._valueOf(k),
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
  @overload(int, bool)
  def pixelSize(self, size: int, a1: bool = False) -> Optional[QtFontSize]:
    """
    Calls Qt's 'QtFontSize *QtFontStyle::pixelSize(unsigned short size, bool
    a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qtfontstyle.html#pixelSize

    Parameters
    ----------

    size : int
      Passed on as it is.

    a1 : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    Optional[QtFontSize]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QtFontSize *QtFontStyle::pixelSize(unsigned short size, bool a1)
    address = self.uglySide.call(
        'ritual_ZN11QtFontStyle9pixelSizeEtb', size, a1,
    )
    from . import QtFontSize
    return QtFontSize._cuteAt(address)

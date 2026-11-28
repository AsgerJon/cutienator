"""
QQuickAbstractPaletteProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickabstractpaletteprovider_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickAbstractPaletteProvider to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QPalette
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPalette = WAIT['QPalette']


class QQuickAbstractPaletteProvider(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickAbstractPaletteProvider: a plain Python object
  standing in front of one C++ QQuickAbstractPaletteProvider.

  What exists
  -----------

  Every function of Qt's QQuickAbstractPaletteProvider that has a ritual and
  that Python can call so far, 2 names in all: 'defaultPalette',
  'parentPalette'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickAbstractPaletteProvider::~QQuickAbstractPaletteProvider()':
    the destructor: Python never removes a C++ QQuickAbstractPaletteProvider.

  What to expect
  --------------

  - The C++ QQuickAbstractPaletteProvider is created at the first use, not by
    'QQuickAbstractPaletteProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAbstractPaletteProvider.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAbstractPaletteProvider'

  #  A C++ QQuickAbstractPaletteProvider Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAbstractPaletteProvider'

  #  The functions Qt calls itself that QQuickAbstractPaletteProvider is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'defaultPalette': (
          ('_ZNK29QQuickAbstractPaletteProvider14defaultPaletteEv',
           ('address', 'value', 'QtGui:QPalette'),
           ()),
      ),
      'parentPalette': (
          ('_ZNK29QQuickAbstractPaletteProvider13parentPaletteERK8QPalette',
           ('address', 'value', 'QtGui:QPalette'),
           (
               ('address', 'value', 'QtGui:QPalette'),
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

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickAbstractPaletteProvider::defaultPalette()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpaletteprovider.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickAbstractPaletteProvider::defaultPalette() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickAbstractPaletteProvider14defaultPaletteEv',
    )
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

  @overload(QPalette)
  def parentPalette(self, fallbackPalette: QPalette) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickAbstractPaletteProvider::parentPalette(const
    QPalette &fallbackPalette) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpaletteprovider.html#parentPalette

    Parameters
    ----------

    fallbackPalette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickAbstractPaletteProvider::parentPalette(const QPalette
    #      &fallbackPalette) const
    ritual = (
        'ritual_ZNK29QQuickAbstractPaletteProvider13parentPaletteERK8QPalet'
        'te')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QQuickAbstractPaletteProvider13parentPaletteERK8'
          'QPalette')
    address = self.uglySide.call(ritual, self._valueOf(fallbackPalette))
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

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

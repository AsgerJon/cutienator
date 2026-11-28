"""
QFileIconProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qfileiconprovider.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAbstractFileIconProvider

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QFileInfo
  from ..QtGui import QIcon
  from . import QFileIconProviderPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileInfo = WAIT['QFileInfo']


class QFileIconProvider(QAbstractFileIconProvider):
  """
  The cute side of Qt's QFileIconProvider: a plain Python object standing in
  front of one C++ QFileIconProvider.

  It is built on the cute 'QAbstractFileIconProvider', as Qt's
  QFileIconProvider is built on Qt's QAbstractFileIconProvider, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QFileIconProvider that has a ritual and that Python
  can call so far, 2 names in all: 'icon', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFileIconProvider::~QFileIconProvider()': the destructor: Python
    never removes a C++ QFileIconProvider.
  - Qt's 'const QFileIconProviderPrivate *QFileIconProvider::d_func() const':
    takes in Python what 'QFileIconProviderPrivate
    *QFileIconProvider::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QFileIconProvider is created at the first use, not by
    'QFileIconProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileIconProvider.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileIconProvider'

  #  A C++ QFileIconProvider Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFileIconProvider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractFileIconProvider.IconType)
  def icon(self, type: QAbstractFileIconProvider.IconType) -> QIcon:
    """
    Calls Qt's 'QIcon QFileIconProvider::icon(IconType type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileiconprovider.html#icon

    Parameters
    ----------

    type : QAbstractFileIconProvider.IconType
      Passed on as its number.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QFileIconProvider::icon(IconType type) const
    ritual = (
        'ritual_ZNK17QFileIconProvider4iconEN25QAbstractFileIconProvider8Ic'
        'onTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QFileIconProvider4iconEN25QAbstractFileIconProvi'
          'der8IconTypeE')
    address = self.uglySide.call(ritual, type.value)
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  @overload(QFileInfo)
  def icon(self, info: QFileInfo) -> QIcon:
    """
    Calls Qt's 'QIcon QFileIconProvider::icon(const QFileInfo &info) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileiconprovider.html#icon

    Parameters
    ----------

    info : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QFileIconProvider::icon(const QFileInfo &info) const
    ritual = 'ritual_ZNK17QFileIconProvider4iconERK9QFileInfo'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QFileIconProvider4iconERK9QFileInfo'
    address = self.uglySide.call(ritual, self._valueOf(info))
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

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
    Notes what was given, for Qt's 'QFileIconProvider::QFileIconProvider()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileiconprovider.html#QFileIconProvider
    """
    #  QFileIconProvider::QFileIconProvider()
    self._noteCreation(QFileIconProvider, lambda: Rituals.call(
        'ritual_ZN17QFileIconProviderC1Ev',
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

  def d_func(self) -> Optional[QFileIconProviderPrivate]:
    """
    Calls Qt's 'QFileIconProviderPrivate *QFileIconProvider::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qfileiconprovider.html#d_func

    Returns
    -------

    Optional[QFileIconProviderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileIconProviderPrivate *QFileIconProvider::d_func()
    address = self.uglySide.call('ritual_ZN17QFileIconProvider6d_funcEv')
    from . import QFileIconProviderPrivate
    return QFileIconProviderPrivate._cuteAt(address)

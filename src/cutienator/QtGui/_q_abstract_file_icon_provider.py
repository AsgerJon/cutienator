"""
QAbstractFileIconProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qabstractfileiconprovider.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QAbstractFileIconProviderIconType
from . import QAbstractFileIconProviderOption

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QFileInfo
  from . import QIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileInfo = WAIT['QFileInfo']


class QAbstractFileIconProvider(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAbstractFileIconProvider: a plain Python object
  standing in front of one C++ QAbstractFileIconProvider.

  What exists
  -----------

  Every function of Qt's QAbstractFileIconProvider that has a ritual and that
  Python can call so far, 4 names in all: 'icon', 'type', 'setOptions',
  'options'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractFileIconProvider::~QAbstractFileIconProvider()': the
    destructor: Python never removes a C++ QAbstractFileIconProvider.

  What has no ritual
  ------------------

  8 of the 15 functions Qt declares: 3 private; 2 forbidden; 1 declared and
  nowhere to be found; 1 a template; 1 protected.

  What to expect
  --------------

  - The C++ QAbstractFileIconProvider is created at the first use, not by
    'QAbstractFileIconProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractFileIconProvider.
  """

  #  The enums Qt writes inside QAbstractFileIconProvider, and the names Qt
  #  has for the combinations of its flags enums.
  IconType = QAbstractFileIconProviderIconType
  Option = QAbstractFileIconProviderOption
  Options = QAbstractFileIconProviderOption

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractFileIconProvider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(IconType)
  def icon(self, a0: IconType) -> QIcon:
    """
    Calls Qt's 'QIcon QAbstractFileIconProvider::icon(IconType a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconprovider.html#icon

    Parameters
    ----------

    a0 : IconType
      Passed on as its number.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QAbstractFileIconProvider::icon(IconType a0) const
    address = self.uglySide.call(
        'ritual_ZNK25QAbstractFileIconProvider4iconENS_8IconTypeE', a0.value,
    )
    from . import QIcon
    return QIcon._cuteOwning(address)

  @overload(QFileInfo)
  def icon(self, a0: QFileInfo) -> QIcon:
    """
    Calls Qt's 'QIcon QAbstractFileIconProvider::icon(const QFileInfo &a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconprovider.html#icon

    Parameters
    ----------

    a0 : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QAbstractFileIconProvider::icon(const QFileInfo &a0) const
    address = self.uglySide.call(
        'ritual_ZNK25QAbstractFileIconProvider4iconERK9QFileInfo',
        self._valueOf(a0),
    )
    from . import QIcon
    return QIcon._cuteOwning(address)

  @overload(QFileInfo)
  def type(self, a0: QFileInfo) -> str:
    """
    Calls Qt's 'QString QAbstractFileIconProvider::type(const QFileInfo &a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconprovider.html#type

    Parameters
    ----------

    a0 : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractFileIconProvider::type(const QFileInfo &a0) const
    return self.uglySide.call(
        'ritual_ZNK25QAbstractFileIconProvider4typeERK9QFileInfo',
        self._valueOf(a0),
    )

  def options(self) -> Options:
    """
    Calls Qt's 'Options QAbstractFileIconProvider::options() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconprovider.html#options

    Returns
    -------

    Options
      The value standing for the combination Qt gave back.
    """
    #  Options QAbstractFileIconProvider::options() const
    return QAbstractFileIconProvider.Options(self.uglySide.call(
        'ritual_ZNK25QAbstractFileIconProvider7optionsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Options)
  def setOptions(self, a0: Options) -> None:
    """
    Calls Qt's 'void QAbstractFileIconProvider::setOptions(Options a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconprovider.html#setOptions

    Parameters
    ----------

    a0 : Options
      Passed on as its number.
    """
    #  void QAbstractFileIconProvider::setOptions(Options a0)
    self.uglySide.call(
        'ritual_ZN25QAbstractFileIconProvider10setOptionsE6QFlagsINS_6Optio'
        'nEE',
        a0.value,
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
    Notes what was given, for Qt's
    'QAbstractFileIconProvider::QAbstractFileIconProvider()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractfileiconprovider.html
    """
    #  QAbstractFileIconProvider::QAbstractFileIconProvider()
    self._noteCreation(QAbstractFileIconProvider, lambda: Rituals.call(
        'ritual_ZN25QAbstractFileIconProviderC1Ev',
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

"""
QCompressedHelpInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qcompressedhelpinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVersionNumber


class QCompressedHelpInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCompressedHelpInfo: a plain Python object standing
  in front of one C++ QCompressedHelpInfo.

  C++ hands a QCompressedHelpInfo around as a copy, so every C++
  QCompressedHelpInfo behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCompressedHelpInfo that has a ritual and that
  Python can call so far, 5 names in all: 'namespaceName', 'component',
  'version', 'isNull', 'fromCompressedHelpFile'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCompressedHelpInfo::QCompressedHelpInfo(QCompressedHelpInfo
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QCompressedHelpInfo::~QCompressedHelpInfo()': the destructor:
    Python removes its C++ QCompressedHelpInfo by it, and has no other use
    for it.
  - Qt's 'QCompressedHelpInfo &QCompressedHelpInfo::operator=(const
    QCompressedHelpInfo &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QCompressedHelpInfo
    &QCompressedHelpInfo::operator=(QCompressedHelpInfo &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCompressedHelpInfo::swap(QCompressedHelpInfo &other)': takes
    a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QCompressedHelpInfo is created at the first use, not by
    'QCompressedHelpInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCompressedHelpInfo back gives a copy the ritual made
    for Python, in a new cute QCompressedHelpInfo.
  - Each name of Qt's QCompressedHelpInfo that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  def fromCompressedHelpFile(
      documentationFileName: str,
  ) -> QCompressedHelpInfo:
    """
    Calls Qt's 'QCompressedHelpInfo
    QCompressedHelpInfo::fromCompressedHelpFile(const QString
    &documentationFileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompressedhelpinfo.html#fromCompressedHelpFile

    Parameters
    ----------

    documentationFileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QCompressedHelpInfo
      A new cute QCompressedHelpInfo around the copy Qt gave back. Python
      owns it.
    """
    #  QCompressedHelpInfo QCompressedHelpInfo::fromCompressedHelpFile(const
    #      QString &documentationFileName)
    address = Rituals.call(
        'ritual_ZN19QCompressedHelpInfo22fromCompressedHelpFileERK7QString',
        documentationFileName,
    )
    return QCompressedHelpInfo._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCompressedHelpInfo'

  #  Qt's '~QCompressedHelpInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QCompressedHelpInfo behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QCompressedHelpInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def namespaceName(self) -> str:
    """
    Calls Qt's 'QString QCompressedHelpInfo::namespaceName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompressedhelpinfo.html#namespaceName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCompressedHelpInfo::namespaceName() const
    return self.uglySide.call(
        'ritual_ZNK19QCompressedHelpInfo13namespaceNameEv',
    )

  def component(self) -> str:
    """
    Calls Qt's 'QString QCompressedHelpInfo::component() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompressedhelpinfo.html#component

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCompressedHelpInfo::component() const
    return self.uglySide.call('ritual_ZNK19QCompressedHelpInfo9componentEv')

  def version(self) -> QVersionNumber:
    """
    Calls Qt's 'QVersionNumber QCompressedHelpInfo::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompressedhelpinfo.html#version

    Returns
    -------

    QVersionNumber
      A new cute QVersionNumber around the copy Qt gave back. Python owns it.
    """
    #  QVersionNumber QCompressedHelpInfo::version() const
    address = self.uglySide.call('ritual_ZNK19QCompressedHelpInfo7versionEv')
    from ..QtCore import QVersionNumber
    return QVersionNumber._cuteOwning(address)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QCompressedHelpInfo::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcompressedhelpinfo.html#isNull
    """
    #  bool QCompressedHelpInfo::isNull() const
    return self.uglySide.call('ritual_ZNK19QCompressedHelpInfo6isNullEv')

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
    'QCompressedHelpInfo::QCompressedHelpInfo()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompressedhelpinfo.html#QCompressedHelpInfo
    """
    #  QCompressedHelpInfo::QCompressedHelpInfo()
    self._noteCreation(QCompressedHelpInfo, lambda: Rituals.call(
        'ritual_ZN19QCompressedHelpInfoC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QCompressedHelpInfo) -> None:
    """
    Notes what was given, for Qt's
    'QCompressedHelpInfo::QCompressedHelpInfo(const QCompressedHelpInfo
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcompressedhelpinfo.html#QCompressedHelpInfo

    Parameters
    ----------

    other : QCompressedHelpInfo
      Passed on as a value: Qt reads the C++ QCompressedHelpInfo, which stays
      Python's own.
    """
    #  QCompressedHelpInfo::QCompressedHelpInfo(const QCompressedHelpInfo
    #      &other)
    self._noteCreation(QCompressedHelpInfo, lambda: Rituals.call(
        'ritual_ZN19QCompressedHelpInfoC1ERKS_', self._valueOf(other),
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
    Qt's 'void QCompressedHelpInfo::swap(QCompressedHelpInfo &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCompressedHelpInfo.swap' has no cute function yet. Qt's 'void "
        "QCompressedHelpInfo::swap(QCompressedHelpInfo &other)': takes a "
        "type Python has no way to hand over yet.")

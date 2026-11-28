"""
QQmlJS::Import binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsimporter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlJS::Import to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QTypeRevision
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTypeRevision = WAIT['QTypeRevision']


class Import(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::Import: a plain Python object standing in
  front of one C++ QQmlJS::Import.

  C++ hands a QQmlJS::Import around as a copy, so every C++ QQmlJS::Import
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlJS::Import that has a ritual and that Python can
  call so far, 7 names in all: 'isValid', 'prefix', 'name', 'version',
  'isFile', 'isDependency', '__eq__'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::Import::~Import()': the destructor: Python removes its C++
    QQmlJS::Import by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJS::Import is created at the first use, not by
    'QQmlJS::Import(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJS::Import back gives a copy the ritual made for
    Python, in a new cute QQmlJS::Import.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::Import'

  #  Qt's '~QQmlJS::Import()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlJS::Import behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN6QQmlJS6ImportD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::Import::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-import.html#isValid
    """
    #  bool QQmlJS::Import::isValid() const
    return self.uglySide.call('ritual_ZNK6QQmlJS6Import7isValidEv')

  def prefix(self) -> str:
    """
    Calls Qt's 'QString QQmlJS::Import::prefix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-import.html#prefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::Import::prefix() const
    return self.uglySide.call('ritual_ZNK6QQmlJS6Import6prefixEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QQmlJS::Import::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-import.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJS::Import::name() const
    return self.uglySide.call('ritual_ZNK6QQmlJS6Import4nameEv')

  def version(self) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QQmlJS::Import::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-import.html#version

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QQmlJS::Import::version() const
    address = self.uglySide.call('ritual_ZNK6QQmlJS6Import7versionEv')
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  def isFile(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::Import::isFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-import.html#isFile
    """
    #  bool QQmlJS::Import::isFile() const
    return self.uglySide.call('ritual_ZNK6QQmlJS6Import6isFileEv')

  def isDependency(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::Import::isDependency() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-import.html#isDependency
    """
    #  bool QQmlJS::Import::isDependency() const
    return self.uglySide.call('ritual_ZNK6QQmlJS6Import12isDependencyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: Import) -> bool:
    """
    Calls Qt's 'bool operator==(const Import &a, const Import &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-import.html#operator==

    Parameters
    ----------

    b : Import
      Passed on as a value: Qt reads the C++ QQmlJS::Import, which stays
      Python's own.
    """
    #  bool operator==(const Import &a, const Import &b)
    return Rituals.call(
        'ritual_ZN6QQmlJSeqERKNS_6ImportES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlJS::Import::Import()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-import.html#Import
    """
    #  QQmlJS::Import::Import()
    self._noteCreation(Import, lambda: Rituals.call(
        'ritual_ZN6QQmlJS6ImportC1Ev',
    ))

  @overload(str, str, QTypeRevision, bool, bool)
  def __init__(
      self,
      prefix: str,
      name: str,
      version: QTypeRevision,
      isFile: bool,
      isDependency: bool,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlJS::Import::Import(QString prefix,
    QString name, QTypeRevision version, bool isFile, bool isDependency)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-import.html#Import

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    isFile : bool
      Passed on as it is.

    isDependency : bool
      Passed on as it is.
    """
    #  QQmlJS::Import::Import(QString prefix, QString name, QTypeRevision
    #      version, bool isFile, bool isDependency)
    self._noteCreation(Import, lambda: Rituals.call(
        'ritual_ZN6QQmlJS6ImportC1E7QStringS1_13QTypeRevisionbb',
        prefix, name, self._valueOf(version), isFile, isDependency,
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

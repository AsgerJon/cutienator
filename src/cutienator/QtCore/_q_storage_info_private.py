"""
QStorageInfoPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qstorageinfo_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QStorageInfoPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QByteArray, QStorageInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QStorageInfoPrivate(QSharedData):
  """
  The cute side of Qt's QStorageInfoPrivate: a plain Python object standing
  in front of one C++ QStorageInfoPrivate.

  It is built on the cute 'QSharedData', as Qt's QStorageInfoPrivate is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QStorageInfoPrivate around as a copy, so every C++
  QStorageInfoPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QStorageInfoPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'root', 'shouldIncludeFs'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QStorageInfoPrivate::setFromMountInfo(MountInfo &&info)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QStorageInfoPrivate::QStorageInfoPrivate(MountInfo &&info)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QStorageInfoPrivate::~QStorageInfoPrivate()': the destructor:
    Python removes its C++ QStorageInfoPrivate by it, and has no other use
    for it.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 3 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 a template.

  What to expect
  --------------

  - The C++ QStorageInfoPrivate is created at the first use, not by
    'QStorageInfoPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QStorageInfoPrivate back gives a copy the ritual made
    for Python, in a new cute QStorageInfoPrivate.
  - Each name of Qt's QStorageInfoPrivate that has no cute function yet,
    'doStat', 'isParentOf', 'mountedVolumes', 'retrieveVolumeInfo',
    'setFromMountInfo', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QStorageInfoPrivate, each a class in here
  #  as in C++.

  class MountInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QStorageInfoPrivate::MountInfo: a plain Python
    object standing in front of one C++ QStorageInfoPrivate::MountInfo.

    C++ hands a QStorageInfoPrivate::MountInfo around as a copy, so every C++
    QStorageInfoPrivate::MountInfo behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QStorageInfoPrivate::MountInfo yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QStorageInfoPrivate::MountInfo::~MountInfo()': the destructor:
      Python removes its C++ QStorageInfoPrivate::MountInfo by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QStorageInfoPrivate::MountInfo is created at the first use, not
      by 'QStorageInfoPrivate::MountInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QStorageInfoPrivate::MountInfo back gives a copy
      the ritual made for Python, in a new cute
      QStorageInfoPrivate::MountInfo.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QStorageInfoPrivate::MountInfo'

    #  Qt's '~QStorageInfoPrivate::MountInfo()'. Naming it makes this a value
    #  class: Python owns every C++ QStorageInfoPrivate::MountInfo behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QStorageInfoPrivate9MountInfoD1Ev'

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

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def root() -> QStorageInfo:
    """
    Calls Qt's 'QStorageInfo QStorageInfoPrivate::root()'.

    Qt's own words: https://doc.qt.io/qt-6/qstorageinfoprivate.html#root

    Returns
    -------

    QStorageInfo
      A new cute QStorageInfo around the copy Qt gave back. Python owns it.
    """
    #  QStorageInfo QStorageInfoPrivate::root()
    address = Rituals.call('ritual_ZN19QStorageInfoPrivate4rootEv')
    from . import QStorageInfo
    return QStorageInfo._cuteOwning(address)

  @staticmethod
  @overload(str, QByteArray)
  def shouldIncludeFs(mountDir: str, fsType: QByteArray) -> bool:
    """
    Calls Qt's 'bool QStorageInfoPrivate::shouldIncludeFs(const QString
    &mountDir, const QByteArray &fsType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstorageinfoprivate.html#shouldIncludeFs

    Parameters
    ----------

    mountDir : str
      Passed on as it is: a QString is made of it for the call.

    fsType : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  bool QStorageInfoPrivate::shouldIncludeFs(const QString &mountDir,
    #      const QByteArray &fsType)
    return Rituals.call(
        'ritual_ZN19QStorageInfoPrivate15shouldIncludeFsERK7QStringRK10QByt'
        'eArray',
        mountDir, CuteMixin._valueOf(fsType),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStorageInfoPrivate'

  #  Qt's '~QStorageInfoPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QStorageInfoPrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QStorageInfoPrivateD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QStorageInfoPrivate::QStorageInfoPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstorageinfoprivate.html#QStorageInfoPrivate
    """
    #  QStorageInfoPrivate::QStorageInfoPrivate()
    self._noteCreation(QStorageInfoPrivate, lambda: Rituals.call(
        'ritual_ZN19QStorageInfoPrivateC1Ev',
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
  def doStat(*__, **_) -> Never:
    """
    Qt's 'void QStorageInfoPrivate::doStat()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QStorageInfoPrivate.doStat' has no cute function yet. Qt's 'void "
        "QStorageInfoPrivate::doStat()': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def isParentOf(*__, **_) -> Never:
    """
    Qt's 'QStorageInfoPrivate::isParentOf': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QStorageInfoPrivate.isParentOf' has no cute function yet. Qt's "
        "'QStorageInfoPrivate::isParentOf': a template: a pattern and no "
        "single function.")

  @staticmethod
  def mountedVolumes(*__, **_) -> Never:
    """
    Qt's 'QList<QStorageInfo> QStorageInfoPrivate::mountedVolumes()': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QStorageInfoPrivate.mountedVolumes' has no cute function yet. "
        "Qt's 'QList<QStorageInfo> QStorageInfoPrivate::mountedVolumes()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def retrieveVolumeInfo(*__, **_) -> Never:
    """
    Qt's 'void QStorageInfoPrivate::retrieveVolumeInfo()': cannot be called
    and cannot be called through the meta-object and cannot be copied: no
    header file has its code, Qt's source does not mark it or its class for
    use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QStorageInfoPrivate.retrieveVolumeInfo' has no cute function yet. "
        "Qt's 'void QStorageInfoPrivate::retrieveVolumeInfo()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def setFromMountInfo(*__, **_) -> Never:
    """
    Qt's 'void QStorageInfoPrivate::setFromMountInfo(MountInfo &&info)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QStorageInfoPrivate.setFromMountInfo' has no cute function yet. "
        "Qt's 'void QStorageInfoPrivate::setFromMountInfo(MountInfo "
        "&&info)': takes a type Python has no way to hand over yet.")

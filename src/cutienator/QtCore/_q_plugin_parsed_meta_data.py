"""
QPluginParsedMetaData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qplugin_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QPluginParsedMetaData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QByteArrayView, QCborMap, QJsonObject, QPluginMetaData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArrayView = WAIT['QByteArrayView']
  QPluginMetaData = WAIT['QPluginMetaData']


class QPluginParsedMetaData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPluginParsedMetaData: a plain Python object standing
  in front of one C++ QPluginParsedMetaData.

  C++ hands a QPluginParsedMetaData around as a copy, so every C++
  QPluginParsedMetaData behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPluginParsedMetaData that has a ritual and that
  Python can call so far, 6 names in all: 'setError', 'isError',
  'errorString', 'parse', 'toJson', 'toCbor'. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCborValue QPluginParsedMetaData::value(QtPluginMetaDataKeys k)
    const': names the enum 'QtPluginMetaDataKeys', whose class cannot be
    named here.
  - Qt's 'QPluginParsedMetaData::~QPluginParsedMetaData()': the destructor:
    Python removes its C++ QPluginParsedMetaData by it, and has no other use
    for it.

  What has no ritual
  ------------------

  1 of the 11 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QPluginParsedMetaData is created at the first use, not by
    'QPluginParsedMetaData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPluginParsedMetaData back gives a copy the ritual
    made for Python, in a new cute QPluginParsedMetaData.
  - Each name of Qt's QPluginParsedMetaData that has no cute function yet,
    'value', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPluginParsedMetaData'

  #  Qt's '~QPluginParsedMetaData()'. Naming it makes this a value class:
  #  Python owns every C++ QPluginParsedMetaData behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QPluginParsedMetaDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isError(self) -> bool:
    """
    Calls Qt's 'bool QPluginParsedMetaData::isError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginparsedmetadata.html#isError
    """
    #  bool QPluginParsedMetaData::isError() const
    return self.uglySide.call('ritual_ZNK21QPluginParsedMetaData7isErrorEv')

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QPluginParsedMetaData::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpluginparsedmetadata.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPluginParsedMetaData::errorString() const
    return self.uglySide.call(
        'ritual_ZNK21QPluginParsedMetaData11errorStringEv',
    )

  def toJson(self) -> QJsonObject:
    """
    Calls Qt's 'QJsonObject QPluginParsedMetaData::toJson() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginparsedmetadata.html#toJson

    Returns
    -------

    QJsonObject
      A new cute QJsonObject around the copy Qt gave back. Python owns it.
    """
    #  QJsonObject QPluginParsedMetaData::toJson() const
    address = self.uglySide.call(
        'ritual_ZNK21QPluginParsedMetaData6toJsonEv',
    )
    from . import QJsonObject
    return QJsonObject._cuteOwning(address)

  def toCbor(self) -> QCborMap:
    """
    Calls Qt's 'QCborMap QPluginParsedMetaData::toCbor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginparsedmetadata.html#toCbor

    Returns
    -------

    QCborMap
      A new cute QCborMap around the copy Qt gave back. Python owns it.
    """
    #  QCborMap QPluginParsedMetaData::toCbor() const
    address = self.uglySide.call(
        'ritual_ZNK21QPluginParsedMetaData6toCborEv',
    )
    from . import QCborMap
    return QCborMap._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setError(self, errorString: str) -> bool:
    """
    Calls Qt's 'bool QPluginParsedMetaData::setError(const QString
    &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpluginparsedmetadata.html#setError

    Parameters
    ----------

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QPluginParsedMetaData::setError(const QString &errorString)
    return self.uglySide.call(
        'ritual_ZN21QPluginParsedMetaData8setErrorERK7QString', errorString,
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
    'QPluginParsedMetaData::QPluginParsedMetaData()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpluginparsedmetadata.html#QPluginParsedMetaData
    """
    #  QPluginParsedMetaData::QPluginParsedMetaData()
    self._noteCreation(QPluginParsedMetaData, lambda: Rituals.call(
        'ritual_ZN21QPluginParsedMetaDataC1Ev',
    ))

  @overload(QByteArrayView)
  def __init__(self, input: QByteArrayView) -> None:
    """
    Notes what was given, for Qt's
    'QPluginParsedMetaData::QPluginParsedMetaData(QByteArrayView input)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpluginparsedmetadata.html#QPluginParsedMetaData

    Parameters
    ----------

    input : QByteArrayView
      Passed on as a value: Qt reads the C++ QByteArrayView, which stays
      Python's own.
    """
    #  QPluginParsedMetaData::QPluginParsedMetaData(QByteArrayView input)
    self._noteCreation(QPluginParsedMetaData, lambda: Rituals.call(
        'ritual_ZN21QPluginParsedMetaDataC1E14QByteArrayView',
        self._valueOf(input),
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

  @overload(QPluginMetaData)
  def parse(self, metaData: QPluginMetaData) -> bool:
    """
    Calls Qt's 'bool QPluginParsedMetaData::parse(QPluginMetaData metaData)'.

    Qt's own words: https://doc.qt.io/qt-6/qpluginparsedmetadata.html#parse

    Parameters
    ----------

    metaData : QPluginMetaData
      Passed on as a value: Qt reads the C++ QPluginMetaData, which stays
      Python's own.
    """
    #  bool QPluginParsedMetaData::parse(QPluginMetaData metaData)
    return self.uglySide.call(
        'ritual_ZN21QPluginParsedMetaData5parseE15QPluginMetaData',
        self._valueOf(metaData),
    )

  @staticmethod
  def value(*__, **_) -> Never:
    """
    Qt's 'QCborValue QPluginParsedMetaData::value(QtPluginMetaDataKeys k)
    const': names the enum 'QtPluginMetaDataKeys', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QPluginParsedMetaData.value' has no cute function yet. Qt's "
        "'QCborValue QPluginParsedMetaData::value(QtPluginMetaDataKeys k) "
        "const': names the enum 'QtPluginMetaDataKeys', whose class cannot "
        "be named here.")

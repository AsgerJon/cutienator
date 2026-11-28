"""
Qt3DCore::Quick::Quick3DBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dbuffer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::Quick::Quick3DBuffer to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl, QVariant
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Quick3DBuffer(Qt3DCore.QBuffer):
  """
  The cute side of Qt's Qt3DCore::Quick::Quick3DBuffer: a plain Python object
  standing in front of one C++ Qt3DCore::Quick::Quick3DBuffer.

  It is built on the cute 'Qt3DCore::QBuffer', as Qt's
  Qt3DCore::Quick::Quick3DBuffer is built on Qt's Qt3DCore::QBuffer, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::Quick::Quick3DBuffer that has a ritual and
  that Python can call so far, 9 names in all: 'metaObject', 'tr',
  'bufferData', 'setBufferData', 'readBinaryFile', 'updateData',
  'bufferDataChanged', 'initEngines', 'convertToRawData'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::Quick::Quick3DBuffer::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DCore::Quick::Quick3DBuffer::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::Quick::Quick3DBuffer is created at the first use, not
    by 'Qt3DCore::Quick::Quick3DBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::Quick::Quick3DBuffer.
  - Qt tells when it has removed the C++ Qt3DCore::Quick::Quick3DBuffer.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DCore::Quick::Quick3DBuffer::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dbuffer.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DCore::Quick::Quick3DBuffer::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore5Quick13Quick3DBuffer2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::Quick::Quick3DBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DCore::Quick::Quick3DBuffer::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dbuffer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::Quick::Quick3DBuffer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick13Quick3DBuffer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def bufferData(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DCore::Quick::Quick3DBuffer::bufferData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dbuffer.html#bufferData

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DCore::Quick::Quick3DBuffer::bufferData() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore5Quick13Quick3DBuffer10bufferDataEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setBufferData(self, bufferData: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::Quick3DBuffer::setBufferData(const
    QVariant &bufferData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dbuffer.html#setBufferData

    Parameters
    ----------

    bufferData : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DCore::Quick::Quick3DBuffer::setBufferData(const QVariant
    #      &bufferData)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick13Quick3DBuffer13setBufferDataERK8QVariant',
        self._valueOf(bufferData),
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::Quick::Quick3DBuffer::Quick3DBuffer(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dbuffer.html#Quick3DBuffer

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::Quick::Quick3DBuffer::Quick3DBuffer(Qt3DCore::QNode *parent)
    self._noteCreation(Quick3DBuffer, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore5Quick13Quick3DBufferC1EPNS_5QNodeE',
        self._addressOf(parent),
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

  @overload(QUrl)
  def readBinaryFile(self, fileUrl: QUrl) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DCore::Quick::Quick3DBuffer::readBinaryFile(const
    QUrl &fileUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dbuffer.html#readBinaryFile

    Parameters
    ----------

    fileUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DCore::Quick::Quick3DBuffer::readBinaryFile(const QUrl
    #      &fileUrl)
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick13Quick3DBuffer14readBinaryFileERK4QUrl',
        self._valueOf(fileUrl),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(int, QVariant)
  def updateData(self, offset: int, bytes: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::Quick3DBuffer::updateData(int offset,
    const QVariant &bytes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dbuffer.html#updateData

    Parameters
    ----------

    offset : int
      Passed on as it is.

    bytes : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DCore::Quick::Quick3DBuffer::updateData(int offset, const
    #      QVariant &bytes)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick13Quick3DBuffer10updateDataEiRK8QVariant',
        offset, self._valueOf(bytes),
    )

  def bufferDataChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::Quick3DBuffer::bufferDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dbuffer.html
    """
    #  void Qt3DCore::Quick::Quick3DBuffer::bufferDataChanged()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick13Quick3DBuffer17bufferDataChangedEv',
    )

  def initEngines(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::Quick::Quick3DBuffer::initEngines()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dbuffer.html#initEngines
    """
    #  void Qt3DCore::Quick::Quick3DBuffer::initEngines()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick13Quick3DBuffer11initEnginesEv',
    )

  @overload(QJSValue)
  def convertToRawData(self, jsValue: QJSValue) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DCore::Quick::Quick3DBuffer::convertToRawData(const QJSValue
    &jsValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-quick-quick3dbuffer.html#convertToRawData

    Parameters
    ----------

    jsValue : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DCore::Quick::Quick3DBuffer::convertToRawData(const
    #      QJSValue &jsValue)
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore5Quick13Quick3DBuffer16convertToRawDataERK8QJSVa'
        'lue',
        self._valueOf(jsValue),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

"""
QQmlGrpcMetadata binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpcQuick/6.12.0/QtGrpcQuick/private/qqmlgrpcmetadata_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlGrpcMetadata to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlGrpcMetadata(QObject):
  """
  The cute side of Qt's QQmlGrpcMetadata: a plain Python object standing in
  front of one C++ QQmlGrpcMetadata.

  It is built on the cute 'QObject', as Qt's QQmlGrpcMetadata is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlGrpcMetadata that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'tr', 'data', 'setData',
  'dataChanged'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlGrpcMetadata::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlGrpcMetadata::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlGrpcMetadata::~QQmlGrpcMetadata()': the destructor: Python
    never removes a C++ QQmlGrpcMetadata.
  - Qt's 'const QMultiHash<QByteArray, QByteArray>
    &QQmlGrpcMetadata::metadata() const': gives a type Python has no way to
    take yet.

  What has no ritual
  ------------------

  7 of the 17 functions Qt declares: 5 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlGrpcMetadata is created at the first use, not by
    'QQmlGrpcMetadata(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlGrpcMetadata.
  - Qt tells when it has removed the C++ QQmlGrpcMetadata. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlGrpcMetadata that has no cute function yet,
    'metadata', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QQmlGrpcMetadata::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgrpcmetadata.html#tr

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
    #  QString QQmlGrpcMetadata::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQmlGrpcMetadata2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlGrpcMetadata'

  #  A C++ QQmlGrpcMetadata Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlGrpcMetadata'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlGrpcMetadata::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgrpcmetadata.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlGrpcMetadata::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlGrpcMetadata10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def data(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'const QVariantMap &QQmlGrpcMetadata::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgrpcmetadata.html#data

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  const QVariantMap &QQmlGrpcMetadata::data() const
    address = self.uglySide.call('ritual_ZNK16QQmlGrpcMetadata4dataEv')
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMap[str, QVariant])
  def setData(self, data: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QQmlGrpcMetadata::setData(const QVariantMap &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgrpcmetadata.html#setData

    Parameters
    ----------

    data : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQmlGrpcMetadata::setData(const QVariantMap &data)
    self.uglySide.call(
        'ritual_ZN16QQmlGrpcMetadata7setDataERK4QMapI7QString8QVariantE',
        self._valueOf(data),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQmlGrpcMetadata::QQmlGrpcMetadata(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcmetadata.html#QQmlGrpcMetadata

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlGrpcMetadata::QQmlGrpcMetadata(QObject *parent)
    self._noteCreation(QQmlGrpcMetadata, lambda: Rituals.call(
        'ritual_ZN16QQmlGrpcMetadataC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def dataChanged(self) -> None:
    """
    Calls Qt's 'void QQmlGrpcMetadata::dataChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgrpcmetadata.html#dataChanged
    """
    #  void QQmlGrpcMetadata::dataChanged()
    self.uglySide.call('ritual_ZN16QQmlGrpcMetadata11dataChangedEv')

  @staticmethod
  def metadata(*__, **_) -> Never:
    """
    Qt's 'const QMultiHash<QByteArray, QByteArray>
    &QQmlGrpcMetadata::metadata() const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQmlGrpcMetadata.metadata' has no cute function yet. Qt's 'const "
        "QMultiHash<QByteArray, QByteArray> &QQmlGrpcMetadata::metadata() "
        "const': gives a type Python has no way to take yet.")

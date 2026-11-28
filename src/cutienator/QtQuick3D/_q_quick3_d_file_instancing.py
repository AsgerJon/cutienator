"""
QQuick3DFileInstancing binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dinstancing_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DFileInstancing to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuick3DInstancing, QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice, QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DFileInstancing(QQuick3DInstancing):
  """
  The cute side of Qt's QQuick3DFileInstancing: a plain Python object
  standing in front of one C++ QQuick3DFileInstancing.

  It is built on the cute 'QQuick3DInstancing', as Qt's
  QQuick3DFileInstancing is built on Qt's QQuick3DInstancing, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DFileInstancing that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'source',
  'setSource', 'loadFromBinaryFile', 'loadFromXmlFile', 'writeToBinaryFile',
  'instanceCount', 'instanceCountChanged', 'sourceChanged', 'loadFromFile'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DFileInstancing::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DFileInstancing::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DFileInstancing::~QQuick3DFileInstancing()': the destructor:
    Python never removes a C++ QQuick3DFileInstancing.
  - Qt's 'QByteArray QQuick3DFileInstancing::getInstanceBuffer(int
    *instanceCount)': takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DFileInstancing is created at the first use, not by
    'QQuick3DFileInstancing(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DFileInstancing.
  - Qt tells when it has removed the C++ QQuick3DFileInstancing. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuick3DFileInstancing::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfileinstancing.html#tr

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
    #  QString QQuick3DFileInstancing::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuick3DFileInstancing2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DFileInstancing'

  #  A C++ QQuick3DFileInstancing Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DFileInstancing'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DFileInstancing::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfileinstancing.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DFileInstancing::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DFileInstancing10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'const QUrl &QQuick3DFileInstancing::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dfileinstancing.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  const QUrl &QQuick3DFileInstancing::source() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DFileInstancing6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def instanceCount(self) -> int:
    """
    Calls Qt's 'int QQuick3DFileInstancing::instanceCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfileinstancing.html#instanceCount
    """
    #  int QQuick3DFileInstancing::instanceCount() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DFileInstancing13instanceCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, newSource: QUrl) -> None:
    """
    Calls Qt's 'void QQuick3DFileInstancing::setSource(const QUrl
    &newSource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfileinstancing.html#setSource

    Parameters
    ----------

    newSource : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuick3DFileInstancing::setSource(const QUrl &newSource)
    self.uglySide.call(
        'ritual_ZN22QQuick3DFileInstancing9setSourceERK4QUrl',
        self._valueOf(newSource),
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DFileInstancing::QQuick3DFileInstancing(QQuick3DObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfileinstancing.html#QQuick3DFileInstancing

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DFileInstancing::QQuick3DFileInstancing(QQuick3DObject *parent)
    self._noteCreation(QQuick3DFileInstancing, lambda: Rituals.call(
        'ritual_ZN22QQuick3DFileInstancingC1EP14QQuick3DObject',
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

  @overload(str)
  def loadFromBinaryFile(self, filename: str) -> bool:
    """
    Calls Qt's 'bool QQuick3DFileInstancing::loadFromBinaryFile(const QString
    &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfileinstancing.html#loadFromBinaryFile

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuick3DFileInstancing::loadFromBinaryFile(const QString
    #      &filename)
    return self.uglySide.call(
        'ritual_ZN22QQuick3DFileInstancing18loadFromBinaryFileERK7QString',
        filename,
    )

  @overload(str)
  def loadFromXmlFile(self, filename: str) -> bool:
    """
    Calls Qt's 'bool QQuick3DFileInstancing::loadFromXmlFile(const QString
    &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfileinstancing.html#loadFromXmlFile

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuick3DFileInstancing::loadFromXmlFile(const QString &filename)
    return self.uglySide.call(
        'ritual_ZN22QQuick3DFileInstancing15loadFromXmlFileERK7QString',
        filename,
    )

  @overload(QIODevice)
  @overload(NoneType)
  def writeToBinaryFile(self, out: Optional[QIODevice]) -> int:
    """
    Calls Qt's 'int QQuick3DFileInstancing::writeToBinaryFile(QIODevice
    *out)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfileinstancing.html#writeToBinaryFile

    Parameters
    ----------

    out : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuick3DFileInstancing::writeToBinaryFile(QIODevice *out)
    return self.uglySide.call(
        'ritual_ZN22QQuick3DFileInstancing17writeToBinaryFileEP9QIODevice',
        self._addressOf(out),
    )

  def instanceCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFileInstancing::instanceCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfileinstancing.html#instanceCountChanged
    """
    #  void QQuick3DFileInstancing::instanceCountChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DFileInstancing20instanceCountChangedEv',
    )

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DFileInstancing::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfileinstancing.html#sourceChanged
    """
    #  void QQuick3DFileInstancing::sourceChanged()
    self.uglySide.call('ritual_ZN22QQuick3DFileInstancing13sourceChangedEv')

  @overload(QUrl)
  def loadFromFile(self, source: QUrl) -> bool:
    """
    Calls Qt's 'bool QQuick3DFileInstancing::loadFromFile(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dfileinstancing.html#loadFromFile

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QQuick3DFileInstancing::loadFromFile(const QUrl &source)
    return self.uglySide.call(
        'ritual_ZN22QQuick3DFileInstancing12loadFromFileERK4QUrl',
        self._valueOf(source),
    )

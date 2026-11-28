"""
QHttpMultiPart binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qhttpmultipart.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QHttpMultiPartPrivate, QHttpPart
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHttpPart = WAIT['QHttpPart']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHttpMultiPart(QObject):
  """
  The cute side of Qt's QHttpMultiPart: a plain Python object standing in
  front of one C++ QHttpMultiPart.

  It is built on the cute 'QObject', as Qt's QHttpMultiPart is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHttpMultiPart that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'append',
  'setContentType', 'boundary', 'setBoundary', 'd_func'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHttpMultiPart::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QHttpMultiPart::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QHttpMultiPart::~QHttpMultiPart()': the destructor: Python never
    removes a C++ QHttpMultiPart.
  - Qt's 'const QHttpMultiPartPrivate *QHttpMultiPart::d_func() const': takes
    in Python what 'QHttpMultiPartPrivate *QHttpMultiPart::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QHttpMultiPart is created at the first use, not by
    'QHttpMultiPart(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHttpMultiPart.
  - Qt tells when it has removed the C++ QHttpMultiPart. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QHttpMultiPart, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ContentType(CuteNum):
    """
    The enum 'QHttpMultiPart::ContentType' of Qt, with the 4 names Qt gives
    in it.
    """

    MixedType = Kee[int](0)
    RelatedType = Kee[int](1)
    FormDataType = Kee[int](2)
    AlternativeType = Kee[int](3)

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
    Calls Qt's 'QString QHttpMultiPart::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipart.html#tr

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
    #  QString QHttpMultiPart::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QHttpMultiPart2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHttpMultiPart'

  #  A C++ QHttpMultiPart Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHttpMultiPart'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHttpMultiPart::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipart.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHttpMultiPart::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QHttpMultiPart10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundary(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QHttpMultiPart::boundary() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipart.html#boundary

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QHttpMultiPart::boundary() const
    address = self.uglySide.call('ritual_ZNK14QHttpMultiPart8boundaryEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ContentType)
  def setContentType(self, contentType: ContentType) -> None:
    """
    Calls Qt's 'void QHttpMultiPart::setContentType(ContentType
    contentType)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipart.html#setContentType

    Parameters
    ----------

    contentType : ContentType
      Passed on as its number.
    """
    #  void QHttpMultiPart::setContentType(ContentType contentType)
    self.uglySide.call(
        'ritual_ZN14QHttpMultiPart14setContentTypeENS_11ContentTypeE',
        contentType.value,
    )

  @overload(QByteArray)
  def setBoundary(self, boundary: QByteArray) -> None:
    """
    Calls Qt's 'void QHttpMultiPart::setBoundary(const QByteArray
    &boundary)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipart.html#setBoundary

    Parameters
    ----------

    boundary : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QHttpMultiPart::setBoundary(const QByteArray &boundary)
    self.uglySide.call(
        'ritual_ZN14QHttpMultiPart11setBoundaryERK10QByteArray',
        self._valueOf(boundary),
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
    Notes what was given, for Qt's 'QHttpMultiPart::QHttpMultiPart(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipart.html#QHttpMultiPart

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHttpMultiPart::QHttpMultiPart(QObject *parent)
    self._noteCreation(QHttpMultiPart, lambda: Rituals.call(
        'ritual_ZN14QHttpMultiPartC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(ContentType)
  @overload(ContentType, QObject)
  @overload(ContentType, NoneType)
  def __init__(
      self,
      contentType: ContentType,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QHttpMultiPart::QHttpMultiPart(ContentType contentType, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipart.html#QHttpMultiPart

    Parameters
    ----------

    contentType : ContentType
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHttpMultiPart::QHttpMultiPart(ContentType contentType, QObject
    #      *parent)
    self._noteCreation(QHttpMultiPart, lambda: Rituals.call(
        'ritual_ZN14QHttpMultiPartC1ENS_11ContentTypeEP7QObject',
        contentType.value, self._addressOf(parent, 'QObject'),
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

  @overload(QHttpPart)
  def append(self, httpPart: QHttpPart) -> None:
    """
    Calls Qt's 'void QHttpMultiPart::append(const QHttpPart &httpPart)'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipart.html#append

    Parameters
    ----------

    httpPart : QHttpPart
      Passed on as a value: Qt reads the C++ QHttpPart, which stays Python's
      own.
    """
    #  void QHttpMultiPart::append(const QHttpPart &httpPart)
    self.uglySide.call(
        'ritual_ZN14QHttpMultiPart6appendERK9QHttpPart',
        self._valueOf(httpPart),
    )

  def d_func(self) -> Optional[QHttpMultiPartPrivate]:
    """
    Calls Qt's 'QHttpMultiPartPrivate *QHttpMultiPart::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qhttpmultipart.html#d_func

    Returns
    -------

    Optional[QHttpMultiPartPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHttpMultiPartPrivate *QHttpMultiPart::d_func()
    address = self.uglySide.call('ritual_ZN14QHttpMultiPart6d_funcEv')
    from . import QHttpMultiPartPrivate
    return QHttpMultiPartPrivate._cuteAt(address)

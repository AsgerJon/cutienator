"""
QQuickFontLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickfontloader_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickFontLoader to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFontLoader(QObject):
  """
  The cute side of Qt's QQuickFontLoader: a plain Python object standing in
  front of one C++ QQuickFontLoader.

  It is built on the cute 'QObject', as Qt's QQuickFontLoader is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFontLoader that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject', 'tr', 'source',
  'setSource', 'name', 'font', 'status', 'updateFontInfo', 'sourceChanged',
  'nameChanged', 'fontChanged', 'statusChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFontLoader::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickFontLoader::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickFontLoaderPrivate *QQuickFontLoader::d_func()': gives
    'QQuickFontLoaderPrivate', which has no cute class yet.
  - Qt's 'const QQuickFontLoaderPrivate *QQuickFontLoader::d_func() const':
    gives 'QQuickFontLoaderPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFontLoader is created at the first use, not by
    'QQuickFontLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFontLoader.
  - Qt tells when it has removed the C++ QQuickFontLoader. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickFontLoader, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'QQuickFontLoader::Status' of Qt, with the 4 names Qt gives in
    it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Loading = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString QQuickFontLoader::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontloader.html#tr

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
    #  QString QQuickFontLoader::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickFontLoader2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFontLoader'

  #  A C++ QQuickFontLoader Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickFontLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFontLoader::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontloader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFontLoader::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFontLoader10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFontLoader::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontloader.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFontLoader::source() const
    address = self.uglySide.call('ritual_ZNK16QQuickFontLoader6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickFontLoader::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontloader.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFontLoader::name() const
    return self.uglySide.call('ritual_ZNK16QQuickFontLoader4nameEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickFontLoader::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontloader.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickFontLoader::font() const
    address = self.uglySide.call('ritual_ZNK16QQuickFontLoader4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuickFontLoader::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontloader.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuickFontLoader::status() const
    return QQuickFontLoader.Status(self.uglySide.call(
        'ritual_ZNK16QQuickFontLoader6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFontLoader::setSource(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontloader.html#setSource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFontLoader::setSource(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN16QQuickFontLoader9setSourceERK4QUrl', self._valueOf(url),
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
    'QQuickFontLoader::QQuickFontLoader(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontloader.html#QQuickFontLoader

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFontLoader::QQuickFontLoader(QObject *parent)
    self._noteCreation(QQuickFontLoader, lambda: Rituals.call(
        'ritual_ZN16QQuickFontLoaderC1EP7QObject',
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

  @overload(int)
  def updateFontInfo(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickFontLoader::updateFontInfo(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontloader.html#updateFontInfo

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickFontLoader::updateFontInfo(int a0)
    self.uglySide.call('ritual_ZN16QQuickFontLoader14updateFontInfoEi', a0)

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontLoader::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontloader.html#sourceChanged
    """
    #  void QQuickFontLoader::sourceChanged()
    self.uglySide.call('ritual_ZN16QQuickFontLoader13sourceChangedEv')

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontLoader::nameChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontloader.html#nameChanged
    """
    #  void QQuickFontLoader::nameChanged()
    self.uglySide.call('ritual_ZN16QQuickFontLoader11nameChangedEv')

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontLoader::fontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontloader.html#fontChanged
    """
    #  void QQuickFontLoader::fontChanged()
    self.uglySide.call('ritual_ZN16QQuickFontLoader11fontChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontLoader::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontloader.html#statusChanged
    """
    #  void QQuickFontLoader::statusChanged()
    self.uglySide.call('ritual_ZN16QQuickFontLoader13statusChangedEv')

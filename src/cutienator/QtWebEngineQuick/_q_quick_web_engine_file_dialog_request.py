"""
QQuickWebEngineFileDialogRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginedialogrequests_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWebEngineFileDialogRequest to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWebEngineFileDialogRequest(QObject):
  """
  The cute side of Qt's QQuickWebEngineFileDialogRequest: a plain Python
  object standing in front of one C++ QQuickWebEngineFileDialogRequest.

  It is built on the cute 'QObject', as Qt's QQuickWebEngineFileDialogRequest
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWebEngineFileDialogRequest that has a ritual
  and that Python can call so far, 9 names in all: 'metaObject', 'tr',
  'acceptedMimeTypes', 'defaultFileName', 'mode', 'isAccepted',
  'setAccepted', 'dialogAccept', 'dialogReject'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWebEngineFileDialogRequest::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickWebEngineFileDialogRequest::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickWebEngineFileDialogRequest::qt_qmlMarker_uncreatable()':
    one of Qt's own inner workings.
  - Qt's
    'QQuickWebEngineFileDialogRequest::~QQuickWebEngineFileDialogRequest()':
    the destructor: Python never removes a C++
    QQuickWebEngineFileDialogRequest.
  - Qt's 'QQuickWebEngineFileDialogRequest::QQuickWebEngineFileDialogRequest(
    QSharedPointer<QtWebEngineCore::FilePickerController> controller, QObject
    *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickWebEngineFileDialogRequest is created at the first use, not
    by 'QQuickWebEngineFileDialogRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWebEngineFileDialogRequest.
  - Qt tells when it has removed the C++ QQuickWebEngineFileDialogRequest.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickWebEngineFileDialogRequest that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickWebEngineFileDialogRequest, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class FileMode(CuteNum):
    """
    The enum 'QQuickWebEngineFileDialogRequest::FileMode' of Qt, with the 4
    names Qt gives in it.
    """

    FileModeOpen = Kee[int](0)
    FileModeOpenMultiple = Kee[int](1)
    FileModeUploadFolder = Kee[int](2)
    FileModeSave = Kee[int](3)

  class QmlIsUncreatable(CuteNum, scoped=True):
    """
    The enum 'QQuickWebEngineFileDialogRequest::QmlIsUncreatable' of Qt, with
    the 1 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    yes = Kee[int](1)

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
    Calls Qt's 'QString QQuickWebEngineFileDialogRequest::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefiledialogrequest.html#tr

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
    #  QString QQuickWebEngineFileDialogRequest::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN32QQuickWebEngineFileDialogRequest2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWebEngineFileDialogRequest'

  #  A C++ QQuickWebEngineFileDialogRequest Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWebEngineFileDialogRequest'

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
    *QQuickWebEngineFileDialogRequest::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefiledialogrequest.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWebEngineFileDialogRequest::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickWebEngineFileDialogRequest10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def acceptedMimeTypes(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QQuickWebEngineFileDialogRequest::acceptedMimeTypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefiledialogrequest.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickWebEngineFileDialogRequest::acceptedMimeTypes()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickWebEngineFileDialogRequest17acceptedMimeTypesEv',
    )
    return QStringList._cuteOwning(address)

  def defaultFileName(self) -> str:
    """
    Calls Qt's 'QString QQuickWebEngineFileDialogRequest::defaultFileName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefiledialogrequest.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickWebEngineFileDialogRequest::defaultFileName() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickWebEngineFileDialogRequest15defaultFileNameEv',
    )

  def mode(self) -> FileMode:
    """
    Calls Qt's 'FileMode QQuickWebEngineFileDialogRequest::mode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefiledialogrequest.html#mode

    Returns
    -------

    FileMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FileMode(number)' gives.
    """
    #  FileMode QQuickWebEngineFileDialogRequest::mode() const
    return QQuickWebEngineFileDialogRequest.FileMode(self.uglySide.call(
        'ritual_ZNK32QQuickWebEngineFileDialogRequest4modeEv',
    ))

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QQuickWebEngineFileDialogRequest::isAccepted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefiledialogrequest.html#isAccepted
    """
    #  bool QQuickWebEngineFileDialogRequest::isAccepted() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickWebEngineFileDialogRequest10isAcceptedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void QQuickWebEngineFileDialogRequest::setAccepted(bool
    accepted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefiledialogrequest.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void QQuickWebEngineFileDialogRequest::setAccepted(bool accepted)
    self.uglySide.call(
        'ritual_ZN32QQuickWebEngineFileDialogRequest11setAcceptedEb',
        accepted,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickWebEngineFileDialogRequest::QQuickWebEngineFileDialogRequest(
    QSharedPointer<QtWebEngineCore::FilePickerController> controller, QObject
    *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickWebEngineFileDialogRequest.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickWebEngineFileDialogRequest::QQuickWebEngineFileDialogRequest"
        "(QSharedPointer<QtWebEngineCore::FilePickerController> controller, "
        "QObject *parent)': takes a type Python has no way to hand over yet."
    )

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

  @overload(QStringList)
  def dialogAccept(self, files: QStringList) -> None:
    """
    Calls Qt's 'void QQuickWebEngineFileDialogRequest::dialogAccept(const
    QStringList &files)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefiledialogrequest.html#dialogAccept

    Parameters
    ----------

    files : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickWebEngineFileDialogRequest::dialogAccept(const QStringList
    #      &files)
    self.uglySide.call(
        'ritual_ZN32QQuickWebEngineFileDialogRequest12dialogAcceptERK5QList'
        'I7QStringE',
        self._valueOf(files),
    )

  def dialogReject(self) -> None:
    """
    Calls Qt's 'void QQuickWebEngineFileDialogRequest::dialogReject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwebenginefiledialogrequest.html#dialogReject
    """
    #  void QQuickWebEngineFileDialogRequest::dialogReject()
    self.uglySide.call(
        'ritual_ZN32QQuickWebEngineFileDialogRequest12dialogRejectEv',
    )

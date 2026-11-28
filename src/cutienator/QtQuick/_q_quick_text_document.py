"""
QQuickTextDocument binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquicktextdocument.h, Qt 6.12.0. Changes made here are lost.
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
  from ..QtGui import QTextDocument
  from . import QQuickItem, QQuickTextDocumentPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']
  QTextDocument = WAIT['QTextDocument']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextDocument(QObject):
  """
  The cute side of Qt's QQuickTextDocument: a plain Python object standing in
  front of one C++ QQuickTextDocument.

  It is built on the cute 'QObject', as Qt's QQuickTextDocument is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextDocument that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'source',
  'setSource', 'isModified', 'setModified', 'textDocument',
  'setTextDocument', 'save', 'saveAs', 'status', 'errorString',
  'textDocumentChanged', 'sourceChanged', 'modifiedChanged', 'statusChanged',
  'errorStringChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTextDocument::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickTextDocument::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickTextDocument::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'const QQuickTextDocumentPrivate *QQuickTextDocument::d_func()
    const': takes in Python what 'QQuickTextDocumentPrivate
    *QQuickTextDocument::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTextDocument is created at the first use, not by
    'QQuickTextDocument(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextDocument.
  - Qt tells when it has removed the C++ QQuickTextDocument. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickTextDocument, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum, scoped=True):
    """
    The enum 'QQuickTextDocument::Status' of Qt, with the 8 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Null = Kee[int](0)
    Loading = Kee[int](1)
    Loaded = Kee[int](2)
    Saving = Kee[int](3)
    Saved = Kee[int](4)
    ReadError = Kee[int](5)
    WriteError = Kee[int](6)
    NonLocalFileError = Kee[int](7)

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
    Calls Qt's 'QString QQuickTextDocument::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextdocument.html#tr

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
    #  QString QQuickTextDocument::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickTextDocument2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextDocument'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTextDocument::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextdocument.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTextDocument::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickTextDocument10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickTextDocument::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextdocument.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickTextDocument::source() const
    address = self.uglySide.call('ritual_ZNK18QQuickTextDocument6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isModified(self) -> bool:
    """
    Calls Qt's 'bool QQuickTextDocument::isModified() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextdocument.html#isModified
    """
    #  bool QQuickTextDocument::isModified() const
    return self.uglySide.call('ritual_ZNK18QQuickTextDocument10isModifiedEv')

  def textDocument(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QQuickTextDocument::textDocument() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocument.html#textDocument

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QQuickTextDocument::textDocument() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickTextDocument12textDocumentEv',
    )
    from ..QtGui import QTextDocument
    return QTextDocument._cuteAt(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuickTextDocument::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextdocument.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuickTextDocument::status() const
    return QQuickTextDocument.Status(self.uglySide.call(
        'ritual_ZNK18QQuickTextDocument6statusEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QQuickTextDocument::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocument.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTextDocument::errorString() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickTextDocument11errorStringEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQuickTextDocument::setSource(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextdocument.html#setSource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickTextDocument::setSource(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN18QQuickTextDocument9setSourceERK4QUrl',
        self._valueOf(url),
    )

  @overload(bool)
  def setModified(self, modified: bool) -> None:
    """
    Calls Qt's 'void QQuickTextDocument::setModified(bool modified)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocument.html#setModified

    Parameters
    ----------

    modified : bool
      Passed on as it is.
    """
    #  void QQuickTextDocument::setModified(bool modified)
    self.uglySide.call(
        'ritual_ZN18QQuickTextDocument11setModifiedEb', modified,
    )

  @overload(QTextDocument)
  @overload(NoneType)
  def setTextDocument(self, document: Optional[QTextDocument]) -> None:
    """
    Calls Qt's 'void QQuickTextDocument::setTextDocument(QTextDocument
    *document)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocument.html#setTextDocument

    Parameters
    ----------

    document : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextDocument::setTextDocument(QTextDocument *document)
    self.uglySide.call(
        'ritual_ZN18QQuickTextDocument15setTextDocumentEP13QTextDocument',
        self._addressOf(document),
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

  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickTextDocument::QQuickTextDocument(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocument.html#QQuickTextDocument

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickTextDocument::QQuickTextDocument(QQuickItem *parent)
    self._noteCreation(QQuickTextDocument, lambda: Rituals.call(
        'ritual_ZN18QQuickTextDocumentC1EP10QQuickItem',
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

  def save(self) -> None:
    """
    Calls Qt's 'void QQuickTextDocument::save()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextdocument.html#save
    """
    #  void QQuickTextDocument::save()
    self.uglySide.call('ritual_ZN18QQuickTextDocument4saveEv')

  @overload(QUrl)
  def saveAs(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QQuickTextDocument::saveAs(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextdocument.html#saveAs

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickTextDocument::saveAs(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN18QQuickTextDocument6saveAsERK4QUrl', self._valueOf(url),
    )

  def textDocumentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextDocument::textDocumentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocument.html#textDocumentChanged
    """
    #  void QQuickTextDocument::textDocumentChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickTextDocument19textDocumentChangedEv',
    )

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextDocument::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocument.html#sourceChanged
    """
    #  void QQuickTextDocument::sourceChanged()
    self.uglySide.call('ritual_ZN18QQuickTextDocument13sourceChangedEv')

  def modifiedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextDocument::modifiedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocument.html#modifiedChanged
    """
    #  void QQuickTextDocument::modifiedChanged()
    self.uglySide.call('ritual_ZN18QQuickTextDocument15modifiedChangedEv')

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextDocument::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocument.html#statusChanged
    """
    #  void QQuickTextDocument::statusChanged()
    self.uglySide.call('ritual_ZN18QQuickTextDocument13statusChangedEv')

  def errorStringChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTextDocument::errorStringChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocument.html#errorStringChanged
    """
    #  void QQuickTextDocument::errorStringChanged()
    self.uglySide.call('ritual_ZN18QQuickTextDocument18errorStringChangedEv')

  def d_func(self) -> Optional[QQuickTextDocumentPrivate]:
    """
    Calls Qt's 'QQuickTextDocumentPrivate *QQuickTextDocument::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextdocument.html#d_func

    Returns
    -------

    Optional[QQuickTextDocumentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextDocumentPrivate *QQuickTextDocument::d_func()
    address = self.uglySide.call('ritual_ZN18QQuickTextDocument6d_funcEv')
    from . import QQuickTextDocumentPrivate
    return QQuickTextDocumentPrivate._cuteAt(address)

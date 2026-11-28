"""
QQuickTextDocumentPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktextdocument_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTextDocumentPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QQuickTextDocument

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
  from ..QtGui import QTextDocument
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextDocument = WAIT['QTextDocument']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextDocumentPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickTextDocumentPrivate: a plain Python object
  standing in front of one C++ QQuickTextDocumentPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQuickTextDocumentPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextDocumentPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'q_func', 'get', 'writeTo',
  'document', 'setDocument', 'setStatus'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickTextDocument *QQuickTextDocumentPrivate::q_func()
    const': takes in Python what 'QQuickTextDocument
    *QQuickTextDocumentPrivate::q_func()' takes.
  - Qt's 'const QQuickTextDocumentPrivate
    *QQuickTextDocumentPrivate::get(const QQuickTextDocument *doc)': takes in
    Python what 'QQuickTextDocumentPrivate
    *QQuickTextDocumentPrivate::get(QQuickTextDocument *doc)' takes.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickTextDocumentPrivate is created at the first use, not by
    'QQuickTextDocumentPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextDocumentPrivate.
  - Each name of Qt's QQuickTextDocumentPrivate that has no cute function
    yet, 'load', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickTextDocument)
  @overload(NoneType)
  def get(
      doc: Optional[QQuickTextDocument],
  ) -> Optional[QQuickTextDocumentPrivate]:
    """
    Calls Qt's 'QQuickTextDocumentPrivate
    *QQuickTextDocumentPrivate::get(QQuickTextDocument *doc)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktextdocumentprivate.html#get

    Parameters
    ----------

    doc : Optional[QQuickTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTextDocumentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextDocumentPrivate
    #      *QQuickTextDocumentPrivate::get(QQuickTextDocument *doc)
    address = Rituals.call(
        'ritual_ZN25QQuickTextDocumentPrivate3getEP18QQuickTextDocument',
        CuteMixin._addressOf(doc),
    )
    return QQuickTextDocumentPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTextDocumentPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def document(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QQuickTextDocumentPrivate::document() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocumentprivate.html#document

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QQuickTextDocumentPrivate::document() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickTextDocumentPrivate8documentEv',
    )
    from ..QtGui import QTextDocument
    return QTextDocument._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextDocument)
  @overload(NoneType)
  def setDocument(self, doc: Optional[QTextDocument]) -> None:
    """
    Calls Qt's 'void QQuickTextDocumentPrivate::setDocument(QTextDocument
    *doc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocumentprivate.html#setDocument

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTextDocumentPrivate::setDocument(QTextDocument *doc)
    self.uglySide.call(
        'ritual_ZN25QQuickTextDocumentPrivate11setDocumentEP13QTextDocument',
        self._addressOf(doc),
    )

  @overload(QQuickTextDocument.Status, str)
  def setStatus(self, s: QQuickTextDocument.Status, err: str) -> None:
    """
    Calls Qt's 'void
    QQuickTextDocumentPrivate::setStatus(QQuickTextDocument::Status s, const
    QString &err)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocumentprivate.html#setStatus

    Parameters
    ----------

    s : QQuickTextDocument.Status
      Passed on as its number.

    err : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTextDocumentPrivate::setStatus(QQuickTextDocument::Status
    #      s, const QString &err)
    self.uglySide.call(
        'ritual_ZN25QQuickTextDocumentPrivate9setStatusEN18QQuickTextDocume'
        'nt6StatusERK7QString',
        s.value, err,
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

  def q_func(self) -> Optional[QQuickTextDocument]:
    """
    Calls Qt's 'QQuickTextDocument *QQuickTextDocumentPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocumentprivate.html#q_func

    Returns
    -------

    Optional[QQuickTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTextDocument *QQuickTextDocumentPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QQuickTextDocumentPrivate6q_funcEv',
    )
    return QQuickTextDocument._cuteAt(address)

  @overload(QUrl)
  def writeTo(self, fileUrl: QUrl) -> None:
    """
    Calls Qt's 'void QQuickTextDocumentPrivate::writeTo(const QUrl
    &fileUrl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextdocumentprivate.html#writeTo

    Parameters
    ----------

    fileUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickTextDocumentPrivate::writeTo(const QUrl &fileUrl)
    self.uglySide.call(
        'ritual_ZN25QQuickTextDocumentPrivate7writeToERK4QUrl',
        self._valueOf(fileUrl),
    )

  @staticmethod
  def load(*__, **_) -> Never:
    """
    Qt's 'void QQuickTextDocumentPrivate::load()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'lcTextDoc'.
    """
    raise NotImplementedError(
        "'QQuickTextDocumentPrivate.load' has no cute function yet. Qt's "
        "'void QQuickTextDocumentPrivate::load()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'lcTextDoc'.")

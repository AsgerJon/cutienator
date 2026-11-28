"""
QTextImageHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qtextimagehandler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QTextImageHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QTextObjectInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF, QSizeF
  from . import QImage, QPainter, QTextDocument, QTextFormat
  from . import QTextImageFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']
  QTextDocument = WAIT['QTextDocument']
  QTextFormat = WAIT['QTextFormat']
  QTextImageFormat = WAIT['QTextImageFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextImageHandler(QObject, QTextObjectInterface):
  """
  The cute side of Qt's QTextImageHandler: a plain Python object standing in
  front of one C++ QTextImageHandler.

  It is built on the cute 'QObject', as Qt's QTextImageHandler is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QTextObjectInterface' as well, as Qt's QTextImageHandler is built on Qt's
  QTextObjectInterface too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextImageHandler that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'tr', 'intrinsicSize',
  'drawObject', 'image'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTextImageHandler::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QTextImageHandler::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QTextImageHandler is created at the first use, not by
    'QTextImageHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextImageHandler.
  - Qt tells when it has removed the C++ QTextImageHandler. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QTextImageHandler::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimagehandler.html#tr

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
    #  QString QTextImageHandler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QTextImageHandler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextImageHandler'

  #  Qt's QTextImageHandler is built on more than one class. The part of a
  #  C++ QTextImageHandler that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QTextObjectInterface':
          'ritual_cast_QTextImageHandler_QTextObjectInterface',
  }

  #  A C++ QTextImageHandler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextImageHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTextImageHandler::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimagehandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTextImageHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QTextImageHandler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QTextImageHandler::QTextImageHandler(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextimagehandler.html#QTextImageHandler

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTextImageHandler::QTextImageHandler(QObject *parent)
    self._noteCreation(QTextImageHandler, lambda: Rituals.call(
        'ritual_ZN17QTextImageHandlerC1EP7QObject',
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

  @overload(QTextDocument, int, QTextFormat)
  @overload(NoneType, int, QTextFormat)
  def intrinsicSize(
      self,
      doc: Optional[QTextDocument],
      posInDocument: int,
      format: QTextFormat,
  ) -> QSizeF:
    """
    Calls Qt's 'QSizeF QTextImageHandler::intrinsicSize(QTextDocument *doc,
    int posInDocument, const QTextFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextimagehandler.html#intrinsicSize

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    posInDocument : int
      Passed on as it is.

    format : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QTextImageHandler::intrinsicSize(QTextDocument *doc, int
    #      posInDocument, const QTextFormat &format)
    ritual = (
        'ritual_ZN17QTextImageHandler13intrinsicSizeEP13QTextDocumentiRK11Q'
        'TextFormat')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QTextImageHandler13intrinsicSizeEP13QTextDocument'
          'iRK11QTextFormat')
    address = self.uglySide.call(
        ritual, self._addressOf(doc), posInDocument, self._valueOf(format),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @overload(QPainter, QRectF, QTextDocument, int, QTextFormat)
  @overload(QPainter, QRectF, NoneType, int, QTextFormat)
  @overload(NoneType, QRectF, QTextDocument, int, QTextFormat)
  @overload(NoneType, QRectF, NoneType, int, QTextFormat)
  def drawObject(
      self,
      p: Optional[QPainter],
      rect: QRectF,
      doc: Optional[QTextDocument],
      posInDocument: int,
      format: QTextFormat,
  ) -> None:
    """
    Calls Qt's 'void QTextImageHandler::drawObject(QPainter *p, const QRectF
    &rect, QTextDocument *doc, int posInDocument, const QTextFormat
    &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimagehandler.html#drawObject

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    posInDocument : int
      Passed on as it is.

    format : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  void QTextImageHandler::drawObject(QPainter *p, const QRectF &rect,
    #      QTextDocument *doc, int posInDocument, const QTextFormat &format)
    ritual = (
        'ritual_ZN17QTextImageHandler10drawObjectEP8QPainterRK6QRectFP13QTe'
        'xtDocumentiRK11QTextFormat')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QTextImageHandler10drawObjectEP8QPainterRK6QRectF'
          'P13QTextDocumentiRK11QTextFormat')
    self.uglySide.call(
        ritual,
        self._addressOf(p), self._valueOf(rect), self._addressOf(doc),
        posInDocument, self._valueOf(format),
    )

  @overload(QTextDocument, QTextImageFormat)
  @overload(NoneType, QTextImageFormat)
  def image(
      self,
      doc: Optional[QTextDocument],
      imageFormat: QTextImageFormat,
  ) -> QImage:
    """
    Calls Qt's 'QImage QTextImageHandler::image(QTextDocument *doc, const
    QTextImageFormat &imageFormat)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextimagehandler.html#image

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    imageFormat : QTextImageFormat
      Passed on as a value: Qt reads the C++ QTextImageFormat, which stays
      Python's own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QTextImageHandler::image(QTextDocument *doc, const
    #      QTextImageFormat &imageFormat)
    address = self.uglySide.call(
        'ritual_ZN17QTextImageHandler5imageEP13QTextDocumentRK16QTextImageF'
        'ormat',
        self._addressOf(doc), self._valueOf(imageFormat),
    )
    from . import QImage
    return QImage._cuteOwning(address)

"""
QQuickTextImageHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktextdocument_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTextImageHandler to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from ..QtGui import QTextObjectInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QSizeF
  from ..QtGui import QPainter, QTextDocument, QTextFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QRectF = WAIT['QRectF']
  QTextDocument = WAIT['QTextDocument']
  QTextFormat = WAIT['QTextFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTextImageHandler(QObject, QTextObjectInterface):
  """
  The cute side of Qt's QQuickTextImageHandler: a plain Python object
  standing in front of one C++ QQuickTextImageHandler.

  It is built on the cute 'QObject', as Qt's QQuickTextImageHandler is built
  on Qt's QObject, and has everything that class has. It is built on the cute
  'QTextObjectInterface' as well, as Qt's QQuickTextImageHandler is built on
  Qt's QTextObjectInterface too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTextImageHandler that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'intrinsicSize',
  'drawObject'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTextImageHandler::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickTextImageHandler::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTextImageHandler::~QQuickTextImageHandler()': the destructor:
    Python never removes a C++ QQuickTextImageHandler.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 2 not a gap; 2 leans on
  'QQuickTextImageHandler.

  What to expect
  --------------

  - The C++ QQuickTextImageHandler is created at the first use, not by
    'QQuickTextImageHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTextImageHandler.
  - Qt tells when it has removed the C++ QQuickTextImageHandler. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickTextImageHandler that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QQuickTextImageHandler'

  #  Qt's QQuickTextImageHandler is built on more than one class. The part of
  #  a C++ QQuickTextImageHandler that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QTextObjectInterface':
          'ritual_cast_QQuickTextImageHandler_QTextObjectInterface',
  }

  #  A C++ QQuickTextImageHandler Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTextImageHandler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTextImageHandler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextimagehandler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTextImageHandler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickTextImageHandler10metaObjectEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickTextImageHandler::QQuickTextImageHandler(QObject *parent)':
    leans on 'QQuickTextImageHandler::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickTextImageHandler.__init__' has no cute function yet. Qt's "
        "'QQuickTextImageHandler::QQuickTextImageHandler(QObject *parent)': "
        "leans on 'QQuickTextImageHandler::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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
    Calls Qt's 'QSizeF QQuickTextImageHandler::intrinsicSize(QTextDocument
    *doc, int posInDocument, const QTextFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextimagehandler.html#intrinsicSize

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
    #  QSizeF QQuickTextImageHandler::intrinsicSize(QTextDocument *doc, int
    #      posInDocument, const QTextFormat &format)
    ritual = (
        'ritual_ZN22QQuickTextImageHandler13intrinsicSizeEP13QTextDocumenti'
        'RK11QTextFormat')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTextImageHandler13intrinsicSizeEP13QTextDoc'
          'umentiRK11QTextFormat')
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
      a0: Optional[QPainter],
      a1: QRectF,
      a2: Optional[QTextDocument],
      a3: int,
      a4: QTextFormat,
  ) -> None:
    """
    Calls Qt's 'void QQuickTextImageHandler::drawObject(QPainter *a0, const
    QRectF &a1, QTextDocument *a2, int a3, const QTextFormat &a4)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktextimagehandler.html#drawObject

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    a2 : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a3 : int
      Passed on as it is.

    a4 : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  void QQuickTextImageHandler::drawObject(QPainter *a0, const QRectF
    #      &a1, QTextDocument *a2, int a3, const QTextFormat &a4)
    ritual = (
        'ritual_ZN22QQuickTextImageHandler10drawObjectEP8QPainterRK6QRectFP'
        '13QTextDocumentiRK11QTextFormat')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickTextImageHandler10drawObjectEP8QPainterRK6Q'
          'RectFP13QTextDocumentiRK11QTextFormat')
    self.uglySide.call(
        ritual,
        self._addressOf(a0), self._valueOf(a1), self._addressOf(a2), a3,
        self._valueOf(a4),
    )

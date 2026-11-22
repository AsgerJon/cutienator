"""
QTextObjectInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qabstracttextdocumentlayout.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF, QSizeF
  from . import QPainter, QTextDocument, QTextFormat
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


class QTextObjectInterface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextObjectInterface: a plain Python object standing
  in front of one C++ QTextObjectInterface.

  What exists
  -----------

  Every function of Qt's QTextObjectInterface that has a ritual and that
  Python can call so far, 2 names in all: 'intrinsicSize', 'drawObject'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextObjectInterface::~QTextObjectInterface()': the destructor:
    Python never removes a C++ QTextObjectInterface.

  What to expect
  --------------

  - The C++ QTextObjectInterface is created at the first use, not by
    'QTextObjectInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextObjectInterface.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextObjectInterface'

  #  A C++ QTextObjectInterface Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextObjectInterface'

  #  The functions Qt calls itself that QTextObjectInterface is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'intrinsicSize': (
          ('_ZN20QTextObjectInterface13intrinsicSizeEP13QTextDocumentiRK11Q'
           'TextFormat',
           ('address', 'value', 'QtCore:QSizeF'),
           (
               ('address', 'address', 'QtGui:QTextDocument'),
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QTextFormat'),
           )),
      ),
      'drawObject': (
          ('_ZN20QTextObjectInterface10drawObjectEP8QPainterRK6QRectFP13QTe'
           'xtDocumentiRK11QTextFormat',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtCore:QRectF'),
               ('address', 'address', 'QtGui:QTextDocument'),
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QTextFormat'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QSizeF QTextObjectInterface::intrinsicSize(QTextDocument
    *doc, int posInDocument, const QTextFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextobjectinterface.html#intrinsicSize

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
    #  QSizeF QTextObjectInterface::intrinsicSize(QTextDocument *doc, int
    #      posInDocument, const QTextFormat &format)
    address = self.uglySide.call(
        'ritual_ZN20QTextObjectInterface13intrinsicSizeEP13QTextDocumentiRK'
        '11QTextFormat',
        self._addressOf(doc), posInDocument, self._valueOf(format),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @overload(QPainter, QRectF, QTextDocument, int, QTextFormat)
  @overload(QPainter, QRectF, NoneType, int, QTextFormat)
  @overload(NoneType, QRectF, QTextDocument, int, QTextFormat)
  @overload(NoneType, QRectF, NoneType, int, QTextFormat)
  def drawObject(
      self,
      painter: Optional[QPainter],
      rect: QRectF,
      doc: Optional[QTextDocument],
      posInDocument: int,
      format: QTextFormat,
  ) -> None:
    """
    Calls Qt's 'void QTextObjectInterface::drawObject(QPainter *painter,
    const QRectF &rect, QTextDocument *doc, int posInDocument, const
    QTextFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextobjectinterface.html#drawObject

    Parameters
    ----------

    painter : Optional[QPainter]
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
    #  void QTextObjectInterface::drawObject(QPainter *painter, const QRectF
    #      &rect, QTextDocument *doc, int posInDocument, const QTextFormat
    #      &format)
    self.uglySide.call(
        'ritual_ZN20QTextObjectInterface10drawObjectEP8QPainterRK6QRectFP13'
        'QTextDocumentiRK11QTextFormat',
        self._addressOf(painter), self._valueOf(rect), self._addressOf(doc),
        posInDocument, self._valueOf(format),
    )

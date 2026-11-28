"""
QSGRhiInternalTextNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgrhiinternaltextnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGRhiInternalTextNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtGui import QTextCharFormat
from . import QSGInternalTextNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGRhiInternalTextNode(QSGInternalTextNode):
  """
  The cute side of Qt's QSGRhiInternalTextNode: a plain Python object
  standing in front of one C++ QSGRhiInternalTextNode.

  It is built on the cute 'QSGInternalTextNode', as Qt's
  QSGRhiInternalTextNode is built on Qt's QSGInternalTextNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGRhiInternalTextNode that has a ritual and that
  Python can call so far, 1 name in all: 'addDecorationNode'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has no ritual
  ------------------

  1 of the 2 functions Qt declares: 1 leans on 'QSGRhiInternalTextNode.

  What to expect
  --------------

  - The C++ QSGRhiInternalTextNode is created at the first use, not by
    'QSGRhiInternalTextNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGRhiInternalTextNode.
  - Each name of Qt's QSGRhiInternalTextNode that has no cute function yet,
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
  __qt_class__ = 'QSGRhiInternalTextNode'

  #  A C++ QSGRhiInternalTextNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGRhiInternalTextNode'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSGRhiInternalTextNode::QSGRhiInternalTextNode(QSGRenderContext
    *renderContext)': leans on
    'QSGRhiInternalTextNode::addDecorationNode(QRectF const&, QColor const&,
    QTextCharFormat::UnderlineStyle, QSGInternalTextNode::RecycleBin*)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QSGRhiInternalTextNode.__init__' has no cute function yet. Qt's "
        "'QSGRhiInternalTextNode::QSGRhiInternalTextNode(QSGRenderContext "
        "*renderContext)': leans on "
        "'QSGRhiInternalTextNode::addDecorationNode(QRectF const&, QColor "
        "const&, QTextCharFormat::UnderlineStyle, "
        "QSGInternalTextNode::RecycleBin*)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(
      QRectF, QColor, QTextCharFormat.UnderlineStyle,
      QSGInternalTextNode.RecycleBin,
  )
  @overload(QRectF, QColor, QTextCharFormat.UnderlineStyle, NoneType)
  def addDecorationNode(
      self,
      rect: QRectF,
      color: QColor,
      style: QTextCharFormat.UnderlineStyle,
      recycleBin: Optional[QSGInternalTextNode.RecycleBin],
  ) -> None:
    """
    Calls Qt's 'void QSGRhiInternalTextNode::addDecorationNode(const QRectF
    &rect, const QColor &color, QTextCharFormat::UnderlineStyle style,
    RecycleBin *recycleBin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgrhiinternaltextnode.html#addDecorationNode

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    style : QTextCharFormat.UnderlineStyle
      Passed on as its number.

    recycleBin : Optional[QSGInternalTextNode.RecycleBin]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGRhiInternalTextNode::addDecorationNode(const QRectF &rect,
    #      const QColor &color, QTextCharFormat::UnderlineStyle style,
    #      RecycleBin *recycleBin)
    self.uglySide.call(
        'ritual_ZN22QSGRhiInternalTextNode17addDecorationNodeERK6QRectFRK6Q'
        'ColorN15QTextCharFormat14UnderlineStyleEPN19QSGInternalTextNode10R'
        'ecycleBinE',
        self._valueOf(rect), self._valueOf(color), style.value,
        self._addressOf(recycleBin),
    )

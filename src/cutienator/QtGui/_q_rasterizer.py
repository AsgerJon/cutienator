"""
QRasterizer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrasterizer_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QRasterizer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QRasterizer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRasterizer: a plain Python object standing in front
  of one C++ QRasterizer.

  C++ hands a QRasterizer around as a copy, so every C++ QRasterizer behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QRasterizer yet. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRasterizer::~QRasterizer()': the destructor: Python removes its
    C++ QRasterizer by it, and has no other use for it.

  What has no ritual
  ------------------

  7 of the 8 functions Qt declares: 7 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QRasterizer is created at the first use, not by
    'QRasterizer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRasterizer back gives a copy the ritual made for
    Python, in a new cute QRasterizer.
  - Each name of Qt's QRasterizer that has no cute function yet, '__init__',
    'initialize', 'rasterize', 'rasterizeLine', 'setAntialiased',
    'setClipRect', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRasterizer'

  #  Qt's '~QRasterizer()'. Naming it makes this a value class: Python owns
  #  every C++ QRasterizer behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QRasterizerD1Ev'

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
    Qt's 'QRasterizer::QRasterizer()': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: allocation
    of incomplete type 'QRasterizerPrivate'.
    """
    raise NotImplementedError(
        "'QRasterizer.__init__' has no cute function yet. Qt's "
        "'QRasterizer::QRasterizer()': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "allocation of incomplete type 'QRasterizerPrivate'.")

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

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'void QRasterizer::initialize(ProcessSpans blend, void *data)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QRasterizerPrivate'.
    """
    raise NotImplementedError(
        "'QRasterizer.initialize' has no cute function yet. Qt's 'void "
        "QRasterizer::initialize(ProcessSpans blend, void *data)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QRasterizerPrivate'.")

  @staticmethod
  def rasterize(*__, **_) -> Never:
    """
    - Qt's 'void QRasterizer::rasterize(const QT_FT_Outline *outline,
      Qt::FillRule fillRule)': Qt's library has no name for it, and its code
      in Qt's source does not compile apart from its file: member access into
      incomplete type 'QRasterizerPrivate'.
    - Qt's 'void QRasterizer::rasterize(const QPainterPath &path,
      Qt::FillRule fillRule)': Qt's library has no name for it, and its code
      in Qt's source does not compile apart from its file: unknown type name
      'QSpanBuffer'.
    """
    raise NotImplementedError(
        "'QRasterizer.rasterize' has no cute function yet. Qt's 'void "
        "QRasterizer::rasterize(const QT_FT_Outline *outline, Qt::FillRule "
        "fillRule)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QRasterizerPrivate'. Qt's 'void "
        "QRasterizer::rasterize(const QPainterPath &path, Qt::FillRule "
        "fillRule)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'QSpanBuffer'.")

  @staticmethod
  def rasterizeLine(*__, **_) -> Never:
    """
    Qt's 'void QRasterizer::rasterizeLine(const QPointF &a, const QPointF &b,
    qreal width, bool squareCap)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: member access
    into incomplete type 'QRasterizerPrivate'.
    """
    raise NotImplementedError(
        "'QRasterizer.rasterizeLine' has no cute function yet. Qt's 'void "
        "QRasterizer::rasterizeLine(const QPointF &a, const QPointF &b, "
        "qreal width, bool squareCap)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QRasterizerPrivate'.")

  @staticmethod
  def setAntialiased(*__, **_) -> Never:
    """
    Qt's 'void QRasterizer::setAntialiased(bool antialiased)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'QRasterizerPrivate'.
    """
    raise NotImplementedError(
        "'QRasterizer.setAntialiased' has no cute function yet. Qt's 'void "
        "QRasterizer::setAntialiased(bool antialiased)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QRasterizerPrivate'.")

  @staticmethod
  def setClipRect(*__, **_) -> Never:
    """
    Qt's 'void QRasterizer::setClipRect(const QRect &clipRect)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'QRasterizerPrivate'.
    """
    raise NotImplementedError(
        "'QRasterizer.setClipRect' has no cute function yet. Qt's 'void "
        "QRasterizer::setClipRect(const QRect &clipRect)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QRasterizerPrivate'.")

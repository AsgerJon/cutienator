"""
QQuickStyledText binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickstyledtext_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickStyledText to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQuickStyledText(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickStyledText: a plain Python object standing in
  front of one C++ QQuickStyledText.

  What exists
  -----------

  No function of Qt's QQuickStyledText yet. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickStyledText::~QQuickStyledText()': the destructor: Python
    never removes a C++ QQuickStyledText.

  What has no ritual
  ------------------

  2 of the 3 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QQuickStyledTextPrivate.

  What to expect
  --------------

  - The C++ QQuickStyledText is created at the first use, not by
    'QQuickStyledText(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStyledText.
  - Each name of Qt's QQuickStyledText that has no cute function yet,
    '__init__', 'parse', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStyledText'

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
    Qt's 'QQuickStyledText::QQuickStyledText(const QString &string,
    QTextLayout &layout, QList<QQuickStyledTextImgTag *> &imgTags, const QUrl
    &baseUrl, QQmlContext *context, bool preloadImages, bool
    *fontSizeModified)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: allocation of
    incomplete type 'QQuickStyledTextPrivate'.
    """
    raise NotImplementedError(
        "'QQuickStyledText.__init__' has no cute function yet. Qt's "
        "'QQuickStyledText::QQuickStyledText(const QString &string, "
        "QTextLayout &layout, QList<QQuickStyledTextImgTag *> &imgTags, "
        "const QUrl &baseUrl, QQmlContext *context, bool preloadImages, "
        "bool *fontSizeModified)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: "
        "allocation of incomplete type 'QQuickStyledTextPrivate'.")

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
  def parse(*__, **_) -> Never:
    """
    Qt's 'void QQuickStyledText::parse(const QString &string, QTextLayout
    &layout, QList<QQuickStyledTextImgTag *> &imgTags, const QUrl &baseUrl,
    QQmlContext *context, bool preloadImages, bool *fontSizeModified)': leans
    on 'QQuickStyledTextPrivate::slash', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickStyledText.parse' has no cute function yet. Qt's 'void "
        "QQuickStyledText::parse(const QString &string, QTextLayout "
        "&layout, QList<QQuickStyledTextImgTag *> &imgTags, const QUrl "
        "&baseUrl, QQmlContext *context, bool preloadImages, bool "
        "*fontSizeModified)': leans on 'QQuickStyledTextPrivate::slash', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

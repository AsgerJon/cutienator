"""
QXmlStreamAttributes binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QXmlStreamAttributes(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlStreamAttributes: a plain Python object standing
  in front of one C++ QXmlStreamAttributes.

  C++ hands a QXmlStreamAttributes around as a copy, so every C++
  QXmlStreamAttributes behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QXmlStreamAttributes that has a ritual and that
  Python can call so far, 3 names in all: 'value', 'append', 'hasAttribute'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlStreamAttributes::~QXmlStreamAttributes()': the destructor:
    Python removes its C++ QXmlStreamAttributes by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QXmlStreamAttributes is created at the first use, not by
    'QXmlStreamAttributes(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QXmlStreamAttributes back gives a copy the ritual
    made for Python, in a new cute QXmlStreamAttributes.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlStreamAttributes'

  #  Qt's '~QXmlStreamAttributes()'. Naming it makes this a value class:
  #  Python owns every C++ QXmlStreamAttributes behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QXmlStreamAttributesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, str)
  def value(self, namespaceUri: str, name: str) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamAttributes::value(QAnyStringView
    namespaceUri, QAnyStringView name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamattributes.html#value

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamAttributes::value(QAnyStringView namespaceUri,
    #      QAnyStringView name) const
    return self.uglySide.call(
        'ritual_ZNK20QXmlStreamAttributes5valueE14QAnyStringViewS0_',
        namespaceUri, name,
    )

  @overload(str)
  def value(self, qualifiedName: str) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamAttributes::value(QAnyStringView
    qualifiedName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamattributes.html#value

    Parameters
    ----------

    qualifiedName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamAttributes::value(QAnyStringView qualifiedName)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QXmlStreamAttributes5valueE14QAnyStringView',
        qualifiedName,
    )

  @overload(str)
  def hasAttribute(self, qualifiedName: str) -> bool:
    """
    Calls Qt's 'bool QXmlStreamAttributes::hasAttribute(QAnyStringView
    qualifiedName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamattributes.html#hasAttribute

    Parameters
    ----------

    qualifiedName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlStreamAttributes::hasAttribute(QAnyStringView qualifiedName)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QXmlStreamAttributes12hasAttributeE14QAnyStringView',
        qualifiedName,
    )

  @overload(str, str)
  def hasAttribute(self, namespaceUri: str, name: str) -> bool:
    """
    Calls Qt's 'bool QXmlStreamAttributes::hasAttribute(QAnyStringView
    namespaceUri, QAnyStringView name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamattributes.html#hasAttribute

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlStreamAttributes::hasAttribute(QAnyStringView namespaceUri,
    #      QAnyStringView name) const
    return self.uglySide.call(
        'ritual_ZNK20QXmlStreamAttributes12hasAttributeE14QAnyStringViewS0_',
        namespaceUri, name,
    )

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QXmlStreamAttributes::QXmlStreamAttributes()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamattributes.html#QXmlStreamAttributes
    """
    #  QXmlStreamAttributes::QXmlStreamAttributes()
    self._noteCreation(QXmlStreamAttributes, lambda: Rituals.call(
        'ritual_ZN20QXmlStreamAttributesC1Ev',
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

  @overload(str, str, str)
  def append(self, namespaceUri: str, name: str, value: str) -> None:
    """
    Calls Qt's 'void QXmlStreamAttributes::append(const QString
    &namespaceUri, const QString &name, const QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamattributes.html#append

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamAttributes::append(const QString &namespaceUri, const
    #      QString &name, const QString &value)
    self.uglySide.call(
        'ritual_ZN20QXmlStreamAttributes6appendERK7QStringS2_S2_',
        namespaceUri, name, value,
    )

  @overload(str, str)
  def append(self, qualifiedName: str, value: str) -> None:
    """
    Calls Qt's 'void QXmlStreamAttributes::append(const QString
    &qualifiedName, const QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamattributes.html#append

    Parameters
    ----------

    qualifiedName : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamAttributes::append(const QString &qualifiedName, const
    #      QString &value)
    self.uglySide.call(
        'ritual_ZN20QXmlStreamAttributes6appendERK7QStringS2_',
        qualifiedName, value,
    )

"""
QTextObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QTextDocument, QTextFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTextDocument = WAIT['QTextDocument']
  QTextFormat = WAIT['QTextFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextObject(QObject):
  """
  The cute side of Qt's QTextObject: a plain Python object standing in front
  of one C++ QTextObject.

  It is built on the cute 'QObject', as Qt's QTextObject is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextObject that has a ritual and that Python can
  call so far, 7 names in all: 'metaObject', 'tr', 'setFormat', 'format',
  'formatIndex', 'document', 'objectIndex'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextObject::~QTextObject()': the destructor: Python never removes
    a C++ QTextObject.

  What has no ritual
  ------------------

  9 of the 18 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QTextObject is created at the first use, not by
    'QTextObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextObject.
  - Qt tells when it has removed the C++ QTextObject. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QTextObject::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextobject.html#tr

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
    #  QString QTextObject::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QTextObject2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextObject'

  #  A C++ QTextObject Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTextObject::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextobject.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTextObject::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QTextObject10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def format(self) -> QTextFormat:
    """
    Calls Qt's 'QTextFormat QTextObject::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextobject.html#format

    Returns
    -------

    QTextFormat
      A new cute QTextFormat around the copy Qt gave back. Python owns it.
    """
    #  QTextFormat QTextObject::format() const
    address = self.uglySide.call('ritual_ZNK11QTextObject6formatEv')
    from . import QTextFormat
    return QTextFormat._cuteOwning(address)

  def formatIndex(self) -> int:
    """
    Calls Qt's 'int QTextObject::formatIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextobject.html#formatIndex
    """
    #  int QTextObject::formatIndex() const
    return self.uglySide.call('ritual_ZNK11QTextObject11formatIndexEv')

  def document(self) -> Optional[QTextDocument]:
    """
    Calls Qt's 'QTextDocument *QTextObject::document() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextobject.html#document

    Returns
    -------

    Optional[QTextDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextDocument *QTextObject::document() const
    address = self.uglySide.call('ritual_ZNK11QTextObject8documentEv')
    from . import QTextDocument
    return QTextDocument._cuteAt(address)

  def objectIndex(self) -> int:
    """
    Calls Qt's 'int QTextObject::objectIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextobject.html#objectIndex
    """
    #  int QTextObject::objectIndex() const
    return self.uglySide.call('ritual_ZNK11QTextObject11objectIndexEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QTextFormat)
  def setFormat(self, format: QTextFormat) -> None:
    """
    Calls Qt's 'void QTextObject::setFormat(const QTextFormat &format)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextobject.html#setFormat

    Parameters
    ----------

    format : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  void QTextObject::setFormat(const QTextFormat &format)
    self.uglySide.call(
        'ritual_ZN11QTextObject9setFormatERK11QTextFormat',
        self._valueOf(format),
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

  @overload(QTextDocument)
  @overload(NoneType)
  def __init__(self, doc: Optional[QTextDocument]) -> None:
    """
    Notes what was given, for Qt's 'QTextObject::QTextObject(QTextDocument
    *doc)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtextobject.html#QTextObject

    Parameters
    ----------

    doc : Optional[QTextDocument]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextObject::QTextObject(QTextDocument *doc)
    self._noteCreation(QTextObject, lambda: Rituals.call(
        'ritual_ZN11QTextObjectC1EP13QTextDocument', self._addressOf(doc),
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

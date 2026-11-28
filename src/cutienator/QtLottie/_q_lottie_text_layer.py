"""
QLottieTextLayer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottietextlayer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottieTextLayer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QLottieBase, QLottieLayer
from ..QtCore import QList, QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QJsonObject
  from ..QtGui import QPainterPath
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJsonObject = WAIT['QJsonObject']


class QLottieTextLayer(QLottieLayer):
  """
  The cute side of Qt's QLottieTextLayer: a plain Python object standing in
  front of one C++ QLottieTextLayer.

  It is built on the cute 'QLottieLayer', as Qt's QLottieTextLayer is built
  on Qt's QLottieLayer, and has everything that class has.

  C++ hands a QLottieTextLayer around as a copy, so every C++
  QLottieTextLayer behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QLottieTextLayer that has a ritual and that Python
  can call so far, 5 names in all: 'clone', 'parse', 'textDocument',
  'setCharData', 'buildGlyphPaths'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QLottieTextLayer::render(QLottieRenderer &renderer) const':
    takes a type Python has no way to hand over yet.
  - Qt's 'QLottieTextLayer::~QLottieTextLayer()': the destructor: Python
    removes its C++ QLottieTextLayer by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QLottieTextLayer is created at the first use, not by
    'QLottieTextLayer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QLottieTextLayer back gives a copy the ritual made
    for Python, in a new cute QLottieTextLayer.
  """

  #  The classes Qt writes inside QLottieTextLayer, each a class in here as
  #  in C++.

  class TextDocument(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QLottieTextLayer::TextDocument: a plain Python
    object standing in front of one C++ QLottieTextLayer::TextDocument.

    C++ hands a QLottieTextLayer::TextDocument around as a copy, so every C++
    QLottieTextLayer::TextDocument behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QLottieTextLayer::TextDocument yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QLottieTextLayer::TextDocument::~TextDocument()': the destructor:
      Python removes its C++ QLottieTextLayer::TextDocument by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QLottieTextLayer::TextDocument is created at the first use, not
      by 'QLottieTextLayer::TextDocument(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QLottieTextLayer::TextDocument back gives a copy
      the ritual made for Python, in a new cute
      QLottieTextLayer::TextDocument.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QLottieTextLayer::TextDocument'

    #  Qt's '~QLottieTextLayer::TextDocument()'. Naming it makes this a value
    #  class: Python owns every C++ QLottieTextLayer::TextDocument behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QLottieTextLayer12TextDocumentD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieTextLayer'

  #  Qt's '~QLottieTextLayer()'. Naming it makes this a value class: Python
  #  owns every C++ QLottieTextLayer behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QLottieTextLayerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QLottieBase]:
    """
    Calls Qt's 'QLottieBase *QLottieTextLayer::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottietextlayer.html#clone

    Returns
    -------

    Optional[QLottieBase]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLottieBase *QLottieTextLayer::clone() const
    ritual = 'ritual_ZNK16QLottieTextLayer5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QLottieTextLayer5cloneEv'
    address = self.uglySide.call(ritual)
    return QLottieBase._cuteAt(address)

  def textDocument(self) -> TextDocument:
    """
    Calls Qt's 'const TextDocument &QLottieTextLayer::textDocument() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottietextlayer.html#textDocument

    Returns
    -------

    TextDocument
      A new cute QLottieTextLayer::TextDocument around the copy Qt gave back.
      Python owns it.
    """
    #  const TextDocument &QLottieTextLayer::textDocument() const
    address = self.uglySide.call(
        'ritual_ZNK16QLottieTextLayer12textDocumentEv',
    )
    return QLottieTextLayer.TextDocument._cuteOwning(address)

  def buildGlyphPaths(self) -> QList[QPainterPath]:
    """
    Calls Qt's 'QList<QPainterPath> QLottieTextLayer::buildGlyphPaths()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottietextlayer.html#buildGlyphPaths

    Returns
    -------

    QList[QPainterPath]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPainterPath> QLottieTextLayer::buildGlyphPaths() const
    address = self.uglySide.call(
        'ritual_ZNK16QLottieTextLayer15buildGlyphPathsEv',
    )
    from ..QtGui import QPainterPath
    return QList[QPainterPath]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMap[str, QJsonObject])
  def setCharData(self, chars: QMap[str, QJsonObject]) -> None:
    """
    Calls Qt's 'void QLottieTextLayer::setCharData(const QMap<QString,
    QJsonObject> &chars)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottietextlayer.html#setCharData

    Parameters
    ----------

    chars : QMap[str, QJsonObject]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QLottieTextLayer::setCharData(const QMap<QString, QJsonObject>
    #      &chars)
    self.uglySide.call(
        'ritual_ZN16QLottieTextLayer11setCharDataERK4QMapI7QString11QJsonOb'
        'jectE',
        self._valueOf(chars),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QLottieTextLayer::QLottieTextLayer()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottietextlayer.html#QLottieTextLayer
    """
    #  QLottieTextLayer::QLottieTextLayer()
    self._noteCreation(QLottieTextLayer, lambda: Rituals.call(
        'ritual_ZN16QLottieTextLayerC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QLottieTextLayer) -> None:
    """
    Notes what was given, for Qt's 'QLottieTextLayer::QLottieTextLayer(const
    QLottieTextLayer &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottietextlayer.html#QLottieTextLayer

    Parameters
    ----------

    other : QLottieTextLayer
      Passed on as a value: Qt reads the C++ QLottieTextLayer, which stays
      Python's own.
    """
    #  QLottieTextLayer::QLottieTextLayer(const QLottieTextLayer &other)
    self._noteCreation(QLottieTextLayer, lambda: Rituals.call(
        'ritual_ZN16QLottieTextLayerC1ERKS_', self._valueOf(other),
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

  @overload(QJsonObject)
  def parse(self, definition: QJsonObject) -> int:
    """
    Calls Qt's 'int QLottieTextLayer::parse(const QJsonObject &definition)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottietextlayer.html#parse

    Parameters
    ----------

    definition : QJsonObject
      Passed on as a value: Qt reads the C++ QJsonObject, which stays
      Python's own.
    """
    #  int QLottieTextLayer::parse(const QJsonObject &definition)
    ritual = 'ritual_ZN16QLottieTextLayer5parseERK11QJsonObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QLottieTextLayer5parseERK11QJsonObject'
    return self.uglySide.call(ritual, self._valueOf(definition))

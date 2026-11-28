"""
QSGInternalImageNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGInternalImageNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGTexture, QSGVisitableNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRectF
  from . import QSGNodeVisitorEx
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QSGNodeVisitorEx = WAIT['QSGNodeVisitorEx']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGInternalImageNode(QSGVisitableNode):
  """
  The cute side of Qt's QSGInternalImageNode: a plain Python object standing
  in front of one C++ QSGInternalImageNode.

  It is built on the cute 'QSGVisitableNode', as Qt's QSGInternalImageNode is
  built on Qt's QSGVisitableNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGInternalImageNode that has a ritual and that
  Python can call so far, 13 names in all: 'setTargetRect',
  'setInnerTargetRect', 'setInnerSourceRect', 'setSubSourceRect',
  'setTexture', 'setAntialiasing', 'setMirror', 'setMipmapFiltering',
  'setFiltering', 'setHorizontalWrapMode', 'setVerticalWrapMode', 'update',
  'accept'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGInternalImageNode::~QSGInternalImageNode()': the destructor:
    Python never removes a C++ QSGInternalImageNode.

  What to expect
  --------------

  - The C++ QSGInternalImageNode is created at the first use, not by
    'QSGInternalImageNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGInternalImageNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGInternalImageNode'

  #  A C++ QSGInternalImageNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGInternalImageNode'

  #  The functions Qt calls itself that QSGInternalImageNode is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setTargetRect': (
          ('_ZN20QSGInternalImageNode13setTargetRectERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'setInnerTargetRect': (
          ('_ZN20QSGInternalImageNode18setInnerTargetRectERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'setInnerSourceRect': (
          ('_ZN20QSGInternalImageNode18setInnerSourceRectERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'setSubSourceRect': (
          ('_ZN20QSGInternalImageNode16setSubSourceRectERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'setTexture': (
          ('_ZN20QSGInternalImageNode10setTextureEP10QSGTexture',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QSGTexture'),
           )),
      ),
      'setAntialiasing': (
          ('_ZN20QSGInternalImageNode15setAntialiasingEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setMirror': (
          ('_ZN20QSGInternalImageNode9setMirrorEbb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'setMipmapFiltering': (
          ('_ZN20QSGInternalImageNode18setMipmapFilteringEN10QSGTexture9Fil'
           'teringE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QSGTexture.Filtering'),
           )),
      ),
      'setFiltering': (
          ('_ZN20QSGInternalImageNode12setFilteringEN10QSGTexture9Filtering'
           'E',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QSGTexture.Filtering'),
           )),
      ),
      'setHorizontalWrapMode': (
          ('_ZN20QSGInternalImageNode21setHorizontalWrapModeEN10QSGTexture8'
           'WrapModeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QSGTexture.WrapMode'),
           )),
      ),
      'setVerticalWrapMode': (
          ('_ZN20QSGInternalImageNode19setVerticalWrapModeEN10QSGTexture8Wr'
           'apModeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick:QSGTexture.WrapMode'),
           )),
      ),
      'update': (
          ('_ZN20QSGInternalImageNode6updateEv',
           ('nothing', 'nothing', ''),
           ()),
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

  @overload(QRectF)
  def setTargetRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGInternalImageNode::setTargetRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalimagenode.html#setTargetRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGInternalImageNode::setTargetRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN20QSGInternalImageNode13setTargetRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QRectF)
  def setInnerTargetRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGInternalImageNode::setInnerTargetRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalimagenode.html#setInnerTargetRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGInternalImageNode::setInnerTargetRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN20QSGInternalImageNode18setInnerTargetRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QRectF)
  def setInnerSourceRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGInternalImageNode::setInnerSourceRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalimagenode.html#setInnerSourceRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGInternalImageNode::setInnerSourceRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN20QSGInternalImageNode18setInnerSourceRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QRectF)
  def setSubSourceRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QSGInternalImageNode::setSubSourceRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalimagenode.html#setSubSourceRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QSGInternalImageNode::setSubSourceRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN20QSGInternalImageNode16setSubSourceRectERK6QRectF',
        self._valueOf(rect),
    )

  @overload(QSGTexture)
  @overload(NoneType)
  def setTexture(self, texture: Optional[QSGTexture]) -> None:
    """
    Calls Qt's 'void QSGInternalImageNode::setTexture(QSGTexture *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalimagenode.html#setTexture

    Parameters
    ----------

    texture : Optional[QSGTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGInternalImageNode::setTexture(QSGTexture *texture)
    self.uglySide.call(
        'ritual_ZN20QSGInternalImageNode10setTextureEP10QSGTexture',
        self._addressOf(texture),
    )

  @overload(bool)
  def setAntialiasing(self, antialiasing: bool) -> None:
    """
    Calls Qt's 'void QSGInternalImageNode::setAntialiasing(bool
    antialiasing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalimagenode.html#setAntialiasing

    Parameters
    ----------

    antialiasing : bool
      Passed on as it is.
    """
    #  void QSGInternalImageNode::setAntialiasing(bool antialiasing)
    ritual = 'ritual_ZN20QSGInternalImageNode15setAntialiasingEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QSGInternalImageNode15setAntialiasingEb'
    self.uglySide.call(ritual, antialiasing)

  @overload(bool, bool)
  def setMirror(self, horizontally: bool, vertically: bool) -> None:
    """
    Calls Qt's 'void QSGInternalImageNode::setMirror(bool horizontally, bool
    vertically)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalimagenode.html#setMirror

    Parameters
    ----------

    horizontally : bool
      Passed on as it is.

    vertically : bool
      Passed on as it is.
    """
    #  void QSGInternalImageNode::setMirror(bool horizontally, bool
    #      vertically)
    self.uglySide.call(
        'ritual_ZN20QSGInternalImageNode9setMirrorEbb',
        horizontally, vertically,
    )

  @overload(QSGTexture.Filtering)
  def setMipmapFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void
    QSGInternalImageNode::setMipmapFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalimagenode.html#setMipmapFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGInternalImageNode::setMipmapFiltering(QSGTexture::Filtering
    #      filtering)
    self.uglySide.call(
        'ritual_ZN20QSGInternalImageNode18setMipmapFilteringEN10QSGTexture9'
        'FilteringE',
        filtering.value,
    )

  @overload(QSGTexture.Filtering)
  def setFiltering(self, filtering: QSGTexture.Filtering) -> None:
    """
    Calls Qt's 'void QSGInternalImageNode::setFiltering(QSGTexture::Filtering
    filtering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalimagenode.html#setFiltering

    Parameters
    ----------

    filtering : QSGTexture.Filtering
      Passed on as its number.
    """
    #  void QSGInternalImageNode::setFiltering(QSGTexture::Filtering
    #      filtering)
    self.uglySide.call(
        'ritual_ZN20QSGInternalImageNode12setFilteringEN10QSGTexture9Filter'
        'ingE',
        filtering.value,
    )

  @overload(QSGTexture.WrapMode)
  def setHorizontalWrapMode(self, wrapMode: QSGTexture.WrapMode) -> None:
    """
    Calls Qt's 'void
    QSGInternalImageNode::setHorizontalWrapMode(QSGTexture::WrapMode
    wrapMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalimagenode.html#setHorizontalWrapMode

    Parameters
    ----------

    wrapMode : QSGTexture.WrapMode
      Passed on as its number.
    """
    #  void QSGInternalImageNode::setHorizontalWrapMode(QSGTexture::WrapMode
    #      wrapMode)
    self.uglySide.call(
        'ritual_ZN20QSGInternalImageNode21setHorizontalWrapModeEN10QSGTextu'
        're8WrapModeE',
        wrapMode.value,
    )

  @overload(QSGTexture.WrapMode)
  def setVerticalWrapMode(self, wrapMode: QSGTexture.WrapMode) -> None:
    """
    Calls Qt's 'void
    QSGInternalImageNode::setVerticalWrapMode(QSGTexture::WrapMode
    wrapMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsginternalimagenode.html#setVerticalWrapMode

    Parameters
    ----------

    wrapMode : QSGTexture.WrapMode
      Passed on as its number.
    """
    #  void QSGInternalImageNode::setVerticalWrapMode(QSGTexture::WrapMode
    #      wrapMode)
    self.uglySide.call(
        'ritual_ZN20QSGInternalImageNode19setVerticalWrapModeEN10QSGTexture'
        '8WrapModeE',
        wrapMode.value,
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

  def update(self) -> None:
    """
    Calls Qt's 'void QSGInternalImageNode::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qsginternalimagenode.html#update
    """
    #  void QSGInternalImageNode::update()
    self.uglySide.call('ritual_ZN20QSGInternalImageNode6updateEv')

  @overload(QSGNodeVisitorEx)
  @overload(NoneType)
  def accept(self, visitor: Optional[QSGNodeVisitorEx]) -> None:
    """
    Calls Qt's 'void QSGInternalImageNode::accept(QSGNodeVisitorEx
    *visitor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsginternalimagenode.html#accept

    Parameters
    ----------

    visitor : Optional[QSGNodeVisitorEx]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGInternalImageNode::accept(QSGNodeVisitorEx *visitor)
    ritual = 'ritual_ZN20QSGInternalImageNode6acceptEP16QSGNodeVisitorEx'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QSGInternalImageNode6acceptEP16QSGNodeVisitorEx')
    self.uglySide.call(ritual, self._addressOf(visitor))

"""
Qt3DRender::TextureDownloadRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qtexture_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::TextureDownloadRequest to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class TextureDownloadRequest(Qt3DCore.QDownloadRequest):
  """
  The cute side of Qt's Qt3DRender::TextureDownloadRequest: a plain Python
  object standing in front of one C++ Qt3DRender::TextureDownloadRequest.

  It is built on the cute 'Qt3DCore::QDownloadRequest', as Qt's
  Qt3DRender::TextureDownloadRequest is built on Qt's
  Qt3DCore::QDownloadRequest, and has everything that class has.

  C++ hands a Qt3DRender::TextureDownloadRequest around as a copy, so every
  C++ Qt3DRender::TextureDownloadRequest behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::TextureDownloadRequest that has a ritual
  and that Python can call so far, 1 name in all: 'onCompleted'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::TextureDownloadRequest::TextureDownloadRequest(const
    QTextureFromSourceGeneratorPtr &functor, const QUrl &url,
    Qt3DCore::QAspectEngine *engine, Qt3DCore::QNodeId texNodeId)': takes a
    type Python has no way to hand over yet.
  - Qt's 'Qt3DRender::TextureDownloadRequest::~TextureDownloadRequest()': the
    destructor: Python removes its C++ Qt3DRender::TextureDownloadRequest by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt3DRender::TextureDownloadRequest is created at the first use,
    not by 'Qt3DRender::TextureDownloadRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::TextureDownloadRequest back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::TextureDownloadRequest.
  - Each name of Qt's Qt3DRender::TextureDownloadRequest that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::TextureDownloadRequest'

  #  Qt's '~Qt3DRender::TextureDownloadRequest()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::TextureDownloadRequest
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender22TextureDownloadRequestD1Ev'

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
    Qt's 'Qt3DRender::TextureDownloadRequest::TextureDownloadRequest(const
    QTextureFromSourceGeneratorPtr &functor, const QUrl &url,
    Qt3DCore::QAspectEngine *engine, Qt3DCore::QNodeId texNodeId)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.TextureDownloadRequest.__init__' has no cute function "
        "yet. Qt's "
        "'Qt3DRender::TextureDownloadRequest::TextureDownloadRequest(const "
        "QTextureFromSourceGeneratorPtr &functor, const QUrl &url, "
        "Qt3DCore::QAspectEngine *engine, Qt3DCore::QNodeId texNodeId)': "
        "takes a type Python has no way to hand over yet.")

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

  def onCompleted(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::TextureDownloadRequest::onCompleted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-texturedownloadrequest.html#onCompleted
    """
    #  void Qt3DRender::TextureDownloadRequest::onCompleted()
    ritual = 'ritual_ZN10Qt3DRender22TextureDownloadRequest11onCompletedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender22TextureDownloadRequest11onCompletedEv')
    self.uglySide.call(ritual)

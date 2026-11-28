"""
QNativeInterface::QSGVulkanTexture binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgtexture_platform.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSGVulkanTexture(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QNativeInterface::QSGVulkanTexture: a plain Python
  object standing in front of one C++ QNativeInterface::QSGVulkanTexture.

  What exists
  -----------

  No function of Qt's QNativeInterface::QSGVulkanTexture yet. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNativeInterface::QSGVulkanTexture::~QSGVulkanTexture()': the
    destructor: Python never removes a C++
    QNativeInterface::QSGVulkanTexture.
  - Qt's 'VkImage QNativeInterface::QSGVulkanTexture::nativeImage() const':
    gives a type Python has no way to take yet.
  - Qt's 'VkImageLayout
    QNativeInterface::QSGVulkanTexture::nativeImageLayout() const': gives a
    type Python has no way to take yet.
  - Qt's 'QSGTexture *QNativeInterface::QSGVulkanTexture::fromNative(VkImage
    image, VkImageLayout layout, QQuickWindow *window, const QSize &size,
    QQuickWindow::CreateTextureOptions options)': names 'struct VkImage_T',
    which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 9 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QNativeInterface::QSGVulkanTexture is created at the first use,
    not by 'QNativeInterface::QSGVulkanTexture(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNativeInterface::QSGVulkanTexture.
  - Each name of Qt's QNativeInterface::QSGVulkanTexture that has no cute
    function yet, '__init__', 'fromNative', 'nativeImage',
    'nativeImageLayout', holds a function that raises 'NotImplementedError',
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
  __qt_class__ = 'QNativeInterface::QSGVulkanTexture'

  #  The functions Qt calls itself that QNativeInterface::QSGVulkanTexture is
  #  the first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'nativeImage': (
          'VkImage QNativeInterface::QSGVulkanTexture::nativeImage() const',
      ),
      'nativeImageLayout': (
          'VkImageLayout '
          'QNativeInterface::QSGVulkanTexture::nativeImageLayout() const',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QNativeInterface::QSGVulkanTexture::QSGVulkanTexture()': the class
    is abstract, so C++ cannot make one, and the C++ class of ours does not
    fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QNativeInterface.QSGVulkanTexture.__init__' has no cute function "
        "yet. Qt's "
        "'QNativeInterface::QSGVulkanTexture::QSGVulkanTexture()': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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
  def fromNative(*__, **_) -> Never:
    """
    Qt's 'QSGTexture *QNativeInterface::QSGVulkanTexture::fromNative(VkImage
    image, VkImageLayout layout, QQuickWindow *window, const QSize &size,
    QQuickWindow::CreateTextureOptions options)': names 'struct VkImage_T',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QSGVulkanTexture.fromNative' has no cute "
        "function yet. Qt's 'QSGTexture "
        "*QNativeInterface::QSGVulkanTexture::fromNative(VkImage image, "
        "VkImageLayout layout, QQuickWindow *window, const QSize &size, "
        "QQuickWindow::CreateTextureOptions options)': names 'struct "
        "VkImage_T', which has no cute class yet.")

  @staticmethod
  def nativeImage(*__, **_) -> Never:
    """
    Qt's 'VkImage QNativeInterface::QSGVulkanTexture::nativeImage() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QSGVulkanTexture.nativeImage' has no cute "
        "function yet. Qt's 'VkImage "
        "QNativeInterface::QSGVulkanTexture::nativeImage() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def nativeImageLayout(*__, **_) -> Never:
    """
    Qt's 'VkImageLayout
    QNativeInterface::QSGVulkanTexture::nativeImageLayout() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.QSGVulkanTexture.nativeImageLayout' has no cute "
        "function yet. Qt's 'VkImageLayout "
        "QNativeInterface::QSGVulkanTexture::nativeImageLayout() const': "
        "gives a type Python has no way to take yet.")

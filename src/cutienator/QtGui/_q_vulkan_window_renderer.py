"""
QVulkanWindowRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qvulkanwindow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute


class QVulkanWindowRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVulkanWindowRenderer: a plain Python object standing
  in front of one C++ QVulkanWindowRenderer.

  What exists
  -----------

  Every function of Qt's QVulkanWindowRenderer that has a ritual and that
  Python can call so far, 8 names in all: 'preInitResources',
  'initResources', 'initSwapChainResources', 'releaseSwapChainResources',
  'releaseResources', 'startNextFrame', 'physicalDeviceLost',
  'logicalDeviceLost'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVulkanWindowRenderer::~QVulkanWindowRenderer()': the destructor:
    Python never removes a C++ QVulkanWindowRenderer.

  What to expect
  --------------

  - The C++ QVulkanWindowRenderer is created at the first use, not by
    'QVulkanWindowRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVulkanWindowRenderer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVulkanWindowRenderer'

  #  A C++ QVulkanWindowRenderer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVulkanWindowRenderer'

  #  The functions Qt calls itself that QVulkanWindowRenderer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'preInitResources': (
          ('_ZN21QVulkanWindowRenderer16preInitResourcesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'initResources': (
          ('_ZN21QVulkanWindowRenderer13initResourcesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'initSwapChainResources': (
          ('_ZN21QVulkanWindowRenderer22initSwapChainResourcesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'releaseSwapChainResources': (
          ('_ZN21QVulkanWindowRenderer25releaseSwapChainResourcesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'releaseResources': (
          ('_ZN21QVulkanWindowRenderer16releaseResourcesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'startNextFrame': (
          ('_ZN21QVulkanWindowRenderer14startNextFrameEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'physicalDeviceLost': (
          ('_ZN21QVulkanWindowRenderer18physicalDeviceLostEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'logicalDeviceLost': (
          ('_ZN21QVulkanWindowRenderer17logicalDeviceLostEv',
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

  def preInitResources(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowRenderer::preInitResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowrenderer.html#preInitResources
    """
    #  void QVulkanWindowRenderer::preInitResources()
    ritual = 'ritual_ZN21QVulkanWindowRenderer16preInitResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QVulkanWindowRenderer16preInitResourcesEv'
    self.uglySide.call(ritual)

  def initResources(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowRenderer::initResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowrenderer.html#initResources
    """
    #  void QVulkanWindowRenderer::initResources()
    ritual = 'ritual_ZN21QVulkanWindowRenderer13initResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QVulkanWindowRenderer13initResourcesEv'
    self.uglySide.call(ritual)

  def initSwapChainResources(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowRenderer::initSwapChainResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowrenderer.html#initSwapChainResources
    """
    #  void QVulkanWindowRenderer::initSwapChainResources()
    ritual = 'ritual_ZN21QVulkanWindowRenderer22initSwapChainResourcesEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QVulkanWindowRenderer22initSwapChainResourcesEv')
    self.uglySide.call(ritual)

  def releaseSwapChainResources(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowRenderer::releaseSwapChainResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowrenderer.html
    """
    #  void QVulkanWindowRenderer::releaseSwapChainResources()
    ritual = 'ritual_ZN21QVulkanWindowRenderer25releaseSwapChainResourcesEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QVulkanWindowRenderer25releaseSwapChainResourcesE'
          'v')
    self.uglySide.call(ritual)

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowRenderer::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowrenderer.html#releaseResources
    """
    #  void QVulkanWindowRenderer::releaseResources()
    ritual = 'ritual_ZN21QVulkanWindowRenderer16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QVulkanWindowRenderer16releaseResourcesEv'
    self.uglySide.call(ritual)

  def startNextFrame(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowRenderer::startNextFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowrenderer.html#startNextFrame
    """
    #  void QVulkanWindowRenderer::startNextFrame()
    self.uglySide.call('ritual_ZN21QVulkanWindowRenderer14startNextFrameEv')

  def physicalDeviceLost(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowRenderer::physicalDeviceLost()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowrenderer.html#physicalDeviceLost
    """
    #  void QVulkanWindowRenderer::physicalDeviceLost()
    ritual = 'ritual_ZN21QVulkanWindowRenderer18physicalDeviceLostEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QVulkanWindowRenderer18physicalDeviceLostEv'
    self.uglySide.call(ritual)

  def logicalDeviceLost(self) -> None:
    """
    Calls Qt's 'void QVulkanWindowRenderer::logicalDeviceLost()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvulkanwindowrenderer.html#logicalDeviceLost
    """
    #  void QVulkanWindowRenderer::logicalDeviceLost()
    ritual = 'ritual_ZN21QVulkanWindowRenderer17logicalDeviceLostEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QVulkanWindowRenderer17logicalDeviceLostEv'
    self.uglySide.call(ritual)

"""
QtMultimediaPrivate stands for the namespace 'QtMultimediaPrivate' of Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.NamespaceGenerator from the records of Qt 6.12.0.
#  Changes made here are lost.
from __future__ import annotations

from worktoy.keenum import Kee

from ..cute import CuteNum


class QtMultimediaPrivate:
  """
  The namespace 'QtMultimediaPrivate' of Qt, which holds no objects. It holds
  the 4 enums Qt writes in it, each under its name, and the 0 names Qt has
  for the combinations of a flags enum, each holding the class of that enum.
  It is never made into an object.
  """

  class AudioEndpointRole(CuteNum, scoped=True):
    """
    The enum 'QtMultimediaPrivate::AudioEndpointRole' of Qt, with the 4 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    MediaPlayback = Kee[int](0)
    SoundEffect = Kee[int](1)
    Accessibility = Kee[int](2)
    Other = Kee[int](3)

  class DRMFormat(CuteNum, scoped=True):
    """
    The enum 'QtMultimediaPrivate::DRMFormat' of Qt, with the 25 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    RGBA8888 = Kee[int](875708754)
    RGB888 = Kee[int](875710290)
    RG88 = Kee[int](943212370)
    ARGB8888 = Kee[int](875713089)
    ABGR8888 = Kee[int](875708993)
    BGRA8888 = Kee[int](875708738)
    BGR888 = Kee[int](875710274)
    GR88 = Kee[int](943215175)
    R8 = Kee[int](538982482)
    R16 = Kee[int](540422482)
    RGB565 = Kee[int](909199186)
    RG1616 = Kee[int](842221394)
    GR1616 = Kee[int](842224199)
    BGRA1010102 = Kee[int](808665410)
    YUYV = Kee[int](1448695129)
    UYVY = Kee[int](1498831189)
    AYUV = Kee[int](1448433985)
    NV12 = Kee[int](842094158)
    NV21 = Kee[int](825382478)
    P010 = Kee[int](808530000)
    YUV411 = Kee[int](825316697)
    YUV420 = Kee[int](842093913)
    YVU420 = Kee[int](842094169)
    YUV422 = Kee[int](909202777)
    YUV444 = Kee[int](875713881)

  class FailureSeverity(CuteNum, scoped=True):
    """
    The enum 'QtMultimediaPrivate::FailureSeverity' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    recoverable = Kee[int](0)
    unrecoverable = Kee[int](1)

  class VoicePlayResult(CuteNum, scoped=True):
    """
    The enum 'QtMultimediaPrivate::VoicePlayResult' of Qt, with the 2 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Playing = Kee[int](0)
    Finished = Kee[int](1)

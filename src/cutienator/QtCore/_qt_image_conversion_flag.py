"""
ImageConversionFlag stands for the flags enum 'Qt::ImageConversionFlag' of
Qt.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.EnumGenerator from the records of
#  QtCore/qnamespace.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from ..cute import CuteFlags


class ImageConversionFlag(CuteFlags):
  """
  The flags enum 'Qt::ImageConversionFlag' of Qt, with the 19 names Qt gives
  in it. Qt names the type of its combinations 'Qt::ImageConversionFlags'.
  """

  ColorMode_Mask = 0x3
  AutoColor = 0x0
  ColorOnly = 0x3
  MonoOnly = 0x2
  AlphaDither_Mask = 0xc
  ThresholdAlphaDither = 0x0
  OrderedAlphaDither = 0x4
  DiffuseAlphaDither = 0x8
  NoAlpha = 0xc
  Dither_Mask = 0x30
  DiffuseDither = 0x0
  OrderedDither = 0x10
  ThresholdDither = 0x20
  DitherMode_Mask = 0xc0
  AutoDither = 0x0
  PreferDither = 0x40
  AvoidDither = 0x80
  NoOpaqueDetection = 0x100
  NoFormatConversion = 0x200

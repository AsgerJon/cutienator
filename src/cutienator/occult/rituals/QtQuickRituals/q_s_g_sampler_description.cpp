//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsgtexture_p.h"
#include "qsgtexture_platform.h"
#include <private/qqmlglobal_p.h>
#include <private/qsgmaterialshader_p.h>
#include <private/qsgrenderer_p.h>
#include <private/qquickitem_p.h> // qquickwindow_p.h cannot be included on its own due to template nonsense
#include <private/qquickwindow_p.h>
#include <QtCore/private/qnativeinterface_p.h>
#include <rhi/qrhi.h>
#if defined(CAN_BACKTRACE_EXECINFO)
#include <execinfo.h>
#include <QHash>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgtexture.cpp, line 62, as _ZN21QSGSamplerDescription11fromTextureEP10QSGTexture
inline QSGSamplerDescription QSGSamplerDescription::fromTexture(QSGTexture *t)
{
    QSGSamplerDescription s;
    s.filtering = t->filtering();
    s.mipmapFiltering = t->mipmapFiltering();
    s.horizontalWrap = t->horizontalWrapMode();
    s.verticalWrap = t->verticalWrapMode();
    s.anisotropylevel = t->anisotropyLevel();
    return s;
}
//  -----------------------------------------------------------------------

//  QSGSamplerDescription QSGSamplerDescription::fromTexture(QSGTexture *t)
extern "C" Q_DECL_EXPORT
QSGSamplerDescription *ritual_ZN21QSGSamplerDescription11fromTextureEP10QSGTexture(
    QSGTexture *t) {
  return new QSGSamplerDescription(QSGSamplerDescription::fromTexture(t));
}

//  QSGSamplerDescription::~QSGSamplerDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSGSamplerDescriptionD1Ev(QSGSamplerDescription *self) {
  delete self;
}

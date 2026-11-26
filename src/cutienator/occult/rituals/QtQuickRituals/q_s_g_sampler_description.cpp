//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQuick/qsgtexture_platform.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQuick/private/qsgmaterialshader_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick/private/qquickitem_p.h> // qquickwindow_p.h cannot be included on its own due to template nonsense
#include <QtQuick/private/qquickwindow_p.h>
#include <QtCore/private/qnativeinterface_p.h>
#include <QtGui/rhi/qrhi.h>
#if defined(CAN_BACKTRACE_EXECINFO)
#include <execinfo.h>
#include <QtCore/QHash>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

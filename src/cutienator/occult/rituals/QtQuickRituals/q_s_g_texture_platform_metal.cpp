//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(metal)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGTexturePlatformMetal::QSGTexturePlatformMetal(QSGTexture *t)
extern "C" Q_DECL_EXPORT
QSGTexturePlatformMetal *ritual_ZN23QSGTexturePlatformMetalC1EP10QSGTexture(
    QSGTexture *t) {
  return new QSGTexturePlatformMetal(t);
}

#endif  // QT_CONFIG(metal)

//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgtexture_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#if QT_CONFIG(metal) || defined(Q_QDOC)
#include <QtQuick/QtQuick>
#include <QtQuick/qsgtexture_platform.h>

//  QNativeInterface::QSGMetalTexture::~QSGMetalTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface15QSGMetalTextureD1Ev(
    QNativeInterface::QSGMetalTexture *self) {
  delete self;
}

#endif  // QT_CONFIG(metal) || defined(Q_QDOC)

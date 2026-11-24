//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickpixmapcache_p.h>
#include <QtQuick/private/qquickimageprovider_p.h>
#include <QtQuick/private/qquickprofiler_p.h>
#include <QtQuick/private/qsgcontext_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick/private/qsgtexturereader_p.h>
#include <QtQuick/qquickwindow.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qimage_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/qimagereader.h>
#include <QtGui/qpixmapcache.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/qqmlfile.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qhash.h>
#include <QtCore/qfile.h>
#include <QtCore/qthread.h>
#include <QtCore/qmutex.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qscopeguard.h>
#if QT_CONFIG(qml_network)
#include <QtQml/qqmlnetworkaccessmanagerfactory.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtNetwork/qsslerror.h>
#endif
#include <private/qdebug_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickpixmapcache.cpp, line 136, as _ZNK27QQuickDefaultTextureFactory13createTextureEP12QQuickWindow
inline QSGTexture *QQuickDefaultTextureFactory::createTexture(QQuickWindow *window) const
{
    QSGTexture *t = window->createTextureFromImage(im, QQuickWindow::TextureCanUseAtlas);
    static bool transient = qEnvironmentVariableIsSet("QSG_TRANSIENT_IMAGES");
    if (transient)
        const_cast<QQuickDefaultTextureFactory *>(this)->im = QImage();
    return t;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickDefaultTextureFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuickDefaultTextureFactory10metaObjectEv(
    const QQuickDefaultTextureFactory *self) {
  return self->metaObject();
}

//  QSGTexture *QQuickDefaultTextureFactory::createTexture(QQuickWindow
//      *window) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK27QQuickDefaultTextureFactory13createTextureEP12QQuickWindow(
    const QQuickDefaultTextureFactory *self,
    QQuickWindow *window) {
  return self->createTexture(window);
}

//  QSize QQuickDefaultTextureFactory::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK27QQuickDefaultTextureFactory11textureSizeEv(
    const QQuickDefaultTextureFactory *self) {
  return new QSize(self->textureSize());
}

//  int QQuickDefaultTextureFactory::textureByteCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QQuickDefaultTextureFactory16textureByteCountEv(
    const QQuickDefaultTextureFactory *self) {
  return self->textureByteCount();
}

//  QImage QQuickDefaultTextureFactory::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK27QQuickDefaultTextureFactory5imageEv(
    const QQuickDefaultTextureFactory *self) {
  return new QImage(self->image());
}

//  QSGTexture *QQuickDefaultTextureFactory::createTexture(QQuickWindow
//      *window) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK27QQuickDefaultTextureFactory13createTextureEP12QQuickWindow(
    const QQuickDefaultTextureFactory *self,
    QQuickWindow *window) {
  return self->QQuickDefaultTextureFactory::createTexture(window);
}

//  QSize QQuickDefaultTextureFactory::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK27QQuickDefaultTextureFactory11textureSizeEv(
    const QQuickDefaultTextureFactory *self) {
  return new QSize(self->QQuickDefaultTextureFactory::textureSize());
}

//  int QQuickDefaultTextureFactory::textureByteCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK27QQuickDefaultTextureFactory16textureByteCountEv(
    const QQuickDefaultTextureFactory *self) {
  return self->QQuickDefaultTextureFactory::textureByteCount();
}

//  QImage QQuickDefaultTextureFactory::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK27QQuickDefaultTextureFactory5imageEv(
    const QQuickDefaultTextureFactory *self) {
  return new QImage(self->QQuickDefaultTextureFactory::image());
}

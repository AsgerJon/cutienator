//  Written by dev_tooling.RitualGenerator from the records of QtWebEngineQui
//  ck/6.12.0/QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qtwebenginequickglobal_p.h>
#include <QtWebEngineQuick/QtWebEngineQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/6.12.0/QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qsize.h>
#include <QtGui/qpixmap.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebEngineQuick/private/qquickwebenginefaviconprovider_p_p.h>
#include <QtWebEngineQuick/qquickwebengineprofile.h>
#include <QtWebEngineQuick/private/qquickwebenginesettings_p.h>
#include <QtCore/qmimedatabase.h>
#include <QtGui/qicon.h>
#include <QtGui/qpixmap.h>
#include <QtCore/QThread>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebengine/src/webenginequick/api/qquickwebenginefaviconprovider.cpp, line 237, as _ZNK20FaviconImageResponse14textureFactoryEv
inline QQuickTextureFactory *FaviconImageResponse::textureFactory() const
{
    return QQuickTextureFactory::textureFactoryForImage(m_image);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *FaviconImageResponse::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20FaviconImageResponse10metaObjectEv(
    const FaviconImageResponse *self) {
  return self->metaObject();
}

//  void *FaviconImageResponse::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20FaviconImageResponse11qt_metacastEPKc(
    FaviconImageResponse *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int FaviconImageResponse::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20FaviconImageResponse11qt_metacallEN11QMetaObject4CallEiPPv(
    FaviconImageResponse *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuickTextureFactory *FaviconImageResponse::textureFactory() const
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_ZNK20FaviconImageResponse14textureFactoryEv(
    const FaviconImageResponse *self) {
  return self->textureFactory();
}

//  const QUrl &FaviconImageResponse::imageSource() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20FaviconImageResponse11imageSourceEv(
    const FaviconImageResponse *self) {
  return new QUrl(self->imageSource());
}

//  const QSize &FaviconImageResponse::requestedSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK20FaviconImageResponse13requestedSizeEv(
    const FaviconImageResponse *self) {
  return new QSize(self->requestedSize());
}

//  bool FaviconImageResponse::isIconUrl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20FaviconImageResponse9isIconUrlEv(
    const FaviconImageResponse *self) {
  return self->isIconUrl();
}

//  void FaviconImageResponse::handleDone(QPixmap pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN20FaviconImageResponse10handleDoneE7QPixmap(
    FaviconImageResponse *self,
    const QPixmap *pixmap) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "FaviconImageResponse")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleDone(QPixmap)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleDone(QPixmap)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(pixmap)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QQuickTextureFactory *FaviconImageResponse::textureFactory() const
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_own_ZNK20FaviconImageResponse14textureFactoryEv(
    const FaviconImageResponse *self) {
  return self->FaviconImageResponse::textureFactory();
}

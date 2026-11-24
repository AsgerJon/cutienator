//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpixmap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtGui/qcolorspace.h>

//  QString QQuickPixmap::tr(const char *sourceText, const char
//      *disambiguation, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQuickPixmap2trEPKcS1_i(
    const char *sourceText,
    const char *disambiguation,
    int n) {
  return new QString(QQuickPixmap::tr(sourceText, disambiguation, n));
}

//  QQuickPixmap::QQuickPixmap()
extern "C" Q_DECL_EXPORT
QQuickPixmap *ritual_ZN12QQuickPixmapC1Ev() {
  return new QQuickPixmap();
}

//  QQuickPixmap::QQuickPixmap(QQmlEngine *a0, const QUrl &a1)
extern "C" Q_DECL_EXPORT
QQuickPixmap *ritual_ZN12QQuickPixmapC1EP10QQmlEngineRK4QUrl(
    QQmlEngine *a0,
    const QUrl *a1) {
  return new QQuickPixmap(a0, *a1);
}

//  QQuickPixmap::QQuickPixmap(QQmlEngine *a0, const QUrl &a1, Options
//      options)
extern "C" Q_DECL_EXPORT
QQuickPixmap *ritual_ZN12QQuickPixmapC1EP10QQmlEngineRK4QUrl6QFlagsINS_6OptionEE(
    QQmlEngine *a0,
    const QUrl *a1,
    int options) {
  return new QQuickPixmap(
      a0,
      *a1,
      QFlags<QQuickPixmap::Option>::fromInt(options));
}

//  QQuickPixmap::QQuickPixmap(QQmlEngine *a0, const QUrl &a1, const QRect
//      &region, const QSize &a3)
extern "C" Q_DECL_EXPORT
QQuickPixmap *ritual_ZN12QQuickPixmapC1EP10QQmlEngineRK4QUrlRK5QRectRK5QSize(
    QQmlEngine *a0,
    const QUrl *a1,
    const QRect *region,
    const QSize *a3) {
  return new QQuickPixmap(a0, *a1, *region, *a3);
}

//  QQuickPixmap::QQuickPixmap(const QUrl &a0, const QImage &image)
extern "C" Q_DECL_EXPORT
QQuickPixmap *ritual_ZN12QQuickPixmapC1ERK4QUrlRK6QImage(
    const QUrl *a0,
    const QImage *image) {
  return new QQuickPixmap(*a0, *image);
}

//  QQuickPixmap::~QQuickPixmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickPixmapD1Ev(QQuickPixmap *self) {
  delete self;
}

//  bool QQuickPixmap::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickPixmap6isNullEv(const QQuickPixmap *self) {
  return self->isNull();
}

//  bool QQuickPixmap::isReady() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickPixmap7isReadyEv(const QQuickPixmap *self) {
  return self->isReady();
}

//  bool QQuickPixmap::isError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickPixmap7isErrorEv(const QQuickPixmap *self) {
  return self->isError();
}

//  bool QQuickPixmap::isLoading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQuickPixmap9isLoadingEv(const QQuickPixmap *self) {
  return self->isLoading();
}

//  Status QQuickPixmap::status() const
extern "C" Q_DECL_EXPORT
QQuickPixmap::Status ritual_ZNK12QQuickPixmap6statusEv(
    const QQuickPixmap *self) {
  return self->status();
}

//  QString QQuickPixmap::error() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQuickPixmap5errorEv(const QQuickPixmap *self) {
  return new QString(self->error());
}

//  const QUrl &QQuickPixmap::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QQuickPixmap3urlEv(const QQuickPixmap *self) {
  return new QUrl(self->url());
}

//  const QSize &QQuickPixmap::implicitSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QQuickPixmap12implicitSizeEv(const QQuickPixmap *self) {
  return new QSize(self->implicitSize());
}

//  const QRect &QQuickPixmap::requestRegion() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QQuickPixmap13requestRegionEv(const QQuickPixmap *self) {
  return new QRect(self->requestRegion());
}

//  const QSize &QQuickPixmap::requestSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QQuickPixmap11requestSizeEv(const QQuickPixmap *self) {
  return new QSize(self->requestSize());
}

//  QQuickImageProviderOptions::AutoTransform QQuickPixmap::autoTransform()
//      const
extern "C" Q_DECL_EXPORT
QQuickImageProviderOptions::AutoTransform ritual_ZNK12QQuickPixmap13autoTransformEv(
    const QQuickPixmap *self) {
  return self->autoTransform();
}

//  int QQuickPixmap::frameCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickPixmap10frameCountEv(const QQuickPixmap *self) {
  return self->frameCount();
}

//  QImage QQuickPixmap::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK12QQuickPixmap5imageEv(const QQuickPixmap *self) {
  return new QImage(self->image());
}

//  void QQuickPixmap::setImage(const QImage &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickPixmap8setImageERK6QImage(
    QQuickPixmap *self,
    const QImage *a0) {
  self->setImage(*a0);
}

//  QColorSpace QQuickPixmap::colorSpace() const
extern "C" Q_DECL_EXPORT
QColorSpace *ritual_ZNK12QQuickPixmap10colorSpaceEv(
    const QQuickPixmap *self) {
  return new QColorSpace(self->colorSpace());
}

//  QQuickTextureFactory *QQuickPixmap::textureFactory() const
extern "C" Q_DECL_EXPORT
QQuickTextureFactory *ritual_ZNK12QQuickPixmap14textureFactoryEv(
    const QQuickPixmap *self) {
  return self->textureFactory();
}

//  QRect QQuickPixmap::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QQuickPixmap4rectEv(const QQuickPixmap *self) {
  return new QRect(self->rect());
}

//  int QQuickPixmap::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickPixmap5widthEv(const QQuickPixmap *self) {
  return self->width();
}

//  int QQuickPixmap::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QQuickPixmap6heightEv(const QQuickPixmap *self) {
  return self->height();
}

//  void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickPixmap4loadEP10QQmlEngineRK4QUrl(
    QQuickPixmap *self,
    QQmlEngine *a0,
    const QUrl *a1) {
  self->load(a0, *a1);
}

//  void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1,
//      QQuickPixmap::Options options)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickPixmap4loadEP10QQmlEngineRK4QUrl6QFlagsINS_6OptionEE(
    QQuickPixmap *self,
    QQmlEngine *a0,
    const QUrl *a1,
    int options) {
  self->load(a0, *a1, QFlags<QQuickPixmap::Option>::fromInt(options));
}

//  void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1, const QRect
//      &requestRegion, const QSize &requestSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickPixmap4loadEP10QQmlEngineRK4QUrlRK5QRectRK5QSize(
    QQuickPixmap *self,
    QQmlEngine *a0,
    const QUrl *a1,
    const QRect *requestRegion,
    const QSize *requestSize) {
  self->load(a0, *a1, *requestRegion, *requestSize);
}

//  void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1, const QRect
//      &requestRegion, const QSize &requestSize, QQuickPixmap::Options
//      options)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickPixmap4loadEP10QQmlEngineRK4QUrlRK5QRectRK5QSize6QFlagsINS_6OptionEE(
    QQuickPixmap *self,
    QQmlEngine *a0,
    const QUrl *a1,
    const QRect *requestRegion,
    const QSize *requestSize,
    int options) {
  self->load(
      a0,
      *a1,
      *requestRegion,
      *requestSize,
      QFlags<QQuickPixmap::Option>::fromInt(options));
}

//  void QQuickPixmap::load(QQmlEngine *a0, const QUrl &a1, const QRect
//      &requestRegion, const QSize &requestSize, QQuickPixmap::Options
//      options, const QQuickImageProviderOptions &providerOptions, int
//      frame, int frameCount, qreal devicePixelRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickPixmap4loadEP10QQmlEngineRK4QUrlRK5QRectRK5QSize6QFlagsINS_6OptionEERK26QQuickImageProviderOptionsiid(
    QQuickPixmap *self,
    QQmlEngine *a0,
    const QUrl *a1,
    const QRect *requestRegion,
    const QSize *requestSize,
    int options,
    const QQuickImageProviderOptions *providerOptions,
    int frame,
    int frameCount,
    qreal devicePixelRatio) {
  self->load(
      a0,
      *a1,
      *requestRegion,
      *requestSize,
      QFlags<QQuickPixmap::Option>::fromInt(options),
      *providerOptions,
      frame,
      frameCount,
      devicePixelRatio);
}

//  void QQuickPixmap::loadImageFromDevice(QQmlEngine *engine, QIODevice
//      *device, const QUrl &url, const QRect &requestRegion, const QSize
//      &requestSize, const QQuickImageProviderOptions &providerOptions, int
//      frame, int frameCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickPixmap19loadImageFromDeviceEP10QQmlEngineP9QIODeviceRK4QUrlRK5QRectRK5QSizeRK26QQuickImageProviderOptionsii(
    QQuickPixmap *self,
    QQmlEngine *engine,
    QIODevice *device,
    const QUrl *url,
    const QRect *requestRegion,
    const QSize *requestSize,
    const QQuickImageProviderOptions *providerOptions,
    int frame,
    int frameCount) {
  self->loadImageFromDevice(
      engine,
      device,
      *url,
      *requestRegion,
      *requestSize,
      *providerOptions,
      frame,
      frameCount);
}

//  void QQuickPixmap::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickPixmap5clearEv(QQuickPixmap *self) {
  self->clear();
}

//  void QQuickPixmap::clear(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickPixmap5clearEP7QObject(
    QQuickPixmap *self,
    QObject *a0) {
  self->clear(a0);
}

//  bool QQuickPixmap::connectFinished(QObject *a0, const char *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickPixmap15connectFinishedEP7QObjectPKc(
    QQuickPixmap *self,
    QObject *a0,
    const char *a1) {
  return self->connectFinished(a0, a1);
}

//  bool QQuickPixmap::connectFinished(QObject *a0, int a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickPixmap15connectFinishedEP7QObjecti(
    QQuickPixmap *self,
    QObject *a0,
    int a1) {
  return self->connectFinished(a0, a1);
}

//  bool QQuickPixmap::connectDownloadProgress(QObject *a0, const char *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickPixmap23connectDownloadProgressEP7QObjectPKc(
    QQuickPixmap *self,
    QObject *a0,
    const char *a1) {
  return self->connectDownloadProgress(a0, a1);
}

//  bool QQuickPixmap::connectDownloadProgress(QObject *a0, int a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickPixmap23connectDownloadProgressEP7QObjecti(
    QQuickPixmap *self,
    QObject *a0,
    int a1) {
  return self->connectDownloadProgress(a0, a1);
}

//  void QQuickPixmap::purgeCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickPixmap10purgeCacheEv() {
  QQuickPixmap::purgeCache();
}

//  bool QQuickPixmap::isCached(const QUrl &url, const QRect &requestRegion,
//      const QSize &requestSize, const int frame, const
//      QQuickImageProviderOptions &options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickPixmap8isCachedERK4QUrlRK5QRectRK5QSizeiRK26QQuickImageProviderOptions(
    const QUrl *url,
    const QRect *requestRegion,
    const QSize *requestSize,
    int frame,
    const QQuickImageProviderOptions *options) {
  return QQuickPixmap::isCached(
      *url,
      *requestRegion,
      *requestSize,
      frame,
      *options);
}

//  bool QQuickPixmap::isScalableImageFormat(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQuickPixmap21isScalableImageFormatERK4QUrl(
    const QUrl *url) {
  return QQuickPixmap::isScalableImageFormat(*url);
}

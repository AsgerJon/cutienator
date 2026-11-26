//  Written by dev_tooling.RitualGenerator from the records of QtLabsSharedIm
//  age/6.12.0/QtLabsSharedImage/private/qsharedimageprovider_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLabsSharedImage/6.12.0/QtLabsSharedImage/private/qtlabssharedimageglobal_p.h>
#include <QtLabsSharedImage/QtLabsSharedImage>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsSharedImage/6.12.0/QtLabsSharedImage/private/qsharedimageprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsSharedImage/private/qsharedimageprovider_p.h>
#include <private/qquickpixmap_p.h>
#include <private/qimage_p.h>
#include <QImageReader>
#include <QFileInfo>
#include <QDir>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/sharedimage/qsharedimageprovider.cpp, line 18, as _ZN22QuickSharedImageLoader8loadFileERK7QStringP5QListI8QVariantE
inline QImage QuickSharedImageLoader::loadFile(const QString &path, ImageParameters *params)
{
    QImageReader imgio(path);
    QSize realSize = imgio.size();
    QSize requestSize;
    QQuickImageProviderOptions options;
    if (params) {
        requestSize = params->value(RequestedSize).toSize();
        options = params->value(ProviderOptions).value<QQuickImageProviderOptions>();
    }

    QSize scSize = QQuickImageProviderWithOptions::loadSize(imgio.size(), requestSize, imgio.format(), options);

    if (scSize.isValid())
        imgio.setScaledSize(scSize);

    QImage image;
    if (imgio.read(&image)) {
        if (realSize.isEmpty())
            realSize = image.size();
        // Make sure we have acceptable format for texture uploader, or it will convert & lose sharing
        // This mimics the testing & conversion normally done by the quick pixmapcache & texturefactory
        if (image.format() != QImage::Format_RGB32 && image.format() != QImage::Format_ARGB32_Premultiplied) {
            QImage::Format newFmt = QImage::Format_RGB32;
            if (image.hasAlphaChannel() && image.data_ptr()->checkForAlphaPixels())
                newFmt = QImage::Format_ARGB32_Premultiplied;
            qCDebug(lcSharedImage) << "Convert on load from format" << image.format() << "to" << newFmt;
            image = image.convertToFormat(newFmt);
        }
    }

    if (params && params->size() > OriginalSize)
        params->replace(OriginalSize, realSize);

    return image;
}

//  from ../qtdeclarative/src/labs/sharedimage/qsharedimageprovider.cpp, line 55, as _ZN22QuickSharedImageLoader3keyERK7QStringP5QListI8QVariantE
inline QString QuickSharedImageLoader::key(const QString &path, ImageParameters *params)
{
    QSize reqSz;
    QQuickImageProviderOptions opts;
    if (params) {
        reqSz = params->value(RequestedSize).toSize();
        opts = params->value(ProviderOptions).value<QQuickImageProviderOptions>();
    }
    if (!reqSz.isValid())
        return path;
    int aspect = opts.preserveAspectRatioCrop() || opts.preserveAspectRatioFit() ? 1 : 0;

    QString key = path + QStringLiteral("_%1x%2_%3").arg(reqSz.width()).arg(reqSz.height()).arg(aspect);
    qCDebug(lcSharedImage) << "KEY:" << key;
    return key;
}
//  -----------------------------------------------------------------------

//  A QuickSharedImageLoader that Python can take functions over in. Every QuickSharedImageLoader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QImage * (*CuteQuickSharedImageLoaderCall0)(const void *, const QString *, QSharedImageLoader::ImageParameters *, int *);
typedef QString * (*CuteQuickSharedImageLoaderCall1)(const void *, const QString *, QSharedImageLoader::ImageParameters *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQuickSharedImageLoaderCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQuickSharedImageLoaderCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQuickSharedImageLoaderCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQuickSharedImageLoaderCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQuickSharedImageLoaderCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQuickSharedImageLoaderCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQuickSharedImageLoaderCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQuickSharedImageLoader : public QuickSharedImageLoader {
public:
  using QuickSharedImageLoader::QuickSharedImageLoader;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QSharedImageLoader8loadFileERK7QStringP5QListI8QVariantE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QSharedImageLoader3keyERK7QStringP5QListI8QVariantE")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QImage QuickSharedImageLoader::loadFile(const QString &path,
  //      ImageParameters *params)
  QImage loadFile(
      const QString &path,
      QSharedImageLoader::ImageParameters *params) override {
    if (taken[0]) {
      int handled = 0;
      CuteQuickSharedImageLoaderCall0 call = reinterpret_cast<CuteQuickSharedImageLoaderCall0>(taken[0]);
      const QImage * given = call(this, &path, params, &handled);
      if (handled && given) return *given;
    }
    return QuickSharedImageLoader::loadFile(path, params);
  }

  //  QString QuickSharedImageLoader::key(const QString &path,
  //      ImageParameters *params)
  QString key(
      const QString &path,
      QSharedImageLoader::ImageParameters *params) override {
    if (taken[1]) {
      int handled = 0;
      CuteQuickSharedImageLoaderCall1 call = reinterpret_cast<CuteQuickSharedImageLoaderCall1>(taken[1]);
      QString * given = call(this, &path, params, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QuickSharedImageLoader::key(path, params);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQuickSharedImageLoaderCall2 call = reinterpret_cast<CuteQuickSharedImageLoaderCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQuickSharedImageLoaderCall3 call = reinterpret_cast<CuteQuickSharedImageLoaderCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQuickSharedImageLoaderCall4 call = reinterpret_cast<CuteQuickSharedImageLoaderCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQuickSharedImageLoaderCall5 call = reinterpret_cast<CuteQuickSharedImageLoaderCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQuickSharedImageLoaderCall6 call = reinterpret_cast<CuteQuickSharedImageLoaderCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQuickSharedImageLoaderCall7 call = reinterpret_cast<CuteQuickSharedImageLoaderCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQuickSharedImageLoaderCall8 call = reinterpret_cast<CuteQuickSharedImageLoaderCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QuickSharedImageLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QuickSharedImageLoader10metaObjectEv(
    const QuickSharedImageLoader *self) {
  return self->metaObject();
}

//  void *QuickSharedImageLoader::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QuickSharedImageLoader11qt_metacastEPKc(
    QuickSharedImageLoader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QuickSharedImageLoader::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QuickSharedImageLoader11qt_metacallEN11QMetaObject4CallEiPPv(
    QuickSharedImageLoader *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QImage QuickSharedImageLoader::loadFile(const QString &path,
//      ImageParameters *params)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN22QuickSharedImageLoader8loadFileERK7QStringP5QListI8QVariantE(
    QuickSharedImageLoader *self,
    const QString *path,
    QSharedImageLoader::ImageParameters *params) {
  return new QImage(self->loadFile(*path, params));
}

//  QString QuickSharedImageLoader::key(const QString &path, ImageParameters
//      *params)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QuickSharedImageLoader3keyERK7QStringP5QListI8QVariantE(
    QuickSharedImageLoader *self,
    const QString *path,
    QSharedImageLoader::ImageParameters *params) {
  return new QString(self->key(*path, params));
}

//  a Python function taken by a CuteQuickSharedImageLoader, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QuickSharedImageLoader(
    QuickSharedImageLoader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQuickSharedImageLoader *>(self)->take(key, call);
}

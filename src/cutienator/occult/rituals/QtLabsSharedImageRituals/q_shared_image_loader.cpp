//  Written by dev_tooling.RitualGenerator from the records of QtLabsSharedIm
//  age/6.12.0/QtLabsSharedImage/private/qsharedimageloader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLabsSharedImage/6.12.0/QtLabsSharedImage/private/qtlabssharedimageglobal_p.h>
#include <QtLabsSharedImage/QtLabsSharedImage>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsSharedImage/6.12.0/QtLabsSharedImage/private/qsharedimageloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QSharedImageLoader may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSharedImageLoader : QSharedImageLoader {
  using QSharedImageLoader::loadFile;
  using QSharedImageLoader::key;
};

//  A QSharedImageLoader that Python can take functions over in. Every QSharedImageLoader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QImage * (*CuteQSharedImageLoaderCall0)(const void *, const QString *, QSharedImageLoader::ImageParameters *, int *);
typedef QString * (*CuteQSharedImageLoaderCall1)(const void *, const QString *, QSharedImageLoader::ImageParameters *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSharedImageLoaderCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSharedImageLoaderCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSharedImageLoaderCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSharedImageLoaderCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSharedImageLoaderCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSharedImageLoaderCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSharedImageLoaderCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSharedImageLoader : public QSharedImageLoader {
public:
  using QSharedImageLoader::QSharedImageLoader;
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

  //  QImage QSharedImageLoader::loadFile(const QString &path,
  //      ImageParameters *params)
  QImage loadFile(
      const QString &path,
      QSharedImageLoader::ImageParameters *params) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSharedImageLoaderCall0 call = reinterpret_cast<CuteQSharedImageLoaderCall0>(taken[0]);
      const QImage * given = call(this, &path, params, &handled);
      if (handled && given) return *given;
    }
    return QSharedImageLoader::loadFile(path, params);
  }

  //  QString QSharedImageLoader::key(const QString &path, ImageParameters
  //      *params)
  QString key(
      const QString &path,
      QSharedImageLoader::ImageParameters *params) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSharedImageLoaderCall1 call = reinterpret_cast<CuteQSharedImageLoaderCall1>(taken[1]);
      QString * given = call(this, &path, params, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QSharedImageLoader::key(path, params);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSharedImageLoaderCall2 call = reinterpret_cast<CuteQSharedImageLoaderCall2>(taken[2]);
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
      CuteQSharedImageLoaderCall3 call = reinterpret_cast<CuteQSharedImageLoaderCall3>(taken[3]);
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
      CuteQSharedImageLoaderCall4 call = reinterpret_cast<CuteQSharedImageLoaderCall4>(taken[4]);
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
      CuteQSharedImageLoaderCall5 call = reinterpret_cast<CuteQSharedImageLoaderCall5>(taken[5]);
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
      CuteQSharedImageLoaderCall6 call = reinterpret_cast<CuteQSharedImageLoaderCall6>(taken[6]);
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
      CuteQSharedImageLoaderCall7 call = reinterpret_cast<CuteQSharedImageLoaderCall7>(taken[7]);
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
      CuteQSharedImageLoaderCall8 call = reinterpret_cast<CuteQSharedImageLoaderCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSharedImageLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QSharedImageLoader10metaObjectEv(
    const QSharedImageLoader *self) {
  return self->metaObject();
}

//  void *QSharedImageLoader::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QSharedImageLoader11qt_metacastEPKc(
    QSharedImageLoader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSharedImageLoader::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QSharedImageLoader11qt_metacallEN11QMetaObject4CallEiPPv(
    QSharedImageLoader *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSharedImageLoader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QSharedImageLoader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSharedImageLoader::tr(s, c, n));
}

//  QSharedImageLoaderPrivate *QSharedImageLoader::d_func()
extern "C" Q_DECL_EXPORT
QSharedImageLoaderPrivate *ritual_ZN18QSharedImageLoader6d_funcEv(
    QSharedImageLoader *self) {
  return self->d_func();
}

//  const QSharedImageLoaderPrivate *QSharedImageLoader::d_func() const
extern "C" Q_DECL_EXPORT
const QSharedImageLoaderPrivate *ritual_ZNK18QSharedImageLoader6d_funcEv(
    const QSharedImageLoader *self) {
  return self->d_func();
}

//  void QSharedImageLoader::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSharedImageLoader22qt_qmlMarker_anonymousEv(
    QSharedImageLoader *self) {
  self->qt_qmlMarker_anonymous();
}

//  QSharedImageLoader::QSharedImageLoader(QObject *parent)
extern "C" Q_DECL_EXPORT
QSharedImageLoader *ritual_ZN18QSharedImageLoaderC1EP7QObject(
    QObject *parent) {
  return new CuteQSharedImageLoader(parent);
}

//  QSharedImageLoader::~QSharedImageLoader()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSharedImageLoaderD1Ev(QSharedImageLoader *self) {
  delete self;
}

//  QImage QSharedImageLoader::load(const QString &path, ImageParameters
//      *params)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN18QSharedImageLoader4loadERK7QStringP5QListI8QVariantE(
    QSharedImageLoader *self,
    const QString *path,
    QSharedImageLoader::ImageParameters *params) {
  return new QImage(self->load(*path, params));
}

//  QImage QSharedImageLoader::loadFile(const QString &path, ImageParameters
//      *params)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN18QSharedImageLoader8loadFileERK7QStringP5QListI8QVariantE(
    QSharedImageLoader *self,
    const QString *path,
    QSharedImageLoader::ImageParameters *params) {
  return new QImage(self->loadFile(*path, params));
}

//  QString QSharedImageLoader::key(const QString &path, ImageParameters
//      *params)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QSharedImageLoader3keyERK7QStringP5QListI8QVariantE(
    QSharedImageLoader *self,
    const QString *path,
    QSharedImageLoader::ImageParameters *params) {
  return new QString(self->key(*path, params));
}

//  a Python function taken by a CuteQSharedImageLoader, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSharedImageLoader(
    QSharedImageLoader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSharedImageLoader *>(self)->take(key, call);
}

//  QImage QSharedImageLoader::loadFile(const QString &path, ImageParameters
//      *params)
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN18QSharedImageLoader8loadFileERK7QStringP5QListI8QVariantE(
    QSharedImageLoader *self,
    const QString *path,
    QSharedImageLoader::ImageParameters *params) {
  return new QImage(
      static_cast<OwnQSharedImageLoader *>(self)->OwnQSharedImageLoader::loadFile(
          *path,
          params));
}

//  QString QSharedImageLoader::key(const QString &path, ImageParameters
//      *params)
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN18QSharedImageLoader3keyERK7QStringP5QListI8QVariantE(
    QSharedImageLoader *self,
    const QString *path,
    QSharedImageLoader::ImageParameters *params) {
  return new QString(
      static_cast<OwnQSharedImageLoader *>(self)->OwnQSharedImageLoader::key(
          *path,
          params));
}

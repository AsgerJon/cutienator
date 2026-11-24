//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhiatlastexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSGRhiAtlasTexture::Atlas that Python can take functions over in. Every QSGRhiAtlasTexture::Atlas
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSGRhiAtlasTexture_AtlasCall0)(const void *, int *);
typedef void (*CuteQSGRhiAtlasTexture_AtlasCall1)(const void *, QSGRhiAtlasTexture::TextureBase *, QRhiResourceUpdateBatch *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_AtlasCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGRhiAtlasTexture_AtlasCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGRhiAtlasTexture_AtlasCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGRhiAtlasTexture_Atlas : public QSGRhiAtlasTexture::Atlas {
public:
  using QSGRhiAtlasTexture::Atlas::Atlas;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QSGRhiAtlasTexture9AtlasBase15generateTextureEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QSGRhiAtlasTexture9AtlasBase20enqueueTextureUploadEPNS_11TextureBaseEP23QRhiResourceUpdateBatch")) {
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

  //  bool QSGRhiAtlasTexture::Atlas::generateTexture()
  bool generateTexture() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_AtlasCall0 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRhiAtlasTexture::Atlas::generateTexture();
  }

  //  void QSGRhiAtlasTexture::Atlas::enqueueTextureUpload(TextureBase *t,
  //      QRhiResourceUpdateBatch *resourceUpdates)
  void enqueueTextureUpload(
      QSGRhiAtlasTexture::TextureBase *t,
      QRhiResourceUpdateBatch *resourceUpdates) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_AtlasCall1 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall1>(taken[1]);
      call(this, t, resourceUpdates, &handled);
      if (handled) return;
    }
    QSGRhiAtlasTexture::Atlas::enqueueTextureUpload(t, resourceUpdates);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRhiAtlasTexture_AtlasCall2 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall2>(taken[2]);
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
      CuteQSGRhiAtlasTexture_AtlasCall3 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall3>(taken[3]);
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
      CuteQSGRhiAtlasTexture_AtlasCall4 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall4>(taken[4]);
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
      CuteQSGRhiAtlasTexture_AtlasCall5 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall5>(taken[5]);
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
      CuteQSGRhiAtlasTexture_AtlasCall6 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall6>(taken[6]);
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
      CuteQSGRhiAtlasTexture_AtlasCall7 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall7>(taken[7]);
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
      CuteQSGRhiAtlasTexture_AtlasCall8 call = reinterpret_cast<CuteQSGRhiAtlasTexture_AtlasCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QRhiTexture::Format QSGRhiAtlasTexture::Atlas::format() const
extern "C" Q_DECL_EXPORT
QRhiTexture::Format ritual_ZNK18QSGRhiAtlasTexture5Atlas6formatEv(
    const QSGRhiAtlasTexture::Atlas *self) {
  return self->format();
}

//  a Python function taken by a CuteQSGRhiAtlasTexture_Atlas, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRhiAtlasTexture_Atlas(
    QSGRhiAtlasTexture::Atlas *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRhiAtlasTexture_Atlas *>(self)->take(key, call);
}

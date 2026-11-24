//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dshaderutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgrenderbasetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DShaderUtilsRenderPassTexture that Python can take functions over in. Every QQuick3DShaderUtilsRenderPassTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuick3DShaderUtilsRenderPassTextureCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassTextureCall1)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassTextureCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassTextureCall3)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassTextureCall4)(const void *, int *);
typedef void (*CuteQQuick3DShaderUtilsRenderPassTextureCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsRenderPassTextureCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DShaderUtilsRenderPassTextureCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassTextureCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassTextureCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassTextureCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassTextureCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DShaderUtilsRenderPassTextureCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DShaderUtilsRenderPassTexture : public QQuick3DShaderUtilsRenderPassTexture {
public:
  using QQuick3DShaderUtilsRenderPassTexture::QQuick3DShaderUtilsRenderPassTexture;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSSGRenderGraphObject
  //      *QQuick3DObject::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassTextureCall0 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassTextureCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DObject::updateSpatialNode(node);
  }

  //  void QQuick3DObject::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassTextureCall1 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassTextureCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassTextureCall2 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassTextureCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassTextureCall3 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassTextureCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassTextureCall4 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassTextureCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassTextureCall5 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassTextureCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassTextureCall6 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassTextureCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassTextureCall7 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassTextureCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassTextureCall8 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassTextureCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassTextureCall9 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassTextureCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassTextureCall10 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassTextureCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassTextureCall11 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassTextureCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DShaderUtilsRenderPassTextureCall12 call = reinterpret_cast<CuteQQuick3DShaderUtilsRenderPassTextureCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DShaderUtilsRenderPassTexture::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK36QQuick3DShaderUtilsRenderPassTexture10metaObjectEv(
    const QQuick3DShaderUtilsRenderPassTexture *self) {
  return self->metaObject();
}

//  QString QQuick3DShaderUtilsRenderPassTexture::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN36QQuick3DShaderUtilsRenderPassTexture2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DShaderUtilsRenderPassTexture::tr(s, c, n));
}

//  QQuick3DShaderUtilsRenderPassTexture::QQuick3DShaderUtilsRenderPassTextur
//      e()
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsRenderPassTexture *ritual_ZN36QQuick3DShaderUtilsRenderPassTextureC1Ev() {
  return new CuteQQuick3DShaderUtilsRenderPassTexture();
}

//  QQuick3DShaderUtilsRenderPassTexture::~QQuick3DShaderUtilsRenderPassTextu
//      re()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QQuick3DShaderUtilsRenderPassTextureD1Ev(
    QQuick3DShaderUtilsRenderPassTexture *self) {
  delete self;
}

//  TextureFormat QQuick3DShaderUtilsRenderPassTexture::format() const
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsRenderPassTexture::TextureFormat ritual_ZNK36QQuick3DShaderUtilsRenderPassTexture6formatEv(
    const QQuick3DShaderUtilsRenderPassTexture *self) {
  return self->format();
}

//  void QQuick3DShaderUtilsRenderPassTexture::setFormat(TextureFormat
//      newFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QQuick3DShaderUtilsRenderPassTexture9setFormatENS_13TextureFormatE(
    QQuick3DShaderUtilsRenderPassTexture *self,
    QQuick3DShaderUtilsRenderPassTexture::TextureFormat newFormat) {
  self->setFormat(newFormat);
}

//  QSSGRenderTextureFormat QQuick3DShaderUtilsRenderPassTexture::asRenderTex
//      tureFormat(QQuick3DShaderUtilsRenderPassTexture::TextureFormat fmt)
extern "C" Q_DECL_EXPORT
QSSGRenderTextureFormat *ritual_ZN36QQuick3DShaderUtilsRenderPassTexture21asRenderTextureFormatENS_13TextureFormatE(
    QQuick3DShaderUtilsRenderPassTexture::TextureFormat fmt) {
  return new QSSGRenderTextureFormat(
      QQuick3DShaderUtilsRenderPassTexture::asRenderTextureFormat(
          fmt));
}

//  QQuick3DShaderUtilsRenderPassTexture::TextureFormat QQuick3DShaderUtilsRe
//      nderPassTexture::fromRenderTextureFormat(QSSGRenderTextureFormat fmt)
extern "C" Q_DECL_EXPORT
QQuick3DShaderUtilsRenderPassTexture::TextureFormat ritual_ZN36QQuick3DShaderUtilsRenderPassTexture23fromRenderTextureFormatE23QSSGRenderTextureFormat(
    const QSSGRenderTextureFormat *fmt) {
  return QQuick3DShaderUtilsRenderPassTexture::fromRenderTextureFormat(*fmt);
}

//  a Python function taken by a CuteQQuick3DShaderUtilsRenderPassTexture,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DShaderUtilsRenderPassTexture(
    QQuick3DShaderUtilsRenderPassTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DShaderUtilsRenderPassTexture *>(self)->take(key, call);
}

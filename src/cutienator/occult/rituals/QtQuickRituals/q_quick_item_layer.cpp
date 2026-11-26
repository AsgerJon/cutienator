//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickItemLayer that Python can take functions over in. Every QQuickItemLayer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickItemLayerCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickItemLayerCall1)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickItemLayerCall2)(const void *, QQuickItem *, QQuickItem *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickItemLayerCall3)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteQQuickItemLayerCall4)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickItemLayerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickItemLayerCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemLayerCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemLayerCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemLayerCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemLayerCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickItemLayerCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickItemLayer : public QQuickItemLayer {
public:
  using QQuickItemLayer::QQuickItemLayer;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN15QQuickItemLayer19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN15QQuickItemLayer18itemOpacityChangedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN15QQuickItemLayer17itemParentChangedEP10QQuickItemS1_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN15QQuickItemLayer23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN15QQuickItemLayer21itemVisibilityChangedEP10QQuickItem")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickItemLayer::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickItemLayerCall0 call = reinterpret_cast<CuteQQuickItemLayerCall0>(taken[0]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickItemLayer::itemGeometryChanged(a0, a1, a2);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickItemLayer::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickItemLayerCall1 call = reinterpret_cast<CuteQQuickItemLayerCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemLayer::itemOpacityChanged(a0);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickItemLayer::itemParentChanged(QQuickItem *a0, QQuickItem
  //      *a1)
  void itemParentChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickItemLayerCall2 call = reinterpret_cast<CuteQQuickItemLayerCall2>(taken[2]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemLayer::itemParentChanged(a0, a1);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickItemLayer::itemSiblingOrderChanged(QQuickItem *a0)
  void itemSiblingOrderChanged(QQuickItem *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickItemLayerCall3 call = reinterpret_cast<CuteQQuickItemLayerCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemLayer::itemSiblingOrderChanged(a0);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickItemLayer::itemVisibilityChanged(QQuickItem *a0)
  void itemVisibilityChanged(QQuickItem *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickItemLayerCall4 call = reinterpret_cast<CuteQQuickItemLayerCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemLayer::itemVisibilityChanged(a0);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickItemLayerCall5 call = reinterpret_cast<CuteQQuickItemLayerCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickItemLayerCall6 call = reinterpret_cast<CuteQQuickItemLayerCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickItemLayerCall7 call = reinterpret_cast<CuteQQuickItemLayerCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickItemLayerCall8 call = reinterpret_cast<CuteQQuickItemLayerCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickItemLayerCall9 call = reinterpret_cast<CuteQQuickItemLayerCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickItemLayerCall10 call = reinterpret_cast<CuteQQuickItemLayerCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickItemLayerCall11 call = reinterpret_cast<CuteQQuickItemLayerCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickItemLayer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickItemLayer10metaObjectEv(
    const QQuickItemLayer *self) {
  return self->metaObject();
}

//  void *QQuickItemLayer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QQuickItemLayer11qt_metacastEPKc(
    QQuickItemLayer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickItemLayer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QQuickItemLayer11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickItemLayer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickItemLayer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickItemLayer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickItemLayer::tr(s, c, n));
}

//  void QQuickItemLayer::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer22qt_qmlMarker_anonymousEv(
    QQuickItemLayer *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickItemLayer::QQuickItemLayer(QQuickItem *item)
extern "C" Q_DECL_EXPORT
QQuickItemLayer *ritual_ZN15QQuickItemLayerC1EP10QQuickItem(
    QQuickItem *item) {
  return new CuteQQuickItemLayer(item);
}

//  QQuickItemLayer::~QQuickItemLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayerD1Ev(QQuickItemLayer *self) {
  delete self;
}

//  void QQuickItemLayer::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer10classBeginEv(QQuickItemLayer *self) {
  self->classBegin();
}

//  void QQuickItemLayer::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer17componentCompleteEv(QQuickItemLayer *self) {
  self->componentComplete();
}

//  bool QQuickItemLayer::enabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickItemLayer7enabledEv(const QQuickItemLayer *self) {
  return self->enabled();
}

//  void QQuickItemLayer::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer10setEnabledEb(
    QQuickItemLayer *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  bool QQuickItemLayer::mipmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickItemLayer6mipmapEv(const QQuickItemLayer *self) {
  return self->mipmap();
}

//  void QQuickItemLayer::setMipmap(bool mipmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer9setMipmapEb(
    QQuickItemLayer *self,
    bool mipmap) {
  self->setMipmap(mipmap);
}

//  bool QQuickItemLayer::smooth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickItemLayer6smoothEv(const QQuickItemLayer *self) {
  return self->smooth();
}

//  void QQuickItemLayer::setSmooth(bool s)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer9setSmoothEb(QQuickItemLayer *self, bool s) {
  self->setSmooth(s);
}

//  bool QQuickItemLayer::live() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickItemLayer4liveEv(const QQuickItemLayer *self) {
  return self->live();
}

//  void QQuickItemLayer::setLive(bool live)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer7setLiveEb(QQuickItemLayer *self, bool live) {
  self->setLive(live);
}

//  QSize QQuickItemLayer::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK15QQuickItemLayer4sizeEv(const QQuickItemLayer *self) {
  return new QSize(self->size());
}

//  void QQuickItemLayer::setSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer7setSizeERK5QSize(
    QQuickItemLayer *self,
    const QSize *size) {
  self->setSize(*size);
}

//  QQuickShaderEffectSource::Format QQuickItemLayer::format() const
extern "C" Q_DECL_EXPORT
QQuickShaderEffectSource::Format ritual_ZNK15QQuickItemLayer6formatEv(
    const QQuickItemLayer *self) {
  return self->format();
}

//  void QQuickItemLayer::setFormat(QQuickShaderEffectSource::Format f)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer9setFormatEN24QQuickShaderEffectSource6FormatE(
    QQuickItemLayer *self,
    QQuickShaderEffectSource::Format f) {
  self->setFormat(f);
}

//  QRectF QQuickItemLayer::sourceRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QQuickItemLayer10sourceRectEv(
    const QQuickItemLayer *self) {
  return new QRectF(self->sourceRect());
}

//  void QQuickItemLayer::setSourceRect(const QRectF &sourceRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer13setSourceRectERK6QRectF(
    QQuickItemLayer *self,
    const QRectF *sourceRect) {
  self->setSourceRect(*sourceRect);
}

//  QQuickShaderEffectSource::WrapMode QQuickItemLayer::wrapMode() const
extern "C" Q_DECL_EXPORT
QQuickShaderEffectSource::WrapMode ritual_ZNK15QQuickItemLayer8wrapModeEv(
    const QQuickItemLayer *self) {
  return self->wrapMode();
}

//  void QQuickItemLayer::setWrapMode(QQuickShaderEffectSource::WrapMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer11setWrapModeEN24QQuickShaderEffectSource8WrapModeE(
    QQuickItemLayer *self,
    QQuickShaderEffectSource::WrapMode mode) {
  self->setWrapMode(mode);
}

//  QByteArray QQuickItemLayer::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QQuickItemLayer4nameEv(const QQuickItemLayer *self) {
  return new QByteArray(self->name());
}

//  void QQuickItemLayer::setName(const QByteArray &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer7setNameERK10QByteArray(
    QQuickItemLayer *self,
    const QByteArray *name) {
  self->setName(*name);
}

//  QQmlComponent *QQuickItemLayer::effect() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK15QQuickItemLayer6effectEv(
    const QQuickItemLayer *self) {
  return self->effect();
}

//  void QQuickItemLayer::setEffect(QQmlComponent *effect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer9setEffectEP13QQmlComponent(
    QQuickItemLayer *self,
    QQmlComponent *effect) {
  self->setEffect(effect);
}

//  QQuickShaderEffectSource::TextureMirroring
//      QQuickItemLayer::textureMirroring() const
extern "C" Q_DECL_EXPORT
QQuickShaderEffectSource::TextureMirroring ritual_ZNK15QQuickItemLayer16textureMirroringEv(
    const QQuickItemLayer *self) {
  return self->textureMirroring();
}

//  void QQuickItemLayer::setTextureMirroring(QQuickShaderEffectSource::Textu
//      reMirroring mirroring)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer19setTextureMirroringEN24QQuickShaderEffectSource16TextureMirroringE(
    QQuickItemLayer *self,
    QQuickShaderEffectSource::TextureMirroring mirroring) {
  self->setTextureMirroring(mirroring);
}

//  int QQuickItemLayer::samples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickItemLayer7samplesEv(const QQuickItemLayer *self) {
  return self->samples();
}

//  void QQuickItemLayer::setSamples(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer10setSamplesEi(
    QQuickItemLayer *self,
    int count) {
  self->setSamples(count);
}

//  QQuickShaderEffectSource *QQuickItemLayer::effectSource() const
extern "C" Q_DECL_EXPORT
QQuickShaderEffectSource *ritual_ZNK15QQuickItemLayer12effectSourceEv(
    const QQuickItemLayer *self) {
  return self->effectSource();
}

//  void QQuickItemLayer::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickItemLayer *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->itemGeometryChanged(a0, *a1, *a2);
}

//  void QQuickItemLayer::itemOpacityChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer18itemOpacityChangedEP10QQuickItem(
    QQuickItemLayer *self,
    QQuickItem *a0) {
  self->itemOpacityChanged(a0);
}

//  void QQuickItemLayer::itemParentChanged(QQuickItem *a0, QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer17itemParentChangedEP10QQuickItemS1_(
    QQuickItemLayer *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->itemParentChanged(a0, a1);
}

//  void QQuickItemLayer::itemSiblingOrderChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer23itemSiblingOrderChangedEP10QQuickItem(
    QQuickItemLayer *self,
    QQuickItem *a0) {
  self->itemSiblingOrderChanged(a0);
}

//  void QQuickItemLayer::itemVisibilityChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer21itemVisibilityChangedEP10QQuickItem(
    QQuickItemLayer *self,
    QQuickItem *a0) {
  self->itemVisibilityChanged(a0);
}

//  void QQuickItemLayer::updateMatrix()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer12updateMatrixEv(QQuickItemLayer *self) {
  self->updateMatrix();
}

//  void QQuickItemLayer::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer14updateGeometryEv(QQuickItemLayer *self) {
  self->updateGeometry();
}

//  void QQuickItemLayer::updateOpacity()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer13updateOpacityEv(QQuickItemLayer *self) {
  self->updateOpacity();
}

//  void QQuickItemLayer::updateZ()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer7updateZEv(QQuickItemLayer *self) {
  self->updateZ();
}

//  void QQuickItemLayer::enabledChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer14enabledChangedEb(
    QQuickItemLayer *self,
    bool enabled) {
  self->enabledChanged(enabled);
}

//  void QQuickItemLayer::sizeChanged(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer11sizeChangedERK5QSize(
    QQuickItemLayer *self,
    const QSize *size) {
  self->sizeChanged(*size);
}

//  void QQuickItemLayer::mipmapChanged(bool mipmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer13mipmapChangedEb(
    QQuickItemLayer *self,
    bool mipmap) {
  self->mipmapChanged(mipmap);
}

//  void QQuickItemLayer::wrapModeChanged(QQuickShaderEffectSource::WrapMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer15wrapModeChangedEN24QQuickShaderEffectSource8WrapModeE(
    QQuickItemLayer *self,
    QQuickShaderEffectSource::WrapMode mode) {
  self->wrapModeChanged(mode);
}

//  void QQuickItemLayer::nameChanged(const QByteArray &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer11nameChangedERK10QByteArray(
    QQuickItemLayer *self,
    const QByteArray *name) {
  self->nameChanged(*name);
}

//  void QQuickItemLayer::effectChanged(QQmlComponent *component)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer13effectChangedEP13QQmlComponent(
    QQuickItemLayer *self,
    QQmlComponent *component) {
  self->effectChanged(component);
}

//  void QQuickItemLayer::smoothChanged(bool smooth)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer13smoothChangedEb(
    QQuickItemLayer *self,
    bool smooth) {
  self->smoothChanged(smooth);
}

//  void QQuickItemLayer::liveChanged(bool live)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer11liveChangedEb(
    QQuickItemLayer *self,
    bool live) {
  self->liveChanged(live);
}

//  void QQuickItemLayer::formatChanged(QQuickShaderEffectSource::Format
//      format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer13formatChangedEN24QQuickShaderEffectSource6FormatE(
    QQuickItemLayer *self,
    QQuickShaderEffectSource::Format format) {
  self->formatChanged(format);
}

//  void QQuickItemLayer::sourceRectChanged(const QRectF &sourceRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer17sourceRectChangedERK6QRectF(
    QQuickItemLayer *self,
    const QRectF *sourceRect) {
  self->sourceRectChanged(*sourceRect);
}

//  void QQuickItemLayer::textureMirroringChanged(QQuickShaderEffectSource::T
//      extureMirroring mirroring)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer23textureMirroringChangedEN24QQuickShaderEffectSource16TextureMirroringE(
    QQuickItemLayer *self,
    QQuickShaderEffectSource::TextureMirroring mirroring) {
  self->textureMirroringChanged(mirroring);
}

//  void QQuickItemLayer::samplesChanged(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer14samplesChangedEi(
    QQuickItemLayer *self,
    int count) {
  self->samplesChanged(count);
}

//  void QQuickItemLayer::activate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer8activateEv(QQuickItemLayer *self) {
  self->activate();
}

//  void QQuickItemLayer::deactivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer10deactivateEv(QQuickItemLayer *self) {
  self->deactivate();
}

//  void QQuickItemLayer::activateEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer14activateEffectEv(QQuickItemLayer *self) {
  self->activateEffect();
}

//  void QQuickItemLayer::deactivateEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickItemLayer16deactivateEffectEv(QQuickItemLayer *self) {
  self->deactivateEffect();
}

//  a Python function taken by a CuteQQuickItemLayer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickItemLayer(
    QQuickItemLayer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickItemLayer *>(self)->take(key, call);
}

//  void QQuickItemLayer::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickItemLayer19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickItemLayer *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->QQuickItemLayer::itemGeometryChanged(a0, *a1, *a2);
}

//  void QQuickItemLayer::itemOpacityChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickItemLayer18itemOpacityChangedEP10QQuickItem(
    QQuickItemLayer *self,
    QQuickItem *a0) {
  self->QQuickItemLayer::itemOpacityChanged(a0);
}

//  void QQuickItemLayer::itemParentChanged(QQuickItem *a0, QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickItemLayer17itemParentChangedEP10QQuickItemS1_(
    QQuickItemLayer *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->QQuickItemLayer::itemParentChanged(a0, a1);
}

//  void QQuickItemLayer::itemSiblingOrderChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickItemLayer23itemSiblingOrderChangedEP10QQuickItem(
    QQuickItemLayer *self,
    QQuickItem *a0) {
  self->QQuickItemLayer::itemSiblingOrderChanged(a0);
}

//  void QQuickItemLayer::itemVisibilityChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickItemLayer21itemVisibilityChangedEP10QQuickItem(
    QQuickItemLayer *self,
    QQuickItem *a0) {
  self->QQuickItemLayer::itemVisibilityChanged(a0);
}

#endif  // QT_CONFIG(quick_shadereffect)

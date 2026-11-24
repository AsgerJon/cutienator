//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DHelpe
//  rs/6.12.0/QtQuick3DHelpers/private/proceduralskytexturedata_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/qtquick3dhelpersglobal_p.h>
#include <QtQuick3DHelpers/QtQuick3DHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/proceduralskytexturedata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A ProceduralSkyTextureData that Python can take functions over in. Every ProceduralSkyTextureData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteProceduralSkyTextureDataCall0)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteProceduralSkyTextureDataCall1)(const void *, int *);
typedef void (*CuteProceduralSkyTextureDataCall2)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteProceduralSkyTextureDataCall3)(const void *, int *);
typedef void (*CuteProceduralSkyTextureDataCall4)(const void *, int *);
typedef void (*CuteProceduralSkyTextureDataCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteProceduralSkyTextureDataCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteProceduralSkyTextureDataCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteProceduralSkyTextureDataCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteProceduralSkyTextureDataCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteProceduralSkyTextureDataCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteProceduralSkyTextureDataCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteProceduralSkyTextureDataCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteProceduralSkyTextureData : public ProceduralSkyTextureData {
public:
  using ProceduralSkyTextureData::ProceduralSkyTextureData;
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
  //      *QQuick3DTextureData::updateSpatialNode(QSSGRenderGraphObject
  //      *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteProceduralSkyTextureDataCall0 call = reinterpret_cast<CuteProceduralSkyTextureDataCall0>(taken[0]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DTextureData::updateSpatialNode(node);
  }

  //  void QQuick3DTextureData::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteProceduralSkyTextureDataCall1 call = reinterpret_cast<CuteProceduralSkyTextureDataCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DTextureData::markAllDirty();
  }

  //  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[2]) {
      int handled = 0;
      CuteProceduralSkyTextureDataCall2 call = reinterpret_cast<CuteProceduralSkyTextureDataCall2>(taken[2]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DObject::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteProceduralSkyTextureDataCall3 call = reinterpret_cast<CuteProceduralSkyTextureDataCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::componentComplete()
  void componentComplete() override {
    if (taken[4]) {
      int handled = 0;
      CuteProceduralSkyTextureDataCall4 call = reinterpret_cast<CuteProceduralSkyTextureDataCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::componentComplete();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[5]) {
      int handled = 0;
      CuteProceduralSkyTextureDataCall5 call = reinterpret_cast<CuteProceduralSkyTextureDataCall5>(taken[5]);
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
      CuteProceduralSkyTextureDataCall6 call = reinterpret_cast<CuteProceduralSkyTextureDataCall6>(taken[6]);
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
      CuteProceduralSkyTextureDataCall7 call = reinterpret_cast<CuteProceduralSkyTextureDataCall7>(taken[7]);
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
      CuteProceduralSkyTextureDataCall8 call = reinterpret_cast<CuteProceduralSkyTextureDataCall8>(taken[8]);
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
      CuteProceduralSkyTextureDataCall9 call = reinterpret_cast<CuteProceduralSkyTextureDataCall9>(taken[9]);
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
      CuteProceduralSkyTextureDataCall10 call = reinterpret_cast<CuteProceduralSkyTextureDataCall10>(taken[10]);
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
      CuteProceduralSkyTextureDataCall11 call = reinterpret_cast<CuteProceduralSkyTextureDataCall11>(taken[11]);
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
      CuteProceduralSkyTextureDataCall12 call = reinterpret_cast<CuteProceduralSkyTextureDataCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *ProceduralSkyTextureData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24ProceduralSkyTextureData10metaObjectEv(
    const ProceduralSkyTextureData *self) {
  return self->metaObject();
}

//  QString ProceduralSkyTextureData::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24ProceduralSkyTextureData2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ProceduralSkyTextureData::tr(s, c, n));
}

//  ProceduralSkyTextureData::ProceduralSkyTextureData()
extern "C" Q_DECL_EXPORT
ProceduralSkyTextureData *ritual_ZN24ProceduralSkyTextureDataC1Ev() {
  return new CuteProceduralSkyTextureData();
}

//  ProceduralSkyTextureData::~ProceduralSkyTextureData()
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureDataD1Ev(
    ProceduralSkyTextureData *self) {
  delete self;
}

//  QColor ProceduralSkyTextureData::skyTopColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK24ProceduralSkyTextureData11skyTopColorEv(
    const ProceduralSkyTextureData *self) {
  return new QColor(self->skyTopColor());
}

//  QColor ProceduralSkyTextureData::skyHorizonColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK24ProceduralSkyTextureData15skyHorizonColorEv(
    const ProceduralSkyTextureData *self) {
  return new QColor(self->skyHorizonColor());
}

//  float ProceduralSkyTextureData::skyCurve() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24ProceduralSkyTextureData8skyCurveEv(
    const ProceduralSkyTextureData *self) {
  return self->skyCurve();
}

//  float ProceduralSkyTextureData::skyEnergy() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24ProceduralSkyTextureData9skyEnergyEv(
    const ProceduralSkyTextureData *self) {
  return self->skyEnergy();
}

//  QColor ProceduralSkyTextureData::groundBottomColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK24ProceduralSkyTextureData17groundBottomColorEv(
    const ProceduralSkyTextureData *self) {
  return new QColor(self->groundBottomColor());
}

//  QColor ProceduralSkyTextureData::groundHorizonColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK24ProceduralSkyTextureData18groundHorizonColorEv(
    const ProceduralSkyTextureData *self) {
  return new QColor(self->groundHorizonColor());
}

//  float ProceduralSkyTextureData::groundCurve() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24ProceduralSkyTextureData11groundCurveEv(
    const ProceduralSkyTextureData *self) {
  return self->groundCurve();
}

//  float ProceduralSkyTextureData::groundEnergy() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24ProceduralSkyTextureData12groundEnergyEv(
    const ProceduralSkyTextureData *self) {
  return self->groundEnergy();
}

//  QColor ProceduralSkyTextureData::sunColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK24ProceduralSkyTextureData8sunColorEv(
    const ProceduralSkyTextureData *self) {
  return new QColor(self->sunColor());
}

//  float ProceduralSkyTextureData::sunLatitude() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24ProceduralSkyTextureData11sunLatitudeEv(
    const ProceduralSkyTextureData *self) {
  return self->sunLatitude();
}

//  float ProceduralSkyTextureData::sunLongitude() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24ProceduralSkyTextureData12sunLongitudeEv(
    const ProceduralSkyTextureData *self) {
  return self->sunLongitude();
}

//  float ProceduralSkyTextureData::sunAngleMin() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24ProceduralSkyTextureData11sunAngleMinEv(
    const ProceduralSkyTextureData *self) {
  return self->sunAngleMin();
}

//  float ProceduralSkyTextureData::sunAngleMax() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24ProceduralSkyTextureData11sunAngleMaxEv(
    const ProceduralSkyTextureData *self) {
  return self->sunAngleMax();
}

//  float ProceduralSkyTextureData::sunCurve() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24ProceduralSkyTextureData8sunCurveEv(
    const ProceduralSkyTextureData *self) {
  return self->sunCurve();
}

//  float ProceduralSkyTextureData::sunEnergy() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24ProceduralSkyTextureData9sunEnergyEv(
    const ProceduralSkyTextureData *self) {
  return self->sunEnergy();
}

//  SkyTextureQuality ProceduralSkyTextureData::textureQuality() const
extern "C" Q_DECL_EXPORT
ProceduralSkyTextureData::SkyTextureQuality ritual_ZNK24ProceduralSkyTextureData14textureQualityEv(
    const ProceduralSkyTextureData *self) {
  return self->textureQuality();
}

//  void ProceduralSkyTextureData::setSkyTopColor(QColor skyTopColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData14setSkyTopColorE6QColor(
    ProceduralSkyTextureData *self,
    const QColor *skyTopColor) {
  self->setSkyTopColor(*skyTopColor);
}

//  void ProceduralSkyTextureData::setSkyHorizonColor(QColor skyHorizonColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData18setSkyHorizonColorE6QColor(
    ProceduralSkyTextureData *self,
    const QColor *skyHorizonColor) {
  self->setSkyHorizonColor(*skyHorizonColor);
}

//  void ProceduralSkyTextureData::setSkyCurve(float skyCurve)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData11setSkyCurveEf(
    ProceduralSkyTextureData *self,
    float skyCurve) {
  self->setSkyCurve(skyCurve);
}

//  void ProceduralSkyTextureData::setSkyEnergy(float skyEnergy)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData12setSkyEnergyEf(
    ProceduralSkyTextureData *self,
    float skyEnergy) {
  self->setSkyEnergy(skyEnergy);
}

//  void ProceduralSkyTextureData::setGroundBottomColor(QColor
//      groundBottomColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData20setGroundBottomColorE6QColor(
    ProceduralSkyTextureData *self,
    const QColor *groundBottomColor) {
  self->setGroundBottomColor(*groundBottomColor);
}

//  void ProceduralSkyTextureData::setGroundHorizonColor(QColor
//      groundHorizonColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData21setGroundHorizonColorE6QColor(
    ProceduralSkyTextureData *self,
    const QColor *groundHorizonColor) {
  self->setGroundHorizonColor(*groundHorizonColor);
}

//  void ProceduralSkyTextureData::setGroundCurve(float groundCurve)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData14setGroundCurveEf(
    ProceduralSkyTextureData *self,
    float groundCurve) {
  self->setGroundCurve(groundCurve);
}

//  void ProceduralSkyTextureData::setGroundEnergy(float groundEnergy)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData15setGroundEnergyEf(
    ProceduralSkyTextureData *self,
    float groundEnergy) {
  self->setGroundEnergy(groundEnergy);
}

//  void ProceduralSkyTextureData::setSunColor(QColor sunColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData11setSunColorE6QColor(
    ProceduralSkyTextureData *self,
    const QColor *sunColor) {
  self->setSunColor(*sunColor);
}

//  void ProceduralSkyTextureData::setSunLatitude(float sunLatitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData14setSunLatitudeEf(
    ProceduralSkyTextureData *self,
    float sunLatitude) {
  self->setSunLatitude(sunLatitude);
}

//  void ProceduralSkyTextureData::setSunLongitude(float sunLongitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData15setSunLongitudeEf(
    ProceduralSkyTextureData *self,
    float sunLongitude) {
  self->setSunLongitude(sunLongitude);
}

//  void ProceduralSkyTextureData::setSunAngleMin(float sunAngleMin)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData14setSunAngleMinEf(
    ProceduralSkyTextureData *self,
    float sunAngleMin) {
  self->setSunAngleMin(sunAngleMin);
}

//  void ProceduralSkyTextureData::setSunAngleMax(float sunAngleMax)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData14setSunAngleMaxEf(
    ProceduralSkyTextureData *self,
    float sunAngleMax) {
  self->setSunAngleMax(sunAngleMax);
}

//  void ProceduralSkyTextureData::setSunCurve(float sunCurve)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData11setSunCurveEf(
    ProceduralSkyTextureData *self,
    float sunCurve) {
  self->setSunCurve(sunCurve);
}

//  void ProceduralSkyTextureData::setSunEnergy(float sunEnergy)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData12setSunEnergyEf(
    ProceduralSkyTextureData *self,
    float sunEnergy) {
  self->setSunEnergy(sunEnergy);
}

//  void ProceduralSkyTextureData::setTextureQuality(SkyTextureQuality
//      textureQuality)
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData17setTextureQualityENS_17SkyTextureQualityE(
    ProceduralSkyTextureData *self,
    ProceduralSkyTextureData::SkyTextureQuality textureQuality) {
  self->setTextureQuality(textureQuality);
}

//  void ProceduralSkyTextureData::generateRGBA16FTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData22generateRGBA16FTextureEv(
    ProceduralSkyTextureData *self) {
  self->generateRGBA16FTexture();
}

//  void ProceduralSkyTextureData::scheduleTextureUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24ProceduralSkyTextureData21scheduleTextureUpdateEv(
    ProceduralSkyTextureData *self) {
  self->scheduleTextureUpdate();
}

//  a Python function taken by a CuteProceduralSkyTextureData, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_ProceduralSkyTextureData(
    ProceduralSkyTextureData *self,
    const char *key,
    void *call) {
  return static_cast<CuteProceduralSkyTextureData *>(self)->take(key, call);
}

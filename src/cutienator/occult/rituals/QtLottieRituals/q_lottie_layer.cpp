//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottielayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottielayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  Only a class built on QLottieLayer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLottieLayer : QLottieLayer {
  using QLottieLayer::resolveLinkedLayer;
  using QLottieLayer::linkedLayer;
};

//  A QLottieLayer that Python can take functions over in. Every QLottieLayer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieLayerCall0)(const void *, int *);
typedef bool (*CuteQLottieLayerCall1)(const void *, int, int *);
typedef int (*CuteQLottieLayerCall2)(const void *, const QJsonObject *, int *);
typedef void (*CuteQLottieLayerCall3)(const void *, int, int *);
typedef void * (*CuteQLottieLayerCall4)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieLayerCall5)(const void *, int *);
typedef void * (*CuteQLottieLayerCall6)(const void *, int *);
typedef void * (*CuteQLottieLayerCall7)(const void *, int *);
typedef bool (*CuteQLottieLayerCall8)(const void *, int, const QVariant *, int *);
class CuteQLottieLayer : public QLottieLayer {
public:
  using QLottieLayer::QLottieLayer;
  CuteQLottieLayer(const QLottieLayer &other) : QLottieLayer(other) {}
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase6activeEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase9findChildERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase9layerSizeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QLottieLayer18resolveLinkedLayerEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieLayer11linkedLayerEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  QLottieBase *QLottieLayer::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieLayerCall0 call = reinterpret_cast<CuteQLottieLayerCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieLayer::clone();
  }

  //  bool QLottieLayer::active(int frame) const
  bool active(int frame) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieLayerCall1 call = reinterpret_cast<CuteQLottieLayerCall1>(taken[1]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieLayer::active(frame);
  }

  //  int QLottieLayer::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieLayerCall2 call = reinterpret_cast<CuteQLottieLayerCall2>(taken[2]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieLayer::parse(definition);
  }

  //  void QLottieLayer::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieLayerCall3 call = reinterpret_cast<CuteQLottieLayerCall3>(taken[3]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieLayer::updateProperties(frame);
  }

  //  QLottieBase *QLottieLayer::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieLayerCall4 call = reinterpret_cast<CuteQLottieLayerCall4>(taken[4]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieLayer::findChild(childName);
  }

  //  QSize QLottieLayer::layerSize() const
  QSize layerSize() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieLayerCall5 call = reinterpret_cast<CuteQLottieLayerCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieLayer::layerSize();
  }

  //  QLottieLayer *QLottieLayer::resolveLinkedLayer()
  QLottieLayer *resolveLinkedLayer() override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieLayerCall6 call = reinterpret_cast<CuteQLottieLayerCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieLayer *>(given);
    }
    return QLottieLayer::resolveLinkedLayer();
  }

  //  QLottieLayer *QLottieLayer::linkedLayer() const
  QLottieLayer *linkedLayer() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieLayerCall7 call = reinterpret_cast<CuteQLottieLayerCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieLayer *>(given);
    }
    return QLottieLayer::linkedLayer();
  }

  //  bool QLottieBase::setProperty(QLottieLiteral::PropertyType
  //      propertyType, QVariant value)
  bool setProperty(
      QLottieLiteral::PropertyType propertyType,
      QVariant value) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottieLayerCall8 call = reinterpret_cast<CuteQLottieLayerCall8>(taken[8]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }
};

//  QLottieLayer::QLottieLayer()
extern "C" Q_DECL_EXPORT
QLottieLayer *ritual_ZN12QLottieLayerC1Ev() {
  return new CuteQLottieLayer();
}

//  QLottieLayer::QLottieLayer(const QLottieLayer &other)
extern "C" Q_DECL_EXPORT
QLottieLayer *ritual_ZN12QLottieLayerC1ERKS_(const QLottieLayer *other) {
  return new CuteQLottieLayer(*other);
}

//  QLottieLayer::~QLottieLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLottieLayerD1Ev(QLottieLayer *self) {
  delete self;
}

//  QLottieBase *QLottieLayer::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK12QLottieLayer5cloneEv(const QLottieLayer *self) {
  return self->clone();
}

//  QLottieLayer *QLottieLayer::construct(QJsonObject definition)
extern "C" Q_DECL_EXPORT
QLottieLayer *ritual_ZN12QLottieLayer9constructE11QJsonObject(
    const QJsonObject *definition) {
  return QLottieLayer::construct(*definition);
}

//  QLottieLayer *QLottieLayer::constructMaskLayer(QLottieLayer *layer)
extern "C" Q_DECL_EXPORT
QLottieLayer *ritual_ZN12QLottieLayer18constructMaskLayerEPS_(
    QLottieLayer *layer) {
  return QLottieLayer::constructMaskLayer(layer);
}

//  int QLottieLayer::constructLayers(QJsonArray jsonLayers, QLottieBase
//      *parent, const QMap<QString, QJsonObject> &assets)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QLottieLayer15constructLayersE10QJsonArrayP11QLottieBaseRK4QMapI7QString11QJsonObjectE(
    const QJsonArray *jsonLayers,
    QLottieBase *parent,
    const QMap<QString, QJsonObject> *assets) {
  return QLottieLayer::constructLayers(*jsonLayers, parent, *assets);
}

//  bool QLottieLayer::active(int frame) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLottieLayer6activeEi(const QLottieLayer *self, int frame) {
  return self->active(frame);
}

//  int QLottieLayer::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QLottieLayer5parseERK11QJsonObject(
    QLottieLayer *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  void QLottieLayer::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLottieLayer16updatePropertiesEi(
    QLottieLayer *self,
    int frame) {
  self->updateProperties(frame);
}

//  QLottieBase *QLottieLayer::findChild(const QString &childName)
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZN12QLottieLayer9findChildERK7QString(
    QLottieLayer *self,
    const QString *childName) {
  return self->findChild(*childName);
}

//  bool QLottieLayer::isUsingMatteLayer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLottieLayer17isUsingMatteLayerEv(
    const QLottieLayer *self) {
  return self->isUsingMatteLayer();
}

//  bool QLottieLayer::isMatteLayer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLottieLayer12isMatteLayerEv(const QLottieLayer *self) {
  return self->isMatteLayer();
}

//  MatteClipMode QLottieLayer::matteMode() const
extern "C" Q_DECL_EXPORT
QLottieLayer::MatteClipMode ritual_ZNK12QLottieLayer9matteModeEv(
    const QLottieLayer *self) {
  return self->matteMode();
}

//  bool QLottieLayer::isAutoOrienting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLottieLayer15isAutoOrientingEv(const QLottieLayer *self) {
  return self->isAutoOrienting();
}

//  int QLottieLayer::layerId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QLottieLayer7layerIdEv(const QLottieLayer *self) {
  return self->layerId();
}

//  QLottieBasicTransform *QLottieLayer::transform() const
extern "C" Q_DECL_EXPORT
QLottieBasicTransform *ritual_ZNK12QLottieLayer9transformEv(
    const QLottieLayer *self) {
  return self->transform();
}

//  bool QLottieLayer::hasLinkedLayer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLottieLayer14hasLinkedLayerEv(const QLottieLayer *self) {
  return self->hasLinkedLayer();
}

//  int QLottieLayer::linkedLayerId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QLottieLayer13linkedLayerIdEv(const QLottieLayer *self) {
  return self->linkedLayerId();
}

//  QSize QLottieLayer::layerSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QLottieLayer9layerSizeEv(const QLottieLayer *self) {
  return new QSize(self->layerSize());
}

//  int QLottieLayer::startFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QLottieLayer10startFrameEv(const QLottieLayer *self) {
  return self->startFrame();
}

//  int QLottieLayer::endFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QLottieLayer8endFrameEv(const QLottieLayer *self) {
  return self->endFrame();
}

//  qreal QLottieLayer::frameOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QLottieLayer11frameOffsetEv(const QLottieLayer *self) {
  return self->frameOffset();
}

//  qreal QLottieLayer::timeStretch() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QLottieLayer11timeStretchEv(const QLottieLayer *self) {
  return self->timeStretch();
}

//  const QLottieLayer *QLottieLayer::checkedCast(const QLottieBase *node)
extern "C" Q_DECL_EXPORT
const QLottieLayer *ritual_ZN12QLottieLayer11checkedCastEPK11QLottieBase(
    const QLottieBase *node) {
  return QLottieLayer::checkedCast(node);
}

//  QLottieLayer *QLottieLayer::resolveLinkedLayer()
extern "C" Q_DECL_EXPORT
QLottieLayer *ritual_ZN12QLottieLayer18resolveLinkedLayerEv(
    QLottieLayer *self) {
  return self->resolveLinkedLayer();
}

//  QLottieLayer *QLottieLayer::linkedLayer() const
extern "C" Q_DECL_EXPORT
QLottieLayer *ritual_ZNK12QLottieLayer11linkedLayerEv(
    const QLottieLayer *self) {
  return self->linkedLayer();
}

//  void QLottieLayer::parseEffects(const QJsonArray &definition, QLottieBase
//      *effectRoot)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLottieLayer12parseEffectsERK10QJsonArrayP11QLottieBase(
    QLottieLayer *self,
    const QJsonArray *definition,
    QLottieBase *effectRoot) {
  self->parseEffects(*definition, effectRoot);
}

//  a Python function taken by a CuteQLottieLayer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieLayer(
    QLottieLayer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieLayer *>(self)->take(key, call);
}

//  QLottieBase *QLottieLayer::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK12QLottieLayer5cloneEv(const QLottieLayer *self) {
  return self->QLottieLayer::clone();
}

//  bool QLottieLayer::active(int frame) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QLottieLayer6activeEi(
    const QLottieLayer *self,
    int frame) {
  return self->QLottieLayer::active(frame);
}

//  int QLottieLayer::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN12QLottieLayer5parseERK11QJsonObject(
    QLottieLayer *self,
    const QJsonObject *definition) {
  return self->QLottieLayer::parse(*definition);
}

//  void QLottieLayer::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QLottieLayer16updatePropertiesEi(
    QLottieLayer *self,
    int frame) {
  self->QLottieLayer::updateProperties(frame);
}

//  QLottieBase *QLottieLayer::findChild(const QString &childName)
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZN12QLottieLayer9findChildERK7QString(
    QLottieLayer *self,
    const QString *childName) {
  return self->QLottieLayer::findChild(*childName);
}

//  QSize QLottieLayer::layerSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK12QLottieLayer9layerSizeEv(const QLottieLayer *self) {
  return new QSize(self->QLottieLayer::layerSize());
}

//  QLottieLayer *QLottieLayer::resolveLinkedLayer()
extern "C" Q_DECL_EXPORT
QLottieLayer *ritual_own_ZN12QLottieLayer18resolveLinkedLayerEv(
    QLottieLayer *self) {
  return static_cast<OwnQLottieLayer *>(self)->OwnQLottieLayer::resolveLinkedLayer();
}

//  QLottieLayer *QLottieLayer::linkedLayer() const
extern "C" Q_DECL_EXPORT
QLottieLayer *ritual_own_ZNK12QLottieLayer11linkedLayerEv(
    const QLottieLayer *self) {
  return static_cast<const OwnQLottieLayer *>(self)->OwnQLottieLayer::linkedLayer();
}

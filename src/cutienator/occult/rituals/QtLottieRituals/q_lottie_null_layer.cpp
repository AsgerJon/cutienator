//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottieflatlayers_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottieflatlayers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QLottieNullLayer that Python can take functions over in. Every QLottieNullLayer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieNullLayerCall0)(const void *, int *);
typedef int (*CuteQLottieNullLayerCall1)(const void *, const QJsonObject *, int *);
typedef bool (*CuteQLottieNullLayerCall2)(const void *, int, int *);
typedef void (*CuteQLottieNullLayerCall3)(const void *, int, int *);
typedef void * (*CuteQLottieNullLayerCall4)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieNullLayerCall5)(const void *, int *);
typedef void * (*CuteQLottieNullLayerCall6)(const void *, int *);
typedef void * (*CuteQLottieNullLayerCall7)(const void *, int *);
typedef bool (*CuteQLottieNullLayerCall8)(const void *, int, const QVariant *, int *);
class CuteQLottieNullLayer : public QLottieNullLayer {
public:
  using QLottieNullLayer::QLottieNullLayer;
  CuteQLottieNullLayer(const QLottieNullLayer & other) : QLottieNullLayer(other) {}
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase6activeEi")) {
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

  //  QLottieBase *QLottieNullLayer::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieNullLayerCall0 call = reinterpret_cast<CuteQLottieNullLayerCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieNullLayer::clone();
  }

  //  int QLottieNullLayer::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieNullLayerCall1 call = reinterpret_cast<CuteQLottieNullLayerCall1>(taken[1]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieNullLayer::parse(definition);
  }

  //  bool QLottieLayer::active(int frame) const
  bool active(int frame) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieNullLayerCall2 call = reinterpret_cast<CuteQLottieNullLayerCall2>(taken[2]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieLayer::active(frame);
  }

  //  void QLottieLayer::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieNullLayerCall3 call = reinterpret_cast<CuteQLottieNullLayerCall3>(taken[3]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieLayer::updateProperties(frame);
  }

  //  QLottieBase *QLottieLayer::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieNullLayerCall4 call = reinterpret_cast<CuteQLottieNullLayerCall4>(taken[4]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieLayer::findChild(childName);
  }

  //  QSize QLottieLayer::layerSize() const
  QSize layerSize() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieNullLayerCall5 call = reinterpret_cast<CuteQLottieNullLayerCall5>(taken[5]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieLayer::layerSize();
  }

  //  QLottieLayer *QLottieLayer::resolveLinkedLayer()
  QLottieLayer *resolveLinkedLayer() override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieNullLayerCall6 call = reinterpret_cast<CuteQLottieNullLayerCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieLayer *>(given);
    }
    return QLottieLayer::resolveLinkedLayer();
  }

  //  QLottieLayer *QLottieLayer::linkedLayer() const
  QLottieLayer *linkedLayer() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieNullLayerCall7 call = reinterpret_cast<CuteQLottieNullLayerCall7>(taken[7]);
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
      CuteQLottieNullLayerCall8 call = reinterpret_cast<CuteQLottieNullLayerCall8>(taken[8]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }
};

//  QLottieNullLayer::QLottieNullLayer()
extern "C" Q_DECL_EXPORT
QLottieNullLayer *ritual_ZN16QLottieNullLayerC1Ev() {
  return new CuteQLottieNullLayer();
}

//  QLottieNullLayer::QLottieNullLayer(const QLottieNullLayer &other)
extern "C" Q_DECL_EXPORT
QLottieNullLayer *ritual_ZN16QLottieNullLayerC1ERKS_(
    const QLottieNullLayer *other) {
  return new CuteQLottieNullLayer(*other);
}

//  QLottieBase *QLottieNullLayer::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK16QLottieNullLayer5cloneEv(
    const QLottieNullLayer *self) {
  return self->clone();
}

//  void QLottieNullLayer::render(QLottieRenderer &render) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QLottieNullLayer6renderER15QLottieRenderer(
    const QLottieNullLayer *self,
    QLottieRenderer *render) {
  self->render(*render);
}

//  int QLottieNullLayer::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QLottieNullLayer5parseERK11QJsonObject(
    QLottieNullLayer *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  QLottieNullLayer::~QLottieNullLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLottieNullLayerD1Ev(QLottieNullLayer *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieNullLayer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieNullLayer(
    QLottieNullLayer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieNullLayer *>(self)->take(key, call);
}

//  QLottieBase *QLottieNullLayer::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK16QLottieNullLayer5cloneEv(
    const QLottieNullLayer *self) {
  return self->QLottieNullLayer::clone();
}

//  int QLottieNullLayer::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN16QLottieNullLayer5parseERK11QJsonObject(
    QLottieNullLayer *self,
    const QJsonObject *definition) {
  return self->QLottieNullLayer::parse(*definition);
}

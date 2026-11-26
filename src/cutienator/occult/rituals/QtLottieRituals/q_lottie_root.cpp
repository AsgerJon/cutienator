//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottieroot_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottieroot_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottieprecomposition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>

//  A QLottieRoot that Python can take functions over in. Every QLottieRoot
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieRootCall0)(const void *, int *);
typedef void (*CuteQLottieRootCall1)(const void *, int, int *);
typedef const QSize * (*CuteQLottieRootCall2)(const void *, int *);
typedef bool (*CuteQLottieRootCall3)(const void *, int, const QVariant *, int *);
typedef int (*CuteQLottieRootCall4)(const void *, const QJsonObject *, int *);
typedef bool (*CuteQLottieRootCall5)(const void *, int, int *);
typedef void * (*CuteQLottieRootCall6)(const void *, const QString *, int *);
class CuteQLottieRoot : public QLottieRoot {
public:
  using QLottieRoot::QLottieRoot;
  CuteQLottieRoot(const QLottieRoot & other) : QLottieRoot(other) {}
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase9layerSizeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase6activeEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase9findChildERK7QString")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  QLottieBase *QLottieRoot::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieRootCall0 call = reinterpret_cast<CuteQLottieRootCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieRoot::clone();
  }

  //  void QLottieRoot::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieRootCall1 call = reinterpret_cast<CuteQLottieRootCall1>(taken[1]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieRoot::updateProperties(frame);
  }

  //  QSize QLottieRoot::layerSize() const
  QSize layerSize() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieRootCall2 call = reinterpret_cast<CuteQLottieRootCall2>(taken[2]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieRoot::layerSize();
  }

  //  bool QLottieBase::setProperty(QLottieLiteral::PropertyType
  //      propertyType, QVariant value)
  bool setProperty(
      QLottieLiteral::PropertyType propertyType,
      QVariant value) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieRootCall3 call = reinterpret_cast<CuteQLottieRootCall3>(taken[3]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  int QLottieBase::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieRootCall4 call = reinterpret_cast<CuteQLottieRootCall4>(taken[4]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieBase::parse(definition);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieRootCall5 call = reinterpret_cast<CuteQLottieRootCall5>(taken[5]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieRootCall6 call = reinterpret_cast<CuteQLottieRootCall6>(taken[6]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }
};

//  QLottieRoot::QLottieRoot()
extern "C" Q_DECL_EXPORT
QLottieRoot *ritual_ZN11QLottieRootC1Ev() {
  return new CuteQLottieRoot();
}

//  QLottieRoot::QLottieRoot(const QLottieRoot &other)
extern "C" Q_DECL_EXPORT
QLottieRoot *ritual_ZN11QLottieRootC1ERKS_(const QLottieRoot *other) {
  return new CuteQLottieRoot(*other);
}

//  QLottieRoot::~QLottieRoot()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieRootD1Ev(QLottieRoot *self) {
  delete self;
}

//  QLottieBase *QLottieRoot::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK11QLottieRoot5cloneEv(const QLottieRoot *self) {
  return self->clone();
}

//  void QLottieRoot::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieRoot16updatePropertiesEi(
    QLottieRoot *self,
    int frame) {
  self->updateProperties(frame);
}

//  QSize QLottieRoot::layerSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QLottieRoot9layerSizeEv(const QLottieRoot *self) {
  return new QSize(self->layerSize());
}

//  int QLottieRoot::parseSource(const QByteArray &jsonSource, const QUrl
//      &fileSource)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QLottieRoot11parseSourceERK10QByteArrayRK4QUrl(
    QLottieRoot *self,
    const QByteArray *jsonSource,
    const QUrl *fileSource) {
  return self->parseSource(*jsonSource, *fileSource);
}

//  void QLottieRoot::setStructureDumping(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLottieRoot19setStructureDumpingEb(
    QLottieRoot *self,
    bool enabled) {
  self->setStructureDumping(enabled);
}

//  int QLottieRoot::startFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLottieRoot10startFrameEv(const QLottieRoot *self) {
  return self->startFrame();
}

//  int QLottieRoot::endFrame() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLottieRoot8endFrameEv(const QLottieRoot *self) {
  return self->endFrame();
}

//  int QLottieRoot::frameRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QLottieRoot9frameRateEv(const QLottieRoot *self) {
  return self->frameRate();
}

//  QMap<QString, QLottiePrecomposition *> QLottieRoot::precompositions()
//      const
extern "C" Q_DECL_EXPORT
QMap<QString, QLottiePrecomposition *> *ritual_ZNK11QLottieRoot15precompositionsEv(
    const QLottieRoot *self) {
  return new QMap<QString, QLottiePrecomposition *>(self->precompositions());
}

//  bool QLottieRoot::resolvePrecompLayers(QLottieBase *element,
//      QStack<QString> *visitedIds)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QLottieRoot20resolvePrecompLayersEP11QLottieBaseP6QStackI7QStringE(
    QLottieRoot *self,
    QLottieBase *element,
    QStack<QString> *visitedIds) {
  return self->resolvePrecompLayers(element, visitedIds);
}

//  a Python function taken by a CuteQLottieRoot, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieRoot(
    QLottieRoot *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieRoot *>(self)->take(key, call);
}

//  QLottieBase *QLottieRoot::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK11QLottieRoot5cloneEv(const QLottieRoot *self) {
  return self->QLottieRoot::clone();
}

//  void QLottieRoot::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QLottieRoot16updatePropertiesEi(
    QLottieRoot *self,
    int frame) {
  self->QLottieRoot::updateProperties(frame);
}

//  QSize QLottieRoot::layerSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK11QLottieRoot9layerSizeEv(const QLottieRoot *self) {
  return new QSize(self->QLottieRoot::layerSize());
}

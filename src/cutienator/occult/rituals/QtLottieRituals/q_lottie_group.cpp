//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottiegroup_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiegroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QLottieGroup that Python can take functions over in. Every QLottieGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieGroupCall0)(const void *, int *);
typedef void (*CuteQLottieGroupCall1)(const void *, int, int *);
typedef int (*CuteQLottieGroupCall2)(const void *, const QJsonObject *, int *);
typedef bool (*CuteQLottieGroupCall3)(const void *, int *);
typedef void (*CuteQLottieGroupCall4)(const void *, const QLottieTrimPath *, int *);
typedef bool (*CuteQLottieGroupCall5)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieGroupCall6)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieGroupCall7)(const void *, int *);
typedef bool (*CuteQLottieGroupCall8)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQLottieGroupCall9)(const void *, int, int *);
typedef void * (*CuteQLottieGroupCall10)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieGroupCall11)(const void *, int *);
class CuteQLottieGroup : public QLottieGroup {
public:
  using QLottieGroup::QLottieGroup;
  CuteQLottieGroup(const QLottieGroup & other) : QLottieGroup(other) {}
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape11acceptsTrimEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QLottieShape9applyTrimERK15QLottieTrimPath")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape10isAnimatedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape4pathEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape12fallbackPathEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase11setPropertyEN14QLottieLiteral12PropertyTypeE8QVariant")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase6activeEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase9findChildERK7QString")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QLottieBase9layerSizeEv")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

  //  QLottieBase *QLottieGroup::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieGroupCall0 call = reinterpret_cast<CuteQLottieGroupCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieGroup::clone();
  }

  //  void QLottieGroup::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieGroupCall1 call = reinterpret_cast<CuteQLottieGroupCall1>(taken[1]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieGroup::updateProperties(frame);
  }

  //  int QLottieGroup::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieGroupCall2 call = reinterpret_cast<CuteQLottieGroupCall2>(taken[2]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieGroup::parse(definition);
  }

  //  bool QLottieGroup::acceptsTrim() const
  bool acceptsTrim() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieGroupCall3 call = reinterpret_cast<CuteQLottieGroupCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieGroup::acceptsTrim();
  }

  //  void QLottieGroup::applyTrim(const QLottieTrimPath &trimmer)
  void applyTrim(const QLottieTrimPath &trimmer) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieGroupCall4 call = reinterpret_cast<CuteQLottieGroupCall4>(taken[4]);
      call(this, &trimmer, &handled);
      if (handled) return;
    }
    QLottieGroup::applyTrim(trimmer);
  }

  //  bool QLottieShape::isAnimated() const
  bool isAnimated() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieGroupCall5 call = reinterpret_cast<CuteQLottieGroupCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::isAnimated();
  }

  //  const QPainterPath &QLottieShape::path() const
  const QPainterPath &path() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieGroupCall6 call = reinterpret_cast<CuteQLottieGroupCall6>(taken[6]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::path();
  }

  //  QPainterPath QLottieShape::fallbackPath() const
  QPainterPath fallbackPath() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieGroupCall7 call = reinterpret_cast<CuteQLottieGroupCall7>(taken[7]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::fallbackPath();
  }

  //  bool QLottieBase::setProperty(QLottieLiteral::PropertyType
  //      propertyType, QVariant value)
  bool setProperty(
      QLottieLiteral::PropertyType propertyType,
      QVariant value) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottieGroupCall8 call = reinterpret_cast<CuteQLottieGroupCall8>(taken[8]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLottieGroupCall9 call = reinterpret_cast<CuteQLottieGroupCall9>(taken[9]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieGroupCall10 call = reinterpret_cast<CuteQLottieGroupCall10>(taken[10]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieGroupCall11 call = reinterpret_cast<CuteQLottieGroupCall11>(taken[11]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieGroup::QLottieGroup(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieGroup *ritual_ZN12QLottieGroupC1EP11QLottieBase(QLottieBase *parent) {
  return new CuteQLottieGroup(parent);
}

//  QLottieBase *QLottieGroup::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK12QLottieGroup5cloneEv(const QLottieGroup *self) {
  return self->clone();
}

//  void QLottieGroup::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLottieGroup16updatePropertiesEi(
    QLottieGroup *self,
    int frame) {
  self->updateProperties(frame);
}

//  void QLottieGroup::render(QLottieRenderer &renderer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QLottieGroup6renderER15QLottieRenderer(
    const QLottieGroup *self,
    QLottieRenderer *renderer) {
  self->render(*renderer);
}

//  int QLottieGroup::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QLottieGroup5parseERK11QJsonObject(
    QLottieGroup *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  bool QLottieGroup::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLottieGroup11acceptsTrimEv(const QLottieGroup *self) {
  return self->acceptsTrim();
}

//  void QLottieGroup::applyTrim(const QLottieTrimPath &trimmer)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLottieGroup9applyTrimERK15QLottieTrimPath(
    QLottieGroup *self,
    const QLottieTrimPath *trimmer) {
  self->applyTrim(*trimmer);
}

//  QLottieGroup::~QLottieGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLottieGroupD1Ev(QLottieGroup *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieGroup, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieGroup(
    QLottieGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieGroup *>(self)->take(key, call);
}

//  QLottieBase *QLottieGroup::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK12QLottieGroup5cloneEv(const QLottieGroup *self) {
  return self->QLottieGroup::clone();
}

//  void QLottieGroup::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QLottieGroup16updatePropertiesEi(
    QLottieGroup *self,
    int frame) {
  self->QLottieGroup::updateProperties(frame);
}

//  int QLottieGroup::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN12QLottieGroup5parseERK11QJsonObject(
    QLottieGroup *self,
    const QJsonObject *definition) {
  return self->QLottieGroup::parse(*definition);
}

//  bool QLottieGroup::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QLottieGroup11acceptsTrimEv(const QLottieGroup *self) {
  return self->QLottieGroup::acceptsTrim();
}

//  void QLottieGroup::applyTrim(const QLottieTrimPath &trimmer)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QLottieGroup9applyTrimERK15QLottieTrimPath(
    QLottieGroup *self,
    const QLottieTrimPath *trimmer) {
  self->QLottieGroup::applyTrim(*trimmer);
}

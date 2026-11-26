//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottieround_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottieround_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QLottieRound that Python can take functions over in. Every QLottieRound
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieRoundCall0)(const void *, int *);
typedef int (*CuteQLottieRoundCall1)(const void *, const QJsonObject *, int *);
typedef void (*CuteQLottieRoundCall2)(const void *, int, int *);
typedef bool (*CuteQLottieRoundCall3)(const void *, int *);
typedef bool (*CuteQLottieRoundCall4)(const void *, int *);
typedef const QPainterPath * (*CuteQLottieRoundCall5)(const void *, int *);
typedef void (*CuteQLottieRoundCall6)(const void *, const QLottieTrimPath *, int *);
typedef const QPainterPath * (*CuteQLottieRoundCall7)(const void *, int *);
typedef bool (*CuteQLottieRoundCall8)(const void *, int, const QVariant *, int *);
typedef bool (*CuteQLottieRoundCall9)(const void *, int, int *);
typedef void * (*CuteQLottieRoundCall10)(const void *, const QString *, int *);
typedef const QSize * (*CuteQLottieRoundCall11)(const void *, int *);
class CuteQLottieRound : public QLottieRound {
public:
  using QLottieRound::QLottieRound;
  CuteQLottieRound(const QLottieRound & other) : QLottieRound(other) {}
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QLottieBase5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase5parseERK11QJsonObject")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QLottieBase16updatePropertiesEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape11acceptsTrimEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape10isAnimatedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QLottieShape4pathEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QLottieShape9applyTrimERK15QLottieTrimPath")) {
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

  //  QLottieBase *QLottieRound::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieRoundCall0 call = reinterpret_cast<CuteQLottieRoundCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieRound::clone();
  }

  //  int QLottieRound::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieRoundCall1 call = reinterpret_cast<CuteQLottieRoundCall1>(taken[1]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieRound::parse(definition);
  }

  //  void QLottieRound::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieRoundCall2 call = reinterpret_cast<CuteQLottieRoundCall2>(taken[2]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieRound::updateProperties(frame);
  }

  //  bool QLottieRound::acceptsTrim() const
  bool acceptsTrim() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieRoundCall3 call = reinterpret_cast<CuteQLottieRoundCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieRound::acceptsTrim();
  }

  //  bool QLottieShape::isAnimated() const
  bool isAnimated() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieRoundCall4 call = reinterpret_cast<CuteQLottieRoundCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLottieShape::isAnimated();
  }

  //  const QPainterPath &QLottieShape::path() const
  const QPainterPath &path() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieRoundCall5 call = reinterpret_cast<CuteQLottieRoundCall5>(taken[5]);
      const QPainterPath * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieShape::path();
  }

  //  void QLottieShape::applyTrim(const QLottieTrimPath &trimmer)
  void applyTrim(const QLottieTrimPath &trimmer) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieRoundCall6 call = reinterpret_cast<CuteQLottieRoundCall6>(taken[6]);
      call(this, &trimmer, &handled);
      if (handled) return;
    }
    QLottieShape::applyTrim(trimmer);
  }

  //  QPainterPath QLottieShape::fallbackPath() const
  QPainterPath fallbackPath() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieRoundCall7 call = reinterpret_cast<CuteQLottieRoundCall7>(taken[7]);
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
      CuteQLottieRoundCall8 call = reinterpret_cast<CuteQLottieRoundCall8>(taken[8]);
      bool given = call(this, static_cast<int>(propertyType), &value, &handled);
      if (handled) return given;
    }
    return QLottieBase::setProperty(propertyType, value);
  }

  //  bool QLottieBase::active(int frame) const
  bool active(int frame) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLottieRoundCall9 call = reinterpret_cast<CuteQLottieRoundCall9>(taken[9]);
      bool given = call(this, frame, &handled);
      if (handled) return given;
    }
    return QLottieBase::active(frame);
  }

  //  QLottieBase *QLottieBase::findChild(const QString &childName)
  QLottieBase *findChild(const QString &childName) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieRoundCall10 call = reinterpret_cast<CuteQLottieRoundCall10>(taken[10]);
      void * given = call(this, &childName, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieBase::findChild(childName);
  }

  //  QSize QLottieBase::layerSize() const
  QSize layerSize() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieRoundCall11 call = reinterpret_cast<CuteQLottieRoundCall11>(taken[11]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QLottieBase::layerSize();
  }
};

//  QLottieRound::QLottieRound(const QLottieRound &other)
extern "C" Q_DECL_EXPORT
QLottieRound *ritual_ZN12QLottieRoundC1ERKS_(const QLottieRound *other) {
  return new CuteQLottieRound(*other);
}

//  QLottieRound::QLottieRound(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieRound *ritual_ZN12QLottieRoundC1EP11QLottieBase(QLottieBase *parent) {
  return new CuteQLottieRound(parent);
}

//  QLottieBase *QLottieRound::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK12QLottieRound5cloneEv(const QLottieRound *self) {
  return self->clone();
}

//  int QLottieRound::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QLottieRound5parseERK11QJsonObject(
    QLottieRound *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  void QLottieRound::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLottieRound16updatePropertiesEi(
    QLottieRound *self,
    int frame) {
  self->updateProperties(frame);
}

//  void QLottieRound::render(QLottieRenderer &renderer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QLottieRound6renderER15QLottieRenderer(
    const QLottieRound *self,
    QLottieRenderer *renderer) {
  self->render(*renderer);
}

//  bool QLottieRound::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLottieRound11acceptsTrimEv(const QLottieRound *self) {
  return self->acceptsTrim();
}

//  QPointF QLottieRound::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QLottieRound8positionEv(const QLottieRound *self) {
  return new QPointF(self->position());
}

//  qreal QLottieRound::radius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QLottieRound6radiusEv(const QLottieRound *self) {
  return self->radius();
}

//  QLottieRound::~QLottieRound()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLottieRoundD1Ev(QLottieRound *self) {
  delete self;
}

//  a Python function taken by a CuteQLottieRound, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieRound(
    QLottieRound *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieRound *>(self)->take(key, call);
}

//  QLottieBase *QLottieRound::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK12QLottieRound5cloneEv(const QLottieRound *self) {
  return self->QLottieRound::clone();
}

//  int QLottieRound::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN12QLottieRound5parseERK11QJsonObject(
    QLottieRound *self,
    const QJsonObject *definition) {
  return self->QLottieRound::parse(*definition);
}

//  void QLottieRound::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QLottieRound16updatePropertiesEi(
    QLottieRound *self,
    int frame) {
  self->QLottieRound::updateProperties(frame);
}

//  bool QLottieRound::acceptsTrim() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QLottieRound11acceptsTrimEv(const QLottieRound *self) {
  return self->QLottieRound::acceptsTrim();
}

//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottiegfill_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottiegfill_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <cstring>

//  A QLottieGFill that Python can take functions over in. Every QLottieGFill
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQLottieGFillCall0)(const void *, int *);
typedef void (*CuteQLottieGFillCall1)(const void *, int, int *);
typedef int (*CuteQLottieGFillCall2)(const void *, const QJsonObject *, int *);
class CuteQLottieGFill : public QLottieGFill {
public:
  using QLottieGFill::QLottieGFill;
  CuteQLottieGFill(const QLottieGFill &other) : QLottieGFill(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QLottieGFill5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QLottieGFill16updatePropertiesEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QLottieGFill5parseERK11QJsonObject")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QLottieBase *QLottieGFill::clone() const
  QLottieBase *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieGFillCall0 call = reinterpret_cast<CuteQLottieGFillCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLottieBase *>(given);
    }
    return QLottieGFill::clone();
  }

  //  void QLottieGFill::updateProperties(int frame)
  void updateProperties(int frame) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieGFillCall1 call = reinterpret_cast<CuteQLottieGFillCall1>(taken[1]);
      call(this, frame, &handled);
      if (handled) return;
    }
    QLottieGFill::updateProperties(frame);
  }

  //  int QLottieGFill::parse(const QJsonObject &definition)
  int parse(const QJsonObject &definition) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieGFillCall2 call = reinterpret_cast<CuteQLottieGFillCall2>(taken[2]);
      int given = call(this, &definition, &handled);
      if (handled) return given;
    }
    return QLottieGFill::parse(definition);
  }
};

//  QLottieGFill::QLottieGFill(const QLottieGFill &other)
extern "C" Q_DECL_EXPORT
QLottieGFill *ritual_ZN12QLottieGFillC1ERKS_(const QLottieGFill *other) {
  return new CuteQLottieGFill(*other);
}

//  QLottieGFill::QLottieGFill(QLottieBase *parent)
extern "C" Q_DECL_EXPORT
QLottieGFill *ritual_ZN12QLottieGFillC1EP11QLottieBase(QLottieBase *parent) {
  return new CuteQLottieGFill(parent);
}

//  QLottieGFill::~QLottieGFill()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLottieGFillD1Ev(QLottieGFill *self) {
  delete self;
}

//  QLottieBase *QLottieGFill::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_ZNK12QLottieGFill5cloneEv(const QLottieGFill *self) {
  return self->clone();
}

//  void QLottieGFill::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLottieGFill16updatePropertiesEi(
    QLottieGFill *self,
    int frame) {
  self->updateProperties(frame);
}

//  int QLottieGFill::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QLottieGFill5parseERK11QJsonObject(
    QLottieGFill *self,
    const QJsonObject *definition) {
  return self->parse(*definition);
}

//  Qt::FillRule QLottieGFill::fillRule() const
extern "C" Q_DECL_EXPORT
Qt::FillRule ritual_ZNK12QLottieGFill8fillRuleEv(const QLottieGFill *self) {
  return self->fillRule();
}

//  a Python function taken by a CuteQLottieGFill, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieGFill(
    QLottieGFill *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieGFill *>(self)->take(key, call);
}

//  QLottieBase *QLottieGFill::clone() const
extern "C" Q_DECL_EXPORT
QLottieBase *ritual_own_ZNK12QLottieGFill5cloneEv(const QLottieGFill *self) {
  return self->QLottieGFill::clone();
}

//  void QLottieGFill::updateProperties(int frame)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QLottieGFill16updatePropertiesEi(
    QLottieGFill *self,
    int frame) {
  self->QLottieGFill::updateProperties(frame);
}

//  int QLottieGFill::parse(const QJsonObject &definition)
extern "C" Q_DECL_EXPORT
int ritual_own_ZN12QLottieGFill5parseERK11QJsonObject(
    QLottieGFill *self,
    const QJsonObject *definition) {
  return self->QLottieGFill::parse(*definition);
}

//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlglobal_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A QQmlColorProvider that Python can take functions over in. Every QQmlColorProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQQmlColorProviderCall0)(const void *, double, double, double, double, int *);
typedef const QVariant * (*CuteQQmlColorProviderCall1)(const void *, double, double, double, double, int *);
typedef const QVariant * (*CuteQQmlColorProviderCall2)(const void *, double, double, double, double, int *);
typedef const QVariant * (*CuteQQmlColorProviderCall3)(const void *, const QVariant *, qreal, int *);
typedef const QVariant * (*CuteQQmlColorProviderCall4)(const void *, const QVariant *, qreal, int *);
typedef const QVariant * (*CuteQQmlColorProviderCall5)(const void *, const QVariant *, qreal, int *);
typedef const QVariant * (*CuteQQmlColorProviderCall6)(const void *, const QVariant *, const QVariant *, int *);
class CuteQQmlColorProvider : public QQmlColorProvider {
public:
  using QQmlColorProvider::QQmlColorProvider;
  CuteQQmlColorProvider(const QQmlColorProvider & other) : QQmlColorProvider(other) {}
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQmlColorProvider8fromRgbFEdddd")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQmlColorProvider8fromHslFEdddd")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQmlColorProvider8fromHsvFEdddd")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQmlColorProvider7lighterERK8QVariantd")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQmlColorProvider6darkerERK8QVariantd")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQmlColorProvider5alphaERK8QVariantd")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQmlColorProvider4tintERK8QVariantS2_")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  QVariant QQmlColorProvider::fromRgbF(double a0, double a1, double a2,
  //      double a3)
  QVariant fromRgbF(double a0, double a1, double a2, double a3) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlColorProviderCall0 call = reinterpret_cast<CuteQQmlColorProviderCall0>(taken[0]);
      const QVariant * given = call(this, a0, a1, a2, a3, &handled);
      if (handled && given) return *given;
    }
    return QQmlColorProvider::fromRgbF(a0, a1, a2, a3);
  }

  //  QVariant QQmlColorProvider::fromHslF(double a0, double a1, double a2,
  //      double a3)
  QVariant fromHslF(double a0, double a1, double a2, double a3) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlColorProviderCall1 call = reinterpret_cast<CuteQQmlColorProviderCall1>(taken[1]);
      const QVariant * given = call(this, a0, a1, a2, a3, &handled);
      if (handled && given) return *given;
    }
    return QQmlColorProvider::fromHslF(a0, a1, a2, a3);
  }

  //  QVariant QQmlColorProvider::fromHsvF(double a0, double a1, double a2,
  //      double a3)
  QVariant fromHsvF(double a0, double a1, double a2, double a3) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlColorProviderCall2 call = reinterpret_cast<CuteQQmlColorProviderCall2>(taken[2]);
      const QVariant * given = call(this, a0, a1, a2, a3, &handled);
      if (handled && given) return *given;
    }
    return QQmlColorProvider::fromHsvF(a0, a1, a2, a3);
  }

  //  QVariant QQmlColorProvider::lighter(const QVariant &a0, qreal a1)
  QVariant lighter(const QVariant &a0, qreal a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlColorProviderCall3 call = reinterpret_cast<CuteQQmlColorProviderCall3>(taken[3]);
      const QVariant * given = call(this, &a0, a1, &handled);
      if (handled && given) return *given;
    }
    return QQmlColorProvider::lighter(a0, a1);
  }

  //  QVariant QQmlColorProvider::darker(const QVariant &a0, qreal a1)
  QVariant darker(const QVariant &a0, qreal a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlColorProviderCall4 call = reinterpret_cast<CuteQQmlColorProviderCall4>(taken[4]);
      const QVariant * given = call(this, &a0, a1, &handled);
      if (handled && given) return *given;
    }
    return QQmlColorProvider::darker(a0, a1);
  }

  //  QVariant QQmlColorProvider::alpha(const QVariant &a0, qreal a1)
  QVariant alpha(const QVariant &a0, qreal a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlColorProviderCall5 call = reinterpret_cast<CuteQQmlColorProviderCall5>(taken[5]);
      const QVariant * given = call(this, &a0, a1, &handled);
      if (handled && given) return *given;
    }
    return QQmlColorProvider::alpha(a0, a1);
  }

  //  QVariant QQmlColorProvider::tint(const QVariant &a0, const QVariant
  //      &a1)
  QVariant tint(const QVariant &a0, const QVariant &a1) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlColorProviderCall6 call = reinterpret_cast<CuteQQmlColorProviderCall6>(taken[6]);
      const QVariant * given = call(this, &a0, &a1, &handled);
      if (handled && given) return *given;
    }
    return QQmlColorProvider::tint(a0, a1);
  }
};

//  QQmlColorProvider::~QQmlColorProvider()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlColorProviderD1Ev(QQmlColorProvider *self) {
  delete self;
}

//  QVariant QQmlColorProvider::colorFromString(const QString &a0, bool *a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN17QQmlColorProvider15colorFromStringERK7QStringPb(
    QQmlColorProvider *self,
    const QString *a0,
    bool *a1) {
  return new QVariant(self->colorFromString(*a0, a1));
}

//  unsigned int QQmlColorProvider::rgbaFromString(const QString &a0, bool
//      *a1)
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZN17QQmlColorProvider14rgbaFromStringERK7QStringPb(
    QQmlColorProvider *self,
    const QString *a0,
    bool *a1) {
  return self->rgbaFromString(*a0, a1);
}

//  QVariant QQmlColorProvider::fromRgbF(double a0, double a1, double a2,
//      double a3)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN17QQmlColorProvider8fromRgbFEdddd(
    QQmlColorProvider *self,
    double a0,
    double a1,
    double a2,
    double a3) {
  return new QVariant(self->fromRgbF(a0, a1, a2, a3));
}

//  QVariant QQmlColorProvider::fromHslF(double a0, double a1, double a2,
//      double a3)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN17QQmlColorProvider8fromHslFEdddd(
    QQmlColorProvider *self,
    double a0,
    double a1,
    double a2,
    double a3) {
  return new QVariant(self->fromHslF(a0, a1, a2, a3));
}

//  QVariant QQmlColorProvider::fromHsvF(double a0, double a1, double a2,
//      double a3)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN17QQmlColorProvider8fromHsvFEdddd(
    QQmlColorProvider *self,
    double a0,
    double a1,
    double a2,
    double a3) {
  return new QVariant(self->fromHsvF(a0, a1, a2, a3));
}

//  QVariant QQmlColorProvider::lighter(const QVariant &a0, qreal a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN17QQmlColorProvider7lighterERK8QVariantd(
    QQmlColorProvider *self,
    const QVariant *a0,
    qreal a1) {
  return new QVariant(self->lighter(*a0, a1));
}

//  QVariant QQmlColorProvider::darker(const QVariant &a0, qreal a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN17QQmlColorProvider6darkerERK8QVariantd(
    QQmlColorProvider *self,
    const QVariant *a0,
    qreal a1) {
  return new QVariant(self->darker(*a0, a1));
}

//  QVariant QQmlColorProvider::alpha(const QVariant &a0, qreal a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN17QQmlColorProvider5alphaERK8QVariantd(
    QQmlColorProvider *self,
    const QVariant *a0,
    qreal a1) {
  return new QVariant(self->alpha(*a0, a1));
}

//  QVariant QQmlColorProvider::tint(const QVariant &a0, const QVariant &a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN17QQmlColorProvider4tintERK8QVariantS2_(
    QQmlColorProvider *self,
    const QVariant *a0,
    const QVariant *a1) {
  return new QVariant(self->tint(*a0, *a1));
}

//  a Python function taken by a CuteQQmlColorProvider, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlColorProvider(
    QQmlColorProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlColorProvider *>(self)->take(key, call);
}

//  QVariant QQmlColorProvider::fromRgbF(double a0, double a1, double a2,
//      double a3)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN17QQmlColorProvider8fromRgbFEdddd(
    QQmlColorProvider *self,
    double a0,
    double a1,
    double a2,
    double a3) {
  return new QVariant(self->QQmlColorProvider::fromRgbF(a0, a1, a2, a3));
}

//  QVariant QQmlColorProvider::fromHslF(double a0, double a1, double a2,
//      double a3)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN17QQmlColorProvider8fromHslFEdddd(
    QQmlColorProvider *self,
    double a0,
    double a1,
    double a2,
    double a3) {
  return new QVariant(self->QQmlColorProvider::fromHslF(a0, a1, a2, a3));
}

//  QVariant QQmlColorProvider::fromHsvF(double a0, double a1, double a2,
//      double a3)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN17QQmlColorProvider8fromHsvFEdddd(
    QQmlColorProvider *self,
    double a0,
    double a1,
    double a2,
    double a3) {
  return new QVariant(self->QQmlColorProvider::fromHsvF(a0, a1, a2, a3));
}

//  QVariant QQmlColorProvider::lighter(const QVariant &a0, qreal a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN17QQmlColorProvider7lighterERK8QVariantd(
    QQmlColorProvider *self,
    const QVariant *a0,
    qreal a1) {
  return new QVariant(self->QQmlColorProvider::lighter(*a0, a1));
}

//  QVariant QQmlColorProvider::darker(const QVariant &a0, qreal a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN17QQmlColorProvider6darkerERK8QVariantd(
    QQmlColorProvider *self,
    const QVariant *a0,
    qreal a1) {
  return new QVariant(self->QQmlColorProvider::darker(*a0, a1));
}

//  QVariant QQmlColorProvider::alpha(const QVariant &a0, qreal a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN17QQmlColorProvider5alphaERK8QVariantd(
    QQmlColorProvider *self,
    const QVariant *a0,
    qreal a1) {
  return new QVariant(self->QQmlColorProvider::alpha(*a0, a1));
}

//  QVariant QQmlColorProvider::tint(const QVariant &a0, const QVariant &a1)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN17QQmlColorProvider4tintERK8QVariantS2_(
    QQmlColorProvider *self,
    const QVariant *a0,
    const QVariant *a1) {
  return new QVariant(self->QQmlColorProvider::tint(*a0, *a1));
}

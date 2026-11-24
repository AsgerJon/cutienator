//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlocale_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlocale.h>
#include <cstring>

//  A QSystemLocale that Python can take functions over in. Every QSystemLocale
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QLocale * (*CuteQSystemLocaleCall0)(const void *, int *);
class CuteQSystemLocale : public QSystemLocale {
public:
  using QSystemLocale::QSystemLocale;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13QSystemLocale14fallbackLocaleEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QLocale QSystemLocale::fallbackLocale() const
  QLocale fallbackLocale() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSystemLocaleCall0 call = reinterpret_cast<CuteQSystemLocaleCall0>(taken[0]);
      const QLocale * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSystemLocale::fallbackLocale();
  }
};

//  QSystemLocale::QSystemLocale()
extern "C" Q_DECL_EXPORT
QSystemLocale *ritual_ZN13QSystemLocaleC1Ev() {
  return new CuteQSystemLocale();
}

//  QSystemLocale::~QSystemLocale()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSystemLocaleD1Ev(QSystemLocale *self) {
  delete self;
}

//  QLocale QSystemLocale::fallbackLocale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK13QSystemLocale14fallbackLocaleEv(
    const QSystemLocale *self) {
  return new QLocale(self->fallbackLocale());
}

//  qsizetype QSystemLocale::fallbackLocaleIndex() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QSystemLocale19fallbackLocaleIndexEv(
    const QSystemLocale *self) {
  return self->fallbackLocaleIndex();
}

//  a Python function taken by a CuteQSystemLocale, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSystemLocale(
    QSystemLocale *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSystemLocale *>(self)->take(key, call);
}

//  QLocale QSystemLocale::fallbackLocale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_own_ZNK13QSystemLocale14fallbackLocaleEv(
    const QSystemLocale *self) {
  return new QLocale(self->QSystemLocale::fallbackLocale());
}

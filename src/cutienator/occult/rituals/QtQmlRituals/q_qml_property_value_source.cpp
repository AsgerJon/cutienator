//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlpropertyvaluesource.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlpropertyvaluesource.h>
#include <QtQml/qqmlproperty.h>
#include <cstring>

//  A QQmlPropertyValueSource that Python can take functions over in. Every QQmlPropertyValueSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlPropertyValueSourceCall0)(const void *, const QQmlProperty *, int *);
class CuteQQmlPropertyValueSource : public QQmlPropertyValueSource {
public:
  using QQmlPropertyValueSource::QQmlPropertyValueSource;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QQmlPropertyValueSource9setTargetERK12QQmlProperty")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQmlPropertyValueSource::setTarget(const QQmlProperty &a0)
  void setTarget(const QQmlProperty &a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlPropertyValueSourceCall0 call = reinterpret_cast<CuteQQmlPropertyValueSourceCall0>(taken[0]);
      call(this, &a0, &handled);
      if (handled) return;
    }
  }
};

//  QQmlPropertyValueSource::QQmlPropertyValueSource()
extern "C" Q_DECL_EXPORT
QQmlPropertyValueSource *ritual_ZN23QQmlPropertyValueSourceC1Ev() {
  return new CuteQQmlPropertyValueSource();
}

//  QQmlPropertyValueSource::~QQmlPropertyValueSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyValueSourceD1Ev(QQmlPropertyValueSource *self) {
  delete self;
}

//  void QQmlPropertyValueSource::setTarget(const QQmlProperty &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlPropertyValueSource9setTargetERK12QQmlProperty(
    QQmlPropertyValueSource *self,
    const QQmlProperty *a0) {
  self->setTarget(*a0);
}

//  a Python function taken by a CuteQQmlPropertyValueSource, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlPropertyValueSource(
    QQmlPropertyValueSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlPropertyValueSource *>(self)->take(key, call);
}

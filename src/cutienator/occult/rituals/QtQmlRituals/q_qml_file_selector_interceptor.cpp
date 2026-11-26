//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlfileselector_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlfileselector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <cstring>

//  Only a class built on QQmlFileSelectorInterceptor may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlFileSelectorInterceptor : QQmlFileSelectorInterceptor {
  using QQmlFileSelectorInterceptor::intercept;
};

//  A QQmlFileSelectorInterceptor that Python can take functions over in. Every QQmlFileSelectorInterceptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QUrl * (*CuteQQmlFileSelectorInterceptorCall0)(const void *, const QUrl *, int, int *);
class CuteQQmlFileSelectorInterceptor : public QQmlFileSelectorInterceptor {
public:
  using QQmlFileSelectorInterceptor::QQmlFileSelectorInterceptor;
  CuteQQmlFileSelectorInterceptor(const QQmlFileSelectorInterceptor & other) : QQmlFileSelectorInterceptor(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QQmlAbstractUrlInterceptor9interceptERK4QUrlNS_8DataTypeE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QUrl QQmlFileSelectorInterceptor::intercept(const QUrl &path,
  //      DataType type)
  QUrl intercept(
      const QUrl &path,
      QQmlAbstractUrlInterceptor::DataType type) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlFileSelectorInterceptorCall0 call = reinterpret_cast<CuteQQmlFileSelectorInterceptorCall0>(taken[0]);
      const QUrl * given = call(this, &path, static_cast<int>(type), &handled);
      if (handled && given) return *given;
    }
    return QQmlFileSelectorInterceptor::intercept(path, type);
  }
};

//  QQmlFileSelectorInterceptor::QQmlFileSelectorInterceptor(QQmlFileSelector
//      Private *pd)
extern "C" Q_DECL_EXPORT
QQmlFileSelectorInterceptor *ritual_ZN27QQmlFileSelectorInterceptorC1EP23QQmlFileSelectorPrivate(
    QQmlFileSelectorPrivate *pd) {
  return new CuteQQmlFileSelectorInterceptor(pd);
}

//  QUrl QQmlFileSelectorInterceptor::intercept(const QUrl &path, DataType
//      type)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN27QQmlFileSelectorInterceptor9interceptERK4QUrlN26QQmlAbstractUrlInterceptor8DataTypeE(
    QQmlFileSelectorInterceptor *self,
    const QUrl *path,
    QQmlAbstractUrlInterceptor::DataType type) {
  return new QUrl(self->intercept(*path, type));
}

//  QQmlFileSelectorInterceptor::~QQmlFileSelectorInterceptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlFileSelectorInterceptorD1Ev(
    QQmlFileSelectorInterceptor *self) {
  delete self;
}

//  a Python function taken by a CuteQQmlFileSelectorInterceptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlFileSelectorInterceptor(
    QQmlFileSelectorInterceptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlFileSelectorInterceptor *>(self)->take(key, call);
}

//  QUrl QQmlFileSelectorInterceptor::intercept(const QUrl &path, DataType
//      type)
extern "C" Q_DECL_EXPORT
QUrl *ritual_own_ZN27QQmlFileSelectorInterceptor9interceptERK4QUrlN26QQmlAbstractUrlInterceptor8DataTypeE(
    QQmlFileSelectorInterceptor *self,
    const QUrl *path,
    QQmlAbstractUrlInterceptor::DataType type) {
  return new QUrl(
      static_cast<OwnQQmlFileSelectorInterceptor *>(self)->OwnQQmlFileSelectorInterceptor::intercept(
          *path,
          type));
}

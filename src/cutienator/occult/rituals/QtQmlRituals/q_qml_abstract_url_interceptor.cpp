//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlabstracturlinterceptor.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlabstracturlinterceptor.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQmlAbstractUrlInterceptor that Python can take functions over in. Every QQmlAbstractUrlInterceptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QUrl * (*CuteQQmlAbstractUrlInterceptorCall0)(const void *, const QUrl *, int, int *);
class CuteQQmlAbstractUrlInterceptor : public QQmlAbstractUrlInterceptor {
public:
  using QQmlAbstractUrlInterceptor::QQmlAbstractUrlInterceptor;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QQmlAbstractUrlInterceptor9interceptERK4QUrlNS_8DataTypeE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QUrl QQmlAbstractUrlInterceptor::intercept(const QUrl &path, DataType
  //      type)
  QUrl intercept(
      const QUrl &path,
      QQmlAbstractUrlInterceptor::DataType type) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlAbstractUrlInterceptorCall0 call = reinterpret_cast<CuteQQmlAbstractUrlInterceptorCall0>(taken[0]);
      const QUrl * given = call(this, &path, static_cast<int>(type), &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QQmlAbstractUrlInterceptor::QQmlAbstractUrlInterceptor()
extern "C" Q_DECL_EXPORT
QQmlAbstractUrlInterceptor *ritual_ZN26QQmlAbstractUrlInterceptorC1Ev() {
  return new CuteQQmlAbstractUrlInterceptor();
}

//  QQmlAbstractUrlInterceptor::~QQmlAbstractUrlInterceptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQmlAbstractUrlInterceptorD1Ev(
    QQmlAbstractUrlInterceptor *self) {
  delete self;
}

//  QUrl QQmlAbstractUrlInterceptor::intercept(const QUrl &path, DataType
//      type)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN26QQmlAbstractUrlInterceptor9interceptERK4QUrlNS_8DataTypeE(
    QQmlAbstractUrlInterceptor *self,
    const QUrl *path,
    QQmlAbstractUrlInterceptor::DataType type) {
  return new QUrl(self->intercept(*path, type));
}

//  a Python function taken by a CuteQQmlAbstractUrlInterceptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlAbstractUrlInterceptor(
    QQmlAbstractUrlInterceptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlAbstractUrlInterceptor *>(self)->take(key, call);
}

//  QList<QQmlAbstractUrlInterceptor *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQmlAbstractUrlInterceptor *> *ritual_list_make_QQmlAbstractUrlInterceptor_ptr() {
  return new QList<QQmlAbstractUrlInterceptor *>();
}

//  void QList<QQmlAbstractUrlInterceptor *>::append(const
//      QQmlAbstractUrlInterceptor * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQmlAbstractUrlInterceptor_ptr(
    QList<QQmlAbstractUrlInterceptor *> *self,
    QQmlAbstractUrlInterceptor *element) {
  self->append(element);
}

//  qsizetype QList<QQmlAbstractUrlInterceptor *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQmlAbstractUrlInterceptor_ptr(
    const QList<QQmlAbstractUrlInterceptor *> *self) {
  return self->size();
}

//  const QQmlAbstractUrlInterceptor * &QList<QQmlAbstractUrlInterceptor
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQmlAbstractUrlInterceptor *ritual_list_at_QQmlAbstractUrlInterceptor_ptr(
    const QList<QQmlAbstractUrlInterceptor *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQmlAbstractUrlInterceptor *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQmlAbstractUrlInterceptor_ptr(
    QList<QQmlAbstractUrlInterceptor *> *self) {
  delete self;
}

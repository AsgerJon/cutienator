//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  A QRhiAdapter that Python can take functions over in. Every QRhiAdapter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRhiDriverInfo * (*CuteQRhiAdapterCall0)(const void *, int *);
class CuteQRhiAdapter : public QRhiAdapter {
public:
  using QRhiAdapter::QRhiAdapter;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QRhiAdapter4infoEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QRhiDriverInfo QRhiAdapter::info() const
  QRhiDriverInfo info() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiAdapterCall0 call = reinterpret_cast<CuteQRhiAdapterCall0>(taken[0]);
      const QRhiDriverInfo * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QRhiAdapter::~QRhiAdapter()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRhiAdapterD1Ev(QRhiAdapter *self) {
  delete self;
}

//  QRhiDriverInfo QRhiAdapter::info() const
extern "C" Q_DECL_EXPORT
QRhiDriverInfo *ritual_ZNK11QRhiAdapter4infoEv(const QRhiAdapter *self) {
  return new QRhiDriverInfo(self->info());
}

//  a Python function taken by a CuteQRhiAdapter, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiAdapter(
    QRhiAdapter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiAdapter *>(self)->take(key, call);
}

//  QList<QRhiAdapter *>::QList()
extern "C" Q_DECL_EXPORT
QList<QRhiAdapter *> *ritual_list_make_QRhiAdapter_ptr() {
  return new QList<QRhiAdapter *>();
}

//  void QList<QRhiAdapter *>::append(const QRhiAdapter * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QRhiAdapter_ptr(
    QList<QRhiAdapter *> *self,
    QRhiAdapter *element) {
  self->append(element);
}

//  qsizetype QList<QRhiAdapter *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QRhiAdapter_ptr(
    const QList<QRhiAdapter *> *self) {
  return self->size();
}

//  const QRhiAdapter * &QList<QRhiAdapter *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QRhiAdapter *ritual_list_at_QRhiAdapter_ptr(
    const QList<QRhiAdapter *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QRhiAdapter *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QRhiAdapter_ptr(QList<QRhiAdapter *> *self) {
  delete self;
}

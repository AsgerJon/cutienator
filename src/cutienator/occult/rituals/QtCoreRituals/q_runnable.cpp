//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrunnable.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qrunnable.h>
#include <cstring>

//  A QRunnable that Python can take functions over in. Every QRunnable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQRunnableCall0)(const void *, int *);
class CuteQRunnable : public QRunnable {
public:
  using QRunnable::QRunnable;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QRunnable3runEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QRunnable::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      CuteQRunnableCall0 call = reinterpret_cast<CuteQRunnableCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  void QRunnable::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRunnable3runEv(QRunnable *self) {
  self->run();
}

//  QRunnable::~QRunnable()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRunnableD1Ev(QRunnable *self) {
  delete self;
}

//  bool QRunnable::autoDelete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QRunnable10autoDeleteEv(const QRunnable *self) {
  return self->autoDelete();
}

//  void QRunnable::setAutoDelete(bool autoDelete)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRunnable13setAutoDeleteEb(QRunnable *self, bool autoDelete) {
  self->setAutoDelete(autoDelete);
}

//  QRunnable *QRunnable::warnNullCallable()
extern "C" Q_DECL_EXPORT
QRunnable *ritual_ZN9QRunnable16warnNullCallableEv() {
  return QRunnable::warnNullCallable();
}

//  a Python function taken by a CuteQRunnable, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRunnable(QRunnable *self, const char *key, void *call) {
  return static_cast<CuteQRunnable *>(self)->take(key, call);
}

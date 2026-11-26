//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QHostInfoRunnable that Python can take functions over in. Every QHostInfoRunnable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQHostInfoRunnableCall0)(const void *, int *);
class CuteQHostInfoRunnable : public QHostInfoRunnable {
public:
  using QHostInfoRunnable::QHostInfoRunnable;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QRunnable3runEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QHostInfoRunnable::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      CuteQHostInfoRunnableCall0 call = reinterpret_cast<CuteQHostInfoRunnableCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QHostInfoRunnable::run();
  }
};

//  QHostInfoRunnable::~QHostInfoRunnable()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHostInfoRunnableD1Ev(QHostInfoRunnable *self) {
  delete self;
}

//  void QHostInfoRunnable::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHostInfoRunnable3runEv(QHostInfoRunnable *self) {
  self->run();
}

//  a Python function taken by a CuteQHostInfoRunnable, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHostInfoRunnable(
    QHostInfoRunnable *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHostInfoRunnable *>(self)->take(key, call);
}

//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlincubator.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlincubator.h>
#include <cstring>

//  Only a class built on QQmlIncubationController may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlIncubationController : QQmlIncubationController {
  using QQmlIncubationController::incubatingObjectCountChanged;
};

//  A QQmlIncubationController that Python can take functions over in. Every QQmlIncubationController
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlIncubationControllerCall0)(const void *, int, int *);
class CuteQQmlIncubationController : public QQmlIncubationController {
public:
  using QQmlIncubationController::QQmlIncubationController;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QQmlIncubationController28incubatingObjectCountChangedEi")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQmlIncubationController::incubatingObjectCountChanged(int a0)
  void incubatingObjectCountChanged(int a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlIncubationControllerCall0 call = reinterpret_cast<CuteQQmlIncubationControllerCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlIncubationController::incubatingObjectCountChanged(a0);
  }
};

//  QQmlIncubationController::QQmlIncubationController()
extern "C" Q_DECL_EXPORT
QQmlIncubationController *ritual_ZN24QQmlIncubationControllerC1Ev() {
  return new CuteQQmlIncubationController();
}

//  QQmlIncubationController::~QQmlIncubationController()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlIncubationControllerD1Ev(
    QQmlIncubationController *self) {
  delete self;
}

//  QQmlEngine *QQmlIncubationController::engine() const
extern "C" Q_DECL_EXPORT
QQmlEngine *ritual_ZNK24QQmlIncubationController6engineEv(
    const QQmlIncubationController *self) {
  return self->engine();
}

//  int QQmlIncubationController::incubatingObjectCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QQmlIncubationController21incubatingObjectCountEv(
    const QQmlIncubationController *self) {
  return self->incubatingObjectCount();
}

//  void QQmlIncubationController::incubateFor(int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlIncubationController11incubateForEi(
    QQmlIncubationController *self,
    int msecs) {
  self->incubateFor(msecs);
}

//  void QQmlIncubationController::incubateWhile(std::atomic<bool> *flag, int
//      msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlIncubationController13incubateWhileEPSt6atomicIbEi(
    QQmlIncubationController *self,
    std::atomic<bool> *flag,
    int msecs) {
  self->incubateWhile(flag, msecs);
}

//  void QQmlIncubationController::incubatingObjectCountChanged(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlIncubationController28incubatingObjectCountChangedEi(
    QQmlIncubationController *self,
    int a0) {
  self->incubatingObjectCountChanged(a0);
}

//  a Python function taken by a CuteQQmlIncubationController, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlIncubationController(
    QQmlIncubationController *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlIncubationController *>(self)->take(key, call);
}

//  void QQmlIncubationController::incubatingObjectCountChanged(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQmlIncubationController28incubatingObjectCountChangedEi(
    QQmlIncubationController *self,
    int a0) {
  static_cast<OwnQQmlIncubationController *>(self)->OwnQQmlIncubationController::incubatingObjectCountChanged(
      a0);
}

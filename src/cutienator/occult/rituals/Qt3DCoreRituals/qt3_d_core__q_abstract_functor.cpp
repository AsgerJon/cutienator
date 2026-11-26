//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qabstractfunctor.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qabstractfunctor.h>
#include <cstring>

//  A Qt3DCore::QAbstractFunctor that Python can take functions over in. Every Qt3DCore::QAbstractFunctor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qintptr (*CuteQt3DCore_QAbstractFunctorCall0)(const void *, int *);
class CuteQt3DCore_QAbstractFunctor : public Qt3DCore::QAbstractFunctor {
public:
  using Qt3DCore::QAbstractFunctor::QAbstractFunctor;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8Qt3DCore16QAbstractFunctor2idEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  qintptr Qt3DCore::QAbstractFunctor::id() const
  qintptr id() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QAbstractFunctorCall0 call = reinterpret_cast<CuteQt3DCore_QAbstractFunctorCall0>(taken[0]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  Qt3DCore::QAbstractFunctor::QAbstractFunctor()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractFunctor *ritual_ZN8Qt3DCore16QAbstractFunctorC1Ev() {
  return new CuteQt3DCore_QAbstractFunctor();
}

//  Qt3DCore::QAbstractFunctor::~QAbstractFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16QAbstractFunctorD1Ev(
    Qt3DCore::QAbstractFunctor *self) {
  delete self;
}

//  qintptr Qt3DCore::QAbstractFunctor::id() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK8Qt3DCore16QAbstractFunctor2idEv(
    const Qt3DCore::QAbstractFunctor *self) {
  return self->id();
}

//  a Python function taken by a CuteQt3DCore_QAbstractFunctor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAbstractFunctor(
    Qt3DCore::QAbstractFunctor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAbstractFunctor *>(self)->take(key, call);
}

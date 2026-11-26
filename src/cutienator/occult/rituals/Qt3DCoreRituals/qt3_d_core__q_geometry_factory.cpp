//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qgeometryfactory_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qgeometryfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::QGeometryFactory that Python can take functions over in. Every Qt3DCore::QGeometryFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qintptr (*CuteQt3DCore_QGeometryFactoryCall0)(const void *, int *);
class CuteQt3DCore_QGeometryFactory : public Qt3DCore::QGeometryFactory {
public:
  using Qt3DCore::QGeometryFactory::QGeometryFactory;
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
      CuteQt3DCore_QGeometryFactoryCall0 call = reinterpret_cast<CuteQt3DCore_QGeometryFactoryCall0>(taken[0]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  Qt3DCore::QGeometryFactory::~QGeometryFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16QGeometryFactoryD1Ev(
    Qt3DCore::QGeometryFactory *self) {
  delete self;
}

//  QGeometry *Qt3DCore::QGeometryFactory::operator()()
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometry *ritual_ZN8Qt3DCore16QGeometryFactoryclEv(
    Qt3DCore::QGeometryFactory *self) {
  return self->operator()();
}

//  bool Qt3DCore::QGeometryFactory::equals(const QGeometryFactory &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore16QGeometryFactory6equalsERKS0_(
    const Qt3DCore::QGeometryFactory *self,
    const Qt3DCore::QGeometryFactory *other) {
  return self->equals(*other);
}

//  bool operator==(const QGeometryFactory &lhs, const QGeometryFactory &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8Qt3DCoreeqERKNS_16QGeometryFactoryES2_(
    const Qt3DCore::QGeometryFactory *lhs,
    const Qt3DCore::QGeometryFactory *rhs) {
  return operator==(*lhs, *rhs);
}

//  a Python function taken by a CuteQt3DCore_QGeometryFactory, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QGeometryFactory(
    Qt3DCore::QGeometryFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QGeometryFactory *>(self)->take(key, call);
}

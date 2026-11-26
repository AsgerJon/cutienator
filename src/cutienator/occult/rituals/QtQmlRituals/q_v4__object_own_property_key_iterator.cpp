//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4object_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4object_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QV4::ObjectOwnPropertyKeyIterator that Python can take functions over in. Every QV4::ObjectOwnPropertyKeyIterator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QV4::PropertyKey * (*CuteQV4_ObjectOwnPropertyKeyIteratorCall0)(const void *, const QV4::Object *, QV4::Property *, QV4::PropertyAttributes *, int *);
class CuteQV4_ObjectOwnPropertyKeyIterator : public QV4::ObjectOwnPropertyKeyIterator {
public:
  using QV4::ObjectOwnPropertyKeyIterator::ObjectOwnPropertyKeyIterator;
  CuteQV4_ObjectOwnPropertyKeyIterator(const QV4::ObjectOwnPropertyKeyIterator & other) : QV4::ObjectOwnPropertyKeyIterator(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN3QV422OwnPropertyKeyIterator4nextEPKNS_6ObjectEPNS_8PropertyEPNS_18PropertyAttributesE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  PropertyKey QV4::ObjectOwnPropertyKeyIterator::next(const Object *o,
  //      Property *pd, PropertyAttributes *attrs)
  QV4::PropertyKey next(
      const QV4::Object *o,
      QV4::Property *pd,
      QV4::PropertyAttributes *attrs) override {
    if (taken[0]) {
      int handled = 0;
      CuteQV4_ObjectOwnPropertyKeyIteratorCall0 call = reinterpret_cast<CuteQV4_ObjectOwnPropertyKeyIteratorCall0>(taken[0]);
      const QV4::PropertyKey * given = call(this, o, pd, attrs, &handled);
      if (handled && given) return *given;
    }
    return QV4::ObjectOwnPropertyKeyIterator::next(o, pd, attrs);
  }
};

//  QV4::ObjectOwnPropertyKeyIterator::~ObjectOwnPropertyKeyIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV428ObjectOwnPropertyKeyIteratorD1Ev(
    QV4::ObjectOwnPropertyKeyIterator *self) {
  delete self;
}

//  PropertyKey QV4::ObjectOwnPropertyKeyIterator::next(const Object *o,
//      Property *pd, PropertyAttributes *attrs)
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZN3QV428ObjectOwnPropertyKeyIterator4nextEPKNS_6ObjectEPNS_8PropertyEPNS_18PropertyAttributesE(
    QV4::ObjectOwnPropertyKeyIterator *self,
    const QV4::Object *o,
    QV4::Property *pd,
    QV4::PropertyAttributes *attrs) {
  return new QV4::PropertyKey(self->next(o, pd, attrs));
}

//  a Python function taken by a CuteQV4_ObjectOwnPropertyKeyIterator, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QV4_ObjectOwnPropertyKeyIterator(
    QV4::ObjectOwnPropertyKeyIterator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQV4_ObjectOwnPropertyKeyIterator *>(self)->take(key, call);
}

//  PropertyKey QV4::ObjectOwnPropertyKeyIterator::next(const Object *o,
//      Property *pd, PropertyAttributes *attrs)
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_own_ZN3QV428ObjectOwnPropertyKeyIterator4nextEPKNS_6ObjectEPNS_8PropertyEPNS_18PropertyAttributesE(
    QV4::ObjectOwnPropertyKeyIterator *self,
    const QV4::Object *o,
    QV4::Property *pd,
    QV4::PropertyAttributes *attrs) {
  return new QV4::PropertyKey(
      self->QV4::ObjectOwnPropertyKeyIterator::next(
          o,
          pd,
          attrs));
}

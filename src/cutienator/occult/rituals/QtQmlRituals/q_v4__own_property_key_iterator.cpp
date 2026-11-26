//  Written by hand on 2026-11-25 from
//  QtQml/6.12.0/QtQml/private/qv4vtable_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt's header does not stand alone: 'ReturnedValue' is declared by
//  qv4staticvalue_p.h, which qv4object_p.h brings in before it (the
//  compiler refused the generated file for it). 'next' takes its two
//  last arguments from Qt's own defaults, left out of the ritual: the
//  Cute class stacks them as overloads. 'next' is pure virtual, so it
//  has no 'own_' ritual.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#include <QtQml/6.12.0/QtQml/private/qv4object_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4vtable_p.h>
#include <cstring>

//  A QV4::OwnPropertyKeyIterator that Python can take functions over in.
//  Every QV4::OwnPropertyKeyIterator Python makes is one. Each function
//  below asks the Python function handed over for it, and runs Qt's own
//  without one.
typedef const QV4::PropertyKey * (*CuteQV4_OwnPropertyKeyIteratorCall0)(const void *, const QV4::Object *, QV4::Property *, QV4::PropertyAttributes *, int *);
class CuteQV4_OwnPropertyKeyIterator : public QV4::OwnPropertyKeyIterator {
public:
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN3QV422OwnPropertyKeyIterator4nextEPKNS_6ObjectEPNS_8PropertyEPNS_18PropertyAttributesE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  PropertyKey QV4::OwnPropertyKeyIterator::next(const Object *o,
  //      Property *p, PropertyAttributes *attrs)
  QV4::PropertyKey next(
      const QV4::Object *o,
      QV4::Property *p,
      QV4::PropertyAttributes *attrs) override {
    if (taken[0]) {
      int handled = 0;
      CuteQV4_OwnPropertyKeyIteratorCall0 call = reinterpret_cast<CuteQV4_OwnPropertyKeyIteratorCall0>(taken[0]);
      const QV4::PropertyKey * given = call(this, o, p, attrs, &handled);
      if (handled && given) return *given;
    }
    return QV4::PropertyKey::invalid();
  }
};

//  QV4::OwnPropertyKeyIterator::~OwnPropertyKeyIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV422OwnPropertyKeyIteratorD1Ev(
    QV4::OwnPropertyKeyIterator *self) {
  delete self;
}

//  PropertyKey QV4::OwnPropertyKeyIterator::next(const Object *o, Property
//      *p, PropertyAttributes *attrs)
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZN3QV422OwnPropertyKeyIterator4nextEPKNS_6ObjectEPNS_8PropertyEPNS_18PropertyAttributesE(
    QV4::OwnPropertyKeyIterator *self,
    const QV4::Object *o,
    QV4::Property *p,
    QV4::PropertyAttributes *attrs) {
  return new QV4::PropertyKey(self->next(o, p, attrs));
}

//  a Python function taken by a CuteQV4_OwnPropertyKeyIterator, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QV4_OwnPropertyKeyIterator(
    QV4::OwnPropertyKeyIterator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQV4_OwnPropertyKeyIterator *>(self)->take(key, call);
}

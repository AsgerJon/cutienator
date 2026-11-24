//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qresultstore.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(future)
#include <QtCore/qresultstore.h>

//  bool operator==(const ResultIteratorBase &lhs, const ResultIteratorBase
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateeqERKNS_18ResultIteratorBaseES2_(
    const QtPrivate::ResultIteratorBase *lhs,
    const QtPrivate::ResultIteratorBase *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const ResultIteratorBase &lhs, const ResultIteratorBase
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivateneERKNS_18ResultIteratorBaseES2_(
    const QtPrivate::ResultIteratorBase *lhs,
    const QtPrivate::ResultIteratorBase *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QtPrivate::ResultIteratorBase::~ResultIteratorBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate18ResultIteratorBaseD1Ev(
    QtPrivate::ResultIteratorBase *self) {
  delete self;
}

#endif  // QT_CONFIG(future)

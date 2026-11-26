//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsharedpointer_impl.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  added by hand, instances of templates of the class: 1. Kept as it is when
//  the generator runs again.
#include <QtCore/qglobal.h>
#if !defined(Q_QDOC)
#include <QtCore/qsharedpointer.h>
#include <QtCore/qobject.h>

//  QtPrivate::EnableInternalData::~EnableInternalData()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate18EnableInternalDataD1Ev(
    QtPrivate::EnableInternalData *self) {
  delete self;
}

//  static QObject
//      *QtPrivate::EnableInternalData::internalData<QObject>(const
//      QWeakPointer<QObject> &p)
extern "C" Q_DECL_EXPORT
QObject * ritual_ZN9QtPrivate18EnableInternalData12internalDataI7QObjectEEPT_RK12QWeakPointerIS3_E(
    const QWeakPointer<QObject> *p) {
  return QtPrivate::EnableInternalData::internalData<QObject>(*p);
}

#endif  // !defined(Q_QDOC)

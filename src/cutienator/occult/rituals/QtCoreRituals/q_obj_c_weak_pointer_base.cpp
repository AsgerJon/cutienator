//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qcore_mac_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  An 'NSObject *', which plain C++ sees as a class of that name, is
//  passed as an address. Not written: 'operator='.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtCore/6.12.0/QtCore/private/qcore_mac_p.h>

//  QObjCWeakPointerBase::QObjCWeakPointerBase(NSObject *object)
extern "C" Q_DECL_EXPORT
QObjCWeakPointerBase *ritual_ZN20QObjCWeakPointerBaseC1EP8NSObject(
    NSObject *object) {
  return new QObjCWeakPointerBase(object);
}

//  QObjCWeakPointerBase::QObjCWeakPointerBase(const QObjCWeakPointerBase
//      &other)
extern "C" Q_DECL_EXPORT
QObjCWeakPointerBase *ritual_ZN20QObjCWeakPointerBaseC1ERKS_(
    const QObjCWeakPointerBase *other) {
  return new QObjCWeakPointerBase(*other);
}

//  QObjCWeakPointerBase::~QObjCWeakPointerBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QObjCWeakPointerBaseD1Ev(QObjCWeakPointerBase *self) {
  delete self;
}

//  NSObject *QObjCWeakPointerBase::get() const
extern "C" Q_DECL_EXPORT
NSObject *ritual_ZNK20QObjCWeakPointerBase3getEv(
    const QObjCWeakPointerBase *self) {
  return self->get();
}

#endif  // defined(Q_OS_DARWIN)

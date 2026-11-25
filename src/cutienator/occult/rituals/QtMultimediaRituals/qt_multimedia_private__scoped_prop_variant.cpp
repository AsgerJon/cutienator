//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qwindows_scopedpropvariant_p.h,
//  Qt 6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
//  A 'PROPVARIANT *' is passed as an address, and so is the 'PROPVARIANT &'
//  'operator*' gives. Not written: the destructor, which calls
//  'PropVariantClear' of Windows, a library outside Qt.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwindows_scopedpropvariant_p.h>

//  QtMultimediaPrivate::ScopedPropVariant::ScopedPropVariant()
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::ScopedPropVariant *ritual_ZN19QtMultimediaPrivate17ScopedPropVariantC1Ev() {
  return new QtMultimediaPrivate::ScopedPropVariant();
}

//  PROPVARIANT *QtMultimediaPrivate::ScopedPropVariant::get()
extern "C" Q_DECL_EXPORT
PROPVARIANT *ritual_ZN19QtMultimediaPrivate17ScopedPropVariant3getEv(
    QtMultimediaPrivate::ScopedPropVariant *self) {
  return self->get();
}

//  PROPVARIANT *QtMultimediaPrivate::ScopedPropVariant::operator->()
extern "C" Q_DECL_EXPORT
PROPVARIANT *ritual_ZN19QtMultimediaPrivate17ScopedPropVariantptEv(
    QtMultimediaPrivate::ScopedPropVariant *self) {
  return self->operator->();
}

//  PROPVARIANT &QtMultimediaPrivate::ScopedPropVariant::operator*()
extern "C" Q_DECL_EXPORT
PROPVARIANT *ritual_ZN19QtMultimediaPrivate17ScopedPropVariantdeEv(
    QtMultimediaPrivate::ScopedPropVariant *self) {
  return &self->operator*();
}

#endif  // defined(Q_OS_WIN)

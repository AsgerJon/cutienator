//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qwindows_propertystore_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
//  Qt's library offers nothing of this class by name: only its destructor,
//  which its header leaves to the compiler, is called. Not written: the
//  constructor, 'open', 'getString', 'getUInt32' and 'getGUID', which Qt's
//  library offers not.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwindows_propertystore_p.h>
#include <propsys.h>

//  QtMultimediaPrivate::PropertyStoreHelper::~PropertyStoreHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate19PropertyStoreHelperD1Ev(
    QtMultimediaPrivate::PropertyStoreHelper *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN)

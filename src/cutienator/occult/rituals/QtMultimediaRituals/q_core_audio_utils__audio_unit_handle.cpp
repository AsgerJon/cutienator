//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qcoreaudioutils_p.h, Qt 6.12.0,
//  as the Qt of macOS installs it. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only what its header
//  writes out is called. Not written: the destructor, 'initialize' and
//  'deinitialize', which Qt's library offers not; the constructors it takes
//  from the template QUniqueHandle, with no destructor to undo them; and
//  'operator='.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcoreaudioutils_p.h>

//  bool QCoreAudioUtils::AudioUnitHandle::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCoreAudioUtils15AudioUnitHandle13isInitializedEv(
    const QCoreAudioUtils::AudioUnitHandle *self) {
  return self->isInitialized();
}

#endif  // defined(Q_OS_DARWIN)

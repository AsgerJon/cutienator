//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qmemory_resource_tlsf_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qmemory_resource_tlsf_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtMultimediaPrivate::QTlsfMemoryResource::QTlsfMemoryResource(std::size_t
//      preallocatedBytes, pmr::memory_resource *upstream)
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::QTlsfMemoryResource *ritual_ZN19QtMultimediaPrivate19QTlsfMemoryResourceC1EmPNSt3pmr15memory_resourceE(
    std::size_t preallocatedBytes,
    QtMultimediaPrivate::pmr::memory_resource *upstream) {
  return new QtMultimediaPrivate::QTlsfMemoryResource(
      preallocatedBytes,
      upstream);
}

//  QtMultimediaPrivate::QTlsfMemoryResource::~QTlsfMemoryResource()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate19QTlsfMemoryResourceD1Ev(
    QtMultimediaPrivate::QTlsfMemoryResource *self) {
  delete self;
}

//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qwmf_support_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its virtual
//  functions, those of IMFMediaBuffer of Windows, are called, through the
//  object. It is final, so 'self' is taken as an IMFMediaBuffer, and the
//  calls stay virtual. A 'BYTE **' and a 'DWORD *' are passed as addresses,
//  a 'DWORD' as an 'unsigned long', and the 'HRESULT' given back as a
//  'long'. Not written: the constructors, the destructor and
//  'CreateInstance' and 'takeByteArray', which Qt's library offers not, and
//  the templates 'withLockedBuffer' of the same header.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwmf_support_p.h>

//  HRESULT QWMF::QByteArrayMFMediaBuffer::Lock(BYTE **ppbBuffer, DWORD
//      *pcbMaxLength, DWORD *pcbCurrentLength)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN4QWMF23QByteArrayMFMediaBuffer4LockEPPhPmS3_(
    IMFMediaBuffer *self,
    BYTE **ppbBuffer,
    DWORD *pcbMaxLength,
    DWORD *pcbCurrentLength) {
  return self->Lock(
      ppbBuffer, pcbMaxLength, pcbCurrentLength);
}

//  HRESULT QWMF::QByteArrayMFMediaBuffer::Unlock()
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN4QWMF23QByteArrayMFMediaBuffer6UnlockEv(
    IMFMediaBuffer *self) {
  return self->Unlock();
}

//  HRESULT QWMF::QByteArrayMFMediaBuffer::GetCurrentLength(DWORD
//      *pcbCurrentLength)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN4QWMF23QByteArrayMFMediaBuffer16GetCurrentLengthEPm(
    IMFMediaBuffer *self,
    DWORD *pcbCurrentLength) {
  return self->GetCurrentLength(pcbCurrentLength);
}

//  HRESULT QWMF::QByteArrayMFMediaBuffer::SetCurrentLength(DWORD
//      cbCurrentLength)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN4QWMF23QByteArrayMFMediaBuffer16SetCurrentLengthEm(
    IMFMediaBuffer *self,
    DWORD cbCurrentLength) {
  return self->SetCurrentLength(cbCurrentLength);
}

//  HRESULT QWMF::QByteArrayMFMediaBuffer::GetMaxLength(DWORD *pcbMaxLength)
extern "C" Q_DECL_EXPORT
HRESULT ritual_ZN4QWMF23QByteArrayMFMediaBuffer12GetMaxLengthEPm(
    IMFMediaBuffer *self,
    DWORD *pcbMaxLength) {
  return self->GetMaxLength(pcbMaxLength);
}

#endif  // defined(Q_OS_WIN)

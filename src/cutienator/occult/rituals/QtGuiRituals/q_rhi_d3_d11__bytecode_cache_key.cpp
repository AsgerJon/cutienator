//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qrhid3d11_p.h, Qt 6.12.0, as the Qt of
//  Windows installs it. Kept as it is when the generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out. Direct3D's interfaces are passed as
//  addresses.
//  Not written: 'qHash'.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qrhid3d11_p.h>

//  QRhiD3D11::BytecodeCacheKey::~BytecodeCacheKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QRhiD3D1116BytecodeCacheKeyD1Ev(
    QRhiD3D11::BytecodeCacheKey *self) {
  delete self;
}

//  bool operator==(const QRhiD3D11::BytecodeCacheKey &a, const
//      QRhiD3D11::BytecodeCacheKey &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN9QRhiD3D1116BytecodeCacheKeyES2_(
    const QRhiD3D11::BytecodeCacheKey *a,
    const QRhiD3D11::BytecodeCacheKey *b) {
  return *a == *b;
}

//  bool operator!=(const QRhiD3D11::BytecodeCacheKey &a, const
//      QRhiD3D11::BytecodeCacheKey &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN9QRhiD3D1116BytecodeCacheKeyES2_(
    const QRhiD3D11::BytecodeCacheKey *a,
    const QRhiD3D11::BytecodeCacheKey *b) {
  return *a != *b;
}

#endif  // defined(Q_OS_WIN)

//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhinull_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qrhinull_p.h>
#include <QtCore/qmath.h>
#include <QtGui/QPainter>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/rhi/qrhinull.cpp, line 666, as _ZN17QNullRenderBufferC1EP18QRhiImplementationN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS2_4FlagEEN11QRhiTexture6FormatE
inline QNullRenderBuffer::QNullRenderBuffer(QRhiImplementation *rhi, Type type, const QSize &pixelSize,
                                     int sampleCount, QRhiRenderBuffer::Flags flags,
                                     QRhiTexture::Format backingFormatHint)
    : QRhiRenderBuffer(rhi, type, pixelSize, sampleCount, flags, backingFormatHint)
{
}

//  from src/gui/rhi/qrhinull.cpp, line 673, as _ZN17QNullRenderBufferD1Ev
inline QNullRenderBuffer::~QNullRenderBuffer()
{
    destroy();
}

//  from src/gui/rhi/qrhinull.cpp, line 678, as _ZN17QNullRenderBuffer7destroyEv
inline void QNullRenderBuffer::destroy()
{
    valid = false;

    QRHI_RES_RHI(QRhiNull);
    if (rhiD)
        rhiD->unregisterResource(this);
}

//  from src/gui/rhi/qrhinull.cpp, line 687, as _ZN17QNullRenderBuffer6createEv
inline bool QNullRenderBuffer::create()
{
    if (valid)
        destroy();

    valid = true;
    generation += 1;

    QRHI_RES_RHI(QRhiNull);
    rhiD->registerResource(this);

    return true;
}

//  from src/gui/rhi/qrhinull.cpp, line 701, as _ZNK17QNullRenderBuffer13backingFormatEv
inline QRhiTexture::Format QNullRenderBuffer::backingFormat() const
{
    return m_type == Color ? QRhiTexture::RGBA8 : QRhiTexture::UnknownFormat;
}
//  -----------------------------------------------------------------------

//  A QNullRenderBuffer that Python can take functions over in. Every QNullRenderBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQNullRenderBufferCall0)(const void *, int *);
typedef bool (*CuteQNullRenderBufferCall1)(const void *, int *);
typedef int (*CuteQNullRenderBufferCall2)(const void *, int *);
typedef int (*CuteQNullRenderBufferCall3)(const void *, int *);
typedef bool (*CuteQNullRenderBufferCall4)(const void *, const QRhiRenderBuffer::NativeRenderBuffer *, int *);
class CuteQNullRenderBuffer : public QNullRenderBuffer {
public:
  using QNullRenderBuffer::QNullRenderBuffer;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QRhiResource7destroyEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QRhiRenderBuffer6createEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QRhiRenderBuffer13backingFormatEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QRhiResource12resourceTypeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QRhiRenderBuffer10createFromENS_18NativeRenderBufferE")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  void QNullRenderBuffer::destroy()
  void destroy() override {
    if (taken[0]) {
      int handled = 0;
      CuteQNullRenderBufferCall0 call = reinterpret_cast<CuteQNullRenderBufferCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QNullRenderBuffer::destroy();
  }

  //  bool QNullRenderBuffer::create()
  bool create() override {
    if (taken[1]) {
      int handled = 0;
      CuteQNullRenderBufferCall1 call = reinterpret_cast<CuteQNullRenderBufferCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNullRenderBuffer::create();
  }

  //  QRhiTexture::Format QNullRenderBuffer::backingFormat() const
  QRhiTexture::Format backingFormat() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNullRenderBufferCall2 call = reinterpret_cast<CuteQNullRenderBufferCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiTexture::Format>(given);
    }
    return QNullRenderBuffer::backingFormat();
  }

  //  QRhiResource::Type QRhiRenderBuffer::resourceType() const
  QRhiResource::Type resourceType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNullRenderBufferCall3 call = reinterpret_cast<CuteQNullRenderBufferCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QRhiResource::Type>(given);
    }
    return QRhiRenderBuffer::resourceType();
  }

  //  bool QRhiRenderBuffer::createFrom(NativeRenderBuffer src)
  bool createFrom(QRhiRenderBuffer::NativeRenderBuffer src) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNullRenderBufferCall4 call = reinterpret_cast<CuteQNullRenderBufferCall4>(taken[4]);
      bool given = call(this, &src, &handled);
      if (handled) return given;
    }
    return QRhiRenderBuffer::createFrom(src);
  }
};

//  QNullRenderBuffer::QNullRenderBuffer(QRhiImplementation *rhi, Type type,
//      const QSize &pixelSize, int sampleCount, QRhiRenderBuffer::Flags
//      flags, QRhiTexture::Format backingFormatHint)
extern "C" Q_DECL_EXPORT
QNullRenderBuffer *ritual_ZN17QNullRenderBufferC1EP18QRhiImplementationN16QRhiRenderBuffer4TypeERK5QSizei6QFlagsINS2_4FlagEEN11QRhiTexture6FormatE(
    QRhiImplementation *rhi,
    QRhiRenderBuffer::Type type,
    const QSize *pixelSize,
    int sampleCount,
    int flags,
    QRhiTexture::Format backingFormatHint) {
  return new CuteQNullRenderBuffer(
      rhi,
      type,
      *pixelSize,
      sampleCount,
      QFlags<QRhiRenderBuffer::Flag>::fromInt(flags),
      backingFormatHint);
}

//  QNullRenderBuffer::~QNullRenderBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNullRenderBufferD1Ev(QNullRenderBuffer *self) {
  delete self;
}

//  void QNullRenderBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNullRenderBuffer7destroyEv(QNullRenderBuffer *self) {
  self->destroy();
}

//  bool QNullRenderBuffer::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QNullRenderBuffer6createEv(QNullRenderBuffer *self) {
  return self->create();
}

//  QRhiTexture::Format QNullRenderBuffer::backingFormat() const
extern "C" Q_DECL_EXPORT
QRhiTexture::Format ritual_ZNK17QNullRenderBuffer13backingFormatEv(
    const QNullRenderBuffer *self) {
  return self->backingFormat();
}

//  a Python function taken by a CuteQNullRenderBuffer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNullRenderBuffer(
    QNullRenderBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNullRenderBuffer *>(self)->take(key, call);
}

//  void QNullRenderBuffer::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QNullRenderBuffer7destroyEv(QNullRenderBuffer *self) {
  self->QNullRenderBuffer::destroy();
}

//  bool QNullRenderBuffer::create()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QNullRenderBuffer6createEv(QNullRenderBuffer *self) {
  return self->QNullRenderBuffer::create();
}

//  QRhiTexture::Format QNullRenderBuffer::backingFormat() const
extern "C" Q_DECL_EXPORT
QRhiTexture::Format ritual_own_ZNK17QNullRenderBuffer13backingFormatEv(
    const QNullRenderBuffer *self) {
  return self->QNullRenderBuffer::backingFormat();
}

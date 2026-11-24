//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qalsaaudiosource_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(alsa)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qalsaaudiosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qcoreapplication.h>
#include <QtCore/qvarlengtharray.h>
#include <QtMultimedia/private/qaudiohelpers_p.h>
#include <QtMultimedia/private/qalsaaudiosource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 642, as _ZN10RingBufferC1Ev
inline RingBuffer::RingBuffer() :
        m_head(0),
        m_tail(0)
{
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 648, as _ZN10RingBuffer6resizeEi
inline void RingBuffer::resize(int size)
{
    m_data.resize(size);
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 653, as _ZNK10RingBuffer19bytesOfDataInBufferEv
inline int RingBuffer::bytesOfDataInBuffer() const
{
    if (m_head < m_tail)
        return m_tail - m_head;
    else if (m_tail < m_head)
        return m_data.size() + m_tail - m_head;
    else
        return 0;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 663, as _ZNK10RingBuffer9freeBytesEv
inline int RingBuffer::freeBytes() const
{
    if (m_head > m_tail)
        return m_head - m_tail - 1;
    else if (m_tail > m_head)
        return m_data.size() - m_tail + m_head - 1;
    else
        return m_data.size() - 1;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 673, as _ZNK10RingBuffer13availableDataEv
inline const char *RingBuffer::availableData() const
{
    return (m_data.constData() + m_head);
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 678, as _ZNK10RingBuffer22availableDataBlockSizeEv
inline int RingBuffer::availableDataBlockSize() const
{
    if (m_head > m_tail)
        return m_data.size() - m_head;
    else if (m_tail > m_head)
        return m_tail - m_head;
    else
        return 0;
}

//  from ../qtmultimedia/src/multimedia/alsa/qalsaaudiosource.cpp, line 688, as _ZN10RingBuffer9readBytesEi
inline void RingBuffer::readBytes(int bytes)
{
    m_head = (m_head + bytes) % m_data.size();
}
//  -----------------------------------------------------------------------

//  RingBuffer::RingBuffer()
extern "C" Q_DECL_EXPORT
RingBuffer *ritual_ZN10RingBufferC1Ev() {
  return new RingBuffer();
}

//  void RingBuffer::resize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10RingBuffer6resizeEi(RingBuffer *self, int size) {
  self->resize(size);
}

//  int RingBuffer::bytesOfDataInBuffer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10RingBuffer19bytesOfDataInBufferEv(const RingBuffer *self) {
  return self->bytesOfDataInBuffer();
}

//  int RingBuffer::freeBytes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10RingBuffer9freeBytesEv(const RingBuffer *self) {
  return self->freeBytes();
}

//  const char *RingBuffer::availableData() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK10RingBuffer13availableDataEv(const RingBuffer *self) {
  return self->availableData();
}

//  int RingBuffer::availableDataBlockSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10RingBuffer22availableDataBlockSizeEv(
    const RingBuffer *self) {
  return self->availableDataBlockSize();
}

//  void RingBuffer::readBytes(int bytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN10RingBuffer9readBytesEi(RingBuffer *self, int bytes) {
  self->readBytes(bytes);
}

//  RingBuffer::~RingBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10RingBufferD1Ev(RingBuffer *self) {
  delete self;
}

#endif  // QT_CONFIG(alsa)

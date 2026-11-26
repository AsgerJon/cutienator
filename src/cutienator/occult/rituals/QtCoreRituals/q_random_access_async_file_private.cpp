//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qrandomaccessasyncfile_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(async_io)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qrandomaccessasyncfile_p.h>
#include <QtCore/6.12.0/QtCore/private/qrandomaccessasyncfile_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/QSpan>
#include <cstddef>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qrandomaccessasyncfile_p.h>
#include <QtCore/private/qrandomaccessasyncfile_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qrandomaccessasyncfile.cpp, line 16, as _ZN29QRandomAccessAsyncFilePrivateD1Ev
inline QRandomAccessAsyncFilePrivate::~QRandomAccessAsyncFilePrivate() = default;

//  from src/corelib/io/qrandomaccessasyncfile.cpp, line 15, as _ZN29QRandomAccessAsyncFilePrivateC1Ev
inline QRandomAccessAsyncFilePrivate::QRandomAccessAsyncFilePrivate() = default;
//  -----------------------------------------------------------------------

//  QRandomAccessAsyncFile *QRandomAccessAsyncFilePrivate::q_func()
extern "C" Q_DECL_EXPORT
QRandomAccessAsyncFile *ritual_ZN29QRandomAccessAsyncFilePrivate6q_funcEv(
    QRandomAccessAsyncFilePrivate *self) {
  return self->q_func();
}

//  const QRandomAccessAsyncFile *QRandomAccessAsyncFilePrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QRandomAccessAsyncFile *ritual_ZNK29QRandomAccessAsyncFilePrivate6q_funcEv(
    const QRandomAccessAsyncFilePrivate *self) {
  return self->q_func();
}

//  QRandomAccessAsyncFilePrivate::QRandomAccessAsyncFilePrivate()
extern "C" Q_DECL_EXPORT
QRandomAccessAsyncFilePrivate *ritual_ZN29QRandomAccessAsyncFilePrivateC1Ev() {
  return new QRandomAccessAsyncFilePrivate();
}

//  QRandomAccessAsyncFilePrivate::~QRandomAccessAsyncFilePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QRandomAccessAsyncFilePrivateD1Ev(
    QRandomAccessAsyncFilePrivate *self) {
  delete self;
}

//  QRandomAccessAsyncFilePrivate
//      *QRandomAccessAsyncFilePrivate::get(QRandomAccessAsyncFile *file)
extern "C" Q_DECL_EXPORT
QRandomAccessAsyncFilePrivate *ritual_ZN29QRandomAccessAsyncFilePrivate3getEP22QRandomAccessAsyncFile(
    QRandomAccessAsyncFile *file) {
  return QRandomAccessAsyncFilePrivate::get(file);
}

//  void QRandomAccessAsyncFilePrivate::cancelAndWait(QIOOperation *op)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QRandomAccessAsyncFilePrivate13cancelAndWaitEP12QIOOperation(
    QRandomAccessAsyncFilePrivate *self,
    QIOOperation *op) {
  self->cancelAndWait(op);
}

//  void QRandomAccessAsyncFilePrivate::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QRandomAccessAsyncFilePrivate5closeEv(
    QRandomAccessAsyncFilePrivate *self) {
  self->close();
}

//  qint64 QRandomAccessAsyncFilePrivate::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK29QRandomAccessAsyncFilePrivate4sizeEv(
    const QRandomAccessAsyncFilePrivate *self) {
  return self->size();
}

//  QIOOperation *QRandomAccessAsyncFilePrivate::open(const QString &path,
//      QIODeviceBase::OpenMode mode)
extern "C" Q_DECL_EXPORT
QIOOperation *ritual_ZN29QRandomAccessAsyncFilePrivate4openERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QRandomAccessAsyncFilePrivate *self,
    const QString *path,
    int mode) {
  return self->open(
      *path,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  QIOOperation *QRandomAccessAsyncFilePrivate::flush()
extern "C" Q_DECL_EXPORT
QIOOperation *ritual_ZN29QRandomAccessAsyncFilePrivate5flushEv(
    QRandomAccessAsyncFilePrivate *self) {
  return self->flush();
}

//  QIOReadOperation *QRandomAccessAsyncFilePrivate::read(qint64 offset,
//      qint64 maxSize)
extern "C" Q_DECL_EXPORT
QIOReadOperation *ritual_ZN29QRandomAccessAsyncFilePrivate4readExx(
    QRandomAccessAsyncFilePrivate *self,
    qint64 offset,
    qint64 maxSize) {
  return self->read(offset, maxSize);
}

//  QIOWriteOperation *QRandomAccessAsyncFilePrivate::write(qint64 offset,
//      const QByteArray &data)
extern "C" Q_DECL_EXPORT
QIOWriteOperation *ritual_ZN29QRandomAccessAsyncFilePrivate5writeExRK10QByteArray(
    QRandomAccessAsyncFilePrivate *self,
    qint64 offset,
    const QByteArray *data) {
  return self->write(offset, *data);
}

//  QIOWriteOperation *QRandomAccessAsyncFilePrivate::write(qint64 offset,
//      QByteArray &&data)
extern "C" Q_DECL_EXPORT
QIOWriteOperation *ritual_ZN29QRandomAccessAsyncFilePrivate5writeExO10QByteArray(
    QRandomAccessAsyncFilePrivate *self,
    qint64 offset,
    QByteArray *data) {
  return self->write(offset, std::move(*data));
}

//  QIOVectoredReadOperation *QRandomAccessAsyncFilePrivate::readInto(qint64
//      offset, QSpan<std::byte> buffer)
extern "C" Q_DECL_EXPORT
QIOVectoredReadOperation *ritual_ZN29QRandomAccessAsyncFilePrivate8readIntoEx5QSpanISt4byteLm18446744073709551615EE(
    QRandomAccessAsyncFilePrivate *self,
    qint64 offset,
    const QSpan<std::byte> *buffer) {
  return self->readInto(offset, *buffer);
}

//  QIOVectoredWriteOperation
//      *QRandomAccessAsyncFilePrivate::writeFrom(qint64 offset, QSpan<const
//      std::byte> buffer)
extern "C" Q_DECL_EXPORT
QIOVectoredWriteOperation *ritual_ZN29QRandomAccessAsyncFilePrivate9writeFromEx5QSpanIKSt4byteLm18446744073709551615EE(
    QRandomAccessAsyncFilePrivate *self,
    qint64 offset,
    const QSpan<const std::byte> *buffer) {
  return self->writeFrom(offset, *buffer);
}

//  QIOVectoredReadOperation *QRandomAccessAsyncFilePrivate::readInto(qint64
//      offset, QSpan<const QSpan<std::byte>> buffers)
extern "C" Q_DECL_EXPORT
QIOVectoredReadOperation *ritual_ZN29QRandomAccessAsyncFilePrivate8readIntoEx5QSpanIKS0_ISt4byteLm18446744073709551615EELm18446744073709551615EE(
    QRandomAccessAsyncFilePrivate *self,
    qint64 offset,
    const QSpan<const QSpan<std::byte>> *buffers) {
  return self->readInto(offset, *buffers);
}

//  QIOVectoredWriteOperation
//      *QRandomAccessAsyncFilePrivate::writeFrom(qint64 offset, QSpan<const
//      QSpan<const std::byte>> buffers)
extern "C" Q_DECL_EXPORT
QIOVectoredWriteOperation *ritual_ZN29QRandomAccessAsyncFilePrivate9writeFromEx5QSpanIKS0_IKSt4byteLm18446744073709551615EELm18446744073709551615EE(
    QRandomAccessAsyncFilePrivate *self,
    qint64 offset,
    const QSpan<const QSpan<const std::byte>> *buffers) {
  return self->writeFrom(offset, *buffers);
}

//  void QRandomAccessAsyncFilePrivate::checkValid() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK29QRandomAccessAsyncFilePrivate10checkValidEv(
    const QRandomAccessAsyncFilePrivate *self) {
  self->checkValid();
}

#endif  // QT_CONFIG(async_io)

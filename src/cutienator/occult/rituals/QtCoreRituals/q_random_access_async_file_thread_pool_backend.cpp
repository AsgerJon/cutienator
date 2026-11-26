//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qrandomaccessasyncfile_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(async_io)
#if QT_CONFIG(future) && QT_CONFIG(thread)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qrandomaccessasyncfile_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>
#include <QtCore/QSpan>
#include <cstddef>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qiooperation_p.h>
#include <QtCore/private/qiooperation_p_p.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/private/qrandomaccessasyncfile_p_p.h>
#include <QtCore/private/qrandomaccessasyncfile_p_p.h>
#include <QtCore/private/qiooperation_p.h>
#include <QtCore/private/qiooperation_p_p.h>
#include <QtCore/qfuture.h>
#include <QtCore/qthread.h>
#include <QtCore/qthreadpool.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qrandomaccessasyncfile_threadpool.cpp, line 281, as local:qrandomaccessasyncfile_threadpool.cpp:executeRead
#if QT_CONFIG(thread)
#if QT_CONFIG(future)
static QRandomAccessAsyncFileThreadPoolBackend::OperationResult
executeRead(QFSFileEngine *engine, QBasicMutex *mutex, qint64 offset, char *buffer, qint64 maxSize)
{
    QRandomAccessAsyncFileThreadPoolBackend::OperationResult result{0, QIOOperation::Error::None};

    QMutexLocker locker(mutex);
    if (engine) {
        if (engine->seek(offset)) {
            qint64 bytesRead = engine->read(buffer, maxSize);
            if (bytesRead >= 0)
                result.bytesProcessed = bytesRead;
            else
                result.error = QIOOperation::Error::Read;
        } else {
            result.error = QIOOperation::Error::IncorrectOffset;
        }
    } else {
        result.error = QIOOperation::Error::FileNotOpen;
    }
    return result;
}
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(thread)

//  from src/corelib/io/qiooperation.cpp, line 28, as _ZN19QIOOperationPrivate17operationCompleteEN12QIOOperation5ErrorE
inline void QIOOperationPrivate::operationComplete(QIOOperation::Error err)
{
    Q_Q(QIOOperation);

    error = err;
    state = State::Finished;
    if (err != QIOOperation::Error::None)
        Q_EMIT q->errorOccurred(err);
    Q_EMIT q->finished();
}

//  from src/corelib/io/qiooperation.cpp, line 23, as _ZN19QIOOperationPrivate20appendBytesProcessedEx
inline void QIOOperationPrivate::appendBytesProcessed(qint64 num)
{
    processed += num;
}

//  from src/corelib/io/qiooperation.cpp, line 39, as _ZN19QIOOperationPrivate8setErrorEN12QIOOperation5ErrorE
inline void QIOOperationPrivate::setError(QIOOperation::Error err)
{
    Q_Q(QIOOperation);
    error = err;
    if (err != QIOOperation::Error::None) {
        state = State::Finished;
        Q_EMIT q->errorOccurred(err);
        Q_EMIT q->finished();
    }
}

//  from src/corelib/io/qrandomaccessasyncfile_threadpool.cpp, line 78, as _ZN39QRandomAccessAsyncFileThreadPoolBackend4initEv
#if QT_CONFIG(thread)
#if QT_CONFIG(future)
inline bool QRandomAccessAsyncFileThreadPoolBackend::init()
{
    QObject::connect(&m_watcher, &QFutureWatcherBase::finished, m_owner, [this]{
        operationComplete();
    });
    QObject::connect(&m_watcher, &QFutureWatcherBase::canceled, m_owner, [this]{
        operationComplete();
    });
    return true;
}
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(thread)

//  from src/corelib/io/qrandomaccessasyncfile_threadpool.cpp, line 89, as _ZN39QRandomAccessAsyncFileThreadPoolBackend13cancelAndWaitEP12QIOOperation
#if QT_CONFIG(thread)
#if QT_CONFIG(future)
inline void QRandomAccessAsyncFileThreadPoolBackend::cancelAndWait(QIOOperation *op)
{
    if (op == m_currentOperation) {
        m_currentOperation = nullptr; // to discard the result
        m_watcher.cancel(); // might have no effect
        m_watcher.waitForFinished();
    } else {
        m_operations.removeAll(op);
    }
}
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(thread)

//  from src/corelib/io/qrandomaccessasyncfile_threadpool.cpp, line 123, as _ZN39QRandomAccessAsyncFileThreadPoolBackend5closeEv
#if QT_CONFIG(thread)
#if QT_CONFIG(future)
inline void QRandomAccessAsyncFileThreadPoolBackend::close()
{
    // all the operations should be aborted
    for (const auto &op : std::as_const(m_operations)) {
        if (op) {
            auto *priv = QIOOperationPrivate::get(op.get());
            priv->setError(QIOOperation::Error::Aborted);
        }
    }
    m_operations.clear();

    // Wait until the current operation is complete
    if (m_currentOperation) {
        auto *priv = QIOOperationPrivate::get(m_currentOperation.get());
        priv->setError(QIOOperation::Error::Aborted);
        cancelAndWait(m_currentOperation.get());
    }

    {
        QMutexLocker locker(&m_engineMutex);
        if (m_engine) {
            m_engine->close();
            m_engine.reset();
        }
    }

    m_fileState = FileState::Closed;
}
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(thread)

//  from src/corelib/io/qrandomaccessasyncfile_threadpool.cpp, line 152, as _ZNK39QRandomAccessAsyncFileThreadPoolBackend4sizeEv
#if QT_CONFIG(thread)
#if QT_CONFIG(future)
inline qint64 QRandomAccessAsyncFileThreadPoolBackend::size() const
{
    QMutexLocker locker(&m_engineMutex);
    if (m_engine)
        return m_engine->size();
    return -1;
}
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(thread)

//  from src/corelib/io/qrandomaccessasyncfile_threadpool.cpp, line 100, as _ZN39QRandomAccessAsyncFileThreadPoolBackend4openERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE
#if QT_CONFIG(thread)
#if QT_CONFIG(future)
inline QIOOperation *
QRandomAccessAsyncFileThreadPoolBackend::open(const QString &path, QIODeviceBase::OpenMode mode)
{
    // We generate the command in any case. But if the file is already opened,
    // it will finish with an error
    if (m_fileState == FileState::Closed) {
        m_filePath = path;
        m_openMode = mode;
        m_fileState = FileState::OpenPending;
    }

    auto *dataStorage = new QtPrivate::QIOOperationDataStorage();

    auto *priv = new QIOOperationPrivate(dataStorage);
    priv->type = QIOOperation::Type::Open;

    auto *op = new QIOOperation(*priv, m_owner);

    m_operations.append(op);
    executeNextOperation();
    return op;
}
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(thread)

//  from src/corelib/io/qrandomaccessasyncfile_threadpool.cpp, line 160, as _ZN39QRandomAccessAsyncFileThreadPoolBackend5flushEv
#if QT_CONFIG(thread)
#if QT_CONFIG(future)
inline QIOOperation *QRandomAccessAsyncFileThreadPoolBackend::flush()
{
    auto *dataStorage = new QtPrivate::QIOOperationDataStorage();

    auto *priv = new QIOOperationPrivate(dataStorage);
    priv->type = QIOOperation::Type::Flush;

    auto *op = new QIOOperation(*priv, m_owner);
    m_operations.append(op);
    executeNextOperation();
    return op;
}
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(thread)

//  from src/corelib/io/qrandomaccessasyncfile_threadpool.cpp, line 173, as _ZN39QRandomAccessAsyncFileThreadPoolBackend4readExx
#if QT_CONFIG(thread)
#if QT_CONFIG(future)
inline QIOReadOperation *QRandomAccessAsyncFileThreadPoolBackend::read(qint64 offset, qint64 maxSize)
{
    QByteArray array;
    array.resizeForOverwrite(maxSize);
    auto *dataStorage = new QtPrivate::QIOOperationDataStorage(std::move(array));

    auto *priv = new QIOOperationPrivate(dataStorage);
    priv->offset = offset;
    priv->type = QIOOperation::Type::Read;

    auto *op = new QIOReadOperation(*priv, m_owner);
    m_operations.append(op);
    executeNextOperation();
    return op;
}
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(thread)

//  from src/corelib/io/qiooperation.cpp, line 13, as _ZN19QIOOperationPrivateC1EPN9QtPrivate23QIOOperationDataStorageE
inline QIOOperationPrivate::QIOOperationPrivate(QtPrivate::QIOOperationDataStorage *storage)
    : dataStorage(storage)
{
    Q_ASSERT(storage);
}
//  -----------------------------------------------------------------------

//  A QRandomAccessAsyncFileThreadPoolBackend that Python can take functions over in. Every QRandomAccessAsyncFileThreadPoolBackend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(future) && QT_CONFIG(thread)
typedef bool (*CuteQRandomAccessAsyncFileThreadPoolBackendCall0)(const void *, int *);
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
typedef void (*CuteQRandomAccessAsyncFileThreadPoolBackendCall1)(const void *, QIOOperation *, int *);
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
typedef void (*CuteQRandomAccessAsyncFileThreadPoolBackendCall2)(const void *, int *);
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
typedef qint64 (*CuteQRandomAccessAsyncFileThreadPoolBackendCall3)(const void *, int *);
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
typedef void * (*CuteQRandomAccessAsyncFileThreadPoolBackendCall4)(const void *, const QString *, int, int *);
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
typedef void * (*CuteQRandomAccessAsyncFileThreadPoolBackendCall5)(const void *, int *);
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
typedef void * (*CuteQRandomAccessAsyncFileThreadPoolBackendCall6)(const void *, qint64, qint64, int *);
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
typedef void * (*CuteQRandomAccessAsyncFileThreadPoolBackendCall7)(const void *, qint64, const QByteArray *, int *);
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
class CuteQRandomAccessAsyncFileThreadPoolBackend : public QRandomAccessAsyncFileThreadPoolBackend {
public:
  using QRandomAccessAsyncFileThreadPoolBackend::QRandomAccessAsyncFileThreadPoolBackend;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(future) && QT_CONFIG(thread)
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend4initEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend13cancelAndWaitEP12QIOOperation")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend5closeEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
    if (!std::strcmp(key, "_ZNK29QRandomAccessAsyncFileBackend4sizeEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend4openERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend5flushEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend4readExx")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#if QT_CONFIG(future) && QT_CONFIG(thread)
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend5writeExRK10QByteArray")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
    return false;
  }

#if QT_CONFIG(future) && QT_CONFIG(thread)
  //  bool QRandomAccessAsyncFileThreadPoolBackend::init()
  bool init() override {
    if (taken[0]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileThreadPoolBackendCall0 call = reinterpret_cast<CuteQRandomAccessAsyncFileThreadPoolBackendCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QRandomAccessAsyncFileThreadPoolBackend::init();
  }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)

#if QT_CONFIG(future) && QT_CONFIG(thread)
  //  void
  //      QRandomAccessAsyncFileThreadPoolBackend::cancelAndWait(QIOOperati
  //      on *op)
  void cancelAndWait(QIOOperation *op) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileThreadPoolBackendCall1 call = reinterpret_cast<CuteQRandomAccessAsyncFileThreadPoolBackendCall1>(taken[1]);
      call(this, op, &handled);
      if (handled) return;
    }
    QRandomAccessAsyncFileThreadPoolBackend::cancelAndWait(op);
  }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)

#if QT_CONFIG(future) && QT_CONFIG(thread)
  //  void QRandomAccessAsyncFileThreadPoolBackend::close()
  void close() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileThreadPoolBackendCall2 call = reinterpret_cast<CuteQRandomAccessAsyncFileThreadPoolBackendCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QRandomAccessAsyncFileThreadPoolBackend::close();
  }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)

#if QT_CONFIG(future) && QT_CONFIG(thread)
  //  qint64 QRandomAccessAsyncFileThreadPoolBackend::size() const
  qint64 size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileThreadPoolBackendCall3 call = reinterpret_cast<CuteQRandomAccessAsyncFileThreadPoolBackendCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QRandomAccessAsyncFileThreadPoolBackend::size();
  }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)

#if QT_CONFIG(future) && QT_CONFIG(thread)
  //  QIOOperation *QRandomAccessAsyncFileThreadPoolBackend::open(const
  //      QString &path, QIODeviceBase::OpenMode mode)
  QIOOperation *open(
      const QString &path,
      QIODeviceBase::OpenMode mode) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileThreadPoolBackendCall4 call = reinterpret_cast<CuteQRandomAccessAsyncFileThreadPoolBackendCall4>(taken[4]);
      void * given = call(this, &path, static_cast<int>(mode.toInt()), &handled);
      if (handled) return static_cast<QIOOperation *>(given);
    }
    return QRandomAccessAsyncFileThreadPoolBackend::open(path, mode);
  }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)

#if QT_CONFIG(future) && QT_CONFIG(thread)
  //  QIOOperation *QRandomAccessAsyncFileThreadPoolBackend::flush()
  QIOOperation *flush() override {
    if (taken[5]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileThreadPoolBackendCall5 call = reinterpret_cast<CuteQRandomAccessAsyncFileThreadPoolBackendCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIOOperation *>(given);
    }
    return QRandomAccessAsyncFileThreadPoolBackend::flush();
  }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)

#if QT_CONFIG(future) && QT_CONFIG(thread)
  //  QIOReadOperation
  //      *QRandomAccessAsyncFileThreadPoolBackend::read(qint64 offset,
  //      qint64 maxSize)
  QIOReadOperation *read(qint64 offset, qint64 maxSize) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileThreadPoolBackendCall6 call = reinterpret_cast<CuteQRandomAccessAsyncFileThreadPoolBackendCall6>(taken[6]);
      void * given = call(this, offset, maxSize, &handled);
      if (handled) return static_cast<QIOReadOperation *>(given);
    }
    return QRandomAccessAsyncFileThreadPoolBackend::read(offset, maxSize);
  }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)

#if QT_CONFIG(future) && QT_CONFIG(thread)
  //  QIOWriteOperation
  //      *QRandomAccessAsyncFileThreadPoolBackend::write(qint64 offset,
  //      const QByteArray &data)
  QIOWriteOperation *write(qint64 offset, const QByteArray &data) override {
    if (taken[7]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileThreadPoolBackendCall7 call = reinterpret_cast<CuteQRandomAccessAsyncFileThreadPoolBackendCall7>(taken[7]);
      void * given = call(this, offset, &data, &handled);
      if (handled) return static_cast<QIOWriteOperation *>(given);
    }
    return QRandomAccessAsyncFileThreadPoolBackend::write(offset, data);
  }
#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
};

//  bool QRandomAccessAsyncFileThreadPoolBackend::init()
extern "C" Q_DECL_EXPORT
bool ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend4initEv(
    QRandomAccessAsyncFileThreadPoolBackend *self) {
  return self->init();
}

//  void QRandomAccessAsyncFileThreadPoolBackend::cancelAndWait(QIOOperation
//      *op)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend13cancelAndWaitEP12QIOOperation(
    QRandomAccessAsyncFileThreadPoolBackend *self,
    QIOOperation *op) {
  self->cancelAndWait(op);
}

//  void QRandomAccessAsyncFileThreadPoolBackend::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend5closeEv(
    QRandomAccessAsyncFileThreadPoolBackend *self) {
  self->close();
}

//  qint64 QRandomAccessAsyncFileThreadPoolBackend::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK39QRandomAccessAsyncFileThreadPoolBackend4sizeEv(
    const QRandomAccessAsyncFileThreadPoolBackend *self) {
  return self->size();
}

//  QIOOperation *QRandomAccessAsyncFileThreadPoolBackend::open(const QString
//      &path, QIODeviceBase::OpenMode mode)
extern "C" Q_DECL_EXPORT
QIOOperation *ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend4openERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QRandomAccessAsyncFileThreadPoolBackend *self,
    const QString *path,
    int mode) {
  return self->open(
      *path,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  QIOOperation *QRandomAccessAsyncFileThreadPoolBackend::flush()
extern "C" Q_DECL_EXPORT
QIOOperation *ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend5flushEv(
    QRandomAccessAsyncFileThreadPoolBackend *self) {
  return self->flush();
}

//  QIOReadOperation *QRandomAccessAsyncFileThreadPoolBackend::read(qint64
//      offset, qint64 maxSize)
extern "C" Q_DECL_EXPORT
QIOReadOperation *ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend4readExx(
    QRandomAccessAsyncFileThreadPoolBackend *self,
    qint64 offset,
    qint64 maxSize) {
  return self->read(offset, maxSize);
}

//  QIOWriteOperation *QRandomAccessAsyncFileThreadPoolBackend::write(qint64
//      offset, const QByteArray &data)
extern "C" Q_DECL_EXPORT
QIOWriteOperation *ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend5writeExRK10QByteArray(
    QRandomAccessAsyncFileThreadPoolBackend *self,
    qint64 offset,
    const QByteArray *data) {
  return self->write(offset, *data);
}

//  QIOWriteOperation *QRandomAccessAsyncFileThreadPoolBackend::write(qint64
//      offset, QByteArray &&data)
extern "C" Q_DECL_EXPORT
QIOWriteOperation *ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend5writeExO10QByteArray(
    QRandomAccessAsyncFileThreadPoolBackend *self,
    qint64 offset,
    QByteArray *data) {
  return self->write(offset, std::move(*data));
}

//  QIOVectoredReadOperation
//      *QRandomAccessAsyncFileThreadPoolBackend::readInto(qint64 offset,
//      QSpan<std::byte> buffer)
extern "C" Q_DECL_EXPORT
QIOVectoredReadOperation *ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend8readIntoEx5QSpanISt4byteLm18446744073709551615EE(
    QRandomAccessAsyncFileThreadPoolBackend *self,
    qint64 offset,
    const QSpan<std::byte> *buffer) {
  return self->readInto(offset, *buffer);
}

//  QIOVectoredWriteOperation
//      *QRandomAccessAsyncFileThreadPoolBackend::writeFrom(qint64 offset,
//      QSpan<const std::byte> buffer)
extern "C" Q_DECL_EXPORT
QIOVectoredWriteOperation *ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend9writeFromEx5QSpanIKSt4byteLm18446744073709551615EE(
    QRandomAccessAsyncFileThreadPoolBackend *self,
    qint64 offset,
    const QSpan<const std::byte> *buffer) {
  return self->writeFrom(offset, *buffer);
}

//  QIOVectoredReadOperation
//      *QRandomAccessAsyncFileThreadPoolBackend::readInto(qint64 offset,
//      QSpan<const QSpan<std::byte>> buffers)
extern "C" Q_DECL_EXPORT
QIOVectoredReadOperation *ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend8readIntoEx5QSpanIKS0_ISt4byteLm18446744073709551615EELm18446744073709551615EE(
    QRandomAccessAsyncFileThreadPoolBackend *self,
    qint64 offset,
    const QSpan<const QSpan<std::byte>> *buffers) {
  return self->readInto(offset, *buffers);
}

//  QIOVectoredWriteOperation
//      *QRandomAccessAsyncFileThreadPoolBackend::writeFrom(qint64 offset,
//      QSpan<const QSpan<const std::byte>> buffers)
extern "C" Q_DECL_EXPORT
QIOVectoredWriteOperation *ritual_ZN39QRandomAccessAsyncFileThreadPoolBackend9writeFromEx5QSpanIKS0_IKSt4byteLm18446744073709551615EELm18446744073709551615EE(
    QRandomAccessAsyncFileThreadPoolBackend *self,
    qint64 offset,
    const QSpan<const QSpan<const std::byte>> *buffers) {
  return self->writeFrom(offset, *buffers);
}

//  a Python function taken by a CuteQRandomAccessAsyncFileThreadPoolBackend,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRandomAccessAsyncFileThreadPoolBackend(
    QRandomAccessAsyncFileThreadPoolBackend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRandomAccessAsyncFileThreadPoolBackend *>(self)->take(key, call);
}

#if QT_CONFIG(thread)
#if QT_CONFIG(future)
//  void QRandomAccessAsyncFileThreadPoolBackend::cancelAndWait(QIOOperation
//      *op)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN39QRandomAccessAsyncFileThreadPoolBackend13cancelAndWaitEP12QIOOperation(
    QRandomAccessAsyncFileThreadPoolBackend *self,
    QIOOperation *op) {
  self->QRandomAccessAsyncFileThreadPoolBackend::cancelAndWait(op);
}
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(thread)

#if QT_CONFIG(thread)
#if QT_CONFIG(future)
//  void QRandomAccessAsyncFileThreadPoolBackend::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN39QRandomAccessAsyncFileThreadPoolBackend5closeEv(
    QRandomAccessAsyncFileThreadPoolBackend *self) {
  self->QRandomAccessAsyncFileThreadPoolBackend::close();
}
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(thread)

#if QT_CONFIG(thread)
#if QT_CONFIG(future)
//  qint64 QRandomAccessAsyncFileThreadPoolBackend::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK39QRandomAccessAsyncFileThreadPoolBackend4sizeEv(
    const QRandomAccessAsyncFileThreadPoolBackend *self) {
  return self->QRandomAccessAsyncFileThreadPoolBackend::size();
}
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(thread)

#endif  // QT_CONFIG(future) && QT_CONFIG(thread)
#endif  // QT_CONFIG(async_io)

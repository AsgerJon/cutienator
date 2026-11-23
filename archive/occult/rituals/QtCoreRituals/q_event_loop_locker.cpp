//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qeventloop.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qeventloop.h>

//  QEventLoopLocker::QEventLoopLocker()
extern "C" Q_DECL_EXPORT
QEventLoopLocker *ritual_ZN16QEventLoopLockerC1Ev() {
  return new QEventLoopLocker();
}

//  QEventLoopLocker::QEventLoopLocker(QEventLoop *loop)
extern "C" Q_DECL_EXPORT
QEventLoopLocker *ritual_ZN16QEventLoopLockerC1EP10QEventLoop(
    QEventLoop *loop) {
  return new QEventLoopLocker(loop);
}

//  QEventLoopLocker::QEventLoopLocker(QThread *thread)
extern "C" Q_DECL_EXPORT
QEventLoopLocker *ritual_ZN16QEventLoopLockerC1EP7QThread(QThread *thread) {
  return new QEventLoopLocker(thread);
}

//  QEventLoopLocker::~QEventLoopLocker()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QEventLoopLockerD1Ev(QEventLoopLocker *self) {
  delete self;
}

//  Type QEventLoopLocker::type() const
extern "C" Q_DECL_EXPORT
QEventLoopLocker::Type ritual_ZNK16QEventLoopLocker4typeEv(
    const QEventLoopLocker *self) {
  return self->type();
}

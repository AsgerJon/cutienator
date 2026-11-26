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

//  QEventLoopLocker::QEventLoopLocker(QEventLoopLocker &&other)
extern "C" Q_DECL_EXPORT
QEventLoopLocker *ritual_ZN16QEventLoopLockerC1EOS_(
    QEventLoopLocker *other) {
  return new QEventLoopLocker(std::move(*other));
}

//  QEventLoopLocker &QEventLoopLocker::operator=(QEventLoopLocker &&other)
extern "C" Q_DECL_EXPORT
QEventLoopLocker *ritual_ZN16QEventLoopLockeraSEOS_(
    QEventLoopLocker *self,
    QEventLoopLocker *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QEventLoopLocker::swap(QEventLoopLocker &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QEventLoopLocker4swapERS_(
    QEventLoopLocker *self,
    QEventLoopLocker *other) {
  self->swap(*other);
}

//  Type QEventLoopLocker::type() const
extern "C" Q_DECL_EXPORT
QEventLoopLocker::Type ritual_ZNK16QEventLoopLocker4typeEv(
    const QEventLoopLocker *self) {
  return self->type();
}

//  void *QEventLoopLocker::pointer() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK16QEventLoopLocker7pointerEv(const QEventLoopLocker *self) {
  return self->pointer();
}

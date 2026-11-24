//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsharedpointer_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if !defined(Q_QDOC)
#include <QtCore/qsharedpointer.h>

//  QtSharedPointer::ExternalRefCountData::~ExternalRefCountData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtSharedPointer20ExternalRefCountDataD1Ev(
    QtSharedPointer::ExternalRefCountData *self) {
  delete self;
}

//  void QtSharedPointer::ExternalRefCountData::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtSharedPointer20ExternalRefCountData7destroyEv(
    QtSharedPointer::ExternalRefCountData *self) {
  self->destroy();
}

#if !defined(QT_NO_QOBJECT)
//  ExternalRefCountData
//      *QtSharedPointer::ExternalRefCountData::getAndRef(const QObject *a0)
extern "C" Q_DECL_EXPORT
QtSharedPointer::ExternalRefCountData *ritual_ZN15QtSharedPointer20ExternalRefCountData9getAndRefEPK7QObject(
    const QObject *a0) {
  return QtSharedPointer::ExternalRefCountData::getAndRef(a0);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QtSharedPointer::ExternalRefCountData::setQObjectShared(const
//      QObject *a0, bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtSharedPointer20ExternalRefCountData16setQObjectSharedEPK7QObjectb(
    QtSharedPointer::ExternalRefCountData *self,
    const QObject *a0,
    bool enable) {
  self->setQObjectShared(a0, enable);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void QtSharedPointer::ExternalRefCountData::checkQObjectShared(const
//      QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtSharedPointer20ExternalRefCountData18checkQObjectSharedEPK7QObject(
    QtSharedPointer::ExternalRefCountData *self,
    const QObject *a0) {
  self->checkQObjectShared(a0);
}
#endif  // !defined(QT_NO_QOBJECT)

#endif  // !defined(Q_QDOC)

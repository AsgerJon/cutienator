//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsharedpointer_impl.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  added by hand:
//  'ritual_ZN15QtSharedPointer20ExternalRefCountData18checkQObjectSharedEz',
//  'ritual_ZN15QtSharedPointer20ExternalRefCountData16setQObjectSharedEz'.
//  Kept as it is when the generator runs again. Also added by hand on
//  2026-11-25, rituals for functions the generator leaves out: 2.
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

//  void *QtSharedPointer::ExternalRefCountData::operator new(std::size_t a0,
//      void *ptr)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QtSharedPointer20ExternalRefCountDatanwEmPv(
    QtSharedPointer::ExternalRefCountData *self,
    std::size_t a0,
    void *ptr) {
  return self->operator new(a0, ptr);
}

//  void QtSharedPointer::ExternalRefCountData::operator delete(void *ptr)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtSharedPointer20ExternalRefCountDatadlEPv(
    QtSharedPointer::ExternalRefCountData *self,
    void *ptr) {
  self->operator delete(ptr);
}

//  void QtSharedPointer::ExternalRefCountData::operator delete(void *a0,
//      void *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtSharedPointer20ExternalRefCountDatadlEPvS1_(
    QtSharedPointer::ExternalRefCountData *self,
    void *a0,
    void *a1) {
  self->operator delete(a0, a1);
}

//  void QtSharedPointer::ExternalRefCountData::checkQObjectShared(...)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtSharedPointer20ExternalRefCountData18checkQObjectSharedEz(
    QtSharedPointer::ExternalRefCountData *self) {
  self->checkQObjectShared();
}

//  void QtSharedPointer::ExternalRefCountData::setQObjectShared(...)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QtSharedPointer20ExternalRefCountData16setQObjectSharedEz(
    QtSharedPointer::ExternalRefCountData *self) {
  self->setQObjectShared();
}

//  QtSharedPointer::ExternalRefCountData::ExternalRefCountData(DestroyerFn
//      d)
extern "C" Q_DECL_EXPORT
QtSharedPointer::ExternalRefCountData *ritual_ZN15QtSharedPointer20ExternalRefCountDataC2EPFvPS0_E(
    void *d) {
  using Data = QtSharedPointer::ExternalRefCountData;
  void *memory = ::operator new(sizeof(Data));
  return new (memory) Data(reinterpret_cast<Data::DestroyerFn>(d));
}

//  QtSharedPointer::ExternalRefCountData::ExternalRefCountData(Qt::Initializ
//      ation a0)
extern "C" Q_DECL_EXPORT
QtSharedPointer::ExternalRefCountData *ritual_ZN15QtSharedPointer20ExternalRefCountDataC2EN2Qt14InitializationE(
    int a0) {
  using Data = QtSharedPointer::ExternalRefCountData;
  void *memory = ::operator new(sizeof(Data));
  return new (memory) Data(static_cast<Qt::Initialization>(a0));
}

#endif  // !defined(Q_QDOC)

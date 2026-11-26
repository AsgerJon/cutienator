//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectdefs.h>

//  QtPrivate::QSlotObjectBase::QSlotObjectBase(ImplFn fn)
extern "C" Q_DECL_EXPORT
QtPrivate::QSlotObjectBase *ritual_ZN9QtPrivate15QSlotObjectBaseC1EPFviPS0_P7QObjectPPvPbE(
    void *fn) {
  return new QtPrivate::QSlotObjectBase(
      reinterpret_cast<QtPrivate::QSlotObjectBase::ImplFn>(fn));
}

//  bool QtPrivate::QSlotObjectBase::ref()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate15QSlotObjectBase3refEv(
    QtPrivate::QSlotObjectBase *self) {
  return self->ref();
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QtPrivate::QSlotObjectBase::destroyIfLastRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QSlotObjectBase16destroyIfLastRefEv(
    QtPrivate::QSlotObjectBase *self) {
  self->destroyIfLastRef();
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  bool QtPrivate::QSlotObjectBase::compare(void **a)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate15QSlotObjectBase7compareEPPv(
    QtPrivate::QSlotObjectBase *self,
    void **a) {
  return self->compare(a);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QtPrivate::QSlotObjectBase::call(QObject *r, void **a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QSlotObjectBase4callEP7QObjectPPv(
    QtPrivate::QSlotObjectBase *self,
    QObject *r,
    void **a) {
  self->call(r, a);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  bool QtPrivate::QSlotObjectBase::isImpl(ImplFn f) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate15QSlotObjectBase6isImplEPFviPS0_P7QObjectPPvPbE(
    const QtPrivate::QSlotObjectBase *self,
    void *f) {
  return self->isImpl(
      reinterpret_cast<QtPrivate::QSlotObjectBase::ImplFn>(f));
}

//  QtPrivate::QSlotObjectBase::~QSlotObjectBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15QSlotObjectBaseD1Ev(
    QtPrivate::QSlotObjectBase *self) {
  delete self;
}

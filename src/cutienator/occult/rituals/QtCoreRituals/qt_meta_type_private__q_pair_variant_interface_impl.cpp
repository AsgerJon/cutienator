//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmetatype.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 7. Kept as it is when the
//  generator runs again.
#include <QtCore/qmetatype.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <utility>

//  QtMetaTypePrivate::QPairVariantInterfaceImpl::QPairVariantInterfaceImpl()
extern "C" Q_DECL_EXPORT
QtMetaTypePrivate::QPairVariantInterfaceImpl *ritual_ZN17QtMetaTypePrivate25QPairVariantInterfaceImplC1Ev() {
  return new QtMetaTypePrivate::QPairVariantInterfaceImpl();
}

//  void QtMetaTypePrivate::QPairVariantInterfaceImpl::first(void *dataPtr)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QtMetaTypePrivate25QPairVariantInterfaceImpl5firstEPv(
    const QtMetaTypePrivate::QPairVariantInterfaceImpl *self,
    void *dataPtr) {
  self->first(dataPtr);
}

//  void QtMetaTypePrivate::QPairVariantInterfaceImpl::second(void *dataPtr)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QtMetaTypePrivate25QPairVariantInterfaceImpl6secondEPv(
    const QtMetaTypePrivate::QPairVariantInterfaceImpl *self,
    void *dataPtr) {
  self->second(dataPtr);
}

//  QtMetaTypePrivate::QPairVariantInterfaceImpl::~QPairVariantInterfaceImpl(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtMetaTypePrivate25QPairVariantInterfaceImplD1Ev(
    QtMetaTypePrivate::QPairVariantInterfaceImpl *self) {
  delete self;
}

//  
//      QtMetaTypePrivate::QPairVariantInterfaceImpl::QPairVariantInterfaceImpl<std::pair<int,
//      int>>(const std::pair<int, int> *p)
extern "C" Q_DECL_EXPORT
QtMetaTypePrivate::QPairVariantInterfaceImpl * ritual_ZN17QtMetaTypePrivate25QPairVariantInterfaceImplC2ISt4pairIiiEEEPKT_(
    const std::pair<int, int> *p) {
  return new QtMetaTypePrivate::QPairVariantInterfaceImpl(p);
}

//  
//      QtMetaTypePrivate::QPairVariantInterfaceImpl::QPairVariantInterfaceImpl<std::pair<QString,
//      int>>(const std::pair<QString, int> *p)
extern "C" Q_DECL_EXPORT
QtMetaTypePrivate::QPairVariantInterfaceImpl * ritual_ZN17QtMetaTypePrivate25QPairVariantInterfaceImplC2ISt4pairI7QStringiEEEPKT_(
    const std::pair<QString, int> *p) {
  return new QtMetaTypePrivate::QPairVariantInterfaceImpl(p);
}

//  
//      QtMetaTypePrivate::QPairVariantInterfaceImpl::QPairVariantInterfaceImpl<std::pair<QString,
//      QVariant>>(const std::pair<QString, QVariant> *p)
extern "C" Q_DECL_EXPORT
QtMetaTypePrivate::QPairVariantInterfaceImpl * ritual_ZN17QtMetaTypePrivate25QPairVariantInterfaceImplC2ISt4pairI7QString8QVariantEEEPKT_(
    const std::pair<QString, QVariant> *p) {
  return new QtMetaTypePrivate::QPairVariantInterfaceImpl(p);
}

//  static void
//      QtMetaTypePrivate::QPairVariantInterfaceImpl::getFirstImpl<std::pair<int,
//      int>>(const void *const *pair, void *dataPtr)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtMetaTypePrivate25QPairVariantInterfaceImpl12getFirstImplISt4pairIiiEEEvPKPKvPv(
    const void *const *pair,
    void *dataPtr) {
  QtMetaTypePrivate::QPairVariantInterfaceImpl::getFirstImpl<std::pair<int, int>>(pair, dataPtr);
}

//  static void
//      QtMetaTypePrivate::QPairVariantInterfaceImpl::getFirstImpl<std::pair<QString,
//      QVariant>>(const void *const *pair, void *dataPtr)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtMetaTypePrivate25QPairVariantInterfaceImpl12getFirstImplISt4pairI7QString8QVariantEEEvPKPKvPv(
    const void *const *pair,
    void *dataPtr) {
  QtMetaTypePrivate::QPairVariantInterfaceImpl::getFirstImpl<std::pair<QString, QVariant>>(pair, dataPtr);
}

//  static void
//      QtMetaTypePrivate::QPairVariantInterfaceImpl::getSecondImpl<std::pair<int,
//      int>>(const void *const *pair, void *dataPtr)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtMetaTypePrivate25QPairVariantInterfaceImpl13getSecondImplISt4pairIiiEEEvPKPKvPv(
    const void *const *pair,
    void *dataPtr) {
  QtMetaTypePrivate::QPairVariantInterfaceImpl::getSecondImpl<std::pair<int, int>>(pair, dataPtr);
}

//  static void
//      QtMetaTypePrivate::QPairVariantInterfaceImpl::getSecondImpl<std::pair<QString,
//      QVariant>>(const void *const *pair, void *dataPtr)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtMetaTypePrivate25QPairVariantInterfaceImpl13getSecondImplISt4pairI7QString8QVariantEEEvPKPKvPv(
    const void *const *pair,
    void *dataPtr) {
  QtMetaTypePrivate::QPairVariantInterfaceImpl::getSecondImpl<std::pair<QString, QVariant>>(pair, dataPtr);
}

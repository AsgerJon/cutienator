//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qaspectfactory_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qaspectfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qlist.h>

//  Qt3DCore::QAspectFactory::QAspectFactory()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectFactory *ritual_ZN8Qt3DCore14QAspectFactoryC1Ev() {
  return new Qt3DCore::QAspectFactory();
}

//  Qt3DCore::QAspectFactory::QAspectFactory(const QAspectFactory &other)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectFactory *ritual_ZN8Qt3DCore14QAspectFactoryC1ERKS0_(
    const Qt3DCore::QAspectFactory *other) {
  return new Qt3DCore::QAspectFactory(*other);
}

//  Qt3DCore::QAspectFactory::~QAspectFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore14QAspectFactoryD1Ev(Qt3DCore::QAspectFactory *self) {
  delete self;
}

//  QAspectFactory &Qt3DCore::QAspectFactory::operator=(const QAspectFactory
//      &other)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectFactory *ritual_ZN8Qt3DCore14QAspectFactoryaSERKS0_(
    Qt3DCore::QAspectFactory *self,
    const Qt3DCore::QAspectFactory *other) {
  return &(self->operator=(*other));
}

#if defined(Q_COMPILER_RVALUE_REFS)
//  QAspectFactory &Qt3DCore::QAspectFactory::operator=(QAspectFactory
//      &&other)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectFactory *ritual_ZN8Qt3DCore14QAspectFactoryaSEOS0_(
    Qt3DCore::QAspectFactory *self,
    Qt3DCore::QAspectFactory *other) {
  return &(self->operator=(std::move(*other)));
}
#endif  // defined(Q_COMPILER_RVALUE_REFS)

//  void Qt3DCore::QAspectFactory::swap(QAspectFactory &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore14QAspectFactory4swapERS0_(
    Qt3DCore::QAspectFactory *self,
    Qt3DCore::QAspectFactory *other) {
  self->swap(*other);
}

//  QList<QLatin1String> Qt3DCore::QAspectFactory::availableFactories() const
extern "C" Q_DECL_EXPORT
QList<QLatin1String> *ritual_ZNK8Qt3DCore14QAspectFactory18availableFactoriesEv(
    const Qt3DCore::QAspectFactory *self) {
  return new QList<QLatin1String>(self->availableFactories());
}

//  QAbstractAspect *Qt3DCore::QAspectFactory::createAspect(const
//      QLatin1String &aspect, QObject *parent) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractAspect *ritual_ZNK8Qt3DCore14QAspectFactory12createAspectERK13QLatin1StringP7QObject(
    const Qt3DCore::QAspectFactory *self,
    const QLatin1String *aspect,
    QObject *parent) {
  return self->createAspect(*aspect, parent);
}

//  QLatin1String Qt3DCore::QAspectFactory::aspectName(QAbstractAspect
//      *aspect) const
extern "C" Q_DECL_EXPORT
QLatin1String *ritual_ZNK8Qt3DCore14QAspectFactory10aspectNameEPNS_15QAbstractAspectE(
    const Qt3DCore::QAspectFactory *self,
    Qt3DCore::QAbstractAspect *aspect) {
  return new QLatin1String(self->aspectName(aspect));
}

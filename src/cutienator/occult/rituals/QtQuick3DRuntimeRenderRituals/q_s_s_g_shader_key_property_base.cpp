//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qbytearrayview.h>

//  QSSGShaderKeyPropertyBase::QSSGShaderKeyPropertyBase(const char *inName)
extern "C" Q_DECL_EXPORT
QSSGShaderKeyPropertyBase *ritual_ZN25QSSGShaderKeyPropertyBaseC1EPKc(
    const char *inName) {
  return new QSSGShaderKeyPropertyBase(inName);
}

//  quint32 QSSGShaderKeyPropertyBase::getOffset() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK25QSSGShaderKeyPropertyBase9getOffsetEv(
    const QSSGShaderKeyPropertyBase *self) {
  return self->getOffset();
}

//  void QSSGShaderKeyPropertyBase::setOffset(quint32 of)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGShaderKeyPropertyBase9setOffsetEj(
    QSSGShaderKeyPropertyBase *self,
    quint32 of) {
  self->setOffset(of);
}

//  quint32 QSSGShaderKeyPropertyBase::getIdx() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK25QSSGShaderKeyPropertyBase6getIdxEv(
    const QSSGShaderKeyPropertyBase *self) {
  return self->getIdx();
}

//  bool QSSGShaderKeyPropertyBase::getBoolValue(const QByteArray &str, const
//      QByteArrayView &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QSSGShaderKeyPropertyBase12getBoolValueERK10QByteArrayRK14QByteArrayView(
    const QByteArray *str,
    const QByteArrayView *name) {
  return QSSGShaderKeyPropertyBase::getBoolValue(*str, *name);
}

//  QSSGShaderKeyPropertyBase::~QSSGShaderKeyPropertyBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGShaderKeyPropertyBaseD1Ev(
    QSSGShaderKeyPropertyBase *self) {
  delete self;
}

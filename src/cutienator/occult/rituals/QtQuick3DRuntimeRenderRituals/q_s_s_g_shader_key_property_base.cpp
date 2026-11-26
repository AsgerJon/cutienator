//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
//  Qt 6.12.0. Edited by hand on 2026-11-25: added by hand, instances of
//  templates of the class: 4. Kept as it is when the generator runs again.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>

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

//  void QSSGShaderKeyPropertyBase::internalToString(QByteArray &ioStr, const
//      QByteArrayView &inBuffer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QSSGShaderKeyPropertyBase16internalToStringER10QByteArrayRK14QByteArrayView(
    const QSSGShaderKeyPropertyBase *self,
    QByteArray *ioStr,
    const QByteArrayView *inBuffer) {
  self->internalToString(*ioStr, *inBuffer);
}

//  void QSSGShaderKeyPropertyBase::internalToString(QByteArray &ioStr, const
//      QByteArrayView &name, bool inValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGShaderKeyPropertyBase16internalToStringER10QByteArrayRK14QByteArrayViewb(
    QByteArray *ioStr,
    const QByteArrayView *name,
    bool inValue) {
  QSSGShaderKeyPropertyBase::internalToString(*ioStr, *name, inValue);
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

//  quint32 QSSGShaderKeyPropertyBase::getMaskTemplate<1u>() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK25QSSGShaderKeyPropertyBase15getMaskTemplateILj1EEjv(const QSSGShaderKeyPropertyBase *self) {
  return self->getMaskTemplate<1>();
}

//  quint32 QSSGShaderKeyPropertyBase::getMaskTemplate<2u>() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK25QSSGShaderKeyPropertyBase15getMaskTemplateILj2EEjv(const QSSGShaderKeyPropertyBase *self) {
  return self->getMaskTemplate<2>();
}

//  quint32 QSSGShaderKeyPropertyBase::getMaskTemplate<7u>() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK25QSSGShaderKeyPropertyBase15getMaskTemplateILj7EEjv(const QSSGShaderKeyPropertyBase *self) {
  return self->getMaskTemplate<7>();
}

//  quint32 QSSGShaderKeyPropertyBase::getMaskTemplate<9u>() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK25QSSGShaderKeyPropertyBase15getMaskTemplateILj9EEjv(const QSSGShaderKeyPropertyBase *self) {
  return self->getMaskTemplate<9>();
}

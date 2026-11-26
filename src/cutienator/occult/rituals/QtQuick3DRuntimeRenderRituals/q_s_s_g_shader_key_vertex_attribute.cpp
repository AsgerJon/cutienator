//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/QByteArray>

//  QSSGShaderKeyVertexAttribute::QSSGShaderKeyVertexAttribute(const char
//      *inName)
extern "C" Q_DECL_EXPORT
QSSGShaderKeyVertexAttribute *ritual_ZN28QSSGShaderKeyVertexAttributeC1EPKc(
    const char *inName) {
  return new QSSGShaderKeyVertexAttribute(inName);
}

//  bool QSSGShaderKeyVertexAttribute::getBitValue(VertexAttributeBits bit,
//      QSSGDataView<quint32> inKeySet) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QSSGShaderKeyVertexAttribute11getBitValueENS_19VertexAttributeBitsE12QSSGDataViewIjE(
    const QSSGShaderKeyVertexAttribute *self,
    QSSGShaderKeyVertexAttribute::VertexAttributeBits bit,
    const QSSGDataView<quint32> *inKeySet) {
  return self->getBitValue(bit, *inKeySet);
}

//  void QSSGShaderKeyVertexAttribute::setBitValue(VertexAttributeBits bit,
//      QSSGDataRef<quint32> inKeySet, bool value) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QSSGShaderKeyVertexAttribute11setBitValueENS_19VertexAttributeBitsE11QSSGDataRefIjEb(
    const QSSGShaderKeyVertexAttribute *self,
    QSSGShaderKeyVertexAttribute::VertexAttributeBits bit,
    const QSSGDataRef<quint32> *inKeySet,
    bool value) {
  self->setBitValue(bit, *inKeySet, value);
}

//  void QSSGShaderKeyVertexAttribute::toString(QByteArray &ioStr,
//      QSSGDataView<quint32> inKeySet) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK28QSSGShaderKeyVertexAttribute8toStringER10QByteArray12QSSGDataViewIjE(
    const QSSGShaderKeyVertexAttribute *self,
    QByteArray *ioStr,
    const QSSGDataView<quint32> *inKeySet) {
  self->toString(*ioStr, *inKeySet);
}

//  void QSSGShaderKeyVertexAttribute::fromString(const QByteArray &ioStr,
//      QSSGDataRef<quint32> inKeySet)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSSGShaderKeyVertexAttribute10fromStringERK10QByteArray11QSSGDataRefIjE(
    QSSGShaderKeyVertexAttribute *self,
    const QByteArray *ioStr,
    const QSSGDataRef<quint32> *inKeySet) {
  self->fromString(*ioStr, *inKeySet);
}

//  QSSGShaderKeyVertexAttribute::~QSSGShaderKeyVertexAttribute()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSSGShaderKeyVertexAttributeD1Ev(
    QSSGShaderKeyVertexAttribute *self) {
  delete self;
}

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

//  QSSGShaderKeyBoolean::QSSGShaderKeyBoolean(const char *inName)
extern "C" Q_DECL_EXPORT
QSSGShaderKeyBoolean *ritual_ZN20QSSGShaderKeyBooleanC1EPKc(
    const char *inName) {
  return new QSSGShaderKeyBoolean(inName);
}

//  quint32 QSSGShaderKeyBoolean::getMask() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK20QSSGShaderKeyBoolean7getMaskEv(
    const QSSGShaderKeyBoolean *self) {
  return self->getMask();
}

//  void QSSGShaderKeyBoolean::setValue(QSSGDataRef<quint32> inDataStore,
//      bool inValue) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QSSGShaderKeyBoolean8setValueE11QSSGDataRefIjEb(
    const QSSGShaderKeyBoolean *self,
    const QSSGDataRef<quint32> *inDataStore,
    bool inValue) {
  self->setValue(*inDataStore, inValue);
}

//  bool QSSGShaderKeyBoolean::getValue(QSSGDataView<quint32> inDataStore)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QSSGShaderKeyBoolean8getValueE12QSSGDataViewIjE(
    const QSSGShaderKeyBoolean *self,
    const QSSGDataView<quint32> *inDataStore) {
  return self->getValue(*inDataStore);
}

//  void QSSGShaderKeyBoolean::toString(QByteArray &ioStr,
//      QSSGDataView<quint32> inKeySet) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QSSGShaderKeyBoolean8toStringER10QByteArray12QSSGDataViewIjE(
    const QSSGShaderKeyBoolean *self,
    QByteArray *ioStr,
    const QSSGDataView<quint32> *inKeySet) {
  self->toString(*ioStr, *inKeySet);
}

//  void QSSGShaderKeyBoolean::fromString(const QByteArray &ioStr,
//      QSSGDataRef<quint32> inKeySet)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGShaderKeyBoolean10fromStringERK10QByteArray11QSSGDataRefIjE(
    QSSGShaderKeyBoolean *self,
    const QByteArray *ioStr,
    const QSSGDataRef<quint32> *inKeySet) {
  self->fromString(*ioStr, *inKeySet);
}

//  QSSGShaderKeyBoolean::~QSSGShaderKeyBoolean()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGShaderKeyBooleanD1Ev(QSSGShaderKeyBoolean *self) {
  delete self;
}

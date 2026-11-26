//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dbuffer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/quick3dbuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurl.h>
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *Qt3DCore::Quick::Quick3DBuffer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore5Quick13Quick3DBuffer10metaObjectEv(
    const Qt3DCore::Quick::Quick3DBuffer *self) {
  return self->metaObject();
}

//  void *Qt3DCore::Quick::Quick3DBuffer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore5Quick13Quick3DBuffer11qt_metacastEPKc(
    Qt3DCore::Quick::Quick3DBuffer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::Quick::Quick3DBuffer::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore5Quick13Quick3DBuffer11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::Quick::Quick3DBuffer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DCore::Quick::Quick3DBuffer::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8Qt3DCore5Quick13Quick3DBuffer2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DCore::Quick::Quick3DBuffer::tr(s, c, n));
}

//  Qt3DCore::Quick::Quick3DBuffer::Quick3DBuffer(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DCore::Quick::Quick3DBuffer *ritual_ZN8Qt3DCore5Quick13Quick3DBufferC1EPNS_5QNodeE(
    Qt3DCore::QNode *parent) {
  return new Qt3DCore::Quick::Quick3DBuffer(parent);
}

//  QVariant Qt3DCore::Quick::Quick3DBuffer::bufferData() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK8Qt3DCore5Quick13Quick3DBuffer10bufferDataEv(
    const Qt3DCore::Quick::Quick3DBuffer *self) {
  return new QVariant(self->bufferData());
}

//  void Qt3DCore::Quick::Quick3DBuffer::setBufferData(const QVariant
//      &bufferData)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick13Quick3DBuffer13setBufferDataERK8QVariant(
    Qt3DCore::Quick::Quick3DBuffer *self,
    const QVariant *bufferData) {
  self->setBufferData(*bufferData);
}

//  QVariant Qt3DCore::Quick::Quick3DBuffer::readBinaryFile(const QUrl
//      &fileUrl)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8Qt3DCore5Quick13Quick3DBuffer14readBinaryFileERK4QUrl(
    Qt3DCore::Quick::Quick3DBuffer *self,
    const QUrl *fileUrl) {
  return new QVariant(self->readBinaryFile(*fileUrl));
}

//  void Qt3DCore::Quick::Quick3DBuffer::updateData(int offset, const
//      QVariant &bytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick13Quick3DBuffer10updateDataEiRK8QVariant(
    Qt3DCore::Quick::Quick3DBuffer *self,
    int offset,
    const QVariant *bytes) {
  self->updateData(offset, *bytes);
}

//  void Qt3DCore::Quick::Quick3DBuffer::bufferDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick13Quick3DBuffer17bufferDataChangedEv(
    Qt3DCore::Quick::Quick3DBuffer *self) {
  self->bufferDataChanged();
}

//  void Qt3DCore::Quick::Quick3DBuffer::initEngines()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick13Quick3DBuffer11initEnginesEv(
    Qt3DCore::Quick::Quick3DBuffer *self) {
  self->initEngines();
}

//  QByteArray Qt3DCore::Quick::Quick3DBuffer::convertToRawData(const
//      QJSValue &jsValue)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN8Qt3DCore5Quick13Quick3DBuffer16convertToRawDataERK8QJSValue(
    Qt3DCore::Quick::Quick3DBuffer *self,
    const QJSValue *jsValue) {
  return new QByteArray(self->convertToRawData(*jsValue));
}

//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qshaderdescription_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qshaderdescription_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsondocument.h>

//  QShaderDescriptionPrivate::QShaderDescriptionPrivate()
extern "C" Q_DECL_EXPORT
QShaderDescriptionPrivate *ritual_ZN25QShaderDescriptionPrivateC1Ev() {
  return new QShaderDescriptionPrivate();
}

//  QShaderDescriptionPrivate::QShaderDescriptionPrivate(const
//      QShaderDescriptionPrivate &other)
extern "C" Q_DECL_EXPORT
QShaderDescriptionPrivate *ritual_ZN25QShaderDescriptionPrivateC1ERKS_(
    const QShaderDescriptionPrivate *other) {
  return new QShaderDescriptionPrivate(*other);
}

//  QShaderDescriptionPrivate
//      *QShaderDescriptionPrivate::get(QShaderDescription *desc)
extern "C" Q_DECL_EXPORT
QShaderDescriptionPrivate *ritual_ZN25QShaderDescriptionPrivate3getEP18QShaderDescription(
    QShaderDescription *desc) {
  return QShaderDescriptionPrivate::get(desc);
}

//  const QShaderDescriptionPrivate *QShaderDescriptionPrivate::get(const
//      QShaderDescription *desc)
extern "C" Q_DECL_EXPORT
const QShaderDescriptionPrivate *ritual_ZN25QShaderDescriptionPrivate3getEPK18QShaderDescription(
    const QShaderDescription *desc) {
  return QShaderDescriptionPrivate::get(desc);
}

//  QJsonDocument QShaderDescriptionPrivate::makeDoc()
extern "C" Q_DECL_EXPORT
QJsonDocument *ritual_ZN25QShaderDescriptionPrivate7makeDocEv(
    QShaderDescriptionPrivate *self) {
  return new QJsonDocument(self->makeDoc());
}

//  void QShaderDescriptionPrivate::writeToStream(QDataStream *stream, int
//      version)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QShaderDescriptionPrivate13writeToStreamEP11QDataStreami(
    QShaderDescriptionPrivate *self,
    QDataStream *stream,
    int version) {
  self->writeToStream(stream, version);
}

//  void QShaderDescriptionPrivate::loadFromStream(QDataStream *stream, int
//      version)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QShaderDescriptionPrivate14loadFromStreamEP11QDataStreami(
    QShaderDescriptionPrivate *self,
    QDataStream *stream,
    int version) {
  self->loadFromStream(stream, version);
}

//  QShaderDescriptionPrivate::~QShaderDescriptionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QShaderDescriptionPrivateD1Ev(
    QShaderDescriptionPrivate *self) {
  delete self;
}

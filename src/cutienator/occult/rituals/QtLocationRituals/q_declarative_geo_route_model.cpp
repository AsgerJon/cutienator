//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeoroutemodel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeoroutemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtLocation/qgeoroute.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  const QMetaObject *QDeclarativeGeoRouteModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QDeclarativeGeoRouteModel10metaObjectEv(
    const QDeclarativeGeoRouteModel *self) {
  return self->metaObject();
}

//  QString QDeclarativeGeoRouteModel::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QDeclarativeGeoRouteModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeGeoRouteModel::tr(s, c, n));
}

//  QDeclarativeGeoRouteModel::QDeclarativeGeoRouteModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoRouteModel *ritual_ZN25QDeclarativeGeoRouteModelC1EP7QObject(
    QObject *parent) {
  return new QDeclarativeGeoRouteModel(parent);
}

//  void QDeclarativeGeoRouteModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel10classBeginEv(
    QDeclarativeGeoRouteModel *self) {
  self->classBegin();
}

//  void QDeclarativeGeoRouteModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel17componentCompleteEv(
    QDeclarativeGeoRouteModel *self) {
  self->componentComplete();
}

//  int QDeclarativeGeoRouteModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QDeclarativeGeoRouteModel8rowCountERK11QModelIndex(
    const QDeclarativeGeoRouteModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QVariant QDeclarativeGeoRouteModel::data(const QModelIndex &index, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QDeclarativeGeoRouteModel4dataERK11QModelIndexi(
    const QDeclarativeGeoRouteModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  QHash<int, QByteArray> QDeclarativeGeoRouteModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK25QDeclarativeGeoRouteModel9roleNamesEv(
    const QDeclarativeGeoRouteModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  void QDeclarativeGeoRouteModel::setPlugin(QDeclarativeGeoServiceProvider
//      *plugin)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel9setPluginEP30QDeclarativeGeoServiceProvider(
    QDeclarativeGeoRouteModel *self,
    QDeclarativeGeoServiceProvider *plugin) {
  self->setPlugin(plugin);
}

//  QDeclarativeGeoServiceProvider *QDeclarativeGeoRouteModel::plugin() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoServiceProvider *ritual_ZNK25QDeclarativeGeoRouteModel6pluginEv(
    const QDeclarativeGeoRouteModel *self) {
  return self->plugin();
}

//  void QDeclarativeGeoRouteModel::setQuery(QDeclarativeGeoRouteQuery
//      *query)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel8setQueryEP25QDeclarativeGeoRouteQuery(
    QDeclarativeGeoRouteModel *self,
    QDeclarativeGeoRouteQuery *query) {
  self->setQuery(query);
}

//  QDeclarativeGeoRouteQuery *QDeclarativeGeoRouteModel::query() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoRouteQuery *ritual_ZNK25QDeclarativeGeoRouteModel5queryEv(
    const QDeclarativeGeoRouteModel *self) {
  return self->query();
}

//  void QDeclarativeGeoRouteModel::setAutoUpdate(bool autoUpdate)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel13setAutoUpdateEb(
    QDeclarativeGeoRouteModel *self,
    bool autoUpdate) {
  self->setAutoUpdate(autoUpdate);
}

//  bool QDeclarativeGeoRouteModel::autoUpdate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QDeclarativeGeoRouteModel10autoUpdateEv(
    const QDeclarativeGeoRouteModel *self) {
  return self->autoUpdate();
}

//  void QDeclarativeGeoRouteModel::setMeasurementSystem(QLocale::Measurement
//      System ms)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel20setMeasurementSystemEN7QLocale17MeasurementSystemE(
    QDeclarativeGeoRouteModel *self,
    QLocale::MeasurementSystem ms) {
  self->setMeasurementSystem(ms);
}

//  QLocale::MeasurementSystem QDeclarativeGeoRouteModel::measurementSystem()
//      const
extern "C" Q_DECL_EXPORT
QLocale::MeasurementSystem ritual_ZNK25QDeclarativeGeoRouteModel17measurementSystemEv(
    const QDeclarativeGeoRouteModel *self) {
  return self->measurementSystem();
}

//  Status QDeclarativeGeoRouteModel::status() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoRouteModel::Status ritual_ZNK25QDeclarativeGeoRouteModel6statusEv(
    const QDeclarativeGeoRouteModel *self) {
  return self->status();
}

//  QString QDeclarativeGeoRouteModel::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QDeclarativeGeoRouteModel11errorStringEv(
    const QDeclarativeGeoRouteModel *self) {
  return new QString(self->errorString());
}

//  RouteError QDeclarativeGeoRouteModel::error() const
extern "C" Q_DECL_EXPORT
QDeclarativeGeoRouteModel::RouteError ritual_ZNK25QDeclarativeGeoRouteModel5errorEv(
    const QDeclarativeGeoRouteModel *self) {
  return self->error();
}

//  int QDeclarativeGeoRouteModel::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QDeclarativeGeoRouteModel5countEv(
    const QDeclarativeGeoRouteModel *self) {
  return self->count();
}

//  QGeoRoute QDeclarativeGeoRouteModel::get(int index)
extern "C" Q_DECL_EXPORT
QGeoRoute *ritual_ZN25QDeclarativeGeoRouteModel3getEi(
    QDeclarativeGeoRouteModel *self,
    int index) {
  return new QGeoRoute(self->get(index));
}

//  void QDeclarativeGeoRouteModel::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel5resetEv(
    QDeclarativeGeoRouteModel *self) {
  self->reset();
}

//  void QDeclarativeGeoRouteModel::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel6cancelEv(
    QDeclarativeGeoRouteModel *self) {
  self->cancel();
}

//  void QDeclarativeGeoRouteModel::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel6updateEv(
    QDeclarativeGeoRouteModel *self) {
  self->update();
}

//  void QDeclarativeGeoRouteModel::routingFinished(QGeoRouteReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel15routingFinishedEP14QGeoRouteReply(
    QDeclarativeGeoRouteModel *self,
    QGeoRouteReply *reply) {
  self->routingFinished(reply);
}

//  void QDeclarativeGeoRouteModel::routingError(QGeoRouteReply *reply,
//      QGeoRouteReply::Error error, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel12routingErrorEP14QGeoRouteReplyNS0_5ErrorERK7QString(
    QDeclarativeGeoRouteModel *self,
    QGeoRouteReply *reply,
    QGeoRouteReply::Error error,
    const QString *errorString) {
  self->routingError(reply, error, *errorString);
}

//  void QDeclarativeGeoRouteModel::queryDetailsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel19queryDetailsChangedEv(
    QDeclarativeGeoRouteModel *self) {
  self->queryDetailsChanged();
}

//  void QDeclarativeGeoRouteModel::pluginReady()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel11pluginReadyEv(
    QDeclarativeGeoRouteModel *self) {
  self->pluginReady();
}

//  void QDeclarativeGeoRouteModel::setStatus(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel9setStatusENS_6StatusE(
    QDeclarativeGeoRouteModel *self,
    QDeclarativeGeoRouteModel::Status status) {
  self->setStatus(status);
}

//  void QDeclarativeGeoRouteModel::setError(RouteError error, const QString
//      &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDeclarativeGeoRouteModel8setErrorENS_10RouteErrorERK7QString(
    QDeclarativeGeoRouteModel *self,
    QDeclarativeGeoRouteModel::RouteError error,
    const QString *errorString) {
  self->setError(error, *errorString);
}

//  QDeclarativeGeoRouteModel as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QDeclarativeGeoRouteModel_QQmlParserStatus(
    QDeclarativeGeoRouteModel *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QDeclarativeGeoRouteModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QDeclarativeGeoRouteModel10classBeginEv(
    QDeclarativeGeoRouteModel *self) {
  self->QDeclarativeGeoRouteModel::classBegin();
}

//  void QDeclarativeGeoRouteModel::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QDeclarativeGeoRouteModel17componentCompleteEv(
    QDeclarativeGeoRouteModel *self) {
  self->QDeclarativeGeoRouteModel::componentComplete();
}

//  int QDeclarativeGeoRouteModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK25QDeclarativeGeoRouteModel8rowCountERK11QModelIndex(
    const QDeclarativeGeoRouteModel *self,
    const QModelIndex *parent) {
  return self->QDeclarativeGeoRouteModel::rowCount(*parent);
}

//  QVariant QDeclarativeGeoRouteModel::data(const QModelIndex &index, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QDeclarativeGeoRouteModel4dataERK11QModelIndexi(
    const QDeclarativeGeoRouteModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QDeclarativeGeoRouteModel::data(*index, role));
}

//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginehistory.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWebEngineCore/qwebenginehistory.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  const QMetaObject *QWebEngineHistoryModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QWebEngineHistoryModel10metaObjectEv(
    const QWebEngineHistoryModel *self) {
  return self->metaObject();
}

//  void *QWebEngineHistoryModel::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QWebEngineHistoryModel11qt_metacastEPKc(
    QWebEngineHistoryModel *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineHistoryModel::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QWebEngineHistoryModel11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineHistoryModel *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineHistoryModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QWebEngineHistoryModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineHistoryModel::tr(s, c, n));
}

//  int QWebEngineHistoryModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QWebEngineHistoryModel8rowCountERK11QModelIndex(
    const QWebEngineHistoryModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QVariant QWebEngineHistoryModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK22QWebEngineHistoryModel4dataERK11QModelIndexi(
    const QWebEngineHistoryModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  QHash<int, QByteArray> QWebEngineHistoryModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK22QWebEngineHistoryModel9roleNamesEv(
    const QWebEngineHistoryModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  void QWebEngineHistoryModel::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWebEngineHistoryModel5resetEv(
    QWebEngineHistoryModel *self) {
  self->reset();
}

//  QWebEngineHistoryModel::QWebEngineHistoryModel(QWebEngineHistoryModelPriv
//      ate *a0)
extern "C" Q_DECL_EXPORT
QWebEngineHistoryModel *ritual_ZN22QWebEngineHistoryModelC1EP29QWebEngineHistoryModelPrivate(
    QWebEngineHistoryModelPrivate *a0) {
  return new QWebEngineHistoryModel(a0);
}

//  QWebEngineHistoryModel::~QWebEngineHistoryModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWebEngineHistoryModelD1Ev(QWebEngineHistoryModel *self) {
  delete self;
}

//  QWebEngineHistoryModelPrivate *QWebEngineHistoryModel::d_func()
extern "C" Q_DECL_EXPORT
QWebEngineHistoryModelPrivate *ritual_ZN22QWebEngineHistoryModel6d_funcEv(
    QWebEngineHistoryModel *self) {
  return self->d_func();
}

//  const QWebEngineHistoryModelPrivate *QWebEngineHistoryModel::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QWebEngineHistoryModelPrivate *ritual_ZNK22QWebEngineHistoryModel6d_funcEv(
    const QWebEngineHistoryModel *self) {
  return self->d_func();
}

//  int QWebEngineHistoryModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK22QWebEngineHistoryModel8rowCountERK11QModelIndex(
    const QWebEngineHistoryModel *self,
    const QModelIndex *parent) {
  return self->QWebEngineHistoryModel::rowCount(*parent);
}

//  QVariant QWebEngineHistoryModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK22QWebEngineHistoryModel4dataERK11QModelIndexi(
    const QWebEngineHistoryModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QWebEngineHistoryModel::data(*index, role));
}

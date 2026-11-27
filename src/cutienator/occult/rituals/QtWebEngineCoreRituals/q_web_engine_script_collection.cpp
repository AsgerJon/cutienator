//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginescriptcollection.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWebEngineCore/qwebenginescriptcollection.h>
#include <QtWebEngineCore/qwebenginescript.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QWebEngineScriptCollection::~QWebEngineScriptCollection()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineScriptCollectionD1Ev(
    QWebEngineScriptCollection *self) {
  delete self;
}

//  bool QWebEngineScriptCollection::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QWebEngineScriptCollection7isEmptyEv(
    const QWebEngineScriptCollection *self) {
  return self->isEmpty();
}

//  int QWebEngineScriptCollection::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QWebEngineScriptCollection5countEv(
    const QWebEngineScriptCollection *self) {
  return self->count();
}

//  bool QWebEngineScriptCollection::contains(const QWebEngineScript &value)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QWebEngineScriptCollection8containsERK16QWebEngineScript(
    const QWebEngineScriptCollection *self,
    const QWebEngineScript *value) {
  return self->contains(*value);
}

//  QList<QWebEngineScript> QWebEngineScriptCollection::find(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
QList<QWebEngineScript> *ritual_ZNK26QWebEngineScriptCollection4findERK7QString(
    const QWebEngineScriptCollection *self,
    const QString *name) {
  return new QList<QWebEngineScript>(self->find(*name));
}

//  void QWebEngineScriptCollection::insert(const QWebEngineScript &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineScriptCollection6insertERK16QWebEngineScript(
    QWebEngineScriptCollection *self,
    const QWebEngineScript *a0) {
  self->insert(*a0);
}

//  void QWebEngineScriptCollection::insert(const QList<QWebEngineScript>
//      &list)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineScriptCollection6insertERK5QListI16QWebEngineScriptE(
    QWebEngineScriptCollection *self,
    const QList<QWebEngineScript> *list) {
  self->insert(*list);
}

//  bool QWebEngineScriptCollection::remove(const QWebEngineScript &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QWebEngineScriptCollection6removeERK16QWebEngineScript(
    QWebEngineScriptCollection *self,
    const QWebEngineScript *a0) {
  return self->remove(*a0);
}

//  void QWebEngineScriptCollection::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWebEngineScriptCollection5clearEv(
    QWebEngineScriptCollection *self) {
  self->clear();
}

//  QList<QWebEngineScript> QWebEngineScriptCollection::toList() const
extern "C" Q_DECL_EXPORT
QList<QWebEngineScript> *ritual_ZNK26QWebEngineScriptCollection6toListEv(
    const QWebEngineScriptCollection *self) {
  return new QList<QWebEngineScript>(self->toList());
}

//  QWebEngineScriptCollection::QWebEngineScriptCollection(QWebEngineScriptCo
//      llectionPrivate *a0)
extern "C" Q_DECL_EXPORT
QWebEngineScriptCollection *ritual_ZN26QWebEngineScriptCollectionC1EP33QWebEngineScriptCollectionPrivate(
    QWebEngineScriptCollectionPrivate *a0) {
  return new QWebEngineScriptCollection(a0);
}

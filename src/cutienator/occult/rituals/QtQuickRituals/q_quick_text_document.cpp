//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquicktextdocument.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qquicktextdocument.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>

//  const QMetaObject *QQuickTextDocument::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickTextDocument10metaObjectEv(
    const QQuickTextDocument *self) {
  return self->metaObject();
}

//  void *QQuickTextDocument::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickTextDocument11qt_metacastEPKc(
    QQuickTextDocument *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTextDocument::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickTextDocument11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTextDocument *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTextDocument::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickTextDocument2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTextDocument::tr(s, c, n));
}

//  void QQuickTextDocument::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTextDocument24qt_qmlMarker_uncreatableEv(
    QQuickTextDocument *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickTextDocument::QQuickTextDocument(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTextDocument *ritual_ZN18QQuickTextDocumentC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickTextDocument(parent);
}

//  QUrl QQuickTextDocument::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QQuickTextDocument6sourceEv(
    const QQuickTextDocument *self) {
  return new QUrl(self->source());
}

//  void QQuickTextDocument::setSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTextDocument9setSourceERK4QUrl(
    QQuickTextDocument *self,
    const QUrl *url) {
  self->setSource(*url);
}

//  bool QQuickTextDocument::isModified() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickTextDocument10isModifiedEv(
    const QQuickTextDocument *self) {
  return self->isModified();
}

//  void QQuickTextDocument::setModified(bool modified)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTextDocument11setModifiedEb(
    QQuickTextDocument *self,
    bool modified) {
  self->setModified(modified);
}

//  QTextDocument *QQuickTextDocument::textDocument() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK18QQuickTextDocument12textDocumentEv(
    const QQuickTextDocument *self) {
  return self->textDocument();
}

//  void QQuickTextDocument::setTextDocument(QTextDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTextDocument15setTextDocumentEP13QTextDocument(
    QQuickTextDocument *self,
    QTextDocument *document) {
  self->setTextDocument(document);
}

//  void QQuickTextDocument::save()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTextDocument4saveEv(QQuickTextDocument *self) {
  self->save();
}

//  void QQuickTextDocument::saveAs(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTextDocument6saveAsERK4QUrl(
    QQuickTextDocument *self,
    const QUrl *url) {
  self->saveAs(*url);
}

//  Status QQuickTextDocument::status() const
extern "C" Q_DECL_EXPORT
QQuickTextDocument::Status ritual_ZNK18QQuickTextDocument6statusEv(
    const QQuickTextDocument *self) {
  return self->status();
}

//  QString QQuickTextDocument::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QQuickTextDocument11errorStringEv(
    const QQuickTextDocument *self) {
  return new QString(self->errorString());
}

//  void QQuickTextDocument::textDocumentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTextDocument19textDocumentChangedEv(
    QQuickTextDocument *self) {
  self->textDocumentChanged();
}

//  void QQuickTextDocument::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTextDocument13sourceChangedEv(
    QQuickTextDocument *self) {
  self->sourceChanged();
}

//  void QQuickTextDocument::modifiedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTextDocument15modifiedChangedEv(
    QQuickTextDocument *self) {
  self->modifiedChanged();
}

//  void QQuickTextDocument::statusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTextDocument13statusChangedEv(
    QQuickTextDocument *self) {
  self->statusChanged();
}

//  void QQuickTextDocument::errorStringChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickTextDocument18errorStringChangedEv(
    QQuickTextDocument *self) {
  self->errorStringChanged();
}

//  QQuickTextDocumentPrivate *QQuickTextDocument::d_func()
extern "C" Q_DECL_EXPORT
QQuickTextDocumentPrivate *ritual_ZN18QQuickTextDocument6d_funcEv(
    QQuickTextDocument *self) {
  return self->d_func();
}

//  const QQuickTextDocumentPrivate *QQuickTextDocument::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTextDocumentPrivate *ritual_ZNK18QQuickTextDocument6d_funcEv(
    const QQuickTextDocument *self) {
  return self->d_func();
}

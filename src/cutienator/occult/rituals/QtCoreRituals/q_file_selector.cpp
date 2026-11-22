//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfileselector.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qfileselector.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>

//  const QMetaObject *QFileSelector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QFileSelector10metaObjectEv(
    const QFileSelector *self) {
  return self->metaObject();
}

//  QString QFileSelector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QFileSelector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFileSelector::tr(s, c, n));
}

//  QFileSelector::QFileSelector(QObject *parent)
extern "C" Q_DECL_EXPORT
QFileSelector *ritual_ZN13QFileSelectorC1EP7QObject(QObject *parent) {
  return new QFileSelector(parent);
}

//  QFileSelector::~QFileSelector()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFileSelectorD1Ev(QFileSelector *self) {
  delete self;
}

//  QString QFileSelector::select(const QString &filePath) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QFileSelector6selectERK7QString(
    const QFileSelector *self,
    const QString *filePath) {
  return new QString(self->select(*filePath));
}

//  QUrl QFileSelector::select(const QUrl &filePath) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13QFileSelector6selectERK4QUrl(
    const QFileSelector *self,
    const QUrl *filePath) {
  return new QUrl(self->select(*filePath));
}

//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qtresourcemodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qtresourcemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QStringList QtResourceSet::activeResourceFilePaths() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK13QtResourceSet23activeResourceFilePathsEv(
    const QtResourceSet *self) {
  return new QList<QString>(self->activeResourceFilePaths());
}

//  void QtResourceSet::activateResourceFilePaths(const QStringList &paths,
//      int *errorCount, QString *errorMessages)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QtResourceSet25activateResourceFilePathsERK5QListI7QStringEPiPS1_(
    QtResourceSet *self,
    const QList<QString> *paths,
    int *errorCount,
    QString *errorMessages) {
  self->activateResourceFilePaths(*paths, errorCount, errorMessages);
}

//  bool QtResourceSet::isModified(const QString &path) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QtResourceSet10isModifiedERK7QString(
    const QtResourceSet *self,
    const QString *path) {
  return self->isModified(*path);
}

//  void QtResourceSet::setModified(const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QtResourceSet11setModifiedERK7QString(
    QtResourceSet *self,
    const QString *path) {
  self->setModified(*path);
}

//  QtResourceSet::QtResourceSet()
extern "C" Q_DECL_EXPORT
QtResourceSet *ritual_ZN13QtResourceSetC1Ev() {
  return new QtResourceSet();
}

//  QtResourceSet::QtResourceSet(QtResourceModel *model)
extern "C" Q_DECL_EXPORT
QtResourceSet *ritual_ZN13QtResourceSetC1EP15QtResourceModel(
    QtResourceModel *model) {
  return new QtResourceSet(model);
}

//  QtResourceSet::~QtResourceSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QtResourceSetD1Ev(QtResourceSet *self) {
  delete self;
}

//  QList<QtResourceSet *>::QList()
extern "C" Q_DECL_EXPORT
QList<QtResourceSet *> *ritual_list_make_QtResourceSet_ptr() {
  return new QList<QtResourceSet *>();
}

//  void QList<QtResourceSet *>::append(const QtResourceSet * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QtResourceSet_ptr(
    QList<QtResourceSet *> *self,
    QtResourceSet *element) {
  self->append(element);
}

//  qsizetype QList<QtResourceSet *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QtResourceSet_ptr(
    const QList<QtResourceSet *> *self) {
  return self->size();
}

//  const QtResourceSet * &QList<QtResourceSet *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QtResourceSet *ritual_list_at_QtResourceSet_ptr(
    const QList<QtResourceSet *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QtResourceSet *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QtResourceSet_ptr(QList<QtResourceSet *> *self) {
  delete self;
}

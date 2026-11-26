//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QPlatformFileDialogHelper::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QPlatformFileDialogHelper10metaObjectEv(
    const QPlatformFileDialogHelper *self) {
  return self->metaObject();
}

//  void *QPlatformFileDialogHelper::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QPlatformFileDialogHelper11qt_metacastEPKc(
    QPlatformFileDialogHelper *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformFileDialogHelper::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QPlatformFileDialogHelper11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformFileDialogHelper *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformFileDialogHelper::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QPlatformFileDialogHelper2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformFileDialogHelper::tr(s, c, n));
}

//  bool QPlatformFileDialogHelper::defaultNameFilterDisables() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QPlatformFileDialogHelper25defaultNameFilterDisablesEv(
    const QPlatformFileDialogHelper *self) {
  return self->defaultNameFilterDisables();
}

//  void QPlatformFileDialogHelper::setDirectory(const QUrl &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFileDialogHelper12setDirectoryERK4QUrl(
    QPlatformFileDialogHelper *self,
    const QUrl *directory) {
  self->setDirectory(*directory);
}

//  QUrl QPlatformFileDialogHelper::directory() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK25QPlatformFileDialogHelper9directoryEv(
    const QPlatformFileDialogHelper *self) {
  return new QUrl(self->directory());
}

//  void QPlatformFileDialogHelper::selectFile(const QUrl &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFileDialogHelper10selectFileERK4QUrl(
    QPlatformFileDialogHelper *self,
    const QUrl *filename) {
  self->selectFile(*filename);
}

//  QList<QUrl> QPlatformFileDialogHelper::selectedFiles() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK25QPlatformFileDialogHelper13selectedFilesEv(
    const QPlatformFileDialogHelper *self) {
  return new QList<QUrl>(self->selectedFiles());
}

//  void QPlatformFileDialogHelper::setFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFileDialogHelper9setFilterEv(
    QPlatformFileDialogHelper *self) {
  self->setFilter();
}

//  void QPlatformFileDialogHelper::selectMimeTypeFilter(const QString
//      &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFileDialogHelper20selectMimeTypeFilterERK7QString(
    QPlatformFileDialogHelper *self,
    const QString *filter) {
  self->selectMimeTypeFilter(*filter);
}

//  void QPlatformFileDialogHelper::selectNameFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFileDialogHelper16selectNameFilterERK7QString(
    QPlatformFileDialogHelper *self,
    const QString *filter) {
  self->selectNameFilter(*filter);
}

//  QString QPlatformFileDialogHelper::selectedMimeTypeFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QPlatformFileDialogHelper22selectedMimeTypeFilterEv(
    const QPlatformFileDialogHelper *self) {
  return new QString(self->selectedMimeTypeFilter());
}

//  QString QPlatformFileDialogHelper::selectedNameFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QPlatformFileDialogHelper18selectedNameFilterEv(
    const QPlatformFileDialogHelper *self) {
  return new QString(self->selectedNameFilter());
}

//  bool QPlatformFileDialogHelper::isSupportedUrl(const QUrl &url) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QPlatformFileDialogHelper14isSupportedUrlERK4QUrl(
    const QPlatformFileDialogHelper *self,
    const QUrl *url) {
  return self->isSupportedUrl(*url);
}

//  const QSharedPointer<QFileDialogOptions>
//      &QPlatformFileDialogHelper::options() const
extern "C" Q_DECL_EXPORT
const QSharedPointer<QFileDialogOptions> *ritual_ZNK25QPlatformFileDialogHelper7optionsEv(
    const QPlatformFileDialogHelper *self) {
  return &(self->options());
}

//  void QPlatformFileDialogHelper::setOptions(const
//      QSharedPointer<QFileDialogOptions> &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFileDialogHelper10setOptionsERK14QSharedPointerI18QFileDialogOptionsE(
    QPlatformFileDialogHelper *self,
    const QSharedPointer<QFileDialogOptions> *options) {
  self->setOptions(*options);
}

//  QStringList QPlatformFileDialogHelper::cleanFilterList(const QString
//      &filter)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN25QPlatformFileDialogHelper15cleanFilterListERK7QString(
    const QString *filter) {
  return new QList<QString>(
      QPlatformFileDialogHelper::cleanFilterList(
          *filter));
}

//  void QPlatformFileDialogHelper::fileSelected(const QUrl &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFileDialogHelper12fileSelectedERK4QUrl(
    QPlatformFileDialogHelper *self,
    const QUrl *file) {
  self->fileSelected(*file);
}

//  void QPlatformFileDialogHelper::filesSelected(const QList<QUrl> &files)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFileDialogHelper13filesSelectedERK5QListI4QUrlE(
    QPlatformFileDialogHelper *self,
    const QList<QUrl> *files) {
  self->filesSelected(*files);
}

//  void QPlatformFileDialogHelper::currentChanged(const QUrl &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFileDialogHelper14currentChangedERK4QUrl(
    QPlatformFileDialogHelper *self,
    const QUrl *path) {
  self->currentChanged(*path);
}

//  void QPlatformFileDialogHelper::directoryEntered(const QUrl &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFileDialogHelper16directoryEnteredERK4QUrl(
    QPlatformFileDialogHelper *self,
    const QUrl *directory) {
  self->directoryEntered(*directory);
}

//  void QPlatformFileDialogHelper::filterSelected(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QPlatformFileDialogHelper14filterSelectedERK7QString(
    QPlatformFileDialogHelper *self,
    const QString *filter) {
  self->filterSelected(*filter);
}

//  void QPlatformFileDialogHelper::selectMimeTypeFilter(const QString
//      &filter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QPlatformFileDialogHelper20selectMimeTypeFilterERK7QString(
    QPlatformFileDialogHelper *self,
    const QString *filter) {
  self->QPlatformFileDialogHelper::selectMimeTypeFilter(*filter);
}

//  QString QPlatformFileDialogHelper::selectedMimeTypeFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK25QPlatformFileDialogHelper22selectedMimeTypeFilterEv(
    const QPlatformFileDialogHelper *self) {
  return new QString(
      self->QPlatformFileDialogHelper::selectedMimeTypeFilter());
}

//  bool QPlatformFileDialogHelper::isSupportedUrl(const QUrl &url) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK25QPlatformFileDialogHelper14isSupportedUrlERK4QUrl(
    const QPlatformFileDialogHelper *self,
    const QUrl *url) {
  return self->QPlatformFileDialogHelper::isSupportedUrl(*url);
}

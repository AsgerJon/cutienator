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

//  QFileDialogOptions::~QFileDialogOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptionsD1Ev(QFileDialogOptions *self) {
  delete self;
}

//  QString QFileDialogOptions::windowTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QFileDialogOptions11windowTitleEv(
    const QFileDialogOptions *self) {
  return new QString(self->windowTitle());
}

//  void QFileDialogOptions::setWindowTitle(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions14setWindowTitleERK7QString(
    QFileDialogOptions *self,
    const QString *a0) {
  self->setWindowTitle(*a0);
}

//  void QFileDialogOptions::setOption(FileDialogOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions9setOptionENS_16FileDialogOptionEb(
    QFileDialogOptions *self,
    QFileDialogOptions::FileDialogOption option,
    bool on) {
  self->setOption(option, on);
}

//  bool QFileDialogOptions::testOption(FileDialogOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFileDialogOptions10testOptionENS_16FileDialogOptionE(
    const QFileDialogOptions *self,
    QFileDialogOptions::FileDialogOption option) {
  return self->testOption(option);
}

//  void QFileDialogOptions::setOptions(FileDialogOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions10setOptionsE6QFlagsINS_16FileDialogOptionEE(
    QFileDialogOptions *self,
    int options) {
  self->setOptions(
      QFlags<QFileDialogOptions::FileDialogOption>::fromInt(options));
}

//  FileDialogOptions QFileDialogOptions::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QFileDialogOptions7optionsEv(
    const QFileDialogOptions *self) {
  return static_cast<int>(self->options().toInt());
}

//  QDir::Filters QFileDialogOptions::filter() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QFileDialogOptions6filterEv(const QFileDialogOptions *self) {
  return static_cast<int>(self->filter().toInt());
}

//  void QFileDialogOptions::setFilter(QDir::Filters filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions9setFilterE6QFlagsIN4QDir6FilterEE(
    QFileDialogOptions *self,
    int filters) {
  self->setFilter(QFlags<QDir::Filter>::fromInt(filters));
}

//  void QFileDialogOptions::setViewMode(ViewMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions11setViewModeENS_8ViewModeE(
    QFileDialogOptions *self,
    QFileDialogOptions::ViewMode mode) {
  self->setViewMode(mode);
}

//  ViewMode QFileDialogOptions::viewMode() const
extern "C" Q_DECL_EXPORT
QFileDialogOptions::ViewMode ritual_ZNK18QFileDialogOptions8viewModeEv(
    const QFileDialogOptions *self) {
  return self->viewMode();
}

//  void QFileDialogOptions::setFileMode(FileMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions11setFileModeENS_8FileModeE(
    QFileDialogOptions *self,
    QFileDialogOptions::FileMode mode) {
  self->setFileMode(mode);
}

//  FileMode QFileDialogOptions::fileMode() const
extern "C" Q_DECL_EXPORT
QFileDialogOptions::FileMode ritual_ZNK18QFileDialogOptions8fileModeEv(
    const QFileDialogOptions *self) {
  return self->fileMode();
}

//  void QFileDialogOptions::setAcceptMode(AcceptMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions13setAcceptModeENS_10AcceptModeE(
    QFileDialogOptions *self,
    QFileDialogOptions::AcceptMode mode) {
  self->setAcceptMode(mode);
}

//  AcceptMode QFileDialogOptions::acceptMode() const
extern "C" Q_DECL_EXPORT
QFileDialogOptions::AcceptMode ritual_ZNK18QFileDialogOptions10acceptModeEv(
    const QFileDialogOptions *self) {
  return self->acceptMode();
}

//  void QFileDialogOptions::setSidebarUrls(const QList<QUrl> &urls)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions14setSidebarUrlsERK5QListI4QUrlE(
    QFileDialogOptions *self,
    const QList<QUrl> *urls) {
  self->setSidebarUrls(*urls);
}

//  QList<QUrl> QFileDialogOptions::sidebarUrls() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK18QFileDialogOptions11sidebarUrlsEv(
    const QFileDialogOptions *self) {
  return new QList<QUrl>(self->sidebarUrls());
}

//  bool QFileDialogOptions::useDefaultNameFilters() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFileDialogOptions21useDefaultNameFiltersEv(
    const QFileDialogOptions *self) {
  return self->useDefaultNameFilters();
}

//  void QFileDialogOptions::setUseDefaultNameFilters(bool d)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions24setUseDefaultNameFiltersEb(
    QFileDialogOptions *self,
    bool d) {
  self->setUseDefaultNameFilters(d);
}

//  void QFileDialogOptions::setNameFilters(const QStringList &filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions14setNameFiltersERK5QListI7QStringE(
    QFileDialogOptions *self,
    const QList<QString> *filters) {
  self->setNameFilters(*filters);
}

//  QStringList QFileDialogOptions::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QFileDialogOptions11nameFiltersEv(
    const QFileDialogOptions *self) {
  return new QList<QString>(self->nameFilters());
}

//  void QFileDialogOptions::setMimeTypeFilters(const QStringList &filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions18setMimeTypeFiltersERK5QListI7QStringE(
    QFileDialogOptions *self,
    const QList<QString> *filters) {
  self->setMimeTypeFilters(*filters);
}

//  QStringList QFileDialogOptions::mimeTypeFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QFileDialogOptions15mimeTypeFiltersEv(
    const QFileDialogOptions *self) {
  return new QList<QString>(self->mimeTypeFilters());
}

//  void QFileDialogOptions::setDefaultSuffix(const QString &suffix)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions16setDefaultSuffixERK7QString(
    QFileDialogOptions *self,
    const QString *suffix) {
  self->setDefaultSuffix(*suffix);
}

//  QString QFileDialogOptions::defaultSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QFileDialogOptions13defaultSuffixEv(
    const QFileDialogOptions *self) {
  return new QString(self->defaultSuffix());
}

//  void QFileDialogOptions::setHistory(const QStringList &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions10setHistoryERK5QListI7QStringE(
    QFileDialogOptions *self,
    const QList<QString> *paths) {
  self->setHistory(*paths);
}

//  QStringList QFileDialogOptions::history() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QFileDialogOptions7historyEv(
    const QFileDialogOptions *self) {
  return new QList<QString>(self->history());
}

//  void QFileDialogOptions::setLabelText(DialogLabel label, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions12setLabelTextENS_11DialogLabelERK7QString(
    QFileDialogOptions *self,
    QFileDialogOptions::DialogLabel label,
    const QString *text) {
  self->setLabelText(label, *text);
}

//  QString QFileDialogOptions::labelText(DialogLabel label) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QFileDialogOptions9labelTextENS_11DialogLabelE(
    const QFileDialogOptions *self,
    QFileDialogOptions::DialogLabel label) {
  return new QString(self->labelText(label));
}

//  bool QFileDialogOptions::isLabelExplicitlySet(DialogLabel label)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFileDialogOptions20isLabelExplicitlySetENS_11DialogLabelE(
    QFileDialogOptions *self,
    QFileDialogOptions::DialogLabel label) {
  return self->isLabelExplicitlySet(label);
}

//  QUrl QFileDialogOptions::initialDirectory() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QFileDialogOptions16initialDirectoryEv(
    const QFileDialogOptions *self) {
  return new QUrl(self->initialDirectory());
}

//  void QFileDialogOptions::setInitialDirectory(const QUrl &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions19setInitialDirectoryERK4QUrl(
    QFileDialogOptions *self,
    const QUrl *a0) {
  self->setInitialDirectory(*a0);
}

//  QString QFileDialogOptions::initiallySelectedMimeTypeFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QFileDialogOptions31initiallySelectedMimeTypeFilterEv(
    const QFileDialogOptions *self) {
  return new QString(self->initiallySelectedMimeTypeFilter());
}

//  void QFileDialogOptions::setInitiallySelectedMimeTypeFilter(const QString
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions34setInitiallySelectedMimeTypeFilterERK7QString(
    QFileDialogOptions *self,
    const QString *a0) {
  self->setInitiallySelectedMimeTypeFilter(*a0);
}

//  QString QFileDialogOptions::initiallySelectedNameFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QFileDialogOptions27initiallySelectedNameFilterEv(
    const QFileDialogOptions *self) {
  return new QString(self->initiallySelectedNameFilter());
}

//  void QFileDialogOptions::setInitiallySelectedNameFilter(const QString
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions30setInitiallySelectedNameFilterERK7QString(
    QFileDialogOptions *self,
    const QString *a0) {
  self->setInitiallySelectedNameFilter(*a0);
}

//  QList<QUrl> QFileDialogOptions::initiallySelectedFiles() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK18QFileDialogOptions22initiallySelectedFilesEv(
    const QFileDialogOptions *self) {
  return new QList<QUrl>(self->initiallySelectedFiles());
}

//  void QFileDialogOptions::setInitiallySelectedFiles(const QList<QUrl> &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions25setInitiallySelectedFilesERK5QListI4QUrlE(
    QFileDialogOptions *self,
    const QList<QUrl> *a0) {
  self->setInitiallySelectedFiles(*a0);
}

//  void QFileDialogOptions::setSupportedSchemes(const QStringList &schemes)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogOptions19setSupportedSchemesERK5QListI7QStringE(
    QFileDialogOptions *self,
    const QList<QString> *schemes) {
  self->setSupportedSchemes(*schemes);
}

//  QStringList QFileDialogOptions::supportedSchemes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QFileDialogOptions16supportedSchemesEv(
    const QFileDialogOptions *self) {
  return new QList<QString>(self->supportedSchemes());
}

//  QString QFileDialogOptions::defaultNameFilterString()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QFileDialogOptions23defaultNameFilterStringEv() {
  return new QString(QFileDialogOptions::defaultNameFilterString());
}

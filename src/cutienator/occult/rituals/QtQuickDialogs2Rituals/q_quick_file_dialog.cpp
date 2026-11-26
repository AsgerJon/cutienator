//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickfiledialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qtquickdialogs2global_p.h>
#include <QtQuickDialogs2/QtQuickDialogs2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickfiledialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>

//  Only a class built on QQuickFileDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFileDialog : QQuickFileDialog {
  using QQuickFileDialog::useNativeDialog;
  using QQuickFileDialog::onCreate;
  using QQuickFileDialog::onShow;
  using QQuickFileDialog::onHide;
  using QQuickFileDialog::accept;
};

//  const QMetaObject *QQuickFileDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickFileDialog10metaObjectEv(
    const QQuickFileDialog *self) {
  return self->metaObject();
}

//  void *QQuickFileDialog::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuickFileDialog11qt_metacastEPKc(
    QQuickFileDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFileDialog::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuickFileDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFileDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFileDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickFileDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFileDialog::tr(s, c, n));
}

//  const QMetaObject *QQuickFileDialog::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN16QQuickFileDialog20qmlExtendedNamespaceEv() {
  return QQuickFileDialog::qmlExtendedNamespace();
}

//  void QQuickFileDialog::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog30qt_qmlMarker_extendedNamespaceEv(
    QQuickFileDialog *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QQuickFileDialog::QQuickFileDialog(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickFileDialog *ritual_ZN16QQuickFileDialogC1EP7QObject(QObject *parent) {
  return new QQuickFileDialog(parent);
}

//  FileMode QQuickFileDialog::fileMode() const
extern "C" Q_DECL_EXPORT
QQuickFileDialog::FileMode ritual_ZNK16QQuickFileDialog8fileModeEv(
    const QQuickFileDialog *self) {
  return self->fileMode();
}

//  void QQuickFileDialog::setFileMode(FileMode fileMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog11setFileModeENS_8FileModeE(
    QQuickFileDialog *self,
    QQuickFileDialog::FileMode fileMode) {
  self->setFileMode(fileMode);
}

//  QUrl QQuickFileDialog::selectedFile() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QQuickFileDialog12selectedFileEv(
    const QQuickFileDialog *self) {
  return new QUrl(self->selectedFile());
}

//  void QQuickFileDialog::setSelectedFile(const QUrl &selectedFile)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog15setSelectedFileERK4QUrl(
    QQuickFileDialog *self,
    const QUrl *selectedFile) {
  self->setSelectedFile(*selectedFile);
}

//  QList<QUrl> QQuickFileDialog::selectedFiles() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK16QQuickFileDialog13selectedFilesEv(
    const QQuickFileDialog *self) {
  return new QList<QUrl>(self->selectedFiles());
}

//  QUrl QQuickFileDialog::currentFile() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QQuickFileDialog11currentFileEv(
    const QQuickFileDialog *self) {
  return new QUrl(self->currentFile());
}

//  void QQuickFileDialog::setCurrentFile(const QUrl &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog14setCurrentFileERK4QUrl(
    QQuickFileDialog *self,
    const QUrl *file) {
  self->setCurrentFile(*file);
}

//  QList<QUrl> QQuickFileDialog::currentFiles() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK16QQuickFileDialog12currentFilesEv(
    const QQuickFileDialog *self) {
  return new QList<QUrl>(self->currentFiles());
}

//  void QQuickFileDialog::setCurrentFiles(const QList<QUrl> &currentFiles)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog15setCurrentFilesERK5QListI4QUrlE(
    QQuickFileDialog *self,
    const QList<QUrl> *currentFiles) {
  self->setCurrentFiles(*currentFiles);
}

//  QUrl QQuickFileDialog::currentFolder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QQuickFileDialog13currentFolderEv(
    const QQuickFileDialog *self) {
  return new QUrl(self->currentFolder());
}

//  void QQuickFileDialog::setCurrentFolder(const QUrl &currentFolder)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog16setCurrentFolderERK4QUrl(
    QQuickFileDialog *self,
    const QUrl *currentFolder) {
  self->setCurrentFolder(*currentFolder);
}

//  QFileDialogOptions::FileDialogOptions QQuickFileDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickFileDialog7optionsEv(const QQuickFileDialog *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QQuickFileDialog::setOptions(QFileDialogOptions::FileDialogOptions
//      options)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog10setOptionsE6QFlagsIN18QFileDialogOptions16FileDialogOptionEE(
    QQuickFileDialog *self,
    int options) {
  self->setOptions(
      QFlags<QFileDialogOptions::FileDialogOption>::fromInt(options));
}

//  void QQuickFileDialog::resetOptions()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog12resetOptionsEv(QQuickFileDialog *self) {
  self->resetOptions();
}

//  QStringList QQuickFileDialog::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16QQuickFileDialog11nameFiltersEv(
    const QQuickFileDialog *self) {
  return new QList<QString>(self->nameFilters());
}

//  void QQuickFileDialog::setNameFilters(const QStringList &filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog14setNameFiltersERK5QListI7QStringE(
    QQuickFileDialog *self,
    const QList<QString> *filters) {
  self->setNameFilters(*filters);
}

//  void QQuickFileDialog::resetNameFilters()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog16resetNameFiltersEv(
    QQuickFileDialog *self) {
  self->resetNameFilters();
}

//  QQuickFileNameFilter *QQuickFileDialog::selectedNameFilter() const
extern "C" Q_DECL_EXPORT
QQuickFileNameFilter *ritual_ZNK16QQuickFileDialog18selectedNameFilterEv(
    const QQuickFileDialog *self) {
  return self->selectedNameFilter();
}

//  QString QQuickFileDialog::defaultSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQuickFileDialog13defaultSuffixEv(
    const QQuickFileDialog *self) {
  return new QString(self->defaultSuffix());
}

//  void QQuickFileDialog::setDefaultSuffix(const QString &suffix)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog16setDefaultSuffixERK7QString(
    QQuickFileDialog *self,
    const QString *suffix) {
  self->setDefaultSuffix(*suffix);
}

//  void QQuickFileDialog::resetDefaultSuffix()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog18resetDefaultSuffixEv(
    QQuickFileDialog *self) {
  self->resetDefaultSuffix();
}

//  QString QQuickFileDialog::acceptLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQuickFileDialog11acceptLabelEv(
    const QQuickFileDialog *self) {
  return new QString(self->acceptLabel());
}

//  void QQuickFileDialog::setAcceptLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog14setAcceptLabelERK7QString(
    QQuickFileDialog *self,
    const QString *label) {
  self->setAcceptLabel(*label);
}

//  void QQuickFileDialog::resetAcceptLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog16resetAcceptLabelEv(
    QQuickFileDialog *self) {
  self->resetAcceptLabel();
}

//  QString QQuickFileDialog::rejectLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQuickFileDialog11rejectLabelEv(
    const QQuickFileDialog *self) {
  return new QString(self->rejectLabel());
}

//  void QQuickFileDialog::setRejectLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog14setRejectLabelERK7QString(
    QQuickFileDialog *self,
    const QString *label) {
  self->setRejectLabel(*label);
}

//  void QQuickFileDialog::resetRejectLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog16resetRejectLabelEv(
    QQuickFileDialog *self) {
  self->resetRejectLabel();
}

//  void QQuickFileDialog::fileModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog15fileModeChangedEv(QQuickFileDialog *self) {
  self->fileModeChanged();
}

//  void QQuickFileDialog::selectedFileChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog19selectedFileChangedEv(
    QQuickFileDialog *self) {
  self->selectedFileChanged();
}

//  void QQuickFileDialog::selectedFilesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog20selectedFilesChangedEv(
    QQuickFileDialog *self) {
  self->selectedFilesChanged();
}

//  void QQuickFileDialog::currentFileChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog18currentFileChangedEv(
    QQuickFileDialog *self) {
  self->currentFileChanged();
}

//  void QQuickFileDialog::currentFilesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog19currentFilesChangedEv(
    QQuickFileDialog *self) {
  self->currentFilesChanged();
}

//  void QQuickFileDialog::currentFolderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog20currentFolderChangedEv(
    QQuickFileDialog *self) {
  self->currentFolderChanged();
}

//  void QQuickFileDialog::optionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog14optionsChangedEv(QQuickFileDialog *self) {
  self->optionsChanged();
}

//  void QQuickFileDialog::nameFiltersChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog18nameFiltersChangedEv(
    QQuickFileDialog *self) {
  self->nameFiltersChanged();
}

//  void QQuickFileDialog::defaultSuffixChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog20defaultSuffixChangedEv(
    QQuickFileDialog *self) {
  self->defaultSuffixChanged();
}

//  void QQuickFileDialog::acceptLabelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog18acceptLabelChangedEv(
    QQuickFileDialog *self) {
  self->acceptLabelChanged();
}

//  void QQuickFileDialog::rejectLabelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog18rejectLabelChangedEv(
    QQuickFileDialog *self) {
  self->rejectLabelChanged();
}

//  bool QQuickFileDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickFileDialog15useNativeDialogEv(
    const QQuickFileDialog *self) {
  return self->useNativeDialog();
}

//  void QQuickFileDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog8onCreateEP21QPlatformDialogHelper(
    QQuickFileDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onCreate(dialog);
}

//  void QQuickFileDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog6onShowEP21QPlatformDialogHelper(
    QQuickFileDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onShow(dialog);
}

//  void QQuickFileDialog::onHide(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog6onHideEP21QPlatformDialogHelper(
    QQuickFileDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onHide(dialog);
}

//  void QQuickFileDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog6acceptEv(QQuickFileDialog *self) {
  self->accept();
}

//  QUrl QQuickFileDialog::addDefaultSuffix(const QUrl &file) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QQuickFileDialog16addDefaultSuffixERK4QUrl(
    const QQuickFileDialog *self,
    const QUrl *file) {
  return new QUrl(self->addDefaultSuffix(*file));
}

//  QList<QUrl> QQuickFileDialog::addDefaultSuffixes(const QList<QUrl>
//      &files) const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK16QQuickFileDialog18addDefaultSuffixesERK5QListI4QUrlE(
    const QQuickFileDialog *self,
    const QList<QUrl> *files) {
  return new QList<QUrl>(self->addDefaultSuffixes(*files));
}

//  void QQuickFileDialog::setSelectedFiles(const QList<QUrl> &selectedFiles)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFileDialog16setSelectedFilesERK5QListI4QUrlE(
    QQuickFileDialog *self,
    const QList<QUrl> *selectedFiles) {
  self->setSelectedFiles(*selectedFiles);
}

//  bool QQuickFileDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QQuickFileDialog15useNativeDialogEv(
    const QQuickFileDialog *self) {
  return static_cast<const OwnQQuickFileDialog *>(self)->OwnQQuickFileDialog::useNativeDialog();
}

//  void QQuickFileDialog::onCreate(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickFileDialog8onCreateEP21QPlatformDialogHelper(
    QQuickFileDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickFileDialog *>(self)->OwnQQuickFileDialog::onCreate(
      dialog);
}

//  void QQuickFileDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickFileDialog6onShowEP21QPlatformDialogHelper(
    QQuickFileDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickFileDialog *>(self)->OwnQQuickFileDialog::onShow(
      dialog);
}

//  void QQuickFileDialog::onHide(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickFileDialog6onHideEP21QPlatformDialogHelper(
    QQuickFileDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickFileDialog *>(self)->OwnQQuickFileDialog::onHide(
      dialog);
}

//  void QQuickFileDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickFileDialog6acceptEv(QQuickFileDialog *self) {
  static_cast<OwnQQuickFileDialog *>(self)->OwnQQuickFileDialog::accept();
}

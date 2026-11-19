//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qfiledialog.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qfiledialog.h>
#include <QtCore/qstring.h>
#include <QtCore/qdir.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QFileDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QFileDialog10metaObjectEv(
    const QFileDialog *self) {
  return self->metaObject();
}

//  QString QFileDialog::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFileDialog2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFileDialog::tr(s, c, n));
}

//  QFileDialog::QFileDialog(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QFileDialog *ritual_ZN11QFileDialogC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new QFileDialog(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QFileDialog::QFileDialog(QWidget *parent, const QString &caption, const
//      QString &directory, const QString &filter)
extern "C" Q_DECL_EXPORT
QFileDialog *ritual_ZN11QFileDialogC1EP7QWidgetRK7QStringS4_S4_(
    QWidget *parent,
    const QString *caption,
    const QString *directory,
    const QString *filter) {
  return new QFileDialog(parent, *caption, *directory, *filter);
}

//  QFileDialog::~QFileDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialogD1Ev(QFileDialog *self) {
  delete self;
}

//  void QFileDialog::setDirectory(const QString &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog12setDirectoryERK7QString(
    QFileDialog *self,
    const QString *directory) {
  self->setDirectory(*directory);
}

//  void QFileDialog::setDirectory(const QDir &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog12setDirectoryERK4QDir(
    QFileDialog *self,
    const QDir *directory) {
  self->setDirectory(*directory);
}

//  QDir QFileDialog::directory() const
extern "C" Q_DECL_EXPORT
QDir *ritual_ZNK11QFileDialog9directoryEv(const QFileDialog *self) {
  return new QDir(self->directory());
}

//  void QFileDialog::setDirectoryUrl(const QUrl &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog15setDirectoryUrlERK4QUrl(
    QFileDialog *self,
    const QUrl *directory) {
  self->setDirectoryUrl(*directory);
}

//  QUrl QFileDialog::directoryUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK11QFileDialog12directoryUrlEv(const QFileDialog *self) {
  return new QUrl(self->directoryUrl());
}

//  void QFileDialog::selectFile(const QString &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog10selectFileERK7QString(
    QFileDialog *self,
    const QString *filename) {
  self->selectFile(*filename);
}

//  void QFileDialog::selectUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog9selectUrlERK4QUrl(
    QFileDialog *self,
    const QUrl *url) {
  self->selectUrl(*url);
}

//  void QFileDialog::setNameFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog13setNameFilterERK7QString(
    QFileDialog *self,
    const QString *filter) {
  self->setNameFilter(*filter);
}

//  void QFileDialog::selectNameFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog16selectNameFilterERK7QString(
    QFileDialog *self,
    const QString *filter) {
  self->selectNameFilter(*filter);
}

//  QString QFileDialog::selectedMimeTypeFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QFileDialog22selectedMimeTypeFilterEv(
    const QFileDialog *self) {
  return new QString(self->selectedMimeTypeFilter());
}

//  QString QFileDialog::selectedNameFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QFileDialog18selectedNameFilterEv(
    const QFileDialog *self) {
  return new QString(self->selectedNameFilter());
}

//  void QFileDialog::selectMimeTypeFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog20selectMimeTypeFilterERK7QString(
    QFileDialog *self,
    const QString *filter) {
  self->selectMimeTypeFilter(*filter);
}

//  QDir::Filters QFileDialog::filter() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFileDialog6filterEv(const QFileDialog *self) {
  return static_cast<int>(self->filter().toInt());
}

//  void QFileDialog::setFilter(QDir::Filters filters)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog9setFilterE6QFlagsIN4QDir6FilterEE(
    QFileDialog *self,
    int filters) {
  self->setFilter(QFlags<QDir::Filter>::fromInt(filters));
}

//  void QFileDialog::setViewMode(ViewMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog11setViewModeENS_8ViewModeE(
    QFileDialog *self,
    QFileDialog::ViewMode mode) {
  self->setViewMode(mode);
}

//  ViewMode QFileDialog::viewMode() const
extern "C" Q_DECL_EXPORT
QFileDialog::ViewMode ritual_ZNK11QFileDialog8viewModeEv(
    const QFileDialog *self) {
  return self->viewMode();
}

//  void QFileDialog::setFileMode(FileMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog11setFileModeENS_8FileModeE(
    QFileDialog *self,
    QFileDialog::FileMode mode) {
  self->setFileMode(mode);
}

//  FileMode QFileDialog::fileMode() const
extern "C" Q_DECL_EXPORT
QFileDialog::FileMode ritual_ZNK11QFileDialog8fileModeEv(
    const QFileDialog *self) {
  return self->fileMode();
}

//  void QFileDialog::setAcceptMode(AcceptMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog13setAcceptModeENS_10AcceptModeE(
    QFileDialog *self,
    QFileDialog::AcceptMode mode) {
  self->setAcceptMode(mode);
}

//  AcceptMode QFileDialog::acceptMode() const
extern "C" Q_DECL_EXPORT
QFileDialog::AcceptMode ritual_ZNK11QFileDialog10acceptModeEv(
    const QFileDialog *self) {
  return self->acceptMode();
}

//  QByteArray QFileDialog::saveState() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QFileDialog9saveStateEv(const QFileDialog *self) {
  return new QByteArray(self->saveState());
}

//  bool QFileDialog::restoreState(const QByteArray &state)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDialog12restoreStateERK10QByteArray(
    QFileDialog *self,
    const QByteArray *state) {
  return self->restoreState(*state);
}

//  void QFileDialog::setDefaultSuffix(const QString &suffix)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog16setDefaultSuffixERK7QString(
    QFileDialog *self,
    const QString *suffix) {
  self->setDefaultSuffix(*suffix);
}

//  QString QFileDialog::defaultSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QFileDialog13defaultSuffixEv(const QFileDialog *self) {
  return new QString(self->defaultSuffix());
}

//  void QFileDialog::setItemDelegate(QAbstractItemDelegate *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog15setItemDelegateEP21QAbstractItemDelegate(
    QFileDialog *self,
    QAbstractItemDelegate *delegate) {
  self->setItemDelegate(delegate);
}

//  QAbstractItemDelegate *QFileDialog::itemDelegate() const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK11QFileDialog12itemDelegateEv(
    const QFileDialog *self) {
  return self->itemDelegate();
}

//  void QFileDialog::setIconProvider(QAbstractFileIconProvider *provider)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog15setIconProviderEP25QAbstractFileIconProvider(
    QFileDialog *self,
    QAbstractFileIconProvider *provider) {
  self->setIconProvider(provider);
}

//  QAbstractFileIconProvider *QFileDialog::iconProvider() const
extern "C" Q_DECL_EXPORT
QAbstractFileIconProvider *ritual_ZNK11QFileDialog12iconProviderEv(
    const QFileDialog *self) {
  return self->iconProvider();
}

//  void QFileDialog::setLabelText(DialogLabel label, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog12setLabelTextENS_11DialogLabelERK7QString(
    QFileDialog *self,
    QFileDialog::DialogLabel label,
    const QString *text) {
  self->setLabelText(label, *text);
}

//  QString QFileDialog::labelText(DialogLabel label) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QFileDialog9labelTextENS_11DialogLabelE(
    const QFileDialog *self,
    QFileDialog::DialogLabel label) {
  return new QString(self->labelText(label));
}

//  void QFileDialog::setProxyModel(QAbstractProxyModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog13setProxyModelEP19QAbstractProxyModel(
    QFileDialog *self,
    QAbstractProxyModel *model) {
  self->setProxyModel(model);
}

//  QAbstractProxyModel *QFileDialog::proxyModel() const
extern "C" Q_DECL_EXPORT
QAbstractProxyModel *ritual_ZNK11QFileDialog10proxyModelEv(
    const QFileDialog *self) {
  return self->proxyModel();
}

//  void QFileDialog::setOption(Option option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog9setOptionENS_6OptionEb(
    QFileDialog *self,
    QFileDialog::Option option,
    bool on) {
  self->setOption(option, on);
}

//  bool QFileDialog::testOption(Option option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFileDialog10testOptionENS_6OptionE(
    const QFileDialog *self,
    QFileDialog::Option option) {
  return self->testOption(option);
}

//  void QFileDialog::setOptions(Options options)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog10setOptionsE6QFlagsINS_6OptionEE(
    QFileDialog *self,
    int options) {
  self->setOptions(QFlags<QFileDialog::Option>::fromInt(options));
}

//  Options QFileDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFileDialog7optionsEv(const QFileDialog *self) {
  return static_cast<int>(self->options().toInt());
}

//  void QFileDialog::open(QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog4openEP7QObjectPKc(
    QFileDialog *self,
    QObject *receiver,
    const char *member) {
  self->open(receiver, member);
}

//  void QFileDialog::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog10setVisibleEb(QFileDialog *self, bool visible) {
  self->setVisible(visible);
}

//  QString QFileDialog::getOpenFileName(QWidget *parent, const QString
//      &caption, const QString &dir, const QString &filter, QString
//      *selectedFilter, Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFileDialog15getOpenFileNameEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsINS_6OptionEE(
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QString(
      QFileDialog::getOpenFileName(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QString QFileDialog::getSaveFileName(QWidget *parent, const QString
//      &caption, const QString &dir, const QString &filter, QString
//      *selectedFilter, Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFileDialog15getSaveFileNameEP7QWidgetRK7QStringS4_S4_PS2_6QFlagsINS_6OptionEE(
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    const QString *filter,
    QString *selectedFilter,
    int options) {
  return new QString(
      QFileDialog::getSaveFileName(
          parent,
          *caption,
          *dir,
          *filter,
          selectedFilter,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  QString QFileDialog::getExistingDirectory(QWidget *parent, const QString
//      &caption, const QString &dir, Options options)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFileDialog20getExistingDirectoryEP7QWidgetRK7QStringS4_6QFlagsINS_6OptionEE(
    QWidget *parent,
    const QString *caption,
    const QString *dir,
    int options) {
  return new QString(
      QFileDialog::getExistingDirectory(
          parent,
          *caption,
          *dir,
          QFlags<QFileDialog::Option>::fromInt(options)));
}

//  void QFileDialog::saveFileContent(const QByteArray &fileContent, const
//      QString &fileNameHint, QWidget *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDialog15saveFileContentERK10QByteArrayRK7QStringP7QWidget(
    const QByteArray *fileContent,
    const QString *fileNameHint,
    QWidget *parent) {
  QFileDialog::saveFileContent(*fileContent, *fileNameHint, parent);
}

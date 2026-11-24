//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquicklabsplatformdialog_p.h"
#include <QtCore/qloggingcategory.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtQuick/qquickitem.h>
#include <QtQuick/qquickwindow.h>
#include "qquicklabsplatformfiledialog_p.h"
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/qlist.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 59, as _ZN24QQuickLabsPlatformDialogC2EN14QPlatformTheme10DialogTypeEP7QObject
inline QQuickLabsPlatformDialog::QQuickLabsPlatformDialog(QPlatformTheme::DialogType type, QObject *parent)
    : QObject(parent),
      m_visible(false),
      m_complete(false),
      m_result(0),
      m_parentWindow(nullptr),
      m_flags(Qt::Dialog),
      m_modality(Qt::WindowModal),
      m_type(type),
      m_handle(nullptr)
{
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 72, as _ZN24QQuickLabsPlatformDialogD2Ev
inline QQuickLabsPlatformDialog::~QQuickLabsPlatformDialog()
{
    destroy();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 77, as _ZNK24QQuickLabsPlatformDialog6handleEv
inline QPlatformDialogHelper *QQuickLabsPlatformDialog::handle() const
{
    return m_handle;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 581, as _ZN32QQuickLabsPlatformFileNameFilter10setOptionsERK14QSharedPointerI18QFileDialogOptionsE
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileNameFilter::setOptions(const QSharedPointer<QFileDialogOptions> &options)
{
    m_options = options;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 547, as _ZN32QQuickLabsPlatformFileNameFilterC1EP7QObject
#if QT_DEPRECATED_SINCE(6, 9)
inline QQuickLabsPlatformFileNameFilter::QQuickLabsPlatformFileNameFilter(QObject *parent)
    : QObject(parent), m_index(-1)
{
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 342, as _ZNK24QQuickLabsPlatformDialog15useNativeDialogEv
inline bool QQuickLabsPlatformDialog::useNativeDialog() const
{
    return !QCoreApplication::testAttribute(Qt::AA_DontUseNativeDialogs)
            && QGuiApplicationPrivate::platformTheme()->usePlatformNativeDialog(m_type);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 268, as _ZN24QQuickLabsPlatformDialog6acceptEv
inline void QQuickLabsPlatformDialog::accept()
{
    done(Accepted);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 92, as _ZNK28QQuickLabsPlatformFileDialog8fileModeEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QQuickLabsPlatformFileDialog::FileMode QQuickLabsPlatformFileDialog::fileMode() const
{
    return m_fileMode;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 187, as _ZNK28QQuickLabsPlatformFileDialog11currentFileEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QUrl QQuickLabsPlatformFileDialog::currentFile() const
{
    return currentFiles().value(0);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 192, as _ZN28QQuickLabsPlatformFileDialog14setCurrentFileERK4QUrl
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileDialog::setCurrentFile(const QUrl &file)
{
    setCurrentFiles(QList<QUrl>() << file);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 208, as _ZNK28QQuickLabsPlatformFileDialog12currentFilesEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QList<QUrl> QQuickLabsPlatformFileDialog::currentFiles() const
{
    if (QPlatformFileDialogHelper *fileDialog = qobject_cast<QPlatformFileDialogHelper *>(handle()))
        return fileDialog->selectedFiles();
    return m_options->initiallySelectedFiles();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 215, as _ZN28QQuickLabsPlatformFileDialog15setCurrentFilesERK5QListI4QUrlE
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileDialog::setCurrentFiles(const QList<QUrl> &files)
{
    if (QPlatformFileDialogHelper *fileDialog = qobject_cast<QPlatformFileDialogHelper *>(handle())) {
        for (const QUrl &file : files)
            fileDialog->selectFile(file);
    }
    m_options->setInitiallySelectedFiles(files);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 232, as _ZNK28QQuickLabsPlatformFileDialog6folderEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QUrl QQuickLabsPlatformFileDialog::folder() const
{
    if (QPlatformFileDialogHelper *fileDialog = qobject_cast<QPlatformFileDialogHelper *>(handle()))
        return fileDialog->directory();
    return m_options->initialDirectory();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 239, as _ZN28QQuickLabsPlatformFileDialog9setFolderERK4QUrl
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileDialog::setFolder(const QUrl &folder)
{
    if (QPlatformFileDialogHelper *fileDialog = qobject_cast<QPlatformFileDialogHelper *>(handle()))
        fileDialog->setDirectory(folder);
    m_options->setInitialDirectory(folder);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 263, as _ZNK28QQuickLabsPlatformFileDialog7optionsEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QFileDialogOptions::FileDialogOptions QQuickLabsPlatformFileDialog::options() const
{
    return m_options->options();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 303, as _ZNK28QQuickLabsPlatformFileDialog11nameFiltersEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QStringList QQuickLabsPlatformFileDialog::nameFilters() const
{
    return m_options->nameFilters();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 390, as _ZNK28QQuickLabsPlatformFileDialog13defaultSuffixEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformFileDialog::defaultSuffix() const
{
    return m_options->defaultSuffix();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 422, as _ZNK28QQuickLabsPlatformFileDialog11acceptLabelEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformFileDialog::acceptLabel() const
{
    return m_options->labelText(QFileDialogOptions::Accept);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 453, as _ZNK28QQuickLabsPlatformFileDialog11rejectLabelEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformFileDialog::rejectLabel() const
{
    return m_options->labelText(QFileDialogOptions::Reject);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 472, as _ZNK28QQuickLabsPlatformFileDialog15useNativeDialogEv
#if QT_DEPRECATED_SINCE(6, 9)
inline bool QQuickLabsPlatformFileDialog::useNativeDialog() const
{
    return QQuickLabsPlatformDialog::useNativeDialog()
            && !m_options->testOption(QFileDialogOptions::DontUseNativeDialog);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 478, as _ZN28QQuickLabsPlatformFileDialog8onCreateEP21QPlatformDialogHelper
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileDialog::onCreate(QPlatformDialogHelper *dialog)
{
    if (QPlatformFileDialogHelper *fileDialog = qobject_cast<QPlatformFileDialogHelper *>(dialog)) {
        // TODO: emit currentFileChanged only when the first entry in currentFiles changes
        connect(fileDialog, &QPlatformFileDialogHelper::currentChanged, this, &QQuickLabsPlatformFileDialog::currentFileChanged);
        connect(fileDialog, &QPlatformFileDialogHelper::currentChanged, this, &QQuickLabsPlatformFileDialog::currentFilesChanged);
        connect(fileDialog, &QPlatformFileDialogHelper::directoryEntered, this, &QQuickLabsPlatformFileDialog::folderChanged);
        fileDialog->setOptions(m_options);
    }
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 489, as _ZN28QQuickLabsPlatformFileDialog6onShowEP21QPlatformDialogHelper
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileDialog::onShow(QPlatformDialogHelper *dialog)
{
    m_options->setWindowTitle(title());
    if (QPlatformFileDialogHelper *fileDialog = qobject_cast<QPlatformFileDialogHelper *>(dialog)) {
        fileDialog->setOptions(m_options); // setOptions only assigns a member and isn't virtual
        if (m_firstShow && m_options->initialDirectory().isValid())
            fileDialog->setDirectory(m_options->initialDirectory());
        if (m_selectedNameFilter) {
            const int index = m_selectedNameFilter->index();
            const QString filter = m_options->nameFilters().value(index);
            m_options->setInitiallySelectedNameFilter(filter);
            fileDialog->selectNameFilter(filter);
            connect(fileDialog, &QPlatformFileDialogHelper::filterSelected, m_selectedNameFilter, &QQuickLabsPlatformFileNameFilter::update);
        }
    }
    if (m_firstShow)
        m_firstShow = false;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 508, as _ZN28QQuickLabsPlatformFileDialog6onHideEP21QPlatformDialogHelper
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileDialog::onHide(QPlatformDialogHelper *dialog)
{
    if (QPlatformFileDialogHelper *fileDialog = qobject_cast<QPlatformFileDialogHelper *>(dialog)) {
        if (m_selectedNameFilter)
            disconnect(fileDialog, &QPlatformFileDialogHelper::filterSelected, m_selectedNameFilter, &QQuickLabsPlatformFileNameFilter::update);
    }
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 516, as _ZN28QQuickLabsPlatformFileDialog6acceptEv
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileDialog::accept()
{
    if (QPlatformFileDialogHelper *fileDialog = qobject_cast<QPlatformFileDialogHelper *>(handle()))
        setFiles(fileDialog->selectedFiles());
    QQuickLabsPlatformDialog::accept();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)
//  -----------------------------------------------------------------------

//  Only a class built on QQuickLabsPlatformFileDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLabsPlatformFileDialog : QQuickLabsPlatformFileDialog {
  using QQuickLabsPlatformFileDialog::useNativeDialog;
};

//  const QMetaObject *QQuickLabsPlatformFileDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickLabsPlatformFileDialog10metaObjectEv(
    const QQuickLabsPlatformFileDialog *self) {
  return self->metaObject();
}

//  const QMetaObject *QQuickLabsPlatformFileDialog::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN28QQuickLabsPlatformFileDialog20qmlExtendedNamespaceEv() {
  return QQuickLabsPlatformFileDialog::qmlExtendedNamespace();
}

//  void QQuickLabsPlatformFileDialog::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog30qt_qmlMarker_extendedNamespaceEv(
    QQuickLabsPlatformFileDialog *self) {
  self->qt_qmlMarker_extendedNamespace();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  FileMode QQuickLabsPlatformFileDialog::fileMode() const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformFileDialog::FileMode ritual_ZNK28QQuickLabsPlatformFileDialog8fileModeEv(
    const QQuickLabsPlatformFileDialog *self) {
  return self->fileMode();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QUrl QQuickLabsPlatformFileDialog::currentFile() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK28QQuickLabsPlatformFileDialog11currentFileEv(
    const QQuickLabsPlatformFileDialog *self) {
  return new QUrl(self->currentFile());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformFileDialog::setCurrentFile(const QUrl &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog14setCurrentFileERK4QUrl(
    QQuickLabsPlatformFileDialog *self,
    const QUrl *file) {
  self->setCurrentFile(*file);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QList<QUrl> QQuickLabsPlatformFileDialog::currentFiles() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK28QQuickLabsPlatformFileDialog12currentFilesEv(
    const QQuickLabsPlatformFileDialog *self) {
  return new QList<QUrl>(self->currentFiles());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformFileDialog::setCurrentFiles(const QList<QUrl>
//      &files)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog15setCurrentFilesERK5QListI4QUrlE(
    QQuickLabsPlatformFileDialog *self,
    const QList<QUrl> *files) {
  self->setCurrentFiles(*files);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QUrl QQuickLabsPlatformFileDialog::folder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK28QQuickLabsPlatformFileDialog6folderEv(
    const QQuickLabsPlatformFileDialog *self) {
  return new QUrl(self->folder());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformFileDialog::setFolder(const QUrl &folder)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog9setFolderERK4QUrl(
    QQuickLabsPlatformFileDialog *self,
    const QUrl *folder) {
  self->setFolder(*folder);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QFileDialogOptions::FileDialogOptions
//      QQuickLabsPlatformFileDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QQuickLabsPlatformFileDialog7optionsEv(
    const QQuickLabsPlatformFileDialog *self) {
  return static_cast<int>(self->options().toInt());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QStringList QQuickLabsPlatformFileDialog::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK28QQuickLabsPlatformFileDialog11nameFiltersEv(
    const QQuickLabsPlatformFileDialog *self) {
  return new QList<QString>(self->nameFilters());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformFileDialog::defaultSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QQuickLabsPlatformFileDialog13defaultSuffixEv(
    const QQuickLabsPlatformFileDialog *self) {
  return new QString(self->defaultSuffix());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformFileDialog::acceptLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QQuickLabsPlatformFileDialog11acceptLabelEv(
    const QQuickLabsPlatformFileDialog *self) {
  return new QString(self->acceptLabel());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformFileDialog::rejectLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QQuickLabsPlatformFileDialog11rejectLabelEv(
    const QQuickLabsPlatformFileDialog *self) {
  return new QString(self->rejectLabel());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  bool QQuickLabsPlatformFileDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QQuickLabsPlatformFileDialog15useNativeDialogEv(
    const QQuickLabsPlatformFileDialog *self) {
  return self->useNativeDialog();
}

//  void QQuickLabsPlatformFileDialog::onCreate(QPlatformDialogHelper
//      *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog8onCreateEP21QPlatformDialogHelper(
    QQuickLabsPlatformFileDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onCreate(dialog);
}

//  void QQuickLabsPlatformFileDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformFileDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onShow(dialog);
}

//  void QQuickLabsPlatformFileDialog::onHide(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog6onHideEP21QPlatformDialogHelper(
    QQuickLabsPlatformFileDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onHide(dialog);
}

//  void QQuickLabsPlatformFileDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog6acceptEv(
    QQuickLabsPlatformFileDialog *self) {
  self->accept();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  bool QQuickLabsPlatformFileDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK28QQuickLabsPlatformFileDialog15useNativeDialogEv(
    const QQuickLabsPlatformFileDialog *self) {
  return static_cast<const OwnQQuickLabsPlatformFileDialog *>(self)->OwnQQuickLabsPlatformFileDialog::useNativeDialog();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#endif  // QT_DEPRECATED_SINCE(6, 9)

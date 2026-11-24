//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformfolderdialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformfolderdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/private/qquicklabsplatformdialog_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtQuick/qquickitem.h>
#include <QtQuick/qquickwindow.h>
#include <QtLabsPlatform/private/qquicklabsplatformfolderdialog_p.h>
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

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 342, as _ZNK24QQuickLabsPlatformDialog15useNativeDialogEv
inline bool QQuickLabsPlatformDialog::useNativeDialog() const
{
    return !QCoreApplication::testAttribute(Qt::AA_DontUseNativeDialogs)
            && QGuiApplicationPrivate::platformTheme()->usePlatformNativeDialog(m_type);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 122, as _ZNK24QQuickLabsPlatformDialog5titleEv
inline QString QQuickLabsPlatformDialog::title() const
{
    return m_title;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 268, as _ZN24QQuickLabsPlatformDialog6acceptEv
inline void QQuickLabsPlatformDialog::accept()
{
    done(Accepted);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfolderdialog.cpp, line 88, as _ZNK30QQuickLabsPlatformFolderDialog6folderEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QUrl QQuickLabsPlatformFolderDialog::folder() const
{
    return m_folder;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfolderdialog.cpp, line 113, as _ZNK30QQuickLabsPlatformFolderDialog13currentFolderEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QUrl QQuickLabsPlatformFolderDialog::currentFolder() const
{
    if (QPlatformFileDialogHelper *fileDialog = qobject_cast<QPlatformFileDialogHelper *>(handle())) {
        const QList<QUrl> selectedFiles = fileDialog->selectedFiles();
        if (!selectedFiles.isEmpty())
            return selectedFiles.first();
        return fileDialog->directory();
    }
    return m_options->initialDirectory();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfolderdialog.cpp, line 124, as _ZN30QQuickLabsPlatformFolderDialog16setCurrentFolderERK4QUrl
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFolderDialog::setCurrentFolder(const QUrl &folder)
{
    if (QPlatformFileDialogHelper *fileDialog = qobject_cast<QPlatformFileDialogHelper *>(handle()))
        fileDialog->setDirectory(folder);
    m_options->setInitialDirectory(folder);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfolderdialog.cpp, line 147, as _ZNK30QQuickLabsPlatformFolderDialog7optionsEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QFileDialogOptions::FileDialogOptions QQuickLabsPlatformFolderDialog::options() const
{
    return m_options->options();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfolderdialog.cpp, line 178, as _ZNK30QQuickLabsPlatformFolderDialog11acceptLabelEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformFolderDialog::acceptLabel() const
{
    return m_options->labelText(QFileDialogOptions::Accept);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfolderdialog.cpp, line 209, as _ZNK30QQuickLabsPlatformFolderDialog11rejectLabelEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QString QQuickLabsPlatformFolderDialog::rejectLabel() const
{
    return m_options->labelText(QFileDialogOptions::Reject);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfolderdialog.cpp, line 228, as _ZNK30QQuickLabsPlatformFolderDialog15useNativeDialogEv
#if QT_DEPRECATED_SINCE(6, 9)
inline bool QQuickLabsPlatformFolderDialog::useNativeDialog() const
{
    return QQuickLabsPlatformDialog::useNativeDialog()
            && !m_options->testOption(QFileDialogOptions::DontUseNativeDialog);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfolderdialog.cpp, line 234, as _ZN30QQuickLabsPlatformFolderDialog8onCreateEP21QPlatformDialogHelper
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFolderDialog::onCreate(QPlatformDialogHelper *dialog)
{
    if (QPlatformFileDialogHelper *fileDialog = qobject_cast<QPlatformFileDialogHelper *>(dialog)) {
        connect(fileDialog, &QPlatformFileDialogHelper::currentChanged, this, &QQuickLabsPlatformFolderDialog::currentFolderChanged);
        fileDialog->setOptions(m_options);
    }
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfolderdialog.cpp, line 242, as _ZN30QQuickLabsPlatformFolderDialog6onShowEP21QPlatformDialogHelper
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFolderDialog::onShow(QPlatformDialogHelper *dialog)
{
    m_options->setWindowTitle(title());
    if (QPlatformFileDialogHelper *fileDialog = qobject_cast<QPlatformFileDialogHelper *>(dialog))
        fileDialog->setOptions(m_options);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfolderdialog.cpp, line 249, as _ZN30QQuickLabsPlatformFolderDialog6acceptEv
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFolderDialog::accept()
{
    setFolder(currentFolder());
    QQuickLabsPlatformDialog::accept();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)
//  -----------------------------------------------------------------------

//  Only a class built on QQuickLabsPlatformFolderDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLabsPlatformFolderDialog : QQuickLabsPlatformFolderDialog {
  using QQuickLabsPlatformFolderDialog::useNativeDialog;
  using QQuickLabsPlatformFolderDialog::onShow;
};

//  const QMetaObject *QQuickLabsPlatformFolderDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QQuickLabsPlatformFolderDialog10metaObjectEv(
    const QQuickLabsPlatformFolderDialog *self) {
  return self->metaObject();
}

//  const QMetaObject *QQuickLabsPlatformFolderDialog::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN30QQuickLabsPlatformFolderDialog20qmlExtendedNamespaceEv() {
  return QQuickLabsPlatformFolderDialog::qmlExtendedNamespace();
}

//  void QQuickLabsPlatformFolderDialog::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickLabsPlatformFolderDialog30qt_qmlMarker_extendedNamespaceEv(
    QQuickLabsPlatformFolderDialog *self) {
  self->qt_qmlMarker_extendedNamespace();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  QUrl QQuickLabsPlatformFolderDialog::folder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK30QQuickLabsPlatformFolderDialog6folderEv(
    const QQuickLabsPlatformFolderDialog *self) {
  return new QUrl(self->folder());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QUrl QQuickLabsPlatformFolderDialog::currentFolder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK30QQuickLabsPlatformFolderDialog13currentFolderEv(
    const QQuickLabsPlatformFolderDialog *self) {
  return new QUrl(self->currentFolder());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformFolderDialog::setCurrentFolder(const QUrl &folder)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickLabsPlatformFolderDialog16setCurrentFolderERK4QUrl(
    QQuickLabsPlatformFolderDialog *self,
    const QUrl *folder) {
  self->setCurrentFolder(*folder);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QFileDialogOptions::FileDialogOptions
//      QQuickLabsPlatformFolderDialog::options() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuickLabsPlatformFolderDialog7optionsEv(
    const QQuickLabsPlatformFolderDialog *self) {
  return static_cast<int>(self->options().toInt());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformFolderDialog::acceptLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QQuickLabsPlatformFolderDialog11acceptLabelEv(
    const QQuickLabsPlatformFolderDialog *self) {
  return new QString(self->acceptLabel());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QString QQuickLabsPlatformFolderDialog::rejectLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK30QQuickLabsPlatformFolderDialog11rejectLabelEv(
    const QQuickLabsPlatformFolderDialog *self) {
  return new QString(self->rejectLabel());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  bool QQuickLabsPlatformFolderDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK30QQuickLabsPlatformFolderDialog15useNativeDialogEv(
    const QQuickLabsPlatformFolderDialog *self) {
  return self->useNativeDialog();
}

//  void QQuickLabsPlatformFolderDialog::onCreate(QPlatformDialogHelper
//      *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickLabsPlatformFolderDialog8onCreateEP21QPlatformDialogHelper(
    QQuickLabsPlatformFolderDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onCreate(dialog);
}

//  void QQuickLabsPlatformFolderDialog::onShow(QPlatformDialogHelper
//      *dialog)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickLabsPlatformFolderDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformFolderDialog *self,
    QPlatformDialogHelper *dialog) {
  self->onShow(dialog);
}

//  void QQuickLabsPlatformFolderDialog::accept()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickLabsPlatformFolderDialog6acceptEv(
    QQuickLabsPlatformFolderDialog *self) {
  self->accept();
}

#if QT_DEPRECATED_SINCE(6, 9)
//  bool QQuickLabsPlatformFolderDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK30QQuickLabsPlatformFolderDialog15useNativeDialogEv(
    const QQuickLabsPlatformFolderDialog *self) {
  return static_cast<const OwnQQuickLabsPlatformFolderDialog *>(self)->OwnQQuickLabsPlatformFolderDialog::useNativeDialog();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformFolderDialog::onShow(QPlatformDialogHelper
//      *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickLabsPlatformFolderDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformFolderDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickLabsPlatformFolderDialog *>(self)->OwnQQuickLabsPlatformFolderDialog::onShow(
      dialog);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#endif  // QT_DEPRECATED_SINCE(6, 9)

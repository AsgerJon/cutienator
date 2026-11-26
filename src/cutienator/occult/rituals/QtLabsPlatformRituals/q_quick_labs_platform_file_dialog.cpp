//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: added are 3 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
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
#include <QtLabsPlatform/private/qquicklabsplatformdialog_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtQuick/qquickitem.h>
#include <QtQuick/qquickwindow.h>
#include <QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h>
#if QT_DEPRECATED_SINCE(6, 9)
#include <QtCore/qlist.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 586, as local:qquicklabsplatformfiledialog.cpp:extractName
#if QT_DEPRECATED_SINCE(6, 9)
static QString extractName(const QString &filter)
{
    return filter.left(filter.indexOf(QLatin1Char('(')) - 1);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 591, as local:qquicklabsplatformfiledialog.cpp:extractExtension
#if QT_DEPRECATED_SINCE(6, 9)
static QString extractExtension(QStringView filter)
{
    return filter.mid(filter.indexOf(QLatin1Char('.')) + 1).toString();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 596, as local:qquicklabsplatformfiledialog.cpp:extractExtensions
#if QT_DEPRECATED_SINCE(6, 9)
static QStringList extractExtensions(QStringView filter)
{
    QStringList extensions;
    const int from = filter.indexOf(QLatin1Char('('));
    const int to = filter.lastIndexOf(QLatin1Char(')')) - 1;
    if (from >= 0 && from < to) {
        const QStringView ref = filter.mid(from + 1, to - from);
        const QList<QStringView> exts = ref.split(QLatin1Char(' '), Qt::SkipEmptyParts);
        for (const QStringView &ref : exts)
            extensions += extractExtension(ref);
    }

    return extensions;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 303, as _ZN24QQuickLabsPlatformDialog10classBeginEv
inline void QQuickLabsPlatformDialog::classBegin()
{
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 307, as _ZN24QQuickLabsPlatformDialog17componentCompleteEv
inline void QQuickLabsPlatformDialog::componentComplete()
{
    m_complete = true;
    if (!m_parentWindow)
        setParentWindow(findParentWindow());
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 292, as _ZN24QQuickLabsPlatformDialog4doneEi
inline void QQuickLabsPlatformDialog::done(int result)
{
    close();
    setResult(result);

    if (result == Accepted)
        emit accepted();
    else if (result == Rejected)
        emit rejected();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 280, as _ZN24QQuickLabsPlatformDialog6rejectEv
inline void QQuickLabsPlatformDialog::reject()
{
    done(Rejected);
}

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

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 516, as _ZN28QQuickLabsPlatformFileDialog6acceptEv
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileDialog::accept()
{
    if (QPlatformFileDialogHelper *fileDialog = qobject_cast<QPlatformFileDialogHelper *>(handle()))
        setFiles(fileDialog->selectedFiles());
    QQuickLabsPlatformDialog::accept();
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

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 581, as _ZN32QQuickLabsPlatformFileNameFilter10setOptionsERK14QSharedPointerI18QFileDialogOptionsE
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileNameFilter::setOptions(const QSharedPointer<QFileDialogOptions> &options)
{
    m_options = options;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 611, as _ZN32QQuickLabsPlatformFileNameFilter6updateERK7QString
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileNameFilter::update(const QString &filter)
{
    const QStringList filters = nameFilters();

    const int oldIndex = m_index;
    const QString oldName = m_name;
    const QStringList oldExtensions = m_extensions;

    m_index = filters.indexOf(filter);
    m_name = extractName(filter);
    m_extensions = extractExtensions(filter);

    if (oldIndex != m_index)
        emit indexChanged(m_index);
    if (oldName != m_name)
        emit nameChanged(m_name);
    if (oldExtensions != m_extensions)
        emit extensionsChanged(m_extensions);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 547, as _ZN32QQuickLabsPlatformFileNameFilterC1EP7QObject
#if QT_DEPRECATED_SINCE(6, 9)
inline QQuickLabsPlatformFileNameFilter::QQuickLabsPlatformFileNameFilter(QObject *parent)
    : QObject(parent), m_index(-1)
{
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 77, as _ZNK24QQuickLabsPlatformDialog6handleEv
inline QPlatformDialogHelper *QQuickLabsPlatformDialog::handle() const
{
    return m_handle;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 472, as _ZNK28QQuickLabsPlatformFileDialog15useNativeDialogEv
#if QT_DEPRECATED_SINCE(6, 9)
inline bool QQuickLabsPlatformFileDialog::useNativeDialog() const
{
    return QQuickLabsPlatformDialog::useNativeDialog()
            && !m_options->testOption(QFileDialogOptions::DontUseNativeDialog);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 552, as _ZNK32QQuickLabsPlatformFileNameFilter5indexEv
#if QT_DEPRECATED_SINCE(6, 9)
inline int QQuickLabsPlatformFileNameFilter::index() const
{
    return m_index;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

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

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 631, as _ZNK32QQuickLabsPlatformFileNameFilter11nameFiltersEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QStringList QQuickLabsPlatformFileNameFilter::nameFilters() const
{
    return m_options ? m_options->nameFilters() : QStringList();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformdialog.cpp, line 268, as _ZN24QQuickLabsPlatformDialog6acceptEv
inline void QQuickLabsPlatformDialog::accept()
{
    done(Accepted);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 164, as _ZN28QQuickLabsPlatformFileDialog8setFilesERK5QListI4QUrlE
#if QT_DEPRECATED_SINCE(6, 9)
inline void QQuickLabsPlatformFileDialog::setFiles(const QList<QUrl> &files)
{
    if (m_files == files)
        return;

    bool firstChanged = m_files.value(0) != files.value(0);
    m_files = files;
    if (firstChanged)
        emit fileChanged();
    emit filesChanged();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 92, as _ZNK28QQuickLabsPlatformFileDialog8fileModeEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QQuickLabsPlatformFileDialog::FileMode QQuickLabsPlatformFileDialog::fileMode() const
{
    return m_fileMode;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 136, as _ZNK28QQuickLabsPlatformFileDialog4fileEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QUrl QQuickLabsPlatformFileDialog::file() const
{
    return addDefaultSuffix(m_files.value(0));
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 159, as _ZNK28QQuickLabsPlatformFileDialog5filesEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QList<QUrl> QQuickLabsPlatformFileDialog::files() const
{
    return addDefaultSuffixes(m_files);
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

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 371, as _ZNK28QQuickLabsPlatformFileDialog18selectedNameFilterEv
#if QT_DEPRECATED_SINCE(6, 9)
inline QQuickLabsPlatformFileNameFilter *QQuickLabsPlatformFileDialog::selectedNameFilter() const
{
    if (!m_selectedNameFilter) {
        QQuickLabsPlatformFileDialog *that = const_cast<QQuickLabsPlatformFileDialog *>(this);
        m_selectedNameFilter = new QQuickLabsPlatformFileNameFilter(that);
        m_selectedNameFilter->setOptions(m_options);
    }
    return m_selectedNameFilter;
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

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 523, as _ZNK28QQuickLabsPlatformFileDialog16addDefaultSuffixERK4QUrl
#if QT_DEPRECATED_SINCE(6, 9)
inline QUrl QQuickLabsPlatformFileDialog::addDefaultSuffix(const QUrl &file) const
{
    QUrl url = file;
    const QString path = url.path();
    const QString suffix = m_options->defaultSuffix();
    // Urls with "content" scheme do not require suffixes. Such schemes are
    // used on Android.
    const bool isContentScheme = url.scheme() == u"content"_s;
    if (!isContentScheme && !suffix.isEmpty() && !path.endsWith(QLatin1Char('/'))
        && path.lastIndexOf(QLatin1Char('.')) == -1) {
        url.setPath(path + QLatin1Char('.') + suffix);
    }
    return url;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformfiledialog.cpp, line 538, as _ZNK28QQuickLabsPlatformFileDialog18addDefaultSuffixesERK5QListI4QUrlE
#if QT_DEPRECATED_SINCE(6, 9)
inline QList<QUrl> QQuickLabsPlatformFileDialog::addDefaultSuffixes(const QList<QUrl> &files) const
{
    QList<QUrl> urls;
    urls.reserve(files.size());
    for (const QUrl &file : files)
        urls += addDefaultSuffix(file);
    return urls;
}
#endif  // QT_DEPRECATED_SINCE(6, 9)
//  -----------------------------------------------------------------------

//  Only a class built on QQuickLabsPlatformFileDialog may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLabsPlatformFileDialog : QQuickLabsPlatformFileDialog {
  using QQuickLabsPlatformFileDialog::useNativeDialog;
  using QQuickLabsPlatformFileDialog::onShow;
  using QQuickLabsPlatformFileDialog::onHide;
};

//  const QMetaObject *QQuickLabsPlatformFileDialog::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuickLabsPlatformFileDialog10metaObjectEv(
    const QQuickLabsPlatformFileDialog *self) {
  return self->metaObject();
}

//  void *QQuickLabsPlatformFileDialog::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QQuickLabsPlatformFileDialog11qt_metacastEPKc(
    QQuickLabsPlatformFileDialog *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLabsPlatformFileDialog::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QQuickLabsPlatformFileDialog11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLabsPlatformFileDialog *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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
//  QUrl QQuickLabsPlatformFileDialog::file() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK28QQuickLabsPlatformFileDialog4fileEv(
    const QQuickLabsPlatformFileDialog *self) {
  return new QUrl(self->file());
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QList<QUrl> QQuickLabsPlatformFileDialog::files() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK28QQuickLabsPlatformFileDialog5filesEv(
    const QQuickLabsPlatformFileDialog *self) {
  return new QList<QUrl>(self->files());
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
//  QQuickLabsPlatformFileNameFilter
//      *QQuickLabsPlatformFileDialog::selectedNameFilter() const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformFileNameFilter *ritual_ZNK28QQuickLabsPlatformFileDialog18selectedNameFilterEv(
    const QQuickLabsPlatformFileDialog *self) {
  return self->selectedNameFilter();
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

//  void QQuickLabsPlatformFileDialog::fileModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog15fileModeChangedEv(
    QQuickLabsPlatformFileDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fileModeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fileModeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFileDialog::fileChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog11fileChangedEv(
    QQuickLabsPlatformFileDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fileChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fileChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFileDialog::filesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog12filesChangedEv(
    QQuickLabsPlatformFileDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "filesChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "filesChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFileDialog::currentFileChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog18currentFileChangedEv(
    QQuickLabsPlatformFileDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "currentFileChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "currentFileChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFileDialog::currentFilesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog19currentFilesChangedEv(
    QQuickLabsPlatformFileDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "currentFilesChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "currentFilesChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFileDialog::folderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog13folderChangedEv(
    QQuickLabsPlatformFileDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "folderChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "folderChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFileDialog::optionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog14optionsChangedEv(
    QQuickLabsPlatformFileDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "optionsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "optionsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFileDialog::nameFiltersChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog18nameFiltersChangedEv(
    QQuickLabsPlatformFileDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "nameFiltersChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "nameFiltersChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFileDialog::defaultSuffixChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog20defaultSuffixChangedEv(
    QQuickLabsPlatformFileDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "defaultSuffixChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "defaultSuffixChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFileDialog::acceptLabelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog18acceptLabelChangedEv(
    QQuickLabsPlatformFileDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "acceptLabelChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "acceptLabelChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformFileDialog::rejectLabelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickLabsPlatformFileDialog18rejectLabelChangedEv(
    QQuickLabsPlatformFileDialog *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformFileDialog")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "rejectLabelChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "rejectLabelChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

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
//  QUrl QQuickLabsPlatformFileDialog::addDefaultSuffix(const QUrl &file)
//      const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK28QQuickLabsPlatformFileDialog16addDefaultSuffixERK4QUrl(
    const QQuickLabsPlatformFileDialog *self,
    const QUrl *file) {
  return new QUrl(self->addDefaultSuffix(*file));
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  QList<QUrl> QQuickLabsPlatformFileDialog::addDefaultSuffixes(const
//      QList<QUrl> &files) const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK28QQuickLabsPlatformFileDialog18addDefaultSuffixesERK5QListI4QUrlE(
    const QQuickLabsPlatformFileDialog *self,
    const QList<QUrl> *files) {
  return new QList<QUrl>(self->addDefaultSuffixes(*files));
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  bool QQuickLabsPlatformFileDialog::useNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK28QQuickLabsPlatformFileDialog15useNativeDialogEv(
    const QQuickLabsPlatformFileDialog *self) {
  return static_cast<const OwnQQuickLabsPlatformFileDialog *>(self)->OwnQQuickLabsPlatformFileDialog::useNativeDialog();
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformFileDialog::onShow(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuickLabsPlatformFileDialog6onShowEP21QPlatformDialogHelper(
    QQuickLabsPlatformFileDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickLabsPlatformFileDialog *>(self)->OwnQQuickLabsPlatformFileDialog::onShow(
      dialog);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#if QT_DEPRECATED_SINCE(6, 9)
//  void QQuickLabsPlatformFileDialog::onHide(QPlatformDialogHelper *dialog)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuickLabsPlatformFileDialog6onHideEP21QPlatformDialogHelper(
    QQuickLabsPlatformFileDialog *self,
    QPlatformDialogHelper *dialog) {
  static_cast<OwnQQuickLabsPlatformFileDialog *>(self)->OwnQQuickLabsPlatformFileDialog::onHide(
      dialog);
}
#endif  // QT_DEPRECATED_SINCE(6, 9)

#endif  // QT_DEPRECATED_SINCE(6, 9)

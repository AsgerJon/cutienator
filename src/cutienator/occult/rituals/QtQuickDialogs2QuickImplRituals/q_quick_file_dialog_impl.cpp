//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p
//  .h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qlist.h>
#include <QtCore/QSharedPointer>

//  const QMetaObject *QQuickFileDialogImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickFileDialogImpl10metaObjectEv(
    const QQuickFileDialogImpl *self) {
  return self->metaObject();
}

//  void *QQuickFileDialogImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickFileDialogImpl11qt_metacastEPKc(
    QQuickFileDialogImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFileDialogImpl::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickFileDialogImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFileDialogImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFileDialogImpl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickFileDialogImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFileDialogImpl::tr(s, c, n));
}

//  void QQuickFileDialogImpl::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl21qt_qmlMarker_attachedEv(
    QQuickFileDialogImpl *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickFileDialogImpl::QQuickFileDialogImpl(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickFileDialogImpl *ritual_ZN20QQuickFileDialogImplC1EP7QObject(
    QObject *parent) {
  return new QQuickFileDialogImpl(parent);
}

//  QQuickFileDialogImplAttached
//      *QQuickFileDialogImpl::qmlAttachedProperties(QObject *object)
extern "C" Q_DECL_EXPORT
QQuickFileDialogImplAttached *ritual_ZN20QQuickFileDialogImpl21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickFileDialogImpl::qmlAttachedProperties(object);
}

//  QUrl QQuickFileDialogImpl::currentFolder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QQuickFileDialogImpl13currentFolderEv(
    const QQuickFileDialogImpl *self) {
  return new QUrl(self->currentFolder());
}

//  void QQuickFileDialogImpl::setCurrentFolder(const QUrl &currentFolder,
//      SetReason setReason)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl16setCurrentFolderERK4QUrlNS_9SetReasonE(
    QQuickFileDialogImpl *self,
    const QUrl *currentFolder,
    QQuickFileDialogImpl::SetReason setReason) {
  self->setCurrentFolder(*currentFolder, setReason);
}

//  QUrl QQuickFileDialogImpl::selectedFile() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QQuickFileDialogImpl12selectedFileEv(
    const QQuickFileDialogImpl *self) {
  return new QUrl(self->selectedFile());
}

//  void QQuickFileDialogImpl::setSelectedFile(const QUrl &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl15setSelectedFileERK4QUrl(
    QQuickFileDialogImpl *self,
    const QUrl *file) {
  self->setSelectedFile(*file);
}

//  void QQuickFileDialogImpl::setInitialCurrentFolderAndSelectedFile(const
//      QUrl &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl38setInitialCurrentFolderAndSelectedFileERK4QUrl(
    QQuickFileDialogImpl *self,
    const QUrl *file) {
  self->setInitialCurrentFolderAndSelectedFile(*file);
}

//  QSharedPointer<QFileDialogOptions> QQuickFileDialogImpl::options() const
extern "C" Q_DECL_EXPORT
QSharedPointer<QFileDialogOptions> *ritual_ZNK20QQuickFileDialogImpl7optionsEv(
    const QQuickFileDialogImpl *self) {
  return new QSharedPointer<QFileDialogOptions>(self->options());
}

//  void QQuickFileDialogImpl::setOptions(const
//      QSharedPointer<QFileDialogOptions> &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl10setOptionsERK14QSharedPointerI18QFileDialogOptionsE(
    QQuickFileDialogImpl *self,
    const QSharedPointer<QFileDialogOptions> *options) {
  self->setOptions(*options);
}

//  QStringList QQuickFileDialogImpl::nameFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK20QQuickFileDialogImpl11nameFiltersEv(
    const QQuickFileDialogImpl *self) {
  return new QList<QString>(self->nameFilters());
}

//  void QQuickFileDialogImpl::resetNameFilters()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl16resetNameFiltersEv(
    QQuickFileDialogImpl *self) {
  self->resetNameFilters();
}

//  QQuickFileNameFilter *QQuickFileDialogImpl::selectedNameFilter() const
extern "C" Q_DECL_EXPORT
QQuickFileNameFilter *ritual_ZNK20QQuickFileDialogImpl18selectedNameFilterEv(
    const QQuickFileDialogImpl *self) {
  return self->selectedNameFilter();
}

//  void QQuickFileDialogImpl::setAcceptLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl14setAcceptLabelERK7QString(
    QQuickFileDialogImpl *self,
    const QString *label) {
  self->setAcceptLabel(*label);
}

//  void QQuickFileDialogImpl::setRejectLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl14setRejectLabelERK7QString(
    QQuickFileDialogImpl *self,
    const QString *label) {
  self->setRejectLabel(*label);
}

//  QString QQuickFileDialogImpl::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQuickFileDialogImpl8fileNameEv(
    const QQuickFileDialogImpl *self) {
  return new QString(self->fileName());
}

//  void QQuickFileDialogImpl::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl11setFileNameERK7QString(
    QQuickFileDialogImpl *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  QString QQuickFileDialogImpl::currentFolderName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQuickFileDialogImpl17currentFolderNameEv(
    const QQuickFileDialogImpl *self) {
  return new QString(self->currentFolderName());
}

//  void QQuickFileDialogImpl::selectNameFilter(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl16selectNameFilterERK7QString(
    QQuickFileDialogImpl *self,
    const QString *filter) {
  self->selectNameFilter(*filter);
}

//  void QQuickFileDialogImpl::currentFolderChanged(const QUrl &folderUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl20currentFolderChangedERK4QUrl(
    QQuickFileDialogImpl *self,
    const QUrl *folderUrl) {
  self->currentFolderChanged(*folderUrl);
}

//  void QQuickFileDialogImpl::selectedFileChanged(const QUrl
//      &selectedFileUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl19selectedFileChangedERK4QUrl(
    QQuickFileDialogImpl *self,
    const QUrl *selectedFileUrl) {
  self->selectedFileChanged(*selectedFileUrl);
}

//  void QQuickFileDialogImpl::nameFiltersChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl18nameFiltersChangedEv(
    QQuickFileDialogImpl *self) {
  self->nameFiltersChanged();
}

//  void QQuickFileDialogImpl::fileSelected(const QUrl &fileUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl12fileSelectedERK4QUrl(
    QQuickFileDialogImpl *self,
    const QUrl *fileUrl) {
  self->fileSelected(*fileUrl);
}

//  void QQuickFileDialogImpl::filterSelected(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl14filterSelectedERK7QString(
    QQuickFileDialogImpl *self,
    const QString *filter) {
  self->filterSelected(*filter);
}

//  void QQuickFileDialogImpl::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl17componentCompleteEv(
    QQuickFileDialogImpl *self) {
  self->componentComplete();
}

//  void QQuickFileDialogImpl::itemChange(QQuickItem::ItemChange change,
//      const QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickFileDialogImpl10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickFileDialogImpl *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->itemChange(change, *data);
}

//  QQuickFileDialogImplPrivate *QQuickFileDialogImpl::d_func()
extern "C" Q_DECL_EXPORT
QQuickFileDialogImplPrivate *ritual_ZN20QQuickFileDialogImpl6d_funcEv(
    QQuickFileDialogImpl *self) {
  return self->d_func();
}

//  const QQuickFileDialogImplPrivate *QQuickFileDialogImpl::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFileDialogImplPrivate *ritual_ZNK20QQuickFileDialogImpl6d_funcEv(
    const QQuickFileDialogImpl *self) {
  return self->d_func();
}

//  void QQuickFileDialogImpl::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickFileDialogImpl17componentCompleteEv(
    QQuickFileDialogImpl *self) {
  self->QQuickFileDialogImpl::componentComplete();
}

//  void QQuickFileDialogImpl::itemChange(QQuickItem::ItemChange change,
//      const QQuickItem::ItemChangeData &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickFileDialogImpl10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickFileDialogImpl *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *data) {
  self->QQuickFileDialogImpl::itemChange(change, *data);
}

//  a QSharedPointer<QFileDialogOptions> a ritual of QQuickFileDialogImpl
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickFileDialogImpl__QSharedPointer_QFileDialogOptions(
    QSharedPointer<QFileDialogOptions> *self) {
  delete self;
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
